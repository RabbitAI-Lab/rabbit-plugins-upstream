---
name: geoskill-carbon-stock-estimation
description: '由 NDVI 幂律异速生长方程估算地上生物量碳，叠加根茎比地下碳与类型化土壤碳密度。Estimates carbon stocks from biomass allometry and soil carbon density. 输出地上碳/土壤碳/总碳三张 GeoTIFF 与汇总 JSON。'
---

# 碳储量估算 | Carbon Stock Estimation

Aboveground biomass is estimated with the power-law allometric equation AGB = scale × max(NDVI, 0)^power and multiplied by the IPCC default carbon fraction of 0.47 to obtain aboveground carbon; belowground carbon = aboveground carbon × root-to-shoot ratio (default 0.30); soil organic carbon is computed from five land cover classes — forest/grassland/cropland/bare land/water — with carbon densities of 60/45/35/15/0 Mg C/ha × pixel area. Total carbon = aboveground carbon × (1 + root-to-shoot ratio) + soil carbon.

Applicable scenarios: regional carbon baseline accounting, dual-carbon (carbon peak and carbon neutrality) target assessment, and measurement of ecological carbon sequestration projects.

## Dependencies / 依赖

```bash
pip install numpy rasterio
```

## Usage / 使用方法

### Example 1: Synthetic Scene with Default Parameters

```bash
python geoskill-carbon-stock-estimation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### Example 2: Real NDVI Raster (band1 Must Be NDVI, Values ≈ −1..1)

```bash
python geoskill-carbon-stock-estimation.py --input ndvi.tif --output-dir ./real
```

### Example 3: Custom Allometric Equation Parameters

```bash
python geoskill-carbon-stock-estimation.py --bbox 116 39 117 40 --synthetic --scale 150 --power 1.8 --output-dir ./tuned
```

### Example 4: Different Region

```bash
python geoskill-carbon-stock-estimation.py --bbox 121 31 122 32 --synthetic --output-dir ./shanghai
```

### Example 5: Quiet Batch Mode

```bash
python geoskill-carbon-stock-estimation.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `agb_carbon.tif` | GeoTIFF (float32) | Aboveground biomass carbon (Mg C/pixel) |
| `soil_carbon.tif` | GeoTIFF (float32) | Soil organic carbon (Mg C/pixel) |
| `total_carbon.tif` | GeoTIFF (float32) | Total carbon stock (Mg C/pixel) |
| `carbon_params.json` | JSON | Carbon fraction, root-to-shoot ratio, and totals of each carbon pool |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/software versions) |

## Data Source / 数据源 / Source

Local GeoTIFF (band1=NDVI, values approximately −1..1; inputs outside this range are rejected with exit code 6);
the carbon fraction (0.47) follows the IPCC 2006 Guidelines for National Greenhouse Gas Inventories, the root-to-shoot ratio follows the global meta-analysis of Mokany et al. 2006, and the soil carbon densities are order-of-magnitude defaults for the 0–30 cm soil layer (IPCC reference stock convention); synthetic mode generates data locally with no external data source.

## Limitations / 局限（诚实声明）

- `AGB = scale × NDVI^power` is an empirical power-law model; scale/power must be calibrated by region and vegetation type, and the default values (200 / 2.0) are intended for screening-level estimates only and cannot be used directly for project-level accounting (MRV).
- The 0.30 root-to-shoot ratio is a global default: in reality it varies by biome (tropical forests ~0.24, shrublands/grasslands higher), and fine-scale accounting should replace it with biome-specific values.
- The soil carbon densities (forest 60 / grassland 45 / cropland 35 / bare land 15 / water 0 Mg C/ha) are fixed defaults that are not refined by climate zone or soil type; surface litter and deadwood carbon pools are not included.

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default; makes no network requests
- `--synthetic` mode reads no external data
- All computation is performed locally; no user data is uploaded

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-carbon-stock-estimation
description: '由 NDVI 幂律异速生长方程估算地上生物量碳，叠加根茎比地下碳与类型化土壤碳密度。Estimates carbon stocks from biomass allometry and soil carbon density. 输出地上碳/土壤碳/总碳三张 GeoTIFF 与汇总 JSON。'
---

# 碳储量估算 | Carbon Stock Estimation

地上生物量按幂律异速方程 AGB = scale × max(NDVI,0)^power 估算，乘以 IPCC 默认含碳系数 0.47 得地上碳；地下碳 = 地上碳 × 根茎比（默认 0.30）；土壤有机碳按林/草/耕/裸/水五类碳密度（60/45/35/15/0 Mg C/ha）× 像元面积。总碳 = 地上碳×(1+根茎比) + 土壤碳。

适用场景：区域碳本底核算、双碳目标评估、生态固碳项目计量。

## 依赖

```bash
pip install numpy rasterio
```

## 使用方法

### 示例 1：合成场景默认参数

```bash
python geoskill-carbon-stock-estimation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### 示例 2：真实 NDVI 栅格（band1 必须为 NDVI，取值约 −1..1）

```bash
python geoskill-carbon-stock-estimation.py --input ndvi.tif --output-dir ./real
```

### 示例 3：自定义异速方程参数

```bash
python geoskill-carbon-stock-estimation.py --bbox 116 39 117 40 --synthetic --scale 150 --power 1.8 --output-dir ./tuned
```

### 示例 4：不同区域

```bash
python geoskill-carbon-stock-estimation.py --bbox 121 31 122 32 --synthetic --output-dir ./shanghai
```

### 示例 5：静默批量

```bash
python geoskill-carbon-stock-estimation.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `agb_carbon.tif` | GeoTIFF (float32) | 地上生物量碳（Mg C/像元） |
| `soil_carbon.tif` | GeoTIFF (float32) | 土壤有机碳（Mg C/像元） |
| `total_carbon.tif` | GeoTIFF (float32) | 总碳储量（Mg C/像元） |
| `carbon_params.json` | JSON | 含碳系数、根茎比、各碳库总量 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

本地 GeoTIFF（band1=NDVI，取值约 −1..1；超出该范围的输入会被拒绝，exit 6）；
含碳系数（0.47）参考 IPCC 2006 清单指南，根茎比参考 Mokany et al. 2006 全球元分析，
土壤碳密度为 0–30 cm 土层的量级默认值（IPCC 参考储量口径）；合成模式本地生成，无外部数据源。

## 局限（诚实声明）

- `AGB = scale × NDVI^power` 为经验幂律模型，scale/power 需按区域/植被类型标定，
  默认值（200 / 2.0）仅作筛查级估算，不能直接用于项目计量（MRV）。
- 根茎比 0.30 为全球通用值：实际随生物区变化（热带林 ~0.24，灌丛/草地更高），
  精细核算应替换为生物区特异值。
- 土壤碳密度（林 60 / 草 45 / 耕 35 / 裸 15 / 水 0 Mg C/ha）为固定默认值，
  未按气候区/土类细化；地表凋落物与死木碳库未计入。

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
