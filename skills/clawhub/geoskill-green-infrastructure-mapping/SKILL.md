---
name: geoskill-green-infrastructure-mapping
description: 'Map green infrastructure from high-resolution NDVI, tree crown detection, green-space classification and patch connectivity.'
---

# 绿色基础设施制图 | Green Infrastructure Mapping

Maps green infrastructure (green spaces, trees) from high-resolution multispectral imagery to support ecological network assessment and green-space planning.

Core algorithm: NDVI = (NIR−Red)/(NIR+Red) with threshold segmentation of green spaces; local-maxima detection on the NDVI field counts tree-crown candidates; connectivity index = largest connected patch area / total green-space area ∈ [0,1], where higher values indicate better-connected green spaces. A single connected block yields 1, while fragmented patterns yield values below 1.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-green-infrastructure-mapping.py --bbox 116.0 39.0 117.0 40.0 [other options]
```

### Examples

#### Example 1 (Synthetic Data (Offline))

```bash
python geoskill-green-infrastructure-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### Example 2 (Usage 2)

```bash
python geoskill-green-infrastructure-mapping.py --input multispectral.tif --output-dir ./out
```

#### Example 3 (Usage 3)

```bash
python geoskill-green-infrastructure-mapping.py --bbox 121.0 31.0 122.0 32.0 --ndvi-threshold 0.35 --output-dir ./out --quiet
```

#### Example 4 (Usage 4)

```bash
python geoskill-green-infrastructure-mapping.py --input ms.tif --ndvi-threshold 0.25 --output-dir ./out
```

#### Example 5 (Usage 5)

```bash
python geoskill-green-infrastructure-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `green_infrastructure.tif` | GeoTIFF | Two bands: band1=NDVI, band2=green-space mask |
| `green_stats.json` | JSON | Mean NDVI, green-space fraction, tree count, connectivity index, patch count |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

Local multispectral GeoTIFF (Red, NIR); `--synthetic` mode simulates a scene of connected green spaces, scattered tree crowns, and an impervious background.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
