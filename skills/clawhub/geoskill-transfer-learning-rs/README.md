# Transfer Learning for Remote Sensing (geoskill-transfer-learning-rs)

> Feature extraction + fine-tuned classifier + accuracy assessment, outputting classification results and an accuracy report (offline numpy-equivalent implementation)

---

## 1. Overview

Extracts features from imagery with a frozen feature extractor, fine-tunes a lightweight classification head on top of them, and evaluates accuracy on a held-out validation set, while comparing against a "raw spectra only" baseline to quantify the gain from transferred features. This skill is an **offline numpy-equivalent implementation** of deep transfer learning (pretrained backbone + fine-tuned head): it does not depend on torch/tensorflow, using a fixed filter bank (raw spectra + Sobel gradients + local-mean texture) as the "frozen backbone" and sklearn logistic regression/random forest as the "classification head"; train/validation split, leakage-free normalization and transfer-gain comparison are all validated in unit tests.

## 2. Features

Extracts features from imagery with a frozen feature extractor, fine-tunes a lightweight classification head on top of them, and evaluates accuracy on a held-out validation set, while comparing against a "raw spectra only" baseline to quantify the gain from transferred features. This skill is an **offline numpy-equivalent implementation** of deep transfer learning (pretrained backbone + fine-tuned head): it does not depend on torch/tensorflow, using a fixed filter bank (raw spectra + Sobel gradients + local-mean texture) as the "frozen backbone" and sklearn logistic regression/random forest as the "classification head"; train/validation split, leakage-free normalization and transfer-gain comparison are all validated in unit tests.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-transfer-learning-rs.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `classification.tif` | GeoTIFF | Full-scene classification/clustering label map |
| `accuracy_report.json` | JSON | Validation accuracy, baseline comparison and transfer gain |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/exit code) |

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

# 遥感迁移学习（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-transfer-learning-rs
description: '特征提取+微调分类器+精度评估，输出分类结果与精度报告（离线numpy等价实现）'
---

# 遥感迁移学习 | Remote Sensing Transfer Learning

用冻结的特征提取器从影像抽取特征，在其上微调轻量分类头，并在留出验证集上评估精度，同时与"仅用原始光谱"的基线对比，量化迁移特征的增益。

本 skill 是深度迁移学习（预训练主干 + fine-tune 头）的**离线 numpy 等价实现**：不依赖 torch/tensorflow，用固定滤波 bank（原始光谱 + Sobel 梯度 + 局部均值纹理）充当"冻结主干"，sklearn 逻辑回归/随机森林充当"分类头"；训练/验证划分、防泄漏标准化、迁移增益对比均在单元测试中验证。

## 依赖

```bash
pip install numpy rasterio scipy scikit-learn geopandas shapely
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-transfer-learning-rs.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2：合成有监督迁移评估（离线）

```bash
python geoskill-transfer-learning-rs.py --bbox 116.0 39.0 117.0 40.0 --synthetic --train-frac 0.6 --output-dir ./out
```

### 示例 3：真实影像无监督特征聚类

```bash
python geoskill-transfer-learning-rs.py --input scene.tif --n-classes 4 --output-dir ./out
```

### 示例 4：随机森林分类头

```bash
python geoskill-transfer-learning-rs.py --bbox 116.0 39.0 117.0 40.0 --synthetic --model rf --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `classification.tif` | GeoTIFF | 全幅分类/聚类标签图 |
| `accuracy_report.json` | JSON | 验证精度、基线对比与迁移增益 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/退出码） |

## 数据源 / Source

本地多波段 GeoTIFF（真实模式无监督聚类），或 --synthetic 三类真值场景（有监督评估）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
