---
name: geoskill-ai-accuracy-assessment
description: '混淆矩阵+OA/mIoU/F1计算+空间精度图，输出精度评估报告（离线numpy等价实现）'
---

# AI模型精度评估 | AI Model Accuracy Assessment

Performs a comprehensive accuracy assessment of classification/segmentation model predictions: confusion matrix, overall accuracy (OA), per-class Precision/Recall/F1, mean Intersection over Union (mIoU), Cohen's Kappa, and local accuracy maps that reveal the spatial distribution of errors.

This skill is an **offline NumPy-equivalent implementation** of the model evaluation pipeline: all metrics are computed directly with NumPy, and each one has unit tests against hand-computed baselines (cell-by-cell confusion matrix, exact OA/mIoU/Kappa values, spatial localization of error blocks).

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy scikit-learn geopandas shapely
```

## Usage / 使用方法

### Example 1 (Synthetic Data, Offline)

```bash
python geoskill-ai-accuracy-assessment.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2: Synthetic Evaluation Experiment (Offline, with Known Error Blocks)

```bash
python geoskill-ai-accuracy-assessment.py --bbox 116.0 39.0 117.0 40.0 --synthetic --window 7 --output-dir ./out
```

### Example 3: Prediction + Ground Truth Dual Rasters

```bash
python geoskill-ai-accuracy-assessment.py --input pred.tif --truth ref.tif --output-dir ./out
```

### 示例 4：单文件双波段 [pred, truth]

```bash
python geoskill-ai-accuracy-assessment.py --input pair.tif --window 9 --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `accuracy_report.json` | JSON | Confusion matrix/OA/mIoU/Kappa/per-class metrics |
| `spatial_accuracy.tif` | GeoTIFF | Windowed local accuracy map [0,1] |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/exit code) |

## Data Source / 数据源 / Source

Prediction/truth label rasters, or --synthetic (truth stripes + systematic error blocks + randomly scattered errors).

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; no user data is ever uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-ai-accuracy-assessment
description: '混淆矩阵+OA/mIoU/F1计算+空间精度图，输出精度评估报告（离线numpy等价实现）'
---

# AI模型精度评估 | AI Model Accuracy Assessment

对分类/分割模型预测做全面精度评估：混淆矩阵、总体精度 OA、逐类 Precision/Recall/F1、平均交并比 mIoU、Cohen's Kappa，以及揭示误差空间分布的局部精度图。

本 skill 是模型评测流水线的**离线 numpy 等价实现**：所有指标由 numpy 直接计算，每一项都有手算基准的单元测试（混淆矩阵逐格、OA/mIoU/Kappa 精确值、误差块空间定位）。

## 依赖

```bash
pip install numpy rasterio scipy scikit-learn geopandas shapely
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-ai-accuracy-assessment.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2：合成评估实验（离线，含已知误差块）

```bash
python geoskill-ai-accuracy-assessment.py --bbox 116.0 39.0 117.0 40.0 --synthetic --window 7 --output-dir ./out
```

### 示例 3：预测 + 真值双栅格

```bash
python geoskill-ai-accuracy-assessment.py --input pred.tif --truth ref.tif --output-dir ./out
```

### 示例 4：单文件双波段 [pred, truth]

```bash
python geoskill-ai-accuracy-assessment.py --input pair.tif --window 9 --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `accuracy_report.json` | JSON | 混淆矩阵/OA/mIoU/Kappa/逐类指标 |
| `spatial_accuracy.tif` | GeoTIFF | 窗口局部精度图 [0,1] |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/退出码） |

## 数据源 / Source

预测/真值标签栅格，或 --synthetic（真值条带 + 系统性误差块 + 随机散布误差）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
