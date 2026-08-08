---
name: geoskill-kriging-interpolation
description: '半变异函数拟合+普通克里金插值+交叉验证，输出插值栅格GeoTIFF'
---

# 克里金空间插值 | Kriging Interpolation

Performs Ordinary Kriging interpolation on discrete sample points: first computes the empirical semivariogram and fits a spherical model (nugget/sill/range), then solves the kriging system with Lagrange multipliers pixel by pixel, and evaluates accuracy with leave-one-out cross-validation (RMSE/ME). Outputs an interpolation raster and a kriging variance raster.

## Core Algorithm / 核心算法

- Semivariogram fitting (spherical model)
- Ordinary kriging system solving
- Leave-one-out cross-validation

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy
```

## Usage / 使用方法

### Example 1 (synthetic data, offline)

```bash
python geoskill-kriging-interpolation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (specified area + quiet mode)

```bash
python geoskill-kriging-interpolation.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### Example 3 (real input)

```bash
python geoskill-kriging-interpolation.py --input <your data file> --output-dir ./out3
```

### Example 4 (tiny-area boundary test)

```bash
python geoskill-kriging-interpolation.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `kriging_result.tif` | GeoTIFF/GeoJSON/JSON | Primary output |
| `kriging_variance.tif` | GeoTIFF/GeoJSON/JSON | Primary output |
| `variogram_params.json` | GeoTIFF/GeoJSON/JSON | Primary output |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- Synthetic mode: locally generates physically consistent simulated data; no external data source.
- Real mode: reads local input files; no network requests.

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default; makes no network requests.
- `--synthetic` mode reads no external data.
- All computation is done locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-kriging-interpolation
description: '半变异函数拟合+普通克里金插值+交叉验证，输出插值栅格GeoTIFF'
---

# 克里金空间插值 | Kriging Interpolation

对离散采样点执行普通克里金（Ordinary Kriging）插值：先计算经验半变异函数并拟合球状模型（nugget/sill/range），再逐像元求解含 Lagrange 乘子的克里金方程组，并用 leave-one-out 交叉验证（RMSE/ME）评估精度。输出插值栅格与克里金方差栅格。

## 核心算法

- 半变异函数拟合（球状模型）
- 普通克里金方程求解
- leave-one-out 交叉验证

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-kriging-interpolation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（指定区域 + 静默）

```bash
python geoskill-kriging-interpolation.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./out2 --quiet
```

### 示例 3（真实输入）

```bash
python geoskill-kriging-interpolation.py --input <你的数据文件> --output-dir ./out3
```

### 示例 4（极小区域边界测试）

```bash
python geoskill-kriging-interpolation.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `kriging_result.tif` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `kriging_variance.tif` | GeoTIFF/GeoJSON/JSON | 主产物 |
| `variogram_params.json` | GeoTIFF/GeoJSON/JSON | 主产物 |
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
