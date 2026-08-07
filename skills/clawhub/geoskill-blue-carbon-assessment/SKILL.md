---
name: blue-carbon-assessment
description: >
  Blue carbon ecosystem assessment - identify mangrove, salt marsh, and seagrass
  ecosystems, estimate carbon stocks, changes, and uncertainty using IPCC default
  factors or project-specific data.
---

## Prerequisites / 先准备 X 文件

> ⚠️ **必读** — 本 skill 不属于即用型，需要先准备特定文件才能跑。

本 skill 需要 **生态系统分类栅格**（GeoTIFF，class=1=红树林/2=盐沼/3=海草）。数据来源：GMW v3 / GLWD / 国家级海岸带调查。

👉 完整教程（含数据源 + 完整工作流）见仓库根目录 `PREREQUISITES.md` 1.1 节。

**先准备 X 文件**：先用 `--synthetic` 跑通，再换成真实数据。

快速试跑命令：

```bash
python blue_carbon_assessment.py --synthetic --output-dir ./test
```


# Blue Carbon Assessment

Identifies and maps blue carbon ecosystems (mangrove, salt marsh, seagrass),
estimates carbon stocks by pool (above-ground biomass, below-ground biomass, soil),
detects changes between time periods, and generates stratified sampling plans for
field validation.

## Trigger

Use when the user wants to:
- Estimate blue carbon stocks in coastal ecosystems
- Analyze carbon stock changes due to ecosystem loss or restoration
- Compare carbon densities across ecosystem types (mangrove, salt marsh, seagrass)
- Generate sampling plans for blue carbon field campaigns
- Produce screening-level carbon assessments for project planning

## CLI Usage

```bash
# Synthetic demo mode (no input files needed)
python scripts/blue_carbon_assessment.py --output-dir ./bca-output

# Assess only mangroves
python scripts/blue_carbon_assessment.py --ecosystem-type mangrove --output-dir ./bca-output

# With custom soil depth
python scripts/blue_carbon_assessment.py --soil-depth 0_200cm --output-dir ./bca-output

# Change detection with specific years
python scripts/blue_carbon_assessment.py --years "2015,2023" --output-dir ./bca-output

# With custom carbon factors
python scripts/blue_carbon_assessment.py --carbon-factors ./my_factors.json --output-dir ./bca-output
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--ecosystem-raster` | None | Path to ecosystem classification GeoTIFF (synthetic if omitted) |
| `--ecosystem-type` | all | Ecosystem type filter (mangrove/salt_marsh/seagrass/all) |
| `--boundary` | strict | Boundary type (strict/inclusive) |
| `--years` | 2020,2023 | Comma-separated years for change detection |
| `--carbon-factors` | None | Path to custom carbon factors JSON |
| `--soil-depth` | 0_100cm | Soil depth for carbon accounting (0_30cm/0_100cm/0_200cm) |
| `--uncertainty` | 0.95 | Confidence level for uncertainty interval (0.5-0.99) |
| `--output-dir` | ./bca-output | Output directory |

## Output

| File | Description |
|---|---|
| `report.html` | Human-readable blue carbon assessment report |
| `ecosystem_extent.npy` | Ecosystem classification raster (synthetic mode) |
| `blue_carbon_stock.npy` | Carbon stock per pixel (tC) |
| `change.geojson` | Change analysis results |
| `carbon_summary.csv` | Per-ecosystem carbon stock summary |
| `sampling_plan.geojson` | Stratified random sampling plan |
| `request.json` | Analysis request metadata |
| `dataset-manifest.json` | Dataset inventory |
| `output-manifest.json` | Output file inventory |
| `qa.json` | Quality assurance checks |

## Key Algorithms

### Carbon Stock Calculation
Total stock = Area x (AGB_density + BGB_density + Soil_density)
where AGB = above-ground biomass, BGB = below-ground biomass.
Soil carbon is depth-specific (0-30cm, 0-100cm, 0-200cm).

### Uncertainty Propagation
Root sum of squares (RSS) of independent errors from area mapping
(assumed 15% for raster-based), biomass factors, and soil factors.
Confidence intervals use Z-scores (1.96 for 95%).

### Change Detection
Compares ecosystem classification between two time periods.
Loss = all carbon pools released (simplified).
Gain = biomass accumulation only.
Stable area = soil carbon accumulation at published rates.

### Sampling Design
Stratified random sampling with Neyman-like allocation.
Sample size per stratum: n = (Z^2 * CV^2) / E^2
where CV = coefficient of variation, E = margin of error.

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |

## Important Limitations

- **Default factors are screening-level**: IPCC Tier 1 default carbon
  densities are global averages. Project-level assessments REQUIRE
  site-specific field sampling.
- **Soil carbon dominates**: Typically 70-90% of total blue carbon stock.
  Soil depth choice dramatically affects total estimates.
- **Simplified change model**: Loss assumes instant release of all pools.
  Gain assumes biomass only (no soil carbon recovery in first years).
- **No tidal/seasonal adjustment**: Ecosystem extent from remote sensing
  must account for tidal stage at time of image acquisition.
- **Seagrass mapping uncertainty**: Submerged vegetation is difficult to
  map from optical imagery; SAR or acoustic methods preferred.

## References

- IPCC 2013 Wetlands Supplement (Tier 1 default factors)
- Fourqurean et al. 2012 (seagrass carbon)
- Alongi 2014 (mangrove carbon cycling)
- Ouyang et al. 2017 (salt marsh accumulation)


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python blue_carbon_assessment.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--image`) 时，skill 自动下载数据。
当用户给 `--image` 时，走原文件路径 (向后兼容)。
