---
name: geoskill-sar-crop-classification
description: '基于多时相 SAR 后向散射时序的农作物分类：逐像元时序/统计/物候特征 + 随机森林。SAR crop classification from multi-temporal backscatter time series using per-pixel phenological features and Random Forest. 合成模式生成水稻/小麦/玉米三类时序真值并评估精度，输出分类 GeoTIFF + 面积统计 + 混淆矩阵 JSON。'
---

# SAR农作物分类 | SAR Crop Classification

(Fill in 2-3 paragraphs of Chinese introduction here: features, application scenarios, core algorithm.)

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy' 'scikit-learn'
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-sar-crop-classification.py --bbox 116.0 39.0 117.0 40.0 [other options]
```

### Example 1 (synthetic data, offline)

```bash
python geoskill-sar-crop-classification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Examples 2-5

(Add at least 4 real usage examples.)

## Output / 输出

| File | Format | Description |
|---|---|---|
| `result.tif` | GeoTIFF | Primary output |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

(Describe the data source: free satellite data / local input / synthetic.)

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode is fully network-free.
- All processing is done locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-sar-crop-classification
description: '基于多时相 SAR 后向散射时序的农作物分类：逐像元时序/统计/物候特征 + 随机森林。SAR crop classification from multi-temporal backscatter time series using per-pixel phenological features and Random Forest. 合成模式生成水稻/小麦/玉米三类时序真值并评估精度，输出分类 GeoTIFF + 面积统计 + 混淆矩阵 JSON。'
---

# SAR农作物分类 | SAR Crop Classification

（在此填写 2-3 段中文介绍：功能、应用场景、核心算法。）

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy' 'scikit-learn'
```

## 使用方法

### 基本用法

```bash
python geoskill-sar-crop-classification.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例 1（合成数据，离线）

```bash
python geoskill-sar-crop-classification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2-5

（补充至少 4 个真实用法示例。）

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `result.tif` | GeoTIFF | 主产物 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

（说明数据来源：免费卫星数据 / 本地输入 / 合成。）

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
