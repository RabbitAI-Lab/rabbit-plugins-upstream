# Raster Resampling (geoskill-raster-resampling)

> Resample raster resolution with nearest-neighbor / bilinear / cubic convolution and output a resampled GeoTIFF plus statistics. Resample raster resolution with nearest / bilinear / cubic convolution and emit a GeoTIFF plus statistics.

---

## 1. Overview

Resample raster resolution (pixel density) with three classic resampling methods implemented in pure numpy, keeping the geographic extent unchanged: - **nearest**: takes the value of the nearest input pixel, preserves the original value set, and suits categorical/thematic rasters. - **bilinear**: 2×2 neighborhood distance weighting, exactly reconstructs pixels inside linear fields, and suits continuous data (DEM, temperature fields). - **cubic**: 4×4 convolution with the Keys (1981) kernel (a=-0.5), sharper edges. The core is implemented via an "output pixel center → input continuous coordinate" mapping that supports arbitrary scale factors; nodata pixels are filled with the local neighborhood mean during interpolation to avoid contamination. The `--synthetic` mode generates a 64×64 test raster with a linear slope on the left half and a categorical block on the right half.

## 2. Features

Resample raster resolution (pixel density) with three classic resampling methods implemented in pure numpy, keeping the geographic extent unchanged: - **nearest**: takes the value of the nearest input pixel, preserves the original value set, and suits categorical/thematic rasters. - **bilinear**: 2×2 neighborhood distance weighting, exactly reconstructs pixels inside linear fields, and suits continuous data (DEM, temperature fields). - **cubic**: 4×4 convolution with the Keys (1981) kernel (a=-0.5), sharper edges. The core is implemented via an "output pixel center → input continuous coordinate" mapping that supports arbitrary scale factors; nodata pixels are filled with the local neighborhood mean during interpolation to avoid contamination. The `--synthetic` mode generates a 64×64 test raster with a linear slope on the left half and a categorical block on the right half.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-raster-resampling.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `resampled.tif` | GeoTIFF (float32) | Resampled result, EPSG:4326 |
| `output-manifest.json` | JSON | Run manifest (includes input/output shapes and value ranges) |

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

# 栅格重采样（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-raster-resampling
description: '用最近邻 / 双线性 / 三次卷积改变栅格分辨率，输出重采样后的 GeoTIFF 与统计。Resample raster resolution with nearest / bilinear / cubic convolution and emit a GeoTIFF plus statistics.'
---

# 栅格重采样 | Raster Resampling

用纯 numpy 实现三种经典重采样方法改变栅格分辨率（像元密度），地理范围
保持不变：

- **nearest**（最近邻）：取最近输入像元值，保持原始取值集合，适合分类/
  专题栅格。
- **bilinear**（双线性）：2×2 邻域距离加权，对线性场内部像元精确重构，
  适合连续数据（DEM、温度场）。
- **cubic**（三次卷积）：Keys 1981 核（a=-0.5）的 4×4 卷积，边缘更锐利。

核心按“输出像元中心 → 输入连续坐标”映射实现，支持任意缩放因子；nodata
像元在插值时用邻域均值填充以避免污染。`--synthetic` 模式生成左半线性
坡面、右半分类块的 64×64 测试栅格。

## 依赖

```bash
pip install numpy rasterio geopandas shapely fiona pyproj
```

## 使用方法

### 基本用法

```bash
python geoskill-raster-resampling.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 1（合成数据，双线性降采样到一半，离线）

```bash
python geoskill-raster-resampling.py --bbox 116.0 39.0 117.0 40.0 --synthetic --method bilinear --scale 0.5 --output-dir ./half
```

### 示例 2：最近邻 2 倍上采样（保分类值）

```bash
python geoskill-raster-resampling.py --input landcover.tif --method nearest --scale 2.0 --output-dir ./up2
```

### 示例 3：三次卷积重采样 DEM

```bash
python geoskill-raster-resampling.py --input dem.tif --method cubic --scale 0.25 --output-dir ./dem_quarter
```

### 示例 4：合成栅格最近邻降采样

```bash
python geoskill-raster-resampling.py --bbox 121.0 31.0 122.0 32.0 --synthetic --method nearest --scale 0.5 --output-dir ./nn --quiet
```

### 示例 5：自定义合成尺寸

```bash
python geoskill-raster-resampling.py --bbox 116.0 39.0 117.0 40.0 --synthetic --size 128 --method bilinear --scale 0.5 --output-dir ./big
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `resampled.tif` | GeoTIFF (float32) | 重采样结果，EPSG:4326 |
| `output-manifest.json` | JSON | 运行清单（含输入/输出形状与值域） |

## 数据源 / Source

- `--input`：本地 GeoTIFF
- `--synthetic`：本地生成测试栅格

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
