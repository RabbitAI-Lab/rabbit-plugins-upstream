---
name: geoskill-service-area-analysis
description: '网络等时圈分析+多设施服务区+覆盖统计，输出服务区GeoJSON'
---

# 服务区分析 | Service Area Analysis

Computes facility service areas (isochrones) from a network graph: for each facility, Dijkstra computes network travel times, and service areas are delineated by time thresholds. Supports multi-facility overlay, nearest-facility assignment, and multi-threshold coverage statistics.

## Core Algorithm / 核心算法

- Multi-source Dijkstra isochrones
- Nearest-facility assignment
- Multi-threshold coverage demand statistics

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy geopandas shapely
```

## Usage / 使用方法

### Example 1 (Synthetic Data, Offline)

```bash
python geoskill-service-area-analysis.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (Specified Region + Silent Mode)

```bash
python geoskill-service-area-analysis.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### Example 3 (Real Input)

```bash
python geoskill-service-area-analysis.py --input <your data file> --output-dir ./out3
```

### Example 4 (Minimal-Region Boundary Test)

```bash
python geoskill-service-area-analysis.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `service_area.geojson` | GeoTIFF/GeoJSON/JSON | Primary output |
| `service_area_stats.json` | GeoTIFF/GeoJSON/JSON | Primary output |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- Synthetic mode: locally generates physically consistent simulated data, with no external data source.
- Real mode: reads local input files, with no network requests.

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default and makes no network requests.
- `--synthetic` mode reads no external data.
- All computation is done locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-service-area-analysis
description: '网络等时圈分析+多设施服务区+覆盖统计，输出服务区GeoJSON'
---

# 服务区分析 | Service Area Analysis

基于网络图计算设施服务区（等时圈）：对每个设施用 Dijkstra 计算网络通行时间，按时间阈值划分服务区，支持多设施叠加、最近设施分配与多阈值覆盖统计。

## 核心算法

- 多源 Dijkstra 等时圈
- 最近设施分配
- 多阈值覆盖需求统计

## 依赖

```bash
pip install numpy rasterio scipy geopandas shapely
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-service-area-analysis.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（指定区域 + 静默）

```bash
python geoskill-service-area-analysis.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### 示例 3（真实输入）

```bash
python geoskill-service-area-analysis.py --input <你的数据文件> --output-dir ./out3
```

### 示例 4（极小区域边界测试）

```bash
python geoskill-service-area-analysis.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `service_area.geojson` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `service_area_stats.json` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- 合成模式：本地生成物理一致的模拟数据，无外部数据源。
- 真实模式：读取本地输入文件，无网络请求。

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求。
- `--synthetic` 模式不读取任何外部数据。
- 所有计算在本地完成，不上传用户数据。

## License

MIT
