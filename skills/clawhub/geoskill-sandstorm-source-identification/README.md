# Sandstorm Source Identification (geoskill-sandstorm-source-identification)

> Sandstorm source identification fusing low-NDVI bare soil and wind-speed dust emission thresholds.

---

## 1. Overview

Identify sandstorm source regions by integrating surface and meteorological conditions: dust emission potential P = bare soil × lack of vegetation protection (1-NDVI') × wind exceedance factor max(V-V_th, 0), with potential zero when wind speed is below the threshold; the physical-criteria source-region mask = {V > V_th} ∩ {NDVI < NDVI_low}; source-region scores are then obtained by weighting with backward-trajectory proximity weights (high upwind, 0 downwind).

## 2. Features

Identify sandstorm source regions by integrating surface and meteorological conditions: dust emission potential P = bare soil × lack of vegetation protection (1-NDVI') × wind exceedance factor max(V-V_th, 0), with potential zero when wind speed is below the threshold; the physical-criteria source-region mask = {V > V_th} ∩ {NDVI < NDVI_low}; source-region scores are then obtained by weighting with backward-trajectory proximity weights (high upwind, 0 downwind).

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-sandstorm-source-identification.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `emission_potential.tif` | GeoTIFF | Dust emission potential [0,1] |
| `source_mask.tif` | GeoTIFF | Physical-criteria source-region mask |
| `source_contribution.tif` | GeoTIFF | Trajectory-weighted source-region score [0,1] |
| `sandstorm_params.json` | JSON | Dust emission threshold / receptor / wind direction parameters |

Each run also produces `output-manifest.json` (run manifest, including input/output and QA summary).

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

# 沙尘暴源区识别（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-sandstorm-source-identification
description: '低NDVI裸土风速起沙阈值融合的沙尘暴源区识别'
---

# 沙尘暴源区识别 | Sandstorm Source Identification

综合地表与气象条件识别沙尘暴源区：起沙潜势 P = 裸土 × 缺植被保护(1-NDVI') × 风超阈值因子 max(V-V_th,0)，风速低于阈值时潜势为 0；物理判据源区掩膜 = {V>V_th} ∩ {NDVI<NDVI_low}；再以后向轨迹邻近权重（上风方高、下风方为 0）加权得源区评分。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-sandstorm-source-identification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 更多示例

```bash
python geoskill-sandstorm-source-identification.py --bbox 80 40 81 41 --synthetic --output-dir ./out
python geoskill-sandstorm-source-identification.py --input scene.tif --threshold 8 --output-dir ./out
python geoskill-sandstorm-source-identification.py --bbox 80 40 81 41 --threshold 7 --wind-dir 90 --synthetic --output-dir ./out
python geoskill-sandstorm-source-identification.py --bbox 81 40 82 41 --synthetic --quiet --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `emission_potential.tif` | GeoTIFF | 粉尘排放潜势 [0,1] |
| `source_mask.tif` | GeoTIFF | 物理判据源区掩膜 |
| `source_contribution.tif` | GeoTIFF | 轨迹加权源区评分 [0,1] |
| `sandstorm_params.json` | JSON | 起沙阈值/受体/风向参数 |

每次运行还会产出 `output-manifest.json`（运行清单，含输入/产物/QA 摘要）。

## 数据源 / Source

真实模式读取多波段 GeoTIFF（band1=风速m/s、band2=NDVI、band3=裸土比例）；合成模式离线生成沙漠-绿洲场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
