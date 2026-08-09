---
name: geoskill-animated-map-series
description: 'Compose multi-temporal rasters into unified rendered frames and a GIF animation'
---

# 动态地图序列 / 动画 | Animated Map Series

Renders multi-temporal rasters (one epoch per band of a multi-band GeoTIFF) into per-frame PNGs using a **unified color scale**, then composes them into a looping GIF. The unified color scale keeps epochs comparable with each other.

Synthetic mode generates an NDVI-like seasonal time series (trend + spatial pattern + noise), with each frame carrying a time label and color bar.

## Core Algorithm / 核心算法

unified_scale computes cross-epoch global minmax/percentile endpoints → per-epoch normalization → colormap rendering of frames (with labels/color bar) → GIF composition with PIL.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## Usage / 使用方法

### Example 1 (Synthetic Data, Offline)

```bash
python geoskill-animated-map-series.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (Custom Frame Duration)

```bash
python geoskill-animated-map-series.py --input series.tif --duration 300 --cmap viridis
```

### Example 3 (Uniform Percentile Color Scale)

```bash
python geoskill-animated-map-series.py --input series.tif --scale percentile --pct 2
```

### Example 4 (12 Synthetic Periods)

```bash
python geoskill-animated-map-series.py --bbox 116 39 117 40 --synthetic --periods 12
```

### Example 5 (Terrain Color Scheme)

```bash
python geoskill-animated-map-series.py --input series.tif --cmap terrain
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `animation.gif` | GIF | Looping animation (primary output) |
| `frames/frame_XXX.png` | PNG | Per-frame images |
| `series_stack.tif` | GeoTIFF | Multi-epoch stack (verifiable output) |
| `frames.json` | JSON | Frame statistics and color scale info |

Each run also produces `output-manifest.json` (run manifest).

## Data Source / 数据源 / Source

Local GeoTIFF / vector files; `--synthetic` mode generates physically consistent simulated data, fully offline.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-animated-map-series
description: 'Compose multi-temporal rasters into unified rendered frames and a GIF animation'
---

# 动态地图序列 / 动画 | Animated Map Series

把多期栅格（多波段 GeoTIFF 每波段一期）用**统一色标**渲染成逐帧 PNG，再合成为循环 GIF。统一色标保证各期之间可比较。

合成模式生成 NDVI 式季节时序（趋势 + 空间格局 + 噪声），每帧带时间标签与色标条。

## 核心算法

unified_scale 计算跨期全局 minmax/percentile 端点 → 逐期归一化 → colormap 渲染帧（含标签/色标）→ PIL 合成 GIF。

## 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-animated-map-series.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（指定帧时长）

```bash
python geoskill-animated-map-series.py --input series.tif --duration 300 --cmap viridis
```

### 示例 3（百分位统一色标）

```bash
python geoskill-animated-map-series.py --input series.tif --scale percentile --pct 2
```

### 示例 4（合成 12 期）

```bash
python geoskill-animated-map-series.py --bbox 116 39 117 40 --synthetic --periods 12
```

### 示例 5（地形配色）

```bash
python geoskill-animated-map-series.py --input series.tif --cmap terrain
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `animation.gif` | GIF | 循环动画（主产物） |
| `frames/frame_XXX.png` | PNG | 逐帧图像 |
| `series_stack.tif` | GeoTIFF | 多期 stack（可验证产物） |
| `frames.json` | JSON | 帧统计与色标信息 |

每次运行还会产出 `output-manifest.json`（运行清单）。

## 数据源 / Source

本地 GeoTIFF / 矢量文件；`--synthetic` 模式生成物理一致的模拟数据，完全离线。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
