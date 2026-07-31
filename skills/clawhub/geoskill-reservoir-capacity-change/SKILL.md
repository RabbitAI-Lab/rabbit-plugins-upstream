---
name: reservoir-capacity-change
description: >
  Establish level-area-storage relationships from multi-period water surface,
  DEM, and water level data. Monitor reservoir capacity change and sedimentation
  trends. Use when analyzing reservoir storage changes, estimating current
  capacity, or detecting sedimentation from area-level curve shifts.
---

# Reservoir Capacity Change

Combines multi-period water surface extent, DEM, and water level data to
establish level-area-storage relationships, monitoring capacity change and
sedimentation trends.

## Trigger

Use when the user wants to:
- Estimate current reservoir capacity from DEM and water level data
- Analyze area-level relationships over time for sedimentation signals
- Compute storage curves and their uncertainty
- Compare storage between two periods
- Generate water extent time series from DEM + water levels

## CLI Usage

```bash
# Synthetic demo mode (no input files needed)
python scripts/reservoir_capacity_change.py --output-dir ./rcc-output

# With input DEM GeoTIFF
python scripts/reservoir_capacity_change.py \
  --dem ./data/reservoir_dem.tif \
  --water-levels ./data/water_levels.csv \
  --output-dir ./rcc-output

# With bounding box for area computation
python scripts/reservoir_capacity_change.py \
  --dem ./data/dem.tif \
  --bbox 116.0 39.5 116.5 40.0 \
  --output-dir ./rcc-output

# With vertical datum specification
python scripts/reservoir_capacity_change.py \
  --dem ./data/dem.tif \
  --dem-datum WGS84 \
  --water-level-datum WGS84 \
  --confidence 0.99 \
  --mc-iterations 1000 \
  --output-dir ./rcc-output
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--dem` | None | Path to DEM GeoTIFF |
| `--water-levels` | None | Path to water levels CSV (date, level columns) |
| `--reservoir-boundary` | None | Path to reservoir boundary GeoJSON/Shapefile |
| `--place` | None | Place name for AOI lookup |
| `--bbox` | None | Bounding box: xmin ymin xmax ymax |
| `--aoi-file` | None | Path to AOI geometry file |
| `--start-date` | None | Start date (ISO 8601) |
| `--end-date` | None | End date (ISO 8601) |
| `--dates` | None | List of dates |
| `--curve-method` | trapezoidal | Curve method: trapezoidal, prism |
| `--reference-level` | None | Reference elevation level (m) |
| `--dem-error` | 5.0 | DEM vertical RMSE (meters) |
| `--water-level-error` | 0.3 | Water level measurement error (meters) |
| `--water-body-error` | 1.0 | Water boundary delineation error (pixels) |
| `--mc-iterations` | 500 | Monte Carlo iterations |
| `--mc-seed` | 42 | Monte Carlo random seed |
| `--confidence` | 0.95 | Confidence level for uncertainty |
| `--dem-datum` | None | DEM vertical datum |
| `--water-level-datum` | None | Water level vertical datum |
| `--output-dir` | ./rcc-output | Output directory |

## Output

| File | Description |
|---|---|
| `area_level_curve.csv` | Elevation-area relationship |
| `storage_curve.csv` | Elevation-area-storage curve |
| `storage_timeseries.csv` | Storage time series |
| `water_extent_timeseries.csv` | Water extent time series |
| `uncertainty.json` | Monte Carlo uncertainty analysis |
| `request.json` | Analysis request metadata |
| `dataset-manifest.json` | Dataset inventory |
| `output-manifest.json` | Output file inventory |
| `qa.json` | Quality assurance checks |

## Curve Methods

| Method | Description | Formula |
|---|---|---|
| trapezoidal | Area by pixel counting, storage by trapezoidal integration | V(h) = integral of A(h) dh |
| prism | Direct prism summation per pixel | V(h) = sum(max(h - DEM_i, 0)) * pixel_area |

## Key Algorithms

### Area at Level
Counts pixels with elevation <= water level, multiplied by pixel area.
Handles both projected and geographic CRS (latitude correction).

### Storage at Level (Prism Method)
For each inundated pixel, computes water depth = level - elevation,
then sums depth * pixel area across all inundated pixels.

### Trapezoidal Integration
Computes area at each level, then integrates using trapezoidal rule:
V(h_i) = V(h_{i-1}) + (A_i + A_{i-1}) / 2 * dh

### Monotonicity Enforcement
Area and storage curves are enforced non-decreasing by cumulative maximum.

### Monte Carlo Uncertainty
Propagates DEM vertical error, water level measurement error, and water
boundary delineation error through Monte Carlo simulation. Produces
confidence intervals at each elevation level.

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |

## Limitations

- Public DEMs (SRTM, Copernicus DEM) represent post-impoundment topography
  and cannot capture original reservoir basin shape
- Sediment deposition alters topography over time; single DEM cannot represent
  multi-period bathymetry
- Water level and satellite image dates may not coincide exactly
- Mixed pixel effects at water boundaries cause area uncertainty
- Relative storage change is more reliable than absolute storage volume
- Absolute storage requires known vertical datum and calibration data
- Outputs are analysis aids; engineering safety decisions require human review

## References

- Sawunyama, T. (2009). Estimating storage in reservoirs using remote sensing. IAHS Publ. 333.
- Zhang, S. et al. (2014). Capability evaluation of retrieving reservoir parameters from satellite imagery.
- McFeeters, S.K. (1996). The use of Normalized Difference Water Index. Remote Sensing.


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python reservoir_capacity_change.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--dem`) 时，skill 自动下载数据。
当用户给 `--dem` 时，走原文件路径 (向后兼容)。
