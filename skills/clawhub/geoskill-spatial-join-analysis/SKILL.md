---
name: geoskill-spatial-join-analysis
description: '空间关系判断(intersects/within/nearest)+属性聚合统计'
---

# 空间连接分析 | Spatial Join Analysis

Spatial join between two vector layers: spatial relationship tests (intersects/within/contains/crosses/touches/overlaps/nearest, accelerated by STRtree) plus attribute aggregation (count/sum/mean/max/min) on the join results.

## Core Algorithm / 核心算法

- Spatial relationship tests (STRtree)
- Nearest-neighbor join
- Attribute aggregation statistics

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy geopandas shapely
```

## Usage / 使用方法

### Example 1 (synthetic data, offline)

```bash
python geoskill-spatial-join-analysis.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (custom region + quiet mode)

```bash
python geoskill-spatial-join-analysis.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### Example 3 (real input)

```bash
python geoskill-spatial-join-analysis.py --input <your data file> --output-dir ./out3
```

### Example 4 (tiny-area boundary test)

```bash
python geoskill-spatial-join-analysis.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `spatial_join.geojson` | GeoTIFF/GeoJSON/JSON | Primary output |
| `join_stats.json` | GeoTIFF/GeoJSON/JSON | Primary output |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- Synthetic mode: locally generates physically consistent simulated data; no external data sources.
- Real-data mode: reads local input files; no network requests.

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default; makes no network requests.
- `--synthetic` mode reads no external data.
- All computation is done locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-spatial-join-analysis
description: '空间关系判断(intersects/within/nearest)+属性聚合统计'
---

# 空间连接分析 | Spatial Join Analysis

两层矢量数据空间连接：关系判断（intersects/within/contains/crosses/touches/overlaps/nearest，STRtree 加速）+ 按连接结果对属性做 count/sum/mean/max/min 聚合。

## 核心算法

- 空间关系判断（STRtree）
- nearest 最近连接
- 属性聚合统计

## 依赖

```bash
pip install numpy rasterio scipy geopandas shapely
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-spatial-join-analysis.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（指定区域 + 静默）

```bash
python geoskill-spatial-join-analysis.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### 示例 3（真实输入）

```bash
python geoskill-spatial-join-analysis.py --input <你的数据文件> --output-dir ./out3
```

### 示例 4（极小区域边界测试）

```bash
python geoskill-spatial-join-analysis.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `spatial_join.geojson` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `join_stats.json` | GeoTIFF/GeoJSON/JSON | 主产物 |
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
