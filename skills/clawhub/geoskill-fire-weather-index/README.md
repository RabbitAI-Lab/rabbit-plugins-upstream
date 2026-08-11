# Fire Weather Index (geoskill-fire-weather-index)

> Implements the Canadian FWI system, deriving FFMC, DMC, DC, ISI, BUI and FWI from daily meteorological elements (temperature/humidity/wind speed/precipitation), outputting fire danger class rasters and time series

---

## 1. Overview

This skill implements the **Canadian Forest Fire Weather Index System** (Van Wagner 1987), deriving six components day-by-day from daily noon meteorological observations (air temperature °C, relative humidity %, wind speed km/h, 24 h precipitation mm): FFMC (Fine Fuel Moisture Code), DMC (Duff Moisture Code), DC (Drought Code), ISI (Initial Spread Index), BUI (Buildup Index) and FWI (Fire Weather Index). The recurrence formulas are consistent with the open-source cffdrs library. FFMC is highly sensitive to precipitation (a single heavy rainfall event can quickly bring it back down); DMC/DC are cumulative drought indicators that grow daily with potential evapotranspiration; ISI/BUI/FWI jointly reflect spread potential and energy release. The final outputs are the final-day six-component raster, a fire danger class raster (Low/Moderate/High/Very High/Extreme) and a daily spatial-mean time series JSON. Application scenarios: forest and grassland fire danger rating forecasting, drought-fire coupling analysis, and review of historical fire weather backgrounds.

## 2. Features

This skill implements the **Canadian Forest Fire Weather Index System** (Van Wagner 1987), deriving six components day-by-day from daily noon meteorological observations (air temperature °C, relative humidity %, wind speed km/h, 24 h precipitation mm): FFMC (Fine Fuel Moisture Code), DMC (Duff Moisture Code), DC (Drought Code), ISI (Initial Spread Index), BUI (Buildup Index) and FWI (Fire Weather Index). The recurrence formulas are consistent with the open-source cffdrs library. FFMC is highly sensitive to precipitation (a single heavy rainfall event can quickly bring it back down); DMC/DC are cumulative drought indicators that grow daily with potential evapotranspiration; ISI/BUI/FWI jointly reflect spread potential and energy release. The final outputs are the final-day six-component raster, a fire danger class raster (Low/Moderate/High/Very High/Extreme) and a daily spatial-mean time series JSON. Application scenarios: forest and grassland fire danger rating forecasting, drought-fire coupling analysis, and review of historical fire weather backgrounds.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-fire-weather-index.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `fwi_components.tif` | GeoTIFF | Final-day six-component stack (6 bands: FFMC/DMC/DC/ISI/BUI/FWI) |
| `fwi_danger_class.tif` | GeoTIFF | Final-day fire danger class (1=Low … 5=Extreme) |
| `fwi_timeseries.json` | JSON | Daily spatial-mean time series of the six components |
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

# 火险天气指数（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-fire-weather-index
description: '基于加拿大 FWI 系统，由气象要素（温度/湿度/风速/降水）逐日递推计算 FFMC、DMC、DC、ISI、BUI、FWI 六分量，输出火险等级栅格与时序'
---

# 火险天气指数 | Fire Weather Index

本 skill 实现**加拿大林火天气指数系统**（Canadian Forest Fire Weather Index
System，Van Wagner 1987），由每日正午气象观测（气温 ℃、相对湿度 %、风速
km/h、24h 降水 mm）逐日递推六个分量：FFMC（细可燃物湿度码）、DMC（腐殖质
湿度码）、DC（干旱码）、ISI（初始蔓延指数）、BUI（累积指数）与 FWI（火险
天气指数）。递推公式与 cffdrs 开源库一致。

FFMC 对降水高度敏感（一次强降水即可快速回落）；DMC/DC 为累积型干旱指标，
随潜在蒸散逐日增长；ISI/BUI/FWI 综合反映蔓延潜力与能量释放。最终输出末日
六分量栅格、火险等级栅格（Low/Moderate/High/Very High/Extreme）与逐日空间
均值时序 JSON。

应用场景：森林草原火险等级预报、干旱-火险耦合分析、历史火灾气象背景复盘。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-fire-weather-index.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例 1（合成数据，离线）

```bash
python geoskill-fire-weather-index.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（仅给 bbox，自动合成，离线）

```bash
python geoskill-fire-weather-index.py --bbox 121.0 31.0 122.0 32.0 --n-dates 45 --output-dir ./out
```

### 示例 3（指定时间步长与静默）

```bash
python geoskill-fire-weather-index.py --bbox 116.0 39.0 117.0 40.0 --synthetic --n-dates 60 --output-dir ./out --quiet
```

### 示例 4（真实气象栅格输入，4 波段=温度/湿度/风速/降水）

```bash
python geoskill-fire-weather-index.py --input meteo_day.tif --output-dir ./out
```

### 示例 5（极小区域）

```bash
python geoskill-fire-weather-index.py --bbox 116.39 39.90 116.40 39.91 --output-dir ./out --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `fwi_components.tif` | GeoTIFF | 末日六分量栈（6 波段：FFMC/DMC/DC/ISI/BUI/FWI） |
| `fwi_danger_class.tif` | GeoTIFF | 末日火险等级（1=Low … 5=Extreme） |
| `fwi_timeseries.json` | JSON | 逐日六分量空间均值时序 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- **真实模式**：本地多波段气象 GeoTIFF（4 波段 = 温度/湿度/风速/降水）。
- **合成模式**（`--synthetic` 或仅 `--bbox`）：本地生成含"干热大风→强降水"事件的物理一致气象时序，无需网络。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
