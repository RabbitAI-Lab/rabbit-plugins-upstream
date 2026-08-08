# Few-Shot Remote Sensing Classification (geoskill-few-shot-classification)

> Prototype-network class-center distance plus nearest-neighbor classification; outputs a classification raster (offline numpy-equivalent implementation).

---

## 1. Overview

Classifies an entire image with very few labeled samples (1–5 per class): the mean feature of each class's support samples serves as the "prototype", every pixel is assigned to the nearest prototype, and a softmax(−distance) confidence is produced; few-shot episode accuracy evaluation is also supported. This skill is an **offline numpy-equivalent implementation** of Prototypical Networks few-shot learning: it does not depend on torch and reproduces the metric-learning paradigm via "feature extraction → support-set normalization → prototype computation → nearest-prototype classification by Euclidean distance". Unit tests cover 1-shot and multi-shot episode accuracy, probability normalization, and errors for insufficient samples.

## 2. Features

Classifies an entire image with very few labeled samples (1–5 per class): the mean feature of each class's support samples serves as the "prototype", every pixel is assigned to the nearest prototype, and a softmax(−distance) confidence is produced; few-shot episode accuracy evaluation is also supported. This skill is an **offline numpy-equivalent implementation** of Prototypical Networks few-shot learning: it does not depend on torch and reproduces the metric-learning paradigm via "feature extraction → support-set normalization → prototype computation → nearest-prototype classification by Euclidean distance". Unit tests cover 1-shot and multi-shot episode accuracy, probability normalization, and errors for insufficient samples.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-few-shot-classification.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `classification.tif` | GeoTIFF | Whole-image nearest-prototype classification label map |
| `few_shot_report.json` | JSON | Episode accuracy / confidence / number of support samples |
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

# 小样本遥感分类（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-few-shot-classification
description: '原型网络类中心距离+最近邻分类，输出分类栅格（离线numpy等价实现）'
---

# 小样本遥感分类 | Few-Shot Remote Sensing Classification

用极少量标注样本（每类 1~5 个）完成整幅影像分类：每类支持样本的特征均值作为"原型"，像元按最近原型归类，并给出 softmax(-距离) 置信度；支持少样本回合 (episode) 精度评估。

本 skill 是 Prototypical Networks 少样本学习的**离线 numpy 等价实现**：不依赖 torch，用"特征提取 -> 支持集标准化 -> 原型计算 -> 欧氏距离最近原型分类"复现度量学习范式；1-shot 与多 shot 回合精度、概率归一性、样本不足报错等均有单元测试覆盖。

## 依赖

```bash
pip install numpy rasterio scipy scikit-learn geopandas shapely
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-few-shot-classification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2：合成 3-way 3-shot（离线）

```bash
python geoskill-few-shot-classification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --n-shot 3 --output-dir ./out
```

### 示例 3：1-shot 极限小样本

```bash
python geoskill-few-shot-classification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --n-shot 1 --output-dir ./out
```

### 示例 4：真实影像伪少样本（KMeans 选支持）

```bash
python geoskill-few-shot-classification.py --input scene.tif --n-classes 4 --n-shot 5 --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `classification.tif` | GeoTIFF | 整幅最近原型分类标签图 |
| `few_shot_report.json` | JSON | episode 精度/置信度/支持样本数 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/退出码） |

## 数据源 / Source

本地多波段 GeoTIFF，或 --synthetic 三类光谱可分场景（真值用于 episode 评估）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
