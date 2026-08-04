---
name: road-accessibility-analysis
description: >
  Compute shortest paths, isochrones, OD matrices, and facility service
  coverage from OSM or user-provided road networks. Supports drive/walk/cycle
  modes, road closures, and population coverage analysis. Use when the user
  needs travel-time analysis, service area delineation, or road network
  criticality assessment.
---

# Road Accessibility Analysis

Performs network analysis on road networks to compute shortest paths, isochrones (service areas), origin-destination matrices, facility coverage, and road closure impact scenarios.

## Trigger

Use when the user wants to:
- Compute shortest paths or travel times on road networks
- Generate isochrones / service areas from facilities
- Build OD matrices between origins and destinations
- Assess facility service coverage (hospitals, schools, etc.)
- Simulate road closure / disruption scenarios
- Identify critical edges whose removal degrades accessibility

## CLI Usage

```bash
# Shortest path between two points
python scripts/road_accessibility_analysis.py --network roads.geojson \
    --origins origins.geojson --destinations dest.geojson --mode drive

# Isochrone from facilities
python scripts/road_accessibility_analysis.py --network roads.geojson \
    --origins facilities.geojson --time-limit 15 30 60 --mode walk

# OD matrix
python scripts/road_accessibility_analysis.py --network roads.geojson \
    --origins origins.geojson --destinations dest.geojson --mode cycle

# With road closures
python scripts/road_accessibility_analysis.py --network roads.geojson \
    --origins origins.geojson --destinations dest.geojson \
    --closures closed_roads.geojson --mode drive

# With population coverage
python scripts/road_accessibility_analysis.py --network roads.geojson \
    --origins hospitals.geojson --time-limit 30 --mode drive \
    --population-raster pop.tif
```

## 数据下载

本 skill 可自动从公开数据源下载路网（无需预先准备数据）:

```bash
# OSM 路网 + MPC DEM (cop-dem-glo-30) 自动下载
python scripts/road_accessibility_analysis.py \
    --bbox 116.30,39.85,116.45,39.95 \
    --date-range 2024-06-01,2024-06-30 \
    --output-dir ./raa-auto

# 或用 AOI 多边形文件
python scripts/road_accessibility_analysis.py \
    --aoi-file aoi.geojson --date-range 2024-06-01,2024-06-30 \
    --output-dir ./raa-auto
```

下载的内容:
- **OSM 道路** (`highway` 要素) — 主输入，替换 `--network`
- **Copernicus DEM GLO-30** (`cop-dem-glo-30`) — 辅输入，写入 `downloaded/`

下载元数据（`data_source`, `fetched_at`, `osm_features`, `dem_path` 等）会写入 `output-manifest.json`。

## Parameters

| Parameter | Required | Default | Description |
|---|---|---|---|
| `--network` | Yes | — | Road network (GeoJSON/Shapefile, LineString features) |
| `--origins` | No | — | Origin points (GeoJSON, Point features) |
| `--destinations` | No | — | Destination points (GeoJSON, Point features) |
| `--mode` | No | `drive` | Travel mode: `drive`, `walk`, `cycle` |
| `--time-limit` | No | `30` | Time threshold(s) in minutes for isochrones |
| `--closures` | No | — | Closed road segments (GeoJSON, LineString features) |
| `--population-raster` | No | — | Population raster for coverage analysis (GeoTIFF) |
| `--output-dir` | No | `raa-output` | Output directory |
| `--speed-file` | No | — | JSON file with custom speed per road type |

## Output

| File | Description |
|---|---|
| `routes.geojson` | Shortest path routes (LineString features) |
| `service_areas.geojson` | Isochrone polygons per origin |
| `od_matrix.csv` | Origin-destination travel time/cost matrix |
| `unserved_population.tif` | Raster of population not covered by service areas |
| `critical_edges.geojson` | Edges whose removal most degrades accessibility |
| `output-manifest.json` | Machine-readable manifest |

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Validation error |
| 7 | Processing failure |
