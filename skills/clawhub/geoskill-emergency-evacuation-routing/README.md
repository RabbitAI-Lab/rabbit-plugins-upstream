# Emergency Evacuation Routing (geoskill-emergency-evacuation-routing)

> Multi-origin evacuation planning combining shortest paths with hazard blockage and capacity constraints

---

## 1. Overview

Evacuation routes are planned on a raster cost surface with 8-neighbor Dijkstra shortest paths (diagonal cost √2): hazardous pixels are set impassable, so paths automatically detour and never cross blocked zones; multiple evacuation origins are assigned to shelters nearest-first, and once a shelter is full no further origins are assigned to it. On an unobstructed uniform grid, the shortest-path cost equals the Euclidean distance.

## 2. Features

Evacuation routes are planned on a raster cost surface with 8-neighbor Dijkstra shortest paths (diagonal cost √2): hazardous pixels are set impassable, so paths automatically detour and never cross blocked zones; multiple evacuation origins are assigned to shelters nearest-first, and once a shelter is full no further origins are assigned to it. On an unobstructed uniform grid, the shortest-path cost equals the Euclidean distance.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-emergency-evacuation-routing.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `distance_to_shelter.tif` | GeoTIFF | Distance field to the nearest shelter |
| `evacuation_routes.geojson` | GeoJSON | Evacuation routes (one LineString per origin) |
| `routing_stats.json` | JSON | Number of assignments / whether hazards were avoided / per-route cost |

Each run also produces `output-manifest.json` (run manifest with inputs/outputs/QA summary).

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

# 应急疏散路径规划（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-emergency-evacuation-routing
description: '最短路径叠加灾害阻断与容量约束的多起点疏散规划'
---

# 应急疏散路径规划 | Emergency Evacuation Routing

在栅格成本面上用 8 邻域 Dijkstra 最短路径规划疏散路线（对角代价 √2）：危险像元设为不可通行，路径自动绕行且绝不穿过阻断区；多个疏散起点按就近优先分配到避难所，避难所容量满后后续起点不再分配。无障碍均匀网格的最短路径代价等于欧氏距离。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-emergency-evacuation-routing.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 更多示例

```bash
python geoskill-emergency-evacuation-routing.py --bbox 116 39 117 40 --synthetic --output-dir ./out
python geoskill-emergency-evacuation-routing.py --input cost.tif --threshold 1.0 --output-dir ./out
python geoskill-emergency-evacuation-routing.py --bbox 116 39 117 40 --threshold 0.5 --capacity 2 --synthetic --output-dir ./out
python geoskill-emergency-evacuation-routing.py --bbox 117 39 118 40 --synthetic --quiet --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `distance_to_shelter.tif` | GeoTIFF | 到最近避难所的距离场 |
| `evacuation_routes.geojson` | GeoJSON | 疏散路线（每个起点一条 LineString） |
| `routing_stats.json` | JSON | 分配数/是否避开危险/各路线代价 |

每次运行还会产出 `output-manifest.json`（运行清单，含输入/产物/QA 摘要）。

## 数据源 / Source

真实模式读取多波段 GeoTIFF（band1=通行成本、band2=危险强度→阻断）；合成模式离线生成含障碍物的场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
