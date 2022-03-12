import keyword
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from defuzzification import systemSimu
from memberFunction import x_humid_range, x_temp_range

def time(x, y):
    systemSimu.input['temp'] = y
    systemSimu.input['humid'] = x
    systemSimu.compute()
    return systemSimu.output['time']

fig_1 = plt.figure()
ax = Axes3D(fig_1, auto_add_to_figure=False)
fig_1.add_axes(ax)

X, Y = np.meshgrid(x_humid_range, x_temp_range)
ax.plot_surface(X, Y, time(X, Y), rstride=1,cstride=1,cmap=plt.cm.coolwarm)
ax.set_xlabel('Air moisture',color='r')
ax.set_ylabel('Air Temperature error',color='g')
ax.set_zlabel('Compressor Time',color='b')

plt.show()