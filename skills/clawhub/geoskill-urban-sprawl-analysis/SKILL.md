---
name: geoskill-urban-sprawl-analysis
description: '多期城市边界量化蔓延形态指标：紧凑度、分形维数、重心迁移与扩张面积速率'
---

# 城市蔓延分析 | Urban Sprawl Analysis

Quantifies the morphology and spatiotemporal dynamics of urban sprawl from multi-epoch urban boundaries (binary rasters, 1=built-up): compactness (circularity 4πA/P²), fractal dimension (perimeter–area relationship D=2·ln(P/4)/ln(A)), built-up centroid coordinates and centroid displacement between adjacent epochs (km), new/net added area (km²), and growth rate.

Typical applications: urban expansion monitoring, sprawl morphology assessment, and compact city indicator accounting in planning. The synthetic mode generates a sequence of urban patches that expand outward and drift eastward epoch by epoch, simultaneously validating two expectations: "net expansion detected" and "centroid shifts eastward". Multi-epoch boundaries are vectorized with geopandas/shapely into a GeoJSON with year attributes, facilitating mapping and downstream spatial analysis.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy' 'geopandas' 'shapely'
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-urban-sprawl-analysis.py --bbox 116.0 39.0 117.0 40.0 --n-dates 4
```

### Example 1 (Synthetic Data, Offline)

```bash
python geoskill-urban-sprawl-analysis.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (Reading Multi-Epoch Binary Rasters, One Epoch per Band)

```bash
python geoskill-urban-sprawl-analysis.py --input urban_multidate.tif --output-dir ./out
```

### Example 3 (Custom Year Interval)

```bash
python geoskill-urban-sprawl-analysis.py --bbox 121 31 122 32 --synthetic --start-year 2005 --interval-years 5 --output-dir ./out
```

### Example 4 (3 Epochs + Silent Mode)

```bash
python geoskill-urban-sprawl-analysis.py --bbox 116 39 117 40 --synthetic --n-dates 3 --quiet --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `sprawl_metrics.json` | JSON | Per-epoch morphological metrics + changes between adjacent epochs + summary |
| `centroid_trajectory.json` | JSON | Centroid trajectory and total displacement |
| `urban_footprint.geojson` | GeoJSON | Multi-epoch urban boundary polygons (with year) |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- Local multi-band binary GeoTIFF (one epoch per band, 1=built-up);
- `--synthetic` generates an offline expansion sequence (no network, no account required).

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
