import cv2
import sys
import os

def show_image(img, window_name = None):
    if img is not None:
        if window_name is None: window_name = 'webcam'
        cv2.imshow(window_name, img)

def save_frame(frame, frame_num):
    os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/../resources') 
    cv2.imwrite('frame{}.bmp'.format(frame_num), frame)

def read_webcam(width, height):
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)
    cap.set(10,150)

    i = 0
    while True:
        success, frame = cap.read()
        if not success: break
        show_image(frame, 'frame')

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        show_image(frame_gray, 'frame_gray')

        frame_binary = cv2.threshold(frame_gray, 128, 255, cv2.THRESH_BINARY)[1]
        show_image(frame_binary, 'frame_binary')

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
