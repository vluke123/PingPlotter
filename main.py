import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as mpath
import matplotlib.dates as mdates
import matplotlib as mpl
import matplotlib.animation as animation
from datetime import datetime
from pythonping import ping

# Comments out the standard toolbar for Matplotlib
mpl.rcParams["toolbar"] = "None"
mpl.style.use('seaborn')  # Sets the matplotlib style as 'Seaborn'

tagret = "192.168.0.1"
average_response_list = []
time_vals = []
_count = 0
players = []


class PingData:
    """Initiates a ping request.\n
    Once a PingData object has been created a method tracks how many times the ping
    function has been called.
    """
    _count = 0

    def __init__(self) -> None:
        pass

    def _counter(self, count):
        self._count += 1
        return self._count

    def ping_once(self):
        response = ping(tagret, count=1, interval=0.25)
        self._counter(self._count)
        print(response)
        return [response.rtt_max_ms, response.packet_loss]


# Initiates the PingData object and creates the matplotlib figure/axes
p = PingData()
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_title('Ping returns (ms)')


def animate(i):
    """Gets the current time and logs the result in time_vals variable.\n
    Calls the ping_once function and logs the response in average_response_list variable.\n
    Then plots the x,y values onto the figure.
    """
    dt = datetime.now()
    global _count, players
    ping_return = p.ping_once() 
    if ping_return[1] == 1:
        average_response_list.append(average_response_list[-1])
        time_vals.append(dt)
        x_point = mdates.date2num(dt)
        ax1.plot(time_vals, average_response_list, 'green')
        ax1.add_patch(patches.Rectangle((x_point,average_response_list[-1]),width=0.00000765,height=2, color='red'))
        _count += 1
        average_ms = round((sum(average_response_list)/_count),2)
        print(f'Average ping is: {average_ms}ms')
    else:    
        average_response_list.append(ping_return[0]) # Gets the 0th list of return from ping_once
        time_vals.append(dt)
        ax1.plot(time_vals, average_response_list, 'green')
        _count += 1
        average_ms = round((sum(average_response_list)/_count),2)
        print(f'Average ping is: {average_ms}ms')


# Repeats the animate function every 100 ms.
ani = animation.FuncAnimation(fig, animate, interval=100)

plt.tight_layout()
plt.show()
