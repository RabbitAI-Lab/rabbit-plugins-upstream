# Machine Learning Land Cover Classification (geoskill-lulc-classification-ml)

> Per-pixel land cover classification from multi-band features using Random Forest / gradient boosting, with accuracy assessment, area statistics, and majority filtering to remove salt-and-pepper noise

---

## 1. Overview

Performs per-pixel supervised classification of multispectral imagery, producing land cover (LULC) class rasters. Feature engineering builds on the 6-band reflectance base, deriving NDVI and the local-variance texture of the near-infrared band to form a per-pixel feature vector. Classifiers support random forest (`rf`) and gradient boosting (`xgboost` option, with an offline equivalent implemented via scikit-learn's `GradientBoostingClassifier`). Typical applications: regional land use / land cover mapping, rapid inventory of urban and agricultural distribution, and preliminary classification feeding change detection. After classification, an optional 3×3 majority filter removes salt-and-pepper noise, and overall accuracy (OA), Kappa, and per-class producer's / user's accuracy are reported on a held-out validation set for quality control. Synthetic mode automatically generates labeled multispectral scenes (water / vegetation / cropland / built-up / bare soil, each with characteristic spectra), fully offline and suitable for teaching, pipeline validation, and unit testing.

## 2. Features

Performs per-pixel supervised classification of multispectral imagery, producing land cover (LULC) class rasters. Feature engineering builds on the 6-band reflectance base, deriving NDVI and the local-variance texture of the near-infrared band to form a per-pixel feature vector. Classifiers support random forest (`rf`) and gradient boosting (`xgboost` option, with an offline equivalent implemented via scikit-learn's `GradientBoostingClassifier`). Typical applications: regional land use / land cover mapping, rapid inventory of urban and agricultural distribution, and preliminary classification feeding change detection. After classification, an optional 3×3 majority filter removes salt-and-pepper noise, and overall accuracy (OA), Kappa, and per-class producer's / user's accuracy are reported on a held-out validation set for quality control. Synthetic mode automatically generates labeled multispectral scenes (water / vegetation / cropland / built-up / bare soil, each with characteristic spectra), fully offline and suitable for teaching, pipeline validation, and unit testing.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-lulc-classification-ml.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `lulc_classified.tif` | GeoTIFF (int32) | Per-pixel classification result (class indices) |
| `accuracy.json` | JSON | OA, Kappa, confusion matrix, per-class accuracy |
| `area_stats.json` | JSON | Per-class pixel count, proportion, area (km²) |
| `output-manifest.json` | JSON | Run manifest |

Class indices: 0=water, 1=vegetation, 2=cropland, 3=built_up, 4=bare_soil.


## 6. Technical Principle

(See SKILL.md for details.)

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 机器学习土地覆被分类（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-lulc-classification-ml
description: '多波段特征逐像元 RandomForest/梯度提升土地覆被分类，含精度评估、面积统计与众数滤波去盐噪'
---

# 机器学习土地覆被分类 | ML Land Cover Classification

对多光谱影像执行逐像元监督分类，产出土地覆被（LULC）类别栅格。特征工程以
6 波段反射率为基础，派生 NDVI 与近红外波段局部方差纹理，构成逐像元特征向量；
分类器支持随机森林（`rf`）与梯度提升（`xgboost` 选项，离线等价实现为
scikit-learn 的 `GradientBoostingClassifier`）。

典型应用：区域土地利用/覆被制图、城市与农田分布快速摸底、变化检测的前置
分类。分类后可选 3×3 众数滤波去除盐噪，并在留出验证集上输出总体精度（OA）、
Kappa 与逐类生产/用户精度，便于质量把关。

合成模式自动生成带标签的多光谱场景（水体/植被/耕地/建成区/裸地各具特征光谱），
完全离线，适合教学、流程验证与单元测试。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy' 'scikit-learn'
```

## 使用方法

### 基本用法

```bash
python geoskill-lulc-classification-ml.py --bbox 116.0 39.0 117.0 40.0 --n-classes 5 --method rf
```

### 示例 1（合成数据，离线）

```bash
python geoskill-lulc-classification-ml.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（梯度提升分类器）

```bash
python geoskill-lulc-classification-ml.py --bbox 121.0 31.0 122.0 32.0 --synthetic --method xgboost --output-dir ./out
```

### 示例 3（读取本地多光谱影像）

```bash
python geoskill-lulc-classification-ml.py --input scene_sr.tif --n-classes 5 --output-dir ./out
```

### 示例 4（关闭众数滤波）

```bash
python geoskill-lulc-classification-ml.py --bbox 116 39 117 40 --synthetic --no-filter --output-dir ./out
```

### 示例 5（3 类 + 自定义验证比例）

```bash
python geoskill-lulc-classification-ml.py --bbox 116 39 117 40 --synthetic --n-classes 3 --test-fraction 0.3 --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `lulc_classified.tif` | GeoTIFF (int32) | 逐像元分类结果（类别索引） |
| `accuracy.json` | JSON | OA、Kappa、混淆矩阵、逐类精度 |
| `area_stats.json` | JSON | 各类像元数、占比、面积（km²） |
| `output-manifest.json` | JSON | 运行清单 |

类别索引：0=water, 1=vegetation, 2=cropland, 3=built_up, 4=bare_soil。

## 数据源 / Source

- 本地多光谱 GeoTIFF（地表反射率，≥4 波段）；
- `--synthetic` 离线合成场景（无需网络、无需账号）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
