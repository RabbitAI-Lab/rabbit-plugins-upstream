---
name: flood-impact-assessment
description: >
  Overlay flood extent with population, buildings, roads, and cropland to
  estimate affected objects and generate impact reports. Use when the user
  wants to assess flood impact, count affected population/roads/buildings,
  or generate flood impact summaries from a flood extent raster.
---

# Flood Impact Assessment

Combines flood extent raster with exposure data (population, roads, buildings) to estimate affected objects.

## Trigger

Use when the user wants to:
- Assess flood impact on population/infrastructure
- Count affected people, roads, buildings
- Generate flood impact reports
- Combine flood extent with exposure data

## CLI Usage

```bash
# Local file mode (backward compatible)
python scripts/flood_impact_assessment.py --flood-raster flood.tif
python scripts/flood_impact_assessment.py --flood-raster flood.tif --population-raster pop.tif
python scripts/flood_impact_assessment.py --flood-raster flood.tif --population-raster pop.tif --roads-file roads.geojson

# Auto-download mode — fetch Sentinel-1 GRD from Microsoft Planetary Computer
# (population raster is synthesized bbox-aware; WorldPop is not on MPC)
python scripts/flood_impact_assessment.py \
    --bbox 116.4,39.6,116.6,39.8 \
    --date-range 2024-06-01,2024-06-30 \
    --output-dir my_output
```

## Data Download

When `--bbox` (or `--aoi-file`) and `--date-range` are provided, the skill
auto-downloads a Sentinel-1 GRD scene (collection `sentinel-1-grd`) from the
**Microsoft Planetary Computer** STAC catalog. Because WorldPop is not exposed
via MPC STAC, the population raster is synthesized to match the same
`bbox`/`crs`. The output manifest records `data_source`, `collection`,
`bbox`, `date_range`, and `fetched_at` whenever auto-download is used.

## Output

| File | Description |
|---|---|
| `report.html` | HTML impact report |
| `impact-report.json` | Detailed results JSON |
| `output-manifest.json` | Machine-readable manifest |

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 7 | Processing failure |

## Parameters

| Flag | Type | Default | Required | Description |
|---|---|---|---|---|
| `--flood-raster` | path | None | (yes unless `--synthetic`) | Flood extent raster (GeoTIFF) |
| `--population-raster` | path | None | no | Population raster (WorldPop GeoTIFF) |
| `--roads-file` | path | None | no | Roads vector (GeoJSON/Shapefile) |
| `--buildings-file` | path | None | no | Buildings vector (GeoJSON/Shapefile) |
| `--confidence-threshold` | float | 0.5 | no | Flood confidence threshold (range 0.0–1.0) |
| `--synthetic` | flag | False | no | Run with synthetic demo data (no real inputs needed) |
| `--output-dir` / `-o` | path | `flood-impact-output` | no | Output directory |
