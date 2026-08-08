# Location-Allocation Analysis (geoskill-location-allocation)

> p-median / p-center / maximal-coverage location models with demand-weighted allocation

---

## 1. Overview

Classic facility location models: p-median (minimize demand-weighted total distance, greedy + Teitz-Bart exchange), p-center (minimize the maximum service distance), and max-coverage (maximize covered demand within a threshold, MCLP greedy).

## 2. Features

Classic facility location models: p-median (minimize demand-weighted total distance, greedy + Teitz-Bart exchange), p-center (minimize the maximum service distance), and max-coverage (maximize covered demand within a threshold, MCLP greedy).

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-location-allocation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `allocation.geojson` | GeoTIFF/GeoJSON/JSON | Primary output |
| `allocation_stats.json` | GeoTIFF/GeoJSON/JSON | Primary output |
| `output-manifest.json` | JSON | Run manifest |


## 6. Technical Principle

- p-median (greedy + exchange improvement)
- p-center minimax
- Maximal coverage MCLP + demand weights

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 选址-分配分析（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

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
