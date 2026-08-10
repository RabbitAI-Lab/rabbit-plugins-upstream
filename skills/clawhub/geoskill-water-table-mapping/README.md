# Groundwater Table Mapping (geoskill-water-table-mapping)

> Interpolates water table and depth-to-water rasters from discrete well observations via IDW or simplified kriging, with leave-one-out cross-validation

---

## 1. Overview

This skill generates regional groundwater table rasters and depth-to-water (distance from the water table to the surface) rasters by spatially interpolating water level observations from discrete monitoring wells. It is suitable for groundwater contour mapping, depth zoning, and well network assessment. Core algorithms: two interpolation methods are provided — **IDW (Inverse Distance Weighting)**, pixel value = Σ(valueᵢ/dᵢᵖ)/Σ(1/dᵢᵖ), robust and fast; **simplified Ordinary Kriging**, which uses an exponential variogram and solves the kriging system with an unbiasedness constraint to obtain the best linear unbiased estimate. **Terrain constraint** is supported (the water table must not exceed the surface elevation). Accuracy is assessed via **leave-one-out cross-validation** statistics: RMSE / MAE / R².

## 2. Features

This skill generates regional groundwater table rasters and depth-to-water (distance from the water table to the surface) rasters by spatially interpolating water level observations from discrete monitoring wells. It is suitable for groundwater contour mapping, depth zoning, and well network assessment. Core algorithms: two interpolation methods are provided — **IDW (Inverse Distance Weighting)**, pixel value = Σ(valueᵢ/dᵢᵖ)/Σ(1/dᵢᵖ), robust and fast; **simplified Ordinary Kriging**, which uses an exponential variogram and solves the kriging system with an unbiasedness constraint to obtain the best linear unbiased estimate. **Terrain constraint** is supported (the water table must not exceed the surface elevation). Accuracy is assessed via **leave-one-out cross-validation** statistics: RMSE / MAE / R².

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-water-table-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out
```

## 4. CLI Parameters

Run `python <skill>.py --help` for the full list. Common parameters:

| Parameter | Type | Description |
|---|---|---|
| `--bbox` | `float[4]` | WGS84 bounding box `min_lon min_lat max_lon max_lat` |
| `--input` | `path` | Local input file (GeoJSON/GeoTIFF/etc.) |
| `--output-dir` | `path` | Output directory (default `./output`) |
| `--synthetic` | `flag` | Use synthetic data instead of real input |
| `--quiet` | `flag` | Suppress non-essential stdout |

## 5. Input / Output

| File | Format | Description |
|---|---|---|
| `water_table.tif` | GeoTIFF | Groundwater table raster (m, terrain-constrained) |
| `depth_to_water.tif` | GeoTIFF | Depth-to-water raster = DEM − water table (m) |
| `interpolation_report.json` | JSON | Cross-validation (RMSE/MAE/R²) + comparison with synthetic ground truth |
| `output-manifest.json` | JSON | Run manifest |

## 6. Technical Principle

(see SKILL.md for details)

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 地下水位空间制图（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-water-table-mapping
description: '由离散井点水位通过IDW或简化克里金插值生成地下水位与埋深栅格，含留一法交叉验证'
---

# 地下水位空间制图 | Water Table Mapping

本 skill 由离散监测井点的水位观测，经空间插值生成区域地下水位栅格与埋深（水位到地表深度）栅格，适用于地下水等水位线图编制、埋深分区、井网评估等场景。

核心算法：提供两种插值方法——**IDW（反距离加权）**，像元值 = Σ(valueᵢ/dᵢᵖ)/Σ(1/dᵢᵖ)，稳健快速；**简化普通克里金（Ordinary Kriging）**，采用指数型变异函数，求解带无偏约束的克里金方程组得最优线性无偏估计。支持**地形约束**（地下水位不得高于地表高程）。精度由**留一法交叉验证**统计 RMSE / MAE / R² 评估。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-water-table-mapping.py --bbox 116.0 39.0 117.0 40.0 --method idw
```

### 示例 1（合成数据，离线）

```bash
python geoskill-water-table-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（克里金插值）

```bash
python geoskill-water-table-mapping.py --bbox 116 39 117 40 --synthetic --method kriging --output-dir ./out
```

### 示例 3（真实井点 CSV：列 x/lon, y/lat, level）

```bash
python geoskill-water-table-mapping.py --input wells.csv --bbox 116 39 117 40 --grid-size 128 --output-dir ./out
```

### 示例 4（自定义 IDW 幂次与井点数）

```bash
python geoskill-water-table-mapping.py --bbox 121 31 122 32 --synthetic --power 3 --n-wells 60 --quiet
```

### 示例 5（更细的输出网格）

```bash
python geoskill-water-table-mapping.py --bbox 113 23 114 24 --synthetic --method idw --grid-size 256 --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `water_table.tif` | GeoTIFF | 地下水位空间栅格（m，受地形约束） |
| `depth_to_water.tif` | GeoTIFF | 埋深栅格 = DEM − 水位（m） |
| `interpolation_report.json` | JSON | 交叉验证（RMSE/MAE/R²）+ 与真值对比（合成） |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- `--input`：本地井点 CSV，自动识别坐标列（x/lon）与水位列（level/water_level/head）。
- `--synthetic`：带空间渐变与观测噪声的井点 + 真值水位场 + DEM，完全离线。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
