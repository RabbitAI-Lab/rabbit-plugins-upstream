---
name: mediapipe
description: "Use Google MediaPipe for on-device computer vision — face, hand, and pose landmark detection, face detection, object detection, and image segmentation on images, videos, or webcam streams. Activate when the user asks to detect faces/hands/poses/objects, extract landmarks or keypoints, do background removal or selfie segmentation, or analyze photos/videos/webcam with MediaPipe. Provides scripts/run_mediapipe.py supporting both the legacy solutions API (bundled models) and the Tasks API (model file required), plus landmark index references. | 使用 Google MediaPipe 进行端侧计算机视觉：人脸/手势/姿态关键点检测、人脸检测、目标检测和图像分割，支持图片、视频和摄像头。当用户要求检测人脸/手/姿态/目标、提取关键点、背景移除（自拍分割）或使用 MediaPipe 处理图片/视频/摄像头时激活。提供 scripts/run_mediapipe.py，同时支持传统 solutions API（内置模型）与 Tasks API（需模型文件），并附带关键点索引参考。"
version: 1.0.0
license: MIT
homepage: https://ai.google.dev/edge/mediapipe/solutions
metadata:
  clawdbot:
    emoji: ✋
    requires:
      bins: [python3]
      packages: [mediapipe, opencv-python, numpy]
      env: []
---

# ✋ MediaPipe Vision Skill | MediaPipe 视觉技能

Google MediaPipe for on-device computer vision on images, videos, or webcam
streams: 468-point face mesh, 21-point hand landmarks, 33-point pose landmarks,
face detection, object detection, and image segmentation.

在图片、视频或摄像头画面上运行的端侧计算机视觉：468 点人脸网格、21 点手势关键点、33 点人体姿态关键点、人脸检测、目标检测与图像分割。

## When to use this skill | 何时使用本技能

Activate when the user wants to: | 当用户需要以下能力时激活：

- detect faces / extract face landmarks / face mesh (blinks, gaze, expressions) | 检测人脸 / 提取人脸关键点 / 人脸网格（眨眼、视线、表情）
- track hands and fingers (21 hand landmarks, gestures, finger counting) | 追踪手部与手指（21 点手势关键点、手势识别、手指计数）
- estimate human pose (33 body landmarks, exercise / sport / ergonomics analysis) | 人体姿态估计（33 点身体关键点、健身 / 运动 / 人体工学分析）
- detect objects in an image or video (80 COCO classes with EfficientDet-Lite0) | 图片或视频中的目标检测（EfficientDet-Lite0，80 类 COCO）
- remove backgrounds / selfie segmentation | 背景移除 / 自拍分割
- get landmark coordinates as structured data (JSON / CSV) for further analysis | 以结构化数据（JSON / CSV）导出关键点坐标用于后续分析
- process photos, videos, or live webcam input using MediaPipe | 使用 MediaPipe 处理照片、视频或实时摄像头画面

Do **not** use for: OCR / text recognition, depth estimation, model training,
or tasks that require a cloud GPU.

**不适用场景**：OCR / 文字识别、深度估计、模型训练，或需要云端 GPU 的任务。

## Environment setup | 环境准备

Requires Python 3.9–3.12 (check the mediapipe release notes for your platform).
需要 Python 3.9–3.12（具体请查阅 mediapipe 发布说明，不同平台支持不同）。

```bash
pip install -r scripts/requirements.txt
```

Install dependencies once per machine. `mediapipe` bundles the models for the
legacy solutions API; the Tasks API additionally needs `.task` / `.tflite`
model files (download URLs are in `references/api_cheatsheet.md`).

依赖每台机器只需安装一次。`mediapipe` 内置传统 solutions API 所需的模型；Tasks API 还需额外下载 `.task` / `.tflite` 模型文件（下载地址见 `references/api_cheatsheet.md`）。


## Quick start | 快速开始

