import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('resources/frontal_face_cascade.xml')
img = cv2.imread('resources/person.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, x + h), (224, 201, 155), 5)

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
