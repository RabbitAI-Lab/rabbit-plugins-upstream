# Insurance Risk Mapping (geoskill-insurance-risk-mapping)

> Multi-hazard probability times asset value times vulnerability curves to compute expected loss for insurance risk mapping

---

## 1. Overview

Multi-hazard Expected Annual Loss (EAL) mapping for property and catastrophe insurance, providing a spatial basis for underwriting, loss reserving, and risk diversification. Core model: EAL = Σ_h P_h · Asset · V_h(I_h), where P_h = 1/return period is the annual exceedance probability of hazard h, Asset is the per-pixel asset value, and V_h is the vulnerability curve mapping hazard intensity to a loss ratio in [0,1] (linear or Sigmoid). Flood, wind, and earthquake losses are computed separately and then overlaid to produce per-pixel expected annual loss and risk class.

## 2. Features

Multi-hazard Expected Annual Loss (EAL) mapping for property and catastrophe insurance, providing a spatial basis for underwriting, loss reserving, and risk diversification. Core model: EAL = Σ_h P_h · Asset · V_h(I_h), where P_h = 1/return period is the annual exceedance probability of hazard h, Asset is the per-pixel asset value, and V_h is the vulnerability curve mapping hazard intensity to a loss ratio in [0,1] (linear or Sigmoid). Flood, wind, and earthquake losses are computed separately and then overlaid to produce per-pixel expected annual loss and risk class.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-insurance-risk-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `expected_annual_loss.tif` | GeoTIFF | Multi-hazard expected annual loss |
| `per_hazard_loss.tif` | GeoTIFF | Per-hazard loss (flood/wind/earthquake) |
| `risk_class.tif` | GeoTIFF | Risk class |
| `risk_report.json` | JSON | Total insured value / total loss / loss ratio / class statistics |
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

# 保险风险制图（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-insurance-risk-mapping
description: 'Multi-hazard probability times asset value times vulnerability curves to compute expected loss for insurance risk mapping'
---

# 保险风险制图 | Insurance Risk Mapping

面向财产/巨灾保险的多灾种年期望损失 (Expected Annual Loss, EAL) 制图，为承保定价、准备金与风险分散提供空间依据。

核心模型 EAL = Σ_h P_h · Asset · V_h(I_h)：P_h = 1/重现期为第 h 种灾害年超越概率，Asset 为像元资产价值，V_h 为把灾害强度映射为损失比 ∈[0,1] 的脆弱性曲线（线性或 Sigmoid）。对洪水、风灾、地震分别计算后叠加，得到逐像元年期望损失与风险等级。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-insurance-risk-mapping.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例 1（合成场景，离线）

```bash
python geoskill-insurance-risk-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out
```

### 示例 2（真实数据（Asset/Flood/Wind/Seismic））

```bash
python geoskill-insurance-risk-mapping.py --input data.tif --output-dir ./out
```

### 示例 3（改用 Sigmoid 脆弱性曲线）

```bash
python geoskill-insurance-risk-mapping.py --input data.tif --curve sigmoid --output-dir ./out
```

### 示例 4（自定义风险分档）

```bash
python geoskill-insurance-risk-mapping.py --input data.tif --class-breaks 5 50 500 --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `expected_annual_loss.tif` | GeoTIFF | 多灾种年期望损失 |
| `per_hazard_loss.tif` | GeoTIFF | 分灾种损失（洪水/风灾/地震） |
| `risk_class.tif` | GeoTIFF | 风险等级 |
| `risk_report.json` | JSON | 总保额/总损失/损失率/分级统计 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

多波段 GeoTIFF，波段顺序 Asset / Flood / Wind / Seismic 强度。 或使用 `--synthetic` 生成物理一致的模拟数据（完全离线）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
