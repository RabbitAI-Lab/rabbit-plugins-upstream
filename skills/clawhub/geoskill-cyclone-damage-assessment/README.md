# Typhoon/Cyclone Damage Assessment (geoskill-cyclone-damage-assessment)

> Damage estimation from Holland wind-field decay combined with precipitation, storm surge, and exposure

---

## 1. Overview

Reconstructs the cyclone wind-speed distribution using a Holland parametric wind field (Vmax at r=Rmax, calm eye, decaying outer rings), converts it to a damage ratio via a sigmoid vulnerability curve (DR=0.5 at V=V50, monotonically increasing with wind speed), then adds the contributions of precipitation and storm surge (∝ wind speed²) and multiplies by exposure value to obtain per-pixel loss. Wind speed is monotonically related to Vmax, and loss is monotonically related to exposure.

## 2. Features

Reconstructs the cyclone wind-speed distribution using a Holland parametric wind field (Vmax at r=Rmax, calm eye, decaying outer rings), converts it to a damage ratio via a sigmoid vulnerability curve (DR=0.5 at V=V50, monotonically increasing with wind speed), then adds the contributions of precipitation and storm surge (∝ wind speed²) and multiplies by exposure value to obtain per-pixel loss. Wind speed is monotonically related to Vmax, and loss is monotonically related to exposure.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-cyclone-damage-assessment.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `wind_speed.tif` | GeoTIFF | Holland wind speed field (m/s) |
| `damage_ratio.tif` | GeoTIFF | Combined damage ratio [0,1] |
| `loss.tif` | GeoTIFF | Per-pixel loss (damage ratio × exposure value) |
| `cyclone_params.json` | JSON | Vmax/Rmax/Holland B/vulnerability parameters |

Each run also produces `output-manifest.json` (run manifest with inputs/outputs/QA summary).

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

# 台风/气旋灾害评估（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-cyclone-damage-assessment
description: 'Holland风场衰减叠加降水风暴潮与暴露度的损失估算'
---

# 台风/气旋灾害评估 | Cyclone Damage Assessment

用 Holland 参数化风场重建气旋风速分布（r=Rmax 处取 Vmax、风眼平静、外围衰减），经 sigmoid 脆弱性曲线转为损毁率（V=V50 时 DR=0.5，随风速单调增），再叠加降水与风暴潮（∝风速²）贡献，与暴露价值相乘得逐像元损失。风速对 Vmax 线性单调，损失对暴露单调。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-cyclone-damage-assessment.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 更多示例

```bash
python geoskill-cyclone-damage-assessment.py --bbox 120 25 121 26 --synthetic --output-dir ./out
python geoskill-cyclone-damage-assessment.py --input exposure.tif --vmax 55 --rmax 30000 --output-dir ./out
python geoskill-cyclone-damage-assessment.py --bbox 120 25 121 26 --vmax 65 --v50 45 --synthetic --output-dir ./out
python geoskill-cyclone-damage-assessment.py --bbox 121 25 122 26 --synthetic --quiet --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `wind_speed.tif` | GeoTIFF | Holland 风速场（m/s） |
| `damage_ratio.tif` | GeoTIFF | 综合损毁率 [0,1] |
| `loss.tif` | GeoTIFF | 逐像元损失（损毁率×暴露价值） |
| `cyclone_params.json` | JSON | Vmax/Rmax/Holland B/脆弱性参数 |

每次运行还会产出 `output-manifest.json`（运行清单，含输入/产物/QA 摘要）。

## 数据源 / Source

真实模式读取多波段 GeoTIFF（band1=暴露价值、band2=降水、band3=海岸掩膜），风场由参数合成；合成模式离线生成完整场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
