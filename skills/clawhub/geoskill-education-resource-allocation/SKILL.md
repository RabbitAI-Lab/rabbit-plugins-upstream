---
name: geoskill-education-resource-allocation
description: 'Population distribution, accessibility and capacity constraints to optimize school layout and equity'
---

# 教育资源空间配置 | Education Resource Allocation

For education facility layout optimization: student demand per district is estimated from the population raster, students are assigned to the nearest available school under capacity constraints, accessibility equity is evaluated, and new schools are sited with a greedy p-median algorithm.

Assignment sends students to existing schools in descending order of demand, nearest available capacity first, and reports coverage and unmet demand; equity is measured by the Gini coefficient or the coefficient of variation of district accessibility distances (∈[0,1], higher is more equitable); siting iteratively selects the k candidate sites that most reduce the population-weighted total accessibility distance.

## Dependencies / 依赖

```bash
pip install 'numpy' 'scipy' 'geopandas' 'shapely'
```

## Usage / 使用方法

### Basic usage

```bash
python geoskill-education-resource-allocation.py --bbox 116.0 39.0 117.0 40.0 [other options]
```

### Example 1 (synthetic scenario: allocation + siting, offline)

```bash
python geoskill-education-resource-allocation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
```

### Example 2 (real population raster)

```bash
python geoskill-education-resource-allocation.py --input population.tif --output-dir ./out
```

### Example 3 (allocation only)

```bash
python geoskill-education-resource-allocation.py --input population.tif --method allocate --capacity 300 --output-dir ./out
```

### Example 4 (siting only (build 3 new schools))

```bash
python geoskill-education-resource-allocation.py --input population.tif --method site-select --k-new 3 --output-dir ./out
```

### Example 5 (use the coefficient of variation for equity)

```bash
python geoskill-education-resource-allocation.py --input population.tif --equity-metric cv --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `allocation.json` | JSON | Allocation results (coverage/equity/loading per school; method=allocate/both) |
| `site_selection.json` | JSON | Siting results (selected sites/cost reduction; method=site-select/both) |
| `education_report.json` | JSON | Summary report |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

GeoTIFF population raster (single band), or use `--synthetic` to generate physically consistent simulated data (fully offline).

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
