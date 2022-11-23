import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break

        img.flags.writeable = False
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = face_detection.process(img)

        img.flags.writeable = True
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        if results.detections:
            #print(len(results.detections))
            for detection in results.detections:
                mp_drawing.draw_detection(img, detection)
                print("1: ", detection.location_data.relative_keypoints[0])
                print("2: ", detection.location_data.relative_keypoints[1])
                print("3: ", detection.location_data.relative_keypoints[2])
                print("4: ", detection.location_data.relative_keypoints[3])
                print("5: ", detection.location_data.relative_keypoints[4])
                print("6: ", detection.location_data.relative_keypoints[5])

        cv2.imshow('oxxostudio', img)
        if cv2.waitKey(1) == ord('q'):
            break    # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()