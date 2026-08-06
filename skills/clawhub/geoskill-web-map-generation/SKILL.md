---
name: geoskill-web-map-generation
description: 'Generate interactive web maps from GeoTIFF or GeoJSON with Leaflet templates and metadata'
---

# 交互式Web地图生成 | Interactive Web Map Generation

Renders GeoTIFF rasters into georeferenced PNGs and embeds them into self-contained Leaflet HTML maps, so users can zoom, pan, and click to inspect coordinates right in the browser.

Supports both percentile and min-max contrast stretches and 8 matplotlib colormaps; produces a metadata JSON with the geographic extent, stretch endpoints, and statistics, plus a reproducible rendered GeoTIFF.

## Core Algorithm / 核心算法

percentile/min-max linear stretch → matplotlib colormap coloring → PIL PNG encoding (base64 embedded) → Leaflet ImageOverlay.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## Usage / 使用方法

### Example 1 (Synthetic Data, Offline)

```bash
python geoskill-web-map-generation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (Custom Color Scheme and Stretch)

```bash
python geoskill-web-map-generation.py --input dem.tif --cmap terrain --stretch percentile --output-dir ./out
```

### 示例 3（min-max 拉伸 + 高不透明度）

```bash
python geoskill-web-map-generation.py --input dem.tif --stretch minmax --opacity 1.0
```

### Example 4 (Specified Title)

```bash
python geoskill-web-map-generation.py --bbox 116 39 117 40 --synthetic --title "Beijing DEM"
```

### Example 5 (Custom Percentile Endpoints)

```bash
python geoskill-web-map-generation.py --input dem.tif --lo-pct 1 --hi-pct 99
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `web_map.html` | HTML | Self-contained interactive map (primary output) |
| `rendered.tif` | GeoTIFF | Stretched [0,1] rendered raster (verifiable output) |
| `map_metadata.json` | JSON | Extent/colormap/statistics metadata |

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
name: geoskill-web-map-generation
description: 'Generate interactive web maps from GeoTIFF or GeoJSON with Leaflet templates and metadata'
---

# 交互式Web地图生成 | Interactive Web Map Generation

把 GeoTIFF 栅格渲染为带地理配准的 PNG，并嵌入自包含的 Leaflet HTML 地图，浏览器打开即可缩放、平移、点击查看经纬度。

支持百分位 / min-max 两种对比度拉伸与 8 种 matplotlib 配色；产出含地理范围、拉伸端点与统计的元数据 JSON，以及可复现的渲染栅格 GeoTIFF。

## 核心算法

percentile/min-max 线性拉伸 → matplotlib colormap 着色 → PIL 编码 PNG(base64 内嵌) → Leaflet ImageOverlay。

## 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-web-map-generation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（指定配色与拉伸）

```bash
python geoskill-web-map-generation.py --input dem.tif --cmap terrain --stretch percentile --output-dir ./out
```

### 示例 3（min-max 拉伸 + 高不透明度）

```bash
python geoskill-web-map-generation.py --input dem.tif --stretch minmax --opacity 1.0
```

### 示例 4（指定标题）

```bash
python geoskill-web-map-generation.py --bbox 116 39 117 40 --synthetic --title "北京 DEM"
```

### 示例 5（自定义百分位端点）

```bash
python geoskill-web-map-generation.py --input dem.tif --lo-pct 1 --hi-pct 99
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `web_map.html` | HTML | 自包含交互式地图（主产物） |
| `rendered.tif` | GeoTIFF | 拉伸后 [0,1] 渲染栅格（可验证产物） |
| `map_metadata.json` | JSON | 范围/配色/统计元数据 |

每次运行还会产出 `output-manifest.json`（运行清单）。

## 数据源 / Source

本地 GeoTIFF / 矢量文件；`--synthetic` 模式生成物理一致的模拟数据，完全离线。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
