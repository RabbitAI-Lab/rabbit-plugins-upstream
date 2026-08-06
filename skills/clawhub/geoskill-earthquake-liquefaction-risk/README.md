# Earthquake Liquefaction Risk Assessment (geoskill-earthquake-liquefaction-risk)

> Liquefaction index assessment using the Youd simplified method combined with geology, groundwater level, and PGA

---

## 1. Overview

Evaluate sandy soil liquefaction using the Youd simplified method: cyclic stress ratio CSR = 0.65·(PGA/g)·rd(z)·gw (rd is the stress reduction factor, gw the shallow groundwater amplification), cyclic resistance ratio CRR increases with SPT blow count N (the denser the soil, the more liquefaction-resistant), factor of safety FS = CRR/CSR (liquefaction is judged when FS < 1), then integrate with Iwasaki depth weights to obtain the liquefaction potential index LPI (≥ 0). Higher PGA → lower FS → higher LPI (positive correlation).

## 2. Features

Evaluate sandy soil liquefaction using the Youd simplified method: cyclic stress ratio CSR = 0.65·(PGA/g)·rd(z)·gw (rd is the stress reduction factor, gw the shallow groundwater amplification), cyclic resistance ratio CRR increases with SPT blow count N (the denser the soil, the more liquefaction-resistant), factor of safety FS = CRR/CSR (liquefaction is judged when FS < 1), then integrate with Iwasaki depth weights to obtain the liquefaction potential index LPI (≥ 0). Higher PGA → lower FS → higher LPI (positive correlation).

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-earthquake-liquefaction-risk.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `liquefaction_index.tif` | GeoTIFF | Liquefaction potential index LPI (≥ 0) |
| `factor_of_safety.tif` | GeoTIFF | Factor of safety FS (< 1 = liquefaction) |
| `liquefaction_params.json` | JSON | Assessment depth / fines content / mean groundwater level |

Each run also produces `output-manifest.json` (run manifest with inputs/outputs/QA summary).

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

# 地震液化风险评估（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-earthquake-liquefaction-risk
description: 'Youd简化法结合地质地下水位与PGA的液化指数评估'
---

# 地震液化风险评估 | Earthquake Liquefaction Risk

用 Youd 简化法评估砂土液化：循环应力比 CSR = 0.65·(PGA/g)·rd(z)·gw（rd 应力折减、gw 浅地下水放大），循环阻抗比 CRR 随 SPT 击数 N 增大（越密实越抗液化），安全系数 FS=CRR/CSR（<1 判定液化），再按 Iwasaki 深度权重积分得液化指数 LPI（≥0）。PGA 越高 → FS 越低 → LPI 越高（正相关）。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-earthquake-liquefaction-risk.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 更多示例

```bash
python geoskill-earthquake-liquefaction-risk.py --bbox 116 39 117 40 --synthetic --output-dir ./out
python geoskill-earthquake-liquefaction-risk.py --input site.tif --depth 5 --output-dir ./out
python geoskill-earthquake-liquefaction-risk.py --bbox 116 39 117 40 --depth 3 --fines 20 --synthetic --output-dir ./out
python geoskill-earthquake-liquefaction-risk.py --bbox 117 39 118 40 --synthetic --quiet --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `liquefaction_index.tif` | GeoTIFF | 液化指数 LPI（≥0） |
| `factor_of_safety.tif` | GeoTIFF | 安全系数 FS（<1 液化） |
| `liquefaction_params.json` | JSON | 评估深度/细粒含量/平均地下水位 |

每次运行还会产出 `output-manifest.json`（运行清单，含输入/产物/QA 摘要）。

## 数据源 / Source

真实模式读取多波段 GeoTIFF（band1=PGA(g)、band2=SPT N值、band3=地下水位埋深m）；合成模式离线生成场地。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
