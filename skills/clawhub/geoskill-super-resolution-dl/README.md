# Deep Learning Super-Resolution (geoskill-super-resolution-dl)

> 2x/3x/4x image super-resolution based on the SRCNN (Dong 2014) convolutional neural network, with training and inference on CUDA GPU; outputs high-resolution rasters and PSNR/SSIM evaluation

---

## 1. Overview

Upscales low-resolution remote sensing imagery to high resolution while enhancing detail, outputting the super-resolved raster and quality assessment metrics (PSNR/SSIM). **Core model**: **SRCNN** (Super-Resolution Convolutional Neural Network, Dong et al. 2014, ECCV/TPAMI) — a 3-layer fully convolutional network (9×9 / 5×5 / 5×5 kernels, 1→64→32→1 channels, ReLU) that takes the bicubic upsampled result as input and learns the HR − bicubic residual; the network architecture, training objective (pixel-wise MSE) and inference pipeline are consistent with the original SRCNN. All training/inference runs on a **CUDA GPU** (torch >= 2.x); the skill ships with pre-trained weights ``srcnn_weights.pt`` (trained on synthetic ground truth); if the weights are missing, they are automatically trained on the GPU at first run and cached to disk. Synthetic mode executes a self-consistent "high-resolution ground truth → downsampling → super-resolution" experiment that directly quantifies restoration quality and compares it against the ``--psnr_bicubic_only`` bicubic baseline.

## 2. Features

Upscales low-resolution remote sensing imagery to high resolution while enhancing detail, outputting the super-resolved raster and quality assessment metrics (PSNR/SSIM). **Core model**: **SRCNN** (Super-Resolution Convolutional Neural Network, Dong et al. 2014, ECCV/TPAMI) — a 3-layer fully convolutional network (9×9 / 5×5 / 5×5 kernels, 1→64→32→1 channels, ReLU) that takes the bicubic upsampled result as input and learns the HR − bicubic residual; the network architecture, training objective (pixel-wise MSE) and inference pipeline are consistent with the original SRCNN. All training/inference runs on a **CUDA GPU** (torch >= 2.x); the skill ships with pre-trained weights ``srcnn_weights.pt`` (trained on synthetic ground truth); if the weights are missing, they are automatically trained on the GPU at first run and cached to disk. Synthetic mode executes a self-consistent "high-resolution ground truth → downsampling → super-resolution" experiment that directly quantifies restoration quality and compares it against the ``--psnr_bicubic_only`` bicubic baseline.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-super-resolution-dl.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `super_resolved.tif` | GeoTIFF | Super-resolved high-resolution raster |
| `quality_metrics.json` | JSON | PSNR/SSIM and comparison against the pure bicubic baseline |
| `output-manifest.json` | JSON | Run manifest (input/output/QA/exit code) |

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

# 深度学习超分辨率（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-super-resolution-dl
description: '基于 SRCNN（Dong 2014）卷积神经网络的 2x/3x/4x 影像超分辨率，在 CUDA GPU 上训练与推理，输出高分辨率栅格与 PSNR/SSIM 评估'
---

# 深度学习超分辨率 | Deep Learning Super-Resolution

把低分辨率遥感影像放大到高分辨率并增强细节，输出超分栅格与质量评估指标（PSNR/SSIM）。

**核心模型**：**SRCNN**（Super-Resolution Convolutional Neural Network, Dong et al. 2014, ECCV/TPAMI）
—— 3 层全卷积网络（9×9 / 5×5 / 5×5 核，1→64→32→1 通道，ReLU），以双三次上采样结果为输入、
学习 HR - bicubic 残差；网络结构、训练目标（pixel-wise MSE）与推理流程与原始 SRCNN 一致。
所有训练/推理在 **CUDA GPU** 上执行（torch >= 2.x）；随 skill 附带预训练权重
``srcnn_weights.pt``（在合成真值上训练得到）；若权重缺失则在首次运行时自动用 GPU
训练并落盘缓存。

合成模式执行"高分辨率真值 -> 降采样 -> 超分"自洽实验，可直接量化恢复质量，并与
``--psnr_bicubic_only`` 双三次基线对比。

## 依赖

```bash
pip install numpy rasterio scipy torch  # torch 需 CUDA 版以使用 GPU 推理
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-super-resolution-dl.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2：真实低分影像 3 倍放大

```bash
python geoskill-super-resolution-dl.py --input low.tif --scale 3 --amount 0.7 --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `super_resolved.tif` | GeoTIFF | 超分后的高分辨率栅格 |
| `quality_metrics.json` | JSON | PSNR/SSIM 及与纯双三次基线的对比 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/退出码） |

## 数据源 / Source

本地单波段 GeoTIFF，或 --synthetic（高分辨率真值降采样得到低分辨率输入，真值留存用于评估）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
