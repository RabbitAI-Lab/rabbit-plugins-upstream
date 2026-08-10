---
name: geoskill-spatial-index-builder
description: '构建 R-tree / Quadtree / GeoHash 空间索引并统计查询性能，结果与暴力搜索对齐。Build R-tree / Quadtree / GeoHash spatial indexes, benchmark query performance and align results with brute-force search.'
---

# 空间索引构建 | Spatial Index Builder

Builds three kinds of spatial indexes and benchmarks their query performance against a batch of query windows; results from every index are strictly validated against brute-force scanning:

- **R-tree**: built on shapely's `STRtree`, performs exact intersection queries with `predicate="intersects"`; the most widely used spatial index in production environments.
- **Quadtree**: a self-implemented quadtree — recursively splits the bounding box into four quadrants, subdividing on capacity overflow; queries only traverse nodes intersecting the window, and features spanning child nodes are kept at the parent node to guarantee no misses.
- **GeoHash**: a self-implemented GeoHash encoder/decoder (base32) that builds an inverted index over all cells covered by each geometry's bounding box (avoiding misses caused by centroids falling outside the window); queries enumerate the cells covered by the window in grid alignment and then filter precisely.

The benchmark times each index and compares result consistency against brute-force scanning, reporting average latency, hit counts and speed-up ratio. `--synthetic` mode generates 300 random points.

## Dependencies / 依赖

```bash
pip install numpy rasterio geopandas shapely fiona pyproj
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-spatial-index-builder.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 1 (synthetic data, 300 points, 15 queries, offline)

```bash
python geoskill-spatial-index-builder.py --bbox 116.0 39.0 117.0 40.0 --synthetic --features 300 --queries 15 --output-dir ./bench
```

### Example 2: build and benchmark indexes on POI data

```bash
python geoskill-spatial-index-builder.py --input pois.shp --queries 30 --output-dir ./poi_bench
```

### Example 3: high-precision GeoHash (precision 7)

```bash
python geoskill-spatial-index-builder.py --bbox 121.0 31.0 122.0 32.0 --synthetic --precision 7 --output-dir ./gh7 --quiet
```

### Example 4: stress test with a large dataset

```bash
python geoskill-spatial-index-builder.py --bbox 116.0 39.0 117.0 40.0 --synthetic --features 2000 --queries 50 --output-dir ./stress
```

### Example 5: low-precision GeoHash comparison

```bash
python geoskill-spatial-index-builder.py --bbox 116.0 39.0 117.0 40.0 --synthetic --precision 4 --features 500 --output-dir ./gh4
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `spatial_index_report.json` | JSON | Per-index performance, hit counts, consistency |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- `--input`: local vector file
- `--synthetic`: locally generated random point set

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
