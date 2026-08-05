---
name: geoskill-map-layout-automation
description: 'Automate map layout with title, legend, scale bar and north arrow to PDF or PNG'
---

# 地图排版自动化 | Map Layout Automation

Automatically lay out a raster map into a finished cartographic product: map frame + title + legend (colorbar) + scale bar + north arrow, output as high-resolution PNG and vector PDF.

The scale bar length is converted from the map-frame width and the reference latitude into an integer number of kilometers following a 1-2-5 sequence; the north arrow is a standard north-pointing arrow.

## Core Algorithm / 核心算法

meters_per_degree_lon=111320·cos(lat) → scale_bar_km=round(map_width×fraction) → draw_scale_bar/north_arrow data-coordinate decoration → matplotlib layout.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## Usage / 使用方法

### Example 1 (synthetic data, offline)

```bash
python geoskill-map-layout-automation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (custom title and color scheme)

```bash
python geoskill-map-layout-automation.py --input dem.tif --title "terrain of the study area" --cmap viridis
```

### Example 3 (omit the north arrow)

```bash
python geoskill-map-layout-automation.py --input dem.tif --no-north
```

### Example 4 (adjust the scale bar fraction)

```bash
python geoskill-map-layout-automation.py --input dem.tif --bar-fraction 0.35
```

### Example 5 (high-dpi output)

```bash
python geoskill-map-layout-automation.py --input dem.tif --dpi 200
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `layout.png` | PNG | Layout map (main deliverable) |
| `layout.pdf` | PDF | Vector version |
| `layout_data.tif` | GeoTIFF | Data raster (verifiable deliverable) |
| `layout_meta.json` | JSON | Scale bar/element toggles/dpi |

Each run also produces `output-manifest.json` (run manifest).

## Data Source / 数据源 / Source

Local GeoTIFF / vector files; `--synthetic` mode generates physically consistent simulated data, fully offline.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is performed locally; no user data is uploaded.

## License / License

MIT

---


<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-map-layout-automation
description: 'Automate map layout with title, legend, scale bar and north arrow to PDF or PNG'
---

# 地图排版自动化 | Map Layout Automation

把栅格地图自动排版成制图成品：图幅 + 标题 + 图例(colorbar) + 比例尺 + 指北针，输出高分辨率 PNG 与矢量 PDF。

比例尺长度按图幅宽度与参考纬度换算成 1-2-5 序列的整数千米；指北针为标准北向箭头。

## 核心算法

meters_per_degree_lon=111320·cos(lat) → scale_bar_km=圆整(图幅宽×fraction) → draw_scale_bar/north_arrow 数据坐标整饰 → matplotlib 排版。

## 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-map-layout-automation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（自定义标题与配色）

```bash
python geoskill-map-layout-automation.py --input dem.tif --title "研究区地形" --cmap viridis
```

### 示例 3（省略指北针）

```bash
python geoskill-map-layout-automation.py --input dem.tif --no-north
```

### 示例 4（调整比例尺占比）

```bash
python geoskill-map-layout-automation.py --input dem.tif --bar-fraction 0.35
```

### 示例 5（高 dpi 输出）

```bash
python geoskill-map-layout-automation.py --input dem.tif --dpi 200
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `layout.png` | PNG | 排版地图（主产物） |
| `layout.pdf` | PDF | 矢量版 |
| `layout_data.tif` | GeoTIFF | 数据栅格（可验证产物） |
| `layout_meta.json` | JSON | 比例尺/元素开关/dpi |

每次运行还会产出 `output-manifest.json`（运行清单）。

## 数据源 / Source

本地 GeoTIFF / 矢量文件；`--synthetic` 模式生成物理一致的模拟数据，完全离线。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
