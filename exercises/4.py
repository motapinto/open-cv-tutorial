import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

def read_image(path):
    img = cv2.imread(path)
    if img is not None: return img
    print('Cannot read image') 
    exit(0)

def plot_histogram(img, axis):
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])

    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max()/ cdf.max()

    axis.plot(cdf_normalized, color = 'b')
    axis.hist(img.flatten(), 256, [0, 256], color = 'r')
    axis.legend(('cdf','histogram'), loc = 'upper left')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        img = read_image(sys.argv[1])
        if img is None:
            print('Cannot read image')
            exit(0)

        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

        # Original image and histogram
        fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
        ax1.imshow(img)
        plot_histogram(img, ax2)

        # Histogram equalization
        img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
        img_equalized = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        ax3.imshow(img_equalized)
        plot_histogram(img_yuv, ax4)

        # CLAHE (Contrast Limited Adaptive Histogram Equalization)
        clahe = cv2.createCLAHE().apply(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
        ax5.imshow(cv2.cvtColor(clahe, cv2.COLOR_BGR2RGB))
        plot_histogram(clahe, ax6)

        plt.xlim([0, 256])
        plt.show()
    else:
        print('Usage: python exercises/4.py <path of image with with low contrast>')
