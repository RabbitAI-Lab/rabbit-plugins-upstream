---
name: geoskill-ecosystem-services-valuation
description: '用当量因子法评估供给、调节、支持、文化四类生态系统服务价值。Estimates four ecosystem service values with a simplified InVEST plus equivalent-factor method. 输出四类服务价值 GeoTIFF 与总量 JSON。'
---

# 生态系统服务评估 | Ecosystem Services Valuation

Based on the equivalent-factor table of Xie Gaodi et al. (1 equivalent ≈ national mean grain production value of 3,000 CNY/ha/yr): five LULC classes — forest, grassland, cropland, water, and built-up land — are first derived from NDVI thresholds; the class × service equivalent coefficient is then multiplied by the pixel area to produce annual value-density rasters and regional totals for the four service categories: provisioning, regulating, supporting, and cultural.

Use cases: ecological asset accounting, Gross Ecosystem Product (GEP) estimation, and calculation of requisition–compensation balance and ecological compensation standards.

## Dependencies / 依赖

```bash
pip install numpy rasterio geopandas shapely
```

## Usage / 使用方法

### Example 1: synthetic NDVI scenario

```bash
python geoskill-ecosystem-services-valuation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### Example 2: real NDVI raster

```bash
python geoskill-ecosystem-services-valuation.py --input ndvi.tif --output-dir ./real
```

### Example 3: different region (Shanghai)

```bash
python geoskill-ecosystem-services-valuation.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./shanghai
```

### Example 4: silent batch run

```bash
python geoskill-ecosystem-services-valuation.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

### Example 5: tiny region for quick validation

```bash
python geoskill-ecosystem-services-valuation.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./tiny
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `value_provisioning.tif` | GeoTIFF (float32) | Provisioning service value (CNY/yr/pixel) |
| `value_regulating.tif` | GeoTIFF (float32) | Regulating service value (CNY/yr/pixel) |
| `value_supporting.tif` | GeoTIFF (float32) | Supporting service value (CNY/yr/pixel) |
| `value_cultural.tif` | GeoTIFF (float32) | Cultural service value (CNY/yr/pixel) |
| `service_value_params.json` | JSON | Pixel area, per-service totals, LULC pixel counts |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/software versions) |

## Data Source / 数据源 / Source

Local GeoTIFF (band1 = NDVI); the equivalent-factor table follows the China ecosystem service value equivalent factors published by Xie Gaodi et al. (2015); synthetic mode generates data locally with no external data sources.

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default and makes no network requests
- `--synthetic` mode reads no external data
- All computation is done locally; user data is never uploaded

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
