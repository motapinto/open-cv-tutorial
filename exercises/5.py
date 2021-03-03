import cv2
from matplotlib import pyplot as plt

img = cv2.imread('resources/noisy_image.png')
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
plt.subplots_adjust(left = 0.125, bottom = 0.1, right = 0.9 , top = 1 , wspace=None, hspace=None)

averaging = cv2.blur(img, (5, 5))
ax1.imshow(averaging)
ax1.set_xlabel('averaging')

gaussian_filtering = cv2.GaussianBlur(img, (5, 5), 0)
ax2.imshow(gaussian_filtering)
ax2.set_xlabel('gaussian_filtering')

median_filtering = cv2.medianBlur(img, 5)
ax3.imshow(median_filtering)
ax3.set_xlabel('median_filtering')

bilateral_filtering = cv2.bilateralFilter(img, 9, 75, 75)
ax4.imshow(bilateral_filtering)
ax4.set_xlabel('bilateral_filtering')

plt.show()
