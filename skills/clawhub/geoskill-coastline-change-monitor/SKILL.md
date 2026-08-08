---
name: coastline-change-monitor
description: >
  Multi-temporal shoreline change rate analysis. Generates transects,
  computes Endpoint Rate (EPR) and Linear Regression Rate (LRR),
  and identifies erosion hotspots. Use when monitoring coastline
  retreat/accretion or identifying erosion-prone segments.
---

# Coastline Change Monitor

Multi-temporal shoreline change analysis with transect-based rate computation.

## Trigger

Use when the user wants to:
- Monitor coastline erosion/accretion over time
- Compute shoreline change rates (EPR/LRR)
- Identify erosion hotspots
- Compare shoreline positions across years

## CLI Usage

```bash
# Vector shorelines
python scripts/coastline_change_monitor.py \
  --shoreline-files shore_2015.geojson shore_018.geojson shore_2021.geojson \
  --years 2015 2018 2021

# Raster water masks
python scripts/coastline_change_monitor.py \
  --shoreline-files water_2015.tif water_2018.tif water_2021.tif \
  --years 2015 2018 2021 \
  --transect-spacing 50 --transect-length 300
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--shoreline-files` | required | Shoreline files (one per year) |
| `--years` | auto | Years for each file |
| `--transect-spacing` | 100 | Spacing between transects |
| `--transect-length` | 500 | Length of each transect |
| `--erosion-threshold` | -1.0 | EPR threshold for hotspots (m/yr) |
| `--output-dir` | ./coastline-output | Output directory |

## Output

| File | Description |
|---|---|
| `shorelines.geojson` | All shorelines with year attribute |
| `transects.geojson` | Generated transect lines |
| `change_rates.csv` | EPR/LRR per transect |
| `erosion_hotspots.geojson` | Significant erosion segments |
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
python coastline_change_monitor.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--image`) 时，skill 自动下载数据。
当用户给 `--image` 时，走原文件路径 (向后兼容)。
