# Spatial Data Validation (geoskill-spatial-data-validation)

> Validates geometry validity, topology, attribute completeness and CRS consistency for vector data and emits a graded quality report

---

## 1. Overview

Performs quality validation on vector data across four dimensions: **geometry validity** (per-feature detection of self-intersection, ring self-intersection, empty geometry and null geometry with reasons, using shapely), **topology checks** (duplicate geometry counts, pairwise polygon overlap detection), **attribute completeness** (null-value ratio per required field) and **CRS consistency** (actual EPSG vs. expected). The four dimensions are combined by weights (geometry 0.40 / topology 0.20 / attribute 0.25 / CRS 0.15) into a 0–1 composite score mapped to an A–F grade, and invalid geometry features are exported to GeoJSON for manual review. Suitable for pre-ingestion quality control, deliverable acceptance and self-checks before data submission. The `--synthetic` mode generates features with deliberately injected defects (bowtie self-intersecting polygons, null geometries, missing attributes), reproducing all defect-detection paths offline.

## 2. Features

Performs quality validation on vector data across four dimensions: **geometry validity** (per-feature detection of self-intersection, ring self-intersection, empty geometry and null geometry with reasons, using shapely), **topology checks** (duplicate geometry counts, pairwise polygon overlap detection), **attribute completeness** (null-value ratio per required field) and **CRS consistency** (actual EPSG vs. expected). The four dimensions are combined by weights (geometry 0.40 / topology 0.20 / attribute 0.25 / CRS 0.15) into a 0–1 composite score mapped to an A–F grade, and invalid geometry features are exported to GeoJSON for manual review. Suitable for pre-ingestion quality control, deliverable acceptance and self-checks before data submission. The `--synthetic` mode generates features with deliberately injected defects (bowtie self-intersecting polygons, null geometries, missing attributes), reproducing all defect-detection paths offline.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-spatial-data-validation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `validation_report.json` | JSON | Four-dimensional check results, composite score and grade |
| `invalid_geometries.geojson` | GeoJSON | Invalid geometry features (for review) |
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

# 空间数据质量验证（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-spatial-data-validation
description: '检查矢量几何有效性、拓扑错误、属性完整性与 CRS 一致性，输出分级质量报告。Validate geometry validity, topology, attribute completeness and CRS consistency for vector data and emit a graded quality report.'
---

# 空间数据质量验证 | Spatial Data Validation

对矢量数据执行四个维度的质量验证：**几何有效性**（shapely 逐要素判定
self-intersection、ring 自交、空几何、null 几何并给出原因）、**拓扑检查**
（重复几何计数、多边形两两重叠检测）、**属性完整性**（逐必填字段统计
空值比例）、**CRS 一致性**（实际 EPSG 与期望值比对）。

四个维度按权重（几何 0.40 / 拓扑 0.20 / 属性 0.25 / CRS 0.15）合成
0-1 综合评分，映射为 A-F 等级，并把无效几何要素导出为 GeoJSON 供人工
复核。适合数据入库质检、成果验收、数据汇交前自检。

`--synthetic` 模式生成含刻意缺陷的要素（bowtie 自相交多边形、null 几何、
缺失属性），可离线复现全部缺陷检出路径。

## 依赖

```bash
pip install numpy rasterio geopandas shapely fiona pyproj
```

## 使用方法

### 基本用法

```bash
python geoskill-spatial-data-validation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 1（合成数据，离线）

```bash
python geoskill-spatial-data-validation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2：验证 Shapefile

```bash
python geoskill-spatial-data-validation.py --input parcels.shp --crs EPSG:4326 --output-dir ./report
```

### 示例 3：自定义必填属性字段

```bash
python geoskill-spatial-data-validation.py --input buildings.gpkg --fields id,name,height,type --output-dir ./r2
```

### 示例 4：验证 GeoPackage 并检查投影一致性

```bash
python geoskill-spatial-data-validation.py --input roads.gpkg --crs EPSG:3857 --output-dir ./r3
```

### 示例 5：静默质检

```bash
python geoskill-spatial-data-validation.py --input data.geojson --quiet --output-dir ./r4
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `validation_report.json` | JSON | 四维检查结果、综合评分与等级 |
| `invalid_geometries.geojson` | GeoJSON | 无效几何要素（供复核） |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- `--input`：本地矢量文件（任意 OGR 格式）
- `--synthetic`：本地生成含缺陷的测试要素

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
