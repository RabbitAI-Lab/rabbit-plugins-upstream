---
name: mine-disturbance-monitor
description: >
  Monitor surface disturbance at mining sites using multi-temporal optical/SAR/DEM data. Detect bare land, pits, dumps, roads,
  and vegetation removal. Track disturbance objects across years, identify boundary violations, and generate area statistics.
---

# Mine Disturbance Monitor

Monitor surface disturbance at mining sites using multi-temporal optical/SAR/DEM data. Detect bare land, pits, dumps, roads, and vegetation removal. Track disturbance objects across years, identify disturbances outside mine boundaries (compliance concern), and generate area statistics with evidence.

## Trigger

Use when the user wants to:
- Monitor mine surface disturbance over multiple years
- Detect bare land / pit / dump / road / vegetation removal expansion
- Identify disturbances outside mine permit boundaries
- Track disturbance object status (new / expanding / stable / reclaimed)
- Generate disturbance area statistics by year and type

## CLI Usage

```bash
python scripts/mine_disturbance_monitor.py \
  --mine-boundary mine_boundary.geojson \
  --years 2020 2021 2022 2023 \
  --image-dir ./imagery \
  --disturbance-types pit dump road bare \
  --min-area 100 \
  --buffer 500 \
  --output-dir ./disturbance-output
```

## Parameters

| Parameter | Required | Default | Description |
|---|---|---|---|
| `--mine-boundary` | Yes | — | Mine permit boundary (GeoJSON) |
| `--years` | Yes | — | List of years to analyze |
| `--image-dir` | Yes | — | Directory with per-year imagery (YYYY.tif) |
| `--disturbance-types` | No | pit dump road bare | Disturbance types to detect |
| `--compare-dem` | No | — | Optional DEM for pit/dump classification |
| `--min-area` | No | 100 | Minimum disturbance area (m²) |
| `--buffer` | No | 0 | Buffer distance around boundary (m) |
| `--output-dir` | No | disturbance-output | Output directory |
| `--version` | No | — | Show version |

## Output

| File | Description |
|---|---|
| `disturbance_by_year.geojson` | All disturbance objects with year, type, area, status |
| `disturbance_type.tif` | Raster map of disturbance types |
| `outside_boundary.geojson` | Disturbances outside mine boundary (compliance) |
| `summary.xlsx` | Area statistics by year and type |

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Validation error |
| 7 | Processing failure |


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python mine_disturbance_monitor.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--image`) 时，skill 自动下载数据。
当用户给 `--image` 时，走原文件路径 (向后兼容)。
