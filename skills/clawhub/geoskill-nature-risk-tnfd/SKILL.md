---
name: nature-risk-tnfd
description: >
  TNFD LEAP-based nature-related financial risk screening. Locates enterprise
  assets relative to protected areas, water stress, and forest cover; evaluates
  nature dependency and impact using sector materiality; produces priority risk
  inventory and audit-ready evidence package.
---

# Nature Risk TNFD

TNFD LEAP approach (Locate → Evaluate) for screening enterprise assets against
ecological sensitive areas, ecosystem state, and natural dependencies. Produces
a spatial evidence package for nature-related financial risk assessment.

## Trigger

Use when the user wants to:
- Screen enterprise assets for proximity to protected areas / Key Biodiversity Areas
- Assess nature dependency and impact by sector using TNFD LEAP methodology
- Evaluate water stress, forest cover, and biodiversity pressure at asset locations
- Generate a priority nature risk inventory for ESG / TNFD reporting
- Produce a Locate-phase spatial evidence package

## CLI Usage

```bash
# Synthetic demo mode (no input files needed)
python scripts/nature_risk_tnfd.py --output-dir ./nrt-output

# With custom assets file (GeoJSON or CSV)
python scripts/nature_risk_tnfd.py --assets ./my-assets.geojson --output-dir ./nrt-output

# With sector override and custom buffers
python scripts/nature_risk_tnfd.py --sector agriculture --buffers "facility:5000,watershed:10000" --output-dir ./nrt-output

# With all parameters
python scripts/nature_risk_tnfd.py --assets ./assets.csv --sector mining --buffers "facility:10000" --indicators-config ./my-indicators.json --output-dir ./nrt-output
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--assets` | None | Path to assets file (GeoJSON or CSV with lat/lon) |
| `--sector` | None | Override sector for all assets (agriculture/mining/manufacturing/energy/real_estate/tourism) |
| `--buffers` | facility:5000 | Buffer distances as `type:meters` pairs |
| `--indicators-config` | None | Path to TNFD indicators JSON |
| `--output-dir` | ./nrt-output | Output directory |

## Output

| File | Description |
|---|---|
| `asset_nature_context.geojson` | Per-asset nature context with all indicators |
| `indicator_table.csv` | Tabular indicator values for all assets |
| `priority_assets.geojson` | High/medium risk assets for prioritization |
| `data_gaps.json` | Identified data gaps by asset and severity |
| `tnfd_screening_report.html` | Human-readable screening report |
| `request.json` | Analysis request metadata |
| `dataset-manifest.json` | Dataset inventory |
| `output-manifest.json` | Output file inventory |
| `qa.json` | Quality assurance checks |
| `run.log` | Execution log |

## Key Algorithms

### Locate: Spatial Screening
For each asset, computes:
- **Protected area proximity**: Direct overlap, nearest distance (haversine), buffer overlap
- **Water stress**: Raster lookup at asset location, classified into 4 levels
- **Forest cover**: Raster lookup at asset location, classified into 4 levels

### Evaluate: Dependency and Impact Scoring
Uses sector materiality matrix (0-5 scale) adjusted for location context:
- **Dependency**: Water supply, pollination, flood protection, climate regulation, timber/fiber
- **Impact**: Land use change, pollution, water withdrawal, GHG emissions, invasive species
- Location adjustments: water stress increases water dependency; protected area proximity increases land use impact

### Priority Scoring
Priority = (dependency + impact) / 2, classified into: negligible / low / medium / high

### Geographic Calculations
- Distances: Haversine formula (great-circle)
- Buffers: cos(lat) * 111320 m/degree approximation
- Areas: cos(lat) * 111320^2 m^2/degree^2 approximation

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |

## Important Limitations

- **Screening only, NOT disclosure**: This is a Locate/Evaluate-phase screening tool.
  Full TNFD disclosure requires Prepare and Assess phases with enterprise processes.
- **Synthetic data for demo**: Without real ecological data inputs, demo mode uses
  synthetic data. Replace with real WDPA, WRI Aqueduct, Hansen GFC data for production use.
- **Approximate geographic calculations**: Buffer and area calculations use cos(lat)
  approximation. For precise analysis, use projected coordinate systems.
- **Sensitive species data excluded**: KBA/IBAT sensitive species locations are
  not included in outputs. Access requires separate licensing.
- **Sector materiality is generic**: Default scores are indicative. Enterprises
  should calibrate materiality to their specific value chain.

## Data Licensing

- Do NOT package commercial biodiversity data (IBAT/KBA) in the skill
- WDPA data requires acceptance of terms of use
- WRI Aqueduct data: CC BY 4.0
- Hansen Global Forest Change: CC BY 4.0

## References

- TNFD (Taskforce on Nature-related Financial Disclosures) LEAP approach
- WDPA (World Database on Protected Areas)
- WRI Aqueduct Water Risk Atlas
- Hansen Global Forest Change dataset
- IUCN Protected Area Categories


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python nature_risk_tnfd.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--assets`) 时，skill 自动下载数据。
当用户给 `--assets` 时，走原文件路径 (向后兼容)。
