---
name: geoskill-sar-urban-mapping
description: '基于SAR后向散射与GLCM纹理的城市建成区提取：Otsu/固定σ⁰阈值 + GLCM对比度纹理 + 形态学闭运算，输出城市范围二值GeoTIFF与面积统计JSON。SAR urban/built-up mapping via backscatter threshold, GLCM texture and morphology.'
---

# SAR 城市制图 | SAR Urban Mapping

Extracts urban / built-up areas from single-temporal SAR backscatter (σ⁰, linear power). Physical basis:

- **High backscatter**: buildings create numerous dihedral / trihedral corner reflectors, so σ⁰ in the C/X bands is significantly higher than over farmland and water.
- **High texture**: building layouts produce strong spatial heterogeneity and high GLCM contrast, whereas farmland / water surfaces are texturally uniform.

Method workflow:

1. **Threshold segmentation**: `--threshold auto` determines the σ⁰ threshold automatically via Otsu's maximum inter-class variance; a fixed linear σ⁰ threshold may also be passed.
2. **Texture assistance** (`--texture true`): applies an additional GLCM contrast threshold (Otsu) to suppress false positives from bare soil / calm water, which show high σ⁰ but uniform texture.
3. **Morphological closing**: fills holes within city blocks and connects urban patches, followed by light opening for denoising.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy
```

## Usage / 使用方法

### 基本用法（仅给 bbox，自动合成）

```bash
python geoskill-sar-urban-mapping.py --bbox 116.0 39.0 117.0 40.0 --output-dir ./out
```

### Example 1: Synthetic Data (Offline)

```bash
python geoskill-sar-urban-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./syn
```

### 示例 2：真实 SAR σ⁰ 影像

```bash
python geoskill-sar-urban-mapping.py --input sigma0_linear.tif --output-dir ./real
```

### Example 3: Fixed Threshold + Texture Disabled

```bash
python geoskill-sar-urban-mapping.py --input sigma0.tif --threshold 0.05 --texture false --output-dir ./fixed
```

### Example 4: Another Region (Shanghai)

```bash
python geoskill-sar-urban-mapping.py --bbox 121.0 31.0 122.0 32.0 --output-dir ./shanghai --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `urban_mask.tif` | GeoTIFF (uint8) | Binary urban extent mask (1=urban, 0=non-urban), EPSG:4326 |
| `urban_statistics.json` | JSON | Urban pixel count / fraction / area (km²), threshold (dB), etc. |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- **Real mode**: a local SAR σ⁰ GeoTIFF (linear power, obtainable from Sentinel-1 GRD via radiometric calibration).
- **Synthetic mode**: locally generates a low-value farmland / water background plus high-value, high-texture urban patches, with no external data source.

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default; `--synthetic` involves no network at all.
- All processing is done locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-sar-urban-mapping
description: '基于SAR后向散射与GLCM纹理的城市建成区提取：Otsu/固定σ⁰阈值 + GLCM对比度纹理 + 形态学闭运算，输出城市范围二值GeoTIFF与面积统计JSON。SAR urban/built-up mapping via backscatter threshold, GLCM texture and morphology.'
---

# SAR 城市制图 | SAR Urban Mapping

从单时相 SAR 后向散射（σ⁰，线性功率）中提取城市 / 建成区。物理依据：

- **高后向散射**：城市建筑形成大量二面角 / 三面角反射器，在 C/X 波段 σ⁰
  显著高于农田与水体。
- **高纹理**：建筑布局造成强空间异质性，GLCM 对比度高；农田 / 水面纹理均匀。

方法流程：

1. **阈值分割**：`--threshold auto` 用 Otsu 最大类间方差自动确定 σ⁰ 门限，
   也可传入固定线性 σ⁰ 门限。
2. **纹理辅助**（`--texture true`）：叠加 GLCM 对比度门限（Otsu），抑制
   高 σ⁰ 但纹理均匀的裸土 / 静水误检。
3. **形态学闭运算**：填充街区空洞、连通城市斑块，并轻微开运算去噪。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（仅给 bbox，自动合成）

```bash
python geoskill-sar-urban-mapping.py --bbox 116.0 39.0 117.0 40.0 --output-dir ./out
```

### 示例 1：合成数据（离线）

```bash
python geoskill-sar-urban-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./syn
```

### 示例 2：真实 SAR σ⁰ 影像

```bash
python geoskill-sar-urban-mapping.py --input sigma0_linear.tif --output-dir ./real
```

### 示例 3：固定阈值 + 关闭纹理

```bash
python geoskill-sar-urban-mapping.py --input sigma0.tif --threshold 0.05 --texture false --output-dir ./fixed
```

### 示例 4：另一区域（上海）

```bash
python geoskill-sar-urban-mapping.py --bbox 121.0 31.0 122.0 32.0 --output-dir ./shanghai --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `urban_mask.tif` | GeoTIFF (uint8) | 城市范围二值掩膜（1=城市，0=非城市），EPSG:4326 |
| `urban_statistics.json` | JSON | 城市像元数 / 占比 / 面积(km²)、阈值(dB)等 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- **真实模式**：本地 SAR σ⁰ GeoTIFF（线性功率，可由 Sentinel-1 GRD 经辐射定标得到）。
- **合成模式**：本地生成低值农田 / 水体背景 + 高值高纹理城市斑块，无外部数据源。

## 隐私声明 / Privacy

- 默认完全离线运行，`--synthetic` 无任何网络。
- 所有处理本地完成，不上传用户数据。

## License

MIT
