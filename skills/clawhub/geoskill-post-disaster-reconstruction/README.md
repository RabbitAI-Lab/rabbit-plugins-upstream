# Post-Disaster Reconstruction Remote Sensing Monitoring (geoskill-post-disaster-reconstruction)

> Building change and reconstruction progress classification from multi-temporal high-resolution imagery.

---

## 1. Overview

Monitors reconstruction progress using building-intensity proxies from multi-temporal high-resolution imagery: comparing the pre-disaster / damaged / reconstruction epochs, each pixel is classified (mutually exclusively) into non_building / unchanged / destroyed / under_construction / rebuilt. Recovery progress of destroyed pixels = clip((R-D)/(B-D),0,1), increasing monotonically with reconstruction-epoch intensity; the higher the reconstruction level, the more pixels are classified as rebuilt.

## 2. Features

Monitors reconstruction progress using building-intensity proxies from multi-temporal high-resolution imagery: comparing the pre-disaster / damaged / reconstruction epochs, each pixel is classified (mutually exclusively) into non_building / unchanged / destroyed / under_construction / rebuilt. Recovery progress of destroyed pixels = clip((R-D)/(B-D),0,1), increasing monotonically with reconstruction-epoch intensity; the higher the reconstruction level, the more pixels are classified as rebuilt.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-post-disaster-reconstruction.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `progress_class.tif` | GeoTIFF | Reconstruction progress class (integer 0-4) |
| `recovery_progress.tif` | GeoTIFF | Recovery progress of destroyed pixels [0,1] |
| `reconstruction_params.json` | JSON | Thresholds and class labels |

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

# 灾后重建遥感监测（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-post-disaster-reconstruction
description: '多期高分辨率影像建筑变化与重建进度分类'
---

# 灾后重建遥感监测 | Post-Disaster Reconstruction Monitoring

用多期高分辨率影像的建筑强度代理监测重建进度：对比灾前/损毁期/重建期三期，逐像元分为 non_building / unchanged / destroyed / under_construction / rebuilt 五类（互斥）。毁坏像元恢复进度 = clip((R-D)/(B-D),0,1)，随重建期强度单调增，重建程度越高 rebuilt 像元越多。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-post-disaster-reconstruction.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 更多示例

```bash
python geoskill-post-disaster-reconstruction.py --bbox 116 39 117 40 --synthetic --output-dir ./out
python geoskill-post-disaster-reconstruction.py --input series.tif --output-dir ./out
python geoskill-post-disaster-reconstruction.py --bbox 116 39 117 40 --recovery 0.9 --synthetic --output-dir ./out
python geoskill-post-disaster-reconstruction.py --bbox 117 39 118 40 --synthetic --quiet --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `progress_class.tif` | GeoTIFF | 重建进度分类（整型 0-4） |
| `recovery_progress.tif` | GeoTIFF | 毁坏像元恢复进度 [0,1] |
| `reconstruction_params.json` | JSON | 阈值与类别标签 |

每次运行还会产出 `output-manifest.json`（运行清单，含输入/产物/QA 摘要）。

## 数据源 / Source

真实模式读取多波段 GeoTIFF（band1=灾前、band2=损毁期、band3=重建期建筑强度）；合成模式离线生成三期场景（恢复程度可调）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
