# Building Density Mapping (geoskill-building-density-mapping)

> Estimate building footprint density and floor area ratio (FAR) from building footprints and heights using kernel density estimation.

---

## 1. Overview

Estimates building density (building coverage ratio) and floor area ratio (FAR) from building footprint rasters, for urban morphology analysis, development intensity assessment and planning management. Core algorithm: taking the binary building footprint raster as input, a local mean convolution with a square kernel produces a continuous density field in [0,1]; the floor area ratio is then computed as FAR = building density × (building height / standard floor height). The density kernel is conservative: density is 1 in pure built-up areas and 0 in pure open ground, and FAR satisfies an analytical relationship with height/floor height.

## 2. Features

Estimates building density (building coverage ratio) and floor area ratio (FAR) from building footprint rasters, for urban morphology analysis, development intensity assessment and planning management. Core algorithm: taking the binary building footprint raster as input, a local mean convolution with a square kernel produces a continuous density field in [0,1]; the floor area ratio is then computed as FAR = building density × (building height / standard floor height). The density kernel is conservative: density is 1 in pure built-up areas and 0 in pure open ground, and FAR satisfies an analytical relationship with height/floor height.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-building-density-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `building_density.tif` | GeoTIFF | Two bands: band1 = building density, band2 = floor area ratio (FAR) |
| `density_stats.json` | JSON | Density/FAR statistics (mean, maximum, floor height) |
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

# 建筑密度制图（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-building-density-mapping
description: 'Estimate building footprint density and floor area ratio (FAR) from building footprints and heights using kernel density estimation.'
---

# 建筑密度制图 | Building Density Mapping

从建筑足迹栅格估计建筑密度（建筑覆盖率）与容积率（FAR），用于城市形态分析、开发强度评估与规划管理。

核心算法：以建筑足迹二值栅格为输入，用方形核做局部均值卷积得到连续的密度场 [0,1]；再由 FAR = 建筑密度 × (建筑高度 / 标准层高) 计算容积率。密度核守恒、纯建筑区密度为 1、纯空地为 0，FAR 与高度/层高满足解析关系。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-building-density-mapping.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例

#### 示例 1（合成数据（离线））

```bash
python geoskill-building-density-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### 示例 2（用法 2）

```bash
python geoskill-building-density-mapping.py --input footprints.tif --heights heights.tif --output-dir ./out
```

#### 示例 3（用法 3）

```bash
python geoskill-building-density-mapping.py --bbox 121.0 31.0 122.0 32.0 --kernel-size 7 --output-dir ./out --quiet
```

#### 示例 4（用法 4）

```bash
python geoskill-building-density-mapping.py --input fp.tif --floor-height 3.5 --output-dir ./out
```

#### 示例 5（用法 5）

```bash
python geoskill-building-density-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --kernel-size 3 --output-dir ./out --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `building_density.tif` | GeoTIFF | 双波段：band1=建筑密度，band2=容积率 FAR |
| `density_stats.json` | JSON | 密度/FAR 统计（均值、最大值、层高） |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地建筑足迹 + 建筑高度 GeoTIFF；`--synthetic` 模式生成含随机建筑块的离线模拟场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
