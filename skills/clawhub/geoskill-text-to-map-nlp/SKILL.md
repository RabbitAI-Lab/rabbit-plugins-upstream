---
name: geoskill-text-to-map-nlp
description: '自然语言关键词解析+参数提取+matplotlib渲染，输出专题地图PNG/GeoJSON（离线numpy等价实现）'
---

# 自然语言生成地图 | Natural Language to Map

Automatically generates a thematic map from a single natural-language sentence (e.g., "generate a nighttime-light map of Shanghai"): parse the intent to select the layer type (vegetation / elevation / nighttime lights / water / temperature / land features) and color scheme, render a map PNG with geographic extent, color bar, and title, and output the layer GeoTIFF and footprint GeoJSON.

This skill is an **offline numpy-equivalent implementation** of an LLM/NL2Map system: with no large-model or network dependency, it reproduces the natural-language mapping pipeline via keyword-rule parsing (the equivalent of intent recognition + slot filling) → physically consistent layer synthesis → matplotlib Agg rendering; the parsed results (layer / color scheme / place name / title) are written to disk for auditability.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy scikit-learn geopandas shapely matplotlib
```

## Usage / 使用方法

### Example 1 (synthetic data, offline)

```bash
python geoskill-text-to-map-nlp.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2: Synthetic-layer mapping (offline)

```bash
python geoskill-text-to-map-nlp.py --bbox 116.0 39.0 117.0 40.0 --synthetic --query "Beijing vegetation index" --output-dir ./out
```

### Example 3: Layer selection via natural language

```bash
python geoskill-text-to-map-nlp.py --bbox 121.0 31.0 122.0 32.0 --query "Shanghai nighttime light distribution" --output-dir ./out
```

### Example 4: Force-specify the layer type

```bash
python geoskill-text-to-map-nlp.py --bbox 116.0 39.0 117.0 40.0 --layer elevation --query "terrain map" --output-dir ./out
```

### Example 5: Direct rendering of a real raster

```bash
python geoskill-text-to-map-nlp.py --input ndvi.tif --query "NDVI of the study area" --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `map.png` | PNG | Rendered thematic map (color bar + title + lat/lon axes) |
| `layer.tif` | GeoTIFF | Map layer raster |
| `footprint.geojson` | GeoJSON | Map extent boundary polygon |
| `parsed_query.json` | JSON | Parsed layer / color scheme / place name / title parameters |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/exit code) |

## Data Source / 数据源 / Source

A local GeoTIFF (used directly as the layer), or a simulated layer of the corresponding type synthesized from the parsed `--query` result.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is performed locally; no user data is uploaded.

## License / License

MIT

---


<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-text-to-map-nlp
description: '自然语言关键词解析+参数提取+matplotlib渲染，输出专题地图PNG/GeoJSON（离线numpy等价实现）'
---

# 自然语言生成地图 | Natural Language to Map

用一句自然语言（如"生成上海的夜间灯光地图"）自动生成专题地图：解析意图选择图层类型（植被/高程/灯光/水体/温度/地物）与配色，渲染带地理范围、色条与标题的地图 PNG，同时输出图层 GeoTIFF 与边界 GeoJSON。

本 skill 是 LLM/NL2Map 系统的**离线 numpy 等价实现**：不依赖大模型与网络，用"关键词规则解析（意图识别 + 槽位填充的等价物）-> 物理一致的图层合成 -> matplotlib Agg 渲染"复现自然语言制图流程；解析结果（图层/配色/地名/标题）落盘可审计。

## 依赖

```bash
pip install numpy rasterio scipy scikit-learn geopandas shapely matplotlib
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-text-to-map-nlp.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2：合成图层制图（离线）

```bash
python geoskill-text-to-map-nlp.py --bbox 116.0 39.0 117.0 40.0 --synthetic --query "北京植被指数" --output-dir ./out
```

### 示例 3：自然语言选图层

```bash
python geoskill-text-to-map-nlp.py --bbox 121.0 31.0 122.0 32.0 --query "上海夜间灯光分布" --output-dir ./out
```

### 示例 4：强制指定图层类型

```bash
python geoskill-text-to-map-nlp.py --bbox 116.0 39.0 117.0 40.0 --layer elevation --query "地形图" --output-dir ./out
```

### 示例 5：真实栅格直接渲染

```bash
python geoskill-text-to-map-nlp.py --input ndvi.tif --query "研究区 NDVI" --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `map.png` | PNG | 渲染好的专题地图（色条 + 标题 + 经纬度轴） |
| `layer.tif` | GeoTIFF | 地图图层栅格 |
| `footprint.geojson` | GeoJSON | 地图范围边界多边形 |
| `parsed_query.json` | JSON | 解析出的图层/配色/地名/标题参数 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/退出码） |

## 数据源 / Source

本地 GeoTIFF（直接作为图层），或按 --query 解析结果合成对应类型的模拟图层。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
