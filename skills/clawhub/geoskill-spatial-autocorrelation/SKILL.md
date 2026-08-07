---
name: geoskill-spatial-autocorrelation
description: 'Global Moran I+LISA+Gi*+蒙特卡洛检验，评估空间聚集模式'
---

# 空间自相关分析 | Spatial Autocorrelation

Assesses spatial clustering patterns: computes Global Moran's I (with normal-approximation z/p values), Local Moran's I (LISA), and Getis-Ord Gi*, and derives pseudo p-values via Monte Carlo random permutation tests. Supports rook adjacency and KNN weight matrices.

## Core Algorithm / 核心算法

- Global Moran's I and its variance
- LISA local autocorrelation
- Getis-Ord Gi* with Monte Carlo test

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy geopandas shapely
```

## Usage / 使用方法

### Example 1 (Synthetic Data, Offline)

```bash
python geoskill-spatial-autocorrelation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (Specified Region + Silent Mode)

```bash
python geoskill-spatial-autocorrelation.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### Example 3 (Real Input)

```bash
python geoskill-spatial-autocorrelation.py --input <your data file> --output-dir ./out3
```

### Example 4 (Minimal-Region Boundary Test)

```bash
python geoskill-spatial-autocorrelation.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `lisa.tif` | GeoTIFF/GeoJSON/JSON | Primary output |
| `gi_star.tif` | GeoTIFF/GeoJSON/JSON | Primary output |
| `autocorrelation_stats.json` | GeoTIFF/GeoJSON/JSON | Primary output |
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
name: geoskill-spatial-autocorrelation
description: 'Global Moran I+LISA+Gi*+蒙特卡洛检验，评估空间聚集模式'
---

# 空间自相关分析 | Spatial Autocorrelation

评估空间聚集模式：计算 Global Moran's I（含正态近似 z/p 值）、Local Moran's I（LISA）与 Getis-Ord Gi*，并用蒙特卡洛随机置换检验给出伪 p 值。支持 rook 邻接与 KNN 权重矩阵。

## 核心算法

- Global Moran's I 及方差
- LISA 局部自相关
- Getis-Ord Gi* 与蒙特卡洛检验

## 依赖

```bash
pip install numpy rasterio scipy geopandas shapely
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-spatial-autocorrelation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（指定区域 + 静默）

```bash
python geoskill-spatial-autocorrelation.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### 示例 3（真实输入）

```bash
python geoskill-spatial-autocorrelation.py --input <你的数据文件> --output-dir ./out3
```

### 示例 4（极小区域边界测试）

```bash
python geoskill-spatial-autocorrelation.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `lisa.tif` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `gi_star.tif` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `autocorrelation_stats.json` | GeoTIFF/GeoJSON/JSON | 主产物 |
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
