---
name: geoskill-sar-flood-mapping
description: '基于 SAR 低后向散射特性的洪水范围制图：Otsu 阈值分割低 σ⁰ 水体 + 形态学去噪 + 可选 DEM 坡度排除，并矢量化为 GeoJSON。SAR flood extent mapping via Otsu thresholding of low backscatter, morphological cleanup and vectorization. 输出洪水二值 GeoTIFF + 面积统计 JSON + 范围 GeoJSON。'
---

# SAR洪水制图 | SAR Flood Mapping

(Fill in 2-3 paragraphs of Chinese introduction here: features, application scenarios, core algorithm.)

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'geopandas' 'shapely' 'scipy'
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-sar-flood-mapping.py --bbox 116.0 39.0 117.0 40.0 [other options]
```

### Example 1 (synthetic data, offline)

```bash
python geoskill-sar-flood-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Examples 2-5

(Add at least 4 real usage examples.)

## Output / 输出

| File | Format | Description |
|---|---|---|
| `result.tif` | GeoTIFF | Primary output |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

(Describe the data source: free satellite data / local input / synthetic.)

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode is fully network-free.
- All processing is done locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-sar-flood-mapping
description: '基于 SAR 低后向散射特性的洪水范围制图：Otsu 阈值分割低 σ⁰ 水体 + 形态学去噪 + 可选 DEM 坡度排除，并矢量化为 GeoJSON。SAR flood extent mapping via Otsu thresholding of low backscatter, morphological cleanup and vectorization. 输出洪水二值 GeoTIFF + 面积统计 JSON + 范围 GeoJSON。'
---

# SAR洪水制图 | SAR Flood Mapping

（在此填写 2-3 段中文介绍：功能、应用场景、核心算法。）

## 依赖

```bash
pip install 'numpy' 'rasterio' 'geopandas' 'shapely' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-sar-flood-mapping.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例 1（合成数据，离线）

```bash
python geoskill-sar-flood-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
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
