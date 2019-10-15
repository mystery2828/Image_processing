

import numpy as np
import cv2 as cv

def change(x):
    print(x)


cap = cv.VideoCapture(0)
cv.namedWindow('tracking')
cv.createTrackbar('LH','tracking',0,255,change)
cv.createTrackbar('LS','tracking',0,255,change)
cv.createTrackbar('LV','tracking',0,255,change)
cv.createTrackbar('UH','tracking',255,255,change)
cv.createTrackbar('US','tracking',255,255,change)
cv.createTrackbar('UV','tracking',255,255,change)


# cv.createTrackbar('B', 'image', 0, 255, change)
# cv.createTrackbar('G', 'image', 0, 255, change)
# cv.createTrackbar('R', 'image', 0, 255, change)

while(1):
    image = cv.imread('smarties.png')
    _, image = cap.read()
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    l_h = cv.getTrackbarPos('LH','tracking')
    u_h = cv.getTrackbarPos('UH','tracking')
    l_s = cv.getTrackbarPos('LS','tracking')
    u_s = cv.getTrackbarPos('US','tracking')
    l_v = cv.getTrackbarPos('LV','tracking')
    u_v = cv.getTrackbarPos('UV','tracking')
    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])

    #provide a mask for a colour using lower bound and upper bound
    mask = cv.inRange(hsv, l_b,u_b)

    res = cv.bitwise_and(image,image, mask=mask)

    cv.imshow('image',image)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()