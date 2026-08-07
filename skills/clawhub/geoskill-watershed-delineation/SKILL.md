---
name: watershed-delineation
description: >
  Automated watershed delineation from DEM. Computes D8 flow direction,
  flow accumulation, delineates watersheds from outlet points, extracts
  stream networks, and generates statistics. Use when the user wants to
  delineate a watershed, compute flow accumulation, extract streams, or
  analyze hydrological characteristics from a DEM.
---

# Watershed Delineation

Automated watershed analysis from DEM using D8 algorithm.

## CLI Usage

```bash
python scripts/watershed_delineation.py --dem dem.tif
python scripts/watershed_delineation.py --dem dem.tif --outlet-row 50 --outlet-col 60
python scripts/watershed_delineation.py --dem dem.tif --stream-threshold 50
python scripts/watershed_delineation.py --synthetic --output-dir ./out
```

## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载 DEM (无需 API key):

```bash
# 自动下载 Copernicus DEM GLO-30
python scripts/watershed_delineation.py \
    --bbox 116.30,39.85,116.45,39.95 \
    --date-range 2020-01-01,2020-12-31 \
    --output-dir ./ws-auto
```

下载的内容:
- **Copernicus DEM GLO-30** (`cop-dem-glo-30`) — 替换 `--dem`

下载元数据（`data_source`, `fetched_at`, `collection`, `dem_downloaded`）会写入 `output-manifest.json`。

## Parameters

| Flag | Type | Default | Description |
|---|---|---|---|
| `--dem` | path | (required, or use `--synthetic`) | Input DEM raster (GeoTIFF) |
| `--outlet-row` | int | None | Outlet row in DEM grid (default: max accumulation) |
| `--outlet-col` | int | None | Outlet column in DEM grid (default: max accumulation) |
| `--stream-threshold` | int | 100 | Stream threshold in accumulation pixels |
| `--output-dir` / `-o` | path | `watershed-output` | Output directory |
| `--synthetic` | flag | False | Run with synthetic demo data (no real inputs needed) |
| `--version` | flag | - | Show version and exit |

## Output

| File | Description |
|---|---|
| `flow_direction.tif` | D8 flow direction raster |
| `flow_accumulation.tif` | Flow accumulation raster |
| `watershed.tif` | Watershed mask |
| `streams.tif` | Stream network |
| `report.html` | Statistics report |
| `output-manifest.json` | Machine-readable manifest |

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 7 | Processing failure |


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python watershed_delineation.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--dem`) 时，skill 自动下载数据。
当用户给 `--dem` 时，走原文件路径 (向后兼容)。
