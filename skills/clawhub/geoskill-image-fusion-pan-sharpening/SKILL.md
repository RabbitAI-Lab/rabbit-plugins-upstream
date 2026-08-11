---
name: geoskill-image-fusion-pan-sharpening
description: 'Brovey/IHS 全色锐化，融合多光谱与全色波段生成高空间分辨率影像'
---

# 影像融合与全色锐化 | Image Fusion & Pan-sharpening

Fuses a high spatial resolution panchromatic band (PAN) with lower-resolution multispectral (MS) imagery to produce imagery that combines high spatial resolution with multispectral information. Two classic methods are implemented: the **Brovey** transform (fused_b = MS_b↑ × PAN / Σ(MS↑), which preserves the per-band proportions so that the fused bands sum to PAN) and **IHS** (the intensity component is replaced by PAN, then inverse-transformed as fused_b = MS_b↑ + (PAN − I), injecting spatial detail into each band via the intensity difference). The multispectral bands are first upsampled to the PAN resolution with bicubic interpolation before fusion.

Typical applications: Landsat-8/9 OLI (30 m MS + 15 m PAN), Sentinel-2 (fusion of 10/20/60 m bands to 10 m), Gaofen (GF) series, Ziyuan (ZY) series, WorldView/GeoEye, etc. Brovey suits scenes with few bands and low noise; IHS is simple to implement and preserves hue well.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## Usage / 使用方法

### Basic usage

```bash
python geoskill-image-fusion-pan-sharpening.py --bbox 116.0 39.0 117.0 40.0 [other arguments]
```

### Example 1 (Synthetic data, offline)

```bash
python geoskill-image-fusion-pan-sharpening.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (IHS method + scale=4)

```bash
python geoskill-image-fusion-pan-sharpening.py --bbox 121.0 31.0 122.0 32.0 --synthetic --method ihs --scale 4 --output-dir ./out2
```

### Example 3 (Real input)

```bash
python geoskill-image-fusion-pan-sharpening.py --input ms.tif --pan pan.tif --method brovey --output-dir ./out3
```

### Example 4 (Tiny-region boundary test)

```bash
python geoskill-image-fusion-pan-sharpening.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

### Example 5 (Custom number of bands)

```bash
python geoskill-image-fusion-pan-sharpening.py --bbox 116.0 39.0 117.0 40.0 --synthetic --method ihs --scale 2 --output-dir ./out5
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `fused_pansharpened.tif` | GeoTIFF | Primary output: fused multispectral (bands × H × W; H, W = PAN resolution) |
| `fusion_params.json` | JSON | Algorithm parameters (method, scale, ms_shape, pan_shape, output_shape) |
| `output-manifest.json` | JSON | Run manifest (output files + QA metrics) |

## Data Source / 数据源 / Source

- Synthetic mode: generates physically consistent simulated data locally (high-resolution multispectral ground truth + derived PAN and low-resolution MS), with no external data sources.
- Real mode: reads local GeoTIFFs (MS + PAN).

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode is fully offline with no network access.
- All processing is performed locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-image-fusion-pan-sharpening
description: 'Brovey/IHS 全色锐化，融合多光谱与全色波段生成高空间分辨率影像'
---

# 影像融合与全色锐化 | Image Fusion & Pan-sharpening

将高空间分辨率全色波段（PAN）与低分辨率多光谱（MS）融合，生成兼具高空间分辨率与多光谱信息的影像。实现了两种经典方法：**Brovey** 变换（fused_b = MS_b↑ × PAN / Σ(MS↑)，保持各波段比例，融合后各波段之和等于 PAN）与 **IHS**（用 PAN 替换强度分量，反变换 fused_b = MS_b↑ + (PAN − I)，空间细节通过强度差注入各波段）。多光谱先经双三次插值上采样到 PAN 的分辨率，再参与融合。

典型应用：Landsat-8/9 OLI（30 m MS + 15 m PAN）、Sentinel-2（10/20/60 m 多波段融合到 10 m）、高分系列、资源系列、WorldView/GeoEye 等。Brovey 适合波段数较少、噪声小的场景；IHS 实现简洁、对色相保持较好。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-image-fusion-pan-sharpening.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例 1（合成数据，离线）

```bash
python geoskill-image-fusion-pan-sharpening.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（IHS 方法 + scale=4）

```bash
python geoskill-image-fusion-pan-sharpening.py --bbox 121.0 31.0 122.0 32.0 --synthetic --method ihs --scale 4 --output-dir ./out2
```

### 示例 3（真实输入）

```bash
python geoskill-image-fusion-pan-sharpening.py --input ms.tif --pan pan.tif --method brovey --output-dir ./out3
```

### 示例 4（极小区域边界测试）

```bash
python geoskill-image-fusion-pan-sharpening.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./out4 --quiet
```

### 示例 5（自定义波段数）

```bash
python geoskill-image-fusion-pan-sharpening.py --bbox 116.0 39.0 117.0 40.0 --synthetic --method ihs --scale 2 --output-dir ./out5
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `fused_pansharpened.tif` | GeoTIFF | 主产物，融合后多光谱（bands × H × W，H,W = PAN 分辨率） |
| `fusion_params.json` | JSON | 算法参数（method、scale、ms_shape、pan_shape、output_shape） |
| `output-manifest.json` | JSON | 运行清单（输出文件 + qa 指标） |

## 数据源 / Source

- 合成模式：本地生成物理一致的模拟数据（高分辨率多光谱真值 + 派生 PAN 与低分辨率 MS），无外部数据源。
- 真实模式：读取本地 GeoTIFF（MS + PAN）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
