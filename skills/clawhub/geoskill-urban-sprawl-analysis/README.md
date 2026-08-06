# Urban Sprawl Analysis (geoskill-urban-sprawl-analysis)

> Quantify sprawl morphology metrics from multi-temporal urban boundaries: compactness, fractal dimension, centroid shift and expansion area rate

---

## 1. Overview

Quantifies the morphology and spatiotemporal dynamics of urban sprawl from multi-temporal urban boundaries (binary rasters, 1 = built-up area): compactness (circularity 4πA/P²), fractal dimension (perimeter–area relation D = 2·ln(P/4)/ln(A)), built-up centroid coordinates and centroid displacement between adjacent periods (km), new/net added area (km²) and growth rate. Typical applications: urban expansion monitoring, sprawl morphology assessment, and compact-city indicator accounting for planning. Synthetic mode generates a sequence of urban patches that expand outward and drift eastward period by period, allowing both expected outcomes — "net expansion detected" and "centroid shifted east" — to be verified. Multi-period boundaries are vectorized with geopandas/shapely into a GeoJSON with year attributes, convenient for mapping and downstream spatial analysis.

## 2. Features

Quantifies the morphology and spatiotemporal dynamics of urban sprawl from multi-temporal urban boundaries (binary rasters, 1 = built-up area): compactness (circularity 4πA/P²), fractal dimension (perimeter–area relation D = 2·ln(P/4)/ln(A)), built-up centroid coordinates and centroid displacement between adjacent periods (km), new/net added area (km²) and growth rate. Typical applications: urban expansion monitoring, sprawl morphology assessment, and compact-city indicator accounting for planning. Synthetic mode generates a sequence of urban patches that expand outward and drift eastward period by period, allowing both expected outcomes — "net expansion detected" and "centroid shifted east" — to be verified. Multi-period boundaries are vectorized with geopandas/shapely into a GeoJSON with year attributes, convenient for mapping and downstream spatial analysis.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-urban-sprawl-analysis.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `sprawl_metrics.json` | JSON | Per-period morphology metrics + inter-period changes + summary |
| `centroid_trajectory.json` | JSON | Centroid trajectory and total displacement |
| `urban_footprint.geojson` | GeoJSON | Multi-period urban boundary polygons (with years) |
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

# 城市蔓延分析（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-urban-sprawl-analysis
description: '多期城市边界量化蔓延形态指标：紧凑度、分形维数、重心迁移与扩张面积速率'
---

# 城市蔓延分析 | Urban Sprawl Analysis

从多期城市边界（二值栅格，1=建成区）量化城市蔓延的形态与时空动态：
紧凑度（圆形度 4πA/P²）、分形维数（周长-面积关系 D=2·ln(P/4)/ln(A)）、
建成区重心坐标及相邻期重心位移（km）、新增/净增面积（km²）与增长率。

典型应用：城市扩张监测、蔓延形态评估、规划 compact city 指标核算。
合成模式生成一个逐期向外且偏东扩张的城市斑块序列，可同时验证
「检测到净扩张」与「重心东移」两项预期。多期边界用 geopandas/shapely
矢量化为带年份属性的 GeoJSON，便于制图与下游空间分析。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy' 'geopandas' 'shapely'
```

## 使用方法

### 基本用法

```bash
python geoskill-urban-sprawl-analysis.py --bbox 116.0 39.0 117.0 40.0 --n-dates 4
```

### 示例 1（合成数据，离线）

```bash
python geoskill-urban-sprawl-analysis.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（读取多期二值栅格，每波段一期）

```bash
python geoskill-urban-sprawl-analysis.py --input urban_multidate.tif --output-dir ./out
```

### 示例 3（自定义年份间隔）

```bash
python geoskill-urban-sprawl-analysis.py --bbox 121 31 122 32 --synthetic --start-year 2005 --interval-years 5 --output-dir ./out
```

### 示例 4（3 期 + 静默）

```bash
python geoskill-urban-sprawl-analysis.py --bbox 116 39 117 40 --synthetic --n-dates 3 --quiet --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `sprawl_metrics.json` | JSON | 逐期形态指标 + 相邻期变化 + 汇总 |
| `centroid_trajectory.json` | JSON | 重心轨迹与总位移 |
| `urban_footprint.geojson` | GeoJSON | 多期城市边界多边形（带年份） |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- 本地多波段二值 GeoTIFF（每波段一期，1=建成区）；
- `--synthetic` 离线合成扩张序列（无需网络、无需账号）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
