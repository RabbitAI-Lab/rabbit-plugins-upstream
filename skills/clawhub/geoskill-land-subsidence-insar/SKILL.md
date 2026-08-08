---
name: land-subsidence-insar
description: Analyze land subsidence from InSAR displacement data. Use when the user wants to analyze changes, detect hazards, or generate assessment reports.
---
# Land Subsidence InSAR
Analyze land subsidence from InSAR displacement data.

## CLI Usage

```bash
python scripts/land_subsidence_insar.py --displacement disp.tif
python scripts/land_subsidence_insar.py --displacement disp.tif --reference baseline.tif
python scripts/land_subsidence_insar.py --displacement disp.tif --output-dir my_output
```

## Data Download

This skill can auto-fetch a Sentinel-1 GRD scene from the Microsoft
Planetary Computer when given a bounding box + date range. The downloaded
asset is then passed through `--displacement` (note: real InSAR displacement
products require additional SAR processing; the raw backscatter/intensity
is only a rough proxy for subsidence hotspots — see Limitations below).

```bash
# Fetch a S1 GRD scene for the Beijing area and analyze
python scripts/land_subsidence_insar.py \
  --bbox 116.4,39.9,116.42,39.92 \
  --date-range 2024-06-01,2024-06-30 \
  --output-dir ./subsidence-output

# Or via an AOI polygon file
python scripts/land_subsidence_insar.py \
  --aoi-file ./aoi.geojson \
  --output-dir ./subsidence-output
```

The `PYTHONPATH` must include the parent of `_geoskill_data_fetcher/`
(the same directory the 50 skills live in). Set it once:

```bash
export PYTHONPATH="/path/to/行业Skill创意-20260727"
```

## Parameters

| Argument | Required | Default | Description |
|---|---|---|---|
| `--displacement` | Yes* | — | Path to InSAR displacement raster (mm, positive = uplift, negative = subsidence) |
| `--reference` | No | — | Optional reference displacement raster for differential analysis |
| `--bbox` | No | — | Bounding box `W,S,E,N` — auto-downloads S1 GRD from MPC |
| `--date-range` | No | — | Date range `START,END` (ISO-8601) for auto-download |
| `--aoi-file` | No | — | Path to AOI GeoJSON polygon for auto-download |
| `--output-dir`, `-o` | No | `subsidence-output` | Directory to write outputs |

*Required unless `--synthetic` or `--bbox+--date-range` is supplied.

## Output

| File | Description |
|---|---|
| `subsidence-report.json` | Machine-readable subsidence stats (max/min/mean rate, affected area) |
| `report.html` | Human-readable HTML report |
| `output-manifest.json` | Run metadata + result summary |

## Exit Codes
| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 7 | Processing failure |
