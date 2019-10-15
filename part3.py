import cv2

img = cv2.imread('lena.jpg',1)
#draw a line
img = cv2.line(img, (0,0), (500,500), (200,122,223), 5)
#draw a arrow line
img = cv2.arrowedLine(img, (200,0), (500,500), (255,0,0), 5)
#draw a rectangle
img = cv2.rectangle(img, (250,424),(439,549), (255,233,45), -1)


cv2.imshow('image', img)

k = cv2.waitKey(0) & 0xFF
if k ==27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
cv2.destroyAllWindows()