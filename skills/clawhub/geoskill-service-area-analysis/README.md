# Service Area Analysis (geoskill-service-area-analysis)

> Network isochrone analysis + multi-facility service areas + coverage statistics, outputting service area GeoJSON.

---

## 1. Overview

Computes facility service areas (isochrones) from a network graph: Dijkstra computes network travel time for each facility, service areas are delineated by time thresholds, with support for multi-facility overlay, nearest-facility assignment and multi-threshold coverage statistics.

## 2. Features

Computes facility service areas (isochrones) from a network graph: Dijkstra computes network travel time for each facility, service areas are delineated by time thresholds, with support for multi-facility overlay, nearest-facility assignment and multi-threshold coverage statistics.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-service-area-analysis.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `service_area.geojson` | GeoTIFF/GeoJSON/JSON | Primary output |
| `service_area_stats.json` | GeoTIFF/GeoJSON/JSON | Primary output |
| `output-manifest.json` | JSON | Run manifest |

## 6. Technical Principle

- Multi-source Dijkstra isochrones
- Nearest-facility assignment
- Multi-threshold coverage demand statistics

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 服务区分析（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-service-area-analysis
description: '网络等时圈分析+多设施服务区+覆盖统计，输出服务区GeoJSON'
---

# 服务区分析 | Service Area Analysis

基于网络图计算设施服务区（等时圈）：对每个设施用 Dijkstra 计算网络通行时间，按时间阈值划分服务区，支持多设施叠加、最近设施分配与多阈值覆盖统计。

## 核心算法

- 多源 Dijkstra 等时圈
- 最近设施分配
- 多阈值覆盖需求统计

## 依赖

```bash
pip install numpy rasterio scipy geopandas shapely
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-service-area-analysis.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（指定区域 + 静默）

```bash
python geoskill-service-area-analysis.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### 示例 3（真实输入）

```bash
python geoskill-service-area-analysis.py --input <你的数据文件> --output-dir ./out3
```

### 示例 4（极小区域边界测试）

```bash
python geoskill-service-area-analysis.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `service_area.geojson` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `service_area_stats.json` | GeoTIFF/GeoJSON/JSON | 主产物 |
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
