# Viewshed Analysis (geoskill-viewshed-analysis)

> DEM-based line-of-sight analysis with Earth curvature correction and multi-observer stacking

---

## 1. Overview

DEM-based visibility analysis: from an observation point, determines pixel by pixel along radial lines whether the line of sight is blocked by terrain, with support for Earth curvature and atmospheric refraction correction (effective Earth radius method). Multi-observer stacking outputs a visibility count and a binary visible raster.

## 2. Features

DEM-based visibility analysis: from an observation point, determines pixel by pixel along radial lines whether the line of sight is blocked by terrain, with support for Earth curvature and atmospheric refraction correction (effective Earth radius method). Multi-observer stacking outputs a visibility count and a binary visible raster.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-viewshed-analysis.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `viewshed.tif` | GeoTIFF/GeoJSON/JSON | Primary output |
| `viewshed_count.tif` | GeoTIFF/GeoJSON/JSON | Primary output |
| `viewshed_stats.json` | GeoTIFF/GeoJSON/JSON | Primary output |
| `output-manifest.json` | JSON | Run manifest |

## 6. Technical Principle

- Ray-by-ray maximum elevation angle tracking
- Earth curvature + refraction correction
- Multi-observer stacking

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 视域分析（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-viewshed-analysis
description: '基于DEM的视线分析，含地球曲率修正和多观察点叠加'
---

# 视域分析 | Viewshed Analysis

基于 DEM 的可视性分析：从观察点沿径向逐像元判断视线是否被地形遮挡，支持地球曲率与大气折射修正（等效地球半径法）。多观察点叠加输出可视次数与二值可视栅格。

## 核心算法

- 逐射线最大仰角追踪
- 地球曲率 + 折射修正
- 多观察点叠加

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-viewshed-analysis.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（指定区域 + 静默）

```bash
python geoskill-viewshed-analysis.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### 示例 3（真实输入）

```bash
python geoskill-viewshed-analysis.py --input <你的数据文件> --output-dir ./out3
```

### 示例 4（极小区域边界测试）

```bash
python geoskill-viewshed-analysis.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `viewshed.tif` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `viewshed_count.tif` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `viewshed_stats.json` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- 合成模式：本地生成物理一致的模拟数据，无外部数据源。
- 真实模式：读取本地输入文件，无网络请求。

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求。
- `--synthetic` 模式不读取任何外部数据。
- 所有计算在本地完成，不上传用户数据。

## License

MIT
