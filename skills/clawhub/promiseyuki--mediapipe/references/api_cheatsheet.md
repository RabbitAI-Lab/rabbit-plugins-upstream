# MediaPipe API Cheatsheet

MediaPipe has two generations of Python API. Both are covered by
`scripts/run_mediapipe.py`, but you can also call them directly.

## 1. Legacy solutions API (`mp.solutions`) — models bundled

```python
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

image = cv2.imread("input.jpg")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)   # MediaPipe expects RGB

with mp_hands.Hands(static_image_mode=True, max_num_hands=2,
                    min_detection_confidence=0.5) as hands:
    results = hands.process(rgb)

if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

cv2.imwrite("output.jpg", image)   # draw on the BGR frame, not the RGB copy
```

For video/webcam: `static_image_mode=False` (tracks across frames) and process
one frame at a time.

| Solution | Constructor key args | Result fields | Landmarks |
|---|---|---|---|
| FaceMesh | `max_num_faces`, `refine_landmarks` | `multi_face_landmarks` | 468 (478 w/ iris) |
| Hands | `max_num_hands` | `multi_hand_landmarks`, `multi_handedness` | 21 |
| Pose | `model_complexity` (0–2) | `pose_landmarks` | 33 |
| Holistic | `model_complexity` (0–2) | `face_landmarks`, `pose_landmarks`, `left_hand_landmarks`, `right_hand_landmarks` | 468+33+21+21 |

Landmark attributes: `x`, `y`, `z` (normalized); pose/holistic also expose
`visibility` and `presence`.

## 2. Tasks API (`mp.tasks.vision`) — Google's recommended API

Requires a model file (`.task` or `.tflite`), see download URLs below.

```python
import mediapipe as mp
from mediapipe.tasks import BaseOptions
from mediapipe.tasks.python import vision

options = vision.HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="hand_landmarker.task"),
    running_mode=vision.VisionRunningMode.IMAGE,
    num_hands=2,
    min_hand_detection_confidence=0.5,
)
with vision.HandLandmarker.create_from_options(options) as landmarker:
    mp_image = mp.Image.create_from_file("input.jpg")
    result = landmarker.detect(mp_image)

# result.hand_landmarks: list of 21 normalized landmarks per detected hand
```

For video: `running_mode=VisionRunningMode.VIDEO` and call
`landmarker.detect_for_video(mp_image, timestamp_ms)` with **strictly
increasing** `timestamp_ms`.

| Task | Options class | Key result fields |
|---|---|---|
| hand_landmarker | `HandLandmarkerOptions` | `hand_landmarks`, `hand_world_landmarks`, `handedness` |
| pose_landmarker | `PoseLandmarkerOptions` | `pose_landmarks`, `pose_world_landmarks` |
| face_landmarker | `FaceLandmarkerOptions` | `face_landmarks`, `face_blendshapes` (blendshapes model only) |
| face_detector | `FaceDetectorOptions` | `detections` (`bounding_box` + `categories`) |
| object_detector | `ObjectDetectorOptions` | `detections` (`bounding_box` + `categories`) |
| image_segmenter | `ImageSegmenterOptions` | `category_mask`, `confidence_masks` |

### Drawing Tasks API landmarks

Tasks results are plain Python lists, so rebuild a protobuf before drawing:

```python
from mediapipe.framework.formats import landmark_pb2
mp_drawing = mp.solutions.drawing_utils

for hand_landmarks in result.hand_landmarks:
    proto = landmark_pb2.NormalizedLandmarkList()
    proto.landmark.extend(
        landmark_pb2.NormalizedLandmark(x=lm.x, y=lm.y, z=lm.z)
        for lm in hand_landmarks
    )
    mp_drawing.draw_landmarks(image_bgr, proto, mp.solutions.hands.HAND_CONNECTIONS)
```

## Model download URLs (Tasks API)

```bash
curl -L -o hand_landmarker.task \
  https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task
```

| Task | File | URL |
|---|---|---|
| Hand landmarker | `hand_landmarker.task` | https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task |
| Pose landmarker (lite) | `pose_landmarker_lite.task` | https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/1/pose_landmarker_lite.task |
| Pose landmarker (full) | `pose_landmarker_full.task` | https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_full/float16/1/pose_landmarker_full.task |
| Face landmarker | `face_landmarker.task` | https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task |
| Face detector | `blaze_face_short_range.tflite` | https://storage.googleapis.com/mediapipe-models/face_detector/blaze_face_short_range/float16/1/blaze_face_short_range.tflite |
| Object detector | `efficientdet_lite0.tflite` | https://storage.googleapis.com/mediapipe-models/object_detector/efficientdet_lite0/float16/1/efficientdet_lite0.tflite |
| Selfie segmenter | `selfie_segmenter.tflite` | https://storage.googleapis.com/mediapipe-models/image_segmenter/selfie_segmenter/float16/1/selfie_segmenter.tflite |

## Common mistakes

- Forgetting BGR → RGB conversion before `process()` / `detect()`.
- Reusing the RGB array for drawing after `process()` (its `writeable` flag
  was flipped to False).
- `static_image_mode=True` for videos (loses tracking, slower).
- Non-increasing `timestamp_ms` in VIDEO mode → RuntimeError.
- Wrong model file for a task → "model not found" or OOM errors.
