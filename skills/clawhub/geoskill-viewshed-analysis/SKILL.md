---
name: geoskill-viewshed-analysis
description: '基于DEM的视线分析，含地球曲率修正和多观察点叠加'
---

# 视域分析 | Viewshed Analysis

DEM-based visibility analysis: from each observer point, it determines pixel by pixel along radial directions whether the line of sight is blocked by terrain, with support for Earth curvature and atmospheric refraction correction (effective Earth radius method). Multiple observer points are overlaid to output the visibility count and a binary visible raster.

## Core Algorithm / 核心算法

- Per-ray maximum elevation angle tracing
- Earth curvature + refraction correction
- Multi-observer overlay

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy
```

## Usage / 使用方法

### Example 1 (Synthetic Data, Offline)

```bash
python geoskill-viewshed-analysis.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (Specified Region + Silent Mode)

```bash
python geoskill-viewshed-analysis.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### Example 3 (Real Input)

```bash
python geoskill-viewshed-analysis.py --input <your data file> --output-dir ./out3
```

### Example 4 (Minimal-Region Boundary Test)

```bash
python geoskill-viewshed-analysis.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `viewshed.tif` | GeoTIFF/GeoJSON/JSON | Primary output |
| `viewshed_count.tif` | GeoTIFF/GeoJSON/JSON | Primary output |
| `viewshed_stats.json` | GeoTIFF/GeoJSON/JSON | Primary output |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- Synthetic mode: generates physically consistent simulated data locally; no external data source.
- Real mode: reads local input files; no network requests.

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default; no network requests are made.
- `--synthetic` mode reads no external data.
- All computation is done locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-viewshed-analysis
description: '基于DEM的视线分析，含地球曲率修正和多观察点叠加'
---

# 视域分析 | Viewshed Analysis

基于 DEM 的可视性分析：从观察点沿径向逐像元判断视线是否被地形遮挡，支持地球曲率与大气折射修正（等效地球半径法）。多观察点叠加输出可视次数与二值可视栅格。

## 核心算法

- 逐射线最大仰角追踪
- 地球曲率 + 折射修正
- 多观察点叠加

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-viewshed-analysis.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（指定区域 + 静默）

```bash
python geoskill-viewshed-analysis.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### 示例 3（真实输入）

```bash
python geoskill-viewshed-analysis.py --input <你的数据文件> --output-dir ./out3
```

### 示例 4（极小区域边界测试）

```bash
python geoskill-viewshed-analysis.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `viewshed.tif` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `viewshed_count.tif` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `viewshed_stats.json` | GeoTIFF/GeoJSON/JSON | 主产物 |
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
