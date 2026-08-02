---
name: land-use-carbon-accounting
description: >
  Compute carbon stock changes, emissions/removals, and uncertainty from
  multi-temporal land cover data using IPCC Tier 1/2 carbon factors.
  Use when analyzing land use change carbon budgets, estimating CO2e
  emissions from deforestation, or generating carbon accounting reports.
---

# Land Use Carbon Accounting

Computes carbon stock changes, emissions/removals, and uncertainty from
multi-temporal land cover data using IPCC Tier 1/2 carbon factors.

## Trigger

Use when the user wants to:
- Compute carbon stock changes from multi-temporal land cover data
- Estimate CO2e emissions/removals from land use transitions
- Generate carbon accounting reports with uncertainty analysis
- Analyze deforestation or afforestation carbon impacts
- Produce transition matrices and carbon change rasters

## CLI Usage

```bash
# Synthetic demo mode (no input files needed)
python scripts/land_use_carbon_accounting.py --output-dir ./luca-output

# With input GeoTIFF land cover rasters
python scripts/land_use_carbon_accounting.py \
  --before-landcover ./data/before.tif \
  --after-landcover ./data/after.tif \
  --eco-zone subtropical \
  --pools BAG BBG SOC \
  --output-dir ./luca-output

# With custom carbon factors and Monte Carlo settings
python scripts/land_use_carbon_accounting.py \
  --before-landcover ./data/before.tif \
  --after-landcover ./data/after.tif \
  --eco-zone temperate \
  --pools BAG BBG DW LT SOC \
  --mc-iterations 5000 \
  --mc-seed 42 \
  --confidence 0.95 \
  --output-dir ./luca-output

# With bounding box for area computation
python scripts/land_use_carbon_accounting.py \
  --before-landcover ./data/before.tif \
  --after-landcover ./data/after.tif \
  --bbox 116.0 39.5 116.5 40.0 \
  --output-dir ./luca-output
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--before-landcover` | None | Before period land cover GeoTIFF |
| `--after-landcover` | None | After period land cover GeoTIFF |
| `--eco-zone` | subtropical | Ecological zone for carbon factors |
| `--pools` | BAG BBG SOC | Carbon pools to include |
| `--carbon-factors` | None | Path to custom carbon factors JSON |
| `--source-system` | auto | Source classification: auto, from_glc_fcs30, from_esri_lulc, from_copernicus |
| `--mc-iterations` | 1000 | Monte Carlo iterations |
| `--mc-seed` | 42 | Monte Carlo random seed |
| `--confidence` | 0.95 | Confidence level for uncertainty |
| `--bbox` | None | Bounding box: xmin ymin xmax ymax |
| `--output-dir` | ./luca-output | Output directory |

## Output

| File | Description |
|---|---|
| `transition_matrix.csv` | Land cover transition matrix (pixel counts) |
| `land_transition.tif` | Transition type raster |
| `carbon_change.tif` | Pixel-level carbon change raster (tC/ha) |
| `carbon_summary.csv` | Per-transition carbon change summary |
| `uncertainty.json` | Monte Carlo uncertainty analysis |
| `request.json` | Analysis request metadata |
| `dataset-manifest.json` | Dataset inventory and mapping info |
| `output-manifest.json` | Output file inventory and carbon results |
| `qa.json` | Quality assurance checks |

## Carbon Pools

| Code | Name | Description |
|---|---|---|
| BAG | Above-ground Biomass | Living vegetation above ground |
| BBG | Below-ground Biomass | Living roots and rhizomes |
| DW | Dead Wood | Standing and fallen dead wood |
| LT | Litter | Leaf litter and fine debris |
| SOC | Soil Organic Carbon | Topsoil organic carbon |

## Land Cover Classes (IPCC)

| Code | Name | Description |
|---|---|---|
| FL | Forest Land | Forest and woodland |
| CL | Cropland | Cropland and pasture |
| GL | Grassland | Natural grassland |
| WL | Wetlands | Wetlands and peatlands |
| SL | Settlements | Built-up areas |
| OL | Other Land | Barren, ice, water |

## Ecological Zones

| Zone | Description |
|---|---|
| tropical | Tropical forest and savanna |
| subtropical | Subtropical and warm temperate |
| temperate | Cool temperate and boreal |
| arid | Arid and semi-arid |

## Key Algorithms

### Stock-Difference Method
Computes carbon stock change using the IPCC stock-difference approach:
ΔC = Σ(A_ij × (C_after_j - C_before_i))

Where A_ij is the area transitioning from class i to j, and C is the
carbon density (tC/ha) for each class.

### Transition Matrix
Counts pixel-level transitions between before and after land cover classes.
Handles nodata values (0, 255) by exclusion.

### Monte Carlo Uncertainty
Samples carbon factors from normal distributions using coefficient of
variation (CV) from the factors registry. Computes confidence intervals
from the distribution of total carbon change.

### Pixel Area Computation
- Projected CRS: Uses transform directly (pixel width × height)
- Geographic CRS: Applies latitude correction (cos(lat) × 111320)

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |

## Limitations

- Tier 1/2 approach only; not certified for MRV/VERRA/Gold Standard
- Carbon factors are regional averages; local calibration recommended
- Does not account for time-dependent carbon dynamics (Tier 3)
- Assumes instantaneous change between two time points
- Pixel resolution affects area accuracy for heterogeneous landscapes

## References

- IPCC 2006 Guidelines for National Greenhouse Gas Inventories
- IPCC 2019 Refinement to the 2006 Guidelines
- GFOI 2016 Integrating remote-sensing and ground-based observations


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python land_use_carbon_accounting.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--image`) 时，skill 自动下载数据。
当用户给 `--image` 时，走原文件路径 (向后兼容)。
