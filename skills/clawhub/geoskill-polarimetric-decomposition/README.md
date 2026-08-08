# Polarimetric SAR Decomposition (geoskill-polarimetric-decomposition)

> Polarimetric SAR decomposition: Cloude-Pottier H/A/α eigen-decomposition and Freeman three-component decomposition, outputting scattering entropy, anisotropy, scattering angle, and surface/dihedral/volume scattering powers.

---

## 1. Overview

Performs polarimetric target decomposition on fully polarimetric SAR data to extract the physical scattering mechanisms of ground targets. Two mainstream methods are implemented:

- **Cloude-Pottier (H/A/α) eigen-decomposition**: applies Hermitian eigen-decomposition to the 3×3 coherency matrix T3 of each pixel, yielding entropy H (scattering randomness, 0 = single mechanism, 1 = fully random), anisotropy A, and scattering angle α (surface scattering α≈0-30°, volume scattering α≈40-60°, dihedral scattering α≈90°).
- **Freeman-Durden three-component decomposition (simplified)**: solves for surface scattering Ps, dihedral scattering Pd, and volume scattering Pv from |Shh|², |Svv|², |Shv|².

## 2. Features

Performs polarimetric target decomposition on fully polarimetric SAR data to extract the physical scattering mechanisms of ground targets. Two mainstream methods are implemented:

- **Cloude-Pottier (H/A/α) eigen-decomposition**: applies Hermitian eigen-decomposition to the 3×3 coherency matrix T3 of each pixel, yielding entropy H (scattering randomness, 0 = single mechanism, 1 = fully random), anisotropy A, and scattering angle α (surface scattering α≈0-30°, volume scattering α≈40-60°, dihedral scattering α≈90°).
- **Freeman-Durden three-component decomposition (simplified)**: solves for surface scattering Ps, dihedral scattering Pd, and volume scattering Pv from |Shh|², |Svv|², |Shv|².

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-polarimetric-decomposition.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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

- Cloude / H/A/α: input GeoTIFF must contain 9 bands encoding the upper triangle of T3
  `[T11, T22, T33, Re T12, Im T12, Re T13, Im T13, Re T23, Im T23]`.
- Freeman: input GeoTIFF must contain 3 bands `[|Shh|², |Svv|², |Shv|²]`.

| File | Format | Description |
|---|---|---|
| `cloude_H_A_alpha.tif` | GeoTIFF (3 band) | Entropy H, anisotropy A, scattering angle α (degrees) |
| `freeman_three_component.tif` | GeoTIFF (3 band) | Ps / Pd / Pv scattering powers |
| `decomposition_stats.json` | JSON | Statistics and synthetic ground truth |
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

# 极化SAR分解（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-polarimetric-decomposition
description: '极化SAR分解：Cloude-Pottier H/A/α 特征分解与 Freeman 三分量分解，输出散射熵、各向异性、散射角与表面/二面角/体散射功率'
---

# 极化SAR分解 | Polarimetric SAR Decomposition

对全极化 SAR 数据执行极化目标分解，提取地物的散射物理机制。实现两类主流方法：

- **Cloude-Pottier（H/A/α）特征分解**：对每个像元的 3×3 相干矩阵 T3 做 Hermitian
  特征分解，得到熵 H（散射随机性，0=单一机制、1=完全随机）、各向异性 A 与散射角 α
  （表面散射 α≈0-30°、体散射 α≈40-60°、二面角散射 α≈90°）。
- **Freeman-Durden 三分量分解（简化）**：从 |Shh|²、|Svv|²、|Shv|² 求解表面散射 Ps、
  二面角散射 Pd 与体散射 Pv。

## 应用场景

- 地物分类与散射机制识别（城市建筑、森林、裸土、水体）
- 森林结构参数提取、农作物长势监测
- 极化 SAR 数据的物理特征工程

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 输入约定

- Cloude / H/A/α：输入 GeoTIFF 需含 9 个波段，按 T3 上三角编码
  `[T11, T22, T33, Re T12, Im T12, Re T13, Im T13, Re T23, Im T23]`。
- Freeman：输入 GeoTIFF 需含 3 个波段 `[|Shh|², |Svv|², |Shv|²]`。

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-polarimetric-decomposition.py --bbox 116.0 39.0 117.0 40.0 --method cloude --output-dir ./out
```

### 示例 2（Freeman 三分量合成）

```bash
python geoskill-polarimetric-decomposition.py --bbox 116.0 39.0 117.0 40.0 --method freeman --synthetic --output-dir ./out
```

### 示例 3（真实 T3 数据）

```bash
python geoskill-polarimetric-decomposition.py --input T3_9band.tif --method ha_alpha --output-dir ./out
```

### 示例 4（真实 C3 三分量）

```bash
python geoskill-polarimetric-decomposition.py --input C3_3band.tif --method freeman --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `cloude_H_A_alpha.tif` | GeoTIFF (3 band) | 熵 H、各向异性 A、散射角 α（度） |
| `freeman_three_component.tif` | GeoTIFF (3 band) | Ps / Pd / Pv 散射功率 |
| `decomposition_stats.json` | JSON | 统计量与合成真值 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地极化 GeoTIFF（T3 9 波段或 C3 3 波段），或 `--synthetic` 物理模拟场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
