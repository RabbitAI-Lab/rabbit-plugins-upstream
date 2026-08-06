# Urban Microclimate Analysis (geoskill-urban-microclimate)

> Analyze urban heat island intensity and ventilation index from land surface temperature, NDVI, impervious surface and building morphology.

---

## 1. Overview

Analyzes urban microclimate from land surface temperature, vegetation, impervious surface and building morphology to support heat island mitigation and ventilation planning. Core algorithm: LST modeling = baseline temperature + α×ISA − β×NDVI (impervious surfaces heat; vegetation evapotranspiration cools); urban heat island intensity UHII = LST − suburban reference temperature, positively correlated with ISA; ventilation index VI = SVF×(1−building density) ∈ [0,1]; high density with a low sky view factor → poor ventilation.

## 2. Features

Analyzes urban microclimate from land surface temperature, vegetation, impervious surface and building morphology to support heat island mitigation and ventilation planning. Core algorithm: LST modeling = baseline temperature + α×ISA − β×NDVI (impervious surfaces heat; vegetation evapotranspiration cools); urban heat island intensity UHII = LST − suburban reference temperature, positively correlated with ISA; ventilation index VI = SVF×(1−building density) ∈ [0,1]; high density with a low sky view factor → poor ventilation.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-urban-microclimate.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `microclimate.tif` | GeoTIFF | Three bands: band1 = LST, band2 = heat island intensity UHII, band3 = ventilation index |
| `microclimate_stats.json` | JSON | Mean LST/UHII, max UHII, ventilation index, UHII-ISA correlation coefficient |
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

# 城市微气候分析（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-urban-microclimate
description: 'Analyze urban heat island intensity and ventilation index from land surface temperature, NDVI, impervious surface and building morphology.'
---

# 城市微气候分析 | Urban Microclimate Analysis

从地表温度、植被、不透水面与建筑形态分析城市微气候，服务于热岛缓解与通风规划。

核心算法：LST 建模 = 基准温度 + α×ISA − β×NDVI（不透水面加热、植被蒸散降温）；热岛强度 UHII = LST − 郊区参考温度，与 ISA 正相关；通风指数 VI = SVF×(1−建筑密度) ∈ [0,1]，密度高且天空可视因子低 → 通风差。

## 依赖

```bash
pip install 'numpy' 'rasterio'
```

## 使用方法

### 基本用法

```bash
python geoskill-urban-microclimate.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例

#### 示例 1（合成数据（离线））

```bash
python geoskill-urban-microclimate.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### 示例 2（用法 2）

```bash
python geoskill-urban-microclimate.py --input features.tif --output-dir ./out
```

#### 示例 3（用法 3）

```bash
python geoskill-urban-microclimate.py --bbox 121.0 31.0 122.0 32.0 --rural-temp 23 --output-dir ./out --quiet
```

#### 示例 4（用法 4）

```bash
python geoskill-urban-microclimate.py --input features.tif --alpha 12 --beta 5 --output-dir ./out
```

#### 示例 5（用法 5）

```bash
python geoskill-urban-microclimate.py --bbox 116.0 39.0 117.0 40.0 --synthetic --base-temp 26 --output-dir ./out --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `microclimate.tif` | GeoTIFF | 三波段：band1=LST，band2=热岛强度 UHII，band3=通风指数 |
| `microclimate_stats.json` | JSON | 平均 LST/UHII、最大 UHII、通风指数、UHII-ISA 相关系数 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地四波段 GeoTIFF（ISA, NDVI, 建筑密度, SVF）；`--synthetic` 模式模拟中心-郊区热岛梯度场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
