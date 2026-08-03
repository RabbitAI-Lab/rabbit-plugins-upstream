---
name: grassland-degradation-monitor
description: >
  Monitor grassland degradation and recovery trends from multi-temporal
  vegetation cover, phenology, bare ground and climate baselines.
  Outputs management zones for restoration prioritization.
  Use when assessing grassland health, identifying degraded areas,
  evaluating restoration effectiveness, or generating management recommendations.
---

# Grassland Degradation Monitor

Identifies grassland degradation and recovery trends from multi-temporal
remote sensing data. Separates climate-driven from management-driven vegetation
change and outputs management zones with restoration priorities.

## Trigger

Use when the user wants to:
- Identify degrading grassland areas from multi-temporal imagery
- Evaluate restoration effectiveness (e.g., grazing exclusion, reseeding)
- Separate climate-driven from management-driven vegetation change
- Generate management zone maps with restoration priorities
- Conduct BACI (Before-After-Control-Impact) analysis for management assessment
- Monitor grassland health trends over years to decades

## CLI Usage

```bash
# Basic analysis with default parameters (10 years, Theil-Sen, climate normalized)
python scripts/grassland_degradation_monitor.py --output-dir ./gdm-output

# Custom years and trend method
python scripts/grassland_degradation_monitor.py \
  --years 15 \
  --trend-method ols \
  --output-dir ./gdm-output

# Without climate normalization (raw trend only)
python scripts/grassland_degradation_monitor.py \
  --years 10 \
  --no-climate-normalize \
  --output-dir ./gdm-output

# With custom degradation schema
python scripts/grassland_degradation_monitor.py \
  --years 10 \
  --degradation-schema references/degradation_schema.json \
  --output-dir ./gdm-output
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--input-ndvi` | None | Input NDVI time series GeoTIFF (multi-band, optional) |
| `--years` | 10 | Number of years for analysis |
| `--trend-method` | theil-sen | Trend estimation: theil-sen, ols, mann-kendall |
| `--climate-normalize` | True | Apply climate normalization (residual trend) |
| `--no-climate-normalize` | - | Disable climate normalization |
| `--degradation-schema` | built-in | Custom degradation schema JSON |
| `--output-dir` | ./gdm-output | Output directory |

## Output

| File | Description |
|---|---|
| `degradation_status.tif` | Raster map of degradation/recovery status codes |
| `trend.tif` | Raster map of trend slopes |
| `priority_areas.geojson` | Point features for priority restoration areas |
| `management_summary.csv` | Area statistics and recommendations per class |
| `timeseries.csv` | Mean NDVI, precipitation, temperature per year |
| `request.json` | Analysis request metadata |
| `output-manifest.json` | Output file inventory and area statistics |
| `qa.json` | Quality assurance checks |

## Degradation Status Codes

| Code | Name | Description | Recommendation |
|---|---|---|---|
| 3 | severe_degradation | NDVI declining >0.02/yr, 3+ years | Immediate restoration |
| 2 | moderate_degradation | NDVI declining 0.01-0.02/yr, 3+ years | Priority restoration |
| 1 | light_degradation | NDVI declining 0.005-0.01/yr, 3+ years | Preventive management |
| 0 | stable | No significant trend | Sustainable use |
| -1 | light_recovery | NDVI increasing 0.005-0.01/yr, 2+ years | Monitor and maintain |
| -2 | moderate_recovery | NDVI increasing 0.01-0.02/yr, 2+ years | Continue current practices |
| -3 | significant_recovery | NDVI increasing >0.02/yr, 2+ years | Success case, replicate |

## Key Algorithms

### Climate Normalization (Residual Trend)
Regresses NDVI against precipitation and temperature anomalies, then computes
the trend of residuals. This separates climate-driven variation from
management-driven change.

### Trend Estimation
- **Theil-Sen**: Robust non-parametric slope (median of pairwise slopes). Recommended for noisy remote sensing data.
- **OLS**: Ordinary Least Squares. Efficient for clean data.
- **Mann-Kendall**: Normalized Kendall tau. Non-parametric trend strength.

### Degradation Classification
Combines three factors:
1. **Trend slope**: Direction and magnitude of change
2. **Persistence**: Minimum consecutive years meeting threshold
3. **Absolute state**: Current NDVI level (very low NDVI escalates severity)

### BACI Analysis
Before-After-Control-Impact design for management effectiveness:
`BACI = (treat_after - treat_before) - (ctrl_after - ctrl_before)`

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |

## Limitations

- Grazing intensity data typically unavailable
- Grassland type differences complicate threshold transfer
- Remote sensing productivity proxies do not replace field biomass measurement
- Climate normalization assumes linear climate-vegetation relationship
- Short time series (< 5 years) reduces trend reliability

## References

- Fensholt & Proud 2012, Remote Sensing of Environment (residual trend)
- Ivits et al. 2013, Remote Sensing (European grassland trends)
- BGC ChinaGrass dataset for grassland classification


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python grassland_degradation_monitor.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--image`) 时，skill 自动下载数据。
当用户给 `--image` 时，走原文件路径 (向后兼容)。
