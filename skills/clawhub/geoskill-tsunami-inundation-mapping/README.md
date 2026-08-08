# Tsunami Inundation Mapping (geoskill-tsunami-inundation-mapping)

> Bathtub hydrological connectivity inundation modeling, outputting water depth, arrival time and evacuation zones

---

## 1. Overview

DEM-based bathtub inundation modeling with hydrological connectivity constraints — only depressions that are 8-connected to a coastal seed zone are inundated; isolated inland basins remain dry even when their elevation is below the water level. Outputs include the inundation extent, water depth (water level − elevation, always non-negative), arrival time from the coast (Euclidean distance × pixel size / wave speed), and critical evacuation zones (dry land not inundated but below the safe margin). Both the inundated area and water depth are monotonically non-decreasing with water level.

## 2. Features

DEM-based bathtub inundation modeling with hydrological connectivity constraints — only depressions that are 8-connected to a coastal seed zone are inundated; isolated inland basins remain dry even when their elevation is below the water level. Outputs include the inundation extent, water depth (water level − elevation, always non-negative), arrival time from the coast (Euclidean distance × pixel size / wave speed), and critical evacuation zones (dry land not inundated but below the safe margin). Both the inundated area and water depth are monotonically non-decreasing with water level.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-tsunami-inundation-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `inundation.tif` | GeoTIFF | Inundation extent mask |
| `water_depth.tif` | GeoTIFF | Water depth (m, ≥0) |
| `arrival_time.tif` | GeoTIFF | Tsunami arrival time (s) |
| `evacuation_zone.tif` | GeoTIFF | Recommended evacuation zone (mutually exclusive with the inundated area) |
| `tsunami_params.json` | JSON | Parameters such as water level / wave speed / pixel size |

Each run also produces `output-manifest.json` (run manifest containing inputs / outputs / QA summary).

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

# 海啸淹没制图（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-tsunami-inundation-mapping
description: 'Bathtub水文连通淹没建模,输出水深、到达时间与撤离区'
---

# 海啸淹没制图 | Tsunami Inundation Mapping

基于 DEM 的 bathtub 淹没建模，并加入水文连通约束——只有与海岸种子区 8-连通的洼地才会被淹，孤立内陆盆地即使高程低于水位也不淹没。输出淹没范围、水深（水位-高程，恒非负）、到海岸的到达时间（欧氏距离×像元尺寸/波速）以及临界撤离区（未淹但低于安全余量的干地）。淹没面积与水深均随水位单调不减。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-tsunami-inundation-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 更多示例

```bash
python geoskill-tsunami-inundation-mapping.py --bbox 120 30 121 31 --synthetic --output-dir ./out
python geoskill-tsunami-inundation-mapping.py --input dem.tif --water-level 15 --output-dir ./out
python geoskill-tsunami-inundation-mapping.py --bbox 120 30 121 31 --water-level 20 --wave-speed 8 --synthetic --output-dir ./out
python geoskill-tsunami-inundation-mapping.py --bbox 121 31 122 32 --synthetic --quiet --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `inundation.tif` | GeoTIFF | 淹没范围掩膜 |
| `water_depth.tif` | GeoTIFF | 淹没水深（m，≥0） |
| `arrival_time.tif` | GeoTIFF | 海啸到达时间（s） |
| `evacuation_zone.tif` | GeoTIFF | 建议撤离区（与淹没区互斥） |
| `tsunami_params.json` | JSON | 水位/波速/像元尺寸等参数 |

每次运行还会产出 `output-manifest.json`（运行清单，含输入/产物/QA 摘要）。

## 数据源 / Source

真实模式读取单波段 DEM GeoTIFF（单位 m）；合成模式离线生成海岸地形（含山脊与孤立洼地）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
