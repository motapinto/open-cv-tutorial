import cv2

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture("resources/video.mp4")

while True:
    success, img = cap.read()
    if not success: break
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("output_video", img)
    if cv2.waitKey(1) == 27: break  

cap.release()
cv2.destroyAllWindows()
   