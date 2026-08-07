# Agricultural Subsidy Remote Sensing Verification (geoskill-agriculture-subsidy-verification)

> Verifies subsidy compliance by overlaying high-resolution crop classification on declared parcels for difference detection.

---

## 1. Overview

Uses an NDVI raster derived from remote sensing imagery to perform crop/non-crop threshold classification, overlays it with the vector parcels declared for subsidy, computes the "remotely measured crop fraction" per parcel, and compares it with the "declared crop fraction"; parcels exceeding the tolerance are flagged as suspected violations (over-declared / under-declared). This is a simplified implementation of the area-consistency check used in the EU CAP "Checks by Monitoring" and in cultivated-land subsidy verification in various countries. Two verification methods: - `area-diff` (default): flag when |measured fraction − declared fraction| > tolerance; - `class-match`: binarize both declared and measured values into "crop/non-crop" with a 0.5 threshold, and flag when the classes disagree. Data quality rules: NoData pixels are excluded from statistics; parcels without valid pixels (or parcels smaller than a pixel that were not burned in) are recorded as `no-coverage` and are **not** flagged as violations; NDVI values are validated against [-1,1]; bbox crossing the 180° meridian is not supported.

## 2. Features

Uses an NDVI raster derived from remote sensing imagery to perform crop/non-crop threshold classification, overlays it with the vector parcels declared for subsidy, computes the "remotely measured crop fraction" per parcel, and compares it with the "declared crop fraction"; parcels exceeding the tolerance are flagged as suspected violations (over-declared / under-declared). This is a simplified implementation of the area-consistency check used in the EU CAP "Checks by Monitoring" and in cultivated-land subsidy verification in various countries. Two verification methods: - `area-diff` (default): flag when |measured fraction − declared fraction| > tolerance; - `class-match`: binarize both declared and measured values into "crop/non-crop" with a 0.5 threshold, and flag when the classes disagree. Data quality rules: NoData pixels are excluded from statistics; parcels without valid pixels (or parcels smaller than a pixel that were not burned in) are recorded as `no-coverage` and are **not** flagged as violations; NDVI values are validated against [-1,1]; bbox crossing the 180° meridian is not supported.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-agriculture-subsidy-verification.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `crop_mask.tif` | GeoTIFF | Crop mask (1=crop, 0=non-crop, NoData areas are nodata) |
| `parcel_grid.tif` | GeoTIFF | Parcel ID raster (background 0, parcels starting at 1) |
| `verification_report.json` | JSON | Per-parcel verification records and statistics (primary output) |
| `flagged_parcels.geojson` | GeoJSON | Vector of suspected non-compliant parcels |
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

# 农业补贴遥感核查（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

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
