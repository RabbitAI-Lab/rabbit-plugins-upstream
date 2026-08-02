---
name: groundwater-recharge-potential
description: >
  Multi-criteria screening of groundwater recharge potential using terrain, soil, geology,
  land cover, drainage density, and rainfall. Supports AHP, weighted overlay, and fuzzy
  aggregation with sensitivity analysis and spatial validation. Use when the user wants to
  identify zones with higher recharge potential, compare weight scenarios, or generate
  candidate recharge area maps for planning purposes.
---

## Prerequisites / 先准备 X 文件

> ⚠️ **必读** — 本 skill 不属于即用型，需要先准备特定文件才能跑。

本 skill 需要 **6 个栅格**（坡度/土壤/地质/土地覆盖/排水密度/降雨）。其中 4 个可自动下载（DEM→slope / SoilGrids / WorldCover / CHIRPS），**地质必须用户准备**。

👉 完整教程见仓库根目录 `PREREQUISITES.md` 1.4 节。

**先准备 X 文件**：1:50万 地质图（矢量化栅格）→ 其余自动下载。

快速试跑命令：

```bash
python groundwater_recharge_potential.py --bbox 116.0 39.5 116.5 40.0 --geology my_geology.tif --output-dir ./grp
```


# Groundwater Recharge Potential

Multi-criteria screening analysis for groundwater recharge potential.

## Purpose

Identify zones with higher groundwater recharge potential by combining:
- **Slope** — flatter terrain favors infiltration
- **Soil permeability** — higher permeability favors recharge
- **Geology** — formation type ranked by permeability
- **Land cover** — surface type ranked by infiltration favorability
- **Drainage density** — lower density favors infiltration over runoff
- **Rainfall** — more rain provides more recharge source

## Positioning

**This is a screening-level tool.** It does NOT:
- Promise specific groundwater volumes
- Guarantee well success rates
- Replace hydrogeological field investigation

Results are for planning reference only. Engineering safety, administrative
determination, and legal compliance require human review.

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Missing dependency |
| 6 | Data validation failure |
| 7 | Processing failure |

## Usage

```bash
python scripts/groundwater_recharge_potential.py \
  --bbox 116.0 39.5 116.5 40.0 \
  --slope slope.tif \
  --soil-permeability soil.tif \
  --geology geology.tif \
  --land-cover landcover.tif \
  --drainage-density drainage.tif \
  --rainfall rainfall.tif \
  --method weighted \
  --sensitivity-runs 100 \
  --min-area 1.0 \
  --output-dir grp-output
```

## Parameters

### Spatial extent (provide one)
- `--place` — Named place to geocode
- `--bbox` — Bounding box (xmin ymin xmax ymax) in EPSG:4326
- `--aoi-file` — Path to AOI vector file

### Analysis
- `--factor-config` — Custom factor configuration JSON
- `--weights` — Weights JSON, `equal`, or `ahp`
- `--method` — `ahp` | `weighted` | `fuzzy` (default: weighted)
- `--constraints` — Hard constraints JSON
- `--sensitivity-runs` — Monte Carlo runs (default: 100)
- `--min-area` — Minimum zone area in hectares (default: 1.0)

### Input rasters
- `--slope` — Slope in degrees
- `--soil-permeability` — Soil permeability proxy
- `--geology` — Geology class (categorical)
- `--land-cover` — Land cover class (categorical)
- `--drainage-density` — Drainage density
- `--rainfall` — Annual rainfall in mm

### Validation
- `--well-points` — Well locations GeoJSON for validation
- `--validation-blocks` — Spatial blocks for cross-validation (default: 5)

### Output
- `--output-dir` / `-o` — Output directory
- `--overwrite` — Allow overwriting
- `--dry-run` — Estimate only
- `--log-level` — Logging level

## Outputs

| File | Description |
|---|---|
| `recharge_potential.tif` | Composite suitability raster (0–1) |
| `candidate_zones.geojson` | Connected high-potential zones |
| `factor_weights.json` | Factor weights and metadata |
| `sensitivity.json` | Sensitivity analysis summary |
| `report.pdf` | HTML report with maps and stats |
| `request.json` | Input request manifest |
| `dataset-manifest.json` | Input data manifest |
| `output-manifest.json` | Output file manifest |
| `qa.json` | Quality assurance record |
| `run.log` | Execution log |

## Method Details

### AHP (Analytic Hierarchy Process)
- Pairwise comparison matrix → eigenvector weights
- Consistency ratio CR < 0.1 required
- Weights derived from expert judgment

### Weighted Overlay
- Linear normalization of continuous factors
- Categorical lookup for geology/land cover
- Weighted arithmetic mean

### Fuzzy Aggregation
- Sigmoid membership functions
- Gamma operator for combining factors
- Smooth transitions between classes

## Sensitivity Analysis
Monte Carlo perturbation of weights (±50%) to assess:
- Spatial stability of high-potential zones
- Mean standard deviation across runs
- Pixel-level consistency

## Validation
When well point data is provided:
- Spatial block cross-validation
- Compare mean suitability at well vs. non-well locations
- Report difference as evidence level indicator

## Constraints
Hard constraints can exclude:
- Slopes above a threshold
- Specific land cover classes (e.g., urban, water)
- Buffered areas around features

## References
- `references/recharge_factors.json` — Default factor scoring tables
- Saaty, T.L. (1980) — AHP methodology
- Bonham-Carter, G.F. (1994) — GIS-based multi-criteria analysis


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python groundwater_recharge_potential.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--dem`) 时，skill 自动下载数据。
当用户给 `--dem` 时，走原文件路径 (向后兼容)。
