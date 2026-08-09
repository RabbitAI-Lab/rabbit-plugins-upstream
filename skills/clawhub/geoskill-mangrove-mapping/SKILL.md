---
name: geoskill-mangrove-mapping
description: '融合 NDVI 高值、NDWI 水陆边界、海岸缓冲与 SAR 潮汐多次散射特征，规则融合提取红树林分布，输出红树林 GeoTIFF、得分栅格、面积统计与多期变化。Maps mangroves by fusing NDVI, NDWI coast buffer and SAR tidal signatures.'
---

# 红树林制图 | Mangrove Mapping

Fuses multispectral and SAR features to map mangrove distribution in the intertidal zone of tropical/subtropical coasts, and supports multi-temporal change (gain/loss) detection. Suitable for mangrove resource baseline surveys, coastal ecological monitoring and conservation effectiveness assessment.

Four remotely detectable characteristics of mangroves:

- **High NDVI**: dense evergreen vegetation with high near-infrared reflectance and low red reflectance; NDVI is typically > 0.5.
- **NDWI boundary**: McFeeters NDWI=(Green−NIR)/(Green+NIR) is used to locate water bodies, and a distance transform yields the distance from each land pixel to the coastline.
- **Coastal buffer**: mangroves occur only within a certain buffer distance from the coastline (intertidal zone).
- **SAR tidal influence**: tidal inundation of the intertidal zone causes multiple scattering in tree trunks, making SAR backscatter brighter.

The algorithm converts the above features into [0,1] memberships and fuses them by rules (product + SAR modulation), then thresholding yields the mangrove mask. `--synthetic` mode generates a physically consistent coastal scene (offline).

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy
```

## Usage / 使用方法

### Basic Usage (synthetic data, offline)

```bash
python geoskill-mangrove-mapping.py --bbox 110.0 21.0 111.0 22.0 --synthetic --output-dir ./output
```

### Example 1: multi-temporal change detection

```bash
python geoskill-mangrove-mapping.py \
    --bbox 110.0 21.0 111.0 22.0 \
    --synthetic --n-dates 3 \
    --output-dir ./change
```

### Example 2: adjust the fusion threshold

```bash
python geoskill-mangrove-mapping.py \
    --bbox 110.0 21.0 111.0 22.0 \
    --synthetic --score-threshold 0.5 \
    --output-dir ./thr
```

### Example 3: real multiband imagery

```bash
python geoskill-mangrove-mapping.py \
    --input coastal.tif \
    --output-dir ./real
```

Input band order: green / red / nir / swir (required), with the 5th band being SAR backscatter (optional; when missing, the algorithm degrades to NDVI + coastal buffer only).

## Output / 输出

| File | Format | Description |
|---|---|---|
| `mangrove.tif` | GeoTIFF (float32) | Final-epoch mangrove mask (1 = mangrove), EPSG:4326 |
| `mangrove_score.tif` | GeoTIFF (float32) | Fusion score [0,1] |
| `mangrove_change.tif` | GeoTIFF (float32) | Multi-temporal change (1=persistent 2=gain 3=loss), only when n-dates≥2 |
| `mangrove_area.json` | JSON | Pixel/area statistics (m², ha, km²) + change statistics |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/software versions) |

## Data Source / 数据源 / Source

- **Synthetic mode**: generated locally, no external data source
- **Real mode**: user-provided multiband GeoTIFF (e.g., coregistered Sentinel-2 + Sentinel-1 products)

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default; no network requests are made
- All computation is done locally; no user data is uploaded

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-mangrove-mapping
description: '融合 NDVI 高值、NDWI 水陆边界、海岸缓冲与 SAR 潮汐多次散射特征，规则融合提取红树林分布，输出红树林 GeoTIFF、得分栅格、面积统计与多期变化。Maps mangroves by fusing NDVI, NDWI coast buffer and SAR tidal signatures.'
---

# 红树林制图 | Mangrove Mapping

融合多光谱与 SAR 特征提取热带/亚热带海岸潮间带的红树林分布，并支持多期
变化（增益/损失）检测。适用于红树林资源本底调查、海岸带生态监测与保护成效评估。

红树林的四个可遥感识别特征：

- **NDVI 高值**：茂密常绿植被，近红外高反射、红光低反射，NDVI 通常 > 0.5。
- **NDWI 边界**：用 McFeeters NDWI=(Green−NIR)/(Green+NIR) 定位水体，距离
  变换得到每个陆地像元到海岸线的距离。
- **海岸缓冲**：红树林只出现在距海岸线一定缓冲范围内（潮间带）。
- **SAR 潮汐影响**：潮间带淹水使树干产生多次散射，SAR 后向散射偏亮。

算法把上述特征转为 [0,1] 隶属度并规则融合（乘积 + SAR 调制），阈值化得到
红树林掩膜。支持 `--synthetic` 模式生成物理一致的海岸带场景（离线）。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-mangrove-mapping.py --bbox 110.0 21.0 111.0 22.0 --synthetic --output-dir ./output
```

### 示例 1：多期变化检测

```bash
python geoskill-mangrove-mapping.py \
    --bbox 110.0 21.0 111.0 22.0 \
    --synthetic --n-dates 3 \
    --output-dir ./change
```

### 示例 2：调整融合阈值

```bash
python geoskill-mangrove-mapping.py \
    --bbox 110.0 21.0 111.0 22.0 \
    --synthetic --score-threshold 0.5 \
    --output-dir ./thr
```

### 示例 3：真实多波段影像

```bash
python geoskill-mangrove-mapping.py \
    --input coastal.tif \
    --output-dir ./real
```

输入波段顺序：green / red / nir / swir（必需），第 5 波段为 SAR 后向散射（可选，
缺失时退化为仅 NDVI+海岸缓冲）。

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `mangrove.tif` | GeoTIFF (float32) | 末期红树林掩膜（1=红树林），EPSG:4326 |
| `mangrove_score.tif` | GeoTIFF (float32) | 融合得分 [0,1] |
| `mangrove_change.tif` | GeoTIFF (float32) | 多期变化（1=持续 2=增益 3=损失），仅 n-dates≥2 |
| `mangrove_area.json` | JSON | 像元/面积（m²、ha、km²）+ 变化统计 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

- **合成模式**：本地生成，无外部数据源
- **真实模式**：用户提供多波段 GeoTIFF（如 Sentinel-2 + Sentinel-1 配准产品）

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- 所有计算在本地完成，不上传用户数据

## License

MIT
