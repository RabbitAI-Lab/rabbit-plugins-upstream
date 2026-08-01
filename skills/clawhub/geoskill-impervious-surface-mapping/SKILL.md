---
name: impervious-surface-mapping
description: >
  Estimate impervious surface fraction from multi-band satellite imagery
  (Sentinel-2) using spectral indices (NDBI, NDVI, MNDWI). Supports binary
  classification and continuous fraction estimation, with zone-level
  aggregation and change detection. Use when mapping urban impervious
  surfaces, computing impervious ratios by watershed/admin unit, or
  analyzing temporal changes in built-up areas.
---

# Impervious Surface Mapping

GIS/remote sensing workflow for estimating impervious surface fraction from
multi-band satellite imagery. Uses spectral indices and sub-pixel estimation
to produce continuous impervious fraction maps, with optional binary
thresholding, zone aggregation, and change detection.

## Trigger

Use when the user wants to:
- Estimate impervious surface fraction from satellite imagery
- Map built-up areas using NDBI and related spectral indices
- Compute impervious ratios by street, community, or watershed
- Compare impervious surface changes between years
- Mask out water and vegetation before impervious analysis

## CLI Usage

```bash
# Basic fraction estimation
python scripts/impervious_surface_mapping.py \
  --raster sentinel2.tif \
  --year 2024 \
  --mode fraction

# Binary classification with threshold
python scripts/impervious_surface_mapping.py \
  --raster sentinel2.tif \
  --year 2024 \
  --mode binary \
  --threshold 0.5

# Zone aggregation
python scripts/impervious_surface_mapping.py \
  --raster sentinel2.tif \
  --year 2024 \
  --mode fraction \
  --aggregation-layer watersheds.geojson

# Change detection
python scripts/impervious_surface_mapping.py \
  --raster sentinel2_2024.tif \
  --year 2024 \
  --compare-year 2020 \
  --raster-compare sentinel2_2020.tif \
  --mode fraction
```

## Data Download

This skill can auto-fetch a Sentinel-2 L2A scene from the Microsoft
Planetary Computer when given a bounding box + date range. The script picks
the `B04` (red) asset by default; you can change `prefer_assets` in the
code to use `visual` for an RGB composite.

```bash
python scripts/impervious_surface_mapping.py \
  --bbox 116,39,117,40 \
  --date-range 2024-06-01,2024-06-30 \
  --output-dir ./impervious-output
```

The `PYTHONPATH` must include the parent of `_geoskill_data_fetcher/`
(the same directory the 50 skills live in). Set it once:

```bash
export PYTHONPATH="/path/to/行业Skill创意-20260727"
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--raster` | required | Multi-band raster (Sentinel-2: B2,B3,B4,B8,B11) |
| `--year` | required | Analysis year |
| `--mode` | fraction | `binary` or `fraction` |
| `--training-data` | None | Training samples GeoJSON (with `impervious` field) |
| `--threshold` | 0.5 | Threshold for binary mode |
| `--aggregation-layer` | None | Zone layer GeoJSON for aggregation |
| `--compare-year` | None | Comparison year for change detection |
| `--raster-compare` | None | Raster for comparison year |
| `--ndvi-mask` | 0.6 | NDVI threshold to mask dense vegetation |
| `--mndwi-mask` | 0.0 | MNDWI threshold to mask water |
| `--output-dir` | ./impervious-output | Output directory |

## Output

| File | Description |
|---|---|
| `impervious_fraction.tif` | Continuous impervious fraction [0, 1] |
| `impervious_binary.tif` | Binary impervious mask (1=impervious) |
| `zones_summary.csv` | Zone-level statistics (if aggregation-layer given) |
| `change.tif` | Change raster (fraction difference) |
| `accuracy.json` | Accuracy metrics (if training-data given) |

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |
