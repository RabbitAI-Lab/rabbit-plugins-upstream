---
name: geoskill-map-style-transfer
description: 'Transfer map styles via color mapping and histogram matching with style templates'
---

# 地图风格迁移 | Map Style Transfer

Transfers the visual style of a source raster to a target: histogram matching (CDF mapping to align the mean/variance of a reference image), style templates (vintage/cool/warm/noir with gamma/contrast/hue adjustments) and palette quantization (posterization).

The three techniques can be combined: first match with `--reference`, then apply a template with `--style`, and finally quantize the color levels with `--levels`.

## Core Algorithm / 核心算法

histogram_match uses np.unique+np.interp to map the source CDF to the reference values → apply_style_template applies grayscale/gamma/contrast/hue adjustments → quantize_palette quantizes by levels.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## Usage / 使用方法

### Example 1 (synthetic data, offline)

```bash
python geoskill-map-style-transfer.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (histogram match to a reference)

```bash
python geoskill-map-style-transfer.py --input src.tif --reference ref.tif
```

### Example 3 (black-and-white high-contrast noir)

```bash
python geoskill-map-style-transfer.py --input src.tif --style noir
```

### Example 4 (palette quantization to 6 levels)

```bash
python geoskill-map-style-transfer.py --input src.tif --levels 6
```

### Example 5 (synthetic + warm template)

```bash
python geoskill-map-style-transfer.py --bbox 116 39 117 40 --synthetic --style warm
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `styled.png` | PNG | Stylized image (main deliverable) |
| `styled.tif` | GeoTIFF | Processed grayscale raster (verifiable deliverable) |
| `style_meta.json` | JSON | Template parameters/matching statistics |

Each run also produces `output-manifest.json` (run manifest).

## Data Source / 数据源 / Source

Local GeoTIFF / vector files; `--synthetic` mode generates physically consistent simulated data, fully offline.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is performed locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
