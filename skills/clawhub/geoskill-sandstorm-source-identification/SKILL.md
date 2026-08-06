---
name: geoskill-sandstorm-source-identification
description: '低NDVI裸土风速起沙阈值融合的沙尘暴源区识别'
---

# 沙尘暴源区识别 | Sandstorm Source Identification

Identifies sandstorm source areas by integrating surface and meteorological conditions: dust emission potential P = bare soil × vegetation-protection deficit (1−NDVI′) × wind-above-threshold factor max(V−V_th, 0), where the potential is 0 when wind speed is below the threshold; the physically based source mask = {V > V_th} ∩ {NDVI < NDVI_low}; source-area scores are then obtained by weighting with backward-trajectory proximity weights (high upwind, 0 downwind).

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy
```

## Usage / 使用方法

### Basic usage (synthetic data, offline)

```bash
python geoskill-sandstorm-source-identification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### More examples

```bash
python geoskill-sandstorm-source-identification.py --bbox 80 40 81 41 --synthetic --output-dir ./out
python geoskill-sandstorm-source-identification.py --input scene.tif --threshold 8 --output-dir ./out
python geoskill-sandstorm-source-identification.py --bbox 80 40 81 41 --threshold 7 --wind-dir 90 --synthetic --output-dir ./out
python geoskill-sandstorm-source-identification.py --bbox 81 40 82 41 --synthetic --quiet --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `emission_potential.tif` | GeoTIFF | Dust emission potential [0,1] |
| `source_mask.tif` | GeoTIFF | Physically based source-area mask |
| `source_contribution.tif` | GeoTIFF | Trajectory-weighted source-area score [0,1] |
| `sandstorm_params.json` | JSON | Dust-emission threshold / receptor / wind direction parameters |

Each run also produces `output-manifest.json` (run manifest with input/output/QA summaries).

## Data Source / 数据源 / Source

Real mode reads a multi-band GeoTIFF (band1 = wind speed m/s, band2 = NDVI, band3 = bare soil fraction); synthetic mode generates a desert-oasis scene offline.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode is fully network-free.
- All processing is done locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
