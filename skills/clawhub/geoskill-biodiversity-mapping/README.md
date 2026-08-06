# Biodiversity Mapping (geoskill-biodiversity-mapping)

> Based on the habitat heterogeneity hypothesis, estimates the spatial distribution of species richness from three proxy types: NDVI productivity, textural structural heterogeneity and terrain roughness. Maps species richness proxies from NDVI, texture and terrain heterogeneity. Outputs species richness and habitat quality GeoTIFFs + a parameters JSON.

---

## 1. Overview

Vegetation productivity (NDVI), habitat structural diversity (local standard deviation of NDVI) and terrain heterogeneity (DEM gradient magnitude) are the most commonly used remote sensing proxies for biodiversity. This skill normalizes each of the three proxies and fuses them with weights into a "habitat quality" index, which is then mapped to relative species richness through the saturation curve S = Smax·(1 - exp(-k·q)) to avoid linear extrapolation. Applicable scenarios: protected area siting, ecological baseline surveys, and identification of priority areas for biodiversity conservation. Two weighting schemes are supported: heterogeneity (emphasizing structural/terrain diversity) and productivity (emphasizing energy availability).

## 2. Features

Vegetation productivity (NDVI), habitat structural diversity (local standard deviation of NDVI) and terrain heterogeneity (DEM gradient magnitude) are the most commonly used remote sensing proxies for biodiversity. This skill normalizes each of the three proxies and fuses them with weights into a "habitat quality" index, which is then mapped to relative species richness through the saturation curve S = Smax·(1 - exp(-k·q)) to avoid linear extrapolation. Applicable scenarios: protected area siting, ecological baseline surveys, and identification of priority areas for biodiversity conservation. Two weighting schemes are supported: heterogeneity (emphasizing structural/terrain diversity) and productivity (emphasizing energy availability).

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-biodiversity-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `species_richness.tif` | GeoTIFF (float32) | Relative species richness [0, Smax], EPSG:4326 |
| `habitat_quality.tif` | GeoTIFF (float32) | Habitat quality index q ∈ [0,1] |
| `richness_params.json` | JSON | Parameters such as weights/window/proxy means |
| `output-manifest.json` | JSON | Run manifest (input/output/QA/software versions) |


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

# 生物多样性制图（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-biodiversity-mapping
description: '基于生境异质性假说，用 NDVI 生产力、纹理结构异质性与地形粗糙度三类代理估算物种丰富度空间分布。Maps species richness proxies from NDVI, texture and terrain heterogeneity. 输出物种丰富度与生境质量 GeoTIFF + 参数 JSON。'
---

# 生物多样性制图 | Biodiversity Mapping

植被生产力（NDVI）、生境结构多样性（NDVI 局部标准差）与地形异质性（DEM 梯度模）是生物多样性最常用的遥感代理量。本 skill 将三者各自归一化后加权融合为「生境质量」，再经饱和曲线 S = Smax·(1 - exp(-k·q)) 映射为相对物种丰富度，避免线性外推。

适用场景：保护区选址、生态本底调查、生物多样性保护优先区识别。支持 heterogeneity（强调结构/地形多样性）与 productivity（强调能量可得性）两种加权方案。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 示例 1：合成数据离线运行

```bash
python geoskill-biodiversity-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### 示例 2：真实多光谱影像（band1=红, band2=近红外, band3=DEM）

```bash
python geoskill-biodiversity-mapping.py --input scene.tif --method heterogeneity --output-dir ./real
```

### 示例 3：生产力主导模式

```bash
python geoskill-biodiversity-mapping.py --bbox 121.0 31.0 122.0 32.0 --synthetic --method productivity --output-dir ./prod
```

### 示例 4：加大纹理窗口 + 调高饱和上限

```bash
python geoskill-biodiversity-mapping.py --bbox 116 39 117 40 --synthetic --window 9 --s-max 300 --k 2.5 --output-dir ./tuned
```

### 示例 5：静默批量模式

```bash
python geoskill-biodiversity-mapping.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `species_richness.tif` | GeoTIFF (float32) | 相对物种丰富度 [0, Smax]，EPSG:4326 |
| `habitat_quality.tif` | GeoTIFF (float32) | 生境质量指数 q ∈ [0,1] |
| `richness_params.json` | JSON | 权重/窗口/代理量均值等参数 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

本地多光谱 GeoTIFF（band1=红、band2=近红外、band3 可选 DEM）；合成模式本地生成植被/水体/裸土场景与起伏 DEM，无外部数据源。

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
