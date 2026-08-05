---
name: climate-risk-screening
description: Assess climate hazards from temperature/precipitation data. Use when the user wants to analyze changes, detect hazards, or generate assessment reports.
---
# Climate Risk Screening
Assess climate hazards from temperature/precipitation data.

## CLI Usage

```bash
python scripts/climate_risk_screening.py --temperature temp.tif --precipitation precip.tif
python scripts/climate_risk_screening.py --temperature temp.tif --precipitation precip.tif --output-dir my_output
```

## Parameters

| Argument | Required | Default | Description |
|---|---|---|---|
| `--temperature` | Yes | — | Path to temperature raster (°C) |
| `--precipitation` | Yes | — | Path to precipitation raster (mm) |
| `--output-dir`, `-o` | No | `climate-output` | Directory to write outputs |

## Output

| File | Description |
|---|---|
| `climate-report.json` | Machine-readable climate hazard stats (heat/cold/flood/drought exposure) |
| `report.html` | Human-readable HTML report |
| `output-manifest.json` | Run metadata + result summary |

## Exit Codes
| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 7 | Processing failure |


## 数据下载

本 skill 可自动从 NASA POWER 下载数据 (无需 API key):

```bash
python climate_risk_screening.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--temperature`) 时，skill 自动下载数据。
当用户给 `--temperature` 时，走原文件路径 (向后兼容)。
