---
name: geoskill-temperature-anomaly-mapping
description: '计算温度距平（当期温度减多年同期气候态）与标准化距平，划分暖/冷异常等级，输出距平栅格、异常等级 GeoTIFF 与时序 JSON。Temperature anomaly mapping: current minus multi-year climatology, standardized anomalies, and warm/cold anomaly classes, outputting anomaly rasters, a class GeoTIFF, and a time-series JSON.'
---

# 温度异常制图 | Temperature Anomaly Mapping

Computes and maps **temperature anomalies** to identify warm/cold anomaly regions relative to the climatological baseline and their intensity levels. Suitable for monthly/annual temperature anomaly monitoring, mapping of extreme warm/cold events, and regional diagnostics against the climatic background.

Core algorithm:

- **Climatology**: group the time series by seasonal phase (e.g., month, via `--n-dates`); the multi-year mean within each group is the multi-year same-phase climatology.
- **Anomaly** = current temperature − climatology.
- **Standardized anomaly** = anomaly / same-phase multi-year standard deviation, which removes the unit of measurement and allows cross-seasonal / cross-regional comparison of anomaly intensity.
- **Anomaly class**: thresholds of ±1σ and ±2σ partition the values into severe warm anomaly / warm anomaly / normal / cold anomaly / severe cold anomaly, output as an integer-encoded class raster.

The built-in `--synthetic` mode generates a simulated monthly temperature series with a climatological component (spatial baseline + seasonal cycle) plus inter-annual noise, and injects a regional warm anomaly at the end of the series for offline validation.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy
```

## Usage / 使用方法

### Basic Usage (synthetic data, offline)

```bash
python geoskill-temperature-anomaly-mapping.py --bbox 116.0 39.0 117.0 40.0 --output-dir ./output
```

### Example 1: Monthly temperature anomaly (12-month phase × 5 years)

```bash
python geoskill-temperature-anomaly-mapping.py --bbox 116 39 117 40 --n-dates 12 --n-years 5 --output-dir ./monthly_anom
```

### Example 2: Longer climatology reference period

```bash
python geoskill-temperature-anomaly-mapping.py --bbox 121 31 122 32 --n-dates 12 --n-years 10 --output-dir ./long_clim
```

### Example 3: Real multi-epoch rasters (monthly stacked, with specified phase cycle)

```bash
python geoskill-temperature-anomaly-mapping.py --input temp_monthly_stack.tif --n-dates 12 --output-dir ./real_anom
```

### Example 4: Seasonal phase (4 seasons)

```bash
python geoskill-temperature-anomaly-mapping.py --bbox 116 39 117 40 --n-dates 4 --n-years 8 --output-dir ./seasonal
```

### Example 5: bbox-only auto-synthesis + quiet mode

```bash
python geoskill-temperature-anomaly-mapping.py --bbox 110 30 111 31 --output-dir ./auto --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `anomaly.tif` | GeoTIFF (float32, 2 band) | Latest epoch; band1 = temperature anomaly, band2 = standardized anomaly, EPSG:4326 |
| `anomaly_class.tif` | GeoTIFF (float32, 1 band) | Anomaly class encoding (2 = severe warm … 0 = normal … -2 = severe cold) |
| `timeseries.json` | JSON | Per-epoch spatially averaged anomaly / standardized anomaly + share of the latest class |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/software versions) |

## Data Source / 数据源 / Source

- **Input mode**: local multi-epoch GeoTIFF (each band = one time step, arranged by year × month).
- **Synthetic mode**: generated locally with an injected warm anomaly; no external data source.

## Privacy / 隐私声明 / Privacy

- Fully offline by default; no network requests are made.
- `--synthetic` mode reads no external data.
- All computation is performed locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-temperature-anomaly-mapping
description: '计算温度距平（当期温度减多年同期气候态）与标准化距平，划分暖/冷异常等级，输出距平栅格、异常等级 GeoTIFF 与时序 JSON。Temperature anomaly mapping: current minus multi-year climatology, standardized anomalies, and warm/cold anomaly classes, outputting anomaly rasters, a class GeoTIFF, and a time-series JSON.'
---

# 温度异常制图 | Temperature Anomaly Mapping

计算**温度距平**（anomaly）并制图，识别相对气候态的暖 / 冷异常区域及其
强度等级。适用于月度 / 年度温度异常监测、极端冷暖事件制图、与气候背景
对比的区域诊断。

核心算法：

- **气候态（climatology）**：按季节相位（如月份，`--n-dates`）把时间序列
  分组，组内多年平均即该相位的多年同期气候态。
- **距平** = 当期温度 − 气候态。
- **标准化距平** = 距平 / 同期多年标准差，消除量纲，可跨季节 / 区域比较
  异常强度。
- **异常等级**：按 ±1σ、±2σ 阈值划分 严重暖异常 / 暖异常 / 正常 / 冷异常 /
  严重冷异常，输出整数编码等级栅格。

内置 `--synthetic` 模式生成含气候态（空间基线 + 季节循环）+ 年际噪声、
并在末期注入区域性暖异常的模拟月温度序列，用于离线验证。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-temperature-anomaly-mapping.py --bbox 116.0 39.0 117.0 40.0 --output-dir ./output
```

### 示例 1：月度温度异常（12 个月相位 × 5 年）

```bash
python geoskill-temperature-anomaly-mapping.py --bbox 116 39 117 40 --n-dates 12 --n-years 5 --output-dir ./monthly_anom
```

### 示例 2：更长的气候态参考期

```bash
python geoskill-temperature-anomaly-mapping.py --bbox 121 31 122 32 --n-dates 12 --n-years 10 --output-dir ./long_clim
```

### 示例 3：真实多期栅格（按月排列，指定相位周期）

```bash
python geoskill-temperature-anomaly-mapping.py --input temp_monthly_stack.tif --n-dates 12 --output-dir ./real_anom
```

### 示例 4：季节相位（4 季）

```bash
python geoskill-temperature-anomaly-mapping.py --bbox 116 39 117 40 --n-dates 4 --n-years 8 --output-dir ./seasonal
```

### 示例 5：仅 bbox 自动合成 + 静默

```bash
python geoskill-temperature-anomaly-mapping.py --bbox 110 30 111 31 --output-dir ./auto --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `anomaly.tif` | GeoTIFF (float32, 2 band) | 最新一期 band1=温度距平，band2=标准化距平，EPSG:4326 |
| `anomaly_class.tif` | GeoTIFF (float32, 1 band) | 异常等级编码（2=严重暖…0=正常…-2=严重冷） |
| `timeseries.json` | JSON | 逐期空间平均距平/标准化距平 + 最新等级占比 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

- **输入模式**：本地多期 GeoTIFF（每波段 = 一个时间步，按年×月排列）。
- **合成模式**：本地生成，含注入暖异常，无外部数据源。

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求。
- `--synthetic` 模式不读取任何外部数据。
- 所有计算在本地完成，不上传用户数据。

## License

MIT
