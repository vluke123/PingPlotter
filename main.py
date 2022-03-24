import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib as mpl
import matplotlib.animation as animation
from datetime import datetime
from pythonping import ping

mpl.rcParams["toolbar"] = "None"  # Comments out the standard toolbar for Matplotlib
mpl.style.use('seaborn') # Sets the matplotlib style as 'Seaborn'

tagret = "8.8.8.8"
average_response_list = []
time_vals = []


class PingData:
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



p = PingData()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_title('Ping returns (ms)')

def animate(i):
    dt = datetime.now()
    ping_return = p.ping_once()
    average_response_list.append(ping_return)
    time_vals.append(dt)
    ax1.plot(time_vals, average_response_list, 'green')

ani = animation.FuncAnimation(fig, animate, interval=250)

plt.tight_layout()
plt.show()
