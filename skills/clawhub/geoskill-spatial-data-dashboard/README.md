# Spatial Data Dashboard (geoskill-spatial-data-dashboard)

> Build spatial dashboards combining map layers and statistical charts into HTML

---

## 1. Overview

Summarizes spatial data into a self-contained HTML dashboard: Leaflet map + rendered overlay layers + KPI metric cards + pure-SVG histograms and zone-mean line charts + zonal statistics tables. Charts are drawn with a built-in SVG generator, require no external JS chart library, and can be opened offline.

## 2. Features

Summarizes spatial data into a self-contained HTML dashboard: Leaflet map + rendered overlay layers + KPI metric cards + pure-SVG histograms and zone-mean line charts + zonal statistics tables. Charts are drawn with a built-in SVG generator, require no external JS chart library, and can be opened offline.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-spatial-data-dashboard.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `dashboard.html` | HTML | Dashboard (primary output) |
| `dashboard.json` | JSON | Statistics/histograms/zones (verifiable output) |
| `dashboard_data.tif` | GeoTIFF | Data raster |

Each run also produces `output-manifest.json` (run manifest).

## 6. Technical Principle

raster_histogram/descriptive_stats/zonal_statistics computation → SVG histogram and line-chart generation → render_overlay terrain overlay → Leaflet dashboard assembly.

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 空间数据仪表盘（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-spatial-data-dashboard
description: 'Build spatial dashboards combining map layers and statistical charts into HTML'
---

# 空间数据仪表盘 | Spatial Data Dashboard

把空间数据汇总成自包含 HTML 仪表盘：Leaflet 地图 + 渲染叠加层 + KPI 指标卡 + 纯 SVG 直方图与分区均值折线图 + 分区统计表。

图表用内置 SVG 生成器绘制，不依赖外部 JS 图表库，离线可开。

## 核心算法

raster_histogram/descriptive_stats/zonal_statistics 统计 → SVG 直方图与折线生成 → render_overlay 地形叠加 → Leaflet 仪表盘组装。

## 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-spatial-data-dashboard.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（指定直方图分箱）

```bash
python geoskill-spatial-data-dashboard.py --input dem.tif --bins 30 --title "流域仪表盘"
```

### 示例 3（合成模式）

```bash
python geoskill-spatial-data-dashboard.py --bbox 116 39 117 40 --synthetic --bins 24
```

### 示例 4（自定义标题）

```bash
python geoskill-spatial-data-dashboard.py --input dem.tif --title "城市热环境"
```

### 示例 5（更多分箱看分布）

```bash
python geoskill-spatial-data-dashboard.py --input dem.tif --bins 50
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `dashboard.html` | HTML | 仪表盘（主产物） |
| `dashboard.json` | JSON | 统计/直方图/分区（可验证产物） |
| `dashboard_data.tif` | GeoTIFF | 数据栅格 |

每次运行还会产出 `output-manifest.json`（运行清单）。

## 数据源 / Source

本地 GeoTIFF / 矢量文件；`--synthetic` 模式生成物理一致的模拟数据，完全离线。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
