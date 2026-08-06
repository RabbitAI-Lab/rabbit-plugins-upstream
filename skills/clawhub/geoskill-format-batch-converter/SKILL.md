---
name: geoskill-format-batch-converter
description: '基于 GDAL / OGR 批量转换栅格与矢量格式 (GeoTIFF / Shapefile / GeoPackage / GeoJSON) 并记录日志。Batch convert raster and vector formats (GeoTIFF / Shapefile / GeoPackage / GeoJSON) via GDAL / OGR with logging.'
---

# 格式批量转换 | Format Batch Converter

Batch-converts raster and vector formats with GDAL/OGR (via rasterio / fiona / geopandas):

- **Raster**: GeoTIFF-to-GeoTIFF conversion/recompression (rasterio + DEFLATE).
- **Vector**: GeoJSON / Shapefile / GeoPackage interconversion (read with geopandas, then written through the target OGR driver).

`--input` may point to a single file or a directory (`--recursive` scans subdirectories); the type is auto-detected by extension, with rasters converted to `--raster-target` and vectors to `--vector-target`. Every conversion writes a structured log entry (source, target, status, byte count); unsupported extensions are logged as skipped and parse failures as error, neither of which interrupts the batch run.

`--synthetic` mode generates a small local source set — a GeoTIFF + GeoJSON points + Shapefile polygons — to demonstrate the full batch conversion offline.

## Dependencies / 依赖

```bash
pip install numpy rasterio geopandas shapely fiona pyproj
```

## Usage / 使用方法

### Basic usage

```bash
python geoskill-format-batch-converter.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 1 (synthetic data, convert everything to GeoPackage, offline)

```bash
python geoskill-format-batch-converter.py --bbox 116.0 39.0 117.0 40.0 --synthetic --vector-target gpkg --output-dir ./gpkg
```

### Example 2: convert all vectors in a directory to GeoJSON (recursive)

```bash
python geoskill-format-batch-converter.py --input ./raw_data --vector-target geojson --recursive --output-dir ./geojson_all
```

### Example 3: batch-convert Shapefiles to GeoPackage

```bash
python geoskill-format-batch-converter.py --input ./shapefiles --vector-target gpkg --output-dir ./gpkg_batch
```

### Example 4: single-file conversion

```bash
python geoskill-format-batch-converter.py --input scene.tif --output-dir ./recompressed
```

### Example 5: synthetic + convert to Shapefile

```bash
python geoskill-format-batch-converter.py --bbox 121.0 31.0 122.0 32.0 --synthetic --vector-target shp --output-dir ./shp_out --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `converted/*` | Target format | Converted files |
| `conversion_log.json` | JSON | Per-file conversion log + summary |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- `--input`: local files or a directory
- `--synthetic`: locally generated mixed source set

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is performed locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
