# Frost Risk Mapping (geoskill-frost-risk-mapping)

> Frost risk mapping: terrain-corrected minimum temperature (lapse rate, cold-air pooling via TPI, aspect) with frost frequency, first/last frost date, frost-free period and risk classification. Outputs frost risk / frost-free period / frequency GeoTIFFs plus statistics JSON.

---

## 1. Overview

Performs terrain correction and frost risk analysis on daily minimum temperature raster time series, for agricultural frost disaster warning, cropping system zoning and ecological chilling damage assessment. Core algorithms: - **Terrain correction** (`apply_terrain_correction`): adjusts the minimum temperature from a reference surface to the actual terrain per pixel — · **Lapse rate** (default 6.5°C/km): T(z) = T_ref − Γ·(z − z_ref), so higher elevations are colder; · **Cold-air pooling**: uses the Topographic Position Index TPI (pixel elevation − neighborhood mean) to identify depressions, where pooling of descending cold air causes additional cooling (capped at −6°C), forming "frost hollows"; · **Aspect effect**: slope/aspect are derived from the DEM; in the Northern Hemisphere, south-facing slopes warm and north-facing slopes cool, with the effect strengthening as slope increases. - **Frost statistics**: per-pixel statistics of frost frequency (fraction of days with Tmin ≤ threshold), number of frost days, first frost date, last frost date and frost-free period (longest consecutive run of days with Tmin > threshold). - **Risk classification**: five classes from frost frequency: 0 none / 1 low / 2 moderate / 3 high / 4 severe. The `--synthetic` mode generates a DEM with ridges and a central depression (frost hollow), plus an elevation-affected daily minimum temperature time series (flat reference surface + terrain correction), allowing physical relationships such as "temperature decreases with elevation" and "high-elevation/depression areas have higher frost risk" to be verified offline without network access or real data.

## 2. Features

Performs terrain correction and frost risk analysis on daily minimum temperature raster time series, for agricultural frost disaster warning, cropping system zoning and ecological chilling damage assessment. Core algorithms: - **Terrain correction** (`apply_terrain_correction`): adjusts the minimum temperature from a reference surface to the actual terrain per pixel — · **Lapse rate** (default 6.5°C/km): T(z) = T_ref − Γ·(z − z_ref), so higher elevations are colder; · **Cold-air pooling**: uses the Topographic Position Index TPI (pixel elevation − neighborhood mean) to identify depressions, where pooling of descending cold air causes additional cooling (capped at −6°C), forming "frost hollows"; · **Aspect effect**: slope/aspect are derived from the DEM; in the Northern Hemisphere, south-facing slopes warm and north-facing slopes cool, with the effect strengthening as slope increases. - **Frost statistics**: per-pixel statistics of frost frequency (fraction of days with Tmin ≤ threshold), number of frost days, first frost date, last frost date and frost-free period (longest consecutive run of days with Tmin > threshold). - **Risk classification**: five classes from frost frequency: 0 none / 1 low / 2 moderate / 3 high / 4 severe. The `--synthetic` mode generates a DEM with ridges and a central depression (frost hollow), plus an elevation-affected daily minimum temperature time series (flat reference surface + terrain correction), allowing physical relationships such as "temperature decreases with elevation" and "high-elevation/depression areas have higher frost risk" to be verified offline without network access or real data.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-frost-risk-mapping.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `frost_risk.tif` | GeoTIFF (float32) | Frost risk class 0-4, EPSG:4326 |
| `frost_free_period.tif` | GeoTIFF (float32) | Frost-free period (longest consecutive frost-free days) |
| `frost_frequency.tif` | GeoTIFF (float32) | Frost frequency (0-1) |
| `frost_stats.json` | JSON | Threshold/DEM range/mean frost statistics/risk distribution |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/software versions) |

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

# 霜冻风险制图（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-frost-risk-mapping
description: '霜冻风险制图：由日最低温时序与 DEM 做高程递减率、冷空气湖（TPI 洼地）与坡向地形修正，逐像元统计霜冻频率/霜冻日数、初霜日、终霜日与无霜期，并分级霜冻风险。Frost risk mapping: terrain-corrected min-temperature (lapse rate, cold-air pooling via TPI, aspect) with frost frequency, first/last frost date, frost-free period and risk classification. 输出霜冻风险/无霜期/频率 GeoTIFF + 统计 JSON。'
---

# 霜冻风险制图 | Frost Risk Mapping

对日最低温时序栅格执行地形修正与霜冻风险分析，用于农业霜冻灾害预警、种植
制度区划与生态冷害评估。核心算法：

- **地形修正**（`apply_terrain_correction`）：把参考面上的最低温修正到逐像元
  实际地形——
  · **高程递减率**（lapse rate，默认 6.5°C/km）：T(z) = T_ref − Γ·(z − z_ref)，
    高程越高越冷；
  · **冷空气湖**（cold-air pooling）：用地形位置指数 TPI（像元高程 − 邻域均值）
    识别洼地，洼地积聚下泄冷空气而额外降温（封顶 −6°C），形成"霜穴"；
  · **坡向效应**（aspect）：由 DEM 解算坡度/坡向，北半球南坡增温、北坡降温，
    随坡度增大而增强。
- **霜冻统计**：逐像元统计霜冻频率（Tmin ≤ 阈值天数占比）、霜冻日数、初霜日、
  终霜日与无霜期（最长连续 Tmin > 阈值天数）。
- **风险分级**：由霜冻频率分为 0 无 / 1 低 / 2 中 / 3 高 / 4 严重 五级。

支持 `--synthetic` 模式生成含山脊与中央洼地（霜穴）的 DEM，以及受高程影响的
日最低温时序（平坦参考面 + 地形修正），无需网络和真实数据即可离线验证
"温度随高程递减""高海拔/洼地霜冻风险高"等物理关系。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法（仅给 bbox，自动合成）

```bash
python geoskill-frost-risk-mapping.py --bbox 116.0 39.0 117.0 40.0 --output-dir ./out
```

### 示例 1：合成数据离线评估

```bash
python geoskill-frost-risk-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --n-dates 40 --output-dir ./out
```

### 示例 2：自定义霜冻阈值（如 -2°C 轻霜）

```bash
python geoskill-frost-risk-mapping.py --bbox 116.0 39.0 117.0 40.0 --synthetic --threshold -2 --output-dir ./light_frost
```

### 示例 3：真实最低温时序 + DEM

```bash
python geoskill-frost-risk-mapping.py --input tmin_ts.tif --dem dem.tif --threshold 0 --output-dir ./real
```

### 示例 4：不做地形修正（直接用原始温度）

```bash
python geoskill-frost-risk-mapping.py --input tmin_ts.tif --correction none --output-dir ./raw
```

### 示例 5：不同区域

```bash
python geoskill-frost-risk-mapping.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./shanghai --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `frost_risk.tif` | GeoTIFF (float32) | 霜冻风险等级 0-4，EPSG:4326 |
| `frost_free_period.tif` | GeoTIFF (float32) | 无霜期（最长连续无霜天数） |
| `frost_frequency.tif` | GeoTIFF (float32) | 霜冻频率（0-1） |
| `frost_stats.json` | JSON | 阈值/DEM 范围/平均霜冻统计/风险分布 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

- **输入**：本地多波段日最低温时序 GeoTIFF（每波段一日）+ 可选 DEM GeoTIFF（米）；
  缺省 DEM 时用合成地形
- **合成模式**：本地生成山脊+洼地 DEM 与受高程影响的最低温场，无外部数据源
- **方法**：气温直减率、TPI 冷池与坡向辐射均为经典微气候学方法

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
