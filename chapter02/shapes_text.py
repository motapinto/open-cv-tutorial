import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
img[:] = 45, 144, 155
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (45, 65, 45), 3)
cv2.rectangle(img, (0,0), (img.shape[1], img.shape[0]), (242, 201, 155), 5)
cv2.circle(img, (400, 50), 30, (211, 211, 155), 8)
cv2.putText(img, 'OpenCV', (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (132, 155, 201), 2)
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()