---
name: crop-type-mapping
description: >
  Identify major crop types from multi-temporal optical/SAR imagery using
  phenological features. Produces pixel/field-level classification, area
  statistics, and confidence maps. Use when mapping crop distributions,
  estimating planted areas, or generating agricultural intelligence from
  remote sensing data.
---

## Prerequisites / 先准备 X 文件

> ⚠️ **必读** — 本 skill 不属于即用型，需要先准备特定文件才能跑。

本 skill 需要 **bbox/AOI + 年份/日期范围**。时序影像自动下载，但 **训练标签和物候 schema 是可选的**——内置 4 种作物（水稻/小麦/玉米/大豆）够用。

👉 完整教程见仓库根目录 `PREREQUISITES.md` 1.2 节。

**先准备 X 文件**：自动下载 + 内置物候 = 1 行命令可跑通。

快速试跑命令：

```bash
python crop_type_mapping.py --bbox 113.0,29.5,114.5,31.0 --year 2024 --output-dir ./ctm
```


# Crop Type Mapping

Identifies major crop types (rice, wheat, corn, etc.) from multi-temporal
satellite imagery using phenological curve matching and spectral indices.

## Trigger

Use when the user wants to:
- Map crop type distribution for a region (e.g., "identify rice/wheat/corn in Henan 2024")
- Estimate planted area by crop type with confidence intervals
- Generate crop classification maps from Sentinel-2/Landsat time series
- Compare crop patterns across years or regions
- Produce agricultural intelligence reports for government or insurance

## CLI Usage

```bash
# Basic: classify crops in a bounding box for a given year
python scripts/crop_type_mapping.py \
  --bbox 113.0,29.5,114.5,31.0 \
  --year 2024

# Using a place name
python scripts/crop_type_mapping.py \
  --place beijing \
  --year 2024

# With custom date range and output directory
python scripts/crop_type_mapping.py \
  --bbox 115.0,30.0,116.0,31.0 \
  --start-date 2024-04-01 \
  --end-date 2024-10-31 \
  --output-dir ./ctm-output

# With custom crop schema and method
python scripts/crop_type_mapping.py \
  --aoi-file region.geojson \
  --year 2024 \
  --crop-schema references/crop_phenology.json \
  --method rule \
  --min-patch-area 9
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--place` | — | Place name (e.g., 'beijing', 'shanghai') |
| `--bbox` | — | Bounding box: 'xmin,ymin,xmax,ymax' (WGS84) |
| `--aoi-file` | — | AOI file (GeoJSON or Shapefile) |
| `--year` | current | Year for analysis (2015-2030) |
| `--start-date` | — | Start date (YYYY-MM-DD), mutually exclusive with --year |
| `--end-date` | — | End date (YYYY-MM-DD) |
| `--crop-schema` | built-in | Custom crop phenology schema JSON |
| `--labels` | — | Training/validation labels (GeoJSON) |
| `--method` | rule | Classification method: rule, rf, xgboost |
| `--min-observations` | 5 | Minimum valid observations per pixel |
| `--field-boundaries` | — | Field boundary polygons (GeoJSON) |
| `--min-patch-area` | 4 | Minimum patch area in pixels (post-processing) |
| `--output-dir` | ./ctm-output | Output directory |

Note: `--place`, `--bbox`, and `--aoi-file` are mutually exclusive.

## Output

| File | Description |
|---|---|
| `crop_classes.tif` | Crop classification raster (class codes) |
| `crop_confidence.tif` | Per-pixel classification confidence (0-1) |
| `crop_polygons.geojson` | Vector polygons per crop region |
| `area_by_admin.csv` | Area statistics per crop class (ha, km², %) |
| `accuracy.json` | Confusion matrix, overall accuracy, per-class F1 |
| `request.json` | Input parameters and AOI metadata |
| `dataset-manifest.json` | Data source and observation metadata |
| `output-manifest.json` | Output file inventory and summary |
| `qa.json` | Quality assurance checks and status |
| `run.log` | Execution log |

## Crop Types (Default Schema)

| Crop | Code | Peak DOY | Description |
|---|---|---|---|
| Rice | 1 | 220 (Aug) | Single-season late rice |
| Wheat | 2 | 120 (Apr) | Winter wheat |
| Corn | 3 | 200 (Jul) | Summer corn |

## Classification Methods

| Method | Description |
|---|---|
| `rule` | Phenological curve matching using peak DOY and amplitude |
| `rf` | Random Forest (requires sklearn, falls back to rule) |
| `xgboost` | XGBoost (requires sklearn, falls back to rule) |

## Workflow

1. **AOI parsing** — resolve place/bbox/aoi-file to WGS84 bounding box
2. **Time range** — parse year or custom date range
3. **Data preparation** — search/acquire Sentinel-2/Landsat time series
4. **Feature extraction** — compute NDVI, EVI, LSWI + phenological features
5. **Classification** — rule-based or ML classification per pixel
6. **Post-processing** — small patch removal, spatial smoothing
7. **Accuracy assessment** — confusion matrix, per-class metrics
8. **Area statistics** — pixel-counting with spherical area correction
9. **Output** — GeoTIFF, GeoJSON, CSV, JSON reports

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |

## Limitations

- Classification is remote-sensing-based estimation, not ground truth
- Accuracy depends on cloud-free observation count and timing
- Crop schema defaults are tuned for major grain regions (North China Plain)
- Double-cropping regions may require custom schema
- Results should be validated with ground truth before operational use


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python crop_type_mapping.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--image`) 时，skill 自动下载数据。
当用户给 `--image` 时，走原文件路径 (向后兼容)。
