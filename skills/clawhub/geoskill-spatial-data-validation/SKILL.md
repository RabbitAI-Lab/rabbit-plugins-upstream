---
name: geoskill-spatial-data-validation
description: '检查矢量几何有效性、拓扑错误、属性完整性与 CRS 一致性，输出分级质量报告。Validate geometry validity, topology, attribute completeness and CRS consistency for vector data and emit a graded quality report.'
---

# 空间数据质量验证 | Spatial Data Validation

Performs four-dimensional quality validation on vector data: **geometry validity** (shapely checks each feature for self-intersection, ring self-intersection, empty geometries, and null geometries, with reasons given), **topology checks** (duplicate geometry counts, pairwise polygon overlap detection), **attribute completeness** (null-value ratio per required field), and **CRS consistency** (actual EPSG compared against the expected value).

The four dimensions are combined by weights (geometry 0.40 / topology 0.20 / attributes 0.25 / CRS 0.15) into a 0–1 composite score, mapped to A–F grades, and invalid geometry features are exported as GeoJSON for manual review. Suitable for pre-load quality control, deliverable acceptance, and self-checks before data submission.

`--synthetic` mode generates features with intentionally planted defects (bowtie self-intersecting polygons, null geometries, missing attributes), reproducing all defect-detection paths offline.

## Dependencies / 依赖

```bash
pip install numpy rasterio geopandas shapely fiona pyproj
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-spatial-data-validation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 1 (Synthetic Data, Offline)

```bash
python geoskill-spatial-data-validation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2：验证 Shapefile

```bash
python geoskill-spatial-data-validation.py --input parcels.shp --crs EPSG:4326 --output-dir ./report
```

### Example 3: Custom Required Attribute Fields

```bash
python geoskill-spatial-data-validation.py --input buildings.gpkg --fields id,name,height,type --output-dir ./r2
```

### 示例 4：验证 GeoPackage 并检查投影一致性

```bash
python geoskill-spatial-data-validation.py --input roads.gpkg --crs EPSG:3857 --output-dir ./r3
```

### Example 5: Silent Quality Check

```bash
python geoskill-spatial-data-validation.py --input data.geojson --quiet --output-dir ./r4
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `validation_report.json` | JSON | Four-dimension check results, composite score and grade |
| `invalid_geometries.geojson` | GeoJSON | Invalid geometry features (for review) |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- `--input`: local vector file (any OGR format)
- `--synthetic`: locally generates defective test features

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
