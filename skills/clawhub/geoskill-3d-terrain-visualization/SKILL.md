---
name: geoskill-3d-terrain-visualization
description: 'Render 3D terrain from DEM and imagery with vertical exaggeration and an HTML viewer'
---

# 三维地形可视化 | 3D Terrain Visualization

Computes per-pixel normal vectors and Lambertian diffuse illumination from a DEM, overlays terrain colors to produce a lit 3D terrain map, and outputs a CSS 3D perspective viewer (draggable pitch/rotation, adjustable vertical exaggeration).

Illumination uses a diffuse reflection model driven by solar azimuth/altitude angles; vertical exaggeration amplifies the influence of elevation relative to horizontal distance via the zfactor.

## Core Algorithm / 核心算法

np.gradient computes the DEM gradient → unit normal vectors (nx,ny,nz) → dot product with the sun direction vector yields the Lambertian shade → terrain colormap × (ambient+shade).

Horizontal pixel size is computed in **meters**: EPSG:4326 (degree) inputs are automatically converted at ≈111320·cos(φ) m/degree, while projected-coordinate inputs are first reprojected to WGS84; zfactor is a pure vertical exaggeration factor (consistent with the GDAL gdaldem `-z` / ESRI z_factor convention). NoData pixels are excluded from the gradient and statistics and are marked as nodata in the output; bbox and parameter ranges are validated (invalid input exits with code 6).

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## Usage / 使用方法

### Example 1 (Synthetic Data, Offline)

```bash
python geoskill-3d-terrain-visualization.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (Custom Lighting)

```bash
python geoskill-3d-terrain-visualization.py --input dem.tif --azimuth 270 --altitude 35 --exaggeration 3
```

### Example 3 (Low Ambient Light for Stronger Relief)

```bash
python geoskill-3d-terrain-visualization.py --input dem.tif --ambient 0.05
```

### Example 4 (Synthetic Mode with Exaggeration)

```bash
python geoskill-3d-terrain-visualization.py --bbox 116 39 117 40 --synthetic --exaggeration 4
```

### 示例 5（自定义 cellsize）

```bash
python geoskill-3d-terrain-visualization.py --input dem.tif --cellsize 30
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `terrain_3d.html` | HTML | CSS 3D perspective viewer (primary output) |
| `shaded_relief.tif` | GeoTIFF | Illumination intensity raster [0,1] (verifiable output) |
| `terrain_3d.json` | JSON | Illumination/exaggeration/extent metadata |

Each run also produces `output-manifest.json` (run manifest).

## Data Source / 数据源 / Source

Local GeoTIFF / vector files; `--synthetic` mode generates physically consistent simulated data, fully offline.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-3d-terrain-visualization
description: 'Render 3D terrain from DEM and imagery with vertical exaggeration and an HTML viewer'
---

# 三维地形可视化 | 3D Terrain Visualization

从 DEM 计算逐像元法向量与 Lambertian 漫反射光照，叠加 terrain 色彩生成带光照的三维地形图，并输出一个 CSS 3D 透视查看器（可拖动俯仰/旋转、调节垂直夸张）。

光照采用太阳方位角/高度角驱动的漫反射模型；垂直夸张通过 zfactor 放大高程相对水平距离的影响。

## 核心算法

np.gradient 求 DEM 梯度 → 单位法向量 (nx,ny,nz) → 与太阳方向向量点积得 Lambertian shade → terrain colormap × (ambient+shade)。

水平像元尺寸按**米**计算：EPSG:4326（度）输入自动按 ≈111320·cos(φ) m/度换算，投影坐标输入先重投影到 WGS84；zfactor 为纯垂直夸张系数（与 GDAL gdaldem `-z` / ESRI z_factor 约定一致）。NoData 像元不参与梯度与统计，输出中标记为 nodata；bbox 与参数值域均有校验（非法输入退出码 6）。

## 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-3d-terrain-visualization.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（自定义光照）

```bash
python geoskill-3d-terrain-visualization.py --input dem.tif --azimuth 270 --altitude 35 --exaggeration 3
```

### 示例 3（低环境光更立体）

```bash
python geoskill-3d-terrain-visualization.py --input dem.tif --ambient 0.05
```

### 示例 4（合成模式指定夸张）

```bash
python geoskill-3d-terrain-visualization.py --bbox 116 39 117 40 --synthetic --exaggeration 4
```

### 示例 5（自定义 cellsize）

```bash
python geoskill-3d-terrain-visualization.py --input dem.tif --cellsize 30
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `terrain_3d.html` | HTML | CSS 3D 透视查看器（主产物） |
| `shaded_relief.tif` | GeoTIFF | 光照强度栅格 [0,1]（可验证产物） |
| `terrain_3d.json` | JSON | 光照/夸张/范围元数据 |

每次运行还会产出 `output-manifest.json`（运行清单）。

## 数据源 / Source

本地 GeoTIFF / 矢量文件；`--synthetic` 模式生成物理一致的模拟数据，完全离线。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
