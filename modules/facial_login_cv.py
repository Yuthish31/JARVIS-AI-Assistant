# modules/facial_login_cv.py
import cv2
import os

def facial_login(known_faces_dir='known_faces'):
    orb = cv2.ORB_create()
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Load known face image
    known_image_path = os.path.join(known_faces_dir, 'yourname.jpg')
    known_image = cv2.imread(known_image_path, 0)
    if known_image is None:
        print("No known image found!")
        return False

    kp1, des1 = orb.detectAndCompute(known_image, None)

    cap = cv2.VideoCapture(0)
    print("Scanning face... Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kp2, des2 = orb.detectAndCompute(gray, None)

        if des2 is not None and len(des2) >= 10:
            matches = bf.match(des1, des2)
            matches = sorted(matches, key=lambda x: x.distance)
            good_matches = [m for m in matches if m.distance < 60]

            cv2.putText(frame, f"Matches: {len(good_matches)}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            if len(good_matches) > 30:
                print("Face matched!")
                cap.release()
                cv2.destroyAllWindows()
                return True

        cv2.imshow("Login Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return False