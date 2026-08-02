---
name: cropland-change-compliance
description: >
  Detect and classify cropland changes from before/after NDVI rasters.
  Identifies suspected construction, water, forest, and bare soil changes
  and generates compliance investigation materials. Use when the user wants
  to check farmland for unauthorized changes, monitor cropland conversion,
  or generate compliance reports.
---

# Cropland Change Compliance

Detects and classifies cropland changes from multi-temporal NDVI rasters.

## CLI Usage

```bash
python scripts/cropland_change_compliance.py --before-ndvi before.tif --after-ndvi after.tif
python scripts/cropland_change_compliance.py --before-ndvi b.tif --after-ndvi a.tif --ndvi-threshold 0.2
```

## Output

| File | Description |
|---|---|
| `report.html` | Compliance report |
| `compliance-report.json` | Detailed results |
| `suspected_changes.geojson` | Suspected change findings |
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
| `--before-ndvi` | path | None | (yes unless `--synthetic`) | Path to before-period NDVI raster (GeoTIFF) |
| `--after-ndvi` | path | None | (yes unless `--synthetic`) | Path to after-period NDVI raster (GeoTIFF) |
| `--ndvi-threshold` | float | 0.15 | no | Minimum |NDVI change| to count as detected (range 0.01–1.0) |
| `--rules` | path | None | no | Custom compliance rules JSON |
| `--synthetic` | flag | False | no | Run with synthetic demo data (no real inputs needed) |
| `--output-dir` / `-o` | path | `compliance-output` | no | Output directory |


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python cropland_change_compliance.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--image`) 时，skill 自动下载数据。
当用户给 `--image` 时，走原文件路径 (向后兼容)。
