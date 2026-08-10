---
name: geoskill-spatial-data-dashboard
description: 'Build spatial dashboards combining map layers and statistical charts into HTML'
---

# 空间数据仪表盘 | Spatial Data Dashboard

Aggregates spatial data into a self-contained HTML dashboard: a Leaflet map + rendered overlay layers + KPI metric cards + pure-SVG histogram and zonal-mean line charts + a zonal statistics table.

Charts are drawn by a built-in SVG generator, with no dependency on external JS charting libraries, so the dashboard works offline.

## Core Algorithm / 核心算法

raster_histogram / descriptive_stats / zonal_statistics statistics → SVG histogram and line-chart generation → render_overlay terrain overlay → Leaflet dashboard assembly.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## Usage / 使用方法

### Example 1 (Synthetic Data, Offline)

```bash
python geoskill-spatial-data-dashboard.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (Custom Histogram Binning)

```bash
python geoskill-spatial-data-dashboard.py --input dem.tif --bins 30 --title "watershed dashboard"
```

### Example 3 (Synthetic Mode)

```bash
python geoskill-spatial-data-dashboard.py --bbox 116 39 117 40 --synthetic --bins 24
```

### Example 4 (Custom Title)

```bash
python geoskill-spatial-data-dashboard.py --input dem.tif --title "urban thermal environment"
```

### Example 5 (More Bins to View Distribution)

```bash
python geoskill-spatial-data-dashboard.py --input dem.tif --bins 50
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `dashboard.html` | HTML | Dashboard (primary output) |
| `dashboard.json` | JSON | Statistics/histogram/zones (verifiable output) |
| `dashboard_data.tif` | GeoTIFF | Data raster |

Each run also produces `output-manifest.json` (run manifest).

## Data Source / 数据源 / Source

Local GeoTIFF / vector files; `--synthetic` mode generates physically consistent simulated data, fully offline.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; no user data is uploaded.

## License / License

MIT

---


<!-- ===== 中文原文 (Chinese Original) ===== -->

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
