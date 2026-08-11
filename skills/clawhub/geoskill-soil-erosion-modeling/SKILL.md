---
name: geoskill-soil-erosion-modeling
description: 'RUSLE 模型空间化估算土壤侵蚀模数：A = R×K×L×S×C×P，含降雨侵蚀力、土壤可蚀性、坡长坡度、植被覆盖与水保措施六因子。Computes soil erosion modulus with RUSLE (R K L S C P) spatialized factors. 输出侵蚀模数与强度分级 GeoTIFF。'
---

# 土壤侵蚀建模 | Soil Erosion Modeling

A = R × K × LS × C × P (t·ha⁻¹·yr⁻¹): R is estimated from mean annual rainfall × an intensity coefficient; K is looked up by soil texture (sand/loam/clay/silt, 0.05–0.42); LS uses the simplified Moore & Burch equation (flow accumulation × slope); C is derived from an exponential decay of NDVI (better vegetation cover, lower erosion, in [0.01, 1]); P is looked up by practice (no measures / contour tillage / terraces, 1.0/0.55/0.25). The erosion modulus is then classified into 5 grades from slight to extremely intense using the 500/2500/5000/8000 thresholds.

Use cases: soil and water conservation planning, erosion hotspot identification, and watershed sediment source analysis.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy
```

## Usage / 使用方法

### Example 1: Synthetic Rainfall/Terrain/Vegetation Scenario

```bash
python geoskill-soil-erosion-modeling.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### 示例 2：真实 6 波段输入（precip,slope,ndvi,soil,practice,flow）

```bash
python geoskill-soil-erosion-modeling.py --input rusle_inputs.tif --output-dir ./real
```

### Example 3: 10 m Resolution Pixels

```bash
python geoskill-soil-erosion-modeling.py --bbox 116 39 117 40 --synthetic --cell-size 10 --output-dir ./fine
```

### Example 4: Different Regions

```bash
python geoskill-soil-erosion-modeling.py --bbox 121 31 122 32 --synthetic --output-dir ./shanghai
```

### Example 5: Silent Batch Mode

```bash
python geoskill-soil-erosion-modeling.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `erosion_modulus.tif` | GeoTIFF (float32) | Erosion modulus (t·ha⁻¹·yr⁻¹), EPSG:4326 |
| `erosion_grade.tif` | GeoTIFF (float32) | Erosion intensity grade 0-4 |
| `rusle_params.json` | JSON | Factor means and per-grade pixel counts |
| `output-manifest.json` | JSON | Run manifest (input/output/QA/software versions) |

## Data Source / 数据源 / Source

Local GeoTIFF (optional 6-band factor input); the RUSLE factor equations and K/P reference values are taken from the USDA-published RUSLE handbook; synthetic mode is generated locally with no external data source.

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default and makes no network requests
- `--synthetic` mode reads no external data
- All computation is done locally; no user data is uploaded

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-soil-erosion-modeling
description: 'RUSLE 模型空间化估算土壤侵蚀模数：A = R×K×L×S×C×P，含降雨侵蚀力、土壤可蚀性、坡长坡度、植被覆盖与水保措施六因子。Computes soil erosion modulus with RUSLE (R K L S C P) spatialized factors. 输出侵蚀模数与强度分级 GeoTIFF。'
---

# 土壤侵蚀建模 | Soil Erosion Modeling

A = R × K × LS × C × P（t·ha⁻¹·yr⁻¹）：R 由年均降雨×强度系数估算；K 按砂/壤/黏/粉砂质地查表（0.05-0.42）；LS 用 Moore & Burch 简化式（汇流累积×坡度）；C 由 NDVI 指数衰减（植被越好侵蚀越小，取值 [0.01,1]）；P 按无措施/等高耕作/梯田查表（1.0/0.55/0.25）。侵蚀模数再按 500/2500/5000/8000 阈值分为微度至极强烈 5 级。

适用场景：水土保持规划、侵蚀热点识别、流域泥沙来源分析。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 示例 1：合成降雨/地形/植被场景

```bash
python geoskill-soil-erosion-modeling.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### 示例 2：真实 6 波段输入（precip,slope,ndvi,soil,practice,flow）

```bash
python geoskill-soil-erosion-modeling.py --input rusle_inputs.tif --output-dir ./real
```

### 示例 3：10 m 分辨率像元

```bash
python geoskill-soil-erosion-modeling.py --bbox 116 39 117 40 --synthetic --cell-size 10 --output-dir ./fine
```

### 示例 4：不同区域

```bash
python geoskill-soil-erosion-modeling.py --bbox 121 31 122 32 --synthetic --output-dir ./shanghai
```

### 示例 5：静默批量

```bash
python geoskill-soil-erosion-modeling.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `erosion_modulus.tif` | GeoTIFF (float32) | 侵蚀模数（t·ha⁻¹·yr⁻¹），EPSG:4326 |
| `erosion_grade.tif` | GeoTIFF (float32) | 侵蚀强度分级 0-4 |
| `rusle_params.json` | JSON | 各因子均值与分级像元计数 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

本地 GeoTIFF（6 波段因子输入，可选）；RUSLE 因子公式与 K/P 参考值取自USDA 公开发表的 RUSLE 手册；合成模式本地生成，无外部数据源。

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
