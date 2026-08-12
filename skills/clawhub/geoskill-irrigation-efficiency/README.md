# Irrigation Efficiency Assessment (geoskill-irrigation-efficiency)

> Computes irrigation water demand from crop evapotranspiration and effective precipitation, and assesses the spatial distribution of irrigation efficiency

---

## 1. Overview

This skill computes the net irrigation water demand from crop evapotranspiration (ET) and effective precipitation, and assesses the spatial distribution of field irrigation efficiency. It suits scenarios such as irrigation-district water management, water allocation optimization, and drought/water-shortage assessment. Core algorithms: **crop evapotranspiration** ET = PET × Kc, where Kc is looked up from the FAO-56 mid-season crop coefficient table by crop type; **effective precipitation** converts total rainfall into the portion available to the crop root zone, supporting two methods — `fixed` (fixed coefficient) and `usda` (USDA-SCS empirical formula, with lower utilization for heavy rainfall); **net irrigation water demand** demand = max(ET − Pe, 0); **irrigation efficiency** efficiency = clip(demand/applied, 0, 1), with an additional water deficit deficit = max(demand − applied, 0) when actual application is insufficient.

## 2. Features

This skill computes the net irrigation water demand from crop evapotranspiration (ET) and effective precipitation, and assesses the spatial distribution of field irrigation efficiency. It suits scenarios such as irrigation-district water management, water allocation optimization, and drought/water-shortage assessment. Core algorithms: **crop evapotranspiration** ET = PET × Kc, where Kc is looked up from the FAO-56 mid-season crop coefficient table by crop type; **effective precipitation** converts total rainfall into the portion available to the crop root zone, supporting two methods — `fixed` (fixed coefficient) and `usda` (USDA-SCS empirical formula, with lower utilization for heavy rainfall); **net irrigation water demand** demand = max(ET − Pe, 0); **irrigation efficiency** efficiency = clip(demand/applied, 0, 1), with an additional water deficit deficit = max(demand − applied, 0) when actual application is insufficient.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-irrigation-efficiency.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `irrigation_demand.tif` | GeoTIFF | Net irrigation demand raster (mm) |
| `irrigation_efficiency.tif` | GeoTIFF | Irrigation efficiency raster (0–1) |
| `water_deficit.tif` | GeoTIFF | Irrigation deficit raster (mm) |
| `irrigation_report.json` | JSON | Regional mean statistics (ET/precipitation/demand/efficiency/deficit) |
| `output-manifest.json` | JSON | Run manifest |

## 6. Technical Principle

(See SKILL.md for details)

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 灌溉效率评估（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-irrigation-efficiency
description: '基于作物蒸散发与有效降水计算灌溉需水量，并评估灌溉效率空间分布'
---

# 灌溉效率评估 | Irrigation Efficiency Assessment

本 skill 基于作物蒸散发（ET）与有效降水计算净灌溉需水量，并评估田间灌溉效率的空间分布，适用于灌区用水管理、配水优化、干旱缺水评估等场景。

核心算法：**作物蒸散发** ET = PET × Kc，Kc 由作物类型查 FAO-56 中期作物系数表；**有效降水**把总降雨折算为作物根区可利用部分，支持 `fixed`（固定系数）与 `usda`（USDA-SCS 经验式，强降雨利用率更低）两种方法；**净灌溉需水量** demand = max(ET − Pe, 0)；**灌溉效率** efficiency = clip(demand/applied, 0, 1)，实灌不足时另计缺水亏缺 deficit = max(demand − applied, 0)。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-irrigation-efficiency.py --bbox 116.0 39.0 117.0 40.0
```

### 示例 1（合成数据，离线）

```bash
python geoskill-irrigation-efficiency.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（USDA 有效降水方法）

```bash
python geoskill-irrigation-efficiency.py --bbox 116 39 117 40 --synthetic --eff-method usda --output-dir ./out
```

### 示例 3（自定义有效降水系数）

```bash
python geoskill-irrigation-efficiency.py --bbox 121 31 122 32 --synthetic --eff-coeff 0.65 --quiet
```

### 示例 4（真实栅格，band1=作物ET, band2=总降水, band3=实灌量）

```bash
python geoskill-irrigation-efficiency.py --input scene.tif --eff-method fixed --output-dir ./out
```

### 示例 5（干旱区高蒸散发场景）

```bash
python geoskill-irrigation-efficiency.py --bbox 87 43 88 44 --synthetic --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `irrigation_demand.tif` | GeoTIFF | 净灌溉需水量栅格（mm） |
| `irrigation_efficiency.tif` | GeoTIFF | 灌溉效率栅格（0–1） |
| `water_deficit.tif` | GeoTIFF | 灌溉亏缺量栅格（mm） |
| `irrigation_report.json` | JSON | 区域均值统计（ET/降水/需水/效率/亏缺） |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- `--input`：本地 GeoTIFF（band1 = 作物 ET，band2 = 总降水，band3 = 实灌量）。
- `--synthetic`：生长季尺度的 PET/作物/降水/实灌量栅格，完全离线。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
