---
name: geoskill-map-print-composition
description: 'Compose multi-layer maps with cartographic decoration and high-resolution render to TIFF or PDF'
---

# 地图打印合成 | Map Print Composition

Print-oriented high-resolution map composition: the colored terrain layer and Horn hillshade are combined with **multiplicative blending** (shaded relief); arbitrary RGB layers can then be overlaid on top (alpha compositing), producing a georeferenced 3-band RGB GeoTIFF and a PDF.

Suitable for producing basemaps for publication-grade topographic maps, wall maps and atlases.

## Core Algorithm / 核心算法

dem_to_color(normalization+colormap) → horn_hillshade → hillshade_blend multiplicative blending (ambient+shade) → optional alpha_composite overlay → uint8 RGB GeoTIFF.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## Usage / 使用方法

### Example 1 (synthetic data, offline)

```bash
python geoskill-map-print-composition.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (high-dpi printing)

```bash
python geoskill-map-print-composition.py --input dem.tif --dpi 300
```

### Example 3 (overlay layer alpha)

```bash
python geoskill-map-print-composition.py --input dem.tif --overlay landcover.tif --overlay-alpha 0.5
```

### Example 4 (custom illumination)

```bash
python geoskill-map-print-composition.py --input dem.tif --azimuth 270 --altitude 40 --ambient 0.1
```

### Example 5 (synthetic shaded relief)

```bash
python geoskill-map-print-composition.py --bbox 116 39 117 40 --synthetic --zfactor 2
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `print_map.tif` | GeoTIFF | 3-band RGB print raster (main/verifiable deliverable) |
| `print_map.pdf` | PDF | Layout PDF |
| `print_meta.json` | JSON | Illumination/overlay/statistics |

Each run also produces `output-manifest.json` (run manifest).

## Data Source / 数据源 / Source

Local GeoTIFF / vector files; `--synthetic` mode generates physically consistent simulated data, fully offline.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is performed locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-map-print-composition
description: 'Compose multi-layer maps with cartographic decoration and high-resolution render to TIFF or PDF'
---

# 地图打印合成 | Map Print Composition

面向印刷的高分辨率地图合成：彩色地形层与 Horn 山体阴影做**乘法混合**（shaded relief），可再叠加任意 RGB 图层（alpha 合成），输出带地理配准的 3 波段 RGB GeoTIFF 与 PDF。

适合出版级地形图、挂图与图集中的底图制作。

## 核心算法

dem_to_color(归一化+colormap) → horn_hillshade → hillshade_blend 乘法混合(ambient+shade) → 可选 alpha_composite 叠加 → uint8 RGB GeoTIFF。

## 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-map-print-composition.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（高 dpi 印刷）

```bash
python geoskill-map-print-composition.py --input dem.tif --dpi 300
```

### 示例 3（叠加图层 alpha）

```bash
python geoskill-map-print-composition.py --input dem.tif --overlay landcover.tif --overlay-alpha 0.5
```

### 示例 4（自定义光照）

```bash
python geoskill-map-print-composition.py --input dem.tif --azimuth 270 --altitude 40 --ambient 0.1
```

### 示例 5（合成 shaded relief）

```bash
python geoskill-map-print-composition.py --bbox 116 39 117 40 --synthetic --zfactor 2
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `print_map.tif` | GeoTIFF | 3 波段 RGB 打印栅格（主产物/可验证产物） |
| `print_map.pdf` | PDF | 版式 PDF |
| `print_meta.json` | JSON | 光照/叠加/统计 |

每次运行还会产出 `output-manifest.json`（运行清单）。

## 数据源 / Source

本地 GeoTIFF / 矢量文件；`--synthetic` 模式生成物理一致的模拟数据，完全离线。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
