---
name: urban-green-equity
description: >
  Assess urban green space distribution equity across populations and
  communities. Evaluates quantity, quality, and walkable accessibility of
  parks and green spaces, identifies service gaps and priority areas for
  intervention. Use when the user needs green space equity analysis,
  service coverage assessment, or priority community identification.
---

## Prerequisites / 先准备 X 文件

> ⚠️ **必读** — 本 skill 不属于即用型，需要先准备特定文件才能跑。

本 skill 需要 **3 个 GeoJSON**：公园/绿地、路网、社区边界。人口栅格和入口点是可选的。

👉 完整教程见仓库根目录 `PREREQUISITES.md` 1.7 节。

**先准备 X 文件**：OSM 提 3 个 GeoJSON 即可跑（osmnx 10 行 Python）。

快速试跑命令：

```bash
python urban_green_equity.py --green-sources parks.geojson --network roads.geojson --communities neighborhoods.geojson --walk-minutes 10 --output-dir ./uge
```


# Urban Green Equity

Evaluates the fairness of urban green space distribution by analyzing
quantity, quality, and walkable accessibility across populations and
communities. Identifies service gaps and priority areas for green
infrastructure investment.

## Trigger

Use when the user wants to:
- Assess green space distribution equity across neighborhoods
- Compute walkable green space coverage for population groups
- Identify communities with inadequate green space access
- Evaluate candidate sites for new green spaces
- Generate equity metrics (Gini, coverage rate, per-capita stats)
- Compare green space accessibility between areas

## CLI Usage

```bash
# Basic equity analysis
python scripts/urban_green_equity.py \
    --green-sources parks.geojson \
    --network roads.geojson \
    --communities neighborhoods.geojson \
    --walk-minutes 10

# With population raster and entrances
python scripts/urban_green_equity.py \
    --green-sources parks.geojson \
    --network roads.geojson \
    --communities neighborhoods.geojson \
    --population pop.tif \
    --entrances park_entrances.geojson \
    --walk-minutes 5 10 15

# With barriers and candidate sites
python scripts/urban_green_equity.py \
    --green-sources parks.geojson \
    --network roads.geojson \
    --communities neighborhoods.geojson \
    --barriers rivers_railways.geojson \
    --candidate-sites new_sites.geojson \
    --equity-metrics gini,coverage_rate,per_capita_stats

# Full analysis
python scripts/urban_green_equity.py \
    --green-sources parks.geojson \
    --network roads.geojson \
    --communities neighborhoods.geojson \
    --population pop.tif \
    --entrances entrances.geojson \
    --barriers barriers.geojson \
    --candidate-sites candidates.geojson \
    --walk-minutes 10 \
    --equity-metrics gini,coverage_rate,per_capita_stats,coverage_stats,disparity_ratio \
    --output-dir my-analysis
```

## Parameters

| Parameter | Required | Default | Description |
|---|---|---|---|
| `--green-sources` | Yes | — | Green spaces (GeoJSON, Polygon features) |
| `--network` | Yes | — | Walkable road network (GeoJSON, LineString) |
| `--communities` | Yes | — | Community boundaries (GeoJSON, Polygon) |
| `--population` | No | — | Population raster (GeoTIFF) |
| `--entrances` | No | — | Green space entrance points (GeoJSON, Point) |
| `--barriers` | No | — | Walk barriers — rivers, railways (GeoJSON, LineString) |
| `--walk-minutes` | No | `10` | Walk time threshold in minutes |
| `--network-mode` | No | `walk` | Network mode (currently only `walk`) |
| `--equity-metrics` | No | `gini,coverage_rate,per_capita_stats,coverage_stats` | Comma-separated metrics |
| `--candidate-sites` | No | — | Candidate new green space sites (GeoJSON) |
| `--output-dir` | No | `uge-output` | Output directory |
| `--place` | No | — | Place name for AOI (future) |
| `--bbox` | No | — | Bounding box `xmin ymin xmax ymax` (4 floats) |
| `--aoi-file` | No | — | AOI polygon file (GeoJSON) |
| `--date-range` | No | — | Date range `START,END` for auto-download |
| `--cache-dir` | No | — | Override the default cache directory |

## Equity Metrics

| Metric | Description |
|---|---|
| `gini` | Gini coefficient of green space per capita (0=perfect equality) |
| `coverage_rate` | Fraction of communities with accessible green space |
| `per_capita_stats` | Mean/min/max/median green area per capita (m²/person) |
| `coverage_stats` | Mean/min/max/median green coverage ratio |
| `disparity_ratio` | Ratio of 75th to 25th percentile per-capita green |
| `population_weighted_coverage` | Population-weighted average coverage ratio |
| `total_green_area` | Total accessible green area across all communities |
| `total_served_population` | Total population with green space access |

## Output

| File | Description |
|---|---|
| `green_service_areas.geojson` | Walkable service areas from green spaces |
| `community_metrics.csv` | Per-community green space metrics |
| `equity_summary.json` | Equity metrics summary |
| `priority_communities.geojson` | Communities ranked by intervention priority |
| `scenario_report.pdf` | Candidate site evaluation report (JSON fallback) |
| `request.json` | Input parameters manifest |
| `dataset-manifest.json` | Input data metadata |
| `output-manifest.json` | Output metadata and results summary |
| `qa.json` | Quality assurance report |

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Validation error |
| 7 | Processing failure |

## Notes

- OSM park boundaries do not guarantee public access; entrance validation
  is recommended for accurate results
- Population raster and community statistics are not double-counted
- Equity metrics are scale-sensitive; results vary with community size
- Sensitive population attributes are not inferred from spatial data alone
- Walk network service areas use convex hull approximation of reachable nodes


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python urban_green_equity.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--image`) 时，skill 自动下载数据。
当用户给 `--image` 时，走原文件路径 (向后兼容)。
