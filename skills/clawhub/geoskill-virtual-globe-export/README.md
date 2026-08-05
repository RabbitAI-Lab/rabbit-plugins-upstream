# Virtual Globe Export (geoskill-virtual-globe-export)

> Export data to KML or CZML with time attributes and popup info for virtual globes

---

## 1. Overview

Exports spatiotemporal point data into formats readable by virtual globes (Google Earth / Cesium): KML (Placemark + TimeStamp + ExtendedData popup info, coordinates strictly in lon,lat,alt order) and CZML (document header + cartographicDegrees position + availability time interval). The synthetic mode generates a timestamped diagonal moving track for demonstrating temporal dynamics.

## 2. Features

Exports spatiotemporal point data into formats readable by virtual globes (Google Earth / Cesium): KML (Placemark + TimeStamp + ExtendedData popup info, coordinates strictly in lon,lat,alt order) and CZML (document header + cartographicDegrees position + availability time interval). The synthetic mode generates a timestamped diagonal moving track for demonstrating temporal dynamics.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-virtual-globe-export.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `export.kml` | KML | KML document (primary output) |
| `export.czml` | CZML | Cesium time-dynamic JSON |
| `export.json` | JSON | Structured features (verifiable output) |
| `track_density.tif` | GeoTIFF | Track density raster |

Each run also produces `output-manifest.json` (run manifest).

## 6. Technical Principle

format_kml_coord(lon,lat,alt) strictly places longitude first → build_kml(TimeStamp/ExtendedData/Point|LineString) → build_czml(document package + position.cartographicDegrees + availability).

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 虚拟地球导出（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-virtual-globe-export
description: 'Export data to KML or CZML with time attributes and popup info for virtual globes'
---

# 虚拟地球导出 | Virtual Globe Export

把时空点数据导出为虚拟地球（Google Earth / Cesium）可读格式：KML（Placemark+TimeStamp+ExtendedData 弹出信息，坐标严格 lon,lat,alt）与 CZML（document 包头 + cartographicDegrees position + availability 时间区间）。

合成模式生成带时间戳的对角线移动航迹，便于演示时间动态。

## 核心算法

format_kml_coord(lon,lat,alt) 严格经度在前 → build_kml(TimeStamp/ExtendedData/Point|LineString) → build_czml(document 包 + position.cartographicDegrees + availability)。

## 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-virtual-globe-export.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（仅导 KML）

```bash
python geoskill-virtual-globe-export.py --input track.geojson --format kml --name "航线"
```

### 示例 3（仅导 CZML）

```bash
python geoskill-virtual-globe-export.py --input track.geojson --format czml
```

### 示例 4（合成 20 点航迹）

```bash
python geoskill-virtual-globe-export.py --bbox 116 39 117 40 --synthetic --points 20
```

### 示例 5（CSV 点输入）

```bash
python geoskill-virtual-globe-export.py --input points.csv --format both
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `export.kml` | KML | KML 文档（主产物） |
| `export.czml` | CZML | Cesium 时间动态 JSON |
| `export.json` | JSON | 结构化要素（可验证产物） |
| `track_density.tif` | GeoTIFF | 航迹密度栅格 |

每次运行还会产出 `output-manifest.json`（运行清单）。

## 数据源 / Source

本地 GeoTIFF / 矢量文件；`--synthetic` 模式生成物理一致的模拟数据，完全离线。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
