---
name: agricultural-disaster-assessment
description: >
  Fuses crop distribution, hazard intensity, and NDVI anomaly to
  estimate agricultural disaster impact. Classifies damage severity
  (mild/moderate/severe) and generates field-level damage maps.
  Use when assessing flood/drought/heat impact on crops.
---

# Agricultural Disaster Assessment

Estimates crop damage by combining hazard intensity with vegetation anomaly.

## Trigger

Use when the user wants to:
- Assess flood/drought/heat impact on crops
- Map agricultural disaster severity
- Generate field-level damage estimates
- Prioritize inspection areas after a disaster

## CLI Usage

```bash
# Basic assessment
python scripts/agricultural_disaster_assessment.py \
  --crop-map crops.tif \
  --hazard-raster flood_depth.tif \
  --baseline-ndvi ndvi_normal.tif \
  --post-ndvi ndvi_post.tif

# With custom thresholds
python scripts/agricultural_disaster_assessment.py \
  --crop-map crops.tif \
  --hazard-raster drought_spi.tif \
  --baseline-ndvi ndvi_normal.tif \
  --post-ndvi ndvi_post.tif \
  --hazard-threshold 0.5 --anomaly-threshold -0.4
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--crop-map` | required | Crop distribution raster (1=crop) |
| `--hazard-raster` | required | Hazard intensity (flood depth, SPI, etc.) |
| `--baseline-ndvi` | required | Normal-year NDVI |
| `--post-ndvi` | required | Post-disaster NDVI |
| `--hazard-threshold` | 0.3 | Hazard intensity threshold |
| `--anomaly-threshold` | -0.3 | NDVI anomaly threshold |
| `--min-area` | 0 | Minimum field area filter |
| `--output-dir` | ./disaster-output | Output directory |

## Output

| File | Description |
|---|---|
| `affected_crops.tif` | Damage level raster (0-4) |
| `field_damage.geojson` | Damaged field polygons |
| `report.html` | HTML summary report |
| `output-manifest.json` | Machine-readable manifest |

## Damage Levels

| Level | Label | Meaning |
|---|---|---|
| 0 | no crop | Not a crop pixel |
| 1 | no damage | Hazard below threshold |
| 2 | mild | Slight NDVI reduction |
| 3 | moderate | Significant NDVI reduction |
| 4 | severe | Major NDVI reduction + high hazard |

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python agricultural_disaster_assessment.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--image`) 时，skill 自动下载数据。
当用户给 `--image` 时，走原文件路径 (向后兼容)。
