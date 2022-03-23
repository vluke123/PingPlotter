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

    def ping_loop(self):
        response = ping(tagret, count=1, interval=0.25)
        # print(f"{average_response_list}")
        average_response_list.append(response.rtt_min_ms)
        try:
            average_ms = round(sum(average_response_list) / self._count, ndigits=2)
        except ZeroDivisionError:
            average_ms = round(sum(average_response_list) / 1, ndigits=2)
        self._counter(self._count)
        # print(f"{response.rtt_min_ms} ms\naverage ms = {average_ms}ms")
        # print(f"max ms = {max(average_response_list)}ms")
        # print(f"min ms = {min(average_response_list)}ms")


p = PingData()
while True:
    p.ping_loop()
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_title('Ping returns (ms)')

    def animate(i):
        dt = datetime.now()
        time_vals.append(dt)
        ax1.plot(time_vals, average_response_list, 'green')

    ani = animation.FuncAnimation(fig, animate, interval=250)

    plt.tight_layout()
    plt.show()

'''
def animate(i):
    dt = datetime.now()
    time_vals.append(dt)
    r1 = random.randint(1,100)
    average_response_list.append(r1)
    ax1.plot(time_vals, average_response_list, 'green')

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
'''