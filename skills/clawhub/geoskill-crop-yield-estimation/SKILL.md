---
name: crop-yield-estimation
display_name: 作物产量估算工具
version: 0.1.0
author: ruiduobao
license: MIT-0
description: |
  融合遥感时序、天气、土壤和统计样本，估算地块或行政区作物产量，
  给出预测区间和可解释因子。支持随机森林、梯度提升和集成模型，
  提供按年份/区域分组的交叉验证。
runtime: python>=3.8
tags: [gis, remote-sensing, agriculture, yield, prediction, uncertainty]
---

# crop-yield-estimation

融合遥感时序、天气、土壤和统计样本，估算地块或行政区作物产量并给出预测区间和可解释因子。

## 功能特性

- **多源数据融合**：遥感植被指数、天气、土壤、地形特征
- **多种模型**：随机森林、梯度提升、集成模型
- **不确定性量化**：分位数回归森林、集成扩散、提升阶段方差
- **可解释输出**：特征重要性排序、SHAP-like 因子贡献
- **严格验证**：按年份/区域分组验证，禁止简单随机划分
- **单位统一**：自动转换单产/总产、鲜重/干重单位
- **外推检测**：检查预测样本是否超出训练特征包络

## 使用方法

```bash
# 基本用法
python crop_yield_estimation.py run --crop maize --year 2023 --yield-labels labels.csv --output-dir output

# 指定模型和验证方式
python crop_yield_estimation.py run --crop wheat --year 2022 --yield-labels labels.geojson \
  --model gradient_boosting --validation-scheme leave_one_year

# 指定边界框
python crop_yield_estimation.py run --crop rice --year 2023 --yield-labels labels.csv \
  --bbox 116 39 117 40 --output-dir output

# 集成模型 + 详细日志
python crop_yield_estimation.py run --crop maize --year 2023 --yield-labels labels.csv \
  --model ensemble --verbose

# Auto-download mode — fetch a reference Sentinel-2 L2A scene from
# Microsoft Planetary Computer (no API key). The downloaded image is
# recorded in the output manifest; if --yield-labels is not provided
# the skill falls back to synthetic labels.
python crop_yield_estimation.py run \
  --crop maize --year 2023 \
  --bbox 116.4 39.6 116.6 39.8 \
  --date-range 2024-06-01,2024-06-30 \
  --output-dir output
```

## 数据下载

当 `--bbox` 和 `--date-range` 同时提供时，本 skill 会从 **Microsoft Planetary Computer**
的 STAC 目录自动下载一张 Sentinel-2 L2A (`sentinel-2-l2a`) 影像（无需 API key），
作为该 AOI 的参考栅格记录到 `output-manifest.json` 的
`data_source / collection / bbox / date_range / fetched_at` 字段。
实际产量估算仍以 `--yield-labels` 为准；未提供时回退到 synthetic 标签。

## 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--crop` | 作物类型 (maize/wheat/rice/soybean) | maize |
| `--year` | 目标年份 | 2023 |
| `--yield-labels` | 产量标签文件路径 (CSV/GeoJSON) | 必填 |
| `--model` | 模型类型 (random_forest/gradient_boosting/ensemble) | random_forest |
| `--validation-scheme` | 验证方式 (random/leave_one_year/leave_one_region/blocked) | leave_one_year |
| `--feature-window` | 特征窗口 (early/mid/late/full) | full |
| `--bbox` | 边界框 (xmin ymin xmax ymax) | 中国全域 |
| `--output-dir` | 输出目录 | output |
| `--confidence-level` | 置信水平 | 0.95 |
| `--n-bootstrap` | Bootstrap 迭代次数 | 200 |
| `--verbose` | 详细日志 | false |
| `--dry-run` | 仅解析请求，不执行 | false |

## 输入格式

### CSV 格式
```csv
id,year,yield_value,yield_unit,admin_code,admin_name,crop
sample_1,2023,5000,kg_ha,region_1,区域1,maize
sample_2,2023,6.5,t_ha,region_2,区域2,wheat
```

### GeoJSON 格式
```json
{
  "type": "FeatureCollection",
  "features": [{
    "type": "Feature",
    "geometry": {"type": "Polygon", "coordinates": [...]},
    "properties": {"id": "s1", "year": 2023, "yield_value": 5000,
                   "yield_unit": "kg_ha", "admin_code": "r1"}
  }]
}
```

## 输出文件

