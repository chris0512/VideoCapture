import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    frame = cv2.resize(frame, (640, 480))

    frame = cv2.flip(frame, 1)

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(0) == ord('q'):
        break