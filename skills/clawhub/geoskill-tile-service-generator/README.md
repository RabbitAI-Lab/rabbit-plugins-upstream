# Tile Service Generator (geoskill-tile-service-generator)

> Slices a raster into multi-zoom XYZ Web Mercator PNG tiles with tile metadata.

---

## 1. Overview

Slices a raster into a standard XYZ tile service; the output directory `{z}/{x}/{y}.png` can be loaded directly by Leaflet / OpenLayers / MapLibre: - **XYZ tiling math**: conversions between lon/lat ↔ tile coordinates ↔ Web Mercator metric bounds, including Bing-style quadkey encoding (z=3, x=3, y=5 → "213"). - **Pure-Python PNG encoding**: writes 8-bit grayscale PNG using only zlib + struct (with IHDR/IDAT/IEND chunks and CRC), no PIL/GDAL dependency, fully offline. - **Per-tile resampling**: back-projects each tile's pixel center to lon/lat and takes a nearest-neighbor sample from the source raster; no-data areas are left as background. Generates multiple zoom levels according to `--min-zoom`/`--max-zoom`, and the tiles.json metadata records the coordinates and quadkey of every tile. The `--synthetic` mode generates a 64×64 gradient raster.

## 2. Features

Slices a raster into a standard XYZ tile service; the output directory `{z}/{x}/{y}.png` can be loaded directly by Leaflet / OpenLayers / MapLibre: - **XYZ tiling math**: conversions between lon/lat ↔ tile coordinates ↔ Web Mercator metric bounds, including Bing-style quadkey encoding (z=3, x=3, y=5 → "213"). - **Pure-Python PNG encoding**: writes 8-bit grayscale PNG using only zlib + struct (with IHDR/IDAT/IEND chunks and CRC), no PIL/GDAL dependency, fully offline. - **Per-tile resampling**: back-projects each tile's pixel center to lon/lat and takes a nearest-neighbor sample from the source raster; no-data areas are left as background. Generates multiple zoom levels according to `--min-zoom`/`--max-zoom`, and the tiles.json metadata records the coordinates and quadkey of every tile. The `--synthetic` mode generates a 64×64 gradient raster.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-tile-service-generator.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `tiles/{z}/{x}/{y}.png` | PNG (8-bit grayscale) | XYZ tiles |
| `tiles.json` | JSON | Per-zoom-level tile inventory (with quadkey) |
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

# 瓦片服务生成（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-tile-service-generator
description: '将栅格按 Web Mercator XYZ 切片方案切分为多缩放级别 PNG 瓦片并生成元数据。Slice a raster into multi-zoom XYZ Web Mercator PNG tiles with tile metadata.'
---

# 瓦片服务生成 | Tile Service Generator

把栅格切分为标准 XYZ 瓦片服务，产物目录 `{z}/{x}/{y}.png` 可直接被
Leaflet / OpenLayers / MapLibre 加载：

- **XYZ 切片数学**：经纬度 ↔ 瓦片坐标 ↔ Web Mercator 米制边界的互转，
  含 Bing 风格 quadkey 编码（z=3,x=3,y=5 → "213"）。
- **纯 Python PNG 编码**：仅用 zlib + struct 写 8-bit 灰度 PNG（含 IHDR/
  IDAT/IEND chunk 与 CRC），不依赖 PIL/GDAL，完全离线。
- **逐瓦片重采样**：把瓦片像元中心反投影回经纬度，再从源栅格最近邻取样，
  无数据区域留作背景。

按 `--min-zoom`/`--max-zoom` 生成多缩放级别，元数据 tiles.json 记录每块
瓦片坐标与 quadkey。`--synthetic` 模式生成 64×64 渐变栅格。

## 依赖

```bash
pip install numpy rasterio geopandas shapely fiona pyproj
```

## 使用方法

### 基本用法

```bash
python geoskill-tile-service-generator.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 1（合成数据，z6-z8，离线）

```bash
python geoskill-tile-service-generator.py --bbox 116.0 39.0 117.0 40.0 --synthetic --min-zoom 6 --max-zoom 8 --output-dir ./tiles
```

### 示例 2：为 DEM 生成 z8-z11 瓦片

```bash
python geoskill-tile-service-generator.py --input dem.tif --min-zoom 8 --max-zoom 11 --output-dir ./dem_tiles
```

### 示例 3：小尺寸瓦片（128px）

```bash
python geoskill-tile-service-generator.py --input ortho.tif --tile-size 128 --min-zoom 10 --max-zoom 12 --output-dir ./t128
```

### 示例 4：单缩放级别快速预览

```bash
python geoskill-tile-service-generator.py --bbox 121.0 31.0 122.0 32.0 --synthetic --min-zoom 7 --max-zoom 7 --output-dir ./z7 --quiet
```

### 示例 5：自定义合成栅格尺寸

```bash
python geoskill-tile-service-generator.py --bbox 116.0 39.0 117.0 40.0 --synthetic --size 128 --max-zoom 9 --output-dir ./hi
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `tiles/{z}/{x}/{y}.png` | PNG (8-bit 灰度) | XYZ 瓦片 |
| `tiles.json` | JSON | 各缩放级别瓦片清单（含 quadkey） |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- `--input`：本地 GeoTIFF
- `--synthetic`：本地生成渐变栅格

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
