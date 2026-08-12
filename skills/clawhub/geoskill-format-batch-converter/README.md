# Batch Format Converter (geoskill-format-batch-converter)

> Batch convert raster and vector formats (GeoTIFF / Shapefile / GeoPackage / GeoJSON) via GDAL / OGR with logging.

---

## 1. Overview

Batch converts raster and vector formats using GDAL/OGR (via rasterio / fiona / geopandas): - **Raster**: conversion between GeoTIFFs and recompression (rasterio + DEFLATE). - **Vector**: conversion between GeoJSON / Shapefile / GeoPackage (read with geopandas, then written out via the target OGR driver). `--input` may point to a single file or a directory (`--recursive` for recursive subdirectories); the type is auto-detected by extension, with rasters converted to `--raster-target` and vectors to `--vector-target`. Each conversion records a structured log (source, target, status, byte count); unsupported extensions are logged as skipped and parse failures as error, neither interrupting the batch. `--synthetic` mode generates a small source set locally (a GeoTIFF + GeoJSON points + Shapefile polygons) to demonstrate the full batch conversion offline.

## 2. Features

Batch converts raster and vector formats using GDAL/OGR (via rasterio / fiona / geopandas): - **Raster**: conversion between GeoTIFFs and recompression (rasterio + DEFLATE). - **Vector**: conversion between GeoJSON / Shapefile / GeoPackage (read with geopandas, then written out via the target OGR driver). `--input` may point to a single file or a directory (`--recursive` for recursive subdirectories); the type is auto-detected by extension, with rasters converted to `--raster-target` and vectors to `--vector-target`. Each conversion records a structured log (source, target, status, byte count); unsupported extensions are logged as skipped and parse failures as error, neither interrupting the batch. `--synthetic` mode generates a small source set locally (a GeoTIFF + GeoJSON points + Shapefile polygons) to demonstrate the full batch conversion offline.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-format-batch-converter.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `converted/*` | Target format | Converted files |
| `conversion_log.json` | JSON | Per-file conversion log + summary |
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

# 格式批量转换（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-format-batch-converter
description: '基于 GDAL / OGR 批量转换栅格与矢量格式 (GeoTIFF / Shapefile / GeoPackage / GeoJSON) 并记录日志。Batch convert raster and vector formats (GeoTIFF / Shapefile / GeoPackage / GeoJSON) via GDAL / OGR with logging.'
---

# 格式批量转换 | Format Batch Converter

用 GDAL/OGR（经 rasterio / fiona / geopandas）批量转换栅格与矢量格式：

- **栅格**：GeoTIFF 之间互转/重压缩（rasterio + DEFLATE）。
- **矢量**：GeoJSON / Shapefile / GeoPackage 互转（geopandas 读取后按
  目标 OGR 驱动写出）。

`--input` 可指向单个文件或目录（`--recursive` 递归子目录）；按扩展名
自动识别类型，栅格转到 `--raster-target`、矢量转到 `--vector-target`。
每次转换记录结构化日志（来源、目标、状态、字节数），不支持的扩展名
记为 skipped、解析失败记为 error，均不中断批处理。

`--synthetic` 模式在本地生成一个小 GeoTIFF + GeoJSON 点 + Shapefile 面
源集，离线演示完整批量转换。

## 依赖

```bash
pip install numpy rasterio geopandas shapely fiona pyproj
```

## 使用方法

### 基本用法

```bash
python geoskill-format-batch-converter.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 1（合成数据，全部转 GeoPackage，离线）

```bash
python geoskill-format-batch-converter.py --bbox 116.0 39.0 117.0 40.0 --synthetic --vector-target gpkg --output-dir ./gpkg
```

### 示例 2：把目录里所有矢量转 GeoJSON（递归）

```bash
python geoskill-format-batch-converter.py --input ./raw_data --vector-target geojson --recursive --output-dir ./geojson_all
```

### 示例 3：Shapefile 批量转 GeoPackage

```bash
python geoskill-format-batch-converter.py --input ./shapefiles --vector-target gpkg --output-dir ./gpkg_batch
```

### 示例 4：单文件转换

```bash
python geoskill-format-batch-converter.py --input scene.tif --output-dir ./recompressed
```

### 示例 5：合成 + 转 Shapefile

```bash
python geoskill-format-batch-converter.py --bbox 121.0 31.0 122.0 32.0 --synthetic --vector-target shp --output-dir ./shp_out --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `converted/*` | 目标格式 | 转换后的文件 |
| `conversion_log.json` | JSON | 逐文件转换日志 + 汇总 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- `--input`：本地文件或目录
- `--synthetic`：本地生成混合源集

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
