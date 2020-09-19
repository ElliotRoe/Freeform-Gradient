from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

fig1 = plt.figure(1)
ax = plt.axes(projection='3d')

from PIL import Image

im = Image.open('TestPics/Freeform-Gradient-Test(bw4).png', 'r')
width, height = im.size
pixel_values = list(im.getdata())
pixel_values_reshape = np.array(pixel_values).flatten('C')

print(pixel_values_reshape[slice(0, len(pixel_values_reshape), 4)])

# Data for three-dimensional scattered points
zdata = pixel_values_reshape[slice(0, len(pixel_values_reshape), 4)]
xdata = np.array(list(range(255)) * 255)
ydata = np.array(list([i] * 255 for i in range(255))).flatten('C')
# ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greys_r');
x = xdata[slice(0, len(xdata), 80)]
y = ydata[slice(0, len(ydata), 80)]
z = zdata[slice(0, len(zdata), 80)]
ax.plot_trisurf(x, y, z,
                cmap='Greys_r', edgecolor='none');
ax.set_facecolor('xkcd:salmon')

plt.show()
