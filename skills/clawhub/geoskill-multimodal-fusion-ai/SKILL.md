---
name: geoskill-multimodal-fusion-ai
description: '多源栅格标准化+加权融合+联合分类，输出融合分类栅格（离线numpy等价实现）'
---

# 多模态遥感AI融合 | Multimodal Remote Sensing AI Fusion

Normalizes multiple heterogeneous data sources (optical/SAR/thermal infrared, etc., supplied as multi-band rasters with each band = one modality) to a comparable scale, fuses them by user-specified or automatic weights, and performs joint classification on the fused image.

This skill is an **offline numpy-equivalent implementation** of a multimodal deep-learning fusion network: without relying on any deep-learning framework, it reproduces the multi-source fusion paradigm via "per-source min-max/z-score normalization → automatic inverse-noise-variance weighting (MAD Laplacian noise estimation) → weighted-average fusion → KMeans joint classification"; synthetic data guarantees that "fused noise below that of any single source" becomes a verifiable mathematical fact.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy scikit-learn geopandas shapely
```

## Usage / 使用方法

### Example 1 (synthetic data, offline)

```bash
python geoskill-multimodal-fusion-ai.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2: synthetic dual-modal fusion (offline)

```bash
python geoskill-multimodal-fusion-ai.py --bbox 116.0 39.0 117.0 40.0 --synthetic --n-classes 3 --output-dir ./out
```

### Example 3: fusion with specified weights

```bash
python geoskill-multimodal-fusion-ai.py --input multi.tif --weights 0.7,0.3 --output-dir ./out
```

### Example 4: z-score normalization

```bash
python geoskill-multimodal-fusion-ai.py --input multi.tif --norm zscore --n-classes 5 --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `fused.tif` | GeoTIFF | Weighted fusion raster |
| `classification.tif` | GeoTIFF | Joint classification labels of the fused image |
| `fusion_report.json` | JSON | Weights, per-source/fused noise levels and denoising verdict |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/exit code) |

## Data Source / 数据源 / Source

Local multi-band GeoTIFF (each band = one modality), or `--synthetic` (optical-like + SAR-like dual observations of the same scene).

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is performed locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
