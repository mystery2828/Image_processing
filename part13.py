import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('messi5.jpg')
canny = cv.Canny(img, 100, 200)
images = [img, canny]
title = ["image",
         'canny']

for i in range(2):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()