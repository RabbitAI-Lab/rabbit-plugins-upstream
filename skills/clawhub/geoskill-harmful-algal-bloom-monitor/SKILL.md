---
name: harmful-algal-bloom-monitor
description: >
  有害藻华监测 — 利用海色/水色遥感反射率监测湖海藻华范围、持续时间和风险等级。
  支持 NDCI/FLH/BGI/ARI 多指数，含云/耀斑/浑浊/浅水质量控制、事件追踪、面积统计与预警报告。
---

# Harmful Algal Bloom Monitor

基于遥感反射率监测湖泊/水库/近岸藻华的范围、持续时间与风险等级。
输出辅助分析、候选对象和证据；行政、工程、安全或事故归因必须人工复核。

## Trigger

Use when the user wants to:
- 监测湖泊/水库/近岸的藻华范围
- 生成藻华持续天数和预警报告
- 评估藻华风险等级
- 比较不同藻华指数的检测效果
- 分析藻华事件的时间演变

## CLI Usage

```bash
# 合成演示模式（无需输入文件）
python scripts/harmful_algal_bloom_monitor.py --output-dir ./habm-output

# 指定传感器和指数
python scripts/harmful_algal_bloom_monitor.py --sensor sentinel2 --index ndci --output-dir ./habm-output

# 自定义阈值和事件参数
python scripts/harmful_algal_bloom_monitor.py --event-threshold 0.4 --min-consecutive-days 5 --output-dir ./habm-output

# MODIS 传感器 + FLH 指数
python scripts/harmful_algal_bloom_monitor.py --sensor modis --index flh --output-dir ./habm-output
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--input-dir` | None | 输入反射率数据目录（省略则使用合成数据） |
| `--sensor` | sentinel2 | 传感器类型（modis/sentinel2/sentinel3_olci） |
| `--index` | ndci | 藻华指数（ndci/flh/bgi/ari） |
| `--event-threshold` | None | 藻华概率阈值（默认使用模型推荐值） |
| `--min-consecutive-days` | 3 | 确认事件所需最少连续天数 |
| `--max-gap-days` | 1 | 事件内允许最大缺测天数 |
| `--n-days` | 10 | 合成数据天数 |
| `--models-config` | None | 模型参数 JSON 文件路径 |
| `--output-dir` | habm-output | 输出目录 |

## Output

| File | Description |
|---|---|
| `alert_report.html` | 藻华监测 HTML 报告 |
| `events.geojson` | 检测到的藻华事件 |
| `daily_area.csv` | 日尺度藻华面积 |
| `bloom_probability.npy` | 最大藻华概率栅格 |
| `duration.npy` | 藻华持续天数栅格 |
| `request.json` | 分析请求元数据 |
| `dataset-manifest.json` | 数据集清单 |
| `output-manifest.json` | 输出文件清单 |
| `qa.json` | 质量保证检查 |

## Key Algorithms

### 藻华指数

| 指数 | 公式 | 适用传感器 | 适用水体 |
|---|---|---|---|
| NDCI | (Red_edge - Red) / (Red_edge + Red) | Sentinel-2/OLCI | 湖泊/水库/近岸 |
| FLH | R_red3 - R_red2 - (R_nir - R_red2) × λ系数 | MODIS | 海洋/大型湖泊 |
| BGI | (Green - Blue) / (Green + Blue) | 通用 | 湖泊/水库 |
| ARI | (1/Green) - (1/Red_edge) | Sentinel-2/OLCI | 湖泊/水库 |

### 质量控制

- **云掩膜**：蓝光反射率 > 阈值
- **耀斑掩膜**：可见光均值 > 阈值
- **浑浊水体**：红/近红外比值 > 阈值
- **浅水/底质**：总反射率 > 阈值

### 事件确认

藻华事件需连续 N 天以上超过概率阈值才确认，允许 M 天以内的数据缺测。
事件输出：起止时间、持续天数、最大概率。

### 风险等级

综合概率与持续时间分为 4 级：低风险（绿）、中风险（黄）、高风险（橙）、严重（红）。
持续时间 ≥ 5 天的藻华自动提升一个风险等级。

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | 成功 |
| 2 | 参数错误 |
| 3 | 依赖缺失 |
| 6 | 数据校验失败 |
| 7 | 处理失败 |

## Important Limitations

- **单指数仅作为候选**：藻华、浑浊和水草可能产生相似信号，单一指数无法完全区分，需多指数综合判断。
- **合成数据非真实观测**：演示模式使用合成反射率，仅用于流程验证，不可作为实际监测结论。
- **阈值需因地制宜**：默认阈值基于文献典型值，实际应用需根据水体类型和本地验证调整。
- **云覆盖影响时效**：云层会遮挡地表，导致缺测天数增加，影响事件检测的完整性。
- **模型不可跨水体迁移**：不同水体的光学特性差异大，模型需针对目标水体率定。

## References

- Gower et al. (2005) — FLH/MTCI for chlorophyll fluorescence
- Mishra & Mishra (2012) — NDCI for chlorophyll-a estimation
- Wynne et al. (2010) — MODIS cyanobacteria bloom detection
- 中国环境监测总站 — 湖泊（水库）富营养化评价方法及分级技术规定


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python harmful_algal_bloom_monitor.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--image`) 时，skill 自动下载数据。

> 注：skill 规格建议使用 `sentinel-3-olci` (更适合叶绿素 / 藻华波段), 但当前分析 pipeline 读取 Sentinel-2 的 B04/B08/B02 GeoTIFF; OLCI L2 NetCDF 是不同格式, 切换会需要重写 analysis. 暂以 `sentinel-2-l2a` 为自动下载源; 切换到 OLCI 是后续增强项.
当用户给 `--image` 时，走原文件路径 (向后兼容)。
