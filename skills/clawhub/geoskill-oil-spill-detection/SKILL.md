---
name: oil-spill-detection
description: >
  SAR 暗斑油膜检测 — 从 SAR 暗斑中筛选疑似油膜，结合风场、形状、纹理、船舶和自然 slick 线索
  输出人工复核候选。支持后向散射阈值分割、多特征融合置信度评分与误报过滤。
---

# Oil Spill Detection

从 SAR 暗斑中筛选疑似油膜，结合风场、形状、纹理、船舶和自然 slick 线索输出人工复核候选。
输出辅助分析、候选对象和证据；涉及行政、工程、安全或事故归因必须人工复核。

## Trigger

Use when the user wants to:
- 识别 SAR 影像中的疑似油膜范围
- 筛选近岸 SAR 暗斑并按可信度排序
- 结合风场和 AIS 数据过滤误报
- 生成人工复核任务清单
- 评估不同检测方法的效果

## CLI Usage

```bash
# 合成演示模式（无需输入文件）
python scripts/oil_spill_detection.py --output-dir ./osd-output

# 指定检测方法
python scripts/oil_spill_detection.py --method threshold_adaptive --output-dir ./osd-output

# 自定义最小面积和置信度阈值
python scripts/oil_spill_detection.py --min-area 2000.0 --confidence-threshold 0.5 --output-dir ./osd-output

# 自适应阈值分割
python scripts/oil_spill_detection.py --method threshold_adaptive --grid-size 200 --output-dir ./osd-output
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--input-dir` | None | 输入数据目录 (省略则使用合成数据) |
| `--output-dir` | osd-output | 输出目录 |
| `--method` | threshold_basic | 检测方法 (threshold_basic/threshold_adaptive/multi_feature) |
| `--min-area` | 1000.0 | 最小暗斑面积 m² |
| `--confidence-threshold` | 0.4 | 置信度阈值 |
| `--grid-size` | 200 | 合成数据网格大小 |
| `--models-config` | None | 模型参数 JSON 文件路径 |

## Output

| File | Description |
|---|---|
| `dark_spots.geojson` | 所有检测到的暗斑矢量 |
| `oil_candidates.geojson` | 高置信度疑似油膜候选 |
| `confidence.npy` | 置信度栅格 [0, 1] |
| `feature_table.csv` | 暗斑特征表 |
| `review_report.txt` | 人工复核报告 |
| `request.json` | 分析请求元数据 |
| `dataset-manifest.json` | 数据集清单 |
| `output-manifest.json` | 输出文件清单 |
| `qa.json` | 质量保证检查 |

## Key Algorithms

### 暗斑分割

| 方法 | 原理 | 适用场景 |
|---|---|---|
| 基础阈值 | 后向散射 < 均值 - σ×N 且 < 全局阈值 | 均匀海面 |
| 自适应阈值 | 基于局部统计的自适应阈值 | 非均匀海面 |

### 特征提取

| 特征类别 | 特征 | 物理意义 |
|---|---|---|
| 形状 | 紧凑度、伸长率、实心度 | 油膜通常伸长、中等紧凑 |
| 纹理 | 均值、标准差、背景对比度 | 油膜均匀且明显暗于背景 |
| 风场 | 风速分区 | 3-10 m/s 最佳检测区间 |
| 船舶 | AIS 距离 | 近距离船舶增加油膜可能 |

### 误报过滤

| 误报来源 | 过滤策略 |
|---|---|
| 低风区 | 风速 < 3 m/s 标记为低置信度 |
| 雨胞 | 圆形 + 高实心度 → rain_cell 指示 |
| 内波 | 低风 + 高伸长率 → internal wave 指示 |
| 生物膜 | 近岸 + 条带 → coastal streak 指示 |

### 置信度分级

| 等级 | 范围 | 含义 |
|---|---|---|
| 极低 | 0.0 - 0.2 | 不太可能是油膜 |
| 低 | 0.2 - 0.4 | 少量油膜证据 |
| 中等 | 0.4 - 0.6 | 中等油膜证据，建议复核 |
| 高 | 0.6 - 0.8 | 较强油膜证据，建议优先复核 |
| 极高 | 0.8 - 1.0 | 强油膜证据，强烈建议复核 |

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | 成功 |
| 2 | 参数错误 |
| 3 | 依赖缺失 |
| 6 | 数据校验失败 |
| 7 | 处理失败 |

## Important Limitations

- **暗斑不等于油膜**：输出始终称疑似油膜，暗斑只是检测起点
- **合成数据非真实观测**：演示模式使用合成数据，仅用于流程验证
- **AIS 数据缺失时不强行归因船舶**：无 AIS 时返回中性置信度
- **SAR 几何门槛高**：MVP 支持外部已校准 SAR 数据
- **分辨率限制**：免费 SAR 分辨率可能不足以识别小范围油膜
- **非最终认定**：输出疑似油膜概率和审核状态，不声称最终结论

## References

- Solberg et al. (2007) — Oil spill detection in Radarsat and Envisat SAR images
- Fiscella et al. (2000) — Oil spill detection using neural networks and SAR data
- Migliaccio et al. (2007) — A physical approach for oil spill detection in SAR imagery
- ESA (2020) — SAR oil spill monitoring guidelines


## 数据下载

本 skill 可自动从 Microsoft Planetary Computer 下载数据 (无需 API key):

```bash
python oil_spill_detection.py --bbox 116,39,117,40 --date-range 2024-06-01,2024-06-30 --output-dir <tmp>
```

- `--bbox W,S,E,N`: WGS-84 边界框 (西, 南, 东, 北)
- `--date-range START,END`: 日期范围 (YYYY-MM-DD,YYYY-MM-DD)
- `--aoi-file <path.geojson>`: 替代 --bbox 的 GeoJSON 多边形
- `--cache-dir <path>`: 缓存目录 (默认 ~/.geoskill_cache)

当用户只给 `--bbox + --date-range` (没有 `--sar`) 时，skill 自动下载数据。
当用户给 `--sar` 时，走原文件路径 (向后兼容)。
