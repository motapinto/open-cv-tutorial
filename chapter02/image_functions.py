import cv2
import numpy as np

img = cv2.imread('resources/person.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
img_canny = cv2.Canny(img, 100, 100)

kernel = np.ones((5, 5), np.uint8)
img_dialation = cv2.dilate(img_canny, kernel, iterations=1)
img_eroded = cv2.erode(img_dialation, kernel, iterations=1)

images = np.concatenate((img_gray, img_blur, img_canny, img_dialation, img_eroded), axis=1)
cv2.imshow('images', images)
cv2.waitKey(0)
cv2.destroyAllWindows()
