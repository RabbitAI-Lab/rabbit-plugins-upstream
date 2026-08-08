# Atmospheric Correction (geoskill-atmospheric-correction)

> DOS/simplified-6S atmospheric correction converting DN/TOA to surface reflectance, with Landsat 8/Sentinel-2 sensor metadata support. Outputs a surface-reflectance GeoTIFF + correction-parameter JSON.

---

## 1. Overview

Performs atmospheric correction on multispectral remote sensing imagery, converting sensor-recorded DN values or top-of-atmosphere (TOA) reflectance into surface reflectance. Two methods are implemented: - **DOS** (Dark Object Subtraction): per-band estimation of atmospheric path radiance from low-percentile DN values, subtracted from TOA reflectance. Suitable for fast preprocessing and temporal radiometric consistency. - **6s-simplified** (simplified 6S radiative transfer): on top of DOS, adds a wavelength-dependent Rayleigh scattering optical-depth correction (strong in blue, weak in red), approximating 6S atmospheric path-radiance behavior. Band metadata for Landsat 8, Sentinel-2 and a generic sensor is built in (central wavelength, extraterrestrial solar irradiance ESUN). The `--synthetic` mode generates physically consistent simulated imagery, allowing the pipeline to be verified without network access or real data.

## 2. Features

Performs atmospheric correction on multispectral remote sensing imagery, converting sensor-recorded DN values or top-of-atmosphere (TOA) reflectance into surface reflectance. Two methods are implemented: - **DOS** (Dark Object Subtraction): per-band estimation of atmospheric path radiance from low-percentile DN values, subtracted from TOA reflectance. Suitable for fast preprocessing and temporal radiometric consistency. - **6s-simplified** (simplified 6S radiative transfer): on top of DOS, adds a wavelength-dependent Rayleigh scattering optical-depth correction (strong in blue, weak in red), approximating 6S atmospheric path-radiance behavior. Band metadata for Landsat 8, Sentinel-2 and a generic sensor is built in (central wavelength, extraterrestrial solar irradiance ESUN). The `--synthetic` mode generates physically consistent simulated imagery, allowing the pipeline to be verified without network access or real data.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-atmospheric-correction.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `surface_reflectance.tif` | GeoTIFF (float32) | Surface reflectance, per band [0,1], EPSG:4326 |
| `correction_params.json` | JSON | Per-band correction parameters (dark-object DN, ρ_dark, ESUN, etc.) |
| `output-manifest.json` | JSON | Run manifest (input/output/QA/software version) |


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

# 大气校正（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-atmospheric-correction
description: '对多光谱影像执行 DOS/简化6S 大气校正，将 DN/TOA 转为地表反射率。DOS/simplified-6S atmospheric correction converting DN/TOA to surface reflectance. 支持 Landsat 8/Sentinel-2 传感器元数据，输出地表反射率 GeoTIFF + 校正参数 JSON。'
---

# 大气校正 | Atmospheric Correction

对多光谱遥感影像执行大气校正，将传感器记录的 DN 值或大气顶（TOA）反射率
转换为地表反射率（surface reflectance）。实现了两种方法：

- **DOS**（Dark Object Subtraction，暗目标扣除）：逐波段用低分位数 DN 估计
  大气路径辐射，从 TOA 反射率中扣除。适用于快速预处理和时序辐射一致性。
- **6s-simplified**（简化 6S 辐射传输）：在 DOS 基础上追加随波长变化的瑞利
  散射光学厚度改正（蓝光强、红光弱），近似 6S 的大气程辐射行为。

内置 Landsat 8、Sentinel-2 和通用传感器的波段元数据（中心波长、太阳大气外
辐照度 ESUN）。支持 `--synthetic` 模式生成物理一致的模拟影像，无需网络和
真实数据即可验证流程。

## 依赖

```bash
pip install numpy rasterio
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-atmospheric-correction.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### 示例 1：Landsat 8 DOS 校正（合成数据）

```bash
python geoskill-atmospheric-correction.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --synthetic \
    --sensor landsat8 \
    --method dos \
    --output-dir ./landsat8_dos
```

### 示例 2：Sentinel-2 简化 6S 校正

```bash
python geoskill-atmospheric-correction.py \
    --bbox 121.0 31.0 122.0 32.0 \
    --synthetic \
    --sensor sentinel2 \
    --method 6s-simplified \
    --output-dir ./s2_6s
```

### 示例 3：真实影像 DOS 校正

```bash
python geoskill-atmospheric-correction.py \
    --input scene_dn.tif \
    --sensor landsat8 \
    --method dos \
    --dark-percentile 0.5 \
    --output-dir ./real_dos
```

### 示例 4：自定义太阳天顶角

```bash
python geoskill-atmospheric-correction.py \
    --input scene.tif \
    --sensor sentinel2 \
    --solar-zenith 45.0 \
    --output-dir ./custom_angle
```

### 示例 5：批量参数对比（DOS vs 6s）

```bash
python geoskill-atmospheric-correction.py --bbox 116 39 117 40 --synthetic --sensor landsat8 --method dos --output-dir ./cmp_dos --quiet
python geoskill-atmospheric-correction.py --bbox 116 39 117 40 --synthetic --sensor landsat8 --method 6s-simplified --output-dir ./cmp_6s --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `surface_reflectance.tif` | GeoTIFF (float32) | 地表反射率，逐波段 [0,1]，EPSG:4326 |
| `correction_params.json` | JSON | 逐波段校正参数（暗目标 DN、ρ_dark、ESUN 等） |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

- **Landsat 8/9**：USGS Collection 2（公共领域），ESUN 取自 Chander et al. 2009
- **Sentinel-2**：ESA（开放数据政策），ESUN 取自 ESA S2 文档
- **合成模式**：本地生成，无外部数据源

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据
- 仅当使用地名解析（非本 skill 直接功能）时才可能访问 Nominatim

## License

MIT
