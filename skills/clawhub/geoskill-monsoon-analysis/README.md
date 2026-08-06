# Monsoon Analysis (geoskill-monsoon-analysis)

> Analyze monsoon systems: seasonal wind reversal, monsoon index, precipitation concentration, and change-point detection of monsoon onset/retreat dates, supporting East Asia/South Asia regions

---

## 1. Overview

This skill diagnoses monsoon systems from wind-field and precipitation time series and outputs three core indicators: - **Seasonal wind reversal**: computes the angle between the mean winter and summer wind directions (close to 180° indicates complete reversal), and defines the monsoon index MI = mean(u, summer half-year) − mean(u, winter half-year) based on seasonal shear of the zonal wind (Webster-Yang type). The East Asian summer monsoon is southerly (u positive), while the South Asian summer monsoon is southwesterly (u negative). - **Precipitation concentration**: the proportion of annual precipitation falling in the monsoon season (concentration) and the normalized seasonality index. - **Monsoon onset/retreat dates**: detects onset / peak / retreat change points on the daily cumulative precipitation series. Supports `--region east_asia|south_asia` (the two regions differ in monsoon season and prevailing wind direction). Suitable for monsoon climate diagnosis, monsoon onset/retreat monitoring, and studies of seasonal precipitation distribution.

## 2. Features

This skill diagnoses monsoon systems from wind-field and precipitation time series and outputs three core indicators: - **Seasonal wind reversal**: computes the angle between the mean winter and summer wind directions (close to 180° indicates complete reversal), and defines the monsoon index MI = mean(u, summer half-year) − mean(u, winter half-year) based on seasonal shear of the zonal wind (Webster-Yang type). The East Asian summer monsoon is southerly (u positive), while the South Asian summer monsoon is southwesterly (u negative). - **Precipitation concentration**: the proportion of annual precipitation falling in the monsoon season (concentration) and the normalized seasonality index. - **Monsoon onset/retreat dates**: detects onset / peak / retreat change points on the daily cumulative precipitation series. Supports `--region east_asia|south_asia` (the two regions differ in monsoon season and prevailing wind direction). Suitable for monsoon climate diagnosis, monsoon onset/retreat monitoring, and studies of seasonal precipitation distribution.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-monsoon-analysis.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `monsoon_index.tif` | GeoTIFF | Monsoon index (zonal wind seasonal shear) raster |
| `u_wind_seasonal.tif` | GeoTIFF | Summer/winter mean zonal wind (2 bands) |
| `monsoon_diagnosis.json` | JSON | Diagnosis such as reversal angle, concentration, onset/retreat dates |
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

# 季风分析（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-monsoon-analysis
description: '分析季风系统：风场季节反转、季风指数、降水集中度与季风进退日期突变点检测，支持东亚/南亚区域'
---

# 季风分析 | Monsoon Analysis

本 skill 对风场与降水时序做季风系统诊断，输出三类核心指标：

- **风场季节反转**：计算冬/夏平均风向夹角（接近 180° 表示完全反转），并以
  纬向风季节剪切定义季风指数 MI = mean(u, 夏半年) − mean(u, 冬半年)
  （Webster-Yang 型）。东亚夏季风偏南（u 为正），南亚夏季西南风（u 为负）。
- **降水集中度**：季风期降水占全年比例（concentration）与归一化季节性指数。
- **季风进退日期**：在逐日降水累计序列上检测 onset / peak / retreat 突变点。

支持 `--region east_asia|south_asia`（两区季风期与主导风向不同）。适用于
季风气候诊断、季风爆发/撤退监测、降水季节分配研究。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-monsoon-analysis.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例 1（合成数据，离线）

```bash
python geoskill-monsoon-analysis.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（仅给 bbox，自动合成，东亚）

```bash
python geoskill-monsoon-analysis.py --bbox 110.0 20.0 122.0 40.0 --output-dir ./out
```

### 示例 3（南亚区域）

```bash
python geoskill-monsoon-analysis.py --bbox 70.0 8.0 90.0 30.0 --region south_asia --synthetic --output-dir ./out
```

### 示例 4（更长时间序列）

```bash
python geoskill-monsoon-analysis.py --bbox 110.0 20.0 122.0 40.0 --region east_asia --n-dates 36 --output-dir ./out --quiet
```

### 示例 5（真实风场栅格输入，u/v 交替波段）

```bash
python geoskill-monsoon-analysis.py --input wind_monthly.tif --region east_asia --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `monsoon_index.tif` | GeoTIFF | 季风指数（纬向风季节剪切）栅格 |
| `u_wind_seasonal.tif` | GeoTIFF | 夏/冬平均纬向风（2 波段） |
| `monsoon_diagnosis.json` | JSON | 反转角、集中度、进退日期等诊断 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- **真实模式**：本地 GeoTIFF（u/v 交替月波段）。
- **合成模式**（`--synthetic` 或仅 `--bbox`）：本地生成季节反转风场 + 季风期集中降水，无需网络。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
