# Wildfire Spread Modeling (geoskill-wildfire-spread-modeling)

> Cellular automaton burned-area simulation modified by slope, wind speed, and fuel moisture

---

## 1. Overview

Cellular automaton (CA) based wildfire spread simulation: at each time step, burning pixels ignite unburned pixels in their 8-neighborhood with a probability that combines fuel flammability, moisture (wetter fuel is harder to ignite), slope (faster uphill), and wind speed (faster downwind, including the wind direction angle). Once ignited, a pixel never extinguishes, so the burned area is monotonically non-decreasing over time; under a fixed random sequence, higher wind speed yields more burned area and higher moisture yields less.

## 2. Features

Cellular automaton (CA) based wildfire spread simulation: at each time step, burning pixels ignite unburned pixels in their 8-neighborhood with a probability that combines fuel flammability, moisture (wetter fuel is harder to ignite), slope (faster uphill), and wind speed (faster downwind, including the wind direction angle). Once ignited, a pixel never extinguishes, so the burned area is monotonically non-decreasing over time; under a fixed random sequence, higher wind speed yields more burned area and higher moisture yields less.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-wildfire-spread-modeling.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `burned_area.tif` | GeoTIFF | Final burned extent |
| `arrival_time.tif` | GeoTIFF | Arrival time step (unburned = -1) |
| `fire_params.json` | JSON | Per-time-step burned area sequence and parameters |

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

# 野火蔓延模拟（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-wildfire-spread-modeling
description: '元胞自动机叠加坡度风速燃料湿度修正的过火面积模拟'
---

# 野火蔓延模拟 | Wildfire Spread Modeling

基于元胞自动机（CA）的野火蔓延模拟：每个时间步，燃烧像元向 8 邻域未燃像元以概率点火，点火概率综合燃料可燃性、湿度（越湿越难点燃）、坡度（上坡更快）与风速（顺风更快，含风向夹角）。一旦点燃永不熄灭，过火面积随时间单调不减；固定随机序列下，风速越大过火越多、湿度越大过火越少。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-wildfire-spread-modeling.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 更多示例

```bash
python geoskill-wildfire-spread-modeling.py --bbox 116 39 117 40 --synthetic --output-dir ./out
python geoskill-wildfire-spread-modeling.py --input fuel.tif --steps 25 --output-dir ./out
python geoskill-wildfire-spread-modeling.py --bbox 116 39 117 40 --wind-speed 4 --wind-dir 90 --steps 20 --synthetic --output-dir ./out
python geoskill-wildfire-spread-modeling.py --bbox 110 35 111 36 --synthetic --quiet --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `burned_area.tif` | GeoTIFF | 最终过火范围 |
| `arrival_time.tif` | GeoTIFF | 到达时间步（未燃=-1） |
| `fire_params.json` | JSON | 逐时间步过火面积序列与参数 |

每次运行还会产出 `output-manifest.json`（运行清单，含输入/产物/QA 摘要）。

## 数据源 / Source

真实模式读取多波段 GeoTIFF（band1=燃料0-1、band2=湿度0-1、band3=坡度0-1）；合成模式离线生成火场。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
