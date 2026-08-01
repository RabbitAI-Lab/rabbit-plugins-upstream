---
name: aquaculture-pond-mapping
description: >
  Identify and monitor aquaculture ponds from multi-temporal remote sensing.
  Detects coastal and inland ponds, computes area statistics, tracks
  expansion/abandonment, and analyzes conversion with wetlands/cropland.
  Use when mapping aquaculture distribution, monitoring pond dynamics,
  assessing environmental impacts, or generating pond inventories.
---

# Aquaculture Pond Mapping

Identifies coastal and inland aquaculture ponds from multi-temporal satellite
imagery. Separates aquaculture ponds from natural water bodies and paddy fields
using shape, texture, water frequency, and adjacency features. Outputs pond
locations, aquaculture zones, change detection, and area statistics.

## Trigger

Use when the user wants to:
- Map aquaculture pond distribution from satellite imagery
- Monitor pond expansion or abandonment over time
- Detect conversion between aquaculture and wetlands/cropland
- Generate pond inventories for fisheries management
- Assess environmental impacts of aquaculture development
- Identify illegal pond construction in protected areas

## CLI Usage

```bash
# Basic analysis with default parameters (rules method, single year)
python scripts/aquaculture_pond_mapping.py --output-dir ./apm-output

# Multi-year analysis with custom minimum area
python scripts/aquaculture_pond_mapping.py \
  --years 2020 2021 2022 2023 \
  --min-area 1000 \
  --output-dir ./apm-output

# ML-based classification (requires training data)
python scripts/aquaculture_pond_mapping.py \
  --method ml \
  --training-data ./training_samples.geojson \
  --output-dir ./apm-output

# With custom input NDWI stack
python scripts/aquaculture_pond_mapping.py \
  --input-ndwi ./ndwi_stack.tif \
  --years 2020 2021 2022 \
  --output-dir ./apm-output
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--input-ndwi` | None | Input NDWI time series GeoTIFF (multi-band, optional) |
| `--method` | rules | Classification method: rules, ml |
| `--years` | [2023] | Years for analysis (space-separated) |
| `--min-area` | 500.0 | Minimum pond area in m² (default: 500) |
| `--output-dir` | ./apm-output | Output directory |

## Output

| File | Description |
|---|---|
| `ponds.geojson` | Point features for detected aquaculture ponds with confidence |
| `aquaculture_zones.geojson` | Point features for aquaculture cluster zones |
| `change.geojson` | Point features showing new/abandoned/stable ponds |
| `area_by_admin.csv` | Area statistics per classification class |
| `accuracy.json` | Classification summary and confidence metrics |
| `request.json` | Analysis request metadata |
| `dataset-manifest.json` | Input data and parameters manifest |
| `output-manifest.json` | Output file inventory and area statistics |
| `qa.json` | Quality assurance checks |

## Classification Classes

| Code | Name | Description |
|---|---|---|
| 1 | aquaculture_pond | Managed aquaculture pond (rectangular, embanked, clustered) |
| 2 | natural_water | Natural water body (irregular shape, permanent, no embankments) |
| 3 | paddy_field | Rice paddy (small, rectangular, seasonal flooding) |
| 0 | non_water | Non-water or below minimum area |

## Change Detection Codes

| Code | Name | Description |
|---|---|---|
| 1 | new_pond | Pond present in latest period but not baseline |
| -1 | abandoned_pond | Pond present in baseline but not latest |
| 0 | stable_pond | Pond present in both periods |

## Key Algorithms

### Two-Step Classification
1. **Water Extraction**: NDWI/MNDWI thresholding to identify water candidates
2. **Pond Classification**: Rule-based scoring using shape, texture, water frequency,
   and adjacency features to separate aquaculture from natural water

### Shape Features
- **Rectangularity**: area / bounding box area (ponds are rectangular)
- **Compactness**: 4π·area / perimeter² (moderate for ponds)
- **Aspect Ratio**: elongation (ponds have moderate ratios)

### Texture Features (Embankment Detection)
- Local variance and edge density detect embankments (堤埂) around ponds
- Higher texture scores indicate human-constructed boundaries

### Water Frequency
- Seasonal water (intermediate frequency) suggests managed aquaculture
- Permanent water suggests natural lakes/rivers

### Adjacency Features
- Clustered ponds indicate aquaculture areas
- Isolated water bodies more likely natural

### Change Detection
- Compares pond masks between baseline and latest periods
- Identifies new, abandoned, and stable ponds

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |

## Limitations

- Paddy fields and salt pans may be confused with aquaculture ponds
- Very small ponds (< 2 pixels) may be missed
- Seasonal drying can cause false negatives in single-date imagery
- Cloud cover affects optical remote sensing accuracy
- Ground truth data recommended for accuracy assessment
- ML method requires representative training samples

## References

- McFeeters 1996 - NDWI for open water delineation
- Xu 2006 - MNDWI for enhanced water detection
- Two-step water-then-pond classification approach


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python aquaculture_pond_mapping.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--image`) 时，skill 自动下载数据。
当用户给 `--image` 时，走原文件路径 (向后兼容)。
