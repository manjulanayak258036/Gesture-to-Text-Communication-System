from pathlib import Path

import cv2
from mediapipe import Image, ImageFormat
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

MODEL_PATH = Path(__file__).with_name("hand_landmarker.task")
HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (5, 6), (6, 7), (7, 8),
    (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20),
    (0, 5), (5, 9), (9, 13), (13, 17), (0, 17),
    (5, 17),
]

base_options = python.BaseOptions(model_asset_path=str(MODEL_PATH))
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO,
    num_hands=1,
    min_hand_detection_confidence=0.6,
    min_hand_presence_confidence=0.6,
    min_tracking_confidence=0.6,
)
landmarker = vision.HandLandmarker.create_from_options(options)


def draw_landmarks(frame, landmarks):
    if not landmarks:
        return

    height, width, _ = frame.shape
    points = [
        (int(landmark.x * width), int(landmark.y * height))
        for landmark in landmarks[0]
    ]

    for start, end in HAND_CONNECTIONS:
        if 0 <= start < len(points) and 0 <= end < len(points):
            cv2.line(frame, points[start], points[end], (0, 255, 0), 2)

    for point in points:
        cv2.circle(frame, point, 4, (0, 0, 255), -1)


cap = cv2.VideoCapture(0)
print("M1 running - Press ESC to exit")
frame_index = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Camera not accessible")
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = Image(image_format=ImageFormat.SRGB, data=rgb)
    timestamp_ms = frame_index * 33
    results = landmarker.detect_for_video(mp_image, timestamp_ms)

    if results.hand_landmarks:
        print("Hand detected")
        draw_landmarks(frame, results.hand_landmarks)

    frame_index += 1
    cv2.imshow("M1 – Hand Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
