# Spatial Autocorrelation Analysis (geoskill-spatial-autocorrelation)

> Global Moran's I + LISA + Gi* + Monte Carlo test to assess spatial clustering patterns

---

## 1. Overview

Assesses spatial clustering patterns: computes Global Moran's I (with z/p values from the normal approximation), Local Moran's I (LISA) and Getis-Ord Gi*, and derives pseudo p-values via Monte Carlo random permutation tests. Supports rook adjacency and KNN weight matrices.

## 2. Features

Assesses spatial clustering patterns: computes Global Moran's I (with z/p values from the normal approximation), Local Moran's I (LISA) and Getis-Ord Gi*, and derives pseudo p-values via Monte Carlo random permutation tests. Supports rook adjacency and KNN weight matrices.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-spatial-autocorrelation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `lisa.tif` | GeoTIFF/GeoJSON/JSON | Primary output |
| `gi_star.tif` | GeoTIFF/GeoJSON/JSON | Primary output |
| `autocorrelation_stats.json` | GeoTIFF/GeoJSON/JSON | Primary output |
| `output-manifest.json` | JSON | Run manifest |

## 6. Technical Principle

- Global Moran's I and its variance
- LISA local autocorrelation
- Getis-Ord Gi* and Monte Carlo test

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 空间自相关分析（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-spatial-autocorrelation
description: 'Global Moran I+LISA+Gi*+蒙特卡洛检验，评估空间聚集模式'
---

# 空间自相关分析 | Spatial Autocorrelation

评估空间聚集模式：计算 Global Moran's I（含正态近似 z/p 值）、Local Moran's I（LISA）与 Getis-Ord Gi*，并用蒙特卡洛随机置换检验给出伪 p 值。支持 rook 邻接与 KNN 权重矩阵。

## 核心算法

- Global Moran's I 及方差
- LISA 局部自相关
- Getis-Ord Gi* 与蒙特卡洛检验

## 依赖

```bash
pip install numpy rasterio scipy geopandas shapely
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-spatial-autocorrelation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（指定区域 + 静默）

```bash
python geoskill-spatial-autocorrelation.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### 示例 3（真实输入）

```bash
python geoskill-spatial-autocorrelation.py --input <你的数据文件> --output-dir ./out3
```

### 示例 4（极小区域边界测试）

```bash
python geoskill-spatial-autocorrelation.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `lisa.tif` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `gi_star.tif` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `autocorrelation_stats.json` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- 合成模式：本地生成物理一致的模拟数据，无外部数据源。
- 真实模式：读取本地输入文件，无网络请求。

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求。
- `--synthetic` 模式不读取任何外部数据。
- 所有计算在本地完成，不上传用户数据。

## License

MIT
