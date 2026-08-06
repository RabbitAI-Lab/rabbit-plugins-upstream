# Spatial Index Builder (geoskill-spatial-index-builder)

> Build R-tree / Quadtree / GeoHash spatial indexes, benchmark query performance and align results with brute-force search.

---

## 1. Overview

Builds three spatial indexes and benchmarks their query performance over a batch of query windows, with all index results strictly aligned with brute-force scanning: - **R-tree**: built on shapely `STRtree`, performs exact intersection queries with `predicate="intersects"`; the most commonly used spatial index in production environments. - **Quadtree**: a self-implemented quadtree — recursively subdivides the bounding rectangle into four quadrants, splitting further when capacity overflows; queries only traverse nodes that intersect the window, and features spanning child nodes remain in the parent node to guarantee no missed detections. - **GeoHash**: a self-implemented GeoHash codec (base32) that builds an inverted index over all cells covered by the geometry's bounding rectangle (avoiding missed detections caused by centroids outside the window); queries enumerate the cells covered by the window with grid alignment and then apply exact filtering. The benchmark times each index and compares result consistency against brute-force scanning, outputting average elapsed time, hit counts and speedup. `--synthetic` mode generates 300 random points.

## 2. Features

Builds three spatial indexes and benchmarks their query performance over a batch of query windows, with all index results strictly aligned with brute-force scanning: - **R-tree**: built on shapely `STRtree`, performs exact intersection queries with `predicate="intersects"`; the most commonly used spatial index in production environments. - **Quadtree**: a self-implemented quadtree — recursively subdivides the bounding rectangle into four quadrants, splitting further when capacity overflows; queries only traverse nodes that intersect the window, and features spanning child nodes remain in the parent node to guarantee no missed detections. - **GeoHash**: a self-implemented GeoHash codec (base32) that builds an inverted index over all cells covered by the geometry's bounding rectangle (avoiding missed detections caused by centroids outside the window); queries enumerate the cells covered by the window with grid alignment and then apply exact filtering. The benchmark times each index and compares result consistency against brute-force scanning, outputting average elapsed time, hit counts and speedup. `--synthetic` mode generates 300 random points.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-spatial-index-builder.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `spatial_index_report.json` | JSON | Per-index performance, hit counts and consistency |
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

# 空间索引构建（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-spatial-index-builder
description: '构建 R-tree / Quadtree / GeoHash 空间索引并统计查询性能，结果与暴力搜索对齐。Build R-tree / Quadtree / GeoHash spatial indexes, benchmark query performance and align results with brute-force search.'
---

# 空间索引构建 | Spatial Index Builder

构建三种空间索引并对一批查询窗口做性能基准测试，所有索引结果与暴力
扫描严格对齐：

- **R-tree**：基于 shapely `STRtree`，用 `predicate="intersects"` 做精确
  相交查询，是生产环境最常用的空间索引。
- **Quadtree**：自实现四叉树——按外包矩形递归四分，容量溢出时细分，查询
  只遍历与窗口相交的节点；跨子节点的要素留在父节点保证不漏检。
- **GeoHash**：自实现 GeoHash 编解码（base32），按几何外包矩形覆盖的所有
  cell 建倒排表（避免质心在窗口外导致的漏检），查询时网格对齐枚举窗口
  覆盖的 cell 再精确过滤。

基准测试对每个索引计时并与暴力扫描比对结果一致性，输出平均耗时、命中
数与加速比。`--synthetic` 模式生成 300 个随机点。

## 依赖

```bash
pip install numpy rasterio geopandas shapely fiona pyproj
```

## 使用方法

### 基本用法

```bash
python geoskill-spatial-index-builder.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 1（合成数据，300 点 15 次查询，离线）

```bash
python geoskill-spatial-index-builder.py --bbox 116.0 39.0 117.0 40.0 --synthetic --features 300 --queries 15 --output-dir ./bench
```

### 示例 2：对 POI 数据建索引基准测试

```bash
python geoskill-spatial-index-builder.py --input pois.shp --queries 30 --output-dir ./poi_bench
```

### 示例 3：高精度 GeoHash（precision 7）

```bash
python geoskill-spatial-index-builder.py --bbox 121.0 31.0 122.0 32.0 --synthetic --precision 7 --output-dir ./gh7 --quiet
```

### 示例 4：大数据量压测

```bash
python geoskill-spatial-index-builder.py --bbox 116.0 39.0 117.0 40.0 --synthetic --features 2000 --queries 50 --output-dir ./stress
```

### 示例 5：低精度 GeoHash 对比

```bash
python geoskill-spatial-index-builder.py --bbox 116.0 39.0 117.0 40.0 --synthetic --precision 4 --features 500 --output-dir ./gh4
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `spatial_index_report.json` | JSON | 各索引性能、命中数、一致性 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- `--input`：本地矢量文件
- `--synthetic`：本地生成随机点集

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
