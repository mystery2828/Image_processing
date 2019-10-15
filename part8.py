import numpy as np
import cv2 as cv

img = np.zeros((300,512, 3), np.uint8)
cv.namedWindow('image')
def change(x):
    print(x)

cv.createTrackbar('B', 'image', 0, 255, change)
cv.createTrackbar('G', 'image', 0, 255, change)
cv.createTrackbar('R', 'image', 0, 255, change)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    b = cv.getTrackbarPos('B','image')
    g = cv.getTrackbarPos('G','image')
    r = cv.getTrackbarPos('R','image')
    img[:] = [b,g,r]
    cv.imshow('image', img)
cv.destroyAllWindows()