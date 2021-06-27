import cv2
import time

cap = cv2.VideoCapture(0)


last_time = time.time()
while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    frame = cv2.flip(frame, 1)

    text = "FPS: " + str(int(1/(time.time() - last_time)))
    last_time = time.time()
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(0) == ord('q'):
        break