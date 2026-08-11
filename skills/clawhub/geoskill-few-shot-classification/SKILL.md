---
name: geoskill-few-shot-classification
description: '原型网络类中心距离+最近邻分类，输出分类栅格（离线numpy等价实现）'
---

# 小样本遥感分类 | Few-Shot Remote Sensing Classification

Classifies an entire image using very few labeled samples (1–5 per class): the feature mean of each class's support samples serves as the "prototype", each pixel is assigned to the nearest prototype, and a softmax(−distance) confidence is provided; few-shot episode accuracy evaluation is supported.

This skill is an **offline numpy-equivalent implementation** of Prototypical Networks few-shot learning: without depending on torch, it reproduces the metric-learning paradigm through "feature extraction → support-set standardization → prototype computation → nearest-prototype classification by Euclidean distance"; unit tests cover 1-shot and multi-shot episode accuracy, probability normalization, and errors for insufficient samples.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy scikit-learn geopandas shapely
```

## Usage / 使用方法

### Example 1 (synthetic data, offline)

```bash
python geoskill-few-shot-classification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2: synthetic 3-way 3-shot (offline)

```bash
python geoskill-few-shot-classification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --n-shot 3 --output-dir ./out
```

### Example 3: extreme 1-shot few-sample case

```bash
python geoskill-few-shot-classification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --n-shot 1 --output-dir ./out
```

### Example 4: pseudo few-shot on real imagery (support selected by KMeans)

```bash
python geoskill-few-shot-classification.py --input scene.tif --n-classes 4 --n-shot 5 --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `classification.tif` | GeoTIFF | Full-image nearest-prototype classification label map |
| `few_shot_report.json` | JSON | Episode accuracy/confidence/number of support samples |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/exit code) |

## Data Source / 数据源 / Source

Local multi-band GeoTIFF, or --synthetic for a three-class spectrally separable scenario (ground truth used for episode evaluation).

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; no user data is ever uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
