import cv2

webcam = cv2.VideoCapture(0)

while webcam.isOpened():
    success,img = webcam.read()

    cv2.imshow("Webcam",img)
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break