import cv2
import os
import sys
import numpy as np
from PIL import Image  

def read_image(path):
    img = cv2.imread(path)
    if img is not None:
        return img
    else:
        print('Cannot read image')

def show_image(img):
    if img is not None:
        cv2.imshow('output_image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print('height: {} | width: {}'.format(img.shape[0], img.shape[1]))

def reformat_image(img, path, format):
    if img is not None:
        new_image = Image.open(path)
        new_path = '{}.{}'.format(os.path.splitext(path)[0], format)
        new_image.save(new_path)

def select_roi(img, path):
    roi = cv2.selectROI(img)
    roi_img = img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
    show_image(roi_img)
    reformat_image(roi_img, path, 'roi.bmp')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        img = read_image(sys.argv[1])
        show_image(img)
        reformat_image(img, sys.argv[1], 'bmp')
        select_roi(img, sys.argv[1])
    else:
        print('Usage: python exercises/1.py <path of image>')
