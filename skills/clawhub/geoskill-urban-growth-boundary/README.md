# Urban Growth Boundary (geoskill-urban-growth-boundary)

> Delineate urban growth boundaries from historical expansion rate and direction plus terrain, cropland and ecological constraints.

---

## 1. Overview

Delineates urban growth boundaries (UGB) from historical expansion and multi-source constraints to support territorial spatial planning and growth management. Core algorithm: relative annual expansion rate = (A2−A1)/A1/years; the expansion trend is characterized by the smoothed difference of built-up areas between two periods; the constraint penalty = weighted sum of slope / cropland / ecology ∈ [0,1]; growth suitability = trend × (1−penalty) ∈ [0,1], tending to 0 on steep slopes and ecologically sensitive areas; the outer edge of contiguous regions above the suitability threshold defines the growth boundary.

## 2. Features

Delineates urban growth boundaries (UGB) from historical expansion and multi-source constraints to support territorial spatial planning and growth management. Core algorithm: relative annual expansion rate = (A2−A1)/A1/years; the expansion trend is characterized by the smoothed difference of built-up areas between two periods; the constraint penalty = weighted sum of slope / cropland / ecology ∈ [0,1]; growth suitability = trend × (1−penalty) ∈ [0,1], tending to 0 on steep slopes and ecologically sensitive areas; the outer edge of contiguous regions above the suitability threshold defines the growth boundary.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-urban-growth-boundary.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `growth_suitability.tif` | GeoTIFF | Two bands: band1 = growth suitability, band2 = boundary mask |
| `growth_stats.json` | JSON | Two-period area, expansion rate, mean suitability, boundary ratio |
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

# 城市增长边界（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-urban-growth-boundary
description: 'Delineate urban growth boundaries from historical expansion rate and direction plus terrain, cropland and ecological constraints.'
---

# 城市增长边界 | Urban Growth Boundary

从历史扩张与多源约束划定城市增长边界（UGB），服务于国土空间规划与增长管理。

核心算法：相对年均扩张速率 = (A2−A1)/A1/年数；扩张趋势由两期建成区差值平滑表征；约束惩罚 = 坡度/耕地/生态加权和 ∈ [0,1]；增长适宜性 = 趋势×(1−惩罚) ∈ [0,1]，陡坡+生态敏感区趋于 0；适宜性高于阈值的连片区域外缘即增长边界。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-urban-growth-boundary.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例

#### 示例 1（合成数据（离线））

```bash
python geoskill-urban-growth-boundary.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### 示例 2（用法 2）

```bash
python geoskill-urban-growth-boundary.py --input built_t2.tif --built-t1 built_t1.tif --years 10 --output-dir ./out
```

#### 示例 3（用法 3）

```bash
python geoskill-urban-growth-boundary.py --bbox 121.0 31.0 122.0 32.0 --threshold 0.4 --output-dir ./out --quiet
```

#### 示例 4（用法 4）

```bash
python geoskill-urban-growth-boundary.py --input built_t2.tif --built-t1 built_t1.tif --years 5 --output-dir ./out
```

#### 示例 5（用法 5）

```bash
python geoskill-urban-growth-boundary.py --bbox 116.0 39.0 117.0 40.0 --synthetic --threshold 0.25 --output-dir ./out --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `growth_suitability.tif` | GeoTIFF | 双波段：band1=增长适宜性，band2=边界掩膜 |
| `growth_stats.json` | JSON | 两期面积、扩张速率、平均适宜性、边界比例 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地双期建成区 GeoTIFF（+ 约束栅格）；`--synthetic` 模式模拟向东扩张 + 北陡坡/南耕地/西生态约束的场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
