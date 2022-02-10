import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from datetime import datetime
from matplotlib.animation import FuncAnimation 
from pythonping import ping

tagret = "8.8.8.8"
average_response_list = []


class PingData:
    _count = 0

    def __init__(self) -> None:
        pass

    def _counter(self, count):
        self._count += 1
        return self._count

    def ping_loop(self):
        response = ping(tagret, count=1, interval=0.25)
        #print(f"{average_response_list}")
        average_response_list.append(response.rtt_min_ms)
        try:
            average_ms = round(sum(average_response_list) / self._count, ndigits=2)
        except ZeroDivisionError:
            average_ms = round(sum(average_response_list) / 1, ndigits=2)
        self._counter(self._count)
        # print(f"{response.rtt_min_ms} ms\naverage ms = {average_ms}ms")
        # print(f"max ms = {max(average_response_list)}ms")
        # print(f"min ms = {min(average_response_list)}ms")

x_vals = []

p = PingData()
while True:
    p.ping_loop()

    def animate(i):
        x_vals.append(datetime.now)

        plt.plot(x_vals, average_response_list)

    ani = FuncAnimation(plt.gcf(), animate, interval=250)

    plt.tight_layout()
    plt.show()

