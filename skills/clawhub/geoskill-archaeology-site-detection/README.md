# Remote Sensing Detection of Archaeological Sites (geoskill-archaeology-site-detection)

> LiDAR micro-topography, multispectral anomaly and SAR fusion for suspected archaeological site detection with anomaly grading

---

## 1. Overview

Fuses LiDAR micro-topography, multispectral vegetation anomalies and SAR backscatter to automatically screen suspected archaeological sites and assign anomaly grades, providing remote sensing leads for large-scale archaeological surveys. The method works in three layers: large-window detrending of the DEM to extract local relief (highlighting micro-relief such as mounds/depressions); NDVI computation with detrending to identify crop marks caused by buried remains; and z-score analysis of SAR backscatter to detect moisture/structural anomalies. The three anomaly layers are normalized and fused by weighted combination (or maximum), graded by thresholds (none/low/high), and local peaks are used to locate suspected site points.

## 2. Features

Fuses LiDAR micro-topography, multispectral vegetation anomalies and SAR backscatter to automatically screen suspected archaeological sites and assign anomaly grades, providing remote sensing leads for large-scale archaeological surveys. The method works in three layers: large-window detrending of the DEM to extract local relief (highlighting micro-relief such as mounds/depressions); NDVI computation with detrending to identify crop marks caused by buried remains; and z-score analysis of SAR backscatter to detect moisture/structural anomalies. The three anomaly layers are normalized and fused by weighted combination (or maximum), graded by thresholds (none/low/high), and local peaks are used to locate suspected site points.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-archaeology-site-detection.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `anomaly_score.tif` | GeoTIFF | Fused anomaly score [0,1] |
| `anomaly_level.tif` | GeoTIFF | Anomaly grade (0 none / 1 low / 2 high) |
| `suspected_sites.geojson` | GeoJSON | Suspected site points (with score and grade) |
| `detection_report.json` | JSON | Statistical summary and top sites |
| `output-manifest.json` | JSON | Run manifest |


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

# 考古遗址遥感探测（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-archaeology-site-detection
description: 'LiDAR micro-topography, multispectral anomaly and SAR fusion for suspected archaeological site detection with anomaly grading'
---

# 考古遗址遥感探测 | Archaeological Site Detection

融合 LiDAR 微地形、多光谱植被异常与 SAR 后向散射，自动筛查疑似考古遗址并给出异常等级，为大范围考古调查提供遥感线索。

方法分三层：对 DEM 做大窗口去趋势提取局部起伏（突出土丘/凹陷等微地貌）；计算 NDVI 并去趋势识别地下遗存导致的作物标志 (crop mark)；对 SAR 后向散射做 z-score 识别湿度/结构异常。三层异常归一化后按权重融合（或取最大），阈值分级（无/低/高）并用局部峰值定位疑似遗址点。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-archaeology-site-detection.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例 1（合成数据，离线）

```bash
python geoskill-archaeology-site-detection.py --bbox 116 39 117 40 --synthetic --output-dir ./out
```

### 示例 2（真实多波段影像（DEM/Red/NIR/SAR））

```bash
python geoskill-archaeology-site-detection.py --input scene.tif --output-dir ./out
```

### 示例 3（改用最大值融合）

```bash
python geoskill-archaeology-site-detection.py --input scene.tif --fusion max --output-dir ./out
```

### 示例 4（调整权重与分级阈值）

```bash
python geoskill-archaeology-site-detection.py --input scene.tif --w-relief 0.5 --w-spectral 0.3 --w-sar 0.2 --high-threshold 0.8 --output-dir ./out
```

### 示例 5（更大去趋势窗口（区域地貌））

```bash
python geoskill-archaeology-site-detection.py --input scene.tif --window 25 --footprint 9 --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `anomaly_score.tif` | GeoTIFF | 融合异常评分 [0,1] |
| `anomaly_level.tif` | GeoTIFF | 异常分级（0 无 / 1 低 / 2 高） |
| `suspected_sites.geojson` | GeoJSON | 疑似遗址点（含评分与等级） |
| `detection_report.json` | JSON | 统计摘要与 Top 站点 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

多波段 GeoTIFF，波段顺序 DEM / Red / NIR / SAR。 或使用 `--synthetic` 生成物理一致的模拟数据（完全离线）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
