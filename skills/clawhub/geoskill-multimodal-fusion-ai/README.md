# Multimodal Remote Sensing AI Fusion (geoskill-multimodal-fusion-ai)

> Multi-source raster normalization + weighted fusion + joint classification, outputting a fused classification raster (offline numpy equivalent implementation)

---

## 1. Overview

Normalizes multiple heterogeneous data sources (optical/SAR/thermal infrared, etc., input as multi-band rasters where band = modality) to a comparable scale, fuses them with user-specified or automatic weights, and performs joint classification on the fused image. This skill is an **offline numpy equivalent implementation** of multimodal deep learning fusion networks: without relying on deep learning frameworks, it reproduces the multi-source fusion paradigm via "per-source min-max/z-score normalization → inverse-noise-variance automatic weighting (MAD Laplacian noise estimation) → weighted-average fusion → KMeans joint classification"; synthetic data guarantees that "fusion noise is lower than any single source" is a verifiable mathematical fact.

## 2. Features

Normalizes multiple heterogeneous data sources (optical/SAR/thermal infrared, etc., input as multi-band rasters where band = modality) to a comparable scale, fuses them with user-specified or automatic weights, and performs joint classification on the fused image. This skill is an **offline numpy equivalent implementation** of multimodal deep learning fusion networks: without relying on deep learning frameworks, it reproduces the multi-source fusion paradigm via "per-source min-max/z-score normalization → inverse-noise-variance automatic weighting (MAD Laplacian noise estimation) → weighted-average fusion → KMeans joint classification"; synthetic data guarantees that "fusion noise is lower than any single source" is a verifiable mathematical fact.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-multimodal-fusion-ai.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `fused.tif` | GeoTIFF | Weighted fusion raster |
| `classification.tif` | GeoTIFF | Joint classification labels of the fused image |
| `fusion_report.json` | JSON | Weights, per-source/fused noise levels, and denoising verdict |
| `output-manifest.json` | JSON | Run manifest (input/output/QA/exit code) |


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

# 多模态遥感AI融合（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-multimodal-fusion-ai
description: '多源栅格标准化+加权融合+联合分类，输出融合分类栅格（离线numpy等价实现）'
---

# 多模态遥感AI融合 | Multimodal Remote Sensing AI Fusion

把多个异源数据（光学/SAR/热红外等，以多波段栅格输入，波段 = 模态）标准化到可比尺度，按用户权重或自动权重加权融合，并在融合图上做联合分类。

本 skill 是多模态深度学习融合网络的**离线 numpy 等价实现**：不依赖深度学习框架，用"逐源 min-max/z-score 标准化 -> 逆噪声方差自动加权（MAD 拉普拉斯噪声估计）-> 加权平均融合 -> KMeans 联合分类"复现多源融合范式；合成数据保证"融合噪声低于任一单源"成为可验证的数学事实。

## 依赖

```bash
pip install numpy rasterio scipy scikit-learn geopandas shapely
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-multimodal-fusion-ai.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2：合成双模态融合（离线）

```bash
python geoskill-multimodal-fusion-ai.py --bbox 116.0 39.0 117.0 40.0 --synthetic --n-classes 3 --output-dir ./out
```

### 示例 3：指定权重融合

```bash
python geoskill-multimodal-fusion-ai.py --input multi.tif --weights 0.7,0.3 --output-dir ./out
```

### 示例 4：z-score 标准化

```bash
python geoskill-multimodal-fusion-ai.py --input multi.tif --norm zscore --n-classes 5 --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `fused.tif` | GeoTIFF | 加权融合栅格 |
| `classification.tif` | GeoTIFF | 融合图联合分类标签 |
| `fusion_report.json` | JSON | 权重、各源/融合噪声水平与降噪判定 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/退出码） |

## 数据源 / Source

本地多波段 GeoTIFF（各波段 = 一个模态），或 --synthetic（同一场景的光学式 + SAR 式双观测）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
