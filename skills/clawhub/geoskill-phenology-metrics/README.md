# phenology-metrics

Extract phenological metrics from NDVI/EVI time series data.

## Features

- SOS, EOS, LOS, Peak, Amplitude, Integral metrics
- Threshold, derivative, and double logistic methods
- CSV input/output
- Fitted curve data for plotting

## Installation

### Option 1: ClawHub
```bash
clawhub install phenology-metrics
```

### Option 2: Manual
```bash
git clone https://github.com/ruiduobao/phenology-metrics.git
cd phenology-metrics
pip install -r requirements.txt
```

### Option 3: Claude Code / skills.sh
```bash
claude skills install phenology-metrics
```

## Quick Start

```bash
python scripts/phenology-metrics.py extract \
  -i ndvi.csv --date-col date --value-col ndvi \
  --method threshold --output phenology.json

python scripts/phenology-metrics.py fit \
  -i ndvi.csv --date-col date --value-col ndvi \
  -o fit.json --plot-data curve.csv
```

## Dependencies

```
numpy>=1.21.0
scipy>=1.7.0
pandas>=1.3.0
```

## Data Source

Local processing of NDVI/EVI time series.

## License

MIT-0 (Public Domain)

---

# 中文说明

从 NDVI/EVI 时间序列中提取植被物候指标。

## 功能

- SOS、EOS、LOS、峰值、振幅、积分指标
- 阈值法、导数法、双 Logistic 拟合
- CSV 输入输出
- 拟合曲线数据用于绘图

## 安装

### 方式一：ClawHub
```bash
clawhub install phenology-metrics
```

### 方式二：手动安装
```bash
git clone https://github.com/ruiduobao/phenology-metrics.git
cd phenology-metrics
pip install -r requirements.txt
```

### 方式三：Claude Code / skills.sh
```bash
claude skills install phenology-metrics
```

## 快速开始

```bash
python scripts/phenology-metrics.py extract \
  -i ndvi.csv --date-col date --value-col ndvi \
  --method threshold --output phenology.json

python scripts/phenology-metrics.py fit \
  -i ndvi.csv --date-col date --value-col ndvi \
  -o fit.json --plot-data curve.csv
```

## 数据来源

本地处理 NDVI/EVI 时间序列数据。

## 许可证

MIT-0 (Public Domain)
