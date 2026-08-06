# SAR Soil Moisture Retrieval (geoskill-sar-soil-moisture)

> SAR soil moisture retrieval: analytical inversion of bare-soil volumetric water content (m³/m³) from the backscatter coefficient σ⁰, incidence angle and surface roughness, based on simplified Dubois/Oh semi-empirical models.

---

## 1. Overview

Retrieves the volumetric soil water content mv (m³/m³) of bare soil from the SAR backscatter coefficient σ⁰, using the simplified Dubois / Oh semi-empirical physical model: σ⁰_dB(mv, ks, θ) = A(θ) + B(θ)·(k·s) + C(θ)·mv where θ is the incidence angle, k = 2π/λ is the radar wavenumber (C-band λ≈5.6 cm), s is the surface RMS height, and ks = k·s is the normalized roughness; C(θ) ∝ cos²θ is the moisture-sensitive term. Since σ⁰_dB is monotonically linear with respect to mv, the inversion solves analytically and clips the result to the physically valid range [0.01, 0.60] m³/m³.

## 2. Features

Retrieves the volumetric soil water content mv (m³/m³) of bare soil from the SAR backscatter coefficient σ⁰, using the simplified Dubois / Oh semi-empirical physical model: σ⁰_dB(mv, ks, θ) = A(θ) + B(θ)·(k·s) + C(θ)·mv where θ is the incidence angle, k = 2π/λ is the radar wavenumber (C-band λ≈5.6 cm), s is the surface RMS height, and ks = k·s is the normalized roughness; C(θ) ∝ cos²θ is the moisture-sensitive term. Since σ⁰_dB is monotonically linear with respect to mv, the inversion solves analytically and clips the result to the physically valid range [0.01, 0.60] m³/m³.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-sar-soil-moisture.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `soil_moisture.tif` | GeoTIFF | Retrieved soil water content (m³/m³) |
| `soil_moisture_stats.json` | JSON | Model coefficients, retrieval statistics, synthetic validation (RMSE/correlation) |
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

# SAR土壤湿度反演（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-sar-soil-moisture
description: 'SAR 土壤湿度反演：基于简化 Dubois/Oh 半经验模型，由后向散射系数 σ⁰、入射角与地表粗糙度解析反演裸土体积含水量 (m³/m³)'
---

# SAR土壤湿度反演 | SAR Soil Moisture Retrieval

从 SAR 后向散射系数 σ⁰ 反演裸土地表土壤体积含水量 mv (m³/m³)。采用简化的
Dubois / Oh 半经验物理模型：

    σ⁰_dB(mv, ks, θ) = A(θ) + B(θ)·(k·s) + C(θ)·mv

其中 θ 为入射角，k = 2π/λ 为雷达波数（C 波段 λ≈5.6 cm），s 为地表 RMS 高度，
ks = k·s 为归一化粗糙度；C(θ) ∝ cos²θ 为湿度敏感项。σ⁰_dB 对 mv 单调线性，
反演时解析求解并裁剪到物理有效范围 [0.01, 0.60] m³/m³。

## 应用场景

- 农田墒情监测、干旱评估
- 水文模型土壤水分同化
- 灌溉管理与精准农业

## 依赖

```bash
pip install 'numpy' 'rasterio'
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-sar-soil-moisture.py --bbox 116.0 39.0 117.0 40.0 --incidence-angle 40 --model dubois --synthetic --output-dir ./out
```

### 示例 2（Oh 模型）

```bash
python geoskill-sar-soil-moisture.py --bbox 116.0 39.0 117.0 40.0 --model oh --synthetic --output-dir ./out
```

### 示例 3（真实 σ⁰ 影像）

```bash
python geoskill-sar-soil-moisture.py --input sigma0_db.tif --model dubois --roughness-ks 1.2 --output-dir ./out
```

### 示例 4（不同入射角）

```bash
python geoskill-sar-soil-moisture.py --input sigma0_db.tif --incidence-angle 35 --model oh --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `soil_moisture.tif` | GeoTIFF | 反演土壤含水量 (m³/m³) |
| `soil_moisture_stats.json` | JSON | 模型系数、反演统计、合成验证 (RMSE/相关) |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地 σ⁰ (dB) GeoTIFF，或 `--synthetic` 土壤湿度 + 粗糙度场正演的模拟场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
