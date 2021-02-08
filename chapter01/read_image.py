import cv2

img = cv2.imread("resources/person.png")
cv2.imshow('output_image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()