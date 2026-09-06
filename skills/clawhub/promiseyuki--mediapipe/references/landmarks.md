# MediaPipe Landmark Index Reference

All landmark coordinates from MediaPipe are **normalized** (0–1) to the input
image size. `x`/`y` are pixel-relative positions; `z` is depth (roughly
proportional to the landmark's distance from the camera plane). For pose and
holistic, each landmark also carries `visibility` and `presence` (0–1).

## Hand landmarks (21)

| Index | Name | Description |
|---:|---|---|
| 0 | WRIST | Wrist |
| 1 | THUMB_CMC | Thumb carpometacarpal joint |
| 2 | THUMB_MCP | Thumb metacarpophalangeal joint |
| 3 | THUMB_IP | Thumb interphalangeal joint |
| 4 | THUMB_TIP | Thumb tip |
| 5 | INDEX_FINGER_MCP | Index MCP |
| 6 | INDEX_FINGER_PIP | Index PIP |
| 7 | INDEX_FINGER_DIP | Index DIP |
| 8 | INDEX_FINGER_TIP | Index tip |
| 9 | MIDDLE_FINGER_MCP | Middle MCP |
| 10 | MIDDLE_FINGER_PIP | Middle PIP |
| 11 | MIDDLE_FINGER_DIP | Middle DIP |
| 12 | MIDDLE_FINGER_TIP | Middle tip |
| 13 | RING_FINGER_MCP | Ring MCP |
| 14 | RING_FINGER_PIP | Ring PIP |
| 15 | RING_FINGER_DIP | Ring DIP |
| 16 | RING_FINGER_TIP | Ring tip |
| 17 | PINKY_MCP | Pinky MCP |
| 18 | PINKY_PIP | Pinky PIP |
| 19 | PINKY_DIP | Pinky DIP |
| 20 | PINKY_TIP | Pinky tip |

Useful finger-extension checks (tip vs PIP): thumb `4 > 2`, index `8 > 6`,
middle `12 > 10`, ring `16 > 14`, pinky `20 > 18` (for upright hands).

## Pose landmarks (33)

| Index | Name | Index | Name |
|---:|---|---:|---|
| 0 | nose | 17 | left_pinky |
| 1 | left_eye_inner | 18 | right_pinky |
| 2 | left_eye | 19 | left_index |
| 3 | left_eye_outer | 20 | right_index |
| 4 | right_eye_inner | 21 | left_thumb |
| 5 | right_eye | 22 | right_thumb |
| 6 | right_eye_outer | 23 | left_hip |
| 7 | left_ear | 24 | right_hip |
| 8 | right_ear | 25 | left_knee |
| 9 | mouth_left | 26 | right_knee |
| 10 | mouth_right | 27 | left_ankle |
| 11 | left_shoulder | 28 | right_ankle |
| 12 | right_shoulder | 29 | left_heel |
| 13 | left_elbow | 30 | right_heel |
| 14 | right_elbow | 31 | left_foot_index |
| 15 | left_wrist | 32 | right_foot_index |
| 16 | right_wrist |  |  |

Common landmarks for upright posture estimation: shoulder mid-point =
`(11 + 12) / 2`, hip mid-point = `(23 + 24) / 2`, spine vector = hip-mid →
shoulder-mid.

## Face mesh (468, or 478 with `refine_landmarks=True`)

Key facial regions (indices are always valid in the 468/478 set):

| Region | Key landmark indices |
|---|---|
| Left eye | 33, 133, 159, 145, 160, 158, 144, 153, 154, 155 |
| Right eye | 362, 263, 387, 373, 380, 374, 386, 384, 385, 398 |
| Left iris (478 only) | 468, 469, 470, 471 |
| Right iris (478 only) | 472, 473, 474, 475 |
| Nose | 1, 2, 4, 5, 6, 98, 168, 195, 197, 327 |
| Outer lips | 61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291, 409, 270, 269, 267, 0, 37, 39, 40, 185 |
| Inner lips | 78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95 |
| Face oval | 10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288, 397, 365, 379, 378, 400, 377, 152, 148, 176, 149, 150, 136, 172, 58, 132, 93, 234, 127, 162, 21, 54, 103, 67, 109 |

Blink detection: compute the eye-aspect-ratio from the eye landmarks
(`(p2 − p6) + (p3 − p5)) / (2 × |p1 − p4|)`) — a low EAR over several frames
means a blink.

## Connections (for drawing)

- Hand: `mp.solutions.hands.HAND_CONNECTIONS`
- Pose: `mp.solutions.pose.POSE_CONNECTIONS`
- Face: `mp.solutions.face_mesh.FACEMESH_CONTOURS`, `FACEMESH_TESSELATION`,
  `FACEMESH_LIPS`, `FACEMESH_LEFT_EYE`, `FACEMESH_RIGHT_EYE`
- Holistic: combines the pose, face, and both-hand connection sets.