| 文件 | 说明 |
|------|------|
| `yield_estimate.geojson` | 产量估算矢量结果 |
| `yield_estimate.tif` | 产量估算栅格 |
| `prediction_interval.tif` | 预测区间宽度栅格 |
| `yield_by_admin.csv` | 按行政单元汇总 |
| `feature_importance.csv` | 特征重要性 |
| `model_card.json` | 模型元数据与性能指标 |
| `qa.json` | 质量评估报告 |
| `request.json` | 请求参数记录 |
| `dataset-manifest.json` | 输入数据清单 |
| `output-manifest.json` | 输出数据清单 |
| `run.log` | 运行日志 |

## 产量单位转换

支持以下单位，内部统一为 kg/ha（干重）：

| 单位 | 说明 | 转换系数 |
|------|------|----------|
| `t_ha` | 吨/公顷 | × 1000 |
| `kg_ha` | 千克/公顷 | × 1 |
| `jin_mu` | 斤/亩 | × 750 |
| `g_m2` | 克/平方米 | × 10 |

鲜重/干重转换系数：
- 玉米：0.85
- 小麦：0.88
- 水稻：0.87
- 大豆：0.88

## 不确定性方法

| 模型 | 方法 | 说明 |
|------|------|------|
| 随机森林 | quantile_regression_forest | 利用各树预测分位数 |
| 梯度提升 | boosting_stage_variance | 利用后期阶段方差 |
| 集成模型 | ensemble_spread | 模型间差异 + 树方差 |

## 验证方式

| 方式 | 说明 | 适用场景 |
|------|------|----------|
| random | 随机 80/20 划分 | 基线对比 |
| leave_one_year | 留一年度验证 | 评估跨年泛化 |
| leave_one_region | 留一区域验证 | 评估跨区泛化 |
| blocked | 前 80% 训练，后 20% 验证 | 时空有序数据 |

## 退出码 (Exit Codes)

| Code | Meaning |
|---|---|
| 0 | 成功 |
| 2 | 参数错误 (EXIT_BAD_ARGS) |
| 3 | 依赖缺失 (EXIT_MISSING_DEP) |
| 6 | 数据校验失败 (EXIT_DATA_VALIDATION) |
| 7 | 处理失败 (EXIT_PROCESSING) |

## 依赖安装

```bash
pip install numpy scipy scikit-learn rasterio shapely
```

## 数据获取指南

产量标签数据来源：
- 国家统计局农业统计
- 县级农业年鉴
- 实地采样调查
- 农业保险记录

遥感特征数据来源：
- Sentinel-2 / Landsat：NDVI/EVI/LAI
- ERA5 / NASA POWER：温度、降水、辐射
- SoilGrids：土壤有机碳、pH、质地
- DEM：海拔、坡度

## 引用格式

```bibtex
@software{crop_yield_estimation_2024,
  title={crop-yield-estimation: Crop Yield Estimation with Uncertainty},
  author={ruiduobao},
  year={2024},
  url={https://github.com/ruiduobao/crop-yield-estimation}
}
```

## 故障排除

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| `EXIT_BAD_ARGS (2)` | 参数错误 | 检查命令行参数 |
| `EXIT_MISSING_DEP (3)` | 缺少依赖 | pip install 安装 |
| `EXIT_DATA_VALIDATION (6)` | 数据校验失败 | 检查产量标签格式 |
| `EXIT_PROCESSING (7)` | 处理失败 | 查看 run.log |
| 样本不足 | 有效样本 < 5 | 增加样本数量 |

---

## 中文说明

融合遥感时序、天气、土壤和统计样本，估算地块或行政区作物产量并给出预测区间和可解释因子。

### 快速开始

```bash
python crop_yield_estimation.py run --crop maize --year 2023 --yield-labels labels.csv --output-dir output
```

### 主要功能

1. **样本管理**：统一官方统计、样方和地块产量的空间时间口径
2. **特征流水线**：聚合关键生育期遥感、天气、土壤和地形特征
3. **模型训练**：基线回归、树模型和可选时序模型，支持按地区/年份留一验证
4. **不确定性**：bootstrap/quantile/ensemble 预测区间和外推检测
5. **交付解释**：特征贡献、行政区汇总和情景更新

### 注意事项

- 训练与验证按年份和区域分组，至少报告跨年、跨区泛化
- 统一单产/总产、鲜重/干重和面积单位
- 检查预测样本是否超出训练特征包络，外推区域降低可信度
- MVP 采用可解释树模型，深度学习仅在样本量和跨区验证充分后加入


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python crop_yield_estimation.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--image`) 时，skill 自动下载数据。
当用户给 `--image` 时，走原文件路径 (向后兼容)。
