# modules/emotion_detector.py
from fer import FER
import cv2

def detect_emotion():
    detector = FER()
    cap = cv2.VideoCapture(0)
    print("Detecting emotion...")

    while True:
        ret, frame = cap.read()
        emotion = detector.top_emotion(frame)
        if emotion:
            print("Emotion:", emotion)
        cv2.imshow("Emotion Detector", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()