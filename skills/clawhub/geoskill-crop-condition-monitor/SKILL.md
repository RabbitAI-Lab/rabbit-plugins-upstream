---
name: crop-condition-monitor
description: Assess crop health from NDVI time series. Use when the user wants to analyze changes, detect hazards, or generate assessment reports.
---
# Crop Condition Monitor
Assess crop health from NDVI time series.

## CLI Usage

```bash
python scripts/crop_condition_monitor.py --ndvi ndvi1.tif ndvi2.tif ndvi3.tif
python scripts/crop_condition_monitor.py --ndvi ndvi1.tif ndvi2.tif --dates 2024-04-01,2024-05-01
python scripts/crop_condition_monitor.py --ndvi ndvi1.tif ndvi2.tif --output-dir my_output
```

## Parameters

| Argument | Required | Default | Description |
|---|---|---|---|
| `--ndvi` | Yes | — | One or more NDVI rasters (chronological order, same grid) |
| `--dates` | No | — | Optional comma-separated acquisition dates matching `--ndvi` files (ISO `YYYY-MM-DD`) |
| `--output-dir`, `-o` | No | `crop-output` | Directory to write outputs |

## Output

| File | Description |
|---|---|
| `crop-report.json` | Machine-readable crop condition stats (mean NDVI, anomaly area) |
| `report.html` | Human-readable HTML report |
| `output-manifest.json` | Run metadata + result summary |

## Exit Codes
| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 7 | Processing failure |

## Data Download

When `--bbox` (or `--aoi-file`) and `--date-range` are provided, this skill
auto-downloads a small set of Sentinel-2 L2A (`sentinel-2-l2a`) visual
previews from the **Microsoft Planetary Computer** STAC catalog (no API key
required) and uses them as the multi-temporal NDVI stack.

The downloaded files are written to `<output_dir>/downloaded/` and the
downstream `monitor_crop` analysis runs on them. The `output-manifest.json`
records `data_source / collection / bbox / date_range / fetched_at` for
traceability.

```bash
python scripts/crop_condition_monitor.py \
  --bbox 116.4,39.6,116.6,39.8 \
  --date-range 2024-06-01,2024-06-30 \
  --output-dir my_output
```
