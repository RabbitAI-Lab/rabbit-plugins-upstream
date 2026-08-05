---
name: forest-health-monitor
description: >
  Monitor forest canopy vitality decline, drought stress, pest damage,
  or wind throw from multi-temporal spectral indices. Distinguishes
  short-term fluctuations from persistent decline using historical
  baselines, persistence state machines, and climate attribution.
  Use when assessing forest health, detecting anomalies, or planning
  field sampling.
---

## Prerequisites / 先准备 X 文件

> ⚠️ **必读** — 本 skill 不属于即用型，需要先准备特定文件才能跑。

本 skill 需要 **bbox + 年份**。所有 NDVI/EVI/NDMI/NBR 时序数据自动从 MPC 下载。

👉 完整教程见仓库根目录 `PREREQUISITES.md` 1.3 节。

**先准备 X 文件**：`--synthetic` 一行跑通，验证工作流后再传真实 AOI。

快速试跑命令：

```bash
python forest_health_monitor.py --synthetic --output-dir ./test
```


# Forest Health Monitor

Detects forest health anomalies from spectral indices (NDVI, EVI, NDMI, NBR)
and distinguishes short-term fluctuations from sustained deterioration using
historical baselines, a persistence state machine, and climate attribution.

## Trigger

Use when the user wants to:
- Detect forest canopy vitality decline from satellite imagery
- Distinguish drought stress, pest damage, or wind throw from seasonal variation
- Identify persistent decline zones vs. short-term fluctuations
- Correlate forest anomalies with climate variables (SPI/SPEI)
- Generate stratified sampling plans for field verification
- Assess forest health by stand type (evergreen, deciduous, mixed)

## CLI Usage

```bash
# Basic health monitoring with bounding box
python scripts/forest_health_monitor.py \
  --bbox 116.0,39.0,117.0,40.0 \
  --forest-type evergreen \
  --year 2024

# With AOI file and custom indices
python scripts/forest_health_monitor.py \
  --aoi-file forest_aoi.geojson \
  --forest-type-file stand_types.geojson \
  --start-date 2022-01-01 \
  --end-date 2024-12-31 \
  --indices ndvi,evi,ndmi,nbr \
  --persistence 3 \
  --climate-attribution spi

# Full parameter set
python scripts/forest_health_monitor.py \
  --aoi-file aoi.geojson \
  --forest-type mixed \
  --baseline-years 5 \
  --indices ndvi,ndmi,nbr \
  --persistence 2 \
  --climate-attribution spei \
  --output-dir ./fhm-output \
  --overwrite

# Synthetic demo (no AOI/rasters needed)
python scripts/forest_health_monitor.py --synthetic --output-dir ./fhm-output
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--aoi-file` | — | AOI boundary (GeoJSON/Shapefile) |
| `--bbox` | — | Bounding box: xmin,ymin,xmax,ymax |
| `--place` | — | Named place (requires geocoding) |
| `--forest-type` | mixed | Forest type: evergreen, deciduous, mixed |
| `--forest-type-file` | — | Forest type polygons GeoJSON |
| `--year` | current | Monitoring year |
| `--start-date` | — | Start date (YYYY-MM-DD) |
| `--end-date` | — | End date (YYYY-MM-DD) |
| `--baseline-years` | 5 | Years for historical baseline |
| `--indices` | ndvi,evi,ndmi,nbr | Comma-separated spectral indices |
| `--persistence` | 2 | Persistence threshold (months) |
| `--climate-attribution` | spi | Climate variable: spi, spei, temperature, precipitation |
| `--severity-schema` | built-in | Custom severity schema JSON |
| `--output-dir` | fhm-output | Output directory |
| `--overwrite` | false | Allow overwriting existing output |
| `--synthetic` | false | Run with synthetic demo data (auto-generates NDVI/EVI rasters + AOI) |

## Output

| File | Description |
|---|---|
| `forest_health.tif` | Multi-temporal severity classification raster |
| `persistent_decline.geojson` | Zones with persistent decline |
| `climate_links.csv` | Climate attribution per zone |
| `timeseries.parquet` | Full health time series per zone |
| `sampling_plan.geojson` | Stratified sampling point recommendations |
| `request.json` | Input request record |
| `dataset-manifest.json` | Data source manifest |
| `output-manifest.json` | Output file manifest |
| `qa.json` | Quality assurance report |
| `run.log` | Execution log |

## Health Severity Levels

| Level | Code | Color | Criteria |
|---|---|---|---|
| Healthy | 0 | 00FF00 | All indices within 1 std of baseline |
| Mild Stress | 1 | FFFF00 | 1+ indices below 1.5 std, or alert state |
| Moderate Decline | 2 | FF9900 | 2+ indices below 1.5 std, decline state |
| Severe Decline | 3 | FF0000 | 2+ indices below 2.0 std, persistent decline |
| Mortality | 4 | 990000 | Extreme decline, absorbing state |

## Health State Machine

| State | Description | Transition |
|---|---|---|
| stable | Normal condition | → alert on anomaly |
| alert | Initial anomaly detected | → decline if persistent |
| decline | Sustained deterioration | → recovery if improving |
| recovery | Improving trend | → stable if sustained |
| mortality | Extreme decline (absorbing) | → recovery only with strong evidence |

## Key Design Principles

1. **Stratified baselines**: Each forest type (evergreen/deciduous/mixed) has
   its own phenological baseline. No universal threshold across all forests.
2. **Multi-index consensus**: At least 2 indices must agree before flagging
   high-confidence anomalies.
3. **Three independent dimensions**: Anomaly (deviation), Persistence (state
   machine), Attribution (climate correlation) are reported separately.
4. **Phenology-aware**: Deciduous winter NDVI drop is not flagged as disease
   because the baseline accounts for seasonal amplitude.

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |

## Limitations

- Species and age-class differences affect baseline accuracy
- Pest/disease attribution typically requires field data
- Long-term sensor differences require cross-normalization
- Output is remote sensing analysis support, not regulatory determination


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python forest_health_monitor.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--image`) 时，skill 自动下载数据。
当用户给 `--image` 时，走原文件路径 (向后兼容)。
