---
name: geoskill-lidar-coastal-erosion
description: '两期LiDAR点云/DSM差分计算海岸侵蚀堆积量，提取海岸线并用EPR端点变化率量化后退速率'
---

# LiDAR海岸侵蚀分析 | LiDAR Coastal Erosion

(Fill in 2–3 paragraphs introducing features, application scenarios, and core algorithms.)

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy' 'geopandas' 'shapely'
```

## Usage / 使用方法

### Basic usage

```bash
python geoskill-lidar-coastal-erosion.py --bbox 116.0 39.0 117.0 40.0 [other parameters]
```

### Example 1 (synthetic data, offline)

```bash
python geoskill-lidar-coastal-erosion.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Examples 2-5

(Add at least 4 real-world usage examples.)

## Output / 输出

| File | Format | Description |
|---|---|---|
| `result.tif` | GeoTIFF | Primary output |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

(Describe the data source: free satellite data / local input / synthetic.)

## Privacy / 隐私声明 / Privacy

- Offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; no user data is uploaded.

## License / License

MIT

---


<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-lidar-coastal-erosion
description: '两期LiDAR点云/DSM差分计算海岸侵蚀堆积量，提取海岸线并用EPR端点变化率量化后退速率'
---

# LiDAR海岸侵蚀分析 | LiDAR Coastal Erosion

（在此填写 2-3 段中文介绍：功能、应用场景、核心算法。）

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy' 'geopandas' 'shapely'
```

## 使用方法

### 基本用法

```bash
python geoskill-lidar-coastal-erosion.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例 1（合成数据，离线）

```bash
python geoskill-lidar-coastal-erosion.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2-5

（补充至少 4 个真实用法示例。）

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `result.tif` | GeoTIFF | 主产物 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

（说明数据来源：免费卫星数据 / 本地输入 / 合成。）

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
