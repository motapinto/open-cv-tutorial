import cv2
import os
import sys
from PIL import Image
from matplotlib import pyplot as plt

def show_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    plt.imshow(img)
    plt.show()
    print('height: {} | width: {}'.format(img.shape[0], img.shape[1]))

def get_image_name(path, extension):
    return '{}.{}'.format(os.path.splitext(path)[0], extension)

def reformat_image(path, new_format):
    new_image = Image.open(path)
    new_path = get_image_name(path, new_format)
    new_image.save(new_path)

def select_roi(img, path):
    roi = cv2.selectROI(img)
    roi_img = img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
    show_image(roi_img)
    cv2.imwrite(get_image_name(path, 'roi.bmp'), roi_img)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        image = cv2.imread(sys.argv[1])
        if image is not None:
            show_image(image)
            reformat_image(sys.argv[1], 'bmp')
            select_roi(image, sys.argv[1])
        else:
            print('Cannot read image')
    else:
        print('Usage: python exercises/1.py <path of image>')
