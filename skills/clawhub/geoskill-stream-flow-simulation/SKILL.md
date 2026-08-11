---
name: geoskill-stream-flow-simulation
description: '基于SCS-CN产流法与三角单位线，由土地利用、DEM与设计降雨模拟流域径流过程线与洪峰'
---

# 径流模拟 | Stream Flow Simulation

This skill simulates the runoff hydrograph and peak flow of small watersheds under design storms using classical runoff-generation and flow-concentration methods. It suits scenarios such as urban drainage, flood estimation for small and medium watersheds, and sponge-city assessment.

Core algorithms: **SCS-CN runoff generation** — S = 25400/CN − 254, Ia = 0.2·S, runoff depth Q = (P−Ia)²/(P−Ia+S), where CN is looked up from the USDA-NRCS standard table by land use type; **design storm** — triangular hyetograph, total rainfall given by `--rainfall`, with duration shortened as the return period `--return-period` increases (larger return periods concentrate the rainfall peak more); **unit hydrograph flow concentration** — the Kirpich formula estimates time of concentration from DEM slope and flow length, a triangular unit hydrograph is constructed and convolved with the net rainfall hyetograph to produce the runoff hydrograph, with the convolution strictly conserving water balance.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-stream-flow-simulation.py --bbox 116.0 39.0 117.0 40.0 --rainfall 100 --return-period 10
```

### Example 1 (synthetic data, offline)

```bash
python geoskill-stream-flow-simulation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --rainfall 80 --output-dir ./out
```

### Example 2 (100-year design storm)

```bash
python geoskill-stream-flow-simulation.py --bbox 116 39 117 40 --synthetic --rainfall 180 --return-period 100 --output-dir ./out
```

### Example 3 (small rainfall event)

```bash
python geoskill-stream-flow-simulation.py --bbox 121 31 122 32 --synthetic --rainfall 30 --return-period 2 --quiet
```

### Example 4 (real land-surface raster, band1 = land use code, band2 = DEM)

```bash
python geoskill-stream-flow-simulation.py --input basin.tif --rainfall 120 --return-period 20 --output-dir ./out
```

### Example 5 (comparison across regions)

```bash
python geoskill-stream-flow-simulation.py --bbox 113 23 114 24 --synthetic --rainfall 150 --return-period 50 --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `runoff_depth.tif` | GeoTIFF | SCS-CN runoff depth spatial distribution raster (mm) |
| `hydrograph.json` | JSON | Runoff hydrograph (time/discharge) + peak flow + concentration parameters + water balance |
| `output-manifest.json` | JSON | Run manifest (including QA: runoff coefficient, peak flow, water balance ratio) |

## Data Source / 数据源 / Source

- `--input`: local GeoTIFF (band1 = integer land use code, band2 = optional DEM).
- `--synthetic`: physically consistent DEM + tiled land-use land surface, fully offline.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-stream-flow-simulation
description: '基于SCS-CN产流法与三角单位线，由土地利用、DEM与设计降雨模拟流域径流过程线与洪峰'
---

# 径流模拟 | Stream Flow Simulation

本 skill 用经典产汇流方法模拟小流域在设计暴雨下的径流过程线与洪峰流量，适用于城市排涝、中小流域洪水预估、海绵城市评估等场景。

核心算法：**SCS-CN 产流**——S = 25400/CN − 254，Ia = 0.2·S，径流深 Q = (P−Ia)²/(P−Ia+S)，CN 由土地利用类型查 USDA-NRCS 标准值表；**设计暴雨**——三角形雨型，总雨量由 `--rainfall` 给定，历时随重现期 `--return-period` 缩短（重现期越大雨峰越集中）；**单位线汇流**——Kirpich 公式由 DEM 坡度/流长估算汇流时间，构建三角单位线并与净雨过程卷积得径流过程线，卷积严格保证水量守恒。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-stream-flow-simulation.py --bbox 116.0 39.0 117.0 40.0 --rainfall 100 --return-period 10
```

### 示例 1（合成数据，离线）

```bash
python geoskill-stream-flow-simulation.py --bbox 116.0 39.0 117.0 40.0 --synthetic --rainfall 80 --output-dir ./out
```

### 示例 2（百年一遇设计暴雨）

```bash
python geoskill-stream-flow-simulation.py --bbox 116 39 117 40 --synthetic --rainfall 180 --return-period 100 --output-dir ./out
```

### 示例 3（小降雨事件）

```bash
python geoskill-stream-flow-simulation.py --bbox 121 31 122 32 --synthetic --rainfall 30 --return-period 2 --quiet
```

### 示例 4（真实下垫面栅格，band1=土地利用码, band2=DEM）

```bash
python geoskill-stream-flow-simulation.py --input basin.tif --rainfall 120 --return-period 20 --output-dir ./out
```

### 示例 5（不同区域对比）

```bash
python geoskill-stream-flow-simulation.py --bbox 113 23 114 24 --synthetic --rainfall 150 --return-period 50 --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `runoff_depth.tif` | GeoTIFF | SCS-CN 径流深空间分布栅格（mm） |
| `hydrograph.json` | JSON | 径流过程线（时间/流量）+ 洪峰 + 汇流参数 + 水量平衡 |
| `output-manifest.json` | JSON | 运行清单（含 QA：径流系数、洪峰、水量平衡比） |

## 数据源 / Source

- `--input`：本地 GeoTIFF（band1 = 土地利用整型码，band2 = DEM 可选）。
- `--synthetic`：物理一致的 DEM + 分块土地利用下垫面，完全离线。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
