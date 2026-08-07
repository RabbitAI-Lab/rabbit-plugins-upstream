---
name: geoskill-habitat-suitability-modeling
description: '由多变量环境栅格训练物种分布模型，输出 0-1 栖息地适宜性概率与变量贡献度。Models habitat suitability probability from environmental rasters with RF or logistic regression. 输出适宜性 GeoTIFF + 模型参数 JSON（含交叉验证 AUC）。'
---

# 栖息地适宜性建模 | Habitat Suitability Modeling

Using environmental rasters such as temperature, precipitation, vegetation, and terrain as features, trains a species distribution model with random forest (rf) or logistic regression (logreg), outputs a habitat suitability probability in [0,1], and reports the relative contribution of each environmental variable (normalized to sum to 1). A built-in 3-fold cross-validated AUC serves as the measure of model discriminative ability.

Synthetic mode generates presence/absence labels from a known niche (NDVI-driven), allowing offline verification that the model correctly learns the dominant variable; real-input mode generates pseudo-presence from high-quantile suitability as an unsupervised fallback.

## Dependencies / 依赖

```bash
pip install numpy rasterio scikit-learn scipy
```

## Usage / 使用方法

### Example 1: Synthetic Niche + Random Forest

```bash
python geoskill-habitat-suitability-modeling.py --bbox 116.0 39.0 117.0 40.0 --synthetic --model rf --output-dir ./output
```

### Example 2: Logistic Regression (Linearly Interpretable)

```bash
python geoskill-habitat-suitability-modeling.py --bbox 116 39 117 40 --synthetic --model logreg --output-dir ./logreg
```

### Example 3: Real Environmental Rasters (Each Band = One Environmental Variable)

```bash
python geoskill-habitat-suitability-modeling.py --input env_stack.tif --model rf --output-dir ./real
```

### Example 4: Changing the Random Seed

```bash
python geoskill-habitat-suitability-modeling.py --bbox 121 31 122 32 --synthetic --seed 7 --output-dir ./seed7
```

### Example 5: Quiet Mode

```bash
python geoskill-habitat-suitability-modeling.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `habitat_suitability.tif` | GeoTIFF (float32) | Suitability probability ∈ [0,1], EPSG:4326 |
| `suitability_params.json` | JSON | Model type, sample count, CV AUC, variable contributions |
| `output-manifest.json` | JSON | Run manifest (input/output/QA/software versions) |

## Data Source / 数据源 / Source

Local multi-band GeoTIFF (each band = an environmental variable); synthetic mode locally generates four layers (temperature/precipitation/NDVI/elevation) and known-niche labels, with no external data source.

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default and makes no network requests
- `--synthetic` mode reads no external data
- All computation is done locally; user data is never uploaded

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-habitat-suitability-modeling
description: '由多变量环境栅格训练物种分布模型，输出 0-1 栖息地适宜性概率与变量贡献度。Models habitat suitability probability from environmental rasters with RF or logistic regression. 输出适宜性 GeoTIFF + 模型参数 JSON（含交叉验证 AUC）。'
---

# 栖息地适宜性建模 | Habitat Suitability Modeling

以温度、降水、植被、地形等环境栅格为特征，训练随机森林（rf）或逻辑回归（logreg）物种分布模型，输出 0-1 的栖息地适宜性概率，并给出各环境变量的相对贡献（归一化和为 1）。内置 3 折交叉验证 AUC 作为模型判别能力度量。

合成模式按已知生态位（NDVI 驱动）生成 presence/absence 标签，可离线验证模型能否正确学到主导变量；真实输入模式用高分位适宜度生成伪 presence（unsupervised fallback）。

## 依赖

```bash
pip install numpy rasterio scikit-learn scipy
```

## 使用方法

### 示例 1：合成生态位 + 随机森林

```bash
python geoskill-habitat-suitability-modeling.py --bbox 116.0 39.0 117.0 40.0 --synthetic --model rf --output-dir ./output
```

### 示例 2：逻辑回归（线性可解释）

```bash
python geoskill-habitat-suitability-modeling.py --bbox 116 39 117 40 --synthetic --model logreg --output-dir ./logreg
```

### 示例 3：真实环境栅格（每个波段=一个环境变量）

```bash
python geoskill-habitat-suitability-modeling.py --input env_stack.tif --model rf --output-dir ./real
```

### 示例 4：更换随机种子

```bash
python geoskill-habitat-suitability-modeling.py --bbox 121 31 122 32 --synthetic --seed 7 --output-dir ./seed7
```

### 示例 5：静默模式

```bash
python geoskill-habitat-suitability-modeling.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `habitat_suitability.tif` | GeoTIFF (float32) | 适宜性概率 ∈ [0,1]，EPSG:4326 |
| `suitability_params.json` | JSON | 模型类型、样本数、CV AUC、变量贡献度 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

本地多波段 GeoTIFF（各波段=环境变量）；合成模式本地生成温度/降水/NDVI/高程四层与已知生态位标签，无外部数据源。

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
