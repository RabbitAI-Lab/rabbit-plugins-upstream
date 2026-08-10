---
name: geoskill-public-health-spatial
description: 'Spatial scan statistics, kernel density, environment association and accessibility for public health spatial analysis'
---

# 公共卫生空间分析 | Public Health Spatial Analysis

A spatial analysis toolbox for public health, covering disease cluster detection, environmental association and healthcare accessibility assessment.

Kernel density estimation (KDE) maps case density with a 2D Gaussian kernel to identify hot spots; Kulldorff spatial scan statistics use a circular moving window to maximize the log-likelihood ratio (LLR) and detect the most likely clusters of significantly elevated incidence; Pearson correlation quantifies the association between incidence and environmental factors; the distance to the nearest healthcare facility (Euclidean distance transform) assesses service accessibility.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy' 'geopandas' 'shapely'
```

## Usage / 使用方法

### Basic usage

```bash
python geoskill-public-health-spatial.py --bbox 116.0 39.0 117.0 40.0 [other options]
```

### Example 1 (all methods on a synthetic scene, offline)

```bash
python geoskill-public-health-spatial.py --bbox 116 39 117 40 --synthetic --output-dir ./out
```

### Example 2 (real population/environment rasters)

```bash
python geoskill-public-health-spatial.py --input data.tif --output-dir ./out
```

### Example 3 (KDE only)

```bash
python geoskill-public-health-spatial.py --input data.tif --method kde --bandwidth 4 --output-dir ./out
```

### Example 4 (spatial scan only)

```bash
python geoskill-public-health-spatial.py --input data.tif --method scan --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `case_density.tif` | GeoTIFF | Case kernel density (method=kde/all) |
| `scan_result.json` | JSON | Most likely cluster (LLR/RR/center, method=scan/all) |
| `accessibility.tif` | GeoTIFF | Distance to nearest facility |
| `health_report.json` | JSON | Environmental correlation and accessibility statistics |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

Multi-band GeoTIFF with band order population / environmental factors. Alternatively, use `--synthetic` to generate physically consistent simulated data (fully offline).

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is performed locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
