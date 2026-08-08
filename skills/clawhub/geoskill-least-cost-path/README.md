# Least Cost Path (geoskill-least-cost-path)

> Cost distance computation + Dijkstra back-links + path extraction, outputting the least-cost path

---

## 1. Overview

Based on a cost raster, Dijkstra computes the minimum accumulated cost distance and back-links from the source point to the whole grid (8-neighborhood, diagonal weighted by √2); the least-cost path is then traced back from the target point. Outputs a cost distance raster and a path GeoJSON.

## 2. Features

Based on a cost raster, Dijkstra computes the minimum accumulated cost distance and back-links from the source point to the whole grid (8-neighborhood, diagonal weighted by √2); the least-cost path is then traced back from the target point. Outputs a cost distance raster and a path GeoJSON.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-least-cost-path.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `cost_distance.tif` | GeoTIFF/GeoJSON/JSON | Primary output |
| `least_cost_path.geojson` | GeoTIFF/GeoJSON/JSON | Primary output |
| `output-manifest.json` | JSON | Run manifest |

## 6. Technical Principle

- Dijkstra cost distance
- Back-links (backlink)
- Path extraction and cost accounting

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 最小成本路径（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-least-cost-path
description: '成本距离计算+Dijkstra回溯链接+路径提取，输出最小成本路径'
---

# 最小成本路径 | Least Cost Path

基于成本栅格用 Dijkstra 计算从源点到全图的最小累积成本距离与回溯链接（8 邻域，对角线 √2 加权），再从目标点回溯提取最小成本路径。输出成本距离栅格与路径 GeoJSON。

## 核心算法

- Dijkstra 成本距离
- 回溯链接（backlink）
- 路径提取与成本核算

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-least-cost-path.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（指定区域 + 静默）

```bash
python geoskill-least-cost-path.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### 示例 3（真实输入）

```bash
python geoskill-least-cost-path.py --input <你的数据文件> --output-dir ./out3
```

### 示例 4（极小区域边界测试）

```bash
python geoskill-least-cost-path.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `cost_distance.tif` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `least_cost_path.geojson` | GeoTIFF/GeoJSON/JSON | 主产物 |
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
