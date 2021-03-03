import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

def show_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    plt.imshow(img)
    plt.show()

def create_images():
    img_1 = np.zeros((100, 200, 1), np.uint8)
    img_1.fill(100)
    cv2.line(img_1,(0, 0),(200, 100),(255), 5)
    cv2.line(img_1,(0, 100),(200, 0),(255),5)

    img_2 = np.zeros((50, 200, 3), np.uint8)
    img_2.fill(100)
    cv2.line(img_2,(0, 0),(200, 100),(255), 5)
    cv2.line(img_2,(0, 100),(200, 0),(255),5)

    show_image(img_1)
    show_image(img_2)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        create_images()
        image = cv2.imread(sys.argv[1])
        if image is not None:
            create_images()
        else:
            print('Cannot read image')
    else:
        print('Usage: python exercises/2.py <path of image>')
