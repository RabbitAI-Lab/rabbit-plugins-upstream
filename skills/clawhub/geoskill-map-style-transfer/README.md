# Map Style Transfer (geoskill-map-style-transfer)

> Transfer map styles via color mapping and histogram matching with style templates

---

## 1. Overview

Transfers the visual style of a source raster onto the target: histogram matching (CDF mapping that aligns the mean/variance with a reference image), style templates (gamma / contrast / hue for vintage / cool / warm / noir), and palette quantization (posterization). The three techniques are composable: first match with `--reference`, then apply a template with `--style`, and finally quantize the color levels with `--levels`.

## 2. Features

Transfers the visual style of a source raster onto the target: histogram matching (CDF mapping that aligns the mean/variance with a reference image), style templates (gamma / contrast / hue for vintage / cool / warm / noir), and palette quantization (posterization). The three techniques are composable: first match with `--reference`, then apply a template with `--style`, and finally quantize the color levels with `--levels`.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-map-style-transfer.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `styled.png` | PNG | Stylized image (primary output) |
| `styled.tif` | GeoTIFF | Processed grayscale raster (verifiable output) |
| `style_meta.json` | JSON | Template parameters / matching statistics |

Each run also produces `output-manifest.json` (run manifest).


## 6. Technical Principle

histogram_match uses np.unique + np.interp to map the source CDF onto reference values → apply_style_template applies grayscale / gamma / contrast / hue → quantize_palette quantizes by levels.

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 地图风格迁移（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-map-style-transfer
description: 'Transfer map styles via color mapping and histogram matching with style templates'
---

# 地图风格迁移 | Map Style Transfer

把源栅格的视觉风格迁移到目标：直方图匹配（CDF 映射对齐参考影像均值/方差）、风格模板（vintage/cool/warm/noir 的 gamma/对比度/色调）与调色板量化（海报化）。

三种手段可组合：先 --reference 匹配，再 --style 套模板，最后 --levels 量化色阶。

## 核心算法

histogram_match 用 np.unique+np.interp 把源 CDF 映射到参考取值 → apply_style_template 做灰度/gamma/对比度/色调 → quantize_palette 按 levels 量化。

## 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-map-style-transfer.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（直方图匹配到参考）

```bash
python geoskill-map-style-transfer.py --input src.tif --reference ref.tif
```

### 示例 3（黑白高对比 noir）

```bash
python geoskill-map-style-transfer.py --input src.tif --style noir
```

### 示例 4（调色板量化 6 级）

```bash
python geoskill-map-style-transfer.py --input src.tif --levels 6
```

### 示例 5（合成 + warm 模板）

```bash
python geoskill-map-style-transfer.py --bbox 116 39 117 40 --synthetic --style warm
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `styled.png` | PNG | 风格化图（主产物） |
| `styled.tif` | GeoTIFF | 处理后灰度栅格（可验证产物） |
| `style_meta.json` | JSON | 模板参数/匹配统计 |

每次运行还会产出 `output-manifest.json`（运行清单）。

## 数据源 / Source

本地 GeoTIFF / 矢量文件；`--synthetic` 模式生成物理一致的模拟数据，完全离线。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
