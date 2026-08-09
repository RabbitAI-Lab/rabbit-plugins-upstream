# Urban Ventilation Corridor Analysis (geoskill-urban-ventilation-corridor)

> Derive aerodynamic roughness and ventilation potential from building morphology and extract least-resistance ventilation corridors.

---

## 1. Overview

Derives aerodynamic roughness and ventilation potential from building morphology and extracts least-resistance ventilation corridors to support urban ventilation planning and thermal environment mitigation. Core algorithm: roughness uses a simplified Macdonald empirical formula z0 = 0.1 × building height × plan area density; ventilation potential VP = exp(−k×z0), monotonically decreasing with roughness; on the resistance raster (1−VP+ε), an 8-neighborhood Dijkstra finds the least-resistance path from the upwind edge to the downwind edge as the ventilation corridor. Corridor geometry is built with shapely and exported as GeoJSON.

## 2. Features

Derives aerodynamic roughness and ventilation potential from building morphology and extracts least-resistance ventilation corridors to support urban ventilation planning and thermal environment mitigation. Core algorithm: roughness uses a simplified Macdonald empirical formula z0 = 0.1 × building height × plan area density; ventilation potential VP = exp(−k×z0), monotonically decreasing with roughness; on the resistance raster (1−VP+ε), an 8-neighborhood Dijkstra finds the least-resistance path from the upwind edge to the downwind edge as the ventilation corridor. Corridor geometry is built with shapely and exported as GeoJSON.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-urban-ventilation-corridor.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `ventilation.tif` | GeoTIFF | Two bands: band1 = roughness z0, band2 = ventilation potential VP |
| `corridor.geojson` | GeoJSON | Least-resistance ventilation corridor (LineString, built with shapely) |
| `ventilation_stats.json` | JSON | Mean roughness, mean ventilation potential, corridor cost/vertex count |
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

# 城市通风廊道分析（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-urban-ventilation-corridor
description: 'Derive aerodynamic roughness and ventilation potential from building morphology and extract least-resistance ventilation corridors.'
---

# 城市通风廊道分析 | Urban Ventilation Corridor Analysis

从建筑形态推导空气动力学粗糙度与通风潜力，并提取最小阻力通风廊道，服务于城市通风规划与热环境缓解。

核心算法：粗糙度采用 Macdonald 经验式简化 z0 = 0.1×建筑高度×平面面积密度；通风潜力 VP = exp(−k×z0)，随粗糙度单调递减；在阻力栅格（1−VP+ε）上用 8 邻域 Dijkstra 求上风缘到下风缘的最小阻力路径作为通风廊道。廊道几何用 shapely 构建并输出 GeoJSON。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'shapely'
```

## 使用方法

### 基本用法

```bash
python geoskill-urban-ventilation-corridor.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例

#### 示例 1（合成数据（离线））

```bash
python geoskill-urban-ventilation-corridor.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### 示例 2（用法 2）

```bash
python geoskill-urban-ventilation-corridor.py --input height.tif --footprints fp.tif --output-dir ./out
```

#### 示例 3（用法 3）

```bash
python geoskill-urban-ventilation-corridor.py --bbox 121.0 31.0 122.0 32.0 --decay-k 0.8 --output-dir ./out --quiet
```

#### 示例 4（用法 4）

```bash
python geoskill-urban-ventilation-corridor.py --input height.tif --roughness-coeff 0.15 --output-dir ./out
```

#### 示例 5（用法 5）

```bash
python geoskill-urban-ventilation-corridor.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `ventilation.tif` | GeoTIFF | 双波段：band1=粗糙度 z0，band2=通风潜力 VP |
| `corridor.geojson` | GeoJSON | 最小阻力通风廊道（LineString，shapely 构建） |
| `ventilation_stats.json` | JSON | 平均粗糙度、平均通风潜力、廊道代价/顶点数 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地建筑高度 + 平面面积密度 GeoTIFF；`--synthetic` 模式生成含低矮通风绿带的城区场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
