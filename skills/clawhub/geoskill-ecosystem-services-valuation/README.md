# Ecosystem Services Valuation (geoskill-ecosystem-services-valuation)

> Assesses provisioning, regulating, supporting, and cultural ecosystem service values using the equivalent-factor method. Outputs GeoTIFFs of the four service values and a total-value JSON.

---

## 1. Overview

Based on the equivalent-factor table of Xie Gaodi et al. (1 equivalent ≈ national mean grain output value of 3000 CNY/ha/yr): five LULC classes (forest, grassland, cropland, water, and built-up) are first retrieved via NDVI thresholds; the equivalent coefficient per class × service is then multiplied by pixel area to obtain annual value-density rasters and regional totals for the provisioning, regulating, supporting, and cultural services. Use cases: ecological asset accounting, GEP estimation, and calibration of occupation–compensation balance and ecological compensation standards.

## 2. Features

Based on the equivalent-factor table of Xie Gaodi et al. (1 equivalent ≈ national mean grain output value of 3000 CNY/ha/yr): five LULC classes (forest, grassland, cropland, water, and built-up) are first retrieved via NDVI thresholds; the equivalent coefficient per class × service is then multiplied by pixel area to obtain annual value-density rasters and regional totals for the provisioning, regulating, supporting, and cultural services. Use cases: ecological asset accounting, GEP estimation, and calibration of occupation–compensation balance and ecological compensation standards.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-ecosystem-services-valuation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `value_provisioning.tif` | GeoTIFF (float32) | Provisioning service value (CNY/yr/pixel) |
| `value_regulating.tif` | GeoTIFF (float32) | Regulating service value (CNY/yr/pixel) |
| `value_supporting.tif` | GeoTIFF (float32) | Supporting service value (CNY/yr/pixel) |
| `value_cultural.tif` | GeoTIFF (float32) | Cultural service value (CNY/yr/pixel) |
| `service_value_params.json` | JSON | Pixel area, total value per service, LULC pixel counts |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/software versions) |

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

# 生态系统服务评估（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-ecosystem-services-valuation
description: '用当量因子法评估供给、调节、支持、文化四类生态系统服务价值。Estimates four ecosystem service values with a simplified InVEST plus equivalent-factor method. 输出四类服务价值 GeoTIFF 与总量 JSON。'
---

# 生态系统服务评估 | Ecosystem Services Valuation

基于谢高地等当量因子表（1 当量 ≈ 全国均值粮食产值 3000 元/ha/yr）：先从 NDVI 阈值反演林/草/耕/水/建设用地五类 LULC，再按类别×服务的当量系数乘以像元面积，得到供给、调节、支持、文化四类服务的年价值密度栅格与区域总量。

适用场景：生态资产核算、GEP 估算、占补平衡与生态补偿标准测算。

## 依赖

```bash
pip install numpy rasterio geopandas shapely
```

## 使用方法

### 示例 1：合成 NDVI 场景

```bash
python geoskill-ecosystem-services-valuation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### 示例 2：真实 NDVI 栅格

```bash
python geoskill-ecosystem-services-valuation.py --input ndvi.tif --output-dir ./real
```

### 示例 3：不同区域（上海）

```bash
python geoskill-ecosystem-services-valuation.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./shanghai
```

### 示例 4：静默批量

```bash
python geoskill-ecosystem-services-valuation.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

### 示例 5：极小区域快速验证

```bash
python geoskill-ecosystem-services-valuation.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./tiny
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `value_provisioning.tif` | GeoTIFF (float32) | 供给服务价值（元/yr/像元） |
| `value_regulating.tif` | GeoTIFF (float32) | 调节服务价值（元/yr/像元） |
| `value_supporting.tif` | GeoTIFF (float32) | 支持服务价值（元/yr/像元） |
| `value_cultural.tif` | GeoTIFF (float32) | 文化服务价值（元/yr/像元） |
| `service_value_params.json` | JSON | 像元面积、各服务总量、LULC 像元计数 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

本地 GeoTIFF（band1=NDVI）；当量因子表参考谢高地等（2015）公开发表的中国生态系统服务价值当量因子；合成模式本地生成，无外部数据源。

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
