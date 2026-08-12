# Spatial Storytelling / Story Map (geoskill-spatial-storytelling)

> Weave multiple maps, text and charts into a scroll-driven storytelling HTML page

---

## 1. Overview

Weaves multiple maps, textual explanations and statistical charts into a **scrollytelling** HTML page: each chapter contains an embedded map, a narrative paragraph and an SVG line chart, revealed chapter by chapter as the user scrolls — suitable for data journalism and science-communication posts. Each band of a multi-band GeoTIFF is treated as one chapter; synthetic mode generates an urban expansion time series.

## 2. Features

Weaves multiple maps, textual explanations and statistical charts into a **scrollytelling** HTML page: each chapter contains an embedded map, a narrative paragraph and an SVG line chart, revealed chapter by chapter as the user scrolls — suitable for data journalism and science-communication posts. Each band of a multi-band GeoTIFF is treated as one chapter; synthetic mode generates an urban expansion time series.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-spatial-storytelling.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `story.html` | HTML | Scroll-driven storytelling page (primary output) |
| `story.json` | JSON | Chapter structure and statistics (verifiable output) |
| `story_stack.tif` | GeoTIFF | Multi-epoch stack |

Each run also produces `output-manifest.json` (run manifest).

## 6. Technical Principle

Per-epoch processing: render_band_png_b64(colormap) → line_chart_svg trend chart → build_section validation → build_story_html assembly (sticky map + chapter cards + navigation).

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 空间叙事 / 故事地图（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-spatial-storytelling
description: 'Weave multiple maps, text and charts into a scroll-driven storytelling HTML page'
---

# 空间叙事 / 故事地图 | Spatial Storytelling

把多幅地图、文字解说与统计图表编织成**滚动叙事（scrollytelling）** HTML：每个章节含一幅内嵌地图、一段叙述与一张 SVG 折线图，随滚动逐章呈现，适合数据新闻与科普推文。

多波段 GeoTIFF 每波段视为一章；合成模式生成城市扩张时序。

## 核心算法

逐期 render_band_png_b64(colormap) → line_chart_svg 趋势图 → build_section 校验 → build_story_html(sticky 地图+章节卡片+导航) 组装。

## 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-spatial-storytelling.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（自定义标题/副标题）

```bash
python geoskill-spatial-storytelling.py --input series.tif --title "城市扩张三十年" --subtitle "1990-2020"
```

### 示例 3（4 章合成故事）

```bash
python geoskill-spatial-storytelling.py --bbox 116 39 117 40 --synthetic --chapters 4
```

### 示例 4（章节前缀）

```bash
python geoskill-spatial-storytelling.py --bbox 116 39 117 40 --synthetic --chapter-prefix "阶段"
```

### 示例 5（地形配色）

```bash
python geoskill-spatial-storytelling.py --input series.tif --cmap terrain
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `story.html` | HTML | 滚动叙事页面（主产物） |
| `story.json` | JSON | 章节结构与统计（可验证产物） |
| `story_stack.tif` | GeoTIFF | 多期 stack |

每次运行还会产出 `output-manifest.json`（运行清单）。

## 数据源 / Source

本地 GeoTIFF / 矢量文件；`--synthetic` 模式生成物理一致的模拟数据，完全离线。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
