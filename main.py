import numpy as np
import matplotlib.pyplot as plt
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


class PingData:
    """Initiates a ping request.
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
        return response.rtt_max_ms


# Initiates the PingData object and creates the matplotlib figure/axes
p = PingData()
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_title('Ping returns (ms)')


def animate(i):
    """Gets the current time and logs the result in time_vals variable.
    Calls the ping_once function and logs the response in average_response_list variable.
    Then plots the x,y values onto the figure.
    """
    dt = datetime.now()
    ping_return = p.ping_once()
    average_response_list.append(ping_return)
    time_vals.append(dt)
    ax1.plot(time_vals, average_response_list, 'green')


# Repeats the animate function every 250 ms.
ani = animation.FuncAnimation(fig, animate, interval=250)

plt.tight_layout()
plt.show()
