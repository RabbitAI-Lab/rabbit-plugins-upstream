# Glacier Retreat Monitoring (geoskill-glacier-retreat-monitoring)

> Monitors glacier retreat from multi-temporal NDSI boundaries: extracts glacier extents, vectorizes them into boundary polygons, analyzes terminus retreat and area change curves, and outputs boundary GeoJSON series, retreat rates and area JSON.

---

## 1. Overview

Extracts multi-temporal glacier extents using the Normalized Difference Snow Index NDSI=(Green−SWIR)/(Green+SWIR) (NDSI>0.4 is snow/ice), vectorizes each epoch's glacier raster into boundary polygons, and analyzes terminus retreat and area change along the time series. Suitable for monitoring alpine glacier responses to climate change and updating glacier inventories. Core algorithms: - **NDSI extraction**: NDSI>0.4 identifies snow/ice, with an adjustable threshold. - **Boundary vectorization**: converts the binary mask into shapely polygons via contour tracing, projects to EPSG:4326, aggregates into a geopandas.GeoDataFrame and exports GeoJSON. - **Area change curve**: glacier area per epoch (pixel count × pixel area). - **Terminus position and retreat rate**: the centroid row coordinate represents the terminus position; a decreasing row number indicates retreat toward higher elevation; the displacement between adjacent epochs (m) divided by the time interval gives the retreat rate. The `--synthetic` mode generates a physically consistent valley scene containing glacier retreat (offline).

## 2. Features

Extracts multi-temporal glacier extents using the Normalized Difference Snow Index NDSI=(Green−SWIR)/(Green+SWIR) (NDSI>0.4 is snow/ice), vectorizes each epoch's glacier raster into boundary polygons, and analyzes terminus retreat and area change along the time series. Suitable for monitoring alpine glacier responses to climate change and updating glacier inventories. Core algorithms: - **NDSI extraction**: NDSI>0.4 identifies snow/ice, with an adjustable threshold. - **Boundary vectorization**: converts the binary mask into shapely polygons via contour tracing, projects to EPSG:4326, aggregates into a geopandas.GeoDataFrame and exports GeoJSON. - **Area change curve**: glacier area per epoch (pixel count × pixel area). - **Terminus position and retreat rate**: the centroid row coordinate represents the terminus position; a decreasing row number indicates retreat toward higher elevation; the displacement between adjacent epochs (m) divided by the time interval gives the retreat rate. The `--synthetic` mode generates a physically consistent valley scene containing glacier retreat (offline).

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-glacier-retreat-monitoring.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `glacier_boundaries.geojson` | GeoJSON | Multi-epoch glacier boundary polygons (with date_index / area) |
| `glacier_last.tif` | GeoTIFF (float32) | Final-epoch glacier mask, EPSG:4326 |
| `glacier_retreat.json` | JSON | Area curves, terminus row series, retreat rates, polygon summary |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/software versions) |

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

# 冰川退缩监测（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-glacier-retreat-monitoring
description: '用 NDSI 提取多期冰川范围并矢量化为边界多边形，分析冰川末端位置后退与面积变化曲线，输出边界 GeoJSON 序列、退缩速率与面积 JSON。Monitors glacier retreat from multi-temporal NDSI boundaries.'
---

# 冰川退缩监测 | Glacier Retreat Monitoring

用归一化差分雪指数 NDSI=(Green−SWIR)/(Green+SWIR) 提取多期冰川范围
（NDSI>0.4 为雪/冰），把每期冰川栅格矢量化为边界多边形，并沿时间序列分析
末端后退与面积变化。适用于高山冰川对气候变化的响应监测与编目更新。

核心算法：

- **NDSI 提取**：NDSI>0.4 判识雪/冰，阈值可调。
- **边界矢量化**：用等高线追踪把二值掩膜转为 shapely 多边形，投影到 EPSG:4326，
  汇总为 geopandas.GeoDataFrame 并导出 GeoJSON。
- **面积变化曲线**：每期冰川面积（像元计数 × 像元面积）。
- **末端位置与退缩速率**：用冰川质心行坐标代表末端位置，行号减小说明向高
  海拔后退；相邻期位移（米）/ 时间间隔即退缩速率。

支持 `--synthetic` 模式生成含冰川后退的物理一致山谷场景（离线）。

## 依赖

```bash
pip install numpy rasterio scipy geopandas shapely matplotlib
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-glacier-retreat-monitoring.py --bbox 86.0 28.0 87.0 29.0 --synthetic --n-dates 3 --output-dir ./output
```

### 示例 1：多期退缩分析

```bash
python geoskill-glacier-retreat-monitoring.py \
    --bbox 86.0 28.0 87.0 29.0 \
    --synthetic --n-dates 5 --years-per-step 2 \
    --output-dir ./retreat
```

### 示例 2：调整 NDSI 阈值

```bash
python geoskill-glacier-retreat-monitoring.py \
    --bbox 86.0 28.0 87.0 29.0 \
    --synthetic --ndsi-threshold 0.5 \
    --output-dir ./thr
```

### 示例 3：真实多期影像立方体

```bash
python geoskill-glacier-retreat-monitoring.py \
    --input glacier_cube.tif \
    --n-dates 3 \
    --output-dir ./real
```

输入立方体约定：形状 (n_dates, 2, H, W)，每个时期的两个波段为 green / swir。

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `glacier_boundaries.geojson` | GeoJSON | 多期冰川边界多边形（含 date_index / area） |
| `glacier_last.tif` | GeoTIFF (float32) | 末期冰川掩膜，EPSG:4326 |
| `glacier_retreat.json` | JSON | 面积曲线、末端行序列、退缩速率、多边形汇总 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

- **合成模式**：本地生成，无外部数据源
- **真实模式**：用户提供多期 green/swir 立方体（如 Landsat / Sentinel-2）

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- 所有计算在本地完成，不上传用户数据

## License

MIT
