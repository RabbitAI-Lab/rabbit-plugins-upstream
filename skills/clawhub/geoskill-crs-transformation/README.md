# Coordinate Reference System Transformation (geoskill-crs-transformation)

> EPSG coordinate reference system transformation via pyproj with built-in WGS84 / GCJ02 / BD09 conversions for point sets and vector features.

---

## 1. Overview

Two conversion paths are provided:
- **EPSG mode** (default): strict transformation between arbitrary EPSG codes via the pyproj `Transformer` (e.g., WGS84 4326 ↔ Web Mercator 3857, UTM zones), supporting whole-layer reprojection and batch conversion of point sets with round-trip consistency.
- **China coordinate system mode**: built-in analytical offset formulas (National Geomatics Center algorithm, Krasovsky ellipsoid) for WGS-84 (GPS) ↔ GCJ-02 (Mars coordinates, Amap/Tencent) ↔ BD-09 (Baidu); GCJ-02 → WGS-84 uses iterative inversion with accuracy better than 1e-6 degrees, and coordinates outside China are returned unchanged. Suitable for GPS track correction, aligning coordinates on internet maps, and registering data across coordinate systems.

The `--synthetic` mode generates a random point set inside the bbox for offline demonstration.

## 2. Features

Two conversion paths are provided:
- **EPSG mode** (default): strict transformation between arbitrary EPSG codes via the pyproj `Transformer` (e.g., WGS84 4326 ↔ Web Mercator 3857, UTM zones), supporting whole-layer reprojection and batch conversion of point sets with round-trip consistency.
- **China coordinate system mode**: built-in analytical offset formulas (National Geomatics Center algorithm, Krasovsky ellipsoid) for WGS-84 (GPS) ↔ GCJ-02 (Mars coordinates, Amap/Tencent) ↔ BD-09 (Baidu); GCJ-02 → WGS-84 uses iterative inversion with accuracy better than 1e-6 degrees, and coordinates outside China are returned unchanged. Suitable for GPS track correction, aligning coordinates on internet maps, and registering data across coordinate systems.

The `--synthetic` mode generates a random point set inside the bbox for offline demonstration.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-crs-transformation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `transformed.geojson` | GeoJSON | Transformed features |
| `transformation_report.json` | JSON | Transformation parameters and sample coordinates before/after |
| `output-manifest.json` | JSON | Run manifest |

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

# 坐标系转换（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-crs-transformation
description: '基于 pyproj 的 EPSG 坐标参考系转换，内置 WGS84 / GCJ02 / BD09 互转，支持点集与矢量要素。EPSG coordinate reference system transformation via pyproj with built-in WGS84 / GCJ02 / BD09 conversions for point sets and vector features.'
---

# 坐标系转换 | CRS Transformation

两条转换路径：

- **EPSG 模式**（默认）：基于 pyproj `Transformer` 在任意 EPSG 代码之间
  严格转换（如 WGS84 4326 ↔ Web Mercator 3857、UTM 分带），支持整图层
  重投影与点集批量转换，往返一致。
- **中国坐标系模式**：内置 WGS-84（GPS）↔ GCJ-02（火星坐标，高德/腾讯）
  ↔ BD-09（百度）的解析加偏公式（国测局算法，克拉索夫斯基椭球），其中
  GCJ-02 → WGS-84 用迭代反算，精度优于 1e-6 度；中国境外坐标原样返回。

适合 GPS 轨迹纠偏、互联网地图坐标对齐、跨坐标系数据配准。`--synthetic`
模式在 bbox 内生成随机点集做离线演示。

## 依赖

```bash
pip install numpy rasterio geopandas shapely fiona pyproj
```

## 使用方法

### 基本用法

```bash
python geoskill-crs-transformation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 1（合成数据，离线，EPSG 4326→3857）

```bash
python geoskill-crs-transformation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --mode epsg --to-crs EPSG:3857 --output-dir ./mercator
```

### 示例 2：矢量文件重投影到 UTM 50N

```bash
python geoskill-crs-transformation.py --input sites.geojson --mode epsg --from-crs EPSG:4326 --to-crs EPSG:32650 --output-dir ./utm
```

### 示例 3：GPS 坐标(WGS84)转高德坐标(GCJ02)

```bash
python geoskill-crs-transformation.py --input gps_track.geojson --mode system --system-from wgs84 --system-to gcj02 --output-dir ./gcj
```

### 示例 4：百度坐标(BD09)转 GPS(WGS84)

```bash
python geoskill-crs-transformation.py --input bd_pois.geojson --mode system --system-from bd09 --system-to wgs84 --output-dir ./wgs
```

### 示例 5：合成点集 GCJ02→BD09

```bash
python geoskill-crs-transformation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --mode system --system-from gcj02 --system-to bd09 --output-dir ./bd --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `transformed.geojson` | GeoJSON | 转换后的要素 |
| `transformation_report.json` | JSON | 转换参数与抽样前后坐标 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- `--input`：本地矢量文件（点/任意几何）
- `--synthetic`：本地生成随机点集
- 加偏公式为公开算法，无外部服务依赖

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
