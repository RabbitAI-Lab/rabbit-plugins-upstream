---
name: geoskill-environmental-impact-assessment
description: '多压力因子归一化加权叠加得综合影响指数，独立概率模型估算累积效应，按阈值划分5 级影响等级。Assesses environmental impact grades by multi-factor overlay and cumulative effects. 输出影响指数与等级 GeoTIFF。'
---

# 环境影响评价 | Environmental Impact Assessment

Four pressure factors (pollution, land-use change, noise, and habitat fragmentation) are each min-max normalized and combined by weighted overlay using sensitivity weights (0.30/0.25/0.25/0.20); cumulative effects are estimated with the independent-probability model C = 1 − Π(1 − Ii), ensuring that the multi-project superposition does not exceed 1 and is ≥ any single project; the final index = 0.5 × weighted overlay + 0.5 × cumulative effect, classified by thresholds of 0.1/0.3/0.5/0.7 into five grades: negligible/slight/moderate/significant/severe.

Use cases: environmental impact assessment (EIA) of construction projects, planning-level EIA, and cumulative environmental impact screening.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy
```

## Usage / 使用方法

### Example 1: synthetic four-factor pressure scenario

```bash
python geoskill-environmental-impact-assessment.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### Example 2: real multi-band pressure raster (each band = one pressure factor)

```bash
python geoskill-environmental-impact-assessment.py --input pressures.tif --output-dir ./real
```

### Example 3: different region

```bash
python geoskill-environmental-impact-assessment.py --bbox 121 31 122 32 --synthetic --output-dir ./shanghai
```

### Example 4: tiny region for quick validation

```bash
python geoskill-environmental-impact-assessment.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./tiny
```

### Example 5: silent batch run

```bash
python geoskill-environmental-impact-assessment.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `impact_index.tif` | GeoTIFF (float32) | Composite impact index ∈ [0,1], EPSG:4326 |
| `impact_grade.tif` | GeoTIFF (float32) | Impact grade 0-4 |
| `eia_params.json` | JSON | Weights, thresholds, pixel counts per grade |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/software versions) |

## Data Source / 数据源 / Source

Local GeoTIFF (multi-band pressure factors, optional); the independent-probability model for cumulative effects is a published EIA method; synthetic mode generates an urban-gradient pressure field locally with no external data sources.

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default and makes no network requests
- `--synthetic` mode reads no external data
- All computation is done locally; user data is never uploaded

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-environmental-impact-assessment
description: '多压力因子归一化加权叠加得综合影响指数，独立概率模型估算累积效应，按阈值划分5 级影响等级。Assesses environmental impact grades by multi-factor overlay and cumulative effects. 输出影响指数与等级 GeoTIFF。'
---

# 环境影响评价 | Environmental Impact Assessment

四个压力因子（污染、土地利用变化、噪声、生境破碎化）各自 min-max 归一化后按敏感度权重（0.30/0.25/0.25/0.20）加权叠加；累积效应用独立概率模型 C = 1 - Π(1-Ii)，保证多项目叠加不超过 1 且 ≥ 任一单独项目；最终指数 = 0.5×加权叠加 + 0.5×累积效应，按 0.1/0.3/0.5/0.7 阈值分为可忽略/轻微/中等/显著/严重 5 级。

适用场景：建设项目环评、规划环评、累积环境影响筛查。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 示例 1：合成四因子压力场景

```bash
python geoskill-environmental-impact-assessment.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### 示例 2：真实多波段压力栅格（每波段=一个压力因子）

```bash
python geoskill-environmental-impact-assessment.py --input pressures.tif --output-dir ./real
```

### 示例 3：不同区域

```bash
python geoskill-environmental-impact-assessment.py --bbox 121 31 122 32 --synthetic --output-dir ./shanghai
```

### 示例 4：极小区域快速验证

```bash
python geoskill-environmental-impact-assessment.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./tiny
```

### 示例 5：静默批量

```bash
python geoskill-environmental-impact-assessment.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `impact_index.tif` | GeoTIFF (float32) | 综合影响指数 ∈ [0,1]，EPSG:4326 |
| `impact_grade.tif` | GeoTIFF (float32) | 影响等级 0-4 |
| `eia_params.json` | JSON | 权重、阈值、等级像元计数 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

本地 GeoTIFF（多波段压力因子，可选）；累积效应独立概率模型为公开环评方法；合成模式本地生成城市梯度压力场，无外部数据源。

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
