---
name: geoskill-multi-hazard-risk-assessment
description: '多灾种危险性×暴露度×脆弱性综合风险指数计算与分区'
---

# 多灾种综合风险评估 | Multi-Hazard Risk Assessment

Multiplies multiple single-hazard risks per pixel according to the IPCC risk triplet (hazard × exposure × vulnerability), then performs a weighted multi-hazard fusion to obtain a composite risk index in [0,1], which is classified by thresholds into five risk zones: low / moderate-low / moderate / moderate-high / high. If any factor is 0 (e.g., no exposure), the pixel risk is 0; the fusion result is a convex combination of the single-hazard risks, monotonically non-decreasing in every input.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy
```

## Usage / 使用方法

### Basic usage (synthetic data, offline)

```bash
python geoskill-multi-hazard-risk-assessment.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### More examples

```bash
python geoskill-multi-hazard-risk-assessment.py --bbox 116 39 117 40 --synthetic --output-dir ./out
python geoskill-multi-hazard-risk-assessment.py --input scene.tif --output-dir ./out
python geoskill-multi-hazard-risk-assessment.py --bbox 116 39 117 40 --hazards 5 --breaks 0.1 0.3 0.5 0.7 --synthetic --output-dir ./out
python geoskill-multi-hazard-risk-assessment.py --bbox 121 31 122 32 --synthetic --quiet --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `risk_index.tif` | GeoTIFF | Composite risk index [0,1] |
| `risk_zones.tif` | GeoTIFF | Risk zones (integer 0-4) |
| `risk_params.json` | JSON | Break thresholds / weights / per-hazard means |

Each run also produces `output-manifest.json` (run manifest including input/output/QA summary).

## Data Source / 数据源 / Source

Real mode reads a multi-band GeoTIFF (band1=hazard, band2=exposure, band3=vulnerability); synthetic mode generates multi-hazard scenes offline.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is performed locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-multi-hazard-risk-assessment
description: '多灾种危险性×暴露度×脆弱性综合风险指数计算与分区'
---

# 多灾种综合风险评估 | Multi-Hazard Risk Assessment

将多个单灾种风险按 IPCC 风险三元组（危险度 × 暴露度 × 脆弱性）逐像元相乘，再做多灾种加权融合，得到 [0,1] 的综合风险指数，并按阈值切分为低/中低/中/中高/高 5 个风险区。任一因子为 0（如无暴露）则该像元风险为 0；融合结果为各单灾种风险的凸组合，对任一输入单调不减。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-multi-hazard-risk-assessment.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 更多示例

```bash
python geoskill-multi-hazard-risk-assessment.py --bbox 116 39 117 40 --synthetic --output-dir ./out
python geoskill-multi-hazard-risk-assessment.py --input scene.tif --output-dir ./out
python geoskill-multi-hazard-risk-assessment.py --bbox 116 39 117 40 --hazards 5 --breaks 0.1 0.3 0.5 0.7 --synthetic --output-dir ./out
python geoskill-multi-hazard-risk-assessment.py --bbox 121 31 122 32 --synthetic --quiet --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `risk_index.tif` | GeoTIFF | 综合风险指数 [0,1] |
| `risk_zones.tif` | GeoTIFF | 风险分区（整型 0-4） |
| `risk_params.json` | JSON | 断裂阈值/权重/各单灾种均值 |

每次运行还会产出 `output-manifest.json`（运行清单，含输入/产物/QA 摘要）。

## 数据源 / Source

真实模式读取多波段 GeoTIFF（band1=危险度、band2=暴露度、band3=脆弱性）；合成模式离线生成多灾种场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
