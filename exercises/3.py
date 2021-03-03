import cv2
import sys
import os
import numpy as np

def save_frame(frame, frame_num):
    os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/../resources') 
    cv2.imwrite('frame{}.bmp'.format(frame_num), frame)
    print('Stored frame {} in resources/'.format(frame_num))

def read_webcam(width, height):
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)
    cap.set(10,150)

    i = 0
    while True:
        success, frame = cap.read()
        if not success: break
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_binary = cv2.threshold(frame_gray, 128, 255, cv2.THRESH_BINARY)[1]
        
        # Object tracking
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # Bitwise-AND mask and original image
        tracking = cv2.bitwise_and(frame,frame, mask=mask)
        
        # reconverts images with 1 channel to 3 channels since hstack requires images with same shape
        frames = np.hstack((frame, cv2.cvtColor(frame_gray, cv2.COLOR_GRAY2BGR), cv2.cvtColor(frame_binary, cv2.COLOR_GRAY2BGR), tracking))
        cv2.imshow('frames', frames)

        i += 1
        if cv2.waitKey(1) != -1:
            save_frame(frame, i)
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    if len(sys.argv) == 3:
        read_webcam(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print('Usage: python exercises/3.py <width> <height>')
