---
name: rooftop-solar-inventory
description: >
  Inventory building rooftop solar potential: available area, slope/aspect,
  shading, and PV capacity/energy yield/economic viability.
  Outputs building-level candidate rankings for solar deployment.
---

# Rooftop Solar Inventory

Assesses building-level rooftop solar potential by extracting roof planes,
computing slope/aspect and shading, deducting setbacks and obstacles,
and estimating installed capacity, annual energy yield, and economics.

## Trigger

Use when the user wants to:
- Calculate solar PV capacity for a portfolio of buildings
- Identify high-potential rooftops without shading issues
- Rank buildings by solar economic viability
- Generate rooftop solar candidate lists for feasibility studies
- Estimate annual energy yield and financial returns for rooftop PV

## CLI Usage

```bash
# Basic analysis with synthetic demo data
python scripts/rooftop_solar_inventory.py --output-dir ./rsi-output

# With custom setback and panel type
python scripts/rooftop_solar_inventory.py \
  --setback 1.5 \
  --panel-type hjt_700w \
  --output-dir ./rsi-output

# With custom economic parameters
python scripts/rooftop_solar_inventory.py \
  --electricity-price 0.65 \
  --annual-ghi 1600 \
  --system-lifetime 30 \
  --output-dir ./rsi-output

# With building footprints file
python scripts/rooftop_solar_inventory.py \
  --buildings ./data/buildings.geojson \
  --dsm ./data/dsm.tif \
  --output-dir ./rsi-output
```

## 数据下载

本 skill 可自动从 Microsoft Planetary Computer + NASA POWER 下载数据 (无需 API key):

```bash
# 自动下载 MS Buildings 建筑足迹 + NASA POWER GHI 太阳辐射
python scripts/rooftop_solar_inventory.py \
    --bbox 116.38,39.90,116.42,39.94 \
    --date-range 2024-06-01,2024-06-30 \
    --output-dir ./rsi-auto
```

下载的内容:
- **MS Buildings** (`ms-buildings` collection on MPC) — 建筑足迹，替换 `--buildings`
- **NASA POWER GHI** (`ALLSKY_SFC_SW_DWN`) — 日均太阳辐照度，写入 `nasa_power_ghi.csv`，并自动计算 annual GHI 替换默认值

下载元数据（`data_source`, `fetched_at`, `collection`, `nasa_power_path`）会写入 `output-manifest.json`。

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--buildings` | None | Building footprints (GeoJSON/Shapefile) |
| `--dsm` | None | Digital Surface Model GeoTIFF |
| `--point-cloud` | None | Point cloud file (LAS/LAZ) |
| `--setback` | 1.0 | Edge setback in meters |
| `--panel-type` | mono_perc_540w | Panel type: mono_perc_540w, mono_perc_600w, hjt_700w |
| `--min-contiguous-area` | 10.0 | Minimum contiguous area in m2 |
| `--annual-ghi` | 1400 | Annual Global Horizontal Irradiance in kWh/m2 |
| `--performance-ratio` | 0.82 | System performance ratio |
| `--electricity-price` | 0.55 | Electricity price in CNY/kWh |
| `--discount-rate` | 0.06 | Discount rate for NPV calculation |
| `--system-lifetime` | 25 | System lifetime in years |
| `--output-dir` | ./rsi-output | Output directory |

## Output

| File | Description |
|---|---|
| `roof_planes.geojson` | Roof plane polygons with slope, aspect, area |
| `solar_candidates.geojson` | Candidate buildings with solar potential |
| `building_potential.csv` | Ranked building-level results table |
| `shading.tif` | Shading mask (requires DSM input) |
| `request.json` | Analysis request metadata |
| `dataset-manifest.json` | Dataset inventory |
| `output-manifest.json` | Output file inventory and statistics |
| `qa.json` | Quality assurance checks |
| `run.log` | Execution log |

## Quality Codes

| Code | Name | Description |
|---|---|---|
| 1 | high | DSM-based segmentation, reliable geometry |
| 2 | medium | Mixed data sources, acceptable confidence |
| 3 | low | No DSM, assumed flat roof |
| 4 | invalid | Processing error or invalid geometry |

## Roof Type Codes

| Code | Name | Description |
|---|---|---|
| 0 | flat | Slope < 5° |
| 1 | single_slope | Single inclined plane |
| 2 | gable | Two-slope gable roof |
| 3 | complex | Multi-plane or steep (>45°) |

## Key Algorithms

### Roof Plane Extraction
Without DSM: assumes flat roof (single plane = building footprint), marked low confidence.
With DSM: segments roof using slope/aspect clustering on connected components.

### Slope and Aspect
Computed from DSM using numpy gradient method:
- slope = arctan(sqrt(gx^2 + gy^2))
- aspect = atan2(-gx, gy) mapped to 0-360°

### Shading
Ray-casting from each pixel toward sun position. A pixel is shaded if terrain
blocks the sun at the given azimuth/altitude. Supports multi-pass annual shading.

### Usable Area
Subtracts edge setback (negative buffer), obstacles, and filters by minimum
contiguous area. Handles MultiPolygon by taking largest component.

### Solar Potential
- Capacity: n_panels = usable_area / (panel_area * (1 + spacing_ratio))
- Energy: E = capacity * GHI * PR * orientation_factor * (1 - shading)
- Economics: NPV, LCOE, payback period over system lifetime

### Building Ranking
Composite score (0-1) based on:
- Installed capacity (40%)
- Economic NPV (30%)
- Specific yield (30%)

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |

## Limitations

- Without DSM, all roofs assumed flat (low confidence)
- Shading computation is simplified (single sun position or coarse multi-pass)
- Structural suitability, roof loading, and ownership not assessed
- Economic results are indicative; actual costs vary by project
- Results are auxiliary analysis only; engineering decisions require manual review

## References

- PVWatts Calculator (NREL)
- IEC 61724-1: Photovoltaic system performance monitoring
- China PV Industry Association (CPIA) annual reports


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python rooftop_solar_inventory.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--buildings`) 时，skill 自动下载数据。
当用户给 `--buildings` 时，走原文件路径 (向后兼容)。
