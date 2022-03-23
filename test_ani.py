from random import random, randrange
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib as mpl
import matplotlib.animation as animation
from datetime import datetime 

mpl.rcParams["toolbar"] = "None"
mpl.style.use('seaborn')

time_vals = []
average_response_list = []
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_title

def animate(i):
    dt = datetime.now()
    time_vals.append(dt)
    r1 = random.randint(1,100)
    average_response_list.append(r1)
    ax1.plot(time_vals, average_response_list, 'green')

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()