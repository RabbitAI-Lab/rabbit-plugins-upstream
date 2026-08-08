---
name: geoskill-object-detection-yolo
description: '滑窗+HOG/阈值特征+NMS+地理编码，输出检测框GeoJSON（离线numpy等价实现）'
---

# 遥感目标检测 | Remote Sensing Object Detection

Automatically detects targets of interest in remote sensing imagery (bright/high-contrast features such as buildings, vehicles, and ships), and outputs detection-box GeoJSON with WGS-84 geographic coordinates plus a score raster.

This skill is an **offline numpy-equivalent implementation** of deep object detectors such as YOLO: without relying on torch/ultralytics, it fully reproduces the detection pipeline of "candidate generation → redundancy suppression → geographic output" via sliding-window scanning + objectness scoring (local brightness z-score or HOG gradient energy) + non-maximum suppression (NMS) + pixel-box geocoding, and every step can be verified by unit tests independently.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy scikit-learn geopandas shapely
```

## Usage / 使用方法

### Example 1 (synthetic data, offline)

```bash
python geoskill-object-detection-yolo.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2: real imagery + HOG features

```bash
python geoskill-object-detection-yolo.py --input scene.tif --feature hog --score-thresh 2.0 --output-dir ./out
```

### Example 3: adjust window/step/NMS thresholds

```bash
python geoskill-object-detection-yolo.py --bbox 121.4 31.1 121.6 31.3 --synthetic --win-size 12 --step 4 --iou-thresh 0.3 --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `detections.geojson` | GeoJSON | Detection-box polygons + score/pixel_box attributes |
| `score_map.tif` | GeoTIFF | Detection score raster (max within boxes) |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/exit code) |

## Data Source / 数据源 / Source

Local single/multi-band GeoTIFF (first band used as intensity), or `--synthetic` scene (dark background + bright square targets).

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is performed locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-object-detection-yolo
description: '滑窗+HOG/阈值特征+NMS+地理编码，输出检测框GeoJSON（离线numpy等价实现）'
---

# 遥感目标检测 | Remote Sensing Object Detection

在遥感影像上自动检测感兴趣目标（建筑、车辆、船只等明亮/高对比地物），输出带 WGS-84 地理坐标的检测框 GeoJSON 与得分栅格。

本 skill 是 YOLO 等深度目标检测器的**离线 numpy 等价实现**：不依赖 torch/ultralytics，用滑窗扫描 + 目标性打分（局部亮度 z-score 或 HOG 梯度能量）+ 非极大值抑制（NMS）+ 像素框地理编码，完整复现"候选生成 -> 冗余抑制 -> 地理输出"的检测流水线，每一步都可单独单元测试验证。

## 依赖

```bash
pip install numpy rasterio scipy scikit-learn geopandas shapely
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-object-detection-yolo.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2：真实影像 + HOG 特征

```bash
python geoskill-object-detection-yolo.py --input scene.tif --feature hog --score-thresh 2.0 --output-dir ./out
```

### 示例 3：调整窗口/步长/NMS 阈值

```bash
python geoskill-object-detection-yolo.py --bbox 121.4 31.1 121.6 31.3 --synthetic --win-size 12 --step 4 --iou-thresh 0.3 --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `detections.geojson` | GeoJSON | 检测框多边形 + score/pixel_box 属性 |
| `score_map.tif` | GeoTIFF | 检测得分栅格（框内最大值） |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/退出码） |

## 数据源 / Source

本地单/多波段 GeoTIFF（取首波段作强度），或 --synthetic 合成场景（暗背景 + 明亮方形目标）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
