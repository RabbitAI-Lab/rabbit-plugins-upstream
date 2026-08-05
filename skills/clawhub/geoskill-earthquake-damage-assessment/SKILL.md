---
name: earthquake-damage-assessment
description: >
  震后损害快速评估 — 利用震前震后 SAR/光学变化和建筑道路暴露，快速筛查疑似建筑损毁、
  道路阻断和受影响人口。支持相干性/后向散射/纹理/光谱多特征融合，对象级聚合，
  损毁概率分级与人工复核任务生成。
---

# Earthquake Damage Assessment

利用震前震后 SAR/光学变化和建筑道路暴露，快速筛查疑似建筑损毁、道路阻断和受影响人口。
输出辅助分析、疑似对象和证据；涉及工程安全、行政认定或赔付时必须人工复核。

## Trigger

Use when the user wants to:
- 震后快速定位疑似重损建筑区
- 统计各乡镇受影响建筑和人口
- 评估道路阻断情况
- 生成人工复核任务清单
- 比较不同损毁评估模型的效果

## CLI Usage

```bash
# 合成演示模式（无需输入文件）
python scripts/earthquake_damage_assessment.py --output-dir ./eda-output

# 指定损毁评估模型
python scripts/earthquake_damage_assessment.py --damage-model sar_coherence --output-dir ./eda-output

# 自定义最小建筑面积
python scripts/earthquake_damage_assessment.py --min-building-area 100.0 --output-dir ./eda-output

# 光学 NDVI 模型
python scripts/earthquake_damage_assessment.py --damage-model optical_ndvi --output-dir ./eda-output
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--input-dir` | None | 输入数据目录 (省略则使用合成数据) |
| `--output-dir` | eda-output | 输出目录 |
| `--damage-model` | combined | 损毁评估模型 (sar_coherence/optical_ndvi/combined) |
| `--epicenter` | None | 震中位置 'lon,lat' (合成模式使用) |
| `--min-building-area` | 50.0 | 最小建筑面积 m² |
| `--grid-size` | 100 | 合成数据网格大小 |
| `--models-config` | None | 模型参数 JSON 文件路径 |

## Output

| File | Description |
|---|---|
| `damage_probability.npy` | 损毁概率栅格 [0, 1] |
| `suspected_buildings.geojson` | 疑似损毁建筑矢量 |
| `road_disruptions.geojson` | 道路阻断点矢量 |
| `impact_summary.csv` | 影响摘要统计 |
| `review_tiles/` | 人工复核任务目录 |
| `request.json` | 分析请求元数据 |
| `dataset-manifest.json` | 数据集清单 |
| `output-manifest.json` | 输出文件清单 |
| `qa.json` | 质量保证检查 |

## Key Algorithms

### 变化检测

| 特征 | 数据来源 | 物理意义 |
|---|---|---|
| 相干性变化 | Sentinel-1 SAR | 相干性下降 = 结构变化/损毁 |
| NDVI 变化 | Sentinel-2/Landsat | NDVI 下降 = 植被/结构损失 |
| 纹理变化 | SAR/光学 | 纹理增加 = 坍塌碎屑 |

### 损毁分级

| 等级 | 概率范围 | 含义 |
|---|---|---|
| 无损毁 | 0.0 - 0.2 | 无明显变化 |
| 轻微 | 0.2 - 0.4 | 可能有轻微损伤 |
| 中等 | 0.4 - 0.6 | 疑似中等损毁 |
| 严重 | 0.6 - 0.8 | 疑似严重损毁 |
| 毁坏 | 0.8 - 1.0 | 疑似完全毁坏 |

### 对象级聚合

以建筑为单位聚合多特征，避免像元噪声直接判建筑损毁：
- 建筑轮廓内像素概率平均
- 概率中位数/最大值统计
- 最小面积过滤

### 质量控制

- **云掩膜**：蓝光反射率 > 阈值
- **阴影掩膜**：近红外反射率 < 阈值
- **SAR 噪声**：相干性 < 阈值

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | 成功 |
| 2 | 参数错误 |
| 3 | 依赖缺失 |
| 6 | 数据校验失败 |
| 7 | 处理失败 |

## Important Limitations

- **合成数据非真实观测**：演示模式使用合成数据，仅用于流程验证，不可作为实际灾情结论。
- **SAR 几何门槛高**：MVP 支持外部已生成相干性图， SLC 处理需专业软件。
- **分辨率限制**：免费影像分辨率可能不足以识别单体建筑损毁。
- **类别不平衡**：真值数据稀缺，模型需针对本地建筑类型率定。
- **非最终认定**：输出疑似损毁概率和审核状态，不声称最终灾情。

## References

- Brett & Rochat (2015) — Coherence change detection for earthquake damage
- Dong & Shan (2013) — Remote sensing for earthquake damage assessment
- USGS PAGER — Global earthquake impact assessment
- UNOSAT — Satellite damage assessment methodology


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python earthquake_damage_assessment.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--sar`) 时，skill 自动下载数据。
当用户给 `--sar` 时，走原文件路径 (向后兼容)。
