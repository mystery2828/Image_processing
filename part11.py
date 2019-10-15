import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('chethan.jpeg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25

dst = cv.filter2D(img, -1, kernel)

gblur = cv.GaussianBlur(img, (5, 5), 0)

blur = cv.blur(img, (5, 5))
images = [img, dst, blur, gblur]
title = ["image",
         'dst']
         #'blur',
         #'gblur']

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()