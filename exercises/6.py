import cv2
from matplotlib import pyplot as plt

img = cv2.imread('resources/cards.jpeg')
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

img_canny = cv2.Canny(img, 100, 100)
ax1.imshow(img_canny)
ax1.set_xlabel('img_canny')

img_sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
ax2.imshow(img_sobel_x)
ax2.set_xlabel('img_sobel_x')

img_sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
ax3.imshow(img_sobel_y)
ax3.set_xlabel('img_sobel_y')

img_laplacian = cv2.Laplacian(img,cv2.CV_64F)
ax4.imshow(img_laplacian)
ax4.set_xlabel('img_laplacian')

plt.show()
