---
name: geoskill-transfer-learning-rs
description: '特征提取+微调分类器+精度评估，输出分类结果与精度报告（离线numpy等价实现）'
---

# 遥感迁移学习 | Remote Sensing Transfer Learning

Extracts features from imagery with a frozen feature extractor, fine-tunes a lightweight classification head on top, evaluates accuracy on a held-out validation set, and compares against a "raw-spectra-only" baseline to quantify the gain from transferred features.

This skill is an **offline numpy-equivalent implementation** of deep transfer learning (pretrained backbone + fine-tuned head): with no torch/tensorflow dependency, a fixed filter bank (raw spectra + Sobel gradients + local-mean texture) serves as the "frozen backbone", and an sklearn logistic regression / random forest serves as the "classification head"; the train/validation split, leak-free standardization, and transfer-gain comparison are all verified in unit tests.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy scikit-learn geopandas shapely
```

## Usage / 使用方法

### Example 1 (synthetic data, offline)

```bash
python geoskill-transfer-learning-rs.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2: Synthetic supervised transfer evaluation (offline)

```bash
python geoskill-transfer-learning-rs.py --bbox 116.0 39.0 117.0 40.0 --synthetic --train-frac 0.6 --output-dir ./out
```

### Example 3: Unsupervised feature clustering of a real image

```bash
python geoskill-transfer-learning-rs.py --input scene.tif --n-classes 4 --output-dir ./out
```

### Example 4: Random forest classification head

```bash
python geoskill-transfer-learning-rs.py --bbox 116.0 39.0 117.0 40.0 --synthetic --model rf --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `classification.tif` | GeoTIFF | Full-scene classification / clustering label map |
| `accuracy_report.json` | JSON | Validation accuracy, baseline comparison, and transfer gain |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/exit code) |

## Data Source / 数据源 / Source

Local multi-band GeoTIFF (unsupervised clustering in real mode), or a `--synthetic` three-class ground-truth scene (supervised evaluation).

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is performed locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
