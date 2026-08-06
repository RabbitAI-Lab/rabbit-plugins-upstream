---
name: geoskill-water-quality-index
description: '基于水色遥感经验模型反演叶绿素a、悬浮物与透明度，做水体掩膜与富营养化分级'
---

# 水质遥感指数 | Water Quality Index

This skill retrieves key water-quality parameters from multispectral imagery and classifies them using empirical water-color remote-sensing models, applicable to lake/coastal algae bloom monitoring, eutrophication assessment, and water transparency mapping.

Core algorithms: **Chlorophyll a (OC3)** — NASA OC3 quartic polynomial, log10(chl) = Σ aᵢ·[log10(blue/green)]ⁱ; **Total suspended solids (TSS)** — empirical red-band retrieval based on an analytical inversion of the backscatter–absorption (Gordon) relationship for water; **Secchi depth** — an empirical model negatively correlated with chl and TSS; **Water mask** — NDWI = (green − nir)/(green + nir) threshold segmentation of water/land; **Trophic classification** — four levels (oligotrophic/mesotrophic/eutrophic/hypereutrophic) by chlorophyll a concentration (OECD thresholds).

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-water-quality-index.py --bbox 116.0 39.0 117.0 40.0
```

### Example 1 (Synthetic Data, Offline)

```bash
python geoskill-water-quality-index.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (Retrieve Chlorophyll and Suspended Sediment Only)

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

### Example 5 (Different Regions + Custom Random Seed)

```bash
python geoskill-water-quality-index.py --bbox 113 23 114 24 --synthetic --seed 7 --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `chl_a.tif` | GeoTIFF | Chlorophyll a concentration (mg/m³, optional per `--parameters`) |
| `tss.tif` | GeoTIFF | Total suspended solids concentration (g/m³, optional per `--parameters`) |
| `secchi.tif` | GeoTIFF | Secchi depth (m, optional per `--parameters`) |
| `trophic_class.tif` | GeoTIFF | Trophic class raster (0 oligotrophic/1 mesotrophic/2 eutrophic/3 hypereutrophic) |
| `water_quality_report.json` | JSON | Water statistics + class distribution + correlation validation against synthetic ground truth |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- `--input`: local multispectral GeoTIFF (band1=blue, band2=green, band3=red, band4=NIR, surface reflectance 0–1).
- `--synthetic`: water-body imagery generated from ground-truth chl/TSS fields via the Gordon forward model, plus land blocks, fully offline.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
