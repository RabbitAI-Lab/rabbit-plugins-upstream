---
name: geoskill-spatial-etl-pipeline
description: '配置驱动的提取-转换-加载流水线，含分步日志与质量报告。Config-driven extract-transform-load pipeline with per-step logging and a quality report.'
---

# 空间ETL流水线 | Spatial ETL Pipeline

Config-driven spatial ETL (Extract-Transform-Load) pipeline:

- **Extract**: extracts a GeoDataFrame from synthetic data or a local vector file.
- **Transform**: executes composable operators in config order — `filter_bbox` (window filter), `filter_attribute` (attribute comparison filter supporting 6 comparison operators such as >/</==), `reproject` (reprojection), `add_field` (derived columns: area / perimeter / centroid / sequence number), `rename` (field renaming), `buffer` (buffering).
- **Load**: writes out GeoJSON or GeoPackage.

Each step records structured logs (step name, duration, input/output feature counts, status), and a quality report (feature gain/loss, retention rate, null-value ratio, invalid geometry count, CRS) is aggregated at the end. Any pipeline can be customized by supplying a JSON config via `--config`. `--synthetic` mode generates random polygons and runs the default pipeline.

## Dependencies / 依赖

```bash
pip install numpy rasterio geopandas shapely fiona pyproj
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-spatial-etl-pipeline.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 1 (Synthetic Data, Default Pipeline, Offline)

```bash
python geoskill-spatial-etl-pipeline.py --bbox 116.0 39.0 117.0 40.0 --synthetic --features 60 --output-dir ./etl
```

### Example 2: Custom Configuration (Filter + Reprojection + Buffer)

```bash
python geoskill-spatial-etl-pipeline.py --config pipeline.json --output-dir ./custom
```

Example configuration `pipeline.json`:

```json
{
  "source": {"type": "file", "path": "raw.geojson"},
  "steps": [
    {"op": "filter_attribute", "field": "value", "cmp": ">", "value": 10},
    {"op": "reproject", "to_crs": "EPSG:3857"},
    {"op": "buffer", "distance": 100}
  ],
  "load": {"format": "gpkg", "path": "out.gpkg"}
}
```

### Example 3: Area Derivation on Real Files

```bash
python geoskill-spatial-etl-pipeline.py --input parcels.shp --output-dir ./area
```

### Example 4: Synthetic + Large Sample

```bash
python geoskill-spatial-etl-pipeline.py --bbox 121.0 31.0 122.0 32.0 --synthetic --features 200 --output-dir ./etl2 --quiet
```

### Example 5: Small-Area Pipeline

```bash
python geoskill-spatial-etl-pipeline.py --bbox 116.39 39.90 116.40 39.91 --synthetic --features 30 --output-dir ./tiny
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `etl_output.geojson` | GeoJSON | Load step output (default config) |
| `etl_report.json` | JSON | Quality report + per-step logs + config |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- `--input`: local vector file
- `--config`: JSON config (can point to any source)
- `--synthetic`: generates random polygons locally

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; no user data is uploaded.

## License / License

MIT

---


<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-spatial-etl-pipeline
description: '配置驱动的提取-转换-加载流水线，含分步日志与质量报告。Config-driven extract-transform-load pipeline with per-step logging and a quality report.'
---

# 空间ETL流水线 | Spatial ETL Pipeline

配置驱动的空间 ETL（Extract-Transform-Load）流水线：

- **Extract**：从合成数据或本地矢量文件提取 GeoDataFrame。
- **Transform**：按配置顺序执行可组合算子——`filter_bbox`（窗口过滤）、
  `filter_attribute`（属性比较过滤，支持 >/</== 等 6 种比较符）、
  `reproject`（重投影）、`add_field`（面积/周长/质心/序号派生列）、
  `rename`（字段重命名）、`buffer`（缓冲）。
- **Load**：写出 GeoJSON 或 GeoPackage。

每个步骤记录结构化日志（步骤名、耗时、输入/输出要素数、状态），结束后
汇总质量报告（要素增减、保留率、空值比例、无效几何数、CRS）。用
`--config` 提供 JSON 配置即可自定义任意流水线。`--synthetic` 模式生成
随机多边形跑默认流水线。

## 依赖

```bash
pip install numpy rasterio geopandas shapely fiona pyproj
```

## 使用方法

### 基本用法

```bash
python geoskill-spatial-etl-pipeline.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 1（合成数据，默认流水线，离线）

```bash
python geoskill-spatial-etl-pipeline.py --bbox 116.0 39.0 117.0 40.0 --synthetic --features 60 --output-dir ./etl
```

### 示例 2：自定义配置（过滤 + 重投影 + 缓冲）

```bash
python geoskill-spatial-etl-pipeline.py --config pipeline.json --output-dir ./custom
```

配置示例 `pipeline.json`：

```json
{
  "source": {"type": "file", "path": "raw.geojson"},
  "steps": [
    {"op": "filter_attribute", "field": "value", "cmp": ">", "value": 10},
    {"op": "reproject", "to_crs": "EPSG:3857"},
    {"op": "buffer", "distance": 100}
  ],
  "load": {"format": "gpkg", "path": "out.gpkg"}
}
```

### 示例 3：对真实文件做面积派生

```bash
python geoskill-spatial-etl-pipeline.py --input parcels.shp --output-dir ./area
```

### 示例 4：合成 + 大样本

```bash
python geoskill-spatial-etl-pipeline.py --bbox 121.0 31.0 122.0 32.0 --synthetic --features 200 --output-dir ./etl2 --quiet
```

### 示例 5：小范围流水线

```bash
python geoskill-spatial-etl-pipeline.py --bbox 116.39 39.90 116.40 39.91 --synthetic --features 30 --output-dir ./tiny
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `etl_output.geojson` | GeoJSON | Load 步骤产物（默认配置） |
| `etl_report.json` | JSON | 质量报告 + 逐步日志 + 配置 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- `--input`：本地矢量文件
- `--config`：JSON 配置（可指向任意源）
- `--synthetic`：本地生成随机多边形

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
