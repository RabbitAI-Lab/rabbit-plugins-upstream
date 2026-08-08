---
name: renewable-energy-site-selection
description: >
  Multi-criteria site selection for solar PV and wind projects.
  Applies hard constraints (slope, water, protected areas) and
  weighted suitability analysis. Use when screening for renewable
  energy development zones or comparing site alternatives.
---

# Renewable Energy Site Selection

GIS-based multi-criteria suitability analysis for solar and wind projects.

## Trigger

Use when the user wants to:
- Screen for solar PV or wind farm sites
- Compare renewable energy development zones
- Estimate potential installed capacity
- Apply constraints (slope, land cover, protected areas)

## CLI Usage

```bash
# Solar site selection
python scripts/renewable_energy_site_selection.py \
  --resource-raster ghi.tif \
  --slope-raster slope.tif \
  --land-cover landcover.tif \
  --technology solar

# Wind with constraints
python scripts/renewable_energy_site_selection.py \
  --resource-raster wind_speed.tif \
  --slope-raster slope.tif \
  --land-cover landcover.tif \
  --water-mask water.tif \
  --protected-mask protected.tif \
  --technology wind

# Custom weights
python scripts/renewable_energy_site_selection.py \
  --resource-raster ghi.tif \
  --slope-raster slope.tif \
  --land-cover landcover.tif \
  --weights '{"resource":0.5,"slope":0.15,"grid_distance":0.2,"land_cover":0.15}'
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--resource-raster` | required | Solar GHI (W/m²) or wind speed (m/s) |
| `--slope-raster` | required | Slope in degrees |
| `--land-cover` | required | Land cover classification raster |
| `--water-mask` | None | Water body mask (1=water) |
| `--protected-mask` | None | Protected area mask (1=protected) |
| `--grid-distance` | None | Distance to grid (m) |
| `--technology` | solar | solar or wind |
| `--weights` | JSON | Factor weights |
| `--max-slope` | 15 | Max slope (degrees) |
| `--suitability-threshold` | 0.6 | Min score for candidates |
| `--min-area` | 10000 | Min site area (m²) |
| `--capacity-density` | auto | MW/km² (solar=40, wind=8) |
| `--output-dir` | ./energy-site-output | Output directory |

## Output

| File | Description |
|---|---|
| `suitability.tif` | Suitability score raster [0, 1] |
| `candidate_sites.geojson` | Candidate site polygons with capacity |
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

本 skill 可自动从 NASA POWER 下载数据 (无需 API key):

```bash
python renewable_energy_site_selection.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--image`) 时，skill 自动下载数据。
当用户给 `--image` 时，走原文件路径 (向后兼容)。
