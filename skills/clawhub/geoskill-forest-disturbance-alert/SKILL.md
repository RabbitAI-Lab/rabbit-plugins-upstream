---
name: forest-disturbance-alert
description: Detect forest disturbance from multi-temporal NDVI. Use when the user wants to analyze changes, detect hazards, or generate assessment reports.
---
# Forest Disturbance Alert
Detect forest disturbance from multi-temporal NDVI.

## CLI Usage

```bash
python scripts/forest_disturbance_alert.py --baseline baseline.tif --current current.tif
python scripts/forest_disturbance_alert.py --baseline baseline.tif --current current.tif --threshold 0.25
python scripts/forest_disturbance_alert.py --baseline baseline.tif --current current.tif --output-dir my_output
```

## Parameters

| Argument | Required | Default | Description |
|---|---|---|---|
| `--baseline` | Yes | — | Path to baseline (undisturbed) NDVI raster |
| `--current` | Yes | — | Path to current NDVI raster (same grid as `--baseline`) |
| `--threshold` | No | `0.2` | NDVI drop threshold (current − baseline < −threshold is flagged) |
| `--output-dir`, `-o` | No | `disturbance-output` | Directory to write outputs |

## Output

| File | Description |
|---|---|
| `disturbance-report.json` | Machine-readable disturbance stats (affected area, severity classes) |
| `report.html` | Human-readable HTML report |
| `output-manifest.json` | Run metadata + result summary |

## Exit Codes
| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 7 | Processing failure |


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python forest_disturbance_alert.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--baseline`) 时，skill 自动下载数据。
当用户给 `--baseline` 时，走原文件路径 (向后兼容)。
