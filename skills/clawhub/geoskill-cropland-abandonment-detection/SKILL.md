---
name: cropland-abandonment-detection
description: >
  Multi-year cropland abandonment detection using NDVI time series.
  Identifies suspected abandoned cropland based on consecutive years
  without cultivation signals. Use when screening for abandoned fields,
  generating field verification lists, or monitoring cultivation continuity.
---

# Cropland Abandonment Detection

Detects suspected abandoned cropland from multi-year NDVI time series.

## Trigger

Use when the user wants to:
- Screen for abandoned cropland
- Identify fields with consecutive years without cultivation
- Generate field verification priorities
- Monitor cultivation continuity

## CLI Usage

```bash
# Basic detection
python scripts/cropland_abandonment_detection.py \
  --ndvi-stack ndvi_2018_2023.tif

# With cropland mask and custom thresholds
python scripts/cropland_abandonment_detection.py \
  --ndvi-stack ndvi_2018_2023.tif \
  --cropland-mask cropland.tif \
  --ndvi-threshold 0.25 --min-abandoned-years 3

# Specify years
python scripts/cropland_abandonment_detection.py \
  --ndvi-stack ndvi_stack.tif \
  --years 2018 2019 2020 2021 2022 2023

# Synthetic demo (no real stack/mask needed)
python scripts/cropland_abandonment_detection.py --synthetic --output-dir ./abandonment-output
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--ndvi-stack` | (required unless `--synthetic`) | Multi-year NDVI stack (bands=years) |
| `--cropland-mask` | None | Cropland mask (1=cropland) |
| `--years` | auto | Years for each band |
| `--ndvi-threshold` | 0.3 | Min max-NDVI for cultivation |
| `--min-abandoned-years` | 2 | Min consecutive fallow years |
| `--min-area` | 0 | Minimum field area filter |
| `--output-dir` | ./abandonment-output | Output directory |
| `--synthetic` | false | Run with synthetic demo data (auto-generates NDVI stack + mask) |

## Output

| File | Description |
|---|---|
| `abandonment_status.tif` | 3-band raster (abandoned, duration, start_year) |
| `suspected_fields.geojson` | Vector of abandoned field polygons |
| `report.html` | HTML summary report |
| `output-manifest.json` | Machine-readable manifest |

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
python cropland_abandonment_detection.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--image`) 时，skill 自动下载数据。
当用户给 `--image` 时，走原文件路径 (向后兼容)。
