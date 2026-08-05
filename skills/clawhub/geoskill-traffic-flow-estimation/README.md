# Traffic Flow Estimation (geoskill-traffic-flow-estimation)

> Estimate traffic flow and speed from multi-temporal vehicle detection, counting and cross-correlation displacement.

---

## 1. Overview

Estimates traffic flow and vehicle speed from multi-temporal high-resolution imagery, supporting traffic monitoring and road-network operation assessment. Core algorithm: threshold segmentation + connected-component labeling + area filtering to detect and count vehicles; flow = vehicle count / time interval; speed is estimated from the phase cross-correlation between two epochs (peak of the FFT cross-power spectrum) to derive the overall displacement, then multiplied by pixel size and divided by time. Cross-correlation can recover cyclic displacement exactly, and flow/speed satisfy an analytical relationship.

## 2. Features

Estimates traffic flow and vehicle speed from multi-temporal high-resolution imagery, supporting traffic monitoring and road-network operation assessment. Core algorithm: threshold segmentation + connected-component labeling + area filtering to detect and count vehicles; flow = vehicle count / time interval; speed is estimated from the phase cross-correlation between two epochs (peak of the FFT cross-power spectrum) to derive the overall displacement, then multiplied by pixel size and divided by time. Cross-correlation can recover cyclic displacement exactly, and flow/speed satisfy an analytical relationship.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-traffic-flow-estimation.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `traffic_flow.tif` | GeoTIFF | Spatialized traffic flow field |
| `traffic_stats.json` | JSON | Two-epoch counts, flow (vehicles/hour), displacement, speed (m/s and km/h) |
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

# 交通流量估算（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-traffic-flow-estimation
description: 'Estimate traffic flow and speed from multi-temporal vehicle detection, counting and cross-correlation displacement.'
---

# 交通流量估算 | Traffic Flow Estimation

从多时相高分辨率影像估算交通流量与车速，服务于交通监测与路网运行评估。

核心算法：阈值分割 + 连通域标记 + 面积筛选检测车辆并计数；流量 = 车辆数/时间间隔；速度由两时相相位互相关（FFT 互功率谱峰值）估计整体位移，再乘像元大小除以时间。互相关可精确恢复循环位移，流量/速度满足解析关系。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-traffic-flow-estimation.py --bbox 116.0 39.0 117.0 40.0 [其他参数]
```

### 示例

#### 示例 1（合成数据（离线））

```bash
python geoskill-traffic-flow-estimation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### 示例 2（用法 2）

```bash
python geoskill-traffic-flow-estimation.py --input two_epoch.tif --dt-minutes 5 --output-dir ./out
```

#### 示例 3（用法 3）

```bash
python geoskill-traffic-flow-estimation.py --bbox 121.0 31.0 122.0 32.0 --dt-minutes 3 --output-dir ./out --quiet
```

#### 示例 4（用法 4）

```bash
python geoskill-traffic-flow-estimation.py --input two_epoch.tif --threshold 0.6 --pixel-size 0.5 --output-dir ./out
```

#### 示例 5（用法 5）

```bash
python geoskill-traffic-flow-estimation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `traffic_flow.tif` | GeoTIFF | 空间化交通流量场 |
| `traffic_stats.json` | JSON | 两时相计数、流量(辆/时)、位移、速度(m/s 与 km/h) |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

本地双时相 GeoTIFF（band1=t1, band2=t2）；`--synthetic` 模式模拟车辆沿道路位移的双时相场景。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
