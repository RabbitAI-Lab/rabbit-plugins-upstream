---
name: geoskill-irrigation-efficiency
description: '基于作物蒸散发与有效降水计算灌溉需水量，并评估灌溉效率空间分布'
---

# 灌溉效率评估 | Irrigation Efficiency Assessment

This skill computes net irrigation water demand from crop evapotranspiration (ET) and effective precipitation, and assesses the spatial distribution of field irrigation efficiency. It suits use cases such as irrigation district water management, water allocation optimization, and drought/deficit assessment.

Core algorithm: **crop evapotranspiration** ET = PET × Kc, where Kc is looked up from the FAO-56 mid-season crop coefficient table by crop type; **effective precipitation** converts total rainfall into the fraction available to the crop root zone, supporting both `fixed` (fixed coefficient) and `usda` (USDA-SCS empirical method, with lower utilization under heavy rainfall); **net irrigation demand** demand = max(ET − Pe, 0); **irrigation efficiency** efficiency = clip(demand/applied, 0, 1); when applied water is insufficient, an additional water deficit deficit = max(demand − applied, 0) is computed.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## Usage / 使用方法

### Basic usage

```bash
python geoskill-irrigation-efficiency.py --bbox 116.0 39.0 117.0 40.0
```

### Example 1 (synthetic data, offline)

```bash
python geoskill-irrigation-efficiency.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (USDA effective precipitation method)

```bash
python geoskill-irrigation-efficiency.py --bbox 116 39 117 40 --synthetic --eff-method usda --output-dir ./out
```

### Example 3 (custom effective precipitation coefficient)

```bash
python geoskill-irrigation-efficiency.py --bbox 121 31 122 32 --synthetic --eff-coeff 0.65 --quiet
```

### Example 4 (real raster: band1 = crop ET, band2 = total precipitation, band3 = applied irrigation)

```bash
python geoskill-irrigation-efficiency.py --input scene.tif --eff-method fixed --output-dir ./out
```

### Example 5 (arid region with high evapotranspiration)

```bash
python geoskill-irrigation-efficiency.py --bbox 87 43 88 44 --synthetic --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `irrigation_demand.tif` | GeoTIFF | Net irrigation demand raster (mm) |
| `irrigation_efficiency.tif` | GeoTIFF | Irrigation efficiency raster (0–1) |
| `water_deficit.tif` | GeoTIFF | Irrigation deficit raster (mm) |
| `irrigation_report.json` | JSON | Regional mean statistics (ET/precipitation/demand/efficiency/deficit) |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- `--input`: local GeoTIFF (band1 = crop ET, band2 = total precipitation, band3 = applied irrigation).
- `--synthetic`: growing-season scale PET/crop/precipitation/applied irrigation rasters, fully offline.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
