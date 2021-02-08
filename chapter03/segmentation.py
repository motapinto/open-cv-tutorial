import cv2
import numpy as np

def get_contours(img, img_contours):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
        x, y, w, h = cv2.boundingRect(approx)
        cv2.drawContours(img_contours, cnt, -1, (64, 24, 31), 4)
        cv2.rectangle(img_contours, (x, y), (x + w, y + h), (12, 145, 198), 2)

img = cv2.imread('resources/shapes.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,7), 1)
img_canny = cv2.Canny(img_blur, 50, 50)

img_contours = img.copy()
get_contours(img_canny, img_contours)

cv2.imshow('img', img)
cv2.imshow('img_canny', img_canny)
cv2.imshow('img_contours', img_contours)

cv2.waitKey(0)
cv2.destroyAllWindows()
