# Light Pollution Assessment (geoskill-light-pollution-assessment)

> Classify light pollution into grades 0–5 from VIIRS night-time light radiance using ecological thresholds, estimate an ecological impact index with a log-response model, and provide a skyglow proxy. Assesses light pollution grades from VIIRS night-time lights and ecological thresholds. Outputs three GeoTIFFs: grade, ecological impact, and skyglow.

---

## 1. Overview

Light pollution grade thresholds (0.25/1/4/15/50 nW·cm⁻²·sr⁻¹) follow the global light pollution classification of Falchi et al. (2016): 0 = pristine dark sky, 5 = extreme light pollution. The ecological impact index uses a log response I = log10(1+k·R)/log10(1+k·Rmax) normalized to [0,1], characterizing the disturbance of artificial light on the circadian rhythms of nocturnal organisms; the skyglow proxy = radiance × scattering coefficient. Use cases: dark-sky reserve delineation, ecological light-environment assessment, and urban lighting planning.

## 2. Features

Light pollution grade thresholds (0.25/1/4/15/50 nW·cm⁻²·sr⁻¹) follow the global light pollution classification of Falchi et al. (2016): 0 = pristine dark sky, 5 = extreme light pollution. The ecological impact index uses a log response I = log10(1+k·R)/log10(1+k·Rmax) normalized to [0,1], characterizing the disturbance of artificial light on the circadian rhythms of nocturnal organisms; the skyglow proxy = radiance × scattering coefficient. Use cases: dark-sky reserve delineation, ecological light-environment assessment, and urban lighting planning.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-light-pollution-assessment.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `light_pollution_grade.tif` | GeoTIFF (float32) | Light pollution grade 0–5 |
| `ecological_impact.tif` | GeoTIFF (float32) | Ecological impact index ∈ [0,1] |
| `skyglow_proxy.tif` | GeoTIFF (float32) | Skyglow proxy |
| `light_pollution_params.json` | JSON | Threshold table, per-grade pixel counts, radiance statistics |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/software versions) |


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

# 光污染评估（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-light-pollution-assessment
description: '由 VIIRS 夜光辐射值按生态阈值分 0-5 级光污染等级，对数响应模型估算生态影响指数，附天空辉光代理。Assesses light pollution grades from VIIRS night-time lights and ecological thresholds. 输出等级/生态影响/天空辉光三张 GeoTIFF。'
---

# 光污染评估 | Light Pollution Assessment

光污染等级阈值（0.25/1/4/15/50 nW·cm⁻²·sr⁻¹）参考 Falchi et al. (2016) 全球光污染分级：0=原始暗夜，5=极端光污染。生态影响指数用对数响应 I = log10(1+k·R)/log10(1+k·Rmax) 归一化到 [0,1]，刻画人造光对夜行生物节律的干扰；天空辉光代理 = 辐射值×散射系数。

适用场景：暗夜保护区划定、生态光环境评估、城市照明规划。

## 依赖

```bash
pip install numpy rasterio
```

## 使用方法

### 示例 1：合成城市梯度夜光

```bash
python geoskill-light-pollution-assessment.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### 示例 2：真实 VIIRS 年平均辐射栅格

```bash
python geoskill-light-pollution-assessment.py --input viirs_annual.tif --output-dir ./real
```

### 示例 3：不同区域

```bash
python geoskill-light-pollution-assessment.py --bbox 121 31 122 32 --synthetic --output-dir ./shanghai
```

### 示例 4：极小区域快速验证

```bash
python geoskill-light-pollution-assessment.py --bbox 116.39 39.90 116.40 39.91 --synthetic --output-dir ./tiny
```

### 示例 5：静默批量

```bash
python geoskill-light-pollution-assessment.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `light_pollution_grade.tif` | GeoTIFF (float32) | 光污染等级 0-5 |
| `ecological_impact.tif` | GeoTIFF (float32) | 生态影响指数 ∈ [0,1] |
| `skyglow_proxy.tif` | GeoTIFF (float32) | 天空辉光代理 |
| `light_pollution_params.json` | JSON | 阈值表、等级像元计数、辐射统计 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

本地 VIIRS 夜光 GeoTIFF（nW·cm⁻²·sr⁻¹）；分级阈值参考 Falchi et al. 2016（Science Advances, 开放获取）；合成模式本地生成城市梯度夜光，无外部数据源。

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
