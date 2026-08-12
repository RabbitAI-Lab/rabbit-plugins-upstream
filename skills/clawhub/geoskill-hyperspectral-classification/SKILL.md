---
name: geoskill-hyperspectral-classification
description: 'PCA降维+RF/SVM逐像元高光谱监督分类'
---

# 高光谱分类 | Hyperspectral Classification

Performs per-pixel supervised classification on hyperspectral image cubes (bands × H × W, typically 30+ bands). PCA first projects the high-dimensional spectra into principal-component space to reduce noise and redundancy; a classifier is then trained with random forest (RF) or support vector machine (SVM) to predict the land-cover class of each pixel.

Synthetic mode automatically generates N land-cover classes with characteristic spectral signatures (e.g., minerals/vegetation/soil/water), distributed as spatial patches with added noise; training samples are produced by stratified sampling from the ground-truth labels (70% training / 30% validation by default). The outputs include a classification map, accuracy assessment (overall accuracy, Kappa), and a confusion matrix. Suitable for hyperspectral mapping, mineral/vegetation mapping, and method-comparison teaching.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy scikit-learn
```

## Usage / 使用方法

### Basic Usage (Synthetic Data, Offline)

```bash
python geoskill-hyperspectral-classification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 1: Random Forest, 4-Class Classification (30 Bands)

```bash
python geoskill-hyperspectral-classification.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --synthetic --n-bands 30 --n-classes 4 --method rf \
    --output-dir ./rf_4class
```

### Example 2: SVM Method Comparison

```bash
python geoskill-hyperspectral-classification.py \
    --bbox 121.0 31.0 122.0 32.0 \
    --synthetic --n-bands 30 --n-classes 4 --method svm \
    --output-dir ./svm_4class
```

### Example 3: More Classes and Bands

```bash
python geoskill-hyperspectral-classification.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --synthetic --n-bands 60 --n-classes 6 --method rf \
    --output-dir ./rf_6class
```

### Example 4: Real Hyperspectral GeoTIFF Input

```bash
python geoskill-hyperspectral-classification.py \
    --input cuprite_subset.tif --method rf \
    --output-dir ./real_rf
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `classification.tif` | GeoTIFF (int class ID) | Per-pixel classification result, EPSG:4326 |
| `accuracy.json` | JSON | Overall accuracy, Kappa, confusion matrix, per-class accuracy |
| `output-manifest.json` | JSON | Run manifest (input/output/QA/software versions) |

## Data Source / 数据源 / Source

- **Real mode**: local hyperspectral GeoTIFF (multi-band rasters exported from ENVI/PRISMA/AVIRIS, etc.)
- **Synthetic mode**: locally generates characteristic spectral curves + spatial patches, with no external data source

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default and makes no network requests
- `--synthetic` mode reads no external data
- All computation is done locally; user data is never uploaded

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-hyperspectral-classification
description: 'PCA降维+RF/SVM逐像元高光谱监督分类'
---

# 高光谱分类 | Hyperspectral Classification

对高光谱影像立方体（bands × H × W，波段数通常 30+）执行逐像元监督
分类。先用 PCA 把高维光谱投影到主成分空间降噪去冗余，再用随机森林
（RF）或支持向量机（SVM）训练分类器，对每个像元预测地物类别。

合成模式自动生成 N 类具有特征光谱曲线的地物（如矿物/植被/土壤/水体），
按空间斑块分布并叠加噪声；训练样本由真值标签分层抽样产生（默认 70%
训练 / 30% 验证），输出分类图、精度评估（总体精度、Kappa）与混淆
矩阵。适用于高光谱制图、矿物/植被填图、方法对比教学等场景。

## 依赖

```bash
pip install numpy rasterio scipy scikit-learn
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-hyperspectral-classification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 1：随机森林 4 类分类（30 波段）

```bash
python geoskill-hyperspectral-classification.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --synthetic --n-bands 30 --n-classes 4 --method rf \
    --output-dir ./rf_4class
```

### 示例 2：SVM 方法对比

```bash
python geoskill-hyperspectral-classification.py \
    --bbox 121.0 31.0 122.0 32.0 \
    --synthetic --n-bands 30 --n-classes 4 --method svm \
    --output-dir ./svm_4class
```

### 示例 3：更多类别与波段

```bash
python geoskill-hyperspectral-classification.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --synthetic --n-bands 60 --n-classes 6 --method rf \
    --output-dir ./rf_6class
```

### 示例 4：真实高光谱 GeoTIFF 输入

```bash
python geoskill-hyperspectral-classification.py \
    --input cuprite_subset.tif --method rf \
    --output-dir ./real_rf
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `classification.tif` | GeoTIFF (int 类别号) | 逐像元分类结果，EPSG:4326 |
| `accuracy.json` | JSON | 总体精度、Kappa、混淆矩阵、各类精度 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

- **真实模式**：本地高光谱 GeoTIFF（ENVI/PRISMA/AVIRIS 等导出的多波段栅格）
- **合成模式**：本地生成特征光谱曲线 + 空间斑块，无外部数据源

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
