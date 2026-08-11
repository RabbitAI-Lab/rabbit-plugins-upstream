---
name: geoskill-bare-soil-mapping
description: '融合裸土指数 BSI、亮度与局部纹理（裸土低对比度）阈值提取裸土/裸地分布，支持 Otsu 自动阈值，输出裸土 GeoTIFF、BSI 栅格与面积统计。Maps bare soil by fusing BSI, brightness and local texture.'
---

# 裸土/裸地制图 | Bare Soil Mapping

Fuses three complementary features to extract the distribution of bare soil/bare land, distinguishing bare soil from vegetation, urban built-up areas, and water bodies.
Suitable for soil erosion baseline surveys, early identification of desertification, verification of exposed land at construction sites, and land cover mapping in arid regions.

Core algorithm:

- **BSI (Bare Soil Index)**: BSI = ((SWIR+Red) − (NIR+Blue)) / ((SWIR+Red) + (NIR+Blue)).
  Bare soil exhibits high reflectance in the red and shortwave infrared bands and relatively low reflectance in the near-infrared, yielding high BSI values; vegetation produces negative BSI values due to its high NIR reflectance.
- **Brightness**: mean multi-band reflectance, used to exclude dark water bodies.
- **Texture**: local standard deviation. Bare soil surfaces are homogeneous with low contrast, whereas urban areas are heterogeneous with high texture.
- **Thresholding**: the membership values of the three features are multiplied to obtain a score in [0, 1]; `--threshold auto` applies the Otsu method for automatic thresholding, or an explicit float in [0, 1] can be given.

Supports `--synthetic` mode to generate physically consistent scenes containing bare soil, vegetation, urban areas, and water bodies (offline).

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy
```

## Usage / 使用方法

### Basic Usage (Synthetic Data + Automatic Threshold, Offline)

```bash
python geoskill-bare-soil-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --threshold auto --output-dir ./output
```

### Example 1: Explicit Threshold

```bash
python geoskill-bare-soil-mapping.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --synthetic --threshold 0.4 \
    --output-dir ./thr
```

### Example 2: Adjusting the Texture Window

```bash
python geoskill-bare-soil-mapping.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --synthetic --texture-size 7 \
    --output-dir ./tex
```

### Example 3: Real Multi-band Imagery

```bash
python geoskill-bare-soil-mapping.py \
    --input scene.tif \
    --threshold auto \
    --output-dir ./real
```

Input band order: blue / green / red / nir / swir (at least 5 bands).

## Output / 输出

| File | Format | Description |
|---|---|---|
| `bare_soil.tif` | GeoTIFF (float32) | Bare soil mask (1 = bare soil), EPSG:4326 |
| `bsi.tif` | GeoTIFF (float32) | Bare Soil Index BSI [−1, 1] |
| `bare_soil_area.json` | JSON | Pixel/area (m², ha, km²), proportion, applied threshold, mean BSI |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/software versions) |

## Data Source / 数据源 / Source

- **Synthetic mode**: generated locally, no external data source
- **Real mode**: user-provided multi-band surface reflectance GeoTIFF (e.g., Landsat / Sentinel-2)

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default; makes no network requests
- All computation is performed locally; no user data is uploaded

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
