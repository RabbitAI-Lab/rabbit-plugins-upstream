# Carbon Stock Estimation (geoskill-carbon-stock-estimation)

> Estimates aboveground biomass carbon from a power-law allometric equation of NDVI, adding belowground carbon via the root-to-shoot ratio and typed soil carbon densities. Estimates carbon stocks from biomass allometry and soil carbon density. Outputs three GeoTIFFs (aboveground carbon/soil carbon/total carbon) and a summary JSON.

---

## 1. Overview

Aboveground biomass is estimated with the power-law allometric equation AGB = scale × max(NDVI,0)^power and multiplied by the IPCC default carbon fraction of 0.47 to obtain aboveground carbon; belowground carbon = aboveground carbon × root-to-shoot ratio (default 0.30); soil organic carbon is computed as carbon density per land-cover type (forest/grassland/cropland/bare/water: 60/45/35/15/0 Mg C/ha) × pixel area. Total carbon = aboveground carbon × (1 + root-to-shoot ratio) + soil carbon. Applicable scenarios: regional carbon baseline accounting, dual-carbon goal assessment, and measurement of ecological carbon sequestration projects.

## 2. Features

Aboveground biomass is estimated with the power-law allometric equation AGB = scale × max(NDVI,0)^power and multiplied by the IPCC default carbon fraction of 0.47 to obtain aboveground carbon; belowground carbon = aboveground carbon × root-to-shoot ratio (default 0.30); soil organic carbon is computed as carbon density per land-cover type (forest/grassland/cropland/bare/water: 60/45/35/15/0 Mg C/ha) × pixel area. Total carbon = aboveground carbon × (1 + root-to-shoot ratio) + soil carbon. Applicable scenarios: regional carbon baseline accounting, dual-carbon goal assessment, and measurement of ecological carbon sequestration projects.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-carbon-stock-estimation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `agb_carbon.tif` | GeoTIFF (float32) | Aboveground biomass carbon (Mg C/pixel) |
| `soil_carbon.tif` | GeoTIFF (float32) | Soil organic carbon (Mg C/pixel) |
| `total_carbon.tif` | GeoTIFF (float32) | Total carbon stock (Mg C/pixel) |
| `carbon_params.json` | JSON | Carbon fraction, root-to-shoot ratio, totals per carbon pool |
| `output-manifest.json` | JSON | Run manifest (input/output/QA/software versions) |


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

# 碳储量估算（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

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
