---
name: geoskill-sar-ship-detection
description: 'SAR 船舶检测：CA/OS-CFAR 恒虚警检测 + 连通域聚类，从单极化 SAR 强度影像提取船舶目标并输出 GeoJSON 矢量与属性表'
---

# SAR船舶检测 | SAR Ship Detection

Automatically detects ship targets at sea from single-polarization SAR intensity imagery. Core workflow:

1. **CFAR constant false alarm rate detection**: within a sliding window, background cells outside the guard band estimate the local clutter power to set an adaptive threshold, maintaining a constant false alarm rate under different sea states.
   - **CA-CFAR** (cell averaging): threshold = α·μ_bg, α = N·(Pfa^(−1/N) − 1) (closed-form solution for exponential clutter).
   - **OS-CFAR** (ordered statistics): uses the k-th order statistic of the background to estimate clutter; more robust to multiple targets / clutter edges.
2. **Connected-component clustering**: labels connected components of threshold-exceeding pixels and extracts each target's area, centroid, peak intensity and bounding box, converting them to geographic coordinates and outputting GeoJSON.

## Application Scenarios / 应用场景

- Maritime vessel surveillance and illegal fishing monitoring
- Traffic-flow statistics for ports and shipping lanes
- Target screening for maritime search and rescue

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'geopandas' 'shapely' 'scipy'
```

## Usage / 使用方法

### Example 1 (synthetic data, offline)

```bash
python geoskill-sar-ship-detection.py --bbox 121.0 30.0 122.0 31.0 --synthetic --cfar ca --pfa 1e-4 --output-dir ./out
```

### Example 2 (OS-CFAR)

```bash
python geoskill-sar-ship-detection.py --bbox 121.0 30.0 122.0 31.0 --synthetic --cfar os --output-dir ./out
```

### Example 3 (real SAR imagery)

```bash
python geoskill-sar-ship-detection.py --input sar_scene.tif --cfar ca --pfa 1e-5 --output-dir ./out
```

### Example 4 (tuning window parameters)

```bash
python geoskill-sar-ship-detection.py --input sar_scene.tif --guard 3 --background 8 --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `ships.geojson` | GeoJSON | Ship point targets (centroids) + attributes |
| `detection_mask.tif` | GeoTIFF | Detection mask (0/1) |
| `ship_attributes.json` | JSON | Target attribute table (area/peak/bounding box) |
| `detection_count.json` | JSON | Detection count and parameters |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

Local single-band SAR intensity GeoTIFF, or a `--synthetic` simulated sea surface (exponential clutter + bright ship targets).

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode is fully network-free.
- All processing is done locally; no user data is uploaded.

## License / License

MIT

---


<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-sar-ship-detection
description: 'SAR 船舶检测：CA/OS-CFAR 恒虚警检测 + 连通域聚类，从单极化 SAR 强度影像提取船舶目标并输出 GeoJSON 矢量与属性表'
---

# SAR船舶检测 | SAR Ship Detection

从单极化 SAR 强度影像中自动检测海上船舶目标。核心流程：

1. **CFAR 恒虚警检测**：在滑动窗口内用保护带外的背景单元估计局部杂波功率，
   自适应设定门限，在不同海况下保持恒定虚警率。
   - **CA-CFAR**（单元平均）：门限 = α·μ_bg，α = N·(Pfa^(−1/N) − 1)（指数杂波解析解）。
   - **OS-CFAR**（有序统计）：取背景第 k 次序统计量估计杂波，对多目标/杂波边缘更稳健。
2. **连通域聚类**：对超门限像元做连通域标记，提取每个目标的面积、质心、
   峰值强度与外接框，转成地理坐标输出 GeoJSON。

## 应用场景

- 海上船舶监视、非法捕捞监测
- 港口与航道交通流统计
- 海上搜救目标筛查

## 依赖

```bash
pip install 'numpy' 'rasterio' 'geopandas' 'shapely' 'scipy'
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-sar-ship-detection.py --bbox 121.0 30.0 122.0 31.0 --synthetic --cfar ca --pfa 1e-4 --output-dir ./out
```

### 示例 2（OS-CFAR）

```bash
python geoskill-sar-ship-detection.py --bbox 121.0 30.0 122.0 31.0 --synthetic --cfar os --output-dir ./out
```

### 示例 3（真实 SAR 影像）

```bash
python geoskill-sar-ship-detection.py --input sar_scene.tif --cfar ca --pfa 1e-5 --output-dir ./out
```

### 示例 4（调窗口参数）

```bash
python geoskill-sar-ship-detection.py --input sar_scene.tif --guard 3 --background 8 --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `ships.geojson` | GeoJSON | 船舶点目标（质心）+ 属性 |
| `detection_mask.tif` | GeoTIFF | 检测掩膜（0/1） |
| `ship_attributes.json` | JSON | 目标属性表（面积/峰值/外接框） |
| `detection_count.json` | JSON | 检测计数与参数 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地单波段 SAR 强度 GeoTIFF，或 `--synthetic` 模拟海面（指数杂波 + 高亮船舶）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
