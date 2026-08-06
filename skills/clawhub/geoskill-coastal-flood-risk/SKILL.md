---
name: coastal-flood-risk
description: >
  Coastal flood risk assessment using static bathtub inundation with ocean
  connectivity. Simulates sea level rise and storm surge scenarios, assesses
  population/building/infrastructure exposure, and identifies adaptation
  priority zones.
---

# Coastal Flood Risk

Static bathtub inundation model for coastal flood risk assessment. Simulates
flooding under sea level rise and storm surge scenarios, assesses exposure of
population, buildings, roads, and critical facilities, and identifies
adaptation priority zones.

## Trigger

Use when the user wants to:
- Simulate coastal flooding under sea level rise or storm surge scenarios
- Assess population and infrastructure exposure to coastal flooding
- Compare multiple flood scenarios (e.g., 0.5m/1m/2m SLR)
- Identify adaptation priority zones in coastal areas
- Generate flood risk reports for coastal planning

## CLI Usage

```bash
# Synthetic demo mode (no input files needed)
python scripts/coastal_flood_risk.py --output-dir ./cfr-output

# With custom water levels
python scripts/coastal_flood_risk.py --water-levels "0.5,1.0,2.0" --output-dir ./cfr-output

# With coastal defenses
python scripts/coastal_flood_risk.py --defense-height 2.0 --output-dir ./cfr-output

# Without ocean connectivity (pure bathtub)
python scripts/coastal_flood_risk.py --connectivity false --output-dir ./cfr-output
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--dem` | None | Path to DEM GeoTIFF (synthetic if omitted) |
| `--water-levels` | 0.5,1.0,2.0 | Comma-separated water levels in meters |
| `--vertical-datum` | MSL | Target vertical datum (MSL/NAVD88/WGS84/unknown) |
| `--connectivity` | true | Apply ocean connectivity filter |
| `--defense-height` | 0.0 | Coastal defense height in meters |
| `--defenses` | None | Path to defense vector/raster file |
| `--scenarios-config` | None | Path to flood scenarios JSON |
| `--output-dir` | ./cfr-output | Output directory |

## Output

| File | Description |
|---|---|
| `report.html` | Human-readable flood risk report |
| `priority_zones.geojson` | Adaptation priority zones |
| `exposure_by_scenario.csv` | Per-scenario exposure statistics |
| `depth_proxy.npy` | Depth proxy array (synthetic mode) |
| `request.json` | Analysis request metadata |
| `dataset-manifest.json` | Dataset inventory |
| `output-manifest.json` | Output file inventory |
| `qa.json` | Quality assurance checks |

## Key Algorithms

### Bathtub Inundation with Ocean Connectivity
Cells below the water level that are connected to the ocean (via flood-fill
from edge cells) are marked as flooded. This eliminates inland depressions
that are not actually connected to the sea — a common false positive in
simple bathtub models.

### Depth Proxy
Depth = water_level - elevation for flooded cells. This is a static proxy,
NOT true hydrodynamic depth. It overestimates depth in areas with drainage
or wave protection.

### Exposure Assessment
For each asset category (population, buildings, roads, critical facilities),
computes total exposed value, exposed fraction, and depth-weighted exposure.

### Priority Zones
Cells flooded in >= 2 scenarios AND with depth >= threshold are identified
as adaptation priority zones. Zones are ranked by priority score (depth x
n_scenarios).

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |

## Important Limitations

- **Static bathtub, NOT hydrodynamic**: This model does not simulate wave
  propagation, drainage, or tidal dynamics. Do not present results as
  "storm surge simulation" — it is a static inundation estimate.
- **Vertical datum critical**: DEM and water levels MUST share the same
  vertical datum. If the datum is unknown, results are RELATIVE only.
- **No defense data = unprotected scenario**: Without defense data, results
  represent an unprotected coastline. This is a worst-case estimate.
- **Connectivity eliminates false positives**: Inland depressions below sea
  level are correctly excluded when connectivity is enabled.

## References

- IPCC AR6 Sea Level Rise projections
- USACE Coastal flood risk assessment guidelines
- Eurocode flood hazard mapping standards


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python coastal_flood_risk.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--dem`) 时，skill 自动下载数据。
当用户给 `--dem` 时，走原文件路径 (向后兼容)。
