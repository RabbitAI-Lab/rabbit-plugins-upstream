---
name: geoskill-monsoon-analysis
description: '分析季风系统：风场季节反转、季风指数、降水集中度与季风进退日期突变点检测，支持东亚/南亚区域'
---

# 季风分析 | Monsoon Analysis

This skill diagnoses the monsoon system from wind-field and precipitation time series, producing three core metrics:

- **Seasonal wind reversal**: computes the angle between winter/summer mean wind directions (close to 180° indicates a complete reversal), and defines the monsoon index MI = mean(u, summer half-year) − mean(u, winter half-year) from the seasonal shear of zonal wind (Webster–Yang type). The East Asian summer monsoon veers southerly (u positive), while the South Asian summer monsoon is southwesterly (u negative).
- **Precipitation concentration**: the proportion of annual precipitation falling within the monsoon season (concentration) and a normalized seasonality index.
- **Monsoon onset/retreat dates**: detects onset / peak / retreat change points along the daily cumulative precipitation series.

Supports `--region east_asia|south_asia` (the two regions differ in monsoon season and prevailing wind direction). Suitable for monsoon climate diagnosis, monsoon onset/withdrawal monitoring, and studies of seasonal precipitation distribution.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## Usage / 使用方法

### Basic usage

```bash
python geoskill-monsoon-analysis.py --bbox 116.0 39.0 117.0 40.0 [other options]
```

### Example 1 (synthetic data, offline)

```bash
python geoskill-monsoon-analysis.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (bbox only, auto synthetic, East Asia)

```bash
python geoskill-monsoon-analysis.py --bbox 110.0 20.0 122.0 40.0 --output-dir ./out
```

### Example 3 (South Asia region)

```bash
python geoskill-monsoon-analysis.py --bbox 70.0 8.0 90.0 30.0 --region south_asia --synthetic --output-dir ./out
```

### Example 4 (longer time series)

```bash
python geoskill-monsoon-analysis.py --bbox 110.0 20.0 122.0 40.0 --region east_asia --n-dates 36 --output-dir ./out --quiet
```

### Example 5 (real wind-field raster input, u/v interleaved bands)

```bash
python geoskill-monsoon-analysis.py --input wind_monthly.tif --region east_asia --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `monsoon_index.tif` | GeoTIFF | Monsoon index (seasonal shear of zonal wind) raster |
| `u_wind_seasonal.tif` | GeoTIFF | Winter/summer mean zonal wind (2 bands) |
| `monsoon_diagnosis.json` | JSON | Diagnostics such as reversal angle, concentration, onset/retreat dates |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- **Real mode**: local GeoTIFF (u/v interleaved monthly bands).
- **Synthetic mode** (`--synthetic` or bbox-only): generates a seasonally reversing wind field plus concentrated monsoon-season precipitation locally, no network required.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is performed locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
