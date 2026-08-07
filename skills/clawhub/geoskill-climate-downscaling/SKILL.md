---
name: geoskill-climate-downscaling
description: '统计降尺度：用多元回归建立粗分辨率气候变量与高分辨率地形预测因子的关系，并对残差做空间插值，生成高分辨率气候栅格'
---

# 气候降尺度 | Climate Downscaling

This skill implements **statistical downscaling**, which downscales coarse-resolution climate variables (temperature/precipitation) to high resolution. The core workflow is "terrain regression + residual spatial interpolation":

1. Derive predictors from the high-resolution DEM: elevation and slope.
2. Average the DEM and the ground-truth blocks onto the coarse-resolution grid to form regression samples.
3. Build the relationship climate variable ~ elevation + slope with multiple linear regression (scikit-learn `LinearRegression`); in the temperature scenario, the elevation coefficient is the lapse rate.
4. Extrapolate the regression model to the high-resolution grid and interpolate the coarse-grid residuals back to high resolution using scipy linear interpolation.
5. Downscaled result = high-resolution regression prediction + high-resolution interpolated residuals.

Outputs a high-resolution downscaled raster, a regression/residual component stack, and a validation report (correlation coefficient against ground truth, RMSE, improvement over the coarse-resolution baseline, lapse rate). Suitable for regional climate refinement, spatialization of temperature/precipitation over complex terrain, and preparation of forcing fields for ecological and hydrological models.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy' 'scikit-learn'
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-climate-downscaling.py --bbox 116.0 39.0 117.0 40.0 [other parameters]
```

### Example 1 (Synthetic Data, Offline)

```bash
python geoskill-climate-downscaling.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (bbox Only, Automatic Synthesis)

```bash
python geoskill-climate-downscaling.py --bbox 100.0 26.0 104.0 30.0 --output-dir ./out
```

### Example 3 (Specify Target Grid Size)

```bash
python geoskill-climate-downscaling.py --bbox 100.0 26.0 104.0 30.0 --target-resolution 128 --synthetic --output-dir ./out
```

### Example 4 (Quiet Mode)

```bash
python geoskill-climate-downscaling.py --bbox 100.0 26.0 104.0 30.0 --synthetic --output-dir ./out --quiet
```

### Example 5 (Real Raster Input, band1=DEM, band2=Ground Truth, band3=Coarse Climate Field)

```bash
python geoskill-climate-downscaling.py --input dem_truth_coarse.tif --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `downscaled.tif` | GeoTIFF | High-resolution downscaled climate raster |
| `downscaling_components.tif` | GeoTIFF | Regression component + residual component (2 bands) |
| `validation_report.json` | JSON | Regression coefficients, correlation, RMSE, lapse rate |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- **Real mode**: local multi-band GeoTIFF (band1=high-resolution DEM, band2=ground truth to be downscaled, band3=coarse-resolution climate field).
- **Synthetic mode** (`--synthetic` or `--bbox` only): generates a "temperature decreasing with elevation" scenario locally, with no network access required.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network access at all.
- All processing is performed locally; no user data is uploaded.

## License / License

MIT

---


<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-climate-downscaling
description: '统计降尺度：用多元回归建立粗分辨率气候变量与高分辨率地形预测因子的关系，并对残差做空间插值，生成高分辨率气候栅格'
---

# 气候降尺度 | Climate Downscaling

本 skill 实现**统计降尺度**（statistical downscaling），将粗分辨率气候变量
（温度/降水）降尺度到高分辨率，核心流程为"地形回归 + 残差空间插值"：

1. 由高分辨率 DEM 提取预测因子：高程（elevation）与坡度（slope）。
2. 将 DEM 与真值块平均到粗分辨率格点，构成回归样本。
3. 用多元线性回归（scikit-learn `LinearRegression`）建立
   气候变量 ~ 高程 + 坡度 的关系；温度场景下高程系数即气温递减率 lapse rate。
4. 将回归模型外推到高分辨率格网，并把粗格点残差用 scipy 线性插值回到高分辨率。
5. 降尺度结果 = 高分辨率回归预测 + 高分辨率插值残差。

输出高分辨率降尺度栅格、回归/残差分量栈与验证报告（与真值相关系数、RMSE、
相对粗分辨率基线的改进、递减率）。适用于区域气候精细化、复杂地形气温/降水
空间化、生态与水文模型的强迫场准备。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy' 'scikit-learn'
```

## 使用方法

### 基本用法

```bash
python geoskill-climate-downscaling.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例 1（合成数据，离线）

```bash
python geoskill-climate-downscaling.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（仅给 bbox，自动合成）

```bash
python geoskill-climate-downscaling.py --bbox 100.0 26.0 104.0 30.0 --output-dir ./out
```

### 示例 3（指定目标网格尺寸）

```bash
python geoskill-climate-downscaling.py --bbox 100.0 26.0 104.0 30.0 --target-resolution 128 --synthetic --output-dir ./out
```

### 示例 4（静默模式）

```bash
python geoskill-climate-downscaling.py --bbox 100.0 26.0 104.0 30.0 --synthetic --output-dir ./out --quiet
```

### 示例 5（真实栅格输入，band1=DEM，band2=真值，band3=粗气候场）

```bash
python geoskill-climate-downscaling.py --input dem_truth_coarse.tif --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `downscaled.tif` | GeoTIFF | 高分辨率降尺度气候栅格 |
| `downscaling_components.tif` | GeoTIFF | 回归分量 + 残差分量（2 波段） |
| `validation_report.json` | JSON | 回归系数、相关、RMSE、递减率 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- **真实模式**：本地多波段 GeoTIFF（band1=高分辨率 DEM，band2=待降尺度真值，band3=粗分辨率气候场）。
- **合成模式**（`--synthetic` 或仅 `--bbox`）：本地生成"温度随高程递减"场景，无需网络。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
