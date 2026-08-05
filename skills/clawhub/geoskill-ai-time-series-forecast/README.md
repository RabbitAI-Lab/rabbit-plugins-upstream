# AI Time-Series Forecasting (geoskill-ai-time-series-forecast)

> LSTM time-series forecasting network (torch+CUDA, default) + classical linear/polynomial/AR(p) interpretable baselines: multi-step extrapolation + holdout MAE/RMSE validation + per-pixel raster output

---

## 1. Overview

Performs single-layer LSTM multi-step extrapolation on remote sensing time series (per-pixel NDVI/temperature/backscatter), validates on a holdout period (MAE/RMSE), and outputs prediction rasters for each future step plus a per-pixel validation RMSE map. **Core model**: single-layer LSTM (many-to-one + recursive extrapolation), trained/inferred on torch + CUDA by default; pre-trained weights `ts_lstm_weights.pt` are bundled with the skill (if missing, they are automatically trained on the GPU at first run and saved to disk). Three interpretable classical baselines (`--method linear|poly|ar`) are also provided for comparison and for GPU-free environments. Each model family has unit tests against hand-computed references for fitting accuracy, AR coefficient recovery, and holdout MAE/RMSE.

## 2. Features

Performs single-layer LSTM multi-step extrapolation on remote sensing time series (per-pixel NDVI/temperature/backscatter), validates on a holdout period (MAE/RMSE), and outputs prediction rasters for each future step plus a per-pixel validation RMSE map. **Core model**: single-layer LSTM (many-to-one + recursive extrapolation), trained/inferred on torch + CUDA by default; pre-trained weights `ts_lstm_weights.pt` are bundled with the skill (if missing, they are automatically trained on the GPU at first run and saved to disk). Three interpretable classical baselines (`--method linear|poly|ar`) are also provided for comparison and for GPU-free environments. Each model family has unit tests against hand-computed references for fitting accuracy, AR coefficient recovery, and holdout MAE/RMSE.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-ai-time-series-forecast.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `forecast.tif` | GeoTIFF | Predictions for the future horizon steps (one band per step) |
| `validation_rmse.tif` | GeoTIFF | Per-pixel holdout validation RMSE |
| `forecast_report.json` | JSON | Global/center-pixel predictions and error metrics |
| `output-manifest.json` | JSON | Run manifest (input/output/QA/exit code) |


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

# AI时序预测（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-ai-time-series-forecast
description: 'LSTM 时序预测网络（torch+CUDA，默认） + 经典线性/多项式/AR(p) 解释基线：多步外推 + 留出 MAE/RMSE 验证 + 逐像元栅格输出'
---

# AI时序预测 | AI Time Series Forecast

对遥感时序（逐像元 NDVI/温度/后向散射）做单层 LSTM 多步外推，并在留出时段上验证（MAE/RMSE），输出未来各步预测栅格与逐像元验证 RMSE 图。

**核心模型**：单层 LSTM（many-to-one + 递归外推），默认在 torch + CUDA 上训练/推理；随 skill 附带预训练权重 `ts_lstm_weights.pt`（缺失时在首次运行时在 GPU 上自动训练并落盘）。同时保留三套可解释经典基线（`--method linear|poly|ar`）用于对比与无 GPU 环境。每一类模型的拟合精度、AR 系数恢复、留出 MAE/RMSE 均有手算基准的单元测试。

## 依赖

```bash
pip install numpy rasterio scipy torch --index-url https://download.pytorch.org/whl/cu121
```

如要跑经典基线方法（`--method linear|poly|ar`）无需 torch。

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-ai-time-series-forecast.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2：合成时序预测（离线）

```bash
python geoskill-ai-time-series-forecast.py --bbox 116.0 39.0 117.0 40.0 --synthetic --method linear --horizon 4 --output-dir ./out
```

### 示例 3：多项式趋势外推

```bash
python geoskill-ai-time-series-forecast.py --bbox 116.0 39.0 117.0 40.0 --synthetic --method poly --degree 2 --horizon 6 --output-dir ./out
```

### 示例 4：自回归模型

```bash
python geoskill-ai-time-series-forecast.py --input series.tif --method ar --order 3 --horizon 3 --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `forecast.tif` | GeoTIFF | 未来 horizon 步预测（每步一个波段） |
| `validation_rmse.tif` | GeoTIFF | 逐像元留出验证 RMSE |
| `forecast_report.json` | JSON | 全局/中心像元预测与误差指标 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/退出码） |

## 数据源 / Source

本地多波段 GeoTIFF（波段 = 时间步），或 --synthetic（趋势 + 年周期 + 噪声的 NDVI 式立方体）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
