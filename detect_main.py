import cv2
import mediapipe as mp
from distance import *
from  detect_gesture import *

def detect_main():
    # Argument parsing #################################################################
    args = get_args()

    cap_device = args.device
    cap_width = args.width
    cap_height = args.height

    use_static_image_mode = args.use_static_image_mode
    min_detection_confidence = args.min_detection_confidence
    min_tracking_confidence = args.min_tracking_confidence

    use_brect = True

    # Camera preparation ###############################################################
    cap = cv.VideoCapture(cap_device)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)

    # Model load #############################################################
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=use_static_image_mode,
        max_num_hands=2,
        min_detection_confidence=min_detection_confidence,
        min_tracking_confidence=min_tracking_confidence,
    )

    keypoint_classifier = KeyPointClassifier()
    point_history_classifier = PointHistoryClassifier()

    # Read labels ###########################################################
    with open('model/keypoint_classifier/keypoint_classifier_label.csv',
              encoding='utf-8-sig') as f:
        keypoint_classifier_labels = csv.reader(f)
        keypoint_classifier_labels = [
            row[0] for row in keypoint_classifier_labels
        ]
    with open(
            'model/point_history_classifier/point_history_classifier_label.csv',
            encoding='utf-8-sig') as f:
        point_history_classifier_labels = csv.reader(f)
        point_history_classifier_labels = [
            row[0] for row in point_history_classifier_labels
        ]

    # FPS Measurement ########################################################
    cvFpsCalc = CvFpsCalc(buffer_len=10)

    # Coordinate history #################################################################
    history_length = 16
    point_history = deque(maxlen=history_length)

    # Finger gesture history ################################################
    finger_gesture_history = deque(maxlen=history_length)

    # load img and video ############################################################
    dark = cv2.imread("data/dark_v2.jpg", cv2.IMREAD_COLOR)
    lighten = cv2.imread("data/lighten.jpg", cv2.IMREAD_COLOR)

    light_rotate = cv2.VideoCapture("data/rotate.mp4")
    len_light_video = int(light_rotate.get(cv2.CAP_PROP_FRAME_COUNT))
    light_video_list = []
    for i in range(len_light_video):
        ret, frame = light_rotate.read()
        if not ret:
            print("error when loading lightening video")
        light_video_list.append(frame)
    tears = cv2.VideoCapture("data/blue_tears_v2.mp4")
    len_tear_video = int(tears.get(cv2.CAP_PROP_FRAME_COUNT))
    tears_video_list = []
    for i in range(len_tear_video):
        ret, frame = tears.read()
        if not ret:
            print("error when loading tears video")
        tears_video_list.append(frame)
    
    cv2.namedWindow('blue tears picture', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('blue tears picture', 1024, 813)
    cv2.imshow("blue tears picture", dark)
    light = False
    rotate = False
    restrict = False
    idx = 0
    index = 0
    cnt = 30
    count_2min = 200
    Distance = 200
    crop_i, crop_j = 3402, 2702
    
    # distance measurement #####################
    ref_image = cv2.imread("data/test.jpg")

    ref_image_face_width = face_data(ref_image)
    focal_length_found = focal_length(KNOWN_DISTANCE, FACE_WIDTH, ref_image_face_width)
    print(focal_length_found)
    
    #  ########################################################################
    mode = 0

    while True:
        fps = cvFpsCalc.get()

        # Process Key (ESC: end) #################################################
        key = cv.waitKey(10)
        if key == 27:  # ESC
            break
        number, mode = select_mode(key, mode)

        # Camera capture #####################################################
        ret, image = cap.read()
        if not ret:
            break
        image = cv.flip(image, 1)  # Mirror display
        debug_image = copy.deepcopy(image)

        # Detection implementation #############################################################
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True

        #  ####################################################################
        if results.multi_hand_landmarks is not None:
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks,
                                                  results.multi_handedness):
                # Bounding box calculation
                brect = calc_bounding_rect(debug_image, hand_landmarks)
                # Landmark calculation
                landmark_list = calc_landmark_list(debug_image, hand_landmarks)

                # Conversion to relative coordinates / normalized coordinates
                pre_processed_landmark_list = pre_process_landmark(
                    landmark_list)
                pre_processed_point_history_list = pre_process_point_history(
                    debug_image, point_history)
                # Write to the dataset file
                logging_csv(number, mode, pre_processed_landmark_list,
                            pre_processed_point_history_list)

                # Hand sign classification
                hand_sign_id = keypoint_classifier(pre_processed_landmark_list)
                if hand_sign_id == 2:  # Point gesture
                    point_history.append(landmark_list[8])
                else:
                    point_history.append([0, 0])

                if hand_sign_id == 0 and (not light) and (not restrict):
                    # turn on the light
                    light = True
                    rotate = True
                    
                    cv2.imshow("blue tears picture", lighten)
                elif hand_sign_id == 1 and (not restrict):
                    # trun off the light
                    light = False
                    rotate = False
                    
                    cv2.imshow("blue tears picture", dark)
                elif hand_sign_id == 4 or hand_sign_id == 5:
                    # blue tears appear
                    rotate = False
                    light = False
                    restrict = True
                    
                    cv2.imshow("blue tears picture", dark)

                # Finger gesture classification
                finger_gesture_id = 0
                point_history_len = len(pre_processed_point_history_list)
                if point_history_len == (history_length * 2):
                    finger_gesture_id = point_history_classifier(
                        pre_processed_point_history_list)

                # Calculates the gesture IDs in the latest detection
                finger_gesture_history.append(finger_gesture_id)
                most_common_fg_id = Counter(
                    finger_gesture_history).most_common()

                # Drawing part
                debug_image = draw_bounding_rect(use_brect, debug_image, brect)
                debug_image = draw_landmarks(debug_image, landmark_list)
                debug_image = draw_info_text(
                    debug_image,
                    brect,
                    handedness,
                    keypoint_classifier_labels[hand_sign_id],
                    point_history_classifier_labels[most_common_fg_id[0][0]],
                )
        else:
            point_history.append([0, 0])

        #debug_image = draw_point_history(debug_image, point_history)
        debug_image = draw_info(debug_image, fps, mode, number)

        face_width_in_frame = face_data(debug_image)
        if face_width_in_frame != 0:
            Distance = distance_finder(focal_length_found, FACE_WIDTH, face_width_in_frame)
            # Drwaing Text on the screen
            cv2.putText(debug_image, f"Distance = {round(Distance, 2)} CM", (300, 30), fonts, 0.6, (BLACK), 2, cv2.LINE_AA)
        # Screen reflection #############################################################
        cv.imshow('Hand Gesture Recognition', debug_image)

        # show video/img
        if cnt > 0 and restrict:
            cv2.putText(debug_image, f"Downcount: {cnt}", (300, 50), fonts, 1.5, (RED), 2, cv2.LINE_AA)
            cnt -= 1
            
        if light and rotate and (not restrict):
            # light rotating
            cv2.imshow('blue tears picture', light_video_list[idx])
            cv2.waitKey(10)
            if (idx < len_light_video-1):
                idx += 1
            else:
                idx = 0
        if cnt == 0 and restrict:
            cv2.putText(debug_image, f"Disapper: : {count_2min}", (300, 70), fonts, 0.5, (GREEN), 2, cv2.LINE_AA)
            count_2min -= 1
            if count_2min == 0:
                cnt = 30
                restrict = False
                light = False
                count_2min = 200
                cv2.imshow("blue tears picture", dark)
            else:
                if Distance < 50:   # zoom in (1122, 891)
                    pts1, pts2 = zoomin(1122, 891, crop_i, crop_j)
                    M = cv2.getPerspectiveTransform(pts1, pts2)
                    dst = cv2.warpPerspective(tears_video_list[index], M, (1024, 813))
                    cv2.imshow('blue tears picture', dst)
                    cv2.waitKey(10)
                    if (index < len_tear_video-1):
                        index += 1
                    else:
                        index = 0
                    # 972=3402-243*10; 772=2702-193*10 (3402:2702=243:193)
                    if crop_i > 972 and crop_j > 772:
                        crop_i -= 243
                        crop_j -= 193
                elif Distance >= 50:    # zoom out
                    pts1, pts2 = zoomin(1122, 891, crop_i, crop_j)
                    M = cv2.getPerspectiveTransform(pts1, pts2)
                    dst = cv2.warpPerspective(tears_video_list[index], M, (1024, 813))
                    cv2.imshow('blue tears picture', dst)
                    cv2.waitKey(10)
                    if (index < len_tear_video-1):
                        index += 1
                    else:
                        index = 0

                    if crop_i < 3402 and crop_j < 2702:
                        crop_i += 243
                        crop_j += 193

    cap.release()
    cv.destroyAllWindows()
