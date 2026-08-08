---
name: building-footprint-height
description: >
  Extract building footprints and estimate height, floor count proxy, and
  volume from DSM/DTM/LiDAR data. Produces 2.5D urban models for 3D city
  modeling, population downscaling, and risk exposure analysis.
---

# Building Footprint Height

Extract building heights from elevation data (DSM, DTM, LiDAR point cloud)
and building footprints. Estimates height, floor count proxy, volume, and
quality codes for each building.

## Trigger

Use when the user wants to:
- Estimate building heights from DSM/DTM raster data
- Compute building volumes and floor count proxies
- Generate 2.5D urban models for 3D city visualization
- Assess building data quality and flag anomalies
- Prepare building data for population downscaling or risk exposure

## CLI Usage

```bash
# Synthetic demo mode (no input files needed)
python scripts/building_footprint_height.py --output-dir ./bfh-output

# With custom floor height assumption
python scripts/building_footprint_height.py --floor-height 3.6 --output-dir ./bfh-output

# With point cloud method
python scripts/building_footprint_height.py --height-method point_cloud_quantile --output-dir ./bfh-output

# With custom standards
python scripts/building_footprint_height.py --standard-config ./my-standards.json --output-dir ./bfh-output
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--dsm` | None | Path to DSM GeoTIFF |
| `--dtm` | None | Path to DTM GeoTIFF |
| `--footprints` | None | Path to building footprints GeoJSON/Shapefile |
| `--point-cloud` | None | Path to LiDAR point cloud (LAS/CSV) |
| `--height-method` | `dsm_minus_dtm` | Height estimation method |
| `--floor-height` | 3.0 | Assumed floor height in meters |
| `--output-dir` | ./bfh-output | Output directory |
| `--standard-config` | None | Path to building height standards JSON |
| `--bbox` | None | W,S,E,N in WGS-84 (auto-downloads Copernicus GLO-30 DEM) |
| `--date-range` | None | START,END ISO-8601 (optional for time-invariant DEM) |
| `--aoi-file` | None | GeoJSON polygon; its bbox is used for the query |
| `--cache-dir` | None | Override the data-fetcher cache directory |

## 数据下载 (Data Download)

This skill can auto-download the elevation input from the Microsoft
Planetary Computer STAC catalog. No API key is required.

```bash
# Download one Copernicus GLO-30 DEM tile over central Beijing and run the
# pipeline using it as a stand-in DSM (the script falls back to a
# percentile-DTM approximation when no DTM is supplied).
python scripts/building_footprint_height.py \
  --bbox 116.0,39.5,116.8,40.0 \
  --output-dir ./bfh-output
```

The downloaded asset is cached under `~/.geoskill_cache/` so a second run
with the same `--bbox` reuses the file. The download route also accepts
`--aoi-file my_polygon.geojson` instead of `--bbox`.

## Height Methods

| Method | Priority | Requirements | Quality |
|---|---|---|---|
| `dsm_minus_dtm` | 1 (recommended) | DSM + DTM rasters | Code 1 (best) |
| `point_cloud_quantile` | 2 | LiDAR point cloud | Code 2 |
| `shadow_based` | 3 | Shadow length + solar angle | Code 3 |

## Output

| File | Description |
|---|---|
| `buildings_3d.geojson` | Building footprints with height/volume/floors |
| `height.tif` (.npy + meta) | Building height raster |
| `building_stats.csv` | Per-building statistics |
| `quality_flags.geojson` | Buildings with quality issues |
| `report.html` | Human-readable HTML report |
| `request.json` | Analysis request metadata |
| `dataset-manifest.json` | Dataset inventory |
| `output-manifest.json` | Output file inventory |
| `qa.json` | Quality assurance checks |

## Quality Codes

| Code | Label | Meaning |
|---|---|---|
| 1 | 高度可靠 | DSM-DTM, coverage >80% |
| 2 | 高度较可靠 | Point cloud quantile, >50 points |
| 3 | 高度估算 | Shadow-based or coarse DEM |
| 4 | 高度可疑 | Coverage <50% or anomaly detected |
| 5 | 高度缺失 | No valid data |

## Key Algorithms

### DSM-DTM Height
Height = quantile(DSM_footprint, 0.95) - median(DTM_footprint)

Uses robust quantile to exclude outliers (antennas, trees). Edge buffer
(default 0.5m) excludes mixed-boundary pixels.

### Point Cloud Quantile
Height = quantile(points_z, 0.95) - quantile(points_z, 0.05)

Requires ≥10 points per building. Ground reference is 5th percentile.

### Floor Count Proxy
floors = round(height / floor_height)

Floor height is an assumption (default 3.0m residential). Min/max range
accounts for ±0.5m uncertainty.

### Volume
V = footprint_area × height × roof_factor

Roof factors: flat=1.0, pitched=0.85, complex=0.9

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |

## Limitations

- Synthetic demo mode only; file-based mode requires GeoTIFF/GeoJSON input
- Floor count is a proxy — actual floors may differ
- Shadow method requires manual shadow length measurement
- Does not produce true 3D mesh models (2.5D only)
- Coarse DEM (e.g., SRTM) should NOT be used for individual building heights
- Tree mixing may inflate height estimates in vegetated areas

## References

- OSM Building Heights dataset
- Microsoft Building Footprints
- AHN (Actueel Hoogtebestand Nederland) DSM/DTM
- USGS 3DEP LiDAR point clouds
