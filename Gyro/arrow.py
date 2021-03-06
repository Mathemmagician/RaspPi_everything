import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from math import sin, cos
from matplotlib.animation import FuncAnimation

Points = []
width, length = 10, 20
lw_ratio = length // width
maxx = max(width, length)

for i in range(-width, width+1):
    for j in range(-length, length):
        if (j > length -  lw_ratio * i) or (j > length + lw_ratio * i) or (((i >= width // 2) or (i <= -width//2)) and j < 0):
            continue
        Points.append([i, j, 0])


def Rx(alpha):
    return np.matrix([[1, 0, 0], [0, cos(alpha), sin(alpha)], [0, -sin(alpha), cos(alpha)]])

def Ry(betta):
    return np.matrix([[cos(betta), 0, -sin(betta)], [0, 1, 0], [sin(betta), 0, cos(betta)]])

def rotateXY(arr, alpha, betta):
    rx = Rx(alpha)
    ry = Ry(betta)

    return np.matmul(np.matmul(arr, rx), ry)


xd = 0
def plotPoints(i):
    global xd
    arr = rotateXY(np.array(Points), xd, xd)
    xd += 0.1
    Xs = arr[:, 0]
    Ys = arr[:, 1]
    Zs = arr[:, 2]

    plt.cla()
    plt.scatter([Xs], [Ys], c=[Zs], cmap="cool", marker='s',
            norm=mpl.colors.Normalize(vmin=-maxx, vmax=maxx) ,s=6)
    d = 50
    plt.xlim([-d, d])
    plt.ylim([-d, d])


if __name__ == '__main__':
    ani = FuncAnimation(plt.gcf(), plotPoints, interval=200)
    plt.tight_layout()
    plt.show()
