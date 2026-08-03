---
name: debris-flow-risk
description: >
  Identify potential debris-flow gullies, integrate terrain, material source,
  rainfall trigger, and downstream exposure to produce basin-level hazard
  screening and risk assessment.
---

# Debris Flow Risk Screening

Identifies potential debris-flow gullies from DEM terrain analysis, integrates
material source availability, rainfall triggering thresholds, and downstream
exposure to produce basin-level hazard and risk screening.

## Trigger

Use when the user wants to:
- Identify potential debris-flow gullies from DEM data
- Produce basin-level debris-flow hazard screening
- Assess downstream exposure and risk from debris flows
- Evaluate runout zones using conservative geometric diffusion
- Generate risk maps integrating hazard, exposure, and vulnerability

## CLI Usage

```bash
# Synthetic demo mode (no input files needed)
python scripts/debris_flow_risk.py --output-dir ./dfr-output

# With custom parameters
python scripts/debris_flow_risk.py \
  --rainfall-scenario 100yr \
  --runout-method geometric \
  --risk-schema three_class \
  --output-dir ./dfr-output

# With custom outlet points
python scripts/debris_flow_risk.py \
  --outlet-points ./outlets.geojson \
  --material-source sparse \
  --output-dir ./dfr-output
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--place` | None | Place name for AOI lookup |
| `--bbox` | None | Bounding box: "west,south,east,north" |
| `--aoi-file` | None | Path to AOI polygon (GeoJSON) |
| `--outlet-points` | None | Path to outlet points (GeoJSON) |
| `--rainfall-scenario` | 50yr | Rainfall scenario: 20yr, 50yr, 100yr |
| `--material-source` | moderate | Material source: sparse, moderate, abundant |
| `--runout-method` | geometric | Runout method: geometric, ramms, flo2d |
| `--risk-schema` | three_class | Risk schema: three_class, four_class, five_class |
| `--infrastructure` | None | Path to infrastructure points (GeoJSON) |
| `--dem-resolution` | 30 | DEM resolution in meters (sensitivity parameter) |
| `--flow-threshold` | 500 | Flow accumulation threshold for channel initiation |
| `--output-dir` | ./dfr-output | Output directory |

## Output

| File | Description |
|---|---|
| `debris_flow_basins.geojson` | Identified debris-flow basins with attributes |
| `hazard_index.tif` | Hazard index raster (0-1) |
| `runout_zones.geojson` | Runout zone polygons |
| `exposure.csv` | Downstream exposure inventory |
| `screening_report.pdf` | Screening report (HTML-based) |
| `request.json` | Analysis request metadata |
| `dataset-manifest.json` | Dataset inventory |
| `output-manifest.json` | Output file inventory |
| `qa.json` | Quality assurance checks |

## Key Algorithms

### D8 Flow Direction
Standard D8 encoding: 1=E, 2=SE, 4=S, 8=SW, 16=W, 32=NW, 64=N, 128=NE.
Flow accumulation computed by recursive upslope contribution.

### Basin Delineation
Watershed basins delineated from outlet points using flow direction.
Basins filtered by slope, curvature, and flow accumulation criteria.

### Hazard Index
Composite index integrating:
- Terrain factor: slope, profile curvature, basin relief
- Material source: loose sediment availability
- Rainfall trigger: intensity-duration threshold exceedance

### Runout Zone (Geometric)
Conservative geometric diffusion: runout distance = H / tan(α), where
H is the elevation drop and α is the average fan angle (default 11°).
RAMMS/FLO-2D interfaces reserved for future implementation.

### Sensitivity Analysis
Outlet position, flow accumulation threshold, and DEM resolution are
key sensitive parameters. Sensitivity analysis varies each parameter
±20% and reports hazard index change.

### Risk Classification
Risk = Hazard × Exposure × Vulnerability
Three-class: Low, Moderate, High

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |

## Important Limitations

- Output is **screening-level**, NOT a substitute for dynamic engineering models
- Results are sensitive to outlet position, flow threshold, and DEM resolution
- Runout uses conservative geometric diffusion; for engineering design use RAMMS/FLO-2D
- Material source estimation is approximate without field validation
- Rainfall thresholds are regional approximations

## References

- Takahashi, T. (2007). Debris Flow: Mechanics, Prediction and Countermeasures.
- Hungr, O., et al. (2005). The Varnes classification of landslide types.
- Horton, P., et al. (2013). Flow-R: a model for susceptibility mapping of debris flows.
- Kang, S., & Lee, S. (2018). Debris flow susceptibility assessment using GIS and machine learning.


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python debris_flow_risk.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--dem`) 时，skill 自动下载数据。
当用户给 `--dem` 时，走原文件路径 (向后兼容)。
