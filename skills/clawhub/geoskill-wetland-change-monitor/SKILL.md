---
name: wetland-change-monitor
description: >
  Monitor wetland extent, inundation frequency, and land cover transitions
  to identify degradation, recovery, and human encroachment. Use when the
  user wants to track wetland changes over time, assess wetland health,
  or detect conversion of wetlands to other land covers.
---

# Wetland Change Monitor

Monitors wetland extent, inundation frequency, and land cover transitions
from multi-year water occurrence rasters. Identifies degradation, recovery,
and human encroachment patterns.

## CLI Usage

```bash
python scripts/wetland_change_monitor.py --water-frequency water_freq.tif --years 2015 2016 2017 2018 2019
python scripts/wetland_change_monitor.py --water-frequency wf.tif --years 2018 2019 2020 --frequency-thresholds 0.25 0.75
python scripts/wetland_change_monitor.py --water-masks masks.tif --years 2015 2020 --change-schema degradation recovery stable
```

## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载水体数据 (无需 API key):

```bash
# 自动下载 JRC GSW (water frequency) + Sentinel-1 GRD (water mask)
python scripts/wetland_change_monitor.py \
    --bbox 116.30,39.85,116.45,39.95 \
    --date-range 2020-06-01,2020-09-30 \
    --years 2015 2020 \
    --output-dir ./wcm-auto
```

下载的内容:
- **JRC Global Surface Water** (`jrc-gsw`) — 历史水体频率，替换 `--water-frequency`
- **Sentinel-1 GRD** (`sentinel-1-grd`) — SAR 水体掩膜，替换 `--water-masks`

下载元数据（`data_source`, `fetched_at`, `collection`, `jrc_downloaded`, `sentinel1_downloaded`）会写入 `output-manifest.json`。

## Parameters

| Parameter | Description |
|---|---|
| `--water-frequency` | Multi-band water frequency raster (JRC-style, bands = years) |
| `--water-masks` | Alternative: multi-band binary water masks (1=water, 0=dry) |
| `--years` | List of years corresponding to bands |
| `--frequency-thresholds` | Two thresholds for classification (default: 0.25 0.75) |
| `--change-schema` | Change types to detect (default: degradation recovery stable) |
| `--include-sar` | Include SAR-based water detection (optional) |
| `--min-area` | Minimum patch area in hectares (default: 0.5) |
| `--output-dir` | Output directory (default: wetland-output) |

## Output

| File | Description |
|---|---|
| `wetland_type.tif` | Wetland type classification raster |
| `inundation_frequency.tif` | Inundation frequency raster (0-1) |
| `wetland_change.geojson` | Vectorized change patches with type and confidence |
| `transition_matrix.csv` | Year-to-year transition matrix |
| `wetland-report.json` | Detailed statistics and summary |
| `output-manifest.json` | Machine-readable manifest |

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
python wetland_change_monitor.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--image`) 时，skill 自动下载数据。
当用户给 `--image` 时，走原文件路径 (向后兼容)。
