---
name: geoskill-network-routing
description: 'Dijkstra/A*多约束路径规划，支持时间/距离权重和多起终点'
---

# 网络路径规划 | Network Routing

Network path planning: supports Dijkstra and A* (admissible heuristic; the scaling factor is derived automatically from the actual edge weights to guarantee optimality), multi-constraint routing weighted by distance or time, and batch planning for multiple origins and destinations.

## Core Algorithm / 核心算法

- Dijkstra shortest path
- A* (admissible heuristic)
- Distance/time multi-constraint + multi-OD

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy geopandas shapely
```

## Usage / 使用方法

### Example 1 (synthetic data, offline)

```bash
python geoskill-network-routing.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (specified area + quiet mode)

```bash
python geoskill-network-routing.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### Example 3 (real input)

```bash
python geoskill-network-routing.py --input <your data file> --output-dir ./out3
```

### Example 4 (tiny-area boundary test)

```bash
python geoskill-network-routing.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `routes.geojson` | GeoTIFF/GeoJSON/JSON | Main output |
| `routing_stats.json` | GeoTIFF/GeoJSON/JSON | Main output |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- Synthetic mode: physically consistent simulated data generated locally; no external data source.
- Real mode: reads local input files; no network requests.

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default; no network requests are made.
- `--synthetic` mode reads no external data.
- All computation is performed locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-network-routing
description: 'Dijkstra/A*多约束路径规划，支持时间/距离权重和多起终点'
---

# 网络路径规划 | Network Routing

网络路径规划：支持 Dijkstra 与 A*（可采纳启发式，缩放系数由实际边权自动推导以保证最优性），按距离或时间加权的多约束路径，多起终点批量规划。

## 核心算法

- Dijkstra 最短路径
- A*（可采纳启发式）
- 距离/时间多约束 + 多 OD

## 依赖

```bash
pip install numpy rasterio scipy geopandas shapely
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-network-routing.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（指定区域 + 静默）

```bash
python geoskill-network-routing.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### 示例 3（真实输入）

```bash
python geoskill-network-routing.py --input <你的数据文件> --output-dir ./out3
```

### 示例 4（极小区域边界测试）

```bash
python geoskill-network-routing.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `routes.geojson` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `routing_stats.json` | GeoTIFF/GeoJSON/JSON | 主产物 |
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
