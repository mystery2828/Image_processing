import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')


ball = img[288:336, 337:392]
img[281:329, 111:166] = ball


img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))

#dstn = cv2.add(img,img2)
dstn = cv2.addWeighted(img,.5,img2,.6,0)
cv2.imshow('image', dstn)


cv2.waitKey(0)
cv2.destroyAllWindows()