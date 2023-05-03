#!/usr/bin/env python3
import matplotlib
###changing the backend for faster time###
matplotlib.use('agg')
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

delta = 0.025
x = np.arange(0., 3.0, delta)
y = np.arange(0., 3.0, delta)
X, Y = np.meshgrid(x, y)
Z = X * Y

fig, ax = plt.subplots()
###reducing contour levels###
CS = ax.contour(X, Y, Z, 10, colors='k')
# ax.clabel(CS, inline=1, fontsize=10)

ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)

plt.show()
