# Bare Soil Mapping (geoskill-bare-soil-mapping)

> Extracts bare soil/bare land distribution by fusing the bare soil index (BSI), brightness and local texture (low-contrast bare soil) thresholds, with Otsu auto-thresholding support; outputs a bare soil GeoTIFF, BSI raster and area statistics. Maps bare soil by fusing BSI, brightness and local texture.

---

## 1. Overview

Fuses three complementary features to extract the distribution of bare soil/bare land, separating it from vegetation, urban buildings and water. Suitable for soil erosion baseline surveys, early desertification identification, bare-land verification of construction land, and land-cover mapping in arid regions. Core algorithms: - **BSI (Bare Soil Index)**: BSI = ((SWIR+Red) − (NIR+Blue)) / ((SWIR+Red) + (NIR+Blue)). Bare soil has high reflectance in the red and SWIR bands and relatively low NIR reflectance, so BSI is high; vegetation has a negative BSI because of high NIR. - **Brightness**: the mean multi-band reflectance, used to exclude dark water bodies. - **Texture**: the local standard deviation. Bare soil surfaces are uniform with low contrast, while urban areas are heterogeneous with high texture. - **Thresholding**: the membership values of the three features are multiplied to produce a score in [0,1]; `--threshold auto` uses the Otsu method for automatic thresholding, or an explicit float in [0,1] can be given. A `--synthetic` mode is supported to generate a physically consistent scene containing bare soil/vegetation/urban/water (offline).

## 2. Features

Fuses three complementary features to extract the distribution of bare soil/bare land, separating it from vegetation, urban buildings and water. Suitable for soil erosion baseline surveys, early desertification identification, bare-land verification of construction land, and land-cover mapping in arid regions. Core algorithms: - **BSI (Bare Soil Index)**: BSI = ((SWIR+Red) − (NIR+Blue)) / ((SWIR+Red) + (NIR+Blue)). Bare soil has high reflectance in the red and SWIR bands and relatively low NIR reflectance, so BSI is high; vegetation has a negative BSI because of high NIR. - **Brightness**: the mean multi-band reflectance, used to exclude dark water bodies. - **Texture**: the local standard deviation. Bare soil surfaces are uniform with low contrast, while urban areas are heterogeneous with high texture. - **Thresholding**: the membership values of the three features are multiplied to produce a score in [0,1]; `--threshold auto` uses the Otsu method for automatic thresholding, or an explicit float in [0,1] can be given. A `--synthetic` mode is supported to generate a physically consistent scene containing bare soil/vegetation/urban/water (offline).

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-bare-soil-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `bare_soil.tif` | GeoTIFF (float32) | Bare soil mask (1 = bare soil), EPSG:4326 |
| `bsi.tif` | GeoTIFF (float32) | Bare soil index BSI [−1,1] |
| `bare_soil_area.json` | JSON | Pixel/area statistics (m², ha, km²), proportion, applied threshold, mean BSI |
| `output-manifest.json` | JSON | Run manifest (input/output/QA/software versions) |


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

# 裸土/裸地制图（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-bare-soil-mapping
description: '融合裸土指数 BSI、亮度与局部纹理（裸土低对比度）阈值提取裸土/裸地分布，支持 Otsu 自动阈值，输出裸土 GeoTIFF、BSI 栅格与面积统计。Maps bare soil by fusing BSI, brightness and local texture.'
---

# 裸土/裸地制图 | Bare Soil Mapping

融合三个互补特征提取裸土/裸地分布，把裸土与植被、城镇建筑、水体区分开。
适用于土壤侵蚀本底调查、荒漠化早期识别、建设用地裸地核查与干旱区地表覆盖制图。

核心算法：

- **BSI（裸土指数）**：BSI = ((SWIR+Red) − (NIR+Blue)) / ((SWIR+Red) + (NIR+Blue))。
  裸土红光与短波红外高反射、近红外相对低，BSI 偏高；植被因 NIR 高而 BSI 为负。
- **亮度（brightness）**：多波段反射率均值，用于排除暗色水体。
- **纹理（texture）**：局部标准差。裸土表面均一、对比度低；城镇异质、纹理高。
- **阈值化**：三者隶属度相乘得到得分 [0,1]；`--threshold auto` 用大津法（Otsu）
  自动阈值，或显式给定 [0,1] 浮点数。

支持 `--synthetic` 模式生成含裸土/植被/城镇/水体的物理一致场景（离线）。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（合成数据 + 自动阈值，离线）

```bash
python geoskill-bare-soil-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --threshold auto --output-dir ./output
```

### 示例 1：显式阈值

```bash
python geoskill-bare-soil-mapping.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --synthetic --threshold 0.4 \
    --output-dir ./thr
```

### 示例 2：调整纹理窗口

```bash
python geoskill-bare-soil-mapping.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --synthetic --texture-size 7 \
    --output-dir ./tex
```

### 示例 3：真实多波段影像

```bash
python geoskill-bare-soil-mapping.py \
    --input scene.tif \
    --threshold auto \
    --output-dir ./real
```

输入波段顺序：blue / green / red / nir / swir（至少 5 波段）。

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `bare_soil.tif` | GeoTIFF (float32) | 裸土掩膜（1=裸土），EPSG:4326 |
| `bsi.tif` | GeoTIFF (float32) | 裸土指数 BSI [−1,1] |
| `bare_soil_area.json` | JSON | 像元/面积（m²、ha、km²）、占比、应用阈值、均值 BSI |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

- **合成模式**：本地生成，无外部数据源
- **真实模式**：用户提供多波段地表反射率 GeoTIFF（如 Landsat / Sentinel-2）

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- 所有计算在本地完成，不上传用户数据

## License

MIT
