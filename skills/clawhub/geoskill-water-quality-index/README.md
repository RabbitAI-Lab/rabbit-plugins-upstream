# Water Quality Remote Sensing Index (geoskill-water-quality-index)

> Retrieves chlorophyll-a, suspended solids, and Secchi depth with empirical water-color remote sensing models, with water masking and eutrophication classification

---

## 1. Overview

This skill retrieves and classifies key water quality parameters from multispectral imagery using empirical water-color remote sensing models. It is suitable for lake/coastal algal bloom monitoring, eutrophication assessment, and water clarity (Secchi depth) mapping. Core algorithms: **Chlorophyll a (OC3)** — NASA OC3 quartic polynomial, log10(chl) = Σ aᵢ·[log10(blue/green)]ⁱ; **Total Suspended Solids (TSS)** — empirical red-band retrieval based on the analytical inversion of the water backscatter–absorption (Gordon) relationship; **Secchi depth** — an empirical model negatively correlated with chl and TSS; **Water masking** — NDWI = (green − nir)/(green + nir) threshold segmentation of water/land; **Eutrophication classification** — four levels (oligotrophic/mesotrophic/eutrophic/hypereutrophic) by chlorophyll-a concentration (OECD thresholds).

## 2. Features

This skill retrieves and classifies key water quality parameters from multispectral imagery using empirical water-color remote sensing models. It is suitable for lake/coastal algal bloom monitoring, eutrophication assessment, and water clarity (Secchi depth) mapping. Core algorithms: **Chlorophyll a (OC3)** — NASA OC3 quartic polynomial, log10(chl) = Σ aᵢ·[log10(blue/green)]ⁱ; **Total Suspended Solids (TSS)** — empirical red-band retrieval based on the analytical inversion of the water backscatter–absorption (Gordon) relationship; **Secchi depth** — an empirical model negatively correlated with chl and TSS; **Water masking** — NDWI = (green − nir)/(green + nir) threshold segmentation of water/land; **Eutrophication classification** — four levels (oligotrophic/mesotrophic/eutrophic/hypereutrophic) by chlorophyll-a concentration (OECD thresholds).

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-water-quality-index.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `chl_a.tif` | GeoTIFF | Chlorophyll-a concentration (mg/m³, optional per `--parameters`) |
| `tss.tif` | GeoTIFF | Total suspended solids concentration (g/m³, optional per `--parameters`) |
| `secchi.tif` | GeoTIFF | Secchi depth (m, optional per `--parameters`) |
| `trophic_class.tif` | GeoTIFF | Eutrophication class raster (0 oligotrophic / 1 mesotrophic / 2 eutrophic / 3 hypereutrophic) |
| `water_quality_report.json` | JSON | Water body statistics + class distribution + correlation validation against synthetic ground truth |
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

# 水质遥感指数（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-water-quality-index
description: '基于水色遥感经验模型反演叶绿素a、悬浮物与透明度，做水体掩膜与富营养化分级'
---

# 水质遥感指数 | Water Quality Index

本 skill 基于水色遥感经验模型从多光谱影像反演关键水质参数并分级，适用于湖泊/近海水华监测、富营养化评估、水体透明度制图等场景。

核心算法：**叶绿素 a（OC3）**——NASA OC3 四次多项式，log10(chl) = Σ aᵢ·[log10(blue/green)]ⁱ；**悬浮物 TSS**——红波段经验反演，基于水体后向散射—吸收（Gordon）关系的解析逆；**透明度 Secchi**——与 chl、TSS 负相关的经验模型；**水体掩膜**——NDWI = (green − nir)/(green + nir) 阈值分割水/陆；**富营养化分级**——按叶绿素 a 浓度分贫/中/富/超富营养四级（OECD 阈值）。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-water-quality-index.py --bbox 116.0 39.0 117.0 40.0
```

### 示例 1（合成数据，离线）

```bash
python geoskill-water-quality-index.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（只反演叶绿素与悬浮物）

```bash
python geoskill-water-quality-index.py --bbox 116 39 117 40 --synthetic --parameters chl_a,tss --output-dir ./out
```

### 示例 3（调整 NDWI 水体阈值）

```bash
python geoskill-water-quality-index.py --bbox 121 31 122 32 --synthetic --ndwi-threshold 0.1 --quiet
```

### 示例 4（真实多光谱影像，band 顺序：蓝/绿/红/近红外反射率）

```bash
python geoskill-water-quality-index.py --input water_scene.tif --parameters chl_a,tss,secchi --output-dir ./out
```

### 示例 5（不同区域 + 自定义随机种子）

```bash
python geoskill-water-quality-index.py --bbox 113 23 114 24 --synthetic --seed 7 --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `chl_a.tif` | GeoTIFF | 叶绿素 a 浓度（mg/m³，按 `--parameters` 可选） |
| `tss.tif` | GeoTIFF | 悬浮物浓度（g/m³，按 `--parameters` 可选） |
| `secchi.tif` | GeoTIFF | 透明度 Secchi 深度（m，按 `--parameters` 可选） |
| `trophic_class.tif` | GeoTIFF | 富营养化分级栅格（0 贫/1 中/2 富/3 超富营养） |
| `water_quality_report.json` | JSON | 水体统计 + 分级分布 + 合成真值相关性验证 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- `--input`：本地多光谱 GeoTIFF（band1=蓝, band2=绿, band3=红, band4=近红外，地表反射率 0–1）。
- `--synthetic`：由真值 chl/TSS 场经 Gordon 前向模型生成的水体影像 + 陆地块，完全离线。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
