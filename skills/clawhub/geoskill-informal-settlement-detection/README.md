# Informal Settlement Detection (geoskill-informal-settlement-detection)

> Detect informal settlements by fusing texture irregularity, building morphology and spectral mixing into a classification score.

---

## 1. Overview

Detects informal settlements (urban villages / shantytowns) by fusing texture irregularity, building density, and spectral mixing, supporting urban renewal surveys and human settlement monitoring. Core algorithm: local standard deviation quantifies textural disorder; building density and NDVI (low vegetation) are combined and weighted on an absolute physical scale to produce an informal score in [0,1], and thresholding delineates informal settlements. High texture + high density + low NDVI → high score.

## 2. Features

Detects informal settlements (urban villages / shantytowns) by fusing texture irregularity, building density, and spectral mixing, supporting urban renewal surveys and human settlement monitoring. Core algorithm: local standard deviation quantifies textural disorder; building density and NDVI (low vegetation) are combined and weighted on an absolute physical scale to produce an informal score in [0,1], and thresholding delineates informal settlements. High texture + high density + low NDVI → high score.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-informal-settlement-detection.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `informal_score.tif` | GeoTIFF | Two bands: band1=informal score, band2=classification mask |
| `informal_stats.json` | JSON | Score mean, informal ratio, threshold |
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

# 非正规聚居区检测（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-informal-settlement-detection
description: 'Detect informal settlements by fusing texture irregularity, building morphology and spectral mixing into a classification score.'
---

# 非正规聚居区检测 | Informal Settlement Detection

融合纹理不规则性、建筑密度与光谱混合检测非正规聚居区（城中村/棚户区），服务于城市更新调查与人居环境监测。

核心算法：用局部标准差量化纹理无序度；结合建筑密度与 NDVI（低植被），以绝对物理标度加权得到非正规评分 [0,1]，阈值分割出非正规聚居区。高纹理 + 高密度 + 低 NDVI → 高评分。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-informal-settlement-detection.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例

#### 示例 1（合成数据（离线））

```bash
python geoskill-informal-settlement-detection.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### 示例 2（用法 2）

```bash
python geoskill-informal-settlement-detection.py --input multispectral.tif --footprints fp.tif --output-dir ./out
```

#### 示例 3（用法 3）

```bash
python geoskill-informal-settlement-detection.py --bbox 121.0 31.0 122.0 32.0 --threshold 0.6 --output-dir ./out --quiet
```

#### 示例 4（用法 4）

```bash
python geoskill-informal-settlement-detection.py --input ms.tif --kernel-size 7 --output-dir ./out
```

#### 示例 5（用法 5）

```bash
python geoskill-informal-settlement-detection.py --bbox 116.0 39.0 117.0 40.0 --synthetic --threshold 0.4 --output-dir ./out --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `informal_score.tif` | GeoTIFF | 双波段：band1=非正规评分，band2=分类掩膜 |
| `informal_stats.json` | JSON | 评分均值、非正规比例、阈值 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地多光谱 GeoTIFF（Red, NIR）+ 可选建筑足迹；`--synthetic` 模式模拟非正规区与正规区各半的场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
