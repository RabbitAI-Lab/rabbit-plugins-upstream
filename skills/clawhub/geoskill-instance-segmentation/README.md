# Instance Segmentation (geoskill-instance-segmentation)

> Threshold segmentation + connected-component labeling + instance attribute extraction; outputs instance-annotated GeoJSON (offline numpy-equivalent implementation)

---

## 1. Overview

Segments every individual object in an image (buildings, parcels, tree crowns, ponds, etc.) into separate instances and extracts each instance's area, centroid, bounding box, and mean brightness, outputting instance-annotated GeoJSON and an instance label raster. This skill is an **offline numpy-equivalent implementation** of the Mask R-CNN instance segmentation network: it does not depend on deep learning frameworks and reproduces the instance segmentation pipeline via "threshold/Otsu foreground separation → scipy connected-component labeling (4/8-connectivity) → per-instance attribute extraction → geocoding". Connectivity differences, instance counts, and attribute computations are all validated by unit tests.

## 2. Features

Segments every individual object in an image (buildings, parcels, tree crowns, ponds, etc.) into separate instances and extracts each instance's area, centroid, bounding box, and mean brightness, outputting instance-annotated GeoJSON and an instance label raster. This skill is an **offline numpy-equivalent implementation** of the Mask R-CNN instance segmentation network: it does not depend on deep learning frameworks and reproduces the instance segmentation pipeline via "threshold/Otsu foreground separation → scipy connected-component labeling (4/8-connectivity) → per-instance attribute extraction → geocoding". Connectivity differences, instance counts, and attribute computations are all validated by unit tests.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-instance-segmentation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
```

## 4. CLI Parameters

Run `python <skill>.py --help` for the full list. Common parameters:

| Parameter | Type | Description |
|---|---|---|
| `--bbox` | `float[4]` | WGS84 bounding box `min_lon min_lat max_lon max_lat` |
| `--input` | `path` | Local input file (GeoJSON/GeoTIFF/etc.) |
| `--output-dir` | `path` | Output directory (default `./output`) |
| `--synthetic` | `flag` | Use synthetic data instead of real input |
| `--quiet` | `flag` | Suppress non-essential stdout |

## 5. Input / Output

| File | Format | Description |
|---|---|---|
| `instances.geojson` | GeoJSON | Instance bbox polygons + area/centroid/brightness attributes |
| `instance_labels.tif` | GeoTIFF | Instance label raster (0=background, 1..K=instances) |
| `output-manifest.json` | JSON | Run manifest (input/output/QA/exit code) |

## 6. Technical Principle

(see SKILL.md for details)

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 实例分割（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-instance-segmentation
description: '阈值分割+连通域标记+实例属性提取，输出实例标注GeoJSON（离线numpy等价实现）'
---

# 实例分割 | Instance Segmentation

把影像中每个独立目标（建筑、地块、树冠、池塘等）分割为独立实例，并提取每个实例的面积、质心、边界框与平均亮度，输出实例标注 GeoJSON 与实例标签栅格。

本 skill 是 Mask R-CNN 实例分割网络的**离线 numpy 等价实现**：不依赖深度学习框架，用"阈值/Otsu 前景分离 -> scipy 连通域标记（4/8 连通）-> 逐实例属性提取 -> 地理编码"复现实例分割流水线，连通性差异、实例计数与属性计算均有单元测试验证。

## 依赖

```bash
pip install numpy rasterio scipy scikit-learn geopandas shapely
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-instance-segmentation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2：真实影像 + 手动阈值 + 4连通

```bash
python geoskill-instance-segmentation.py --input scene.tif --threshold 80 --connectivity 4 --min-area 9 --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `instances.geojson` | GeoJSON | 实例 bbox 多边形 + 面积/质心/亮度属性 |
| `instance_labels.tif` | GeoTIFF | 实例标签栅格（0=背景，1..K=实例） |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/退出码） |

## 数据源 / Source

本地单/多波段 GeoTIFF（取首波段），或 --synthetic 合成场景（暗背景 + 分离明亮斑块）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
