# Wetland Mapping (geoskill-wetland-mapping)

> Classifies wetland types and computes area statistics with rule-based thresholds fusing NDWI/MNDWI, NDVI, topographic depressions, and SAR backscatter

---

## 1. Overview

Multi-source fused wetland type mapping. Combines four co-registered raster layers (band order: NDWI/MNDWI, NDVI, DEM, SAR backscatter σ⁰) and classifies every pixel into open water, swamp, mudflat, or non-wetland via a physical rule-based decision tree, with priority water > swamp > mudflat. Example criteria: open water requires high NDWI and very low SAR (specular reflection from the water surface); swamp requires high NDVI (wetland vegetation), low-lying terrain, and relatively low SAR; mudflat requires low NDVI, moist conditions (relatively high NDWI), low-lying terrain, and relatively low SAR. The DEM is automatically normalized into a lowness index (0 = lowest). Typical applications: wetland resource baseline surveys, coastal/lakeshore wetland mapping, and mangrove and swamp distribution inventories. The synthetic mode generates multi-source data containing all four wetland classes, with an overall classification accuracy >0.95 against the injected ground truth.

## 2. Features

Multi-source fused wetland type mapping. Combines four co-registered raster layers (band order: NDWI/MNDWI, NDVI, DEM, SAR backscatter σ⁰) and classifies every pixel into open water, swamp, mudflat, or non-wetland via a physical rule-based decision tree, with priority water > swamp > mudflat. Example criteria: open water requires high NDWI and very low SAR (specular reflection from the water surface); swamp requires high NDVI (wetland vegetation), low-lying terrain, and relatively low SAR; mudflat requires low NDVI, moist conditions (relatively high NDWI), low-lying terrain, and relatively low SAR. The DEM is automatically normalized into a lowness index (0 = lowest). Typical applications: wetland resource baseline surveys, coastal/lakeshore wetland mapping, and mangrove and swamp distribution inventories. The synthetic mode generates multi-source data containing all four wetland classes, with an overall classification accuracy >0.95 against the injected ground truth.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-wetland-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out
```

## 4. CLI Parameters

Run `python <skill>.py --help` for the full list. Common parameters:

| Parameter | Type | Description |
|---|---|---|
| `--bbox` | `float[4]` | WGS84 bounding box `min_lon min_lat max_lon max_lat` |
| `--input` | `path` | Local input file (GeoJSON/GeoTIFF/etc.) |
| `--output-dir` | `path` | Output directory (default `./output`) |
| `--synthetic` | `flag` | Use synthetic data instead of real input |
| `--quiet` | `flag` | Suppress non-essential stdout |

## 5. Input / Output

| File | Format | Description |
|---|---|---|
| `wetland_class.tif` | GeoTIFF (int32) | 0=non-wetland, 1=water, 2=swamp, 3=mudflat |
| `area_stats.json` | JSON | Per-class area/percentage + total wetland area |
| `output-manifest.json` | JSON | Run manifest (with accuracy QA in synthetic mode) |

## 6. Technical Principle

(see SKILL.md for details)

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 湿地制图（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-wetland-mapping
description: '融合 NDWI/MNDWI、NDVI、地形低洼与 SAR 后向散射，规则阈值分类湿地类型并统计面积'
---

# 湿地制图 | Wetland Mapping

多源融合的湿地类型制图。组合四个共配准栅格层（波段顺序：NDWI/MNDWI、
NDVI、DEM、SAR 后向散射 σ⁰），按物理规则决策树把每个像元分为
开放水域（water）、沼泽（swamp）、滩涂（mudflat）与非湿地（non_wetland），
优先级 water > swamp > mudflat。

判据示例：开放水域要求 NDWI 高且 SAR 极低（水面镜面反射）；沼泽要求
NDVI 高（湿生植被）、地形低洼且 SAR 偏低；滩涂要求 NDVI 低、湿润
（NDWI 偏高）、低洼且 SAR 偏低。DEM 自动归一化为低洼度（0=最低）。

典型应用：湿地资源本底调查、滨海/湖滨湿地制图、红树林与沼泽分布摸底。
合成模式生成含四类湿地的多源数据，分类总体精度与注入真值 >0.95。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-wetland-mapping.py --bbox 116.0 39.0 117.0 40.0
```

### 示例 1（合成数据，离线）

```bash
python geoskill-wetland-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（读取本地 4 波段融合栅格）

```bash
python geoskill-wetland-mapping.py --input fused_4band.tif --output-dir ./out
```

输入波段顺序：`[NDWI, NDVI, DEM, SAR(dB)]`；DEM 会被自动归一化到 [0,1]。

### 示例 3（不同区域 + 静默）

```bash
python geoskill-wetland-mapping.py --bbox 121.0 31.0 122.0 32.0 --synthetic --quiet --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `wetland_class.tif` | GeoTIFF (int32) | 0=非湿地, 1=水域, 2=沼泽, 3=滩涂 |
| `area_stats.json` | JSON | 逐类面积/占比 + 湿地总量 |
| `output-manifest.json` | JSON | 运行清单（合成模式含精度 QA） |

## 数据源 / Source

- 本地 4 波段 GeoTIFF（NDWI/NDVI/DEM/SAR，共配准）；
- `--synthetic` 离线合成多源场景（无需网络、无需账号）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
