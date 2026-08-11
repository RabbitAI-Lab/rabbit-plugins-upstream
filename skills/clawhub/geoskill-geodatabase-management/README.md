# Geodatabase Management (geoskill-geodatabase-management)

> Create tables, import vector features, build spatial indexes and run spatial queries in a GeoPackage.

---

## 1. Overview

A full spatial database management workflow around a GeoPackage (SQLite container): - **Create tables/import**: writes vector features into GeoPackage layers (GDAL/fiona ensures OGC specification compliance), with support for appending imports to existing layers. - **Spatial index**: builds an R-tree index using the SQLite built-in `rtree` virtual table (`idx_<layer>_geom`, storing the bounding rectangle of each feature), no GDAL extension required. - **Spatial queries**: two bbox query paths — indexed query (SQL overlap test against the rtree table) and brute-force scan, whose results are strictly consistent. - **Info inspection**: lists layers, feature counts and index status from `gpkg_contents`. Suitable for local spatial data management, feature-service backend prototyping and offline GIS database construction. `--synthetic` mode generates 200 random points.

## 2. Features

A full spatial database management workflow around a GeoPackage (SQLite container): - **Create tables/import**: writes vector features into GeoPackage layers (GDAL/fiona ensures OGC specification compliance), with support for appending imports to existing layers. - **Spatial index**: builds an R-tree index using the SQLite built-in `rtree` virtual table (`idx_<layer>_geom`, storing the bounding rectangle of each feature), no GDAL extension required. - **Spatial queries**: two bbox query paths — indexed query (SQL overlap test against the rtree table) and brute-force scan, whose results are strictly consistent. - **Info inspection**: lists layers, feature counts and index status from `gpkg_contents`. Suitable for local spatial data management, feature-service backend prototyping and offline GIS database construction. `--synthetic` mode generates 200 random points.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-geodatabase-management.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `database.gpkg` | GeoPackage | Layers + R-tree spatial index |
| `database_report.json` | JSON | Index stats, query consistency, layer info |
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

# 空间数据库管理（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-geodatabase-management
description: '在 GeoPackage 中建表、导入矢量要素、创建空间索引并执行空间查询。Create tables, import vector features, build spatial indexes and run spatial queries in a GeoPackage.'
---

# 空间数据库管理 | Geodatabase Management

围绕 GeoPackage（SQLite 容器）的完整空间数据库管理流程：

- **建表/导入**：把矢量要素写入 GeoPackage 图层（GDAL/fiona 保证 OGC
  规范合规），支持向已有图层追加导入。
- **空间索引**：用 SQLite 内置 `rtree` 虚拟表构建 R-tree 索引
  （`idx_<layer>_geom`，存每个要素的外包矩形），无需 GDAL 扩展。
- **空间查询**：按 bbox 提供两条查询路径——索引查询（SQL 对 rtree 表做
  overlap 判定）与暴力扫描，二者结果严格对齐。
- **信息检查**：从 `gpkg_contents` 列出图层、要素数与索引状态。

适合本地化空间数据管理、要素服务后端原型、离线 GIS 数据库构建。
`--synthetic` 模式生成 200 个随机点。

## 依赖

```bash
pip install numpy rasterio geopandas shapely fiona pyproj
```

## 使用方法

### 基本用法

```bash
python geoskill-geodatabase-management.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 1（合成数据，离线）

```bash
python geoskill-geodatabase-management.py --bbox 116.0 39.0 117.0 40.0 --synthetic --features 500 --layer cities --output-dir ./db
```

### 示例 2：把 Shapefile 导入 GeoPackage

```bash
python geoskill-geodatabase-management.py --input parcels.shp --layer parcels --output-dir ./cadastral
```

### 示例 3：导入并按图层名管理

```bash
python geoskill-geodatabase-management.py --input pois.geojson --layer amenities --output-dir ./poi_db
```

### 示例 4：大批量随机点建库

```bash
python geoskill-geodatabase-management.py --bbox 121.0 31.0 122.0 32.0 --synthetic --features 1000 --output-dir ./big_db --quiet
```

### 示例 5：小范围快速建库

```bash
python geoskill-geodatabase-management.py --bbox 116.39 39.90 116.40 39.91 --synthetic --features 50 --output-dir ./tiny
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `database.gpkg` | GeoPackage | 含图层 + R-tree 空间索引 |
| `database_report.json` | JSON | 索引统计、查询一致性、图层信息 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- `--input`：本地矢量文件
- `--synthetic`：本地生成随机点集

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
