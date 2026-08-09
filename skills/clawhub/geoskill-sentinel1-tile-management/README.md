# Sentinel-1 Tile Management (geoskill-sentinel1-tile-management)

> Simulates the Sentinel-1 GRD preprocessing pipeline: linear σ⁰ to dB conversion (10·log10), bbox pixel-aligned clipping, VV/VH dual-polarization processing and physical-range QA, outputting the preprocessed σ⁰(dB) GeoTIFF and a processing-log JSON with steps/parameters/statistics. Sentinel-1 GRD preprocessing pipeline: dB conversion, bbox clip, dual-pol QA.

---

## 1. Overview

Simulates the standard preprocessing pipeline for Sentinel-1 GRD (ground range detected) imagery: 1. **Read / generate σ⁰** (linear power). 2. **dB conversion**: `dB = 10·log10(σ⁰)`, the logarithmic scale conventionally used in SAR. 3. **Clip to bbox**: pixel-aligned clip to the user-specified geographic extent (intersection). 4. **Per-polarization processing** (`--polarization vv,vh`): IW dual-pol, EW optional. 5. **Physical-range QA**: flags pixels outside `--db-min/--db-max` (default −35~5 dB). Outputs the preprocessed σ⁰(dB) GeoTIFF + processing-log JSON (steps, parameters, per-polarization statistics).

## 2. Features

Simulates the standard preprocessing pipeline for Sentinel-1 GRD (ground range detected) imagery: 1. **Read / generate σ⁰** (linear power). 2. **dB conversion**: `dB = 10·log10(σ⁰)`, the logarithmic scale conventionally used in SAR. 3. **Clip to bbox**: pixel-aligned clip to the user-specified geographic extent (intersection). 4. **Per-polarization processing** (`--polarization vv,vh`): IW dual-pol, EW optional. 5. **Physical-range QA**: flags pixels outside `--db-min/--db-max` (default −35~5 dB). Outputs the preprocessed σ⁰(dB) GeoTIFF + processing-log JSON (steps, parameters, per-polarization statistics).

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-sentinel1-tile-management.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `sigma0_db.tif` | GeoTIFF (float32) | Preprocessed σ⁰(dB), one band per polarization, EPSG:4326 |
| `processing_log.json` | JSON | Processing steps / parameters / per-polarization statistics / out-of-range share |
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

# Sentinel-1 数据管理流水线（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-sentinel1-tile-management
description: '模拟Sentinel-1 GRD预处理流水线：线性σ⁰分贝转换(10·log10)、bbox像素对齐裁剪、VV/VH双极化处理与物理区间QA，输出预处理σ⁰(dB) GeoTIFF与含步骤/参数/统计的处理日志JSON。Sentinel-1 GRD preprocessing pipeline: dB conversion, bbox clip, dual-pol QA.'
---

# Sentinel-1 数据管理流水线 | Sentinel-1 Tile Management

模拟 Sentinel-1 GRD（地距多视）影像的标准预处理流水线：

1. **读入 / 生成 σ⁰**（线性功率）。
2. **分贝转换**：`dB = 10·log10(σ⁰)`，SAR 惯用的对数刻度。
3. **裁剪到 bbox**：像素对齐裁到用户指定的地理范围（取交集）。
4. **逐极化处理**（`--polarization vv,vh`）：IW 双极化、EW 可选。
5. **物理区间 QA**：标记超出 `--db-min/--db-max`（默认 −35~5 dB）的像元。

输出预处理后的 σ⁰(dB) GeoTIFF + 处理日志 JSON（步骤、参数、逐极化统计）。

## 依赖

```bash
pip install numpy rasterio
```

## 使用方法

### 基本用法（仅给 bbox，自动合成双极化场景）

```bash
python geoskill-sentinel1-tile-management.py --bbox 116.0 39.0 117.0 40.0 --output-dir ./out
```

### 示例 1：合成数据（离线）

```bash
python geoskill-sentinel1-tile-management.py --bbox 116 39 117 40 --synthetic --mode iw --polarization vv,vh --output-dir ./syn
```

### 示例 2：真实 GRD + 裁剪

```bash
python geoskill-sentinel1-tile-management.py --input grd.tif --bbox 116.4 39.4 116.6 39.6 --output-dir ./clip
```

### 示例 3：EW 模式单极化

```bash
python geoskill-sentinel1-tile-management.py --bbox 121 31 122 32 --mode ew --polarization hh --output-dir ./ew --quiet
```

### 示例 4：自定义物理区间 QA

```bash
python geoskill-sentinel1-tile-management.py --bbox 116 39 117 40 --db-min -30 --db-max 0 --output-dir ./qa --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `sigma0_db.tif` | GeoTIFF (float32) | 预处理后 σ⁰(dB)，逐极化波段，EPSG:4326 |
| `processing_log.json` | JSON | 处理步骤 / 参数 / 逐极化统计 / 越界比例 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- **真实模式**：本地 S1 GRD 线性 σ⁰ GeoTIFF（多波段视为 VV/VH/...）。
- **合成模式**：本地生成 S1 风格双极化 σ⁰ 场景（VV > VH，含斑点噪声）。

## 隐私声明 / Privacy

- 默认完全离线运行，`--synthetic` 无任何网络。
- 所有处理本地完成，不上传用户数据。

## License

MIT
