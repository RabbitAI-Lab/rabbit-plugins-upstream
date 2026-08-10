# Land Value Estimation (geoskill-land-value-estimation)

> Estimate land value with a hedonic price model driven by accessibility, POI density and green proximity.

---

## 1. Overview

Estimates the spatial distribution of land value with a hedonic price model, supporting land price appraisal and location analysis. Core algorithms: accessibility = exp(−distance to center/decay scale), higher closer to the center; green proximity is analogous; value = intercept + β_acc×accessibility + β_poi×POI density + β_green×green proximity. The model is linearly additive with non-negative value; it includes a least-squares coefficient calibration function that can exactly recover known coefficients from samples.

## 2. Features

Estimates the spatial distribution of land value with a hedonic price model, supporting land price appraisal and location analysis. Core algorithms: accessibility = exp(−distance to center/decay scale), higher closer to the center; green proximity is analogous; value = intercept + β_acc×accessibility + β_poi×POI density + β_green×green proximity. The model is linearly additive with non-negative value; it includes a least-squares coefficient calibration function that can exactly recover known coefficients from samples.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-land-value-estimation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `land_value.tif` | GeoTIFF | Land value raster |
| `hedonic_coefficients.json` | JSON | Hedonic model coefficients and decay scale |
| `value_stats.json` | JSON | Value mean/range, mean accessibility |
| `output-manifest.json` | JSON | Run manifest |

## 6. Technical Principle

(See SKILL.md for details)

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 土地价值估算（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-land-value-estimation
description: 'Estimate land value with a hedonic price model driven by accessibility, POI density and green proximity.'
---

# 土地价值估算 | Land Value Estimation

用特征价格（Hedonic）模型估算土地价值空间分布，服务于地价评估与区位分析。

核心算法：可达性 = exp(−到中心距离/衰减尺度)，越靠近中心越高；绿地邻近性同理；价值 = 截距 + β_acc×可达性 + β_poi×POI密度 + β_green×绿地邻近性。模型线性可加、价值非负；附带最小二乘系数标定函数，可由样本精确恢复已知系数。

## 依赖

```bash
pip install 'numpy' 'rasterio'
```

## 使用方法

### 基本用法

```bash
python geoskill-land-value-estimation.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例

#### 示例 1（合成数据（离线））

```bash
python geoskill-land-value-estimation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### 示例 2（用法 2）

```bash
python geoskill-land-value-estimation.py --input features.tif --output-dir ./out
```

#### 示例 3（用法 3）

```bash
python geoskill-land-value-estimation.py --bbox 121.0 31.0 122.0 32.0 --decay 50 --output-dir ./out --quiet
```

#### 示例 4（用法 4）

```bash
python geoskill-land-value-estimation.py --input features.tif --coef-acc 8000 --intercept 2000 --output-dir ./out
```

#### 示例 5（用法 5）

```bash
python geoskill-land-value-estimation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --coef-poi 3000 --output-dir ./out --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `land_value.tif` | GeoTIFF | 土地价值栅格 |
| `hedonic_coefficients.json` | JSON | Hedonic 模型系数与衰减尺度 |
| `value_stats.json` | JSON | 价值均值/范围、平均可达性 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地三波段特征 GeoTIFF（到中心距离、POI 密度、到绿地距离）；`--synthetic` 模式模拟单中心城市格局。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
