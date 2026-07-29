---
name: phenology-metrics
description: 'Extract phenological metrics from NDVI/EVI time series data. Computes description: 'Extract phenological metrics from NDVI/EVI time series data. Computes SOS, EOS,  LOS, peak value/date, amplitude, and integral using threshold, derivative,  or double logistic fitting methods.  '
---

# Phenology Metrics

Extract vegetation phenology metrics from NDVI/EVI time series. Supports threshold, derivative, and double logistic fitting methods.

## Features

- **Key metrics**: SOS, EOS, LOS, Peak value, Peak date, Amplitude, Integral
- **Threshold method**: 10%/50% of amplitude ratio
- **Derivative method**: Inflection points of fitted curve
- **Logistic fitting**: Double logistic function for smooth phenology
- **Input formats**: CSV (date, value) or multi-band GeoTIFF stack
- **Output formats**: CSV and JSON

## Phenology Metrics

| Metric | Description |
|--------|-------------|
| SOS | Start of Season (green-up) |
| EOS | End of Season (senescence) |
| LOS | Length of Season (EOS - SOS) |
| Peak | Maximum NDVI/EVI value |
| Peak Date | Date of peak value |
| Amplitude | Peak - baseline |
| Integral | Area under curve (season productivity) |

## Usage

### Extract from CSV time series
```bash
python scripts\phenology-metrics.py extract \
  --input ndvi_series.csv \
  --date-col date --value-col ndvi \
  --method threshold --threshold-ratio 0.5 \
  --output phenology.json
```

### Fit double logistic curve
```bash
python scripts\phenology-metrics.py fit \
  --input ndvi_series.csv \
  --date-col date --value-col ndvi \
  --output fitted.json --plot-data plot.csv
```

### Generate plot data
```bash
python scripts\phenology-metrics.py plot-data \
  --input ndvi_series.csv --date-col date --value-col ndvi \
  --output curve.csv
```

## Installation

```bash
pip install numpy>=1.21.0 scipy>=1.7.0 pandas>=1.3.0
# Or: pip install -r scripts/requirements.txt
```

## Parameters

- `--input`: Input CSV file (date, value columns)
- `--date-col`: Date column name (default: `date`)
- `--value-col`: Value column name (default: `ndvi`)
- `--method`: Extraction method (`threshold`, `derivative`, `logistic`)
- `--threshold-ratio`: Threshold ratio for SOS/EOS (default: 0.5)
- `--output`: Output file path (CSV or JSON)
- `--plot-data`: Output fitted curve data for plotting
- `--json`: Output as JSON

## Output

- **Phenology metrics**: CSV/JSON with all computed metrics
- **Fitted curve**: CSV with date, original, fitted values
- **Statistics**: Goodness of fit (R²)

## Dependencies

```
numpy>=1.21.0
scipy>=1.7.0
pandas>=1.3.0
```

## GeoTIFF Stack Usage

Use a multi-band GeoTIFF stack (one band per time step) as input:

```bash
python scripts\phenology-metrics.py extract \
  --input ndvi_stack.tif \
  --input-format geotiff \
  --date-file dates.txt \
  --method logistic \
  --output phenology.json
```

- `--input-format geotiff`: Specifies GeoTIFF stack input
- `--date-file`: Text file with one date per line (YYYY-MM-DD), one per band
- `--band-epoch`: Reference date for band numbering (default: band 1 = first date)

## Date Format Specification

Supported date formats:

| Format | Example | Notes |
|--------|---------|-------|
| ISO date | `2023-06-15` | Recommended (YYYY-MM-DD) |
| US date | `06/15/2023` | MM/DD/YYYY |
| DOY | `166` | Day of year (1-366) |
| Year-DOY | `2023-166` | Combined format |

Specify with `--date-format` parameter.

## Method Selection Guidance

| Method | Best For | Pros / Cons |
|--------|----------|-------------|
| `threshold` | Quick estimation, sparse data | Simple but less precise |
| `derivative` | Precise timing, smooth data | Sensitive to noise |
| `logistic` | Smooth curves, research-grade | Best fit but needs clean data |

**Recommendation**: Use `threshold` for exploratory analysis; `logistic` for publication-quality results.

## Missing Data Handling

Time series gaps are common (clouds, sensor issues). The tool handles them via:

- **Interpolation**: Linear interpolation for gaps ≤30 days (configurable via `--max-gap`)
- **Gap filling**: Savitzky-Golay smoothing for noisy data
- **Flagging**: Outputs data quality flag in results

```bash
python scripts\phenology-metrics.py extract \
  --input ndvi_series.csv --method logistic \
  --max-gap 30 --sg-window 7 \
  --output phenology.json
```

## Multi-Year Data Handling

For multi-year time series:

- **Per-year extraction**: Use `--year-range 2020-2023` to loop over each year
- **Specify year**: Use `--year 2022` for single-year analysis
- **Phenology metrics**: Computed separately per year, output as multi-row CSV/JSON

