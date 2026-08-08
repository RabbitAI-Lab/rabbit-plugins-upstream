# Air Quality Dispersion Simulation (geoskill-air-quality-dispersion)

> Simulates point-source pollutant concentration fields with a Gaussian plume model, Pasquill-Gifford A-F stability parameterization of σy/σz, plus DEM terrain correction. Outputs a concentration-field GeoTIFF + parameters JSON.

---

## 1. Overview

Standard Gaussian plume formula (with ground reflection term): C = Q/(2π·u·σy·σz)·exp(-y²/2σy²)·[exp(-(z-H)²/2σz²)+exp(-(z+H)²/2σz²)]. σy/σz are parameterized with the Briggs formulas for the six Pasquill-Gifford stability classes A-F; a terrain correction factor converts terrain above the source into an effective source-height reduction and higher concentrations (clipped to 0.5-3.0). Use cases: environmental impact assessment of industrial parks, chimney siting, and rapid estimation of pollution exposure.

## 2. Features

Standard Gaussian plume formula (with ground reflection term): C = Q/(2π·u·σy·σz)·exp(-y²/2σy²)·[exp(-(z-H)²/2σz²)+exp(-(z+H)²/2σz²)]. σy/σz are parameterized with the Briggs formulas for the six Pasquill-Gifford stability classes A-F; a terrain correction factor converts terrain above the source into an effective source-height reduction and higher concentrations (clipped to 0.5-3.0). Use cases: environmental impact assessment of industrial parks, chimney siting, and rapid estimation of pollution exposure.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-air-quality-dispersion.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `concentration.tif` | GeoTIFF (float32) | Ground-level concentration field (μg/m³, with terrain correction), EPSG:4326 |
| `dispersion_params.json` | JSON | Stability class, source strength, wind speed, source location, concentration statistics |
| `output-manifest.json` | JSON | Run manifest (input/output/QA/software version) |


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

# 空气质量扩散模拟（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-air-quality-dispersion
description: '高斯烟羽模型模拟点源污染物浓度场，Pasquill-Gifford A-F 稳定度参数化 σy/σz，叠加 DEM 地形修正。Simulates pollutant concentration fields with a Gaussian plume model plus terrain correction. 输出浓度场 GeoTIFF + 参数 JSON。'
---

# 空气质量扩散模拟 | Air Quality Dispersion Modeling

标准高斯烟羽公式（含地面反射项）：C = Q/(2π·u·σy·σz)·exp(-y²/2σy²)·[exp(-(z-H)²/2σz²)+exp(-(z+H)²/2σz²)]。σy/σz 用 Briggs 公式按 A-F 六类大气稳定度参数化；地形修正因子把高于源的地形折算为有效源高降低、浓度增大（clip 0.5-3.0）。

适用场景：工业园区环评、烟囱选址、污染暴露快速估算。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 示例 1：中性大气（D 类）默认源强

```bash
python geoskill-air-quality-dispersion.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### 示例 2：稳定大气（F 类）+ 强源

```bash
python geoskill-air-quality-dispersion.py --bbox 116 39 117 40 --synthetic --stability F --source-strength 500 --output-dir ./stable
```

### 示例 3：真实 DEM 地形修正

```bash
python geoskill-air-quality-dispersion.py --bbox 116 39 117 40 --input dem.tif --stability D --output-dir ./terrain
```

### 示例 4：高烟囱 + 大风速

```bash
python geoskill-air-quality-dispersion.py --bbox 116 39 117 40 --synthetic --effective-height 120 --wind-speed 6 --output-dir ./tall_stack
```

### 示例 5：静默批量

```bash
python geoskill-air-quality-dispersion.py --bbox 121 31 122 32 --synthetic --quiet --output-dir ./batch
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `concentration.tif` | GeoTIFF (float32) | 地面浓度场（μg/m³，含地形修正），EPSG:4326 |
| `dispersion_params.json` | JSON | 稳定度、源强、风速、源位置、浓度统计 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

本地 DEM GeoTIFF（可选，地形修正）；Pasquill-Gifford/Briggs 扩散参数为公开发表经验值；合成模式生成平坦地形，无外部数据源。

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
