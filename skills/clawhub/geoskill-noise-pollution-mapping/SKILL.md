---
name: geoskill-noise-pollution-mapping
description: '交通噪声衰减模型制图 dB(A) 等级：FHWA 简化声源级、点/线源几何发散、建筑屏障衰减与地面吸收。Maps traffic noise levels with distance attenuation, building shielding and terrain. 输出噪声级 GeoTIFF + 参数 JSON。'
---

# 噪声污染制图 | Noise Pollution Mapping

Source level is estimated with the FHWA simplified formula L = 10·log10(flow) + 20·log10(speed/50) + 30; geometric divergence attenuates point sources by -20·log10(R/R0) and line sources by -10·log10(R/R0) (6 dB / 3 dB per doubling of distance, respectively); each row of building barriers attenuates 5 dB (capped at 20 dB); soft-ground absorption is 0.5 dB/100 m. The synthesized noise level is clipped to [0,120] dB(A).

Use cases: road environmental impact assessment, acoustic environment functional zoning, and noise-barrier siting.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy
```

## Usage / 使用方法

### Example 1: default traffic flow (1000 veh/h, 60 km/h)

```bash
python geoskill-noise-pollution-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### Example 2: highway (high-flow line source)

```bash
python geoskill-noise-pollution-mapping.py --bbox 116 39 117 40 --synthetic --flow 5000 --speed 100 --source-type line --output-dir ./highway
```

### Example 3: distance/barrier raster input (band0=distance cell, band1=number of barriers)

```bash
python geoskill-noise-pollution-mapping.py --input dist_barriers.tif --flow 2000 --output-dir ./real
```

### Example 4: low-flow residential road

```bash
python geoskill-noise-pollution-mapping.py --bbox 121 31 122 32 --synthetic --flow 300 --speed 40 --output-dir ./residential
```

### Example 5: quiet batch run

```bash
python geoskill-noise-pollution-mapping.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `noise_level.tif` | GeoTIFF (float32) | Noise level dB(A), EPSG:4326 |
| `noise_params.json` | JSON | Source level, pixel scale, noise statistics |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/software versions) |

## Data Source / 数据源 / Source

Local GeoTIFF (band0=pixel distance to road, band1=number of barriers, optional); attenuation coefficients follow public FHWA traffic noise model literature; synthetic mode generates a road network + building belts locally, with no external data source.

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default; no network requests are made.
- `--synthetic` mode reads no external data.
- All computation is performed locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-noise-pollution-mapping
description: '交通噪声衰减模型制图 dB(A) 等级：FHWA 简化声源级、点/线源几何发散、建筑屏障衰减与地面吸收。Maps traffic noise levels with distance attenuation, building shielding and terrain. 输出噪声级 GeoTIFF + 参数 JSON。'
---

# 噪声污染制图 | Noise Pollution Mapping

声源级按 FHWA 简化式 L = 10·log10(flow) + 20·log10(speed/50) + 30 估算；几何发散点源 -20·log10(R/R0)、线源 -10·log10(R/R0)（距离加倍分别衰减 6 dB / 3 dB）；建筑屏障每排衰减 5 dB（上限 20 dB）；软地面吸收 0.5 dB/100m。合成噪声级 clip 到 [0,120] dB(A)。

适用场景：道路环评、声环境功能区划、降噪屏障选址。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 示例 1：默认车流（1000 辆/h, 60 km/h）

```bash
python geoskill-noise-pollution-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### 示例 2：高速公路（大流量线源）

```bash
python geoskill-noise-pollution-mapping.py --bbox 116 39 117 40 --synthetic --flow 5000 --speed 100 --source-type line --output-dir ./highway
```

### 示例 3：距离/屏障栅格输入（band0=距离像元, band1=屏障数）

```bash
python geoskill-noise-pollution-mapping.py --input dist_barriers.tif --flow 2000 --output-dir ./real
```

### 示例 4：低流量居住区道路

```bash
python geoskill-noise-pollution-mapping.py --bbox 121 31 122 32 --synthetic --flow 300 --speed 40 --output-dir ./residential
```

### 示例 5：静默批量

```bash
python geoskill-noise-pollution-mapping.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `noise_level.tif` | GeoTIFF (float32) | 噪声级 dB(A)，EPSG:4326 |
| `noise_params.json` | JSON | 声源级、像元尺度、噪声统计 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

本地 GeoTIFF（band0=距道路像元距离、band1=屏障数，可选）；衰减系数参考FHWA 交通噪声模型公开文献；合成模式本地生成路网+建筑带，无外部数据源。

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
