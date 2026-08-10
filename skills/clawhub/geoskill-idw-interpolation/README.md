# Inverse Distance Weighting Interpolation (geoskill-idw-interpolation)

> Inverse Distance Weighting (IDW) spatial interpolation with adjustable power parameter and search radius; outputs an interpolated GeoTIFF raster

---

## 1. Overview

Inverse Distance Weighting (IDW) spatial interpolation: the value at a target point is the distance-weighted average of known point values in its neighborhood, with weights w = 1/d^p. Supports an adjustable power parameter p, search-radius limits, and nearest-neighbor search. Vectorized implementation; outputs an interpolated raster.

## 2. Features

Inverse Distance Weighting (IDW) spatial interpolation: the value at a target point is the distance-weighted average of known point values in its neighborhood, with weights w = 1/d^p. Supports an adjustable power parameter p, search-radius limits, and nearest-neighbor search. Vectorized implementation; outputs an interpolated raster.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-idw-interpolation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `idw_result.tif` | GeoTIFF/GeoJSON/JSON | Primary output |
| `output-manifest.json` | JSON | Run manifest |

## 6. Technical Principle

- IDW distance-weighted formula
- Power parameter and nearest-neighbor search
- Exact-hit handling

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 反距离权重插值（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-idw-interpolation
description: '反距离权重(IDW)空间插值，支持幂参数和搜索半径，输出插值栅格GeoTIFF'
---

# 反距离权重插值 | IDW Interpolation

反距离权重（IDW）空间插值：目标点值为其邻域已知点值的距离加权平均，权重 w=1/d^p。支持幂参数 p 调节、搜索半径限制与最近邻域搜索。向量化实现，输出插值栅格。

## 核心算法

- IDW 距离加权公式
- 幂参数与最近邻搜索
- 精确命中处理

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-idw-interpolation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（指定区域 + 静默）

```bash
python geoskill-idw-interpolation.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### 示例 3（真实输入）

```bash
python geoskill-idw-interpolation.py --input <你的数据文件> --output-dir ./out3
```

### 示例 4（极小区域边界测试）

```bash
python geoskill-idw-interpolation.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `idw_result.tif` | GeoTIFF/GeoJSON/JSON | 主产物 |
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
