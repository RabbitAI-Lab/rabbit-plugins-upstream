---
name: forest-fire-burn-severity
description: >
  Compute forest fire burn severity from pre/post-fire NIR and SWIR imagery
  using differenced Normalized Burn Ratio (dNBR). Classifies severity into
  unburned, low, moderate, and high categories. Use when the user wants to
  assess burn severity, map fire damage, or generate burn severity reports.
---

# Forest Fire Burn Severity

Computes dNBR from pre/post-fire NIR+SWIR bands and classifies burn severity.

## CLI Usage

```bash
python scripts/forest_fire_burn_severity.py \
  --pre-nir pre_nir.tif --pre-swir pre_swir.tif \
  --post-nir post_nir.tif --post-swir post_swir.tif
```

Or with synthetic demo data (no real inputs needed):

```bash
python scripts/forest_fire_burn_severity.py --synthetic
```

## Parameters

| Flag | Type | Required | Description |
|---|---|---|---|
| `--pre-nir` | path | one-of | Pre-fire NIR band GeoTIFF |
| `--pre-swir` | path | one-of | Pre-fire SWIR band GeoTIFF |
| `--post-nir` | path | one-of | Post-fire NIR band GeoTIFF |
| `--post-swir` | path | one-of | Post-fire SWIR band GeoTIFF |
| `--synthetic` | flag | one-of | Run with synthetic demo data (no real inputs needed) |
| `--output-dir`, `-o` | path | no | Output directory (default: `burn-severity-output`) |
| `--version` | flag | no | Show version and exit |

## Output

| File | Description |
|---|---|
| `report.html` | Burn severity report |
| `burn-severity-report.json` | Detailed results |
| `output-manifest.json` | Machine-readable manifest |

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 7 | Processing failure |


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python forest_fire_burn_severity.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--image`) 时，skill 自动下载数据。
当用户给 `--image` 时，走原文件路径 (向后兼容)。
