---
name: geoskill-location-allocation
description: 'p-median/p-center/最大覆盖选址模型+需求权重分配'
---

# 选址-分配分析 | Location Allocation

Classic facility location models: p-median (minimizes the demand-weighted total distance; greedy + Teitz-Bart exchange), p-center (minimizes the maximum service distance), and max-coverage (maximizes the demand covered within a threshold distance; MCLP greedy).

## Core Algorithm / 核心算法

- p-median (greedy + exchange improvement)
- p-center minimax
- Max-coverage MCLP + demand weights

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy geopandas shapely
```

## Usage / 使用方法

### Example 1 (synthetic data, offline)

```bash
python geoskill-location-allocation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (specified area + quiet mode)

```bash
python geoskill-location-allocation.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### Example 3 (real input)

```bash
python geoskill-location-allocation.py --input <your data file> --output-dir ./out3
```

### Example 4 (edge-case test on a tiny area)

```bash
python geoskill-location-allocation.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `allocation.geojson` | GeoTIFF/GeoJSON/JSON | Primary output |
| `allocation_stats.json` | GeoTIFF/GeoJSON/JSON | Primary output |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- Synthetic mode: locally generated, physically consistent simulated data; no external data source.
- Real mode: reads local input files; no network requests.

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default; makes no network requests.
- `--synthetic` mode reads no external data.
- All computation is done locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-location-allocation
description: 'p-median/p-center/最大覆盖选址模型+需求权重分配'
---

# 选址-分配分析 | Location Allocation

经典设施选址模型：p-median（最小化需求加权总距离，贪心 + Teitz-Bart 交换）、p-center（最小化最大服务距离）、max-coverage（阈值内最大化覆盖需求，MCLP 贪心）。

## 核心算法

- p-median（贪心 + 交换改进）
- p-center 最小最大
- 最大覆盖 MCLP + 需求权重

## 依赖

```bash
pip install numpy rasterio scipy geopandas shapely
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-location-allocation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（指定区域 + 静默）

```bash
python geoskill-location-allocation.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### 示例 3（真实输入）

```bash
python geoskill-location-allocation.py --input <你的数据文件> --output-dir ./out3
```

### 示例 4（极小区域边界测试）

```bash
python geoskill-location-allocation.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `allocation.geojson` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `allocation_stats.json` | GeoTIFF/GeoJSON/JSON | 主产物 |
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
