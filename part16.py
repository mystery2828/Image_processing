import cv2
import numpy as np
import pickle
from PIL import Image

face_cascade = cv2.CascadeClassifier('F:/image_pro/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
labels = {"Chethan": 1, "Akash": 0}
with open("labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in labels.items()}

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x,y,w,h) in faces:
        #print(x,y,w,h)

        roi_gray = gray[y:y+h, x:x+w]
        roi_colour = frame[y:y+h, x:x+w]

        id_, conf = recognizer.predict(roi_gray)
        if conf >= 45:
            print(id_)
            print(labels[id_])
            #frame = frame.resize((720,720), Image.ANTIALIAS)
            cv2.putText(frame, labels[id_], (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(40) == 27:
        break


cap.release()
cv2.destroyAllWindows()
