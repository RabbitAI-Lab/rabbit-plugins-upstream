# SAR Forest Biomass Estimation (geoskill-sar-forest-biomass)

> SAR forest biomass estimation: invert forest above-ground biomass AGB (t/ha) from backscatter σ⁰ using linear/saturation empirical models, with C/L band support and ground-sample calibration.

---

## 1. Overview

Estimates forest above-ground biomass AGB (above-ground biomass, t/ha) from the SAR backscatter coefficient σ⁰. Implements two types of empirical relationships: - **Linear model**: σ⁰_dB = m·AGB + c, suitable for low-biomass, non-saturated ranges. - **Saturation model**: AGB = AGB_sat·(1 − e^(−k·σ⁰_lin)), capturing the physical behavior of SAR backscatter saturating as biomass increases (sensitivity decreases in high-AGB regions). Supports `--calibration` with a ground-sample CSV (columns `sigma0,agb`) for coefficient fitting: least squares for the linear model, non-linear least squares (scipy curve_fit) for the saturation model. Without calibration, built-in default coefficients per band (C / L) are used; the L band penetrates deeper and has a higher saturation biomass.

## 2. Features

Estimates forest above-ground biomass AGB (above-ground biomass, t/ha) from the SAR backscatter coefficient σ⁰. Implements two types of empirical relationships: - **Linear model**: σ⁰_dB = m·AGB + c, suitable for low-biomass, non-saturated ranges. - **Saturation model**: AGB = AGB_sat·(1 − e^(−k·σ⁰_lin)), capturing the physical behavior of SAR backscatter saturating as biomass increases (sensitivity decreases in high-AGB regions). Supports `--calibration` with a ground-sample CSV (columns `sigma0,agb`) for coefficient fitting: least squares for the linear model, non-linear least squares (scipy curve_fit) for the saturation model. Without calibration, built-in default coefficients per band (C / L) are used; the L band penetrates deeper and has a higher saturation biomass.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-sar-forest-biomass.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `forest_biomass.tif` | GeoTIFF | Inverted AGB (t/ha) |
| `biomass_report.json` | JSON | Model coefficients, statistics, synthetic validation (RMSE/correlation) |
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

# SAR森林生物量估算（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-sar-forest-biomass
description: 'SAR 森林生物量估算：由后向散射 σ⁰ 用线性/饱和经验模型反演森林地上生物量 AGB (t/ha)，支持 C/L 波段与地面样本标定'
---

# SAR森林生物量估算 | SAR Forest Biomass Estimation

从 SAR 后向散射系数 σ⁰ 估算森林地上生物量 AGB（above-ground biomass, t/ha）。
实现两类经验关系：

- **线性模型**：σ⁰_dB = m·AGB + c，适用于低生物量、未饱和区间。
- **饱和模型**：AGB = AGB_sat·(1 − e^(−k·σ⁰_lin))，刻画 SAR 后向散射随生物量
  增加趋于饱和的物理特征（高 AGB 区敏感度下降）。

支持 `--calibration` 提供地面样本 CSV（列 `sigma0,agb`）做系数拟合：线性用最小
二乘，饱和用非线性最小二乘（scipy curve_fit）。无标定时使用按波段（C / L）内置的
默认系数，L 波段穿透性强、饱和生物量更高。

## 应用场景

- 森林碳储量估算、碳汇监测
- 森林资源调查与生物量制图
- REDD+ 与气候变化研究

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy' 'scikit-learn'
```

## 使用方法

### 示例 1（合成数据，离线，L 波段饱和模型）

```bash
python geoskill-sar-forest-biomass.py --bbox 110.0 22.0 111.0 23.0 --band l --synthetic --output-dir ./out
```

### 示例 2（C 波段线性模型）

```bash
python geoskill-sar-forest-biomass.py --bbox 110.0 22.0 111.0 23.0 --band c --model linear --synthetic --output-dir ./out
```

### 示例 3（真实 σ⁰ 影像 + 地面样本标定）

```bash
python geoskill-sar-forest-biomass.py --input sigma0_db.tif --band c --model linear --calibration samples.csv --output-dir ./out
```

### 示例 4（饱和模型标定）

```bash
python geoskill-sar-forest-biomass.py --input sigma0_db.tif --band l --model saturation --calibration samples.csv --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `forest_biomass.tif` | GeoTIFF | 反演 AGB (t/ha) |
| `biomass_report.json` | JSON | 模型系数、统计、合成验证 (RMSE/相关) |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地 σ⁰ (dB) GeoTIFF + 可选标定 CSV，或 `--synthetic` AGB 场正演的模拟场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
