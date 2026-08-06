# Interactive WebGIS Platform (geoskill-interactive-webgis)

> Configure a lightweight WebGIS with query support as a self-contained HTML app

---

## 1. Overview

Generates a self-contained lightweight WebGIS: Leaflet base map + rendered overlay layers + POI monitoring-point layer + **click-to-query** (embedded downsampled raster JSON with browser-side nearest-neighbor elevation lookup) + a layer toggle panel. No backend required. The attribute query engine supports six operators — gt/lt/ge/le/eq/contains — and is unit-testable; point features are also aggregated into a density raster.

## 2. Features

Generates a self-contained lightweight WebGIS: Leaflet base map + rendered overlay layers + POI monitoring-point layer + **click-to-query** (embedded downsampled raster JSON with browser-side nearest-neighbor elevation lookup) + a layer toggle panel. No backend required. The attribute query engine supports six operators — gt/lt/ge/le/eq/contains — and is unit-testable; point features are also aggregated into a density raster.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-interactive-webgis.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `webgis.html` | HTML | WebGIS application (primary output) |
| `webgis_data.json` | JSON | Raster grid/sites/config (verifiable output) |
| `features.geojson` | GeoJSON | Point features |
| `density.tif` | GeoTIFF | Point density raster |

Each run also produces `output-manifest.json` (run manifest).

## 6. Technical Principle

query_value_at bilinear point query + nearest_query nearest neighbor → build_layer_config layer configuration → point_density_raster aggregation → Leaflet + embedded GRID assembly.

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 交互式WebGIS平台（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-interactive-webgis
description: 'Configure a lightweight WebGIS with query support as a self-contained HTML app'
---

# 交互式WebGIS平台 | Interactive WebGIS Platform

生成自包含轻量级 WebGIS：Leaflet 底图 + 渲染叠加层 + POI 监测点图层 + **点击即查**（内嵌降采样栅格 JSON，浏览器端最近邻查询高程）+ 图层开关面板。无需后端。

属性查询引擎支持 gt/lt/ge/le/eq/contains 六种运算符，可单测；另把点要素聚合成密度栅格。

## 核心算法

query_value_at 双线性点查询 + nearest_query 最近邻 → build_layer_config 图层配置 → point_density_raster 聚合 → Leaflet+内嵌 GRID 组装。

## 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-interactive-webgis.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（属性查询）

```bash
python geoskill-interactive-webgis.py --input poi.geojson --query-field value --query-op gt --query-value 50
```

### 示例 3（contains 查询）

```bash
python geoskill-interactive-webgis.py --input poi.geojson --query-field category --query-op contains --query-value school
```

### 示例 4（合成 200 个 POI）

```bash
python geoskill-interactive-webgis.py --bbox 116 39 117 40 --synthetic --n-points 200
```

### 示例 5（自定义颜色与标题）

```bash
python geoskill-interactive-webgis.py --bbox 116 39 117 40 --synthetic --color "#e6550d" --title "城市设施"
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `webgis.html` | HTML | WebGIS 应用（主产物） |
| `webgis_data.json` | JSON | 栅格网格/站点/配置（可验证产物） |
| `features.geojson` | GeoJSON | 点要素 |
| `density.tif` | GeoTIFF | 点密度栅格 |

每次运行还会产出 `output-manifest.json`（运行清单）。

## 数据源 / Source

本地 GeoTIFF / 矢量文件；`--synthetic` 模式生成物理一致的模拟数据，完全离线。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
