## Description:

Use Google MediaPipe for on-device computer vision: face, hand, and pose landmark detection, face detection, object detection, and image segmentation on images, videos, or webcam streams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[promiseyuki](https://clawhub.ai/user/promiseyuki)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to run local MediaPipe vision workflows for landmark extraction, object or face detection, segmentation, and annotated media generation from images, videos, or webcam streams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Webcam mode and saved media or structured outputs can capture faces, bodies, surroundings, and pose data.

Mitigation: Use webcam input and persistent output files only when the captured people and environment are appropriate to record and store.

Risk: Computer-vision dependencies can carry vulnerability or compatibility risk.

Mitigation: Install the skill in an isolated Python environment and update or pin opencv-python to a patched version.

Risk: The Tasks API requires externally downloaded model files before use.

Mitigation: Download model files from the documented MediaPipe model URLs and verify the local model path before running Tasks API commands.

## Reference(s):

- [MediaPipe solutions](https://ai.google.dev/edge/mediapipe/solutions)
- [ClawHub skill page](https://clawhub.ai/promiseyuki/skills/mediapipe)
- [MediaPipe API Cheatsheet](references/api_cheatsheet.md)
- [MediaPipe Landmark Index Reference](references/landmarks.md)
- [Hand landmarker model](https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task)
- [Pose landmarker lite model](https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/1/pose_landmarker_lite.task)
- [Pose landmarker full model](https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_full/float16/1/pose_landmarker_full.task)
- [Face landmarker model](https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task)
- [Face detector model](https://storage.googleapis.com/mediapipe-models/face_detector/blaze_face_short_range/float16/1/blaze_face_short_range.tflite)
- [Object detector model](https://storage.googleapis.com/mediapipe-models/object_detector/efficientdet_lite0/float16/1/efficientdet_lite0.tflite)
- [Selfie segmenter model](https://storage.googleapis.com/mediapipe-models/image_segmenter/selfie_segmenter/float16/1/selfie_segmenter.tflite)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, Python examples, and file output descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled CLI can create annotated image or video files, JSON frame results, landmark CSV files, and segmentation mask PNG files.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
