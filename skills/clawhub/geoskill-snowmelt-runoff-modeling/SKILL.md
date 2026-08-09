---
name: geoskill-snowmelt-runoff-modeling
description: '度日因子法（DDF）融雪径流模拟，逐日累积融雪生成径流过程线与积雪面积曲线。Degree-day-factor snowmelt runoff modeling producing daily hydrograph and snow-cover depletion curve. 输出径流时序/积雪曲线 JSON + 径流深栅格。'
---

# 融雪径流模拟 | Snowmelt Runoff Modeling

Degree-day-factor (DDF) snowmelt runoff modeling, suitable for spring snowmelt flood forecasting, water resource assessment, and snowmelt dynamics monitoring in high-elevation / high-latitude basins. Core equation:

    M = DDF × max(0, T − T_base)

where `M` is the daily snowmelt (mm/day, as water equivalent), `DDF` is the degree-day factor (mm·°C⁻¹·day⁻¹), `T` is the daily mean air temperature, and `T_base` is the melt threshold temperature (default 0 °C).

The model laps the reference temperature down to each pixel using a temperature lapse rate (default 6 °C/km), so higher elevations are colder and snow melts more slowly. In the daily loop, the actual melt at each pixel is limited by its remaining snow water equivalent (SWE) (it cannot melt more than what is available), accumulating into a pixel-wise runoff depth raster; basin-wide averaging yields a daily runoff hydrograph, and a snow-cover depletion curve over time is also produced. The whole process conserves water: cumulative runoff = initial snowpack − residual snowpack.

A `--synthetic` mode is supported to generate a complete simulated dataset containing elevation zones (500–3000 m), a spring warming sequence, and initial snowpack distributed by elevation, so the workflow can be validated without network access or real data.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy
```

## Usage / 使用方法

### Basic Usage (Synthetic Data, Offline)

```bash
python geoskill-snowmelt-runoff-modeling.py --bbox 116.0 39.0 117.0 40.0 --ddf 4.0 --output-dir ./output
```

### Example 1: Synthetic Data Snowmelt Simulation

```bash
python geoskill-snowmelt-runoff-modeling.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --ddf 4.0 \
    --synthetic \
    --output-dir ./snowmelt_syn
```

### Example 2: Sensitivity to Different Degree-Day Factors

```bash
python geoskill-snowmelt-runoff-modeling.py --bbox 116 39 117 40 --ddf 2.0 --synthetic --output-dir ./ddf2 --quiet
python geoskill-snowmelt-runoff-modeling.py --bbox 116 39 117 40 --ddf 6.0 --synthetic --output-dir ./ddf6 --quiet
```

### 示例 3：真实 DEM

```bash
python geoskill-snowmelt-runoff-modeling.py \
    --input dem.tif \
    --ddf 4.0 \
    --n-days 90 \
    --output-dir ./real_snowmelt
```

(In real mode, the temperature time series and initial snowpack are synthesized from elevation, for workflow demonstration purposes.)

### Example 4: Custom Melting Threshold Temperature

```bash
python geoskill-snowmelt-runoff-modeling.py \
    --bbox 116 39 117 40 \
    --ddf 4.0 --t-base 1.0 --n-days 60 \
    --synthetic --output-dir ./tbase1
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `runoff_depth.tif` | GeoTIFF (float32) | Cumulative snowmelt runoff depth (mm), EPSG:4326 |
| `runoff_time_series.json` | JSON | Daily hydrograph, snow-cover depletion curve, cumulative runoff, temperature series, statistics |
| `output-manifest.json` | JSON | Run manifest (input/output/QA/software versions) |

## Data Source / 数据源 / Source

- **DEM**: local input GeoTIFF (EPSG:4326), e.g. from SRTM / Copernicus DEM
- **Temperature/snow**: generated in synthetic mode; real applications can ingest weather station or reanalysis data
- **Synthetic mode**: generated locally, no external data source

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default and makes no network requests
- `--synthetic` mode reads no external data
- All computation is done locally; no user data is uploaded

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-snowmelt-runoff-modeling
description: '度日因子法（DDF）融雪径流模拟，逐日累积融雪生成径流过程线与积雪面积曲线。Degree-day-factor snowmelt runoff modeling producing daily hydrograph and snow-cover depletion curve. 输出径流时序/积雪曲线 JSON + 径流深栅格。'
---

# 融雪径流模拟 | Snowmelt Runoff Modeling

度日因子法（Degree-Day Factor, DDF）融雪径流模拟，适用于高海拔/高纬度流域
春季融雪洪水预估、水资源量评估、积雪消融动态监测等场景。核心公式：

    M = DDF × max(0, T − T_base)

其中 `M` 为日融雪量（mm/day，以水当量计），`DDF` 为度日因子
（mm·°C⁻¹·day⁻¹），`T` 为日平均气温，`T_base` 为融化临界温度（默认 0 °C）。

模型通过气温递减率（默认 6 °C/km）把参考气温下垫到每个像元，因此高海拔更冷、
融雪更慢。逐日循环中，每个像元的实际融雪受其剩余雪水当量（SWE）限制（不能
融超），累积形成逐像元径流深栅格；全流域平均得到逐日径流过程线（hydrograph），
并输出积雪面积随时间递减曲线（snow-cover depletion curve）。整个过程满足
水量守恒：累积径流 = 初始积雪 − 残余积雪。

支持 `--synthetic` 模式生成含高程带（500–3000 m）、春季升温过程与随高程分布
的初始积雪的完整模拟数据集，无需网络和真实数据即可验证流程。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-snowmelt-runoff-modeling.py --bbox 116.0 39.0 117.0 40.0 --ddf 4.0 --output-dir ./output
```

### 示例 1：合成数据融雪模拟

```bash
python geoskill-snowmelt-runoff-modeling.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --ddf 4.0 \
    --synthetic \
    --output-dir ./snowmelt_syn
```

### 示例 2：不同度日因子敏感性

```bash
python geoskill-snowmelt-runoff-modeling.py --bbox 116 39 117 40 --ddf 2.0 --synthetic --output-dir ./ddf2 --quiet
python geoskill-snowmelt-runoff-modeling.py --bbox 116 39 117 40 --ddf 6.0 --synthetic --output-dir ./ddf6 --quiet
```

### 示例 3：真实 DEM

```bash
python geoskill-snowmelt-runoff-modeling.py \
    --input dem.tif \
    --ddf 4.0 \
    --n-days 90 \
    --output-dir ./real_snowmelt
```

（真实模式下气温时序与初始积雪由高程合成，用于演示流程。）

### 示例 4：自定义融化临界温度

```bash
python geoskill-snowmelt-runoff-modeling.py \
    --bbox 116 39 117 40 \
    --ddf 4.0 --t-base 1.0 --n-days 60 \
    --synthetic --output-dir ./tbase1
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `runoff_depth.tif` | GeoTIFF (float32) | 累积融雪径流深（mm），EPSG:4326 |
| `runoff_time_series.json` | JSON | 逐日径流过程线、积雪面积曲线、累积径流、气温序列、统计量 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

- **DEM**：本地输入 GeoTIFF（EPSG:4326），可来自 SRTM / Copernicus DEM
- **气温/积雪**：合成模式生成；真实应用可接入气象站点或再分析数据
- **合成模式**：本地生成，无外部数据源

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
