---
name: geoskill-groundwater-level-prediction
description: '基于历史水位时序与降水/开采驱动因子，用回归或随机森林预测未来地下水位并做空间插值与不确定性评估'
---

# 地下水位预测 | Groundwater Level Prediction

This skill predicts groundwater levels several steps ahead from historical water-level time series and driving factors (precipitation recharge, abstraction), then spatially interpolates the predictions into a regional raster. It is suited to scenarios such as groundwater dynamics analysis, over-extraction early warning, and water resource planning.

The core algorithm consists of three parts: **time-series decomposition** (a centered moving average extracts the trend component, periodic averaging extracts the seasonal component, and the remainder is the residual); **driver regression / random forest** (fits the water-level response using precipitation and its lagged recharge terms, abstraction, and the seasonal and trend components as features, then extrapolates `--predict-steps` months ahead); **spatial interpolation** (interpolates the predicted well-point water levels into a raster using inverse distance weighting, IDW). Uncertainty is characterized by the RMSE estimated with a temporal hold-out method and the prediction–truth correlation coefficient.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy' 'scikit-learn'
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-groundwater-level-prediction.py --bbox 116.0 39.0 117.0 40.0 --predict-steps 6
```

### Example 1 (Synthetic Data, Offline)

```bash
python geoskill-groundwater-level-prediction.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (Random Forest Method)

```bash
python geoskill-groundwater-level-prediction.py --bbox 116 39 117 40 --synthetic --method rf --predict-steps 12 --output-dir ./out
```

### Example 3 (Longer Prediction Horizon)

```bash
python geoskill-groundwater-level-prediction.py --bbox 114 30 115 31 --synthetic --predict-steps 24 --quiet
```

### Example 4 (Real Multi-temporal Water-Level Raster, band = Monthly Snapshot)

```bash
python geoskill-groundwater-level-prediction.py --input gwl_monthly.tif --predict-steps 6 --output-dir ./out
```

### Example 5 (Custom Seasonal Period + Random Seed)

```bash
python geoskill-groundwater-level-prediction.py --bbox 121 31 122 32 --synthetic --period 12 --seed 7 --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `predicted_level.tif` | GeoTIFF | Spatial interpolation raster of predicted water levels (EPSG:4326) |
| `prediction_curve.json` | JSON | Spatially averaged historical/predicted/truth curves + per-well RMSE |
| `output-manifest.json` | JSON | Run manifest (with QA: correlation coefficient, RMSE) |

## Data Source / 数据源 / Source

- `--input`: local multi-temporal water-level GeoTIFF (each band is a monthly snapshot).
- `--synthetic`: physically consistent well-point time series + driving factors (precipitation/abstraction), fully offline.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-groundwater-level-prediction
description: '基于历史水位时序与降水/开采驱动因子，用回归或随机森林预测未来地下水位并做空间插值与不确定性评估'
---

# 地下水位预测 | Groundwater Level Prediction

本 skill 从历史地下水位时序与驱动因子（降水补给、开采量）出发，预测未来若干步的水位，并把预测结果空间插值为区域栅格。适用于地下水动态分析、超采区预警、水资源规划等场景。

核心算法包括三部分：**时序分解**（居中滑动平均提取趋势项、按周期叠加提取季节项、剩余为残差）；**驱动回归 / 随机森林**（以降水及其滞后补给项、开采量、季节项、趋势项为特征拟合水位响应，外推 `--predict-steps` 个月）；**空间插值**（把井点预测水位用反距离加权 IDW 插值为栅格）。不确定性由时间留出法估计的 RMSE 与预测—真值相关系数刻画。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy' 'scikit-learn'
```

## 使用方法

### 基本用法

```bash
python geoskill-groundwater-level-prediction.py --bbox 116.0 39.0 117.0 40.0 --predict-steps 6
```

### 示例 1（合成数据，离线）

```bash
python geoskill-groundwater-level-prediction.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（随机森林方法）

```bash
python geoskill-groundwater-level-prediction.py --bbox 116 39 117 40 --synthetic --method rf --predict-steps 12 --output-dir ./out
```

### 示例 3（更长的预测步长）

```bash
python geoskill-groundwater-level-prediction.py --bbox 114 30 115 31 --synthetic --predict-steps 24 --quiet
```

### 示例 4（真实多时相水位栅格，band = 月份快照）

```bash
python geoskill-groundwater-level-prediction.py --input gwl_monthly.tif --predict-steps 6 --output-dir ./out
```

### 示例 5（自定义季节周期 + 随机种子）

```bash
python geoskill-groundwater-level-prediction.py --bbox 121 31 122 32 --synthetic --period 12 --seed 7 --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `predicted_level.tif` | GeoTIFF | 预测水位空间插值栅格（EPSG:4326） |
| `prediction_curve.json` | JSON | 空间均值历史/预测/真值曲线 + 逐井 RMSE |
| `output-manifest.json` | JSON | 运行清单（含 QA：相关系数、RMSE） |

## 数据源 / Source

- `--input`：本地多时相水位 GeoTIFF（每个 band 为一个月快照）。
- `--synthetic`：物理一致的井点时序 + 驱动因子（降水/开采），完全离线。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
