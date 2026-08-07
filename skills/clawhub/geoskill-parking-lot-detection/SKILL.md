---
name: geoskill-parking-lot-detection
description: 'Detect parking lots using asphalt spectral signature, regular row and column texture, and painted marking density.'
---

# 停车场检测 | Parking Lot Detection

Detects parking lots by fusing spectral, textural, and geometric features, supporting urban facility surveys and land-use mapping.

Core algorithm: asphalt score = low-brightness factor × low-vegetation factor (absolute scale); marking density extracts high-frequency bright lines via Sobel gradient + brightness threshold; regularity characterizes row/column periodicity with the ratio of local to global variance; the composite score is a weighted sum clipped to [0,1], and thresholding segments out the parking lots.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## Usage / 使用方法

### Basic usage

```bash
python geoskill-parking-lot-detection.py --bbox 116.0 39.0 117.0 40.0 [other options]
```

### Examples

#### Example 1 (synthetic data (offline))

```bash
python geoskill-parking-lot-detection.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### Example 2 (use case 2)

```bash
python geoskill-parking-lot-detection.py --input multispectral.tif --output-dir ./out
```

#### Example 3 (use case 3)

```bash
python geoskill-parking-lot-detection.py --bbox 121.0 31.0 122.0 32.0 --threshold 0.5 --output-dir ./out --quiet
```

#### Example 4 (use case 4)

```bash
python geoskill-parking-lot-detection.py --input ms.tif --regularity-block 24 --output-dir ./out
```

#### Example 5 (use case 5)

```bash
python geoskill-parking-lot-detection.py --bbox 116.0 39.0 117.0 40.0 --synthetic --threshold 0.35 --output-dir ./out --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `parking_score.tif` | GeoTIFF | Two bands: band1=parking score, band2=classification mask |
| `parking_stats.json` | JSON | Means of score/marking/regularity, parking-lot proportion |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

Local multispectral GeoTIFF (Red, NIR); `--synthetic` mode simulates parking lots with regular markings plus vegetation/roof control areas.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is performed locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-parking-lot-detection
description: 'Detect parking lots using asphalt spectral signature, regular row and column texture, and painted marking density.'
---

# 停车场检测 | Parking Lot Detection

融合光谱、纹理与几何特征检测停车场，服务于城市设施调查与用地制图。

核心算法：沥青分数 = 低亮度因子 × 低植被因子（绝对标度）；标线密度由 Sobel 梯度 + 亮度阈值提取高频亮线；规则性用局部方差/全局方差之比刻画行列周期性；综合评分 = 加权和，裁剪到 [0,1]，阈值分割出停车场。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-parking-lot-detection.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例

#### 示例 1（合成数据（离线））

```bash
python geoskill-parking-lot-detection.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### 示例 2（用法 2）

```bash
python geoskill-parking-lot-detection.py --input multispectral.tif --output-dir ./out
```

#### 示例 3（用法 3）

```bash
python geoskill-parking-lot-detection.py --bbox 121.0 31.0 122.0 32.0 --threshold 0.5 --output-dir ./out --quiet
```

#### 示例 4（用法 4）

```bash
python geoskill-parking-lot-detection.py --input ms.tif --regularity-block 24 --output-dir ./out
```

#### 示例 5（用法 5）

```bash
python geoskill-parking-lot-detection.py --bbox 116.0 39.0 117.0 40.0 --synthetic --threshold 0.35 --output-dir ./out --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `parking_score.tif` | GeoTIFF | 双波段：band1=停车场评分，band2=分类掩膜 |
| `parking_stats.json` | JSON | 评分/标线/规则性均值、停车场比例 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地多光谱 GeoTIFF（Red, NIR）；`--synthetic` 模式模拟含规则标线的停车场与植被/屋顶对照区。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
