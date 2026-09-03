# ✋ MediaPipe Vision Skill | MediaPipe 视觉技能

A [ClawHub](https://clawhub.com) / OpenClaw skill for **on-device computer
vision** with Google MediaPipe — face, hand, and pose landmark detection, face
detection, object detection, and image segmentation on images, videos, and
webcam streams.

一个基于 Google MediaPipe 的**端侧计算机视觉** ClawHub / OpenClaw 技能——支持
人脸/手势/姿态关键点检测、人脸检测、目标检测和图像分割，可处理图片、视频和摄像头画面。

## ✨ Features | 特性

- 🖐️ **Hand tracking** — 21-point landmarks, gesture-ready | 手势追踪：21 点关键点
- 🧍 **Pose estimation** — 33-point body landmarks | 人体姿态估计：33 点身体关键点
- 🧑 **Face mesh** — 468/478-point face mesh (with iris) | 人脸网格：468/478 点（含虹膜）
- 📦 **Object detection** — 80 COCO classes (EfficientDet-Lite0) | 目标检测：80 类 COCO
- 🖼️ **Selfie segmentation** — background removal | 自拍分割：背景移除
- 📊 **Structured output** — annotated images/videos, JSON, and landmark CSV | 结构化输出：标注图/视频、JSON、关键点 CSV
- 📹 **Multiple inputs** — image, video, or live webcam | 多输入：图片、视频或实时摄像头
- 🔀 **Two APIs** — legacy solutions API (bundled models) and Tasks API (recommended) | 两代 API：传统 solutions API（内置模型）与 Tasks API（官方推荐）

## 📦 Installation | 安装

```bash
pip install -r scripts/requirements.txt
```

Requires Python 3.9–3.12. | 需要 Python 3.9–3.12。

## 🚀 Quick start | 快速开始

```bash
# Hand landmarks from an image | 图片手势关键点检测
python scripts/run_mediapipe.py landmarks --type hand --input hand.jpg --output out.jpg

# Pose landmarks from a video + CSV | 视频姿态检测 + CSV 导出
python scripts/run_mediapipe.py landmarks --type pose --input pose.mp4 --output out.mp4 --landmark-csv pose.csv

# Object detection (Tasks API, download a model first) | 目标检测（Tasks API，先下载模型）
python scripts/run_mediapipe.py tasks --type object_detector --model efficientdet_lite0.tflite --input scene.jpg --output det.jpg

# Selfie segmentation | 自拍分割
python scripts/run_mediapipe.py tasks --type image_segmenter --model selfie_segmenter.tflite --input me.jpg --output cutout.png
```

For the Tasks API you need model files first — download URLs are listed in
`references/api_cheatsheet.md`.
Tasks API 需要先下载模型文件——下载地址见 `references/api_cheatsheet.md`。

## 📁 Directory structure | 目录结构

```
mediapipe/
├── SKILL.md                     # Skill definition for ClawHub | 技能定义
├── LICENSE                      # MIT license | MIT 许可证
├── scripts/
│   ├── run_mediapipe.py         # Unified CLI (legacy + Tasks APIs) | 统一命令行
│   └── requirements.txt         # Python dependencies | Python 依赖
└── references/
    ├── landmarks.md             # Landmark index tables | 关键点索引表
    └── api_cheatsheet.md        # API patterns + model URLs | API 模式 + 模型地址
```

## 📚 References | 参考

- MediaPipe solutions: <https://ai.google.dev/edge/mediapipe/solutions>
- This skill's full docs live in [`SKILL.md`](SKILL.md) (bilingual).

## 📄 License | 许可证

[MIT](LICENSE)