```bash
python scripts\phenology-metrics.py extract \
  --input ndvi_series.csv --method logistic \
  --year-range 2020-2023 \
  --output phenology_multiyear.csv
```

## Batch Processing for Multiple Pixels

Process multiple pixels from a GeoTIFF stack:

```bash
python scripts\phenology-metrics.py batch \
  --input ndvi_stack.tif \
  --input-format geotiff \
  --method logistic \
  --output-dir ./phenology_results/ \
  --max-workers 4
```

Outputs one JSON per pixel (row, col) in the output directory.

## Visualization

- **Time series**: Plot NDVI/EVI points with fitted curve overlay
- **Key dates**: Vertical lines for SOS, EOS, Peak Date
- **Multi-year**: Facet plot showing each year's phenology curve

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('fitted.csv')
plt.plot(df['date'], df['original'], 'o', label='Original')
plt.plot(df['date'], df['fitted'], '-', label='Fitted')
plt.axvline(x=sos_date, color='green', label='SOS')
plt.axvline(x=eos_date, color='red', label='EOS')
plt.legend()
plt.show()
```

## Citation

```bibtex
@software{phenology_metrics,
  author  = {ruiduobao},
  title   = {Phenology Metrics Extraction Tool},
  url     = {https://github.com/ruiduobao/phenology-metrics},
  version = {0.1.0},
  year    = {2024},
}
```

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| `ConnectionError` | Network issue | Check internet, retry |
| `HTTP 429` | Rate limit | Wait 60s, retry |
| `ValueError` | Invalid input | Check parameter format |
| Empty output | No valid data | Check input data quality |
| `ModuleNotFoundError` | Missing dep | Run pip install |
| Poor fit (low R²) | Noisy data | Try logistic or increase `--sg-window` |
| Missing SOS/EOS | Weak seasonality | Lower threshold ratio or check data range |

## Data Source

Local processing of NDVI/EVI time series data.

---

## Advanced Usage

### Batch Pixel Processing
```bash
# Process a multi-band GeoTIFF stack (one pixel = one time series)
python scripts\phenology-metrics.py extract   --input ndvi_stack.csv --method logistic   --output phenology_results.csv
```

### CI/CD Integration (GitHub Actions)
```yaml
# .github/workflows/phenology-update.yml
name: Phenology Update
on:
  schedule:
    - cron: '0 0 1 3 *'  # Every March (growing season start)
jobs:
  extract:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install numpy scipy pandas
      - run: |
          python scripts\phenology-metrics.py extract \
            --input data/ndvi_2024.csv \
            --method logistic --output data/phenology_2024.csv
```

### PostgreSQL Import
```bash
python scripts\phenology-metrics.py extract   --input ndvi_stack.csv --method logistic --output phenology.csv

psql -d gis_db -c "\COPY phenology(pixel_id, sos, eos, los, peak_date, amplitude) FROM 'phenology.csv' CSV HEADER"
```

### Performance Tips
- Use `--method threshold` for fastest results (least accurate)
- `--method logistic` is recommended for most vegetation types
- `--sg-window 7` controls Savitzky-Golay smoothing window (larger = smoother)
- `--max-gap 30` fills gaps up to 30 days; increase for cloudy regions

---

## 中文说明

从 NDVI/EVI 时间序列数据中提取植被物候指标。支持阈值法、导数法和双 Logistic 拟合。

## 功能特性

- **关键指标**：SOS（生长季开始）、EOS（生长季结束）、LOS（生长季长度）、峰值、峰值日期、振幅、积分
- **阈值法**：振幅的 10%/50% 阈值
- **导数法**：拟合曲线的拐点
- **双 Logistic 拟合**：平滑物候曲线
- **输入格式**：CSV（日期, 值）或多波段 GeoTIFF
- **输出格式**：CSV 和 JSON

## 物候指标

| 指标 | 说明 |
|------|------|
| SOS | 生长季开始（返青） |
| EOS | 生长季结束（衰老） |
| LOS | 生长季长度（EOS - SOS） |
| Peak | 最大 NDVI/EVI 值 |
| Peak Date | 峰值日期 |
| Amplitude | 峰值 - 基线 |
| Integral | 积分 | 曲线下面积（季节生产力） |

## 使用示例

### 从 CSV 提取
```bash
python scripts\phenology-metrics.py extract \
  --input ndvi_series.csv \
  --date-col date --value-col ndvi \
  --method threshold --threshold-ratio 0.5 \
  --output phenology.json
```

### 双 Logistic 拟合
```bash
python scripts\phenology-metrics.py fit \
  --input ndvi_series.csv \
  --date-col date --value-col ndvi \
  --output fitted.json --plot-data plot.csv
```

### 生成绘图数据
```bash
python scripts\phenology-metrics.py plot-data \
  --input ndvi_series.csv --date-col date --value-col ndvi \
  --output curve.csv
```

## 安装

```bash
pip install numpy>=1.21.0 scipy>=1.7.0 pandas>=1.3.0
# 或: pip install -r scripts/requirements.txt
```

## 参数说明

- `--input`: 输入 CSV 文件（日期, 值列）
- `--date-col`: 日期列名（默认: `date`）
- `--value-col`: 值列名（默认: `ndvi`）
- `--method`: 提取方法（`threshold`, `derivative`, `logistic`）
- `--threshold-ratio`: SOS/EOS 阈值比率（默认: 0.5）
- `--output`: 输出文件路径
- `--plot-data`: 输出拟合曲线数据
- `--json`: 以 JSON 输出

## 输出结果

- **物候指标**：CSV/JSON 格式的所有计算指标
- **拟合曲线**：CSV 含日期、原始值、拟合值
- **统计信息**：拟合优度（R²）

## 依赖库

```
numpy>=1.21.0
scipy>=1.7.0
pandas>=1.3.0
```

## GeoTIFF 堆栈使用

使用多波段 GeoTIFF 堆栈（每个时间步一个波段）作为输入：

```bash
python scripts\phenology-metrics.py extract \
  --input ndvi_stack.tif \
  --input-format geotiff \
  --date-file dates.txt \
  --method logistic \
  --output phenology.json
```

- `--input-format geotiff`：指定 GeoTIFF 堆栈输入
- `--date-file`：每行一个日期的文本文件（YYYY-MM-DD），每个波段对应一个日期
- `--band-epoch`：波段编号参考日期（默认：波段 1 = 第一个日期）

## 日期格式说明

支持的日期格式：

| 格式 | 示例 | 说明 |
|------|------|------|
| ISO 日期 | `2023-06-15` | 推荐（YYYY-MM-DD） |
| 美国格式 | `06/15/2023` | MM/DD/YYYY |
| DOY | `166` | 年积日（1-366） |
| 年-DOY | `2023-166` | 组合格式 |

使用 `--date-format` 参数指定。

## 方法选择指南

| 方法 | 适用场景 | 优缺点 |
|------|---------|--------|
| `threshold` | 快速估算、稀疏数据 | 简单但不够精确 |
| `derivative` | 精确时间、平滑数据 | 对噪声敏感 |
| `logistic` | 平滑曲线、科研级 | 拟合最佳但需要干净数据 |

**建议**：探索性分析用 `threshold`；发表级结果用 `logistic`。

## 缺失数据处理

时间序列常有缺口（云、传感器问题）。工具通过以下方式处理：

- **插值**：≤30 天缺口使用线性插值（可通过 `--max-gap` 配置）
- **缺口填充**：Savitzky-Golay 平滑处理噪声数据
- **标记**：在结果中输出数据质量标志

```bash
python scripts\phenology-metrics.py extract \
  --input ndvi_series.csv --method logistic \
  --max-gap 30 --sg-window 7 \
  --output phenology.json
```

## 多年数据处理

对于多年时间序列：

- **逐年提取**：使用 `--year-range 2020-2023` 循环每年
- **指定年份**：使用 `--year 2022` 进行单年分析
- **物候指标**：每年单独计算，输出为多行 CSV/JSON

```bash
python scripts\phenology-metrics.py extract \
  --input ndvi_series.csv --method logistic \
  --year-range 2020-2023 \
  --output phenology_multiyear.csv
```

## 多像元批量处理

处理 GeoTIFF 堆栈中的多个像元：

```bash
python scripts\phenology-metrics.py batch \
  --input ndvi_stack.tif \
  --input-format geotiff \
  --method logistic \
  --output-dir ./phenology_results/ \
  --max-workers 4
```

输出每个像元（行, 列）一个 JSON 文件。

## 可视化

- **时间序列**：绘制 NDVI/EVI 点 + 拟合曲线叠加
- **关键日期**：SOS、EOS、峰值日期的垂直线
- **多年对比**：分面图展示每年物候曲线

## 引用格式

```bibtex
@software{phenology_metrics,
  author  = {ruiduobao},
  title   = {Phenology Metrics Extraction Tool},
  url     = {https://github.com/ruiduobao/phenology-metrics},
  version = {0.1.0},
  year    = {2024},
}
```

## 故障排除

| 错误 | 原因 | 解决方案 |
|------|------|---------|
| `ConnectionError` | 网络问题 | 检查网络，重试 |
| `HTTP 429` | 速率限制 | 等待 60 秒后重试 |
| `ValueError` | 无效输入 | 检查参数格式 |
| 无输出 | 无有效数据 | 检查输入数据质量 |
| `ModuleNotFoundError` | 缺少依赖 | 运行 pip install |
| 拟合差（低 R²） | 数据噪声大 | 尝试 logistic 或增大 `--sg-window` |
| 缺少 SOS/EOS | 季节性弱 | 降低阈值比率或检查数据范围 |

## 数据来源

本地处理 NDVI/EVI 时间序列数据。
