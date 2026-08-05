---
name: geoskill-map-symbology-optimizer
description: 'Optimize map symbology using color theory, contrast, visual hierarchy and accessible palettes'
---

# 地图符号优化 | Map Symbology Optimizer

Optimizes map symbology colors based on color theory and visual perception: **WCAG contrast** (selects the optimal black/white text color for each class), **color-vision accessibility** (class colors must remain distinguishable after deuteranopia simulation) and **visual hierarchy** (inter-class color distance metric).

Classification uses the Okabe-Ito / Tol accessible palettes, and outputs a complete symbology scheme as JSON plus a color scheme figure.

## Core Algorithm / 核心算法

relative_luminance/contrast_ratio (WCAG, (L1+.05)/(L2+.05)) → simulate_deuteranopia linear matrix → min_pairwise_separation determines color-vision safety → best_text_color picks the text color → optimize_symbology assembles the scheme.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## Usage / 使用方法

### Example 1 (synthetic data, offline)

```bash
python geoskill-map-symbology-optimizer.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (equal-interval classification)

```bash
python geoskill-map-symbology-optimizer.py --input landcover.tif --method equal_interval --classes 6
```

### Example 3 (Tol muted palette)

```bash
python geoskill-map-symbology-optimizer.py --input landcover.tif --palette tol-muted
```

### Example 4 (synthetic, 4 classes)

```bash
python geoskill-map-symbology-optimizer.py --bbox 116 39 117 40 --synthetic --classes 4
```

### Example 5 (quantile + Okabe-Ito)

```bash
python geoskill-map-symbology-optimizer.py --input landcover.tif --method quantile --palette okabe-ito
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `symbology.png` | PNG | Color-classified map + legend (main deliverable) |
| `classes.tif` | GeoTIFF | Class index raster (verifiable deliverable) |
| `symbology.json` | JSON | Breaks/colors/contrast/color-vision-safety QA |

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
name: geoskill-map-symbology-optimizer
description: 'Optimize map symbology using color theory, contrast, visual hierarchy and accessible palettes'
---

# 地图符号优化 | Map Symbology Optimizer

基于色彩理论与视觉感知优化地图符号配色：**WCAG 对比度**（为每类选最优黑/白文字）、**色觉无障碍**（deuteranopia 模拟后要求类别色仍可区分）、**视觉层次**（类间色彩距离度量）。

分类采用 Okabe-Ito / Tol 无障碍调色板，输出完整符号方案 JSON 与配色图。

## 核心算法

relative_luminance/contrast_ratio(WCAG,(L1+.05)/(L2+.05)) → simulate_deuteranopia 线性矩阵 → min_pairwise_separation 判定色觉安全 → best_text_color 选文字色 → optimize_symbology 组装方案。

## 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-map-symbology-optimizer.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（等间距分类）

```bash
python geoskill-map-symbology-optimizer.py --input landcover.tif --method equal_interval --classes 6
```

### 示例 3（Tol muted 调色板）

```bash
python geoskill-map-symbology-optimizer.py --input landcover.tif --palette tol-muted
```

### 示例 4（合成 4 类）

```bash
python geoskill-map-symbology-optimizer.py --bbox 116 39 117 40 --synthetic --classes 4
```

### 示例 5（分位数 + Okabe-Ito）

```bash
python geoskill-map-symbology-optimizer.py --input landcover.tif --method quantile --palette okabe-ito
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `symbology.png` | PNG | 配色分类图+图例（主产物） |
| `classes.tif` | GeoTIFF | 类别索引栅格（可验证产物） |
| `symbology.json` | JSON | 断点/配色/对比度/色觉安全 QA |

每次运行还会产出 `output-manifest.json`（运行清单）。

## 数据源 / Source

本地 GeoTIFF / 矢量文件；`--synthetic` 模式生成物理一致的模拟数据，完全离线。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
