from PIL import Image
import numpy as np
from scipy.spatial import distance

w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
k = 0
point1 = (256, 250, 0)
color1 = (242, 7, 50)
point2 = (256, 260, 0)
color2 = (7, 3, 140)

for i in range(w):
    for j in range(h):
        dist1 = distance.euclidean(point1, (i, j, 0))
        dist2 = distance.euclidean(point2, (i, j, 0))
        denom = dist1 + dist2
        data[i, j] = tuple(color1[k] * dist1/denom + color2[k] * dist2/denom for k in range(0,3))

img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()
