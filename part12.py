import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.png', cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

sobel = cv2.bitwise_or(sobelx, sobely)
gauss = cv2.adaptiveThreshold(sobel, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 10)
titles = ['images','lap', 'sox','soy','sob', 'gauss']

images = [img, lap, sobelx, sobely, sobel, gauss]

for i in range(6):
    plt.subplot(3, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()