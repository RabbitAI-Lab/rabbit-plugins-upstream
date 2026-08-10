---
name: geoskill-agriculture-subsidy-verification
description: '高分辨率作物识别叠加申报地块做差异检测，核查补贴合规性。Verifies subsidy compliance by overlaying high-resolution crop classification on declared parcels for difference detection.'
---

# 农业补贴遥感核查 | Agriculture Subsidy Verification

Uses an NDVI raster derived from remote sensing imagery to classify crop/non-crop by threshold, overlays it with the vector parcels declared for subsidy, computes the "remotely sensed crop fraction" per parcel, and compares it with the "declared crop fraction": parcels exceeding the tolerance are flagged as suspected violations (over-declared / under-declared). This is a simplified implementation of the area-consistency check used in the EU CAP "Checks by Monitoring" and in national cropland subsidy verification.

Two verification methods:

- `area-diff` (default): flagged when |measured fraction − declared fraction| > tolerance;
- `class-match`: binarizes declared/measured fractions into "crop/non-crop" at the 0.5 boundary, flagged when classes do not match.

Data quality rules: NoData pixels are excluded from statistics; parcels with no valid pixels inside (or parcels smaller than the pixel and thus not burned in) are recorded as `no-coverage` and are **not** flagged as violations; NDVI values are validated to [-1,1]; bbox does not support crossing the 180° meridian.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'geopandas' 'shapely'
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-agriculture-subsidy-verification.py --bbox 116.0 39.0 117.0 40.0 [other parameters]
```

### Example 1 (Synthetic Data, Offline)

```bash
python geoskill-agriculture-subsidy-verification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（真实 NDVI + 申报地块）

```bash
python geoskill-agriculture-subsidy-verification.py --input ndvi.tif --parcels parcels.geojson --output-dir ./out
```

### Example 3 (Class Matching + Custom Tolerance)

```bash
python geoskill-agriculture-subsidy-verification.py --input ndvi.tif --parcels parcels.geojson --method class-match --tolerance 0.1
```

### 示例 4（调整 NDVI 阈值）

```bash
python geoskill-agriculture-subsidy-verification.py --input ndvi.tif --parcels parcels.geojson --threshold 0.35
```

### Example 5 (Projected Coordinate Input with Auto-Reprojection)

```bash
python geoskill-agriculture-subsidy-verification.py --input ndvi_utm.tif --parcels parcels_utm.gpkg --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `crop_mask.tif` | GeoTIFF | Crop mask (1=crop, 0=non-crop, nodata in NoData areas) |
| `parcel_grid.tif` | GeoTIFF | Parcel ID raster (background 0, parcels start from 1) |
| `verification_report.json` | JSON | Per-parcel verification records and statistics (primary output) |
| `flagged_parcels.geojson` | GeoJSON | Vector of suspected violation parcels |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

Local high-resolution NDVI GeoTIFF (EPSG:4326; projected coordinates are automatically reprojected) + declared parcel vectors (GeoJSON/GPKG/Shapefile, must contain `parcel_id` and `declared_crop_frac` columns, with declared fraction in [0,1]); `--synthetic` mode simulates offline without network.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; user data is never uploaded.

## License / License

MIT

---


<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-agriculture-subsidy-verification
description: '高分辨率作物识别叠加申报地块做差异检测，核查补贴合规性。Verifies subsidy compliance by overlaying high-resolution crop classification on declared parcels for difference detection.'
---

# 农业补贴遥感核查 | Agriculture Subsidy Verification

用遥感影像派生的 NDVI 栅格做作物/非作物阈值分类，与申报补贴的地块矢量叠加，
逐地块计算"遥感实测作物占比"，与"申报作物占比"比较，超过容差即标记为疑似违规
（虚报 over-declared / 少报 under-declared）。这是欧盟 CAP "Checks by Monitoring"
与各国耕地补贴核查中面积一致性检查的简化实现。

两种核查方法：

- `area-diff`（默认）：|实测占比 − 申报占比| > tolerance 即标记；
- `class-match`：以 0.5 为界把申报/实测二值化为"作物/非作物"，类别不一致即标记。

数据质量规则：NoData 像元不参与统计；地块内无有效像元（或地块小于像元未被烧录）
记为 `no-coverage`，**不**判定违规；NDVI 值域校验 [-1,1]；bbox 不支持跨 180° 经线。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'geopandas' 'shapely'
```

## 使用方法

### 基本用法

```bash
python geoskill-agriculture-subsidy-verification.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例 1（合成数据，离线）

```bash
python geoskill-agriculture-subsidy-verification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（真实 NDVI + 申报地块）

```bash
python geoskill-agriculture-subsidy-verification.py --input ndvi.tif --parcels parcels.geojson --output-dir ./out
```

### 示例 3（类别匹配法 + 自定义容差）

```bash
python geoskill-agriculture-subsidy-verification.py --input ndvi.tif --parcels parcels.geojson --method class-match --tolerance 0.1
```

### 示例 4（调整 NDVI 阈值）

```bash
python geoskill-agriculture-subsidy-verification.py --input ndvi.tif --parcels parcels.geojson --threshold 0.35
```

### 示例 5（投影坐标输入自动重投影）

```bash
python geoskill-agriculture-subsidy-verification.py --input ndvi_utm.tif --parcels parcels_utm.gpkg --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `crop_mask.tif` | GeoTIFF | 作物掩膜（1=作物，0=非作物，NoData 区域为 nodata） |
| `parcel_grid.tif` | GeoTIFF | 地块编号栅格（背景 0，地块从 1 起） |
| `verification_report.json` | JSON | 逐地块核查记录与统计（主产物） |
| `flagged_parcels.geojson` | GeoJSON | 疑似违规地块矢量 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地高分辨率 NDVI GeoTIFF（EPSG:4326；投影坐标自动重投影）+ 申报地块矢量
（GeoJSON/GPKG/Shapefile，需含 `parcel_id` 与 `declared_crop_frac` 列，
申报占比取值 [0,1]）；`--synthetic` 模式离线模拟，无需网络。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
