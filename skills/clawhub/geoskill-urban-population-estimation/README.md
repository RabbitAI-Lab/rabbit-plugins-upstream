# Urban Population Estimation (geoskill-urban-population-estimation)

> Estimate population density from building volume, residential ratio, night-light correction and land-cover weights with total conservation.

---

## 1. Overview

Estimates the spatial distribution of population density from building volume, night lights and land-use weights to support population spatialization and urban research. Core algorithm: building volume = footprint area × height; residential weight = volume × night-light correction × LULC weight (water/vegetation weight = 0); population is allocated by normalized weights, density = weight/Σweight × total population / pixel area. Key property: Σ(density × pixel area) = total population, i.e., the total population is strictly conserved.

## 2. Features

Estimates the spatial distribution of population density from building volume, night lights and land-use weights to support population spatialization and urban research. Core algorithm: building volume = footprint area × height; residential weight = volume × night-light correction × LULC weight (water/vegetation weight = 0); population is allocated by normalized weights, density = weight/Σweight × total population / pixel area. Key property: Σ(density × pixel area) = total population, i.e., the total population is strictly conserved.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-urban-population-estimation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `population_density.tif` | GeoTIFF | Population density (people per unit area) |
| `population_stats.json` | JSON | Target/estimated total population, conservation error, mean/max density |
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

# 城市人口估算（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-urban-population-estimation
description: 'Estimate population density from building volume, residential ratio, night-light correction and land-cover weights with total conservation.'
---

# 城市人口估算 | Urban Population Estimation

从建筑体积、夜光与土地利用权重估算人口密度空间分布，服务于人口空间化与城市研究。

核心算法：建筑体积 = 足迹面积×高度；居住权重 = 体积×夜光校正×LULC 权重（水体/植被权重为 0）；人口按权重归一化分配，density = weight/Σweight × 总人口/像元面积。关键性质：Σ(density×像元面积) = 总人口，人口总量严格守恒。

## 依赖

```bash
pip install 'numpy' 'rasterio'
```

## 使用方法

### 基本用法

```bash
python geoskill-urban-population-estimation.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例

#### 示例 1（合成数据（离线））

```bash
python geoskill-urban-population-estimation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### 示例 2（用法 2）

```bash
python geoskill-urban-population-estimation.py --input height.tif --nightlight nl.tif --lulc lulc.tif --output-dir ./out
```

#### 示例 3（用法 3）

```bash
python geoskill-urban-population-estimation.py --bbox 121.0 31.0 122.0 32.0 --total-population 500000 --output-dir ./out --quiet
```

#### 示例 4（用法 4）

```bash
python geoskill-urban-population-estimation.py --input height.tif --total-population 200000 --pixel-size 30 --output-dir ./out
```

#### 示例 5（用法 5）

```bash
python geoskill-urban-population-estimation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --total-population 80000 --output-dir ./out --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `population_density.tif` | GeoTIFF | 人口密度（人/单位面积） |
| `population_stats.json` | JSON | 目标/估算总人口、守恒误差、密度均值/最大值 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地建筑高度 + 夜光 + LULC GeoTIFF；`--synthetic` 模式模拟居住区与水体/植被区的对照场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
