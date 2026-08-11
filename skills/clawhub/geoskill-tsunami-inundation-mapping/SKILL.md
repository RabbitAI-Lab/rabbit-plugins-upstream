---
name: geoskill-tsunami-inundation-mapping
description: 'Bathtub水文连通淹没建模,输出水深、到达时间与撤离区'
---

# 海啸淹没制图 | Tsunami Inundation Mapping

Bathtub inundation modeling based on a DEM with hydrological connectivity constraints — only depressions 8-connected to the coastal seed region are flooded; isolated inland basins remain dry even when their elevation is below the water level. Outputs include the inundation extent, water depth (water level − elevation, always non-negative), arrival time from the coast (Euclidean distance × pixel size / wave speed), and critical evacuation zones (dry land below the safety margin that is not flooded). Both the inundated area and water depth are monotonically non-decreasing with water level.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy
```

## Usage / 使用方法

### Basic Usage (Synthetic Data, Offline)

```bash
python geoskill-tsunami-inundation-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### More Examples

```bash
python geoskill-tsunami-inundation-mapping.py --bbox 120 30 121 31 --synthetic --output-dir ./out
python geoskill-tsunami-inundation-mapping.py --input dem.tif --water-level 15 --output-dir ./out
python geoskill-tsunami-inundation-mapping.py --bbox 120 30 121 31 --water-level 20 --wave-speed 8 --synthetic --output-dir ./out
python geoskill-tsunami-inundation-mapping.py --bbox 121 31 122 32 --synthetic --quiet --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `inundation.tif` | GeoTIFF | Inundation extent mask |
| `water_depth.tif` | GeoTIFF | Flood water depth (m, ≥0) |
| `arrival_time.tif` | GeoTIFF | Tsunami arrival time (s) |
| `evacuation_zone.tif` | GeoTIFF | Recommended evacuation zone (mutually exclusive with the inundated area) |
| `tsunami_params.json` | JSON | Parameters such as water level / wave speed / pixel size |

Each run also produces `output-manifest.json` (run manifest, including inputs / products / QA summary).

## Data Source / 数据源 / Source

Real mode reads a single-band DEM GeoTIFF (in meters); synthetic mode generates coastal terrain offline (including ridges and isolated depressions).

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
