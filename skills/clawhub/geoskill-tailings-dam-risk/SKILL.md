---
name: tailings-dam-risk
description: >
  Screen tailings dam bodies, reservoir areas, catchments, and downstream
  exposure using remote sensing change detection. Produce patrol priorities
  based on hazard, exposure, and evidence.
---

## Prerequisites / 先准备 X 文件

> ⚠️ **必读** — 本 skill 不属于即用型，需要先准备特定文件才能跑。

本 skill 需要 **设施清单 JSON**（geometry + 属性）。`--bbox` 模式下 DEM 和 Sentinel-2 时序自动从 MPC 下载。

👉 完整教程见仓库根目录 `PREREQUISITES.md` 1.6 节。

**先准备 X 文件**：先准备一份 `facilities.json`（可手写小样本），其他自动下载。

快速试跑命令：

```bash
python tailings_dam_risk.py --bbox 116.30,39.85,116.45,39.95 --date-range 2023-06-01,2023-09-30 --facilities facilities.json --output-dir ./tdr
```


# Tailings Dam Risk

Screens tailings dam facilities using remote sensing and DEM analysis.
Produces risk rankings and patrol priorities based on multi-temporal change
detection, catchment analysis, and downstream exposure assessment.

## Trigger

Use when the user wants to:
- Screen tailings dam facilities for safety risks
- Detect water surface changes in tailings reservoirs
- Analyze upstream catchment contributions
- Estimate downstream impact zones from potential dam failure
- Identify exposed objects (buildings, roads, population) downstream
- Generate risk reports for patrol prioritization
- Assess deformation patterns from InSAR data

## CLI Usage

```bash
# Basic screening with synthetic data (demo)
python scripts/tailings_dam_risk.py --output-dir ./tdr-output

# With custom facilities file
python scripts/tailings_dam_risk.py \
  --facilities facilities.json \
  --output-dir ./tdr-output

# With DEM and water masks
python scripts/tailings_dam_risk.py \
  --dem-file dem.tif \
  --water-masks water_2019.tif water_2021.tif water_2023.tif \
  --output-dir ./tdr-output

# Full analysis with all options
python scripts/tailings_dam_risk.py \
  --facilities facilities.json \
  --dem-file dem.tif \
  --water-masks water_2019.tif water_2021.tif \
  --deformation-data insar_deformation.tif \
  --exposure-objects downstream_objects.json \
  --rainfall-scenario 500yr \
  --runout-method simplified \
  --deformation-threshold 15.0 \
  --exposure-radius 8000.0 \
  --output-dir ./tdr-output
```

## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载 DEM 和 Sentinel-2 (无需 API key):

```bash
# 自动下载 cop-dem-glo-30 DEM + sentinel-2-l2a 水体变化快照
python scripts/tailings_dam_risk.py \
    --bbox 116.30,39.85,116.45,39.95 \
    --date-range 2023-06-01,2023-09-30 \
    --output-dir ./tdr-auto
```

下载的内容:
- **Copernicus DEM GLO-30** (`cop-dem-glo-30`) — 替换 `--dem-file`
- **Sentinel-2 L2A** (`sentinel-2-l2a`) — 2 个时相的影像，生成水体变化，替换 `--water-masks`

下载元数据（`data_source`, `fetched_at`, `collection`, `dem_path`, `sentinel2_paths`）会写入 `output-manifest.json`。

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--facilities` | None | Path to facilities JSON file with geometry and attributes |
| `--dem-file` | None | Path to DEM GeoTIFF file |
| `--water-masks` | None | Input water mask GeoTIFF files (ordered by time) |
| `--deformation-data` | None | Path to InSAR deformation rate GeoTIFF (mm/yr) |
| `--exposure-objects` | None | Path to downstream exposure objects JSON |
| `--rainfall-scenario` | 100yr | Rainfall scenario: 100yr, 500yr, 1000yr |
| `--runout-method` | simplified | Runout method: simplified, energy_line |
| `--deformation-threshold` | 10.0 | Deformation threshold in mm/yr |
| `--exposure-radius` | 5000.0 | Exposure analysis radius in meters |
| `--risk-rules` | None | Path to custom risk scoring rules JSON |
| `--output-dir` | ./tdr-output | Output directory |

## Output

| File | Description |
|---|---|
| `facility_changes.geojson` | Water surface change polygons (expansion/contraction) |
| `catchments.geojson` | Upstream catchment boundaries |
| `screening_zones.geojson` | Runout/impact zones |
| `downstream_exposure.csv` | Downstream exposure statistics |
| `risk_report.html` | Risk screening report |
| `request.json` | Analysis request metadata |
| `dataset-manifest.json` | Dataset inventory and quality info |
| `output-manifest.json` | Output file inventory and results |
| `qa.json` | Quality assurance checks |
| `run.log` | Execution log |

## Risk Levels

| Code | Name | Description |
|---|---|---|
| 3 | HIGH | Combined score >= 70 |
| 2 | MEDIUM | Combined score >= 40 |
| 1 | LOW | Combined score >= 20 |
| 0 | UNKNOWN | Combined score < 20 |

## Risk Components

### Hazard (40%)
Based on dam height, capacity, water surface change, catchment size,
and runout potential.

### Exposure (35%)
Based on number of objects in impact zone and exposure area.

### Evidence (25%)
Based on observed water surface changes and catchment characteristics.

## Key Algorithms

### Water Surface Change Detection
Compares binary water masks between time periods to detect expansion
and contraction areas. Calculates change percentage and extracts
change polygons.

### Catchment Analysis
Uses D8 flow direction algorithm on DEM to compute flow accumulation
and delineate upstream watershed contributing to the dam location.

### Runout Zone Estimation
Two simplified methods for screening:
- **Simplified**: Uses reach angle concept (height / tan(alpha))
- **Energy_line**: Uses H/L ratio to estimate flow extent

Both methods are SCREENING-ONLY and do not replace engineering analysis.

### Downstream Exposure
Analyzes objects within potential impact zone. Counts buildings,
roads, and other infrastructure at risk.

### Deformation Analysis
Processes InSAR deformation data to identify areas with significant
movement exceeding threshold.

### Rainfall Scenario
Estimates peak flow using rational method (Q = C * i * A) for
different return period events.

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |

## Limitations

- **SCREENING ONLY**: Results are auxiliary analysis only and do NOT
  replace dam safety engineering assessment
- Simplified runout models are not substitutes for detailed
  engineering analysis
- Facility data completeness affects result confidence
- Free satellite imagery may not detect fine cracks or small deformations
- All results must be reviewed by qualified engineers before
  making safety decisions

## Data Requirements

- DEM: Any resolution (30m SRTM or 12m PALSAR recommended)
- Water masks: Binary (0/1) rasters from NDWI/MNDWI or classification
- Deformation data: InSAR-derived rate map (mm/yr, optional)
- Facilities: GeoJSON with geometry and optional dam_height, capacity

## References

- US Dam Safety Guidelines (FEMA 1998)
- ICOLD Bulletin 153: Tailings Dams - Risk of Dangerous Occurrences
- Hungr et al. 1984: Debris flow runout estimation


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python tailings_dam_risk.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--dem`) 时，skill 自动下载数据。
当用户给 `--dem` 时，走原文件路径 (向后兼容)。
