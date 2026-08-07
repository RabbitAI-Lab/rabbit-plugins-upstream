# Green Infrastructure Mapping (geoskill-green-infrastructure-mapping)

> Map green infrastructure from high-resolution NDVI, tree crown detection, green-space classification and patch connectivity.

---

## 1. Overview

Maps green infrastructure (green spaces, trees) from high-resolution multispectral imagery to support ecological network assessment and green space planning. Core algorithm: NDVI = (NIR−Red)/(NIR+Red) with threshold-based green space segmentation; local maximum detection on the NDVI field to count tree crown candidates; connectivity index = largest connected patch area / total green space area ∈ [0,1], where higher values indicate more connected green space. A single connected patch yields 1, while fragmented ones yield values less than 1.

## 2. Features

Maps green infrastructure (green spaces, trees) from high-resolution multispectral imagery to support ecological network assessment and green space planning. Core algorithm: NDVI = (NIR−Red)/(NIR+Red) with threshold-based green space segmentation; local maximum detection on the NDVI field to count tree crown candidates; connectivity index = largest connected patch area / total green space area ∈ [0,1], where higher values indicate more connected green space. A single connected patch yields 1, while fragmented ones yield values less than 1.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-green-infrastructure-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `green_infrastructure.tif` | GeoTIFF | Two bands: band1=NDVI, band2=green space mask |
| `green_stats.json` | JSON | Mean NDVI, green space ratio, tree count, connectivity index, patch count |
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

# 绿色基础设施制图（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-green-infrastructure-mapping
description: 'Map green infrastructure from high-resolution NDVI, tree crown detection, green-space classification and patch connectivity.'
---

# 绿色基础设施制图 | Green Infrastructure Mapping

从高分辨率多光谱影像制图绿色基础设施（绿地、树木），服务于生态网络评估与绿地规划。

核心算法：NDVI = (NIR−Red)/(NIR+Red)，阈值分割绿地；对 NDVI 场做局部极大值检测统计树冠候选数；连通性指数 = 最大连通斑块面积/总绿地面积 ∈ [0,1]，值越高表示绿地越连通。单一连通块为 1，碎片化小于 1。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-green-infrastructure-mapping.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例

#### 示例 1（合成数据（离线））

```bash
python geoskill-green-infrastructure-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### 示例 2（用法 2）

```bash
python geoskill-green-infrastructure-mapping.py --input multispectral.tif --output-dir ./out
```

#### 示例 3（用法 3）

```bash
python geoskill-green-infrastructure-mapping.py --bbox 121.0 31.0 122.0 32.0 --ndvi-threshold 0.35 --output-dir ./out --quiet
```

#### 示例 4（用法 4）

```bash
python geoskill-green-infrastructure-mapping.py --input ms.tif --ndvi-threshold 0.25 --output-dir ./out
```

#### 示例 5（用法 5）

```bash
python geoskill-green-infrastructure-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `green_infrastructure.tif` | GeoTIFF | 双波段：band1=NDVI，band2=绿地掩膜 |
| `green_stats.json` | JSON | 平均 NDVI、绿地比例、树木数、连通性指数、斑块数 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地多光谱 GeoTIFF（Red, NIR）；`--synthetic` 模式模拟连通绿地 + 散布树冠 + 不透水背景的场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
