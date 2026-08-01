---
name: flood-extent-mapping
description: Extract flood extent from SAR backscatter imagery. Use when the user wants to analyze changes, detect hazards, or generate assessment reports.
---
# Flood Extent Mapping
Extract flood extent from SAR backscatter imagery.

## CLI Usage

```bash
# Local file mode (backward compatible)
python scripts/flood_extent_mapping.py --sar sar.tif
python scripts/flood_extent_mapping.py --sar sar.tif --threshold -16
python scripts/flood_extent_mapping.py --sar sar.tif --output-dir my_output

# Auto-download mode — fetch Sentinel-1 GRD from Microsoft Planetary Computer
# (no API key required; one scene per invocation)
python scripts/flood_extent_mapping.py \
    --bbox 116,39,117,40 \
    --date-range 2024-06-01,2024-06-30 \
    --output-dir my_output
```

## Data Download

When `--bbox` (or `--aoi-file`) and `--date-range` are provided, the skill
auto-downloads one Sentinel-1 GRD scene from the **Microsoft Planetary
Computer** STAC catalog (collection `sentinel-1-grd`). The downloaded file
is written to `<output_dir>/downloaded/` and the SAR analysis runs on it
exactly as if a local file had been passed via `--sar`.

The `output-manifest.json` records `data_source`, `collection`, `bbox`,
`date_range`, and `fetched_at` whenever auto-download is used.

## Parameters

| Argument | Required | Default | Description |
|---|---|---|---|
| `--sar` | One-of | — | Path to local SAR backscatter raster (dB, calibrated) |
| `--bbox` | One-of | — | `W,S,E,N` in WGS-84; triggers auto-download |
| `--date-range` | w/ bbox | — | `START,END` ISO-8601; triggers auto-download |
| `--aoi-file` | No | — | GeoJSON Polygon / MultiPolygon (alternative to `--bbox`) |
| `--threshold` | No | `-15` | Water threshold in dB |
| `--output-dir`, `-o` | No | `flood-output` | Directory to write outputs |
| `--synthetic` | No | off | Use synthetic demo data (no real inputs) |

## Output

| File | Description |
|---|---|
| `flood-report.json` | Machine-readable flood extent stats (water area, depth proxy) |
| `report.html` | Human-readable HTML report |
| `output-manifest.json` | Run metadata + result summary |

## Exit Codes
| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 7 | Processing failure |
