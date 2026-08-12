# Hillshade Visualization (geoskill-hillshade-visualization)

> Multi-directional hillshade with vertical exaggeration and color overlay using the Horn algorithm

---

## 1. Overview

Computes hillshade using the Horn (1981) algorithm, supporting **multi-directional weighted compositing** (highlighting terrain textures of different orientations), vertical exaggeration via zfactor, and terrain color overlay. Multi-directional compositing computes hillshade for each azimuth angle and then combines them with weights (automatically normalized).

## 2. Features

Computes hillshade using the Horn (1981) algorithm, supporting **multi-directional weighted compositing** (highlighting terrain textures of different orientations), vertical exaggeration via zfactor, and terrain color overlay. Multi-directional compositing computes hillshade for each azimuth angle and then combines them with weights (automatically normalized).

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-hillshade-visualization.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `color_shaded.png` | PNG | Color-overlay shaded relief (primary output) |
| `hillshade.tif` | GeoTIFF | Hillshade raster [0,1] (verifiable output) |
| `hillshade_meta.json` | JSON | Azimuth/weights/statistics |

Each run also produces `output-manifest.json` (run manifest).


## 6. Technical Principle

Horn 3×3 differences give dz/dx, dz/dy → slope/aspect → sin(alt)cos(slope)+cos(alt)sin(slope)cos(az-aspect); multi-directional is the normalized weighted sum of the per-azimuth hillshade values.

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 山体阴影可视化（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-hillshade-visualization
description: 'Multi-directional hillshade with vertical exaggeration and color overlay using the Horn algorithm'
---

# 山体阴影可视化 | Hillshade Visualization

用 Horn (1981) 算法计算山体阴影，支持**多方向加权合成**（突出不同走向的地形纹理）、垂直夸张 zfactor 与地形色彩叠加。

多方向合成对每个方位角分别求 hillshade 再按权重（自动归一化）加权。

## 核心算法

Horn 3×3 差分求 dz/dx,dz/dy → slope/aspect → sin(alt)cos(slope)+cos(alt)sin(slope)cos(az-aspect)；多方向为各方位角 hillshade 的归一化加权和。

## 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-hillshade-visualization.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（自定义方位与权重）

```bash
python geoskill-hillshade-visualization.py --input dem.tif --azimuths 315 270 --weights 0.7 0.3
```

### 示例 3（低太阳角更锐利）

```bash
python geoskill-hillshade-visualization.py --input dem.tif --altitude 30 --zfactor 2
```

### 示例 4（灰度配色）

```bash
python geoskill-hillshade-visualization.py --input dem.tif --cmap gray
```

### 示例 5（合成多山脊）

```bash
python geoskill-hillshade-visualization.py --bbox 116 39 117 40 --synthetic --zfactor 3
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `color_shaded.png` | PNG | 色彩叠加山体阴影（主产物） |
| `hillshade.tif` | GeoTIFF | 山体阴影栅格 [0,1]（可验证产物） |
| `hillshade_meta.json` | JSON | 方位/权重/统计 |

每次运行还会产出 `output-manifest.json`（运行清单）。

## 数据源 / Source

本地 GeoTIFF / 矢量文件；`--synthetic` 模式生成物理一致的模拟数据，完全离线。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
