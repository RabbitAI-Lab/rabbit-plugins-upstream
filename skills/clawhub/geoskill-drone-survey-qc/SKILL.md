---
name: drone-survey-qc
description: >
  Automated quality inspection for UAV/drone survey deliverables including
  aerial images, orthomosaics, DSM/DEM, control points, and aerial
  triangulation reports. Generates coverage, clarity, seam, and accuracy QA.
---

## Prerequisites / 先准备 X 文件

> ⚠️ **必读** — 本 skill 不属于即用型，需要先准备特定文件才能跑。

本 skill 需要 **无人机航测项目目录**（含 ortho.tif / dsm.tif / 相机位置 / 控制点）。

👉 完整教程见仓库根目录 `PREREQUISITES.md` 2.2 节。

**先准备 X 文件**：把航测交付包按指定结构组织好；没有就先用 `--synthetic` 跑。

快速试跑命令：

```bash
python drone_survey_qc.py --project-dir ./my_drone_project --output-dir ./qc
```


# Drone Survey QC

Automated quality inspection for UAV survey deliverables. Checks drone aerial
images, orthomosaics, DSM/DEM, control points, and aerial triangulation
reports. Generates coverage, clarity, seam, and accuracy QA.

## Trigger

Use when the user wants to:
- Check drone orthomosaic for holes, blur, or seam issues
- Summarize control point residuals and generate acceptance reports
- Verify image overlap and GSD meet project specifications
- Inspect DSM/DEM for nodata holes and elevation anomalies
- Generate a comprehensive QC report for survey deliverables

## CLI Usage

```bash
# Synthetic demo mode (no input files needed)
python scripts/drone_survey_qc.py --output-dir ./dsq-output

# With project directory
python scripts/drone_survey_qc.py --project-dir ./survey-project --output-dir ./dsq-output

# With custom QC standards
python scripts/drone_survey_qc.py --standard-config ./my-standards.json --output-dir ./dsq-output
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--project-dir` | None | Project directory to analyze |
| `--orthomosaic` | None | Path to orthomosaic GeoTIFF |
| `--dsm` | None | Path to DSM/DEM GeoTIFF |
| `--camera-positions` | None | Path to camera positions CSV/JSON |
| `--control-points` | None | Path to control points CSV/JSON |
| `--standard-config` | None | Path to QC standards JSON (default: references/qc_standards.json) |
| `--output-dir` | ./dsq-output | Output directory |

## Output

| File | Description |
|---|---|
| `qc.json` | Comprehensive QC results with all metrics |
| `issues.geojson` | GeoJSON FeatureCollection of QC issues |
| `image_quality.csv` | Per-image quality metrics (blur, exposure) |
| `control_point_residuals.csv` | Control point residual analysis |
| `qc_report.html` | Human-readable HTML QC report |
| `request.json` | Analysis request metadata |
| `dataset-manifest.json` | Dataset inventory |
| `output-manifest.json` | Output file inventory |
| `qa.json` | Quality assurance checks |

## QC Standards

Default thresholds from `references/qc_standards.json`:

| Check | Minimum | Preferred |
|---|---|---|
| Forward overlap | 70% | 80% |
| Side overlap | 60% | 70% |
| GSD | <5.0 cm/px | <3.0 cm/px |
| Blur (Laplacian var) | >50 | >100 |
| GCP RMSE_XY | <5 cm | <3 cm |
| Ortho nodata | <2% | - |
| DSM nodata | <5% | - |

## Key Algorithms

### Blur Detection
Uses Laplacian variance — lower values indicate blurrier images.
Threshold: variance < 50 = blurry.

### Overlap Analysis
Computes ground footprint from camera parameters (altitude, focal length,
sensor size) and calculates intersection-over-minimum-area for adjacent
pairs. Classifies pairs as forward (same strip) or side (cross-strip) using
strip clustering on cross-strip coordinate.

### Control Point Analysis
Computes XY, Z, and 3D residuals. Reports RMSE, max residual, and detects
outliers using Median Absolute Deviation (MAD) with σ ≈ 1.4826 × MAD.

### GSD Computation
GSD (cm/px) = (altitude × sensor_width) / (focal_length × image_width) × 100

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |

## Limitations

- Synthetic demo mode only; file-based mode requires GeoTIFF/CSV input
- Blur detection is resolution-dependent; calibrate thresholds for your sensor
- Control point outlier detection requires ≥7 points for MAD-based method
- Does not replace certified survey inspection for legal/compliance purposes

## References

- CH/T 9024-2014 无人机航测规范
- DJI Pilot flight planning specifications
- ASPRS Positional Accuracy Standards for Digital Geospatial Data


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python drone_survey_qc.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--orthomosaic`) 时，skill 自动下载数据。
当用户给 `--orthomosaic` 时，走原文件路径 (向后兼容)。
