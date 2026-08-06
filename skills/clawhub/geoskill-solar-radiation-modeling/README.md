# Solar Radiation Modeling (geoskill-solar-radiation-modeling)

> Models extraterrestrial radiation, terrain shading and atmospheric transmissivity, outputting a surface solar radiation raster

---

## 1. Overview

Simulates surface solar radiation from DEM and astronomical geometry: computes the sun position (declination / hour angle / elevation angle / azimuth), top-of-atmosphere extraterrestrial radiation, terrain slope-aspect incidence angle and shading, then combines them with a simplified clear-sky atmospheric transmissivity and integrates over time steps to obtain total daily radiation (MJ/m²).

## 2. Features

Simulates surface solar radiation from DEM and astronomical geometry: computes the sun position (declination / hour angle / elevation angle / azimuth), top-of-atmosphere extraterrestrial radiation, terrain slope-aspect incidence angle and shading, then combines them with a simplified clear-sky atmospheric transmissivity and integrates over time steps to obtain total daily radiation (MJ/m²).

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-solar-radiation-modeling.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `solar_radiation.tif` | GeoTIFF/GeoJSON/JSON | Primary output |
| `radiation_stats.json` | GeoTIFF/GeoJSON/JSON | Primary output |
| `output-manifest.json` | JSON | Run manifest |

## 6. Technical Principle

- Solar geometry (elevation / azimuth)
- Terrain incidence angle and shading
- Atmospheric transmissivity + time-interval integration

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 太阳辐射建模（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-solar-radiation-modeling
description: '天文辐射+地形遮蔽+大气透过率建模，输出地表太阳辐射量栅格'
---

# 太阳辐射建模 | Solar Radiation Modeling

基于 DEM 与天文几何模拟地表太阳辐射：计算太阳位置（赤纬/时角/高度角/方位角）、大气顶天文辐射、地形坡向入射角与遮蔽，叠加简化晴空大气透过率，逐时刻积分得日总辐射量（MJ/m²）。

## 核心算法

- 太阳几何（高度角/方位角）
- 地形入射角与遮蔽
- 大气透过率 + 时段积分

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-solar-radiation-modeling.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（指定区域 + 静默）

```bash
python geoskill-solar-radiation-modeling.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### 示例 3（真实输入）

```bash
python geoskill-solar-radiation-modeling.py --input <你的数据文件> --output-dir ./out3
```

### 示例 4（极小区域边界测试）

```bash
python geoskill-solar-radiation-modeling.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `solar_radiation.tif` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `radiation_stats.json` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- 合成模式：本地生成物理一致的模拟数据，无外部数据源。
- 真实模式：读取本地输入文件，无网络请求。

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求。
- `--synthetic` 模式不读取任何外部数据。
- 所有计算在本地完成，不上传用户数据。

## License

MIT