All functionality is exposed through `scripts/run_mediapipe.py`
(run `python scripts/run_mediapipe.py --help` for the full reference).
所有功能都通过 `scripts/run_mediapipe.py` 提供（运行 `python scripts/run_mediapipe.py --help` 查看完整说明）。

### Legacy solutions API — models bundled, works offline | 传统 API——内置模型，离线可用

```bash
# Hand landmarks from an image, save the annotated result
# 从图片检测手势关键点并保存标注结果
python scripts/run_mediapipe.py landmarks --type hand --input hand.jpg --output out.jpg

# Pose landmarks from a video + a CSV dump of every landmark
# 视频姿态检测 + 导出关键点 CSV
python scripts/run_mediapipe.py landmarks --type pose --input pose.mp4 --output out.mp4 --landmark-csv pose.csv

# Face mesh | 人脸网格
python scripts/run_mediapipe.py landmarks --type face --input face.jpg --output face_mesh.jpg

# Everything at once: face + body + hands | 同时检测：人脸 + 身体 + 双手
python scripts/run_mediapipe.py landmarks --type holistic --input video.mp4 --output out.mp4

# Live webcam | 实时摄像头
python scripts/run_mediapipe.py landmarks --type pose --input webcam
```

### Tasks API — Google's recommended API, needs a model file | Tasks API——官方推荐，需模型文件

```bash
# Download a model first, e.g.: | 先下载模型，例如：
#   https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task

python scripts/run_mediapipe.py tasks --type hand_landmarker --model hand_landmarker.task --input hand.jpg --output out.jpg

python scripts/run_mediapipe.py tasks --type object_detector --model efficientdet_lite0.tflite --input scene.jpg --output det.jpg

python scripts/run_mediapipe.py tasks --type image_segmenter --model selfie_segmenter.tflite --input me.jpg --output cutout.png
```

## Command reference | 命令参考

### `landmarks` — legacy solutions API (bundled models) | 传统 solutions API（内置模型）

| Argument 参数 | Meaning 含义 |
|---|---|
| `--type` | `face` (face mesh) · `hand` (21 landmarks) · `pose` (33 landmarks) · `holistic` 人脸网格/手势/姿态/全身 |
| `--input` | image/video file path, or the literal `webcam` 图片/视频路径，或 `webcam` |
| `--output` | annotated output path (`.jpg`/`.png` images, `.mp4`/`.avi` video) 标注输出路径 |
| `--max-num` | max faces/hands/poses to track (default 2) 最多检测数量（默认 2） |
| `--min-confidence` | detection threshold, 0–1 (default 0.5) 检测置信度阈值（默认 0.5） |
| `--landmark-csv` | write per-landmark coordinates to CSV 将关键点坐标写入 CSV |
| `--json` | write structured per-frame results to JSON 将逐帧结构化结果写入 JSON |
| `--no-draw` | skip annotation drawing 跳过标注绘制 |

### `tasks` — Tasks API (model file required) | Tasks API（需模型文件）

| Argument 参数 | Meaning 含义 |
|---|---|
| `--type` | `hand_landmarker` · `pose_landmarker` · `face_landmarker` · `face_detector` · `object_detector` · `image_segmenter` |
| `--model` | path to the `.task`/`.tflite` model file 模型文件路径 |
| `--input` | image/video file path, or the literal `webcam` 图片/视频路径，或 `webcam` |
| `--output` | annotated output path; for `image_segmenter` a `_mask.png` is also written 标注输出路径；分割任务会额外生成 `_mask.png` |
| `--max-num` | max detections (default 2) 最多检测数量（默认 2） |
| `--min-confidence` | detection threshold, 0–1 (default 0.5) 检测置信度阈值（默认 0.5） |
| `--json` | write structured per-frame results to JSON 将逐帧结构化结果写入 JSON |
| `--no-draw` | skip annotation drawing 跳过标注绘制 |

## Outputs | 输出结果

