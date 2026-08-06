---
name: geoskill-desertification-monitoring
description: '融合 NDVI 趋势（Sen 斜率/线性回归）、反照率与植被稀缺度，综合评分分级荒漠化（稳定/轻/中/重度），输出等级与趋势栅格、面积统计。Fuses NDVI trend (Sen/linear slope), albedo and vegetation scarcity to grade desertification.'
---

# 荒漠化监测 | Desertification Monitoring

Fuses multi-epoch NDVI trend, albedo, and vegetation scarcity to score and grade desertification severity (stable / mild / moderate / severe). Suitable for long time-series monitoring of land degradation in arid and semi-arid regions, identifying degradation hotspots, and evaluating restoration effectiveness.

Core algorithm:

- **NDVI trend**: estimates the slope of the NDVI time series for each pixel, supporting Sen's slope (robust median slope, resistant to outliers) and least-squares linear regression. A negative slope indicates vegetation degradation.
- **Albedo**: mean of the visible-light bands. Bare soil / desert has high albedo, while vegetated areas are low.
- **Vegetation scarcity**: reflected by mean NDVI; low NDVI indicates sparse vegetation or bare ground.
- **Fusion score**: score = 0.4×scarcity + 0.35×bare + 0.25×decline, thresholded into four levels.

`--synthetic` mode generates a physically consistent simulated sequence with degradation trends, allowing the full workflow to be validated without network access or real data.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy
```

## Usage / 使用方法

### Basic Usage (synthetic data, offline)

```bash
python geoskill-desertification-monitoring.py --bbox 100.0 40.0 101.0 41.0 --synthetic --n-dates 6 --output-dir ./output
```

### Example 1: Sen's slope trend estimation

```bash
python geoskill-desertification-monitoring.py \
    --bbox 100.0 40.0 101.0 41.0 \
    --synthetic --n-dates 6 --method sens \
    --output-dir ./sens
```

### Example 2: least-squares linear trend

```bash
python geoskill-desertification-monitoring.py \
    --bbox 100.0 40.0 101.0 41.0 \
    --synthetic --n-dates 6 --method linear \
    --output-dir ./linear
```

### Example 3: real multi-epoch NDVI raster

```bash
python geoskill-desertification-monitoring.py \
    --input ndvi_series.tif \
    --n-dates 6 --method sens \
    --output-dir ./real
```

Input band convention: the first `n-dates` bands are the NDVI of each epoch; if one extra band is present (n-dates+1 in total), the last band is treated as albedo; otherwise `(1 − mean_ndvi)` is used as an albedo proxy.

## Output / 输出

| File | Format | Description |
|---|---|---|
| `desertification_grade.tif` | GeoTIFF (float32) | Grade 0=stable 1=mild 2=moderate 3=severe, EPSG:4326 |
| `ndvi_trend.tif` | GeoTIFF (float32) | NDVI trend slope (per epoch), negative=degradation |
| `desertification_score.tif` | GeoTIFF (float32) | Fusion score [0,1] |
| `desertification_area.json` | JSON | Pixel/area/share per grade + component means |
| `output-manifest.json` | JSON | Run manifest (input/output/QA/software versions) |

## Data Source / 数据源 / Source

- **Synthetic mode**: generated locally, no external data source
- **Real mode**: user provides multi-epoch NDVI GeoTIFF (e.g., MODIS MOD13 / Landsat NDVI time series)

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default and makes no network requests
- All computation is done locally; no user data is uploaded

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-desertification-monitoring
description: '融合 NDVI 趋势（Sen 斜率/线性回归）、反照率与植被稀缺度，综合评分分级荒漠化（稳定/轻/中/重度），输出等级与趋势栅格、面积统计。Fuses NDVI trend (Sen/linear slope), albedo and vegetation scarcity to grade desertification.'
---

# 荒漠化监测 | Desertification Monitoring

融合多期 NDVI 趋势、反照率（albedo）与植被稀缺度，对荒漠化程度综合评分并
分级（稳定 / 轻度 / 中度 / 重度）。适用于干旱-半干旱区土地退化的长时序监测、
退化热点识别与治理成效评估。

核心算法：

- **NDVI 趋势**：对每个像元的 NDVI 时间序列估计斜率，支持 Sen's slope（稳健
  中位数斜率，抗异常值）与最小二乘线性回归。负斜率指示植被退化。
- **反照率**：可见光波段均值。裸土/沙漠反照率高，植被覆盖区低。
- **植被稀缺度**：由平均 NDVI 反映，低 NDVI 指示稀疏植被或裸地。
- **融合评分**：score = 0.4×scarcity + 0.35×bare + 0.25×decline，阈值化为四级。

支持 `--synthetic` 模式生成含退化趋势的物理一致模拟序列，无需网络和真实数据
即可验证全流程。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-desertification-monitoring.py --bbox 100.0 40.0 101.0 41.0 --synthetic --n-dates 6 --output-dir ./output
```

### 示例 1：Sen's slope 趋势估计

```bash
python geoskill-desertification-monitoring.py \
    --bbox 100.0 40.0 101.0 41.0 \
    --synthetic --n-dates 6 --method sens \
    --output-dir ./sens
```

### 示例 2：最小二乘线性趋势

```bash
python geoskill-desertification-monitoring.py \
    --bbox 100.0 40.0 101.0 41.0 \
    --synthetic --n-dates 6 --method linear \
    --output-dir ./linear
```

### 示例 3：真实多期 NDVI 栅格

```bash
python geoskill-desertification-monitoring.py \
    --input ndvi_series.tif \
    --n-dates 6 --method sens \
    --output-dir ./real
```

输入波段约定：前 `n-dates` 个波段为各期 NDVI；若再多一个波段（共 n-dates+1），
末波段被视为反照率，否则用 `(1 − mean_ndvi)` 作为反照率代理。

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `desertification_grade.tif` | GeoTIFF (float32) | 等级 0=稳定 1=轻度 2=中度 3=重度，EPSG:4326 |
| `ndvi_trend.tif` | GeoTIFF (float32) | NDVI 趋势斜率（每期），负值=退化 |
| `desertification_score.tif` | GeoTIFF (float32) | 融合得分 [0,1] |
| `desertification_area.json` | JSON | 各等级像元/面积/占比 + 分项均值 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

- **合成模式**：本地生成，无外部数据源
- **真实模式**：用户提供多期 NDVI GeoTIFF（如 MODIS MOD13 / Landsat NDVI 时序）

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- 所有计算在本地完成，不上传用户数据

## License

MIT
