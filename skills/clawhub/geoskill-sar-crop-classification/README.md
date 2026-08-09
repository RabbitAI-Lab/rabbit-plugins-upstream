# SAR Crop Classification (geoskill-sar-crop-classification)

> Crop classification based on multi-temporal SAR backscatter time series: per-pixel time-series/statistical/phenological features + Random Forest. SAR crop classification from multi-temporal backscatter time series using per-pixel phenological features and Random Forest. Synthetic mode generates ground-truth time series for rice/wheat/maize and evaluates accuracy, outputting a classification GeoTIFF + area statistics + confusion matrix JSON.

---

## 1. Overview

(Fill in 2-3 paragraphs of introduction here: features, application scenarios, core algorithms.)

## 2. Features

(Fill in 2-3 paragraphs of introduction here: features, application scenarios, core algorithms.)

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-sar-crop-classification.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `result.tif` | GeoTIFF | Primary output |
| `output-manifest.json` | JSON | Run manifest |

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

# SAR农作物分类（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

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
