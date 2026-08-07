# D-InSAR Coherence Analysis (geoskill-dinsar-coherence-analysis)

> Estimate multi-look complex coherence and interferometric phase from registered master/slave complex SLC images, identifying stable scatterers and decorrelated change areas (building changes / landslides / vegetation), and outputting coherence and phase GeoTIFFs plus statistics JSON.

---

## 1. Overview

Estimate the **complex coherence coefficient** and **interferometric phase** from registered master/slave complex single-look images (SLC): - **Complex coherence** γ = |Σ(m·conj(s))| / sqrt(Σ|m|²·Σ|s|²), estimated within a `--looks-r` × `--looks-a` multi-look window. γ∈[0,1]: stable scatterers (buildings, exposed bedrock) show high coherence; changed areas (new construction / demolition, landslide bodies, vegetation) decorrelate and show low coherence. - **Interferometric phase** φ = angle(Σ m·conj(s)), reflecting line-of-sight deformation / topographic phase. Multi-looking is implemented with a boxcar sliding-window mean, where the normalization between numerator and denominator within the same window cancels out.

## 2. Features

Estimate the **complex coherence coefficient** and **interferometric phase** from registered master/slave complex single-look images (SLC): - **Complex coherence** γ = |Σ(m·conj(s))| / sqrt(Σ|m|²·Σ|s|²), estimated within a `--looks-r` × `--looks-a` multi-look window. γ∈[0,1]: stable scatterers (buildings, exposed bedrock) show high coherence; changed areas (new construction / demolition, landslide bodies, vegetation) decorrelate and show low coherence. - **Interferometric phase** φ = angle(Σ m·conj(s)), reflecting line-of-sight deformation / topographic phase. Multi-looking is implemented with a boxcar sliding-window mean, where the normalization between numerator and denominator within the same window cancels out.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-dinsar-coherence-analysis.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `coherence.tif` | GeoTIFF (float32) | Complex coherence γ∈[0,1], EPSG:4326 |
| `phase.tif` | GeoTIFF (float32) | Interferometric phase φ∈(-π,π], EPSG:4326 |
| `coherence_statistics.json` | JSON | Mean / quantiles / low-coherence area, etc. |
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

# D-InSAR 相干性分析（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-dinsar-coherence-analysis
description: '从配准主/从复SLC估计多视复相干系数γ与干涉相位，识别稳定散射体与去相关变化区（建筑变化/滑坡/植被），输出相干性与相位GeoTIFF及统计JSON。D-InSAR complex coherence and interferometric phase estimation with multi-looking.'
---

# D-InSAR 相干性分析 | D-InSAR Coherence Analysis

从配准后的主 / 从复单视图像（SLC）估计 **复相干系数** 与 **干涉相位**：

- **复相干系数** γ = |Σ(m·conj(s))| / sqrt(Σ|m|²·Σ|s|²)，在
  `--looks-r` × `--looks-a` 多视窗口内估计。γ∈[0,1]：稳定散射体（建筑、
  裸岩）相干性高；变化区域（新建 / 拆除、滑坡体、植被）去相关、相干性低。
- **干涉相位** φ = angle(Σ m·conj(s))，反映视线向形变 / 地形相位。

多视用 boxcar 滑窗均值实现，分子分母同窗口归一化相互抵消。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（仅给 bbox，自动合成主从 SLC）

```bash
python geoskill-dinsar-coherence-analysis.py --bbox 116.0 39.0 117.0 40.0 --output-dir ./out
```

### 示例 1：合成数据（离线）

```bash
python geoskill-dinsar-coherence-analysis.py --bbox 116 39 117 40 --synthetic --looks-r 5 --looks-a 1 --output-dir ./syn
```

### 示例 2：真实主从 SLC

```bash
python geoskill-dinsar-coherence-analysis.py --input master_slc.tif --slave slave_slc.tif --looks-r 5 --looks-a 2 --output-dir ./real
```

### 示例 3：更大多视窗（更平滑相干性）

```bash
python geoskill-dinsar-coherence-analysis.py --bbox 116 39 117 40 --looks-r 8 --looks-a 4 --output-dir ./smooth --quiet
```

### 示例 4：指定极化与低相干阈值

```bash
python geoskill-dinsar-coherence-analysis.py --bbox 121 31 122 32 --polarization vh --coh-threshold 0.4 --output-dir ./sh --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `coherence.tif` | GeoTIFF (float32) | 复相干系数 γ∈[0,1]，EPSG:4326 |
| `phase.tif` | GeoTIFF (float32) | 干涉相位 φ∈(-π,π]，EPSG:4326 |
| `coherence_statistics.json` | JSON | 均值 / 分位数 / 低相干区面积等 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- **真实模式**：本地配准主 / 从复 SLC GeoTIFF（2 波段：实部 + 虚部）。
- **合成模式**：本地生成主从复 SLC（稳定区高相关 + 注入变化斑块去相关）。

## 隐私声明 / Privacy

- 默认完全离线运行，`--synthetic` 无任何网络。
- 所有处理本地完成，不上传用户数据。

## License

MIT
