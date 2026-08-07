# Volcanic Hazard Assessment (geoskill-volcanic-hazard-assessment)

> Volcanic activity level assessment integrating thermal infrared anomalies, InSAR deformation, and SO2 column concentration

---

## 1. Overview

Assesses volcanic activity levels by fusing multi-source observations: thermal infrared brightness temperature positive anomalies (magma/hydrothermal), InSAR deformation rates (magma recharge), SO₂ column concentration (degassing intensity), and the recency of historical eruptions (exp(-years/tau)). The four [0,1] components are summed with weights to produce an activity score, which is then divided into 5 levels: normal/advisory/watch/warning/extreme. The score is monotonically non-decreasing with respect to each component.

## 2. Features

Assesses volcanic activity levels by fusing multi-source observations: thermal infrared brightness temperature positive anomalies (magma/hydrothermal), InSAR deformation rates (magma recharge), SO₂ column concentration (degassing intensity), and the recency of historical eruptions (exp(-years/tau)). The four [0,1] components are summed with weights to produce an activity score, which is then divided into 5 levels: normal/advisory/watch/warning/extreme. The score is monotonically non-decreasing with respect to each component.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-volcanic-hazard-assessment.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `activity_score.tif` | GeoTIFF | Volcanic activity score [0,1] |
| `activity_level.tif` | GeoTIFF | Activity level (integer 0-4) |
| `volcano_params.json` | JSON | Baseline brightness temperature / recency / level labels |

Each run also produces `output-manifest.json` (run manifest, including inputs/outputs/QA summary).

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

# 火山灾害评估（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-volcanic-hazard-assessment
description: '融合热红外异常、InSAR形变与SO2柱浓度的火山活动等级评估'
---

# 火山灾害评估 | Volcanic Hazard Assessment

融合多源观测评估火山活动等级：热红外亮温正异常（岩浆/热液）、InSAR 形变速率（岩浆补给）、SO₂ 柱浓度（脱气强度）与历史喷发新近度（exp(-years/tau)）。四个 [0,1] 分量加权求和得活动度评分，再切分为 normal/advisory/watch/warning/extreme 5 级。评分对每个分量单调不减。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-volcanic-hazard-assessment.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 更多示例

```bash
python geoskill-volcanic-hazard-assessment.py --bbox 120 30 121 31 --synthetic --output-dir ./out
python geoskill-volcanic-hazard-assessment.py --input volcano.tif --years-since 12 --output-dir ./out
python geoskill-volcanic-hazard-assessment.py --bbox 120 30 121 31 --baseline 285 --years-since 3 --synthetic --output-dir ./out
python geoskill-volcanic-hazard-assessment.py --bbox 121 31 122 32 --synthetic --quiet --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `activity_score.tif` | GeoTIFF | 火山活动度评分 [0,1] |
| `activity_level.tif` | GeoTIFF | 活动等级（整型 0-4） |
| `volcano_params.json` | JSON | 基线亮温/新近度/分级标签 |

每次运行还会产出 `output-manifest.json`（运行清单，含输入/产物/QA 摘要）。

## 数据源 / Source

真实模式读取多波段 GeoTIFF（band1=亮温K、band2=形变mm/yr、band3=SO₂ DU）；合成模式离线生成火山场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
