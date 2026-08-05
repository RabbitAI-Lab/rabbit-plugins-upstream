---
name: geoskill-water-table-mapping
description: '由离散井点水位通过IDW或简化克里金插值生成地下水位与埋深栅格，含留一法交叉验证'
---

# 地下水位空间制图 | Water Table Mapping

This skill generates regional groundwater level rasters and depth-to-water (surface-to-water-table depth) rasters from water level observations at discrete monitoring wells via spatial interpolation, applicable to groundwater contour mapping, depth zoning, and well network assessment.

Core algorithms: two interpolation methods are provided — **IDW (Inverse Distance Weighting)**, pixel value = Σ(valueᵢ/dᵢᵖ)/Σ(1/dᵢᵖ), robust and fast; and **simplified Ordinary Kriging**, which uses an exponential variogram and solves the kriging system with an unbiasedness constraint to obtain the best linear unbiased estimate. **Terrain constraints** are supported (the water table must not exceed the surface elevation). Accuracy is assessed with **leave-one-out cross-validation** statistics (RMSE / MAE / R²).

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-water-table-mapping.py --bbox 116.0 39.0 117.0 40.0 --method idw
```

### Example 1 (Synthetic Data, Offline)

```bash
python geoskill-water-table-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (Kriging Interpolation)

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

### Example 5 (Finer Output Grid)

```bash
python geoskill-water-table-mapping.py --bbox 113 23 114 24 --synthetic --method idw --grid-size 256 --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `water_table.tif` | GeoTIFF | Groundwater level spatial raster (m, terrain-constrained) |
| `depth_to_water.tif` | GeoTIFF | Depth-to-water raster = DEM − water level (m) |
| `interpolation_report.json` | JSON | Cross-validation (RMSE/MAE/R²) + comparison against ground truth (synthetic) |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- `--input`: local well CSV; coordinate columns (x/lon) and water level columns (level/water_level/head) are auto-detected.
- `--synthetic`: wells with spatial gradients and observational noise + ground-truth water level field + DEM, fully offline.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
