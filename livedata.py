import random
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation as animation
from itertools import count

x = []
y = []
index = count()


def animate(i):
    x.append(next(index))
    y.append(random.randint(0, 100))
    plt.cla()
    plt.plot(x, y)


ani = animation(plt.gcf(), animate, interval=1000)
plt.xlabel = 'x'
plt.xlabel = 'y'
plt.tight_layout()
plt.show()
