import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png',-0)
# _,th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# _,th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
# _,th3 = cv.threshold(img, 20, 255, cv.THRESH_TRUNC)
th4 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 19, 8)
while(True):
    cv.imshow('image1', th4)
    cv.imshow('image2', img)
    # cv.imshow('image3', th3)
    k = cv.waitKey(0)
    if k == 27:
        break

cv.destroyAllWindows()