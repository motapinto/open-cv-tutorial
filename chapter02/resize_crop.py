import cv2

img = cv2.imread('resources/person.png')
img_resize = cv2.resize(img, (300, 200))
img_cropped = img[0:200, 200:500]

cv2.imshow('img', img)
cv2.imshow('img_resize', img_resize)
cv2.imshow('img_cropped', img_cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()