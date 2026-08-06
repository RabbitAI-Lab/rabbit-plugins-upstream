---
name: geoskill-snow-avalanche-susceptibility
description: '坡度坡向地形粗糙度叠加积雪与温度的雪崩易发性评估'
---

# 雪崩易发性评估 | Snow Avalanche Susceptibility

Snow avalanche susceptibility is assessed by fusing terrain and snow/meteorological factors: a slope factor (Gaussian-shaped, peaking at ~38°, with 30–45° being the high-risk range), an aspect factor (higher on north-facing leeward slopes in the Northern Hemisphere), terrain roughness (smoother surfaces are more susceptible), snow depth (saturating increase), and temperature (wet snow near 0 °C is the most unstable). Each factor is normalized to [0,1], then combined by weighted sum into a susceptibility index, which is subsequently classified into levels.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy
```

## Usage / 使用方法

### Basic Usage (Synthetic Data, Offline)

```bash
python geoskill-snow-avalanche-susceptibility.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### More Examples

```bash
python geoskill-snow-avalanche-susceptibility.py --bbox 90 30 91 31 --synthetic --output-dir ./out
python geoskill-snow-avalanche-susceptibility.py --input terrain.tif --output-dir ./out
python geoskill-snow-avalanche-susceptibility.py --bbox 90 30 91 31 --roughness 0.5 --synthetic --output-dir ./out
python geoskill-snow-avalanche-susceptibility.py --bbox 91 30 92 31 --synthetic --quiet --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `susceptibility.tif` | GeoTIFF | Avalanche susceptibility index [0,1] |
| `susceptibility_level.tif` | GeoTIFF | Susceptibility level (0 low – 3 extremely high) |
| `avalanche_params.json` | JSON | Factor weights |

Each run also produces `output-manifest.json` (a run manifest containing input, outputs, and a QA summary).

## Data Source / 数据源 / Source

Real mode reads a multi-band GeoTIFF (band1 = slope°, band2 = aspect°, band3 = snow depth m, band4 = temperature °C); synthetic mode generates a mountain scene offline.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-snow-avalanche-susceptibility
description: '坡度坡向地形粗糙度叠加积雪与温度的雪崩易发性评估'
---

# 雪崩易发性评估 | Snow Avalanche Susceptibility

融合地形与积雪/气象因子评估雪崩易发性：坡度因子（高斯型，峰值 ~38°，30–45° 高发）、坡向因子（北半球偏北背风坡更高）、地形粗糙度（越光滑越易发）、积雪深度（饱和递增）与温度（接近 0°C 湿雪最不稳定）。各因子归一到 [0,1] 后加权求和得易发性指数，再分级。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-snow-avalanche-susceptibility.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 更多示例

```bash
python geoskill-snow-avalanche-susceptibility.py --bbox 90 30 91 31 --synthetic --output-dir ./out
python geoskill-snow-avalanche-susceptibility.py --input terrain.tif --output-dir ./out
python geoskill-snow-avalanche-susceptibility.py --bbox 90 30 91 31 --roughness 0.5 --synthetic --output-dir ./out
python geoskill-snow-avalanche-susceptibility.py --bbox 91 30 92 31 --synthetic --quiet --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `susceptibility.tif` | GeoTIFF | 雪崩易发性指数 [0,1] |
| `susceptibility_level.tif` | GeoTIFF | 易发性分级（0低-3极高） |
| `avalanche_params.json` | JSON | 因子权重 |

每次运行还会产出 `output-manifest.json`（运行清单，含输入/产物/QA 摘要）。

## 数据源 / Source

真实模式读取多波段 GeoTIFF（band1=坡度°、band2=坡向°、band3=雪深m、band4=温度°C）；合成模式离线生成山地场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
