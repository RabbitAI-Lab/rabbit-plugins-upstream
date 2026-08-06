# Telecom Coverage Optimization (geoskill-telecom-coverage-optimization)

> Simplified Okumura-Hata propagation with terrain and buildings to map coverage and blind spots for telecom planning

---

## 1. Overview

Estimates base-station coverage and blind spots using a simplified Okumura-Hata propagation model plus terrain/building clutter loss, supporting telecom network planning and blind-spot filling. Path loss is computed with the Hata empirical formula (including mobile-station height correction and urban/suburban/open-area empirical corrections); received signal level RSL = transmit power + antenna gain − path loss − clutter loss (additional dB from terrain relief and building height). For multiple base stations, the strongest signal is taken per pixel; RSL ≥ threshold is classified as covered, otherwise as a blind spot.

## 2. Features

Estimates base-station coverage and blind spots using a simplified Okumura-Hata propagation model plus terrain/building clutter loss, supporting telecom network planning and blind-spot filling. Path loss is computed with the Hata empirical formula (including mobile-station height correction and urban/suburban/open-area empirical corrections); received signal level RSL = transmit power + antenna gain − path loss − clutter loss (additional dB from terrain relief and building height). For multiple base stations, the strongest signal is taken per pixel; RSL ≥ threshold is classified as covered, otherwise as a blind spot.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-telecom-coverage-optimization.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `signal_strength.tif` | GeoTIFF | Best received signal level RSL (dBm) |
| `coverage_mask.tif` | GeoTIFF | Coverage mask (1 covered / 0 blind spot) |
| `towers.geojson` | GeoJSON | Base-station locations and parameters |
| `coverage_report.json` | JSON | Coverage rate / blind-spot rate / blind-spot filling suggestions |
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

# 通信覆盖优化（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-telecom-coverage-optimization
description: 'Simplified Okumura-Hata propagation with terrain and buildings to map coverage and blind spots for telecom planning'
---

# 通信覆盖优化 | Telecom Coverage Optimization

基于简化 Okumura-Hata 传播模型 + 地形/建筑杂波损耗估算基站覆盖与盲区，服务通信网络规划与补盲。

路径损耗用 Hata 经验式（含移动台高度修正，城区/郊区/开阔地经验改正）；接收功率 RSL = 发射功率 + 天线增益 − 路径损耗 − 杂波损耗（地形高差与建筑高度附加 dB）。多基站逐像元取最强信号，RSL ≥ 门限判为覆盖，否则为盲区。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-telecom-coverage-optimization.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例 1（合成场景，离线）

```bash
python geoskill-telecom-coverage-optimization.py --bbox 116 39 117 40 --synthetic --output-dir ./out
```

### 示例 2（真实地形/建筑（DEM/建筑高度））

```bash
python geoskill-telecom-coverage-optimization.py --input terrain.tif --output-dir ./out
```

### 示例 3（郊区环境 + 900MHz）

```bash
python geoskill-telecom-coverage-optimization.py --input terrain.tif --environment suburban --frequency 900 --output-dir ./out
```

### 示例 4（更严覆盖门限）

```bash
python geoskill-telecom-coverage-optimization.py --input terrain.tif --threshold -95 --output-dir ./out
```

### 示例 5（提高发射功率评估覆盖改善）

```bash
python geoskill-telecom-coverage-optimization.py --input terrain.tif --tx-power 46 --gain 18 --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `signal_strength.tif` | GeoTIFF | 最佳接收信号电平 RSL（dBm） |
| `coverage_mask.tif` | GeoTIFF | 覆盖掩膜（1 覆盖 / 0 盲区） |
| `towers.geojson` | GeoJSON | 基站位置与参数 |
| `coverage_report.json` | JSON | 覆盖率/盲区率/补盲建议 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

多波段 GeoTIFF，波段顺序 DEM / 建筑高度。 或使用 `--synthetic` 生成物理一致的模拟数据（完全离线）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
