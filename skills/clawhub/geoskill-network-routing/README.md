# Network Routing (geoskill-network-routing)

> Dijkstra/A* multi-constraint path planning with time/distance weights and multiple origins and destinations

---

## 1. Overview

Network path planning: supports Dijkstra and A* (admissible heuristic; the scaling factor is automatically derived from the actual edge weights to guarantee optimality), multi-constraint paths weighted by distance or time, and batch planning of multiple origin-destination pairs.

## 2. Features

Network path planning: supports Dijkstra and A* (admissible heuristic; the scaling factor is automatically derived from the actual edge weights to guarantee optimality), multi-constraint paths weighted by distance or time, and batch planning of multiple origin-destination pairs.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-network-routing.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `routes.geojson` | GeoTIFF/GeoJSON/JSON | Primary output |
| `routing_stats.json` | GeoTIFF/GeoJSON/JSON | Primary output |
| `output-manifest.json` | JSON | Run manifest |


## 6. Technical Principle

- Dijkstra shortest path
- A* (admissible heuristic)
- Distance/time multi-constraint + multi-OD

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 网络路径规划（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-network-routing
description: 'Dijkstra/A*多约束路径规划，支持时间/距离权重和多起终点'
---

# 网络路径规划 | Network Routing

网络路径规划：支持 Dijkstra 与 A*（可采纳启发式，缩放系数由实际边权自动推导以保证最优性），按距离或时间加权的多约束路径，多起终点批量规划。

## 核心算法

- Dijkstra 最短路径
- A*（可采纳启发式）
- 距离/时间多约束 + 多 OD

## 依赖

```bash
pip install numpy rasterio scipy geopandas shapely
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-network-routing.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（指定区域 + 静默）

```bash
python geoskill-network-routing.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### 示例 3（真实输入）

```bash
python geoskill-network-routing.py --input <你的数据文件> --output-dir ./out3
```

### 示例 4（极小区域边界测试）

```bash
python geoskill-network-routing.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `routes.geojson` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `routing_stats.json` | GeoTIFF/GeoJSON/JSON | 主产物 |
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
