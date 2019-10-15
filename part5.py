import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)
def call_back(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strxy = str(x) + ',' + str(y)
        cv2.putText(img, strxy, (x,y), font, 1, (255,0,0), 1)
        cv2.imshow('imgage', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        blue = img[x ,y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        strbgr = str(blue) + ',' + str(green)+ ','+ str(red)
        cv2.putText(img, strbgr, (x, y), font, 1, (255, 255, 255), 1)
        cv2.imshow('imgage', img)



img = cv2.imread('fruits.jpg', 1)
cv2.imshow('image', img)

cv2.setMouseCallback('image', call_back)

cv2.waitKey(0)
cv2.destroyAllWindows()