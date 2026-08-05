# Evapotranspiration Estimation (geoskill-evapotranspiration-estimation)

> Priestley-Taylor and simplified SEBAL evapotranspiration estimation, computing ET (mm/day) from net radiation, air temperature, LST, and NDVI. Outputs an ET raster plus a statistics JSON.

---

## 1. Overview

Estimates regional evapotranspiration (ET, mm/day) from net radiation, air temperature, land surface temperature, and vegetation indices. Suitable for farmland irrigation-demand assessment, watershed water-consumption analysis, drought monitoring, and land-surface process validation. Two methods are implemented: - **pt** (Priestley-Taylor, 1972): ET = α × Δ/(Δ + γ) × Rn × 0.408, with α ≈ 1.26 (empirical coefficient for well-watered conditions), Δ the slope of the saturation vapor pressure–temperature curve (kPa/°C, derived from air temperature via the Tetens formula `es = 0.6108·exp(17.27T/(T+237.3))`), γ ≈ 0.066 kPa/°C the psychrometric constant, Rn net radiation (MJ/m²/day), and 0.408 the latent-heat conversion from MJ/m² to mm water depth. This method has a clear physical basis, requires only radiation and air temperature, and suits large-area estimation. - **sebal** (simplified empirical SEBAL): builds the evaporative fraction EF from NDVI and LST (`EF = clip(NDVI_norm × (1 − LST_norm), 0, 1)`), then `ET = EF × Rn × 0.408`. Dense, cool vegetated surfaces yield high EF and high ET; bare land / urban heat islands yield low ET. Outputs an ET raster (mm/day, EPSG:4326) and a statistics JSON. The `--synthetic` mode generates physically consistent Rn/T/LST/NDVI fields (high ET over vegetation on the left, low ET over bare land on the right); estimates should fall within the physically plausible 0–10 mm/day range and ET should be positively correlated with net radiation.

## 2. Features

Estimates regional evapotranspiration (ET, mm/day) from net radiation, air temperature, land surface temperature, and vegetation indices. Suitable for farmland irrigation-demand assessment, watershed water-consumption analysis, drought monitoring, and land-surface process validation. Two methods are implemented: - **pt** (Priestley-Taylor, 1972): ET = α × Δ/(Δ + γ) × Rn × 0.408, with α ≈ 1.26 (empirical coefficient for well-watered conditions), Δ the slope of the saturation vapor pressure–temperature curve (kPa/°C, derived from air temperature via the Tetens formula `es = 0.6108·exp(17.27T/(T+237.3))`), γ ≈ 0.066 kPa/°C the psychrometric constant, Rn net radiation (MJ/m²/day), and 0.408 the latent-heat conversion from MJ/m² to mm water depth. This method has a clear physical basis, requires only radiation and air temperature, and suits large-area estimation. - **sebal** (simplified empirical SEBAL): builds the evaporative fraction EF from NDVI and LST (`EF = clip(NDVI_norm × (1 − LST_norm), 0, 1)`), then `ET = EF × Rn × 0.408`. Dense, cool vegetated surfaces yield high EF and high ET; bare land / urban heat islands yield low ET. Outputs an ET raster (mm/day, EPSG:4326) and a statistics JSON. The `--synthetic` mode generates physically consistent Rn/T/LST/NDVI fields (high ET over vegetation on the left, low ET over bare land on the right); estimates should fall within the physically plausible 0–10 mm/day range and ET should be positively correlated with net radiation.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-evapotranspiration-estimation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `evapotranspiration.tif` | GeoTIFF (float32) | Evapotranspiration ET (mm/day), EPSG:4326 |
| `et_stats.json` | JSON | Method, parameters, ET mean/extremes/std, Rn mean |
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

# 蒸散发估算（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-evapotranspiration-estimation
description: 'Priestley-Taylor 与简化 SEBAL 蒸散发估算，从净辐射/气温/LST/NDVI 计算 ET (mm/day)。Priestley-Taylor and simplified SEBAL evapotranspiration estimation from net radiation/air temperature/LST/NDVI. 输出 ET 栅格 + 统计 JSON。'
---

# 蒸散发估算 | Evapotranspiration Estimation

从净辐射、气温、地表温度与植被指数估算区域蒸散发（ET，mm/day），适用于农田
灌溉需水评估、流域耗水分析、干旱监测、陆面过程验证等场景。实现两种方法：

- **pt**（Priestley-Taylor，1972）：

      ET = α × Δ/(Δ + γ) × Rn × 0.408

  α≈1.26（充分供水经验系数），Δ 为饱和水汽压—温度曲线斜率（kPa/°C，由气温
  经 Tetens 公式 `es = 0.6108·exp(17.27T/(T+237.3))` 求得），γ≈0.066 kPa/°C
  为干湿表常数，Rn 为净辐射（MJ/m²/day），0.408 为 MJ/m² → mm 水深的潜热换算。
  该方法物理基础清晰，只需辐射与气温，适合大范围估算。
- **sebal**（简化 SEBAL 经验版）：用 NDVI 与 LST 构建蒸发比 EF
  （`EF = clip(NDVI_norm × (1 − LST_norm), 0, 1)`），再 `ET = EF × Rn × 0.408`。
  植被茂密、地表凉爽处 EF 高、ET 高；裸地/城市热岛处 ET 低。

输出 ET 栅格（mm/day，EPSG:4326）与统计 JSON。支持 `--synthetic` 模式生成
物理一致的 Rn/T/LST/NDVI 场（左侧植被高 ET、右侧裸地低 ET），估算结果应落在
0–10 mm/day 的物理合理区间，且 ET 与净辐射正相关。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-evapotranspiration-estimation.py --bbox 116.0 39.0 117.0 40.0 --method pt --output-dir ./output
```

### 示例 1：Priestley-Taylor（合成数据）

```bash
python geoskill-evapotranspiration-estimation.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --method pt \
    --synthetic \
    --output-dir ./et_pt
```

### 示例 2：简化 SEBAL

```bash
python geoskill-evapotranspiration-estimation.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --method sebal \
    --synthetic \
    --output-dir ./et_sebal
```

### 示例 3：真实净辐射栅格

```bash
python geoskill-evapotranspiration-estimation.py \
    --input net_radiation.tif \
    --method pt \
    --output-dir ./et_real
```

（输入为净辐射 Rn，MJ/m²/day；配套气象/地表场由合成生成以演示流程。）

### 示例 4：自定义 Priestley-Taylor 系数

```bash
python geoskill-evapotranspiration-estimation.py \
    --bbox 116 39 117 40 \
    --method pt --alpha 1.10 \
    --synthetic --output-dir ./et_a11
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `evapotranspiration.tif` | GeoTIFF (float32) | 蒸散发 ET（mm/day），EPSG:4326 |
| `et_stats.json` | JSON | 方法、参数、ET 均值/极值/标准差、Rn 均值 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

- **净辐射 Rn**：本地 GeoTIFF，或来自 MODIS / Landsat 辐射平衡、再分析资料
- **气温 T / LST / NDVI**：合成模式生成；真实应用可接入气象站、MODIS LST/NDVI
- **合成模式**：本地生成，无外部数据源

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
