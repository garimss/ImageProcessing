import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('/images/tower.jpg',cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.show()
