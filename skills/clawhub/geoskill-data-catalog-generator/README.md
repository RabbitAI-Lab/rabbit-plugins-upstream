# Data Catalog Generator (geoskill-data-catalog-generator)

> Scan raster and vector files in a directory, extract and classify metadata, and generate a browsable HTML / CSV data catalog.

---

## 1. Overview

Scan geographic data files in a directory, extract and classify metadata, and generate a browsable data catalog: - **Scanning**: Recursively or non-recursively traverse the directory and identify raster (.tif) and vector (.geojson/.shp/.gpkg) files by extension, automatically skipping Shapefile auxiliary files (.shx/.dbf/.prj). - **Metadata extraction**: For rasters, read dimensions, band count, CRS, extent, resolution, and dtype (rasterio); for vectors, read feature count, geometry type, CRS, extent, and attribute fields (geopandas). Files that cannot be parsed are recorded as error without interrupting the overall workflow. - **Classification**: Break down by type (single-band / multispectral / hyperspectral raster; point / line / polygon / mixed vector) and CRS family (WGS 84 / Web Mercator / UTM projection / unknown). - **Catalog output**: catalog.csv (one row per file), catalog.html (styled table with summary cards), catalog.json (machine-readable full record). Suitable for data asset inventory, project data listing, and data sharing pages. The `--synthetic` mode generates a mixed source set of tif×2 + geojson + shp + gpkg.

## 2. Features

Scan geographic data files in a directory, extract and classify metadata, and generate a browsable data catalog: - **Scanning**: Recursively or non-recursively traverse the directory and identify raster (.tif) and vector (.geojson/.shp/.gpkg) files by extension, automatically skipping Shapefile auxiliary files (.shx/.dbf/.prj). - **Metadata extraction**: For rasters, read dimensions, band count, CRS, extent, resolution, and dtype (rasterio); for vectors, read feature count, geometry type, CRS, extent, and attribute fields (geopandas). Files that cannot be parsed are recorded as error without interrupting the overall workflow. - **Classification**: Break down by type (single-band / multispectral / hyperspectral raster; point / line / polygon / mixed vector) and CRS family (WGS 84 / Web Mercator / UTM projection / unknown). - **Catalog output**: catalog.csv (one row per file), catalog.html (styled table with summary cards), catalog.json (machine-readable full record). Suitable for data asset inventory, project data listing, and data sharing pages. The `--synthetic` mode generates a mixed source set of tif×2 + geojson + shp + gpkg.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-data-catalog-generator.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `catalog.html` | HTML | Styled catalog table with summary cards |
| `catalog.csv` | CSV | One row of metadata per file |
| `catalog.json` | JSON | Machine-readable full metadata + summary |
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

# 数据目录生成器（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-data-catalog-generator
description: '扫描目录中的栅格与矢量文件，提取元数据并分类，生成可浏览的 HTML / CSV 数据目录。Scan raster and vector files in a directory, extract and classify metadata, and generate a browsable HTML / CSV data catalog.'
---

# 数据目录生成器 | Data Catalog Generator

扫描目录中的地理数据文件，提取元数据并分类，生成可浏览的数据目录：

- **扫描**：递归/非递归遍历目录，按扩展名识别栅格（.tif）与矢量
  （.geojson/.shp/.gpkg）文件，自动跳过 Shapefile 辅助文件（.shx/.dbf/
  .prj）。
- **元数据提取**：栅格读尺寸、波段数、CRS、范围、分辨率、dtype（rasterio）；
  矢量读要素数、几何类型、CRS、范围、属性字段（geopandas）。无法解析的
  文件记为 error 而不中断整体流程。
- **分类**：按类型细分（单波段/多光谱/高光谱栅格；点/线/面/混合矢量）
  与 CRS 家族（WGS 84 / Web Mercator / UTM 投影 / 未知）。
- **目录输出**：catalog.csv（每文件一行）、catalog.html（带汇总卡片的
  样式化表格）、catalog.json（机读全量）。

适合数据资产盘点、项目数据清单生成、数据共享页面。`--synthetic` 模式
生成 tif×2 + geojson + shp + gpkg 混合源集。

## 依赖

```bash
pip install numpy rasterio geopandas shapely fiona pyproj
```

## 使用方法

### 基本用法

```bash
python geoskill-data-catalog-generator.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 1（合成数据，离线）

```bash
python geoskill-data-catalog-generator.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./catalog
```

### 示例 2：递归扫描项目数据目录

```bash
python geoskill-data-catalog-generator.py --input ./project_data --recursive --output-dir ./inventory
```

### 示例 3：单层扫描（不递归）

```bash
python geoskill-data-catalog-generator.py --input ./delivery --output-dir ./delivery_catalog
```

### 示例 4：为共享目录生成目录页

```bash
python geoskill-data-catalog-generator.py --input /data/shared --recursive --output-dir ./shared_catalog --quiet
```

### 示例 5：合成 + 自定义栅格尺寸

```bash
python geoskill-data-catalog-generator.py --bbox 121.0 31.0 122.0 32.0 --synthetic --size 32 --output-dir ./cat2
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `catalog.html` | HTML | 带汇总卡片的样式化目录表 |
| `catalog.csv` | CSV | 每文件一行元数据 |
| `catalog.json` | JSON | 机读全量元数据 + 汇总 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- `--input`：本地文件或目录
- `--synthetic`：本地生成混合源集

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
