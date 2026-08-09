---
name: geoskill-urban-growth-boundary
description: 'Delineate urban growth boundaries from historical expansion rate and direction plus terrain, cropland and ecological constraints.'
---

# 城市增长边界 | Urban Growth Boundary

Delineates urban growth boundaries (UGB) from historical expansion and multi-source constraints, supporting territorial spatial planning and growth management.

Core algorithm: relative annual expansion rate = (A2−A1)/A1/number of years; the expansion trend is characterized by the smoothed difference of the built-up areas between the two epochs; constraint penalty = weighted sum of slope/cropland/ecological factors ∈ [0,1]; growth suitability = trend × (1−penalty) ∈ [0,1], tending to 0 on steep slopes and ecologically sensitive areas; the outer edge of contiguous areas whose suitability exceeds the threshold forms the growth boundary.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-urban-growth-boundary.py --bbox 116.0 39.0 117.0 40.0 [other parameters]
```

### Examples

#### Example 1 (Synthetic Data (Offline))

```bash
python geoskill-urban-growth-boundary.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### Example 2 (Usage 2)

```bash
python geoskill-urban-growth-boundary.py --input built_t2.tif --built-t1 built_t1.tif --years 10 --output-dir ./out
```

#### Example 3 (Usage 3)

```bash
python geoskill-urban-growth-boundary.py --bbox 121.0 31.0 122.0 32.0 --threshold 0.4 --output-dir ./out --quiet
```

#### Example 4 (Usage 4)

```bash
python geoskill-urban-growth-boundary.py --input built_t2.tif --built-t1 built_t1.tif --years 5 --output-dir ./out
```

#### Example 5 (Usage 5)

```bash
python geoskill-urban-growth-boundary.py --bbox 116.0 39.0 117.0 40.0 --synthetic --threshold 0.25 --output-dir ./out --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `growth_suitability.tif` | GeoTIFF | Two bands: band1=growth suitability, band2=boundary mask |
| `growth_stats.json` | JSON | Two-epoch areas, expansion rate, mean suitability, boundary ratio |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

Local two-epoch built-up area GeoTIFFs (+ constraint rasters); `--synthetic` mode simulates a scenario of eastward expansion with steep slopes to the north, cropland to the south and ecological constraints to the west.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; user data is never uploaded.

## License / License

MIT

---


<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-urban-growth-boundary
description: 'Delineate urban growth boundaries from historical expansion rate and direction plus terrain, cropland and ecological constraints.'
---

# 城市增长边界 | Urban Growth Boundary

从历史扩张与多源约束划定城市增长边界（UGB），服务于国土空间规划与增长管理。

核心算法：相对年均扩张速率 = (A2−A1)/A1/年数；扩张趋势由两期建成区差值平滑表征；约束惩罚 = 坡度/耕地/生态加权和 ∈ [0,1]；增长适宜性 = 趋势×(1−惩罚) ∈ [0,1]，陡坡+生态敏感区趋于 0；适宜性高于阈值的连片区域外缘即增长边界。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-urban-growth-boundary.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例

#### 示例 1（合成数据（离线））

```bash
python geoskill-urban-growth-boundary.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### 示例 2（用法 2）

```bash
python geoskill-urban-growth-boundary.py --input built_t2.tif --built-t1 built_t1.tif --years 10 --output-dir ./out
```

#### 示例 3（用法 3）

```bash
python geoskill-urban-growth-boundary.py --bbox 121.0 31.0 122.0 32.0 --threshold 0.4 --output-dir ./out --quiet
```

#### 示例 4（用法 4）

```bash
python geoskill-urban-growth-boundary.py --input built_t2.tif --built-t1 built_t1.tif --years 5 --output-dir ./out
```

#### 示例 5（用法 5）

```bash
python geoskill-urban-growth-boundary.py --bbox 116.0 39.0 117.0 40.0 --synthetic --threshold 0.25 --output-dir ./out --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `growth_suitability.tif` | GeoTIFF | 双波段：band1=增长适宜性，band2=边界掩膜 |
| `growth_stats.json` | JSON | 两期面积、扩张速率、平均适宜性、边界比例 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地双期建成区 GeoTIFF（+ 约束栅格）；`--synthetic` 模式模拟向东扩张 + 北陡坡/南耕地/西生态约束的场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
