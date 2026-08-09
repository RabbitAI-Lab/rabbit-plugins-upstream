---
name: geoskill-smart-city-digital-twin
description: 'Multi-source data fusion to build 3D scene configuration and API interface descriptions for a city digital twin'
---

# 城市信息模型/数字孪生 | Smart City Digital Twin

Fuses multi-source geospatial data (DEM/DSM/building height) into a 3D scene configuration and API interface description for a city digital twin, consumable by 3D engines such as Cesium / three.js.

Building height is derived from DSM − DEM, footprints are extracted via connected-component analysis and extruded into LOD1 box blocks; a scene configuration with a unified coordinate system, scene bbox, tiling scheme, and LOD distance thresholds is generated; an OpenAPI-style list of REST endpoints (tile / building / scene metadata, etc.) is produced; and a fusion completeness check covering layer coverage and height consistency is performed.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'geopandas' 'shapely' 'scipy'
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-smart-city-digital-twin.py --bbox 116.0 39.0 117.0 40.0 [other parameters]
```

### Example 1 (Synthetic City, Offline)

```bash
python geoskill-smart-city-digital-twin.py --bbox 116 39 117 40 --synthetic --output-dir ./out
```

### 示例 2（真实 DEM/DSM）

```bash
python geoskill-smart-city-digital-twin.py --input city.tif --output-dir ./out
```

### Example 3 (Generate Scene Config Only)

```bash
python geoskill-smart-city-digital-twin.py --input city.tif --format scene --output-dir ./out
```

### 示例 4（只生成 API 描述）

```bash
python geoskill-smart-city-digital-twin.py --input city.tif --format api --base-url https://twin.city.gov/api/v1 --output-dir ./out
```

### 示例 5（调建筑高度门限与 LOD 级数）

```bash
python geoskill-smart-city-digital-twin.py --input city.tif --height-threshold 5 --lod-levels 5 --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `building_height.tif` | GeoTIFF | Building / feature height (DSM−DEM) |
| `buildings_3d.geojson` | GeoJSON | LOD1 building blocks (with height / number of floors, format=scene/both) |
| `scene_config.json` | JSON | 3D scene configuration (CRS/bbox/layers/LOD/tiles) |
| `api_spec.json` | JSON | OpenAPI-style endpoint list (format=api/both) |
| `twin_report.json` | JSON | Fusion completeness report |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

A multi-band GeoTIFF with band order DEM / DSM, or `--synthetic` to generate physically consistent simulated data (fully offline).

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; no user data is uploaded.

## License / License

MIT

---


<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-smart-city-digital-twin
description: 'Multi-source data fusion to build 3D scene configuration and API interface descriptions for a city digital twin'
---

# 城市信息模型/数字孪生 | Smart City Digital Twin

把多源地理空间数据（DEM/DSM/建筑高度）融合为城市数字孪生的 3D 场景配置与 API 接口描述，供 Cesium / three.js 等三维引擎消费。

由 DSM − DEM 得建筑高度，连通域提取足迹并挤出为 LOD1 长方体体块；生成统一坐标系、场景 bbox、瓦片方案、LOD 距离阈值的场景配置；并以 OpenAPI 风格输出瓦片/建筑/场景元数据等 REST 端点清单；同时做图层覆盖率与高度一致性的融合完整性校验。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'geopandas' 'shapely' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-smart-city-digital-twin.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例 1（合成城市，离线）

```bash
python geoskill-smart-city-digital-twin.py --bbox 116 39 117 40 --synthetic --output-dir ./out
```

### 示例 2（真实 DEM/DSM）

```bash
python geoskill-smart-city-digital-twin.py --input city.tif --output-dir ./out
```

### 示例 3（只生成场景配置）

```bash
python geoskill-smart-city-digital-twin.py --input city.tif --format scene --output-dir ./out
```

### 示例 4（只生成 API 描述）

```bash
python geoskill-smart-city-digital-twin.py --input city.tif --format api --base-url https://twin.city.gov/api/v1 --output-dir ./out
```

### 示例 5（调建筑高度门限与 LOD 级数）

```bash
python geoskill-smart-city-digital-twin.py --input city.tif --height-threshold 5 --lod-levels 5 --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `building_height.tif` | GeoTIFF | 建筑/地物高度（DSM−DEM） |
| `buildings_3d.geojson` | GeoJSON | LOD1 建筑体块（含高度/层数，format=scene/both） |
| `scene_config.json` | JSON | 3D 场景配置（CRS/bbox/图层/LOD/瓦片） |
| `api_spec.json` | JSON | OpenAPI 风格接口清单（format=api/both） |
| `twin_report.json` | JSON | 融合完整性报告 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

多波段 GeoTIFF，波段顺序 DEM / DSM。 或使用 `--synthetic` 生成物理一致的模拟数据（完全离线）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
