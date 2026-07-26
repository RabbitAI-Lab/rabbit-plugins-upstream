# DEV.md — change-detection

## Goal
Multi-temporal change detection for satellite imagery. Detect vegetation, urban, and water changes between two time periods.

## Data Source
Local raster processing — two co-registered GeoTIFF images (same extent, resolution, CRS).

## Core Functions
1. **detect** — Run change detection on two images
2. **report** — Generate change statistics report

## Methods
- **NDVI Difference**: ΔNDVI = NDVI_t2 - NDVI_t1
- **Image Differencing**: ΔBand = Band_t2 - Band_t1
- **Change Vector Analysis (CVA)**: Multi-band magnitude and direction

## Change Types
- Vegetation gain/loss (NDVI-based)
- Urban expansion (NDBI-based)
- Water change (NDWI-based)

## Output
- Change magnitude GeoTIFF
- Binary change mask
- Statistics JSON

## Dependencies
- rasterio, numpy, tqdm

## Verification
1. `python scripts/change-detection.py --help` works
2. Subcommand help works
