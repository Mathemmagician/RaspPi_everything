import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from math import sin, cos, radians
from matplotlib.animation import FuncAnimation

from gyroscope import Gyroscope


def Rx(alpha):
    return np.matrix([[1, 0, 0], [0, cos(alpha), sin(alpha)], [0, -sin(alpha), cos(alpha)]])

def Ry(betta):
    return np.matrix([[cos(betta), 0, -sin(betta)], [0, 1, 0], [sin(betta), 0, cos(betta)]])

def rotateXY(arr, alpha, betta):
    rx = Rx(alpha)
    ry = Ry(betta)

    return np.matmul(np.matmul(arr, rx), ry)

def plotPoints(i):
    x, y, z = g.get_xyz_rotation()
    arr = rotateXY(np.array(Points), radians(x), radians(y))
    Xs = arr[:, 0]
    Ys = arr[:, 1]
    Zs = arr[:, 2]

    plt.cla()
    plt.scatter([Xs], [Ys], c=[Zs], cmap="magma", marker='s', 
            norm=mpl.colors.Normalize(vmin=-maxx, vmax=maxx) ,s=6)
    d = 2 * maxx 
    plt.xlim([-d, d])
    plt.ylim([-d, d])


# Here we define a set of points with xyz coordinates forming an arrow shape
# We then will gather rotation info from gyroscope and apply Rx, Ry rotations 
# using matrix multiplication magic

g = Gyroscope()

Points = []
width, length = 5, 10
lw_ratio = length // width
maxx = max(width, length)

for i in range(-width, width+1):
    for j in range(-length, length):
        if (j > length -  lw_ratio * abs(i)) or (abs(i) >= width//2 and (j < 0)):
            continue
        Points.append([i, j, 0])


if __name__ == '__main__':
    ani = FuncAnimation(plt.gcf(), plotPoints, interval=200)
    plt.tight_layout()
    plt.show()
