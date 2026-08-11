---
name: geoskill-urban-canyon-analysis
description: 'Compute street canyon height-to-width ratio and sky view factor (SVF) from a digital surface model.'
---

# 城市峡谷分析 | Urban Canyon Analysis

Derives street canyon morphological parameters from a digital surface model (DSM), for urban climate, thermal environment and radiation studies.

Core algorithm: building height = DSM − DTM (when no DTM is available, the ground surface is estimated with morphological opening); street width is estimated from the Euclidean distance transform of non-building areas (centerline width ≈ 2 × distance to the nearest building); H/W ratio = height/width; the sky view factor adopts the analytical solution for a two-dimensional canyon, SVF = 1/sqrt(1+(H/W)²), in the range [0,1] — open areas take 1, deep canyons tend to 0.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-urban-canyon-analysis.py --bbox 116.0 39.0 117.0 40.0 [other parameters]
```

### Examples

#### Example 1 (Synthetic Data (Offline))

```bash
python geoskill-urban-canyon-analysis.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### Example 2 (Usage 2)

```bash
python geoskill-urban-canyon-analysis.py --input dsm.tif --dtm dtm.tif --output-dir ./out
```

#### Example 3 (Usage 3)

```bash
python geoskill-urban-canyon-analysis.py --bbox 121.0 31.0 122.0 32.0 --threshold 3.0 --output-dir ./out --quiet
```

#### Example 4 (Usage 4)

```bash
python geoskill-urban-canyon-analysis.py --input dsm.tif --threshold 1.5 --output-dir ./out
```

#### Example 5 (Usage 5)

```bash
python geoskill-urban-canyon-analysis.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `urban_canyon.tif` | GeoTIFF | Three bands: band1=building height, band2=H/W ratio, band3=SVF |
| `canyon_stats.json` | JSON | Mean street H/W, mean SVF, SVF range |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

Local DSM GeoTIFF (+ optional DTM); `--synthetic` mode generates an offline scene of a regular block grid (building blocks + straight streets).

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; user data is never uploaded.

## License / License

MIT

---


<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-urban-canyon-analysis
description: 'Compute street canyon height-to-width ratio and sky view factor (SVF) from a digital surface model.'
---

# 城市峡谷分析 | Urban Canyon Analysis

从数字表面模型（DSM）推导街道峡谷形态参数，用于城市气候、热环境与辐射研究。

核心算法：建筑高度 = DSM − DTM（无 DTM 时用形态学开运算估计地面）；街道宽度由非建筑区欧氏距离变换估计（中心线宽度 ≈ 2×到最近建筑距离）；H/W 比 = 高度/宽度；天空可视因子取二维峡谷解析解 SVF = 1/sqrt(1+(H/W)²)，值域 [0,1]，开阔地为 1、深峡谷趋于 0。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-urban-canyon-analysis.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例

#### 示例 1（合成数据（离线））

```bash
python geoskill-urban-canyon-analysis.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### 示例 2（用法 2）

```bash
python geoskill-urban-canyon-analysis.py --input dsm.tif --dtm dtm.tif --output-dir ./out
```

#### 示例 3（用法 3）

```bash
python geoskill-urban-canyon-analysis.py --bbox 121.0 31.0 122.0 32.0 --threshold 3.0 --output-dir ./out --quiet
```

#### 示例 4（用法 4）

```bash
python geoskill-urban-canyon-analysis.py --input dsm.tif --threshold 1.5 --output-dir ./out
```

#### 示例 5（用法 5）

```bash
python geoskill-urban-canyon-analysis.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `urban_canyon.tif` | GeoTIFF | 三波段：band1=建筑高度，band2=H/W 比，band3=SVF |
| `canyon_stats.json` | JSON | 街道平均 H/W、平均 SVF、SVF 范围 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地 DSM GeoTIFF（+ 可选 DTM）；`--synthetic` 模式生成规则街区网格（建筑块 + 直街道）的离线场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
