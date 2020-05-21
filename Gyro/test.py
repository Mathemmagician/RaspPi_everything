import matplotlib
matplotlib.use('tkagg')

import matplotlib.pyplot as plt
from itertools import count
import random
from matplotlib.animation import FuncAnimation

from gyroscope import Gyroscope

g = Gyroscope()

x_vals = []
y_vals = []

#index = count()

def animate(i):
    #x_vals.append(next(index))
    #y_vals.append(random.randint(0,5))

    x, y = g.xy_rotation()
    x_vals.append(x)
    y_vals.append(y)

    plt.cla()
    plt.xlabel('X [degrees]')
    plt.ylabel('Y [degrees]')
    plt.xlim([-90, 90])
    plt.ylim([-90, 90])
    plt.scatter(x_vals, y_vals)


ani = FuncAnimation(plt.gcf(), animate) #, interval=1000)

plt.tight_layout()
plt.show()
