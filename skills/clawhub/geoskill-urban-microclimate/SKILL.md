---
name: geoskill-urban-microclimate
description: 'Analyze urban heat island intensity and ventilation index from land surface temperature, NDVI, impervious surface and building morphology.'
---

# 城市微气候分析 | Urban Microclimate Analysis

Analyzes urban microclimate from land surface temperature, vegetation, impervious surface and building morphology, supporting heat island mitigation and ventilation planning.

Core algorithm: LST modeling = baseline temperature + α×ISA − β×NDVI (impervious surfaces heat, vegetation cools through evapotranspiration); heat island intensity UHII = LST − rural reference temperature, positively correlated with ISA; ventilation index VI = SVF×(1−building density) ∈ [0,1] — high density combined with a low sky view factor indicates poor ventilation.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio'
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-urban-microclimate.py --bbox 116.0 39.0 117.0 40.0 [other parameters]
```

### Examples

#### Example 1 (Synthetic Data (Offline))

```bash
python geoskill-urban-microclimate.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### Example 2 (Usage 2)

```bash
python geoskill-urban-microclimate.py --input features.tif --output-dir ./out
```

#### Example 3 (Usage 3)

```bash
python geoskill-urban-microclimate.py --bbox 121.0 31.0 122.0 32.0 --rural-temp 23 --output-dir ./out --quiet
```

#### Example 4 (Usage 4)

```bash
python geoskill-urban-microclimate.py --input features.tif --alpha 12 --beta 5 --output-dir ./out
```

#### Example 5 (Usage 5)

```bash
python geoskill-urban-microclimate.py --bbox 116.0 39.0 117.0 40.0 --synthetic --base-temp 26 --output-dir ./out --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `microclimate.tif` | GeoTIFF | Three bands: band1=LST, band2=heat island intensity UHII, band3=ventilation index |
| `microclimate_stats.json` | JSON | Mean LST/UHII, max UHII, ventilation index, UHII-ISA correlation coefficient |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

Local four-band GeoTIFF (ISA, NDVI, building density, SVF); `--synthetic` mode simulates a center-to-suburb heat island gradient scenario.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; user data is never uploaded.

## License / License

MIT

---


<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-urban-microclimate
description: 'Analyze urban heat island intensity and ventilation index from land surface temperature, NDVI, impervious surface and building morphology.'
---

# 城市微气候分析 | Urban Microclimate Analysis

从地表温度、植被、不透水面与建筑形态分析城市微气候，服务于热岛缓解与通风规划。

核心算法：LST 建模 = 基准温度 + α×ISA − β×NDVI（不透水面加热、植被蒸散降温）；热岛强度 UHII = LST − 郊区参考温度，与 ISA 正相关；通风指数 VI = SVF×(1−建筑密度) ∈ [0,1]，密度高且天空可视因子低 → 通风差。

## 依赖

```bash
pip install 'numpy' 'rasterio'
```

## 使用方法

### 基本用法

```bash
python geoskill-urban-microclimate.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例

#### 示例 1（合成数据（离线））

```bash
python geoskill-urban-microclimate.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### 示例 2（用法 2）

```bash
python geoskill-urban-microclimate.py --input features.tif --output-dir ./out
```

#### 示例 3（用法 3）

```bash
python geoskill-urban-microclimate.py --bbox 121.0 31.0 122.0 32.0 --rural-temp 23 --output-dir ./out --quiet
```

#### 示例 4（用法 4）

```bash
python geoskill-urban-microclimate.py --input features.tif --alpha 12 --beta 5 --output-dir ./out
```

#### 示例 5（用法 5）

```bash
python geoskill-urban-microclimate.py --bbox 116.0 39.0 117.0 40.0 --synthetic --base-temp 26 --output-dir ./out --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `microclimate.tif` | GeoTIFF | 三波段：band1=LST，band2=热岛强度 UHII，band3=通风指数 |
| `microclimate_stats.json` | JSON | 平均 LST/UHII、最大 UHII、通风指数、UHII-ISA 相关系数 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地四波段 GeoTIFF（ISA, NDVI, 建筑密度, SVF）；`--synthetic` 模式模拟中心-郊区热岛梯度场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
