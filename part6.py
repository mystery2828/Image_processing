import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)
def call_back(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (255,23,33), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255,255,255), 1)
        cv2.imshow('image', img)



img = np.zeros((512,512,3), np.uint8)
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', call_back)

cv2.waitKey(0)
cv2.destroyAllWindows()