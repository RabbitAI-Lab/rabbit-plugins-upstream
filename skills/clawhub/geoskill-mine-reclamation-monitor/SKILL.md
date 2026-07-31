
## Prerequisites / 先准备 X 文件

> ⚠️ **必读** — 本 skill 不属于即用型，需要先准备特定文件才能跑。

本 skill 需要 **pre-mining NDVI + post-reclamation NDVI** 两张栅格（同一网格）。或用 `--bbox --date-range` 让 skill 自动下载并算。

👉 完整教程见仓库根目录 `PREREQUISITES.md` 1.5 节。

**先准备 X 文件**：`--synthetic` 跑通流程，或先传两张 NDVI 栅格试跑。

快速试跑命令：

```bash
python mine_reclamation_monitor.py --synthetic --output-dir ./test
```

﻿---
name: mine-reclamation-monitor
description: >
  Assess vegetation recovery at mining sites using NDVI comparison. Use when the user wants to analyze changes, compare multi-temporal
  rasters, compute indices, or generate assessment reports.
---

# Mine Reclamation Monitor

Assess vegetation recovery at mining sites using NDVI comparison.

## CLI Usage

```bash
python scripts/mine_reclamation_monitor.py --pre-mining pre.tif --post-reclamation post.tif
python scripts/mine_reclamation_monitor.py --pre-mining pre.tif --post-reclamation post.tif --reference natural.tif
python scripts/mine_reclamation_monitor.py --pre-mining pre.tif --post-reclamation post.tif --output-dir my_output
python scripts/mine_reclamation_monitor.py --synthetic --output-dir my_output
```

## Parameters

| Argument | Required | Default | Description |
|---|---|---|---|
| `--pre-mining` | (yes unless `--synthetic`) | — | Path to pre-mining NDVI raster |
| `--post-reclamation` | (yes unless `--synthetic`) | — | Path to post-reclamation NDVI raster (same grid as `--pre-mining`) |
| `--reference` | No | — | Optional reference (natural) NDVI raster for recovery gap analysis |
| `--synthetic` | No | False | Run with synthetic demo data (auto-generates 2 NDVI rasters in `<output-dir>/synthetic_input/`) |
| `--output-dir`, `-o` | No | `reclamation-output` | Directory to write outputs |

## Output

| File | Description |
|---|---|
| `reclamation-report.json` | Machine-readable recovery stats (mean NDVI change, recovery ratio) |
| `report.html` | Human-readable HTML report |
| `output-manifest.json` | Run metadata + result summary |

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error (e.g. missing input file) |
| 7 | Processing failure |


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python mine_reclamation_monitor.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--reference`) 时，skill 自动下载数据。
当用户给 `--reference` 时，走原文件路径 (向后兼容)。
