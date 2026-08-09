---
name: geoskill-vector-simplification
description: '用 Douglas-Peucker / Visvalingam 算法简化矢量几何，统计顶点减少与面积保持。Simplify vector geometries with Douglas-Peucker / Visvalingam and report vertex reduction and area retention.'
---

# 矢量简化 | Vector Simplification

Reduces the number of vertices in vector geometries with two classic line simplification algorithms, for small-scale cartographic generalization, data volume reduction and lower tile rendering load:

- **Douglas-Peucker**: iterative implementation that compares the perpendicular distance of points to the chord against a tolerance epsilon and removes points within the tolerance band; good shape preservation and the most widely used line/area simplification algorithm.
- **Visvalingam-Whyatt**: iteratively removes the point with the smallest "effective area" (the triangle area of three adjacent points) and supports stopping by an area threshold; smoother for jagged lines.

LineString / Polygon (with holes) / Multi* / GeometryCollection geometries are simplified recursively; simplified rings are guaranteed to remain closed with no fewer than 3 points. Reports the vertex reduction ratio and the polygon area retention rate. `--synthetic` mode generates a high-density circle (64 vertices) and a jagged line as test features.

## Dependencies / 依赖

```bash
pip install numpy rasterio geopandas shapely fiona pyproj
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-vector-simplification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 1（合成数据，Douglas-Peucker，离线）

```bash
python geoskill-vector-simplification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --method douglas-peucker --tolerance 0.001 --output-dir ./dp
```

### 示例 2：简化道路 Shapefile

```bash
python geoskill-vector-simplification.py --input roads.shp --method douglas-peucker --tolerance 0.0005 --output-dir ./roads_simp
```

### 示例 3：Visvalingam 面积阈值简化边界

```bash
python geoskill-vector-simplification.py --input boundary.gpkg --method visvalingam --tolerance 0.00001 --output-dir ./visv
```

### 示例 4：合成数据 Visvalingam

```bash
python geoskill-vector-simplification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --method visvalingam --tolerance 0.0001 --output-dir ./visv2 --quiet
```

### Example 5: Large-Tolerance Quick Overview

```bash
python geoskill-vector-simplification.py --input coast.geojson --method douglas-peucker --tolerance 0.01 --output-dir ./coarse
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `simplified.geojson` | GeoJSON | Simplified features |
| `simplification_stats.json` | JSON | Vertex reduction ratio, area retention rate |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- `--input`: local vector file
- `--synthetic`: locally generated high-density test features

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-vector-simplification
description: '用 Douglas-Peucker / Visvalingam 算法简化矢量几何，统计顶点减少与面积保持。Simplify vector geometries with Douglas-Peucker / Visvalingam and report vertex reduction and area retention.'
---

# 矢量简化 | Vector Simplification

用两种经典线简化算法减少矢量几何顶点数，用于小比例尺制图综合、降低
数据量与瓦片渲染负载：

- **Douglas-Peucker**：迭代版实现，比较点到弦的垂直距离与容差 epsilon，
  删除容差带内的点，保形性好，是最常用的线/面简化算法。
- **Visvalingam-Whyatt**：迭代删除“有效面积”（相邻三点三角形面积）最小
  的点，支持按面积阈值停止；对锯齿状线更平滑。

对 LineString / Polygon（含孔）/ Multi* / GeometryCollection 递归简化，
环简化后保证闭合且不少于 3 点。统计顶点减少比例与多边形面积保持率。
`--synthetic` 模式生成高密度圆（64 顶点）与锯齿线作为测试要素。

## 依赖

```bash
pip install numpy rasterio geopandas shapely fiona pyproj
```

## 使用方法

### 基本用法

```bash
python geoskill-vector-simplification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 1（合成数据，Douglas-Peucker，离线）

```bash
python geoskill-vector-simplification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --method douglas-peucker --tolerance 0.001 --output-dir ./dp
```

### 示例 2：简化道路 Shapefile

```bash
python geoskill-vector-simplification.py --input roads.shp --method douglas-peucker --tolerance 0.0005 --output-dir ./roads_simp
```

### 示例 3：Visvalingam 面积阈值简化边界

```bash
python geoskill-vector-simplification.py --input boundary.gpkg --method visvalingam --tolerance 0.00001 --output-dir ./visv
```

### 示例 4：合成数据 Visvalingam

```bash
python geoskill-vector-simplification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --method visvalingam --tolerance 0.0001 --output-dir ./visv2 --quiet
```

### 示例 5：大容差快速概览

```bash
python geoskill-vector-simplification.py --input coast.geojson --method douglas-peucker --tolerance 0.01 --output-dir ./coarse
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `simplified.geojson` | GeoJSON | 简化后的要素 |
| `simplification_stats.json` | JSON | 顶点减少比例、面积保持率 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- `--input`：本地矢量文件
- `--synthetic`：本地生成高密度测试要素

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
