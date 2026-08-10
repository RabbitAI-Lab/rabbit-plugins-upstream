# Water Balance Calculation (geoskill-water-balance-calculation)

> Per-pixel water balance computation P = ET + Q + ΔS with closure residual assessment. Outputs per-component/closure-residual GeoTIFFs + a report JSON.

---

## 1. Overview

Per-pixel water balance computation, with the core equation: P = ET + Q + ΔS, i.e. **precipitation = evapotranspiration + runoff + storage change**. Each component is computed independently per pixel, and the closure residual is derived as: residual = P − ET − Q − ΔS. The residual is 0 under ideal closure; real observation data contain residuals because each component comes from a different data source (precipitation gauge networks, remote-sensing evapotranspiration products, hydrological model runoff, gravity-satellite storage change). This skill uses the relative closure error (mean|residual| / mean P) to quantify data consistency, a common approach for diagnosing the quality of multi-source hydrological data and identifying systematic biases. It is suitable for basin water balance diagnosis, cross-validation of remote-sensing products, and quality assessment before data assimilation. The `--synthetic` mode generates a complete, physically closed dataset (ET≈0.45P, Q≈0.30P, ΔS as the closing residual, with an added observational perturbation of std≈3 mm), so the workflow can be verified without network access or real data; the relative closure error of synthetic data should be < 2%.

## 2. Features

Per-pixel water balance computation, with the core equation: P = ET + Q + ΔS, i.e. **precipitation = evapotranspiration + runoff + storage change**. Each component is computed independently per pixel, and the closure residual is derived as: residual = P − ET − Q − ΔS. The residual is 0 under ideal closure; real observation data contain residuals because each component comes from a different data source (precipitation gauge networks, remote-sensing evapotranspiration products, hydrological model runoff, gravity-satellite storage change). This skill uses the relative closure error (mean|residual| / mean P) to quantify data consistency, a common approach for diagnosing the quality of multi-source hydrological data and identifying systematic biases. It is suitable for basin water balance diagnosis, cross-validation of remote-sensing products, and quality assessment before data assimilation. The `--synthetic` mode generates a complete, physically closed dataset (ET≈0.45P, Q≈0.30P, ΔS as the closing residual, with an added observational perturbation of std≈3 mm), so the workflow can be verified without network access or real data; the relative closure error of synthetic data should be < 2%.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-water-balance-calculation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `balance_components.tif` | GeoTIFF (float32, 4 bands) | Component raster: B1=P, B2=ET, B3=Q, B4=ΔS, EPSG:4326 |
| `closure_residual.tif` | GeoTIFF (float32) | Closure residual P−ET−Q−ΔS |
| `water_balance_report.json` | JSON | Per-component means, closure residual mean/std, relative closure error, volumetric quantities |
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

# 水量平衡计算（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-water-balance-calculation
description: '逐像元水量平衡计算 P = ET + Q + ΔS，评估闭合差。Per-pixel water balance computation P = ET + Q + ΔS with closure residual assessment. 输出各分量/闭合差 GeoTIFF + 报告 JSON。'
---

# 水量平衡计算 | Water Balance Calculation

逐像元水量平衡计算，核心方程：

    P = ET + Q + ΔS

即 **降水 = 蒸散发 + 径流 + 蓄水变化**。对每个像元独立计算各分量，并求闭合差
（closure residual）：

    residual = P − ET − Q − ΔS

理想闭合时残差为 0；真实观测数据因各分量来自不同数据源（降水站网、遥感蒸散发
产品、水文模型径流、重力卫星蓄水变化）而存在残差。本 skill 用相对闭合误差
（mean|residual| / mean P）量化数据一致性，是诊断多源水文数据质量、识别系统
偏差的常用手段，适用于流域水平衡诊断、遥感产品交叉验证、数据同化前的质量评估。

支持 `--synthetic` 模式生成物理闭合（ET≈0.45P、Q≈0.30P、ΔS 为闭合残值，
再叠加 std≈3 mm 的观测扰动）的完整数据集，无需网络和真实数据即可验证流程，
合成数据的相对闭合误差应 < 2%。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-water-balance-calculation.py --bbox 116.0 39.0 117.0 40.0 --output-dir ./output
```

### 示例 1：合成数据水量平衡

```bash
python geoskill-water-balance-calculation.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --synthetic \
    --output-dir ./wb_syn
```

### 示例 2：真实降水栅格（演示模式）

```bash
python geoskill-water-balance-calculation.py \
    --input precip_annual.tif \
    --output-dir ./wb_real
```

（以输入降水为 P，其余分量按经验比例合成以演示流程。）

### 示例 3：不同区域

```bash
python geoskill-water-balance-calculation.py --bbox 121 31 122 32 --synthetic --output-dir ./wb_sh --quiet
```

### 示例 4：极小区域

```bash
python geoskill-water-balance-calculation.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./wb_tiny --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `balance_components.tif` | GeoTIFF (float32, 4 bands) | 分量栅格：B1=P, B2=ET, B3=Q, B4=ΔS，EPSG:4326 |
| `closure_residual.tif` | GeoTIFF (float32) | 闭合差 P−ET−Q−ΔS |
| `water_balance_report.json` | JSON | 各分量均值、闭合差均值/标准差、相对闭合误差、体积量 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

- **降水 P**：本地 GeoTIFF，或来自 CHIRPS / GPM / 地面站点
- **ET / Q / ΔS**：合成模式生成；真实应用可接入 MODIS ET、水文模型、GRACE 等
- **合成模式**：本地生成，无外部数据源

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
