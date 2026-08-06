# Spatial Allocation of Educational Resources (geoskill-education-resource-allocation)

> Population distribution, accessibility and capacity constraints to optimize school layout and equity

---

## 1. Overview

For educational facility layout optimization: student demand per zone is estimated from population rasters, students are assigned to the nearest schools under capacity constraints, accessibility equity is evaluated, and new schools are sited with a greedy p-median approach. Assignment places students in existing schools in descending order of demand, nearest-first where capacity remains, and reports coverage rate and unmet demand; equity is measured with the Gini coefficient or coefficient of variation of per-zone accessibility distances (∈[0,1], higher = more equitable); siting greedily selects the k school sites from candidates that most reduce the population-weighted total accessibility distance.

## 2. Features

For educational facility layout optimization: student demand per zone is estimated from population rasters, students are assigned to the nearest schools under capacity constraints, accessibility equity is evaluated, and new schools are sited with a greedy p-median approach. Assignment places students in existing schools in descending order of demand, nearest-first where capacity remains, and reports coverage rate and unmet demand; equity is measured with the Gini coefficient or coefficient of variation of per-zone accessibility distances (∈[0,1], higher = more equitable); siting greedily selects the k school sites from candidates that most reduce the population-weighted total accessibility distance.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-education-resource-allocation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `allocation.json` | JSON | Allocation results (coverage/equity/enrollment per school, method=allocate/both) |
| `site_selection.json` | JSON | Siting results (selected sites/cost reduction, method=site-select/both) |
| `education_report.json` | JSON | Summary report |
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

# 教育资源空间配置（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-education-resource-allocation
description: 'Population distribution, accessibility and capacity constraints to optimize school layout and equity'
---

# 教育资源空间配置 | Education Resource Allocation

面向教育设施布局优化：由人口栅格估计各区学生需求，在容量约束下就近分配学生，评价可达性公平性，并用贪心 p-median 选址新建学校。

分配按“需求降序、就近有空位”把学生分到现有学校，统计覆盖率与未满足需求；公平性用基尼系数或变异系数度量各区可达距离（∈[0,1]，越大越公平）；选址从候选点中依次选出使人口加权总可达距离下降最大的 k 个校址。

## 依赖

```bash
pip install 'numpy' 'scipy' 'geopandas' 'shapely'
```

## 使用方法

### 基本用法

```bash
python geoskill-education-resource-allocation.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例 1（合成场景分配+选址，离线）

```bash
python geoskill-education-resource-allocation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
```

### 示例 2（真实人口栅格）

```bash
python geoskill-education-resource-allocation.py --input population.tif --output-dir ./out
```

### 示例 3（只做容量分配）

```bash
python geoskill-education-resource-allocation.py --input population.tif --method allocate --capacity 300 --output-dir ./out
```

### 示例 4（只做选址（新建 3 所））

```bash
python geoskill-education-resource-allocation.py --input population.tif --method site-select --k-new 3 --output-dir ./out
```

### 示例 5（改用变异系数度量公平）

```bash
python geoskill-education-resource-allocation.py --input population.tif --equity-metric cv --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `allocation.json` | JSON | 分配结果（覆盖率/公平性/各校载量，method=allocate/both） |
| `site_selection.json` | JSON | 选址结果（选中校址/成本下降，method=site-select/both） |
| `education_report.json` | JSON | 汇总报告 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

GeoTIFF 人口栅格（单波段）。 或使用 `--synthetic` 生成物理一致的模拟数据（完全离线）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
