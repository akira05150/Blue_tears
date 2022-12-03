import cv2
#import mediapipe as mp
import dlib

# distance from camera to object(face) measured
KNOWN_DISTANCE = 60  # centimeter
FACE_WIDTH = 14  # centimeter
# Colors
GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
fonts = cv2.FONT_HERSHEY_SIMPLEX

#mp_face_detection = mp.solutions.face_detection
#mp_drawing = mp.solutions.drawing_utils

detector = dlib.get_frontal_face_detector()

# focal length finder function
def focal_length(measured_distance, real_width, width_in_rf_image):
    focal_length_value = (width_in_rf_image * measured_distance) / real_width
    return focal_length_value

# distance estimation function
def distance_finder(focal_length, real_face_width, face_width_in_frame):
    distance = (real_face_width * focal_length) / face_width_in_frame
    return distance

# face detector function
def face_data(img):
    face_width = 0
    """
    size = img.shape
    w = size[1]
    h = size[0]
    with mp_face_detection.FaceDetection(             
    model_selection=0, min_detection_confidence=0.5) as face_detection:
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = face_detection.process(img2)
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(img, detection)
                # two sides of the face
                a = detection.location_data.relative_keypoints[4]
                b = detection.location_data.relative_keypoints[5]
                ax, ay = int(a.x * w), int(a.y * h)
                bx, by = int(b.x * w), int(b.y * h)
                face_width = math.sqrt((ax - bx)**2 + (ay - by)**2)
    """
    face_rects, scores, idx = detector.run(img, 0)
    for i, d in enumerate(face_rects):
        x1 = d.left()
        y1 = d.top()
        x2 = d.right()
        y2 = d.bottom()
        
        cv2.rectangle(img, (x1, y1), (x2, y2), (255,255, 255), 4,cv2.LINE_AA)
        face_width = abs(x1 - x2)
        
    return face_width
