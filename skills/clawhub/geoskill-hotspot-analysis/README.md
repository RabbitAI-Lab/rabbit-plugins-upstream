# Hotspot Analysis (geoskill-hotspot-analysis)

> Getis-Ord Gi* hotspot analysis + kernel density estimation + multi-scale significance testing

---

## 1. Overview

Identifies statistically significant hotspots (clusters of high values) and coldspots (clusters of low values) using the Getis-Ord Gi* statistic, combined with Gaussian kernel density estimation (KDE) and multi-scale analysis. Outputs Gi* z-score raster, 90/95/99% significance level rasters, and kernel density raster.

## 2. Features

Identifies statistically significant hotspots (clusters of high values) and coldspots (clusters of low values) using the Getis-Ord Gi* statistic, combined with Gaussian kernel density estimation (KDE) and multi-scale analysis. Outputs Gi* z-score raster, 90/95/99% significance level rasters, and kernel density raster.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-hotspot-analysis.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `gi_star_zscore.tif` | GeoTIFF/GeoJSON/JSON | Primary output |
| `hotspot_significance.tif` | GeoTIFF/GeoJSON/JSON | Primary output |
| `kernel_density.tif` | GeoTIFF/GeoJSON/JSON | Primary output |
| `hotspot_stats.json` | GeoTIFF/GeoJSON/JSON | Primary output |
| `output-manifest.json` | JSON | Run manifest |


## 6. Technical Principle

- Getis-Ord Gi* z-score
- Significance classification (90/95/99%)
- Gaussian kernel density estimation + multi-scale

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 热点分析（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-hotspot-analysis
description: 'Getis-Ord Gi*热点分析+核密度估计+多尺度显著性检验'
---

# 热点分析 | Hotspot Analysis

基于 Getis-Ord Gi* 统计量识别统计显著的热点（高值聚集）与冷点（低值聚集），叠加高斯核密度估计（KDE）与多尺度分析。输出 Gi* z 得分栅格、90/95/99% 显著性分级栅格与核密度栅格。

## 核心算法

- Getis-Ord Gi* z 得分
- 显著性分级（90/95/99%）
- 高斯核密度估计 + 多尺度

## 依赖

```bash
pip install numpy rasterio scipy geopandas shapely
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-hotspot-analysis.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（指定区域 + 静默）

```bash
python geoskill-hotspot-analysis.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### 示例 3（真实输入）

```bash
python geoskill-hotspot-analysis.py --input <你的数据文件> --output-dir ./out3
```

### 示例 4（极小区域边界测试）

```bash
python geoskill-hotspot-analysis.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `gi_star_zscore.tif` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `hotspot_significance.tif` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `kernel_density.tif` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `hotspot_stats.json` | GeoTIFF/GeoJSON/JSON | 主产物 |
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
