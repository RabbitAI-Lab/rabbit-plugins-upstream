---
name: building-change-audit
description: >
  Object-level building change detection between two epochs. Identifies
  new, demolished, expanded, reduced, split, and merged buildings from
  footprint vectors. Use when comparing two building datasets, auditing
  construction changes, or generating building change reports.
---

# Building Change Audit

Compares two epochs of building footprints to detect object-level changes.

## Trigger

Use when the user wants to:
- Compare two building datasets for changes
- Identify new/demolished buildings
- Audit construction changes between epochs
- Generate building change statistics

## CLI Usage

```bash
# Basic comparison
python scripts/building_change_audit.py \
  --before-buildings before.geojson \
  --after-buildings after.geojson

# With custom IoU threshold
python scripts/building_change_audit.py \
  --before-buildings before.geojson \
  --after-buildings after.geojson \
  --match-iou 0.3 --area-tolerance 0.1

# Specify output directory
python scripts/building_change_audit.py \
  --before-buildings before.geojson \
  --after-buildings after.geojson \
  --output-dir ./audit-output
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--before-buildings` | required* | Before epoch buildings (GeoJSON/Shapefile) |
| `--after-buildings` | required* | After epoch buildings (GeoJSON/Shapefile) |
| `--match-iou` | 0.1 | IoU threshold for matching |
| `--area-tolerance` | 0.05 | Area ratio tolerance for "unchanged" |
| `--bbox` | — | Bounding box `W,S,E,N` for auto-downloading ms-buildings |
| `--date-range` | — | Date range `START,END` for auto-download |
| `--aoi-file` | — | AOI polygon file (GeoJSON) |
| `--cache-dir` | — | Override the default cache directory |
| `--output-dir` | ./building-change-output | Output directory |

*Required unless `--synthetic` or `--bbox+--date-range` is supplied.

## Output

| File | Description |
|---|---|
| `building_changes.geojson` | Change features with type and metrics |
| `report.html` | HTML summary report |
| `output-manifest.json` | Machine-readable manifest |

## Change Types

| Type | Meaning |
|---|---|
| `new` | Building present only in after epoch |
| `demolished` | Building present only in before epoch |
| `expanded` | Matched, area increased > tolerance |
| `reduced` | Matched, area decreased > tolerance |
| `unchanged` | Matched, area within tolerance |
| `split` | One before → multiple after |
| `merge` | Multiple before → one after |

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载 Microsoft Building
Footprints (ms-buildings) data, generating **two snapshots** — one for
`--before-buildings` and one for `--after-buildings` — so you can run a
change audit without supplying your own GeoJSON.

```bash
python building_change_audit.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--before-buildings`/`--after-buildings`) 时，
skill 自动下载两份 ms-buildings 数据 (一前一后)。
**注意**：ms-buildings 是单一静态数据集, 两次下载返回的通常是同一份 parquet
blob — 真正的 temporal change detection 需要在脚本外做区域/日期过滤。
由于 ms-buildings 用的是 `abfs://` URL (urllib 不支持)，下载会失败并自动
fall back 到 `--synthetic` 模式。
