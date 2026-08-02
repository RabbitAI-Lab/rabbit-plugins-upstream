---
name: lidar-point-cloud-analysis
description: >
  Read LAS/LAZ/COPC point clouds, compute statistics, classification QA,
  DEM/DSM/CHM rasters, cross-sections, density maps, and quality reports.
  Use when analyzing LiDAR point cloud data, generating terrain models,
  checking point cloud quality, or producing canopy height models.
---

## Prerequisites / 先准备 X 文件

> ⚠️ **必读** — 本 skill 不属于即用型，需要先准备特定文件才能跑。

本 skill 需要 **LAS/LAZ 点云文件**，不自动下载（数据太大且按需购买）。

👉 完整教程见仓库根目录 `PREREQUISITES.md` 2.5 节。

**先准备 X 文件**：不传 `--input` 直接跑，用合成点云验证工作流。

快速试跑命令：

```bash
python lidar_point_cloud_analysis.py --output-dir ./test
```


# LiDAR Point Cloud Analysis

Reads LAS/LAZ/COPC point clouds, computes statistics, classification QA,
DEM/DSM/CHM rasters, cross-sections, density maps, and quality reports.

## Trigger

Use when the user wants to:
- Generate DEM/DSM/CHM from LiDAR point cloud data
- Check point cloud density, classification, and quality
- Extract cross-section profiles from point clouds
- Compute multi-temporal DEM differences for change detection
- Produce canopy height models for forestry analysis
- Assess point cloud data quality and coverage

## CLI Usage

```bash
# Synthetic demo mode (no input files needed)
python scripts/lidar_point_cloud_analysis.py --output-dir ./lpca-output

# With custom resolution and all products
python scripts/lidar_point_cloud_analysis.py \
  --resolution 0.5 \
  --products dem,dsm,chm,density,qa \
  --output-dir ./lpca-output

# DEM only with specific bounding box (legacy 4-floats form)
python scripts/lidar_point_cloud_analysis.py \
  --bbox-bounds 0 0 500 500 \
  --products dem \
  --resolution 1.0 \
  --output-dir ./lpca-output
```

## Data Download (interface reserved)

This skill works on **local LAS/LAZ point clouds** and does not auto-download
from any data source. The standard `--bbox / --date-range / --aoi-file` CLI
flags are exposed (from the shared `_geoskill_data_fetcher` library) so that a
future integration with the USGS 3DEP, OpenTopography, or ESA Copernicus DEM
endpoints can be added without changing the CLI surface.

```bash
# Reserved: --bbox is parsed to drive the synthetic-data bounds.
# (no actual download happens; this is the interface contract.)
python scripts/lidar_point_cloud_analysis.py \
  --bbox 116,39,117,40 \
  --date-range 2024-06-01,2024-06-30 \
  --output-dir ./lpca-output
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--input` | None | Input LAS/LAZ file path (optional, uses synthetic data if omitted) |
| `--output-dir` | ./lpca-output | Output directory |
| `--resolution` | 1.0 | Raster resolution in meters |
| `--ground-method` | grid_min | Ground classification: grid_min, pmf |
| `--products` | dem,dsm,chm,density,qa | Comma-separated products to generate |
| `--tile-size` | 100.0 | Tile size in meters for QA |
| `--bbox-bounds` | None | (legacy) Bounding box for synthetic data: xmin ymin xmax ymax |
| `--bbox` | None | Bounding box W,S,E,N (shared flag, drives synthetic-data bounds) |
| `--date-range` | None | Date range START,END in ISO-8601 (reserved for future DEM endpoint) |
| `--aoi-file` | None | Optional GeoJSON AOI polygon (reserved) |

## Output

| File | Description |
|---|---|
| `dem.tif` | Digital Elevation Model (bare earth) |
| `dsm.tif` | Digital Surface Model (first return) |
| `chm.tif` | Canopy Height Model (DSM - DEM) |
| `density.tif` | Point density map (points/m²) |
| `profiles.geojson` | Cross-section profiles as GeoJSON |
| `pointcloud_qa.json` | Point cloud statistics and QA results |
| `request.json` | Analysis request metadata |
| `dataset-manifest.json` | Dataset inventory |
| `output-manifest.json` | Output file inventory and raster info |
| `qa.json` | Quality assurance checks |

## Products

| Code | Name | Description |
|---|---|---|
| dem | Digital Elevation Model | Ground surface (minimum Z per cell) |
| dsm | Digital Surface Model | Surface including objects (maximum Z per cell) |
| chm | Canopy Height Model | Height above ground (DSM - DEM) |
| density | Point Density | Points per square meter |
| qa | Quality Report | Statistics and quality checks |

## Ground Classification Methods

| Method | Description |
|---|---|
| grid_min | Grid-based lowest point classification with slope threshold |
| pmf | Progressive Morphological Filter (requires scipy) |

## ASPRS Classification Codes

| Code | Name |
|---|---|
| 0 | Created, Never Classified |
| 1 | Unassigned |
| 2 | Ground |
| 3 | Low Vegetation |
| 4 | Medium Vegetation |
| 5 | High Vegetation |
| 6 | Building |
| 7 | Low Point (Noise) |
| 8 | Model Key-point |
| 9 | Water |
| 10-18 | Reserved (Rail, Road, Wire, Bridge, etc.) |

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |

## Limitations

- LAS/LAZ reading requires laspy (falls back to synthetic data if not installed)
- Ground classification is simplified; production workflows should use PDAL
- Large files may require streaming/chunking (not yet implemented for LAS input)
- Vertical datum is assumed consistent; no datum transformation
- Multi-temporal difference requires co-registered point clouds

## References

- ASPRS LAS Specification (ASPRS 1.4)
- IPCC Good Practice Guidance for Land Use
- OpenTopography Point Cloud Processing Guidelines
