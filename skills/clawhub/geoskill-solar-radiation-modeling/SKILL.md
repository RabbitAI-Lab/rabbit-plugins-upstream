---
name: geoskill-solar-radiation-modeling
description: '天文辐射+地形遮蔽+大气透过率建模，输出地表太阳辐射量栅格'
---

# 太阳辐射建模 | Solar Radiation Modeling

Simulates surface solar radiation from a DEM and astronomical geometry: computes the solar position (declination / hour angle / elevation angle / azimuth), top-of-atmosphere astronomical radiation, terrain incidence angle and shadowing, combines them with a simplified clear-sky atmospheric transmittance, and integrates over time steps to obtain daily total radiation (MJ/m²).

## Core Algorithm / 核心算法

- Solar geometry (elevation angle / azimuth)
- Terrain incidence angle and shadowing
- Atmospheric transmittance + time integration

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy
```

## Usage / 使用方法

### Example 1 (Synthetic Data, Offline)

```bash
python geoskill-solar-radiation-modeling.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (Specified Region + Silent Mode)

```bash
python geoskill-solar-radiation-modeling.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### Example 3 (Real Input)

```bash
python geoskill-solar-radiation-modeling.py --input <your data file> --output-dir ./out3
```

### Example 4 (Minimal-Region Boundary Test)

```bash
python geoskill-solar-radiation-modeling.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `solar_radiation.tif` | GeoTIFF/GeoJSON/JSON | Primary output |
| `radiation_stats.json` | GeoTIFF/GeoJSON/JSON | Primary output |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- Synthetic mode: locally generates physically consistent simulated data, with no external data source.
- Real mode: reads local input files, with no network requests.

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default and makes no network requests.
- `--synthetic` mode reads no external data.
- All computation is done locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