- **Annotated image/video** — landmarks, boxes, or segmentation overlay via `--output`. 通过 `--output` 输出标注后的图片/视频（关键点、检测框或分割叠加）。
- **JSON** (`--json path.json`) — one object per frame: `{index, timestamp_ms, detections: [...]}`. Landmarks are normalized `{x, y, z}` coordinates; pose also includes `visibility` and `presence`. 每个帧一个对象；关键点为归一化 `{x, y, z}` 坐标，姿态还含 `visibility`、`presence`。
- **CSV** (`--landmark-csv path.csv`, landmark tasks only) — one row per landmark: `frame, kind, landmark_index, x, y, z, visibility, presence`. 每个关键点一行（仅关键点任务）。
- For `image_segmenter`, a raw category-mask PNG (`<output>_mask.png`) is written next to the annotated result. 分割任务会在标注结果旁额外生成原始类别掩码 PNG。

## References | 参考资料

| File 文件 | Contents 内容 |
|---|---|
| `references/landmarks.md` | Landmark index tables: hand (21), pose (33), face mesh (468/478) 关键点索引表：手势(21)/姿态(33)/人脸网格(468/478) |
| `references/api_cheatsheet.md` | Code patterns for both APIs + model download URLs 两代 API 代码模式 + 模型下载地址 |

## Important gotchas | 重要注意事项

- MediaPipe always expects **RGB** input; images are converted internally, but in your own code remember `cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)`. MediaPipe 始终期望 **RGB** 输入；脚本内部会自动转换，但自己写代码时记得 BGR→RGB 转换。
- Legacy solutions: pass `static_image_mode=True` for still images and `False` for video/webcam so MediaPipe tracks across frames. 传统 API：静态图片用 `static_image_mode=True`，视频/摄像头用 `False`（跨帧追踪）。
- Tasks API `detect_for_video` requires **strictly increasing** `timestamp_ms`. Tasks API 的 `detect_for_video` 需要**严格递增**的 `timestamp_ms`。
- Draw on the **BGR** frame after processing the RGB copy — never reuse the RGB array for drawing (its `writeable` flag is flipped). 处理完 RGB 副本后再在 **BGR** 原帧上绘制，切勿复用 RGB 数组（其 `writeable` 已被置 False）。
- Face mesh gives 468 landmarks, or 478 with `refine_landmarks=True` (iris). 人脸网格为 468 点，`refine_landmarks=True` 时为 478 点（含虹膜）。
- Landmark coordinates are **normalized** (0–1) to the image size. 关键点坐标为**归一化**值（0–1），相对图像尺寸。

## Limitations | 局限性

- MediaPipe runs on the CPU; very large images or long videos are slow. 在 CPU 上运行，超大图片或长视频较慢。
- The legacy solutions API is deprecated upstream — prefer the Tasks API for new work; the legacy path is kept because its models are bundled. 传统 solutions API 已被上游弃用——新项目优先用 Tasks API；本技能保留传统路径因其模型内置。
- Object detection covers the 80 COCO classes only (EfficientDet-Lite0). 目标检测仅覆盖 80 类 COCO（EfficientDet-Lite0）。
- Segmentation masks are per-frame; there is no temporal smoothing. 分割掩码逐帧独立，无时间平滑。

## Troubleshooting | 故障排查

| Problem 问题 | Fix 解决方法 |
|---|---|
| `No module named mediapipe` | `pip install -r scripts/requirements.txt` |
| MediaPipe import error on Windows | Use Python 3.9–3.12, upgrade pip, see mediapipe release notes 使用 Python 3.9–3.12，升级 pip，查看发布说明 |
| Tasks API errors | Confirm the model file exists and the path is correct 确认模型文件存在且路径正确 |
| No detections | Lower `--min-confidence`; improve lighting / face orientation 降低 `--min-confidence`；改善光照/人脸朝向 |
| Webcam not opening | Pass `0` instead of `webcam`, or check the camera index 传 `0` 代替 `webcam`，或检查摄像头索引 |
| VideoWriter codec errors | Re-encode the input to `.mp4` first, or write `.avi` output 先将输入重编码为 `.mp4`，或输出 `.avi` |

