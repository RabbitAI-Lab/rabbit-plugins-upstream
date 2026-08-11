---
name: geoskill-traffic-flow-estimation
description: 'Estimate traffic flow and speed from multi-temporal vehicle detection, counting and cross-correlation displacement.'
---

# 交通流量估算 | Traffic Flow Estimation

Estimates traffic flow and vehicle speed from multi-temporal high-resolution imagery, serving traffic monitoring and road network performance assessment.

Core algorithm: threshold segmentation + connected-component labeling + area filtering detect and count vehicles; flow = vehicle count / time interval; speed is derived from the overall displacement estimated by two-epoch phase cross-correlation (peak of the FFT cross-power spectrum), multiplied by pixel size and divided by time. Cross-correlation recovers cyclic displacement exactly, and flow/speed satisfy an analytic relationship.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-traffic-flow-estimation.py --bbox 116.0 39.0 117.0 40.0 [other parameters]
```

### Examples

#### Example 1 (synthetic data (offline))

```bash
python geoskill-traffic-flow-estimation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

#### Example 2 (usage 2)

```bash
python geoskill-traffic-flow-estimation.py --input two_epoch.tif --dt-minutes 5 --output-dir ./out
```

#### Example 3 (usage 3)

```bash
python geoskill-traffic-flow-estimation.py --bbox 121.0 31.0 122.0 32.0 --dt-minutes 3 --output-dir ./out --quiet
```

#### Example 4 (usage 4)

```bash
python geoskill-traffic-flow-estimation.py --input two_epoch.tif --threshold 0.6 --pixel-size 0.5 --output-dir ./out
```

#### Example 5 (usage 5)

```bash
python geoskill-traffic-flow-estimation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `traffic_flow.tif` | GeoTIFF | Spatially distributed traffic flow field |
| `traffic_stats.json` | JSON | Two-epoch counts, flow (vehicles/hour), displacement, speed (m/s and km/h) |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

Local two-epoch GeoTIFF (band1 = t1, band2 = t2); `--synthetic` mode simulates a two-epoch scene of vehicles displaced along roads.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is performed locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
