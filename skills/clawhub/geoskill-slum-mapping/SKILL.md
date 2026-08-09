---
name: geoskill-slum-mapping
description: 'Map slums and shanty areas using a multi-indicator index of texture, building density, night light and population density.'
---

# 贫民窟/棚户区制图 | Slum Mapping

Maps slums / shanty areas using a multi-indicator composite index, supporting living-environment monitoring and targeted governance.

Core algorithm: the slum index SI = w_tex×texture + w_den×building density + w_pop×population density − w_nl×night light, where each factor is normalized to an absolute physical scale and clipped to [0, 1]. The index increases with texture / density / population and decreases with night light; high texture + high density + dark night light + high population → high index, while formally planned areas (smooth / bright night light) → low index.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-slum-mapping.py --bbox 116.0 39.0 117.0 40.0 [other parameters]
```

### Examples

#### Example 1 (Synthetic Data (Offline))

```bash
python geoskill-slum-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### Example 2 (Usage 2)

```bash
python geoskill-slum-mapping.py --input scene.tif --nightlight nl.tif --population pop.tif --output-dir ./out
```

#### Example 3 (Usage 3)

```bash
python geoskill-slum-mapping.py --bbox 121.0 31.0 122.0 32.0 --threshold 0.55 --output-dir ./out --quiet
```

#### Example 4 (Usage 4)

```bash
python geoskill-slum-mapping.py --input scene.tif --kernel-size 7 --output-dir ./out
```

#### Example 5 (Usage 5)

```bash
python geoskill-slum-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --threshold 0.45 --output-dir ./out --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `slum_index.tif` | GeoTIFF | Two bands: band1 = slum index, band2 = classification mask |
| `slum_stats.json` | JSON | Mean index, slum fraction, mean texture, threshold |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

Local multi-source rasters (grayscale texture source + density + night light + population); `--synthetic` mode simulates a scene split evenly between shanty areas and formally planned areas.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; no user data is uploaded.

## License / License

MIT

---


<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-slum-mapping
description: 'Map slums and shanty areas using a multi-indicator index of texture, building density, night light and population density.'
---

# 贫民窟/棚户区制图 | Slum Mapping

用多指标综合指数制图贫民窟/棚户区，服务于人居环境监测与精准治理。

核心算法：贫民窟指数 SI = w_tex×纹理 + w_den×建筑密度 + w_pop×人口密度 − w_nl×夜光，各因子用绝对物理标度归一化后裁剪到 [0,1]。指数随纹理/密度/人口递增、随夜光递减；高纹理 + 高密度 + 暗夜光 + 高人口 → 高指数，正规规划区（平滑/亮夜光）→ 低指数。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-slum-mapping.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例

#### 示例 1（合成数据（离线））

```bash
python geoskill-slum-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### 示例 2（用法 2）

```bash
python geoskill-slum-mapping.py --input scene.tif --nightlight nl.tif --population pop.tif --output-dir ./out
```

#### 示例 3（用法 3）

```bash
python geoskill-slum-mapping.py --bbox 121.0 31.0 122.0 32.0 --threshold 0.55 --output-dir ./out --quiet
```

#### 示例 4（用法 4）

```bash
python geoskill-slum-mapping.py --input scene.tif --kernel-size 7 --output-dir ./out
```

#### 示例 5（用法 5）

```bash
python geoskill-slum-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --threshold 0.45 --output-dir ./out --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `slum_index.tif` | GeoTIFF | 双波段：band1=贫民窟指数，band2=分类掩膜 |
| `slum_stats.json` | JSON | 平均指数、贫民窟比例、平均纹理、阈值 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地多源栅格（灰度纹理源 + 密度 + 夜光 + 人口）；`--synthetic` 模式模拟棚户区与正规规划区各半的场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
