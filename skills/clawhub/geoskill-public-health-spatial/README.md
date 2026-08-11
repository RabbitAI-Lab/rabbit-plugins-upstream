# Public Health Spatial Analysis (geoskill-public-health-spatial)

> Spatial scan statistics, kernel density, environment association and accessibility for public health spatial analysis

---

## 1. Overview

A spatial analysis toolkit for public health, covering disease-cluster detection, environmental association, and healthcare accessibility assessment. Kernel density estimation (KDE) maps case points with a 2D Gaussian kernel to identify hotspots; Kulldorff spatial scan statistics use circular moving windows that maximize the log-likelihood ratio (LLR) to detect the most likely cluster with significantly elevated incidence; Pearson correlation quantifies the association between incidence and environmental factors; distance to the nearest healthcare facility (Euclidean distance transform) assesses service accessibility.

## 2. Features

A spatial analysis toolkit for public health, covering disease-cluster detection, environmental association, and healthcare accessibility assessment. Kernel density estimation (KDE) maps case points with a 2D Gaussian kernel to identify hotspots; Kulldorff spatial scan statistics use circular moving windows that maximize the log-likelihood ratio (LLR) to detect the most likely cluster with significantly elevated incidence; Pearson correlation quantifies the association between incidence and environmental factors; distance to the nearest healthcare facility (Euclidean distance transform) assesses service accessibility.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-public-health-spatial.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `case_density.tif` | GeoTIFF | Case kernel density (method=kde/all) |
| `scan_result.json` | JSON | Most likely cluster (LLR/RR/center, method=scan/all) |
| `accessibility.tif` | GeoTIFF | Distance to nearest facility |
| `health_report.json` | JSON | Environmental correlations and accessibility statistics |
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

# 公共卫生空间分析（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-public-health-spatial
description: 'Spatial scan statistics, kernel density, environment association and accessibility for public health spatial analysis'
---

# 公共卫生空间分析 | Public Health Spatial Analysis

面向公共卫生的空间分析工具集，覆盖疾病聚集探测、环境关联与医疗可达性评估。

核密度估计 (KDE) 用 2D 高斯核对病例点做密度制图识别热点；Kulldorff 空间扫描统计用圆形移动窗口最大化对数似然比 (LLR) 探测发病率显著升高的最可能聚集区；Pearson 相关量化发病率与环境因子的关联；到最近医疗设施的距离（欧氏距离变换）评估服务可达性。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy' 'geopandas' 'shapely'
```

## 使用方法

### 基本用法

```bash
python geoskill-public-health-spatial.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例 1（合成场景全部方法，离线）

```bash
python geoskill-public-health-spatial.py --bbox 116 39 117 40 --synthetic --output-dir ./out
```

### 示例 2（真实人口/环境栅格）

```bash
python geoskill-public-health-spatial.py --input data.tif --output-dir ./out
```

### 示例 3（只做 KDE）

```bash
python geoskill-public-health-spatial.py --input data.tif --method kde --bandwidth 4 --output-dir ./out
```

### 示例 4（只做空间扫描）

```bash
python geoskill-public-health-spatial.py --input data.tif --method scan --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `case_density.tif` | GeoTIFF | 病例核密度（method=kde/all） |
| `scan_result.json` | JSON | 最可能聚集（LLR/RR/中心，method=scan/all） |
| `accessibility.tif` | GeoTIFF | 到最近设施距离 |
| `health_report.json` | JSON | 环境相关性与可达性统计 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

多波段 GeoTIFF，波段顺序 人口 / 环境因子。 或使用 `--synthetic` 生成物理一致的模拟数据（完全离线）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
