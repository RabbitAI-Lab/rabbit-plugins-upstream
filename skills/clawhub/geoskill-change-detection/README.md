# change-detection

Multi-temporal change detection for satellite imagery using NDVI difference, image differencing, and Change Vector Analysis (CVA).

## Features

- NDVI difference (vegetation change)
- Image differencing (general change)
- Change Vector Analysis (CVA)
- Binary change mask with Otsu threshold
- Statistics report

## Installation

### Option 1: ClawHub
```bash
clawhub install change-detection
```

### Option 2: Manual
```bash
git clone https://github.com/ruiduobao/change-detection.git
cd change-detection
pip install -r requirements.txt
```

### Option 3: Claude Code / skills.sh
```bash
claude skills install change-detection
```

## Quick Start

```bash
# NDVI difference
python scripts/change-detection.py detect \
  --image-t1 2020.tif --image-t2 2023.tif \
  --sensor landsat8 --method ndvi-diff \
  --output change.tif --mask mask.tif

# CVA
python scripts/change-detection.py detect \
  -t1 img1.tif -t2 img2.tif --sensor sentinel2 --method cva \
  -o cva.tif --mask cva_mask.tif --threshold 0.15

# Report
python scripts/change-detection.py report --mask mask.tif --json report.json
```

## Dependencies

```
rasterio>=1.3.0
numpy>=1.21.0
tqdm>=4.64.0
```

## Data Source

Local raster processing — two co-registered GeoTIFF images required.

## License

MIT-0 (Public Domain)

---

# 中文说明

对两期卫星影像进行变化检测，支持 NDVI 差值、影像差值和变化向量分析（CVA）。

## 功能

- NDVI 差值（植被变化）
- 影像差值（通用变化）
- 变化向量分析（CVA）
- 二值变化掩膜 + Otsu 阈值
- 统计报告

## 安装

### 方式一：ClawHub
```bash
clawhub install change-detection
```

### 方式二：手动安装
```bash
git clone https://github.com/ruiduobao/change-detection.git
cd change-detection
pip install -r requirements.txt
```

### 方式三：Claude Code / skills.sh
```bash
claude skills install change-detection
```

## 快速开始

```bash
# NDVI 差值
python scripts/change-detection.py detect \
  --image-t1 2020.tif --image-t2 2023.tif \
  --sensor landsat8 --method ndvi-diff \
  --output change.tif --mask mask.tif

# CVA
python scripts/change-detection.py detect \
  -t1 img1.tif -t2 img2.tif --sensor sentinel2 --method cva \
  -o cva.tif --mask cva_mask.tif --threshold 0.15

# 报告
python scripts/change-detection.py report --mask mask.tif --json report.json
```

## 数据来源

本地栅格处理 — 需要两幅配准好的 GeoTIFF 影像。

## 许可证

MIT-0 (Public Domain)
