# Wind Resource Assessment (geoskill-wind-resource-assessment)

> Wind resource assessment from wind-speed time series: per-pixel Weibull distribution fitting (method of moments/MLE), wind power density WPD=0.5ρmean(v³), power-law height extrapolation, and annual energy yield. Outputs mean wind speed / power density / Weibull parameter GeoTIFFs + a parameters JSON + manifest.

---

## 1. Overview

Performs wind resource assessment on wind-speed time series rasters, estimating Weibull distribution parameters and computing the Wind Power Density (WPD) per pixel for wind farm siting, resource surveys, and energy yield estimation. Core algorithms: - **Weibull fitting**: the wind speed frequency distribution is described by Weibull(k, c). Two methods are provided — the method of moments (Justus & Mikhail 1978: k ≈ (σ/μ)^-1.086, c = μ/Γ(1+1/k)) and maximum likelihood (scipy.stats.weibull_min MLE). - **Wind power density**: WPD = 0.5 × ρ × mean(v³), with ρ the standard air density ≈ 1.225 kg/m³. This is the most direct physical measure of wind resource strength (unit W/m²). - **Power-law height extrapolation**: v(z) = v_ref × (z/z_ref)^α, with α ≈ 1/ln(z_ref/z0), extrapolating 10 m observed wind speeds to hub height (default 100 m). - **Annual energy yield estimation**: estimates the annual energy yield of a single turbine (MWh/yr) from the regional mean WPD and capacity factor. The `--synthetic` mode generates simulated wind fields that follow a Weibull distribution (spatially varying scale parameter c), allowing the full workflow and parameter recovery to be verified without network access or real data.

## 2. Features

Performs wind resource assessment on wind-speed time series rasters, estimating Weibull distribution parameters and computing the Wind Power Density (WPD) per pixel for wind farm siting, resource surveys, and energy yield estimation. Core algorithms: - **Weibull fitting**: the wind speed frequency distribution is described by Weibull(k, c). Two methods are provided — the method of moments (Justus & Mikhail 1978: k ≈ (σ/μ)^-1.086, c = μ/Γ(1+1/k)) and maximum likelihood (scipy.stats.weibull_min MLE). - **Wind power density**: WPD = 0.5 × ρ × mean(v³), with ρ the standard air density ≈ 1.225 kg/m³. This is the most direct physical measure of wind resource strength (unit W/m²). - **Power-law height extrapolation**: v(z) = v_ref × (z/z_ref)^α, with α ≈ 1/ln(z_ref/z0), extrapolating 10 m observed wind speeds to hub height (default 100 m). - **Annual energy yield estimation**: estimates the annual energy yield of a single turbine (MWh/yr) from the regional mean WPD and capacity factor. The `--synthetic` mode generates simulated wind fields that follow a Weibull distribution (spatially varying scale parameter c), allowing the full workflow and parameter recovery to be verified without network access or real data.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-wind-resource-assessment.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `mean_wind_speed.tif` | GeoTIFF (float32) | Time-series mean wind speed (extrapolated to height), m/s, EPSG:4326 |
| `wind_power_density.tif` | GeoTIFF (float32) | Mean wind power density WPD, W/m² |
| `weibull_params.tif` | GeoTIFF (2 bands) | band1=shape k, band2=scale c (m/s) |
| `weibull_params.json` | JSON | Regional statistics, parameter settings, annual energy yield estimate |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/software versions) |

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

# 风能资源评估（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-wind-resource-assessment
description: '基于风速时序的风能资源评估：逐像元 Weibull 分布拟合（矩估计/MLE）、风功率密度 WPD=0.5ρmean(v³)、幂律高度外推与年发电量估算。Wind resource assessment from wind-speed time series: per-pixel Weibull fitting, wind power density, power-law height extrapolation, and annual energy yield. 输出平均风速/功率密度/Weibull 参数 GeoTIFF + 参数 JSON + manifest。'
---

# 风能资源评估 | Wind Resource Assessment

对风速时序栅格执行风能资源评估，逐像元估计 Weibull 分布参数并计算风功率
密度（Wind Power Density, WPD），用于风电场选址、资源普查和发电量预估。

核心算法：

- **Weibull 拟合**：风速频率分布用 Weibull(k, c) 描述。提供矩估计
  （Justus & Mikhail 1978：k ≈ (σ/μ)^-1.086，c = μ/Γ(1+1/k)）与最大似然
  （scipy.stats.weibull_min MLE）两种方法。
- **风功率密度**：WPD = 0.5 × ρ × mean(v³)，ρ 为标准空气密度 ≈ 1.225 kg/m³。
  这是衡量风能资源强弱最直接的物理量（单位 W/m²）。
- **幂律高度外推**：v(z) = v_ref × (z/z_ref)^α，α ≈ 1/ln(z_ref/z0)，把 10 m
  观测风速外推到轮毂高度（默认 100 m）。
- **年发电量估算**：由区域平均 WPD 与容量系数估算单台机组年发电量（MWh/yr）。

支持 `--synthetic` 模式生成符合 Weibull 分布的模拟风速场（尺度参数 c 空间变化），
无需网络和真实数据即可验证全流程与参数恢复。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法（仅给 bbox，自动合成）

```bash
python geoskill-wind-resource-assessment.py --bbox 116.0 39.0 117.0 40.0 --output-dir ./out
```

### 示例 1：合成数据离线评估

```bash
python geoskill-wind-resource-assessment.py --bbox 116.0 39.0 117.0 40.0 --synthetic --n-dates 100 --output-dir ./out
```

### 示例 2：MLE 拟合 + 自定义轮毂高度

```bash
python geoskill-wind-resource-assessment.py --bbox 121.0 31.0 122.0 32.0 --synthetic --method mle --height 120 --output-dir ./sh
```

### 示例 3：真实风速时序栅格

```bash
python geoskill-wind-resource-assessment.py --input wind_ts.tif --height 100 --roughness 0.1 --output-dir ./real
```

### 示例 4：自定义空气密度与容量系数（高海拔）

```bash
python geoskill-wind-resource-assessment.py --input wind_ts.tif --air-density 1.0 --capacity-factor 0.30 --output-dir ./plateau
```

### 示例 5：矩估计 vs MLE 对比

```bash
python geoskill-wind-resource-assessment.py --bbox 116 39 117 40 --synthetic --method moment --output-dir ./cmp_moment --quiet
python geoskill-wind-resource-assessment.py --bbox 116 39 117 40 --synthetic --method mle --output-dir ./cmp_mle --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `mean_wind_speed.tif` | GeoTIFF (float32) | 时序平均风速（外推到 height），m/s，EPSG:4326 |
| `wind_power_density.tif` | GeoTIFF (float32) | 平均风功率密度 WPD，W/m² |
| `weibull_params.tif` | GeoTIFF (2 bands) | band1=形状 k，band2=尺度 c (m/s) |
| `weibull_params.json` | JSON | 区域统计、参数设置、年发电量估算 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

- **输入**：本地多波段风速时序 GeoTIFF（每个波段一个时相）
- **合成模式**：本地生成 Weibull(k, c) 分布风速场，无外部数据源

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
