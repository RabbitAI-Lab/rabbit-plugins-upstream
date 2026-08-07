---
name: geoskill-water-purification-mapping
description: '简化 InVEST Budyko 水量平衡计算产水量，叠加 NDVI 调制的植被截留系数得水源涵养量，并估算养分截留净化量。Maps water retention and purification with a simplified InVEST water yield model. 输出产水/涵养/净化三张 GeoTIFF。'
---

# 水源涵养/净化功能制图 | Water Purification Mapping

Water yield is computed with a Budyko-style water balance Y = P - AET, where AET/P = 1 + φ - (1+φ^ω)^(1/ω), φ = ET0/P is the dryness index, and ω is the soil-water parameter (default 1.5). Water retention = water yield × NDVI-modulated vegetation interception coefficient (saturating type, capped at 0.85); water purification estimates nitrogen retention as nutrient load × NDVI-modulated interception efficiency (default 0.65).

Use cases: water-retention function assessment, watershed water-purification service accounting, and ecological conservation red line delineation.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy
```

## Usage / 使用方法

### Example 1: Synthetic Climate/Soil/Vegetation Scenario

```bash
python geoskill-water-purification-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### 示例 2：真实 5 波段输入（precip,et0,awc,ndvi,n_load）

```bash
python geoskill-water-purification-mapping.py --input water_inputs.tif --output-dir ./real
```

### 示例 3：调整 Budyko ω 参数

```bash
python geoskill-water-purification-mapping.py --bbox 116 39 117 40 --synthetic --omega 2.0 --output-dir ./tuned
```

### Example 4: Different Regions

```bash
python geoskill-water-purification-mapping.py --bbox 121 31 122 32 --synthetic --output-dir ./shanghai
```

### Example 5: Silent Batch Mode

```bash
python geoskill-water-purification-mapping.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `water_yield.tif` | GeoTIFF (float32) | Water yield (mm/yr), EPSG:4326 |
| `water_retention.tif` | GeoTIFF (float32) | Water retention (mm/yr) |
| `nutrient_retention.tif` | GeoTIFF (float32) | Nitrogen retention (kg/ha/yr) |
| `water_purification_params.json` | JSON | ω parameter and per-product means/totals |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/software versions) |

## Data Source / 数据源 / Source

Local GeoTIFF (optional 5-band factor input); the Budyko water balance is a public hydrological model; synthetic mode is generated locally with no external data source.

## Privacy / 隐私声明 / Privacy

- Fully offline by default; no network requests are made
- `--synthetic` mode reads no external data
- All computation is done locally; no user data is uploaded

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-water-purification-mapping
description: '简化 InVEST Budyko 水量平衡计算产水量，叠加 NDVI 调制的植被截留系数得水源涵养量，并估算养分截留净化量。Maps water retention and purification with a simplified InVEST water yield model. 输出产水/涵养/净化三张 GeoTIFF。'
---

# 水源涵养/净化功能制图 | Water Purification Mapping

产水量用 Budyko 风格水量平衡 Y = P - AET，其中 AET/P = 1 + φ - (1+φ^ω)^(1/ω)，φ = ET0/P 为干燥指数，ω 为土壤水分参数（默认 1.5）。水源涵养量 = 产水量 × NDVI 调制的植被截留系数（饱和型，上限 0.85）；水质净化用养分负荷 × NDVI 调制截留效率（默认 0.65）估算氮截留量。

适用场景：水源涵养功能评估、流域水质净化服务核算、生态保护红线划定。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 示例 1：合成气候/土壤/植被场景

```bash
python geoskill-water-purification-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### 示例 2：真实 5 波段输入（precip,et0,awc,ndvi,n_load）

```bash
python geoskill-water-purification-mapping.py --input water_inputs.tif --output-dir ./real
```

### 示例 3：调整 Budyko ω 参数

```bash
python geoskill-water-purification-mapping.py --bbox 116 39 117 40 --synthetic --omega 2.0 --output-dir ./tuned
```

### 示例 4：不同区域

```bash
python geoskill-water-purification-mapping.py --bbox 121 31 122 32 --synthetic --output-dir ./shanghai
```

### 示例 5：静默批量

```bash
python geoskill-water-purification-mapping.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `water_yield.tif` | GeoTIFF (float32) | 产水量（mm/yr），EPSG:4326 |
| `water_retention.tif` | GeoTIFF (float32) | 水源涵养量（mm/yr） |
| `nutrient_retention.tif` | GeoTIFF (float32) | 氮截留量（kg/ha/yr） |
| `water_purification_params.json` | JSON | ω 参数与各产物均值/总量 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

本地 GeoTIFF（5 波段因子输入，可选）；Budyko 水量平衡为公开水文模型；合成模式本地生成，无外部数据源。

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
