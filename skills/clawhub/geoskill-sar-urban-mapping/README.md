# SAR Urban Mapping (geoskill-sar-urban-mapping)

> Urban/built-up area extraction from SAR backscatter and GLCM texture: Otsu/fixed σ⁰ thresholding + GLCM contrast texture + morphological closing, outputting a binary urban extent GeoTIFF and area statistics JSON. SAR urban/built-up mapping via backscatter threshold, GLCM texture and morphology.

---

## 1. Overview

Extracts urban / built-up areas from single-temporal SAR backscatter (σ⁰, linear power). Physical basis: - **High backscatter**: urban buildings form numerous dihedral / trihedral corner reflectors, giving σ⁰ significantly higher than cropland and water in the C/X band. - **High texture**: building layouts create strong spatial heterogeneity and high GLCM contrast, whereas cropland / water surfaces have uniform texture. Method flow: 1. **Threshold segmentation**: `--threshold auto` uses Otsu's maximum inter-class variance to determine the σ⁰ threshold automatically; a fixed linear σ⁰ threshold can also be provided. 2. **Texture assistance** (`--texture true`): combines a GLCM contrast threshold (Otsu) to suppress false positives from bare soil / calm water with high σ⁰ but uniform texture. 3. **Morphological closing**: fills holes within blocks, connects urban patches, and applies light opening to remove noise.

## 2. Features

Extracts urban / built-up areas from single-temporal SAR backscatter (σ⁰, linear power). Physical basis: - **High backscatter**: urban buildings form numerous dihedral / trihedral corner reflectors, giving σ⁰ significantly higher than cropland and water in the C/X band. - **High texture**: building layouts create strong spatial heterogeneity and high GLCM contrast, whereas cropland / water surfaces have uniform texture. Method flow: 1. **Threshold segmentation**: `--threshold auto` uses Otsu's maximum inter-class variance to determine the σ⁰ threshold automatically; a fixed linear σ⁰ threshold can also be provided. 2. **Texture assistance** (`--texture true`): combines a GLCM contrast threshold (Otsu) to suppress false positives from bare soil / calm water with high σ⁰ but uniform texture. 3. **Morphological closing**: fills holes within blocks, connects urban patches, and applies light opening to remove noise.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-sar-urban-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `urban_mask.tif` | GeoTIFF (uint8) | Binary urban extent mask (1=urban, 0=non-urban), EPSG:4326 |
| `urban_statistics.json` | JSON | Urban pixel count / share / area (km²), threshold (dB), etc. |
| `output-manifest.json` | JSON | Run manifest |

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

# SAR 城市制图（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

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
