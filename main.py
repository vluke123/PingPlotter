import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.dates as mdates
import matplotlib as mpl
import matplotlib.animation as animation
from datetime import datetime
from pythonping import ping

# Comments out the standard toolbar for mpl
mpl.rcParams["toolbar"] = "None"
mpl.style.use("seaborn")  # Sets the mpl style as 'Seaborn'

tagret = "8.8.8.8"
average_response_list = []
time_vals = []
_count = 0


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


# Initiates the PingData object and creates the mpl figure/axes
p = PingData()
fig = plt.figure(figsize=(12, 10))
subfigs = fig.subfigures(1, 2, width_ratios=[5, 1])

# Initiates the first subplot for plotting ping returns
ax1 = subfigs[0].add_subplot()
ax1.set_title("PingPlotter Ripoff")
ax1.set_ylabel("Latency (ms)")
ax1.set_xlabel("Time")

# Initiates the second subplot to just have data in text format
ax2 = subfigs[1].add_subplot()
ax2_avg_txt = ax2.text(0.05, 0.9, "Avg ping is 0 ms", transform=ax2.transAxes)
ax2_min_txt = ax2.text(0.05, 0.8, "Max ping is 0 ms", transform=ax2.transAxes)
ax2_max_txt = ax2.text(0.05, 0.7, "Min ping is 0 ms", transform=ax2.transAxes)
ax2.set_axis_off()
ax2_avg_txt.set_animated(True)  # Enables the 3 Artists as intended for animation
ax2_min_txt.set_animated(True)
ax2_max_txt.set_animated(True)
plt.subplots_adjust(left=0.855, right=1)  # Adjust figure due to cutting off issue


def animate(i):
    """Gets the current time and logs the result in time_vals variable.\n
    Calls the ping_once function and logs the response in average_response_list variable.\n
    Then plots the x,y values onto the figure.
    """
    dt = datetime.now()
    global _count, players, ax2_avg_txt, ax2_max_txt, ax2_min_txt
    ping_return = p.ping_once()
    if ping_return[1] == 1:  # IF packet loss occurs
        average_response_list.append(
            average_response_list[-1]
        )  # Gets last variable so graph looks normal
        time_vals.append(dt)
        x_point = mdates.date2num(dt)
        ax1.plot(time_vals, average_response_list, "green")
        ax1.add_artist(
            plt.Rectangle((x_point, 0), width=0.00000765, height=2000, color="red")
        )
        _count += 1
        average_ms = round((sum(average_response_list) / _count), 2)
        mpl.artist.Artist.remove(ax2_avg_txt)  # Remove old text to paste new one in
        mpl.artist.Artist.remove(ax2_min_txt)
        mpl.artist.Artist.remove(ax2_max_txt)
        ax2_avg_txt = ax2.text(
            0.05, 0.9, f"Avg ping is {average_ms}ms", transform=ax2.transAxes
        )
        ax2_max_txt = ax2.text(
            0.05,
            0.8,
            f"Max ping is {max(average_response_list)}ms",
            transform=ax2.transAxes,
        )
        ax2_min_txt = ax2.text(
            0.05,
            0.7,
            f"Min ping is {min(average_response_list)}ms",
            transform=ax2.transAxes,
        )

    else:
        average_response_list.append(
            ping_return[0]
        )  # Gets the first return from ping_once (this is the latency)
        time_vals.append(dt)
        ax1.plot(time_vals, average_response_list, "green")
        _count += 1
        average_ms = round((sum(average_response_list) / _count), 2)

        mpl.artist.Artist.remove(ax2_avg_txt)  # Remove old text to paste new one in
        mpl.artist.Artist.remove(ax2_min_txt)
        mpl.artist.Artist.remove(ax2_max_txt)

        ax2_avg_txt = ax2.text(
            -0.1,
            0.9,
            f"Avg ping is {average_ms}ms",
            transform=ax2.transAxes,
            fontsize="large",
            fontweight="semibold",
        )

        ax2_max_txt = ax2.text(
            -0.1,
            0.8,
            f"Max ping is {max(average_response_list)}ms",
            transform=ax2.transAxes,
            fontsize="large",
            fontweight="semibold",
        )

        ax2_min_txt = ax2.text(
            -0.1,
            0.7,
            f"Min ping is {min(average_response_list)}ms",
            transform=ax2.transAxes,
            fontsize="large",
            fontweight="semibold",
        )


# Repeats the animate function every 100 ms.
ani = animation.FuncAnimation(fig, animate, interval=100)

plt.tight_layout()
plt.show()
