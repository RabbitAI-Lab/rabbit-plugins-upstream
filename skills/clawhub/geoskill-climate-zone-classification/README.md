# Climate Zone Classification (geoskill-climate-zone-classification)

> Climate zone classification from monthly temperature/precipitation rasters (Köppen-Geiger rule tree & simplified Strahler), with area statistics and optional change detection.

---

## 1. Overview

Classifies climate zones from monthly mean temperature and monthly precipitation rasters, for applications such as climate mapping, ecological zoning, agro-climatic resource assessment, and climate change monitoring. Two schemes are built in:
- **Köppen-Geiger**: the classic rule tree (Peel et al. 2007 / Kottek et al. 2006). The five main groups A (tropical) / B (arid) / C (temperate) / D (continental) / E (polar) are determined from the coldest/warmest monthly mean temperatures, annual mean temperature, annual precipitation, and seasonal precipitation distribution, with second and third letters refining each group into 30 classes (Af tropical rainforest, Am tropical monsoon, Aw/As tropical savanna, BWh/BWk desert, BSh/BSk steppe, Cfa/Cfb/Cfc, Csa/Csb/Csc, Dfa...Dfd, ET tundra, EF ice cap).
- **Strahler (simplified genetic classification)**: merges thermal belts and moisture conditions into 10 genetic climate types (tropical humid / tropical arid / humid subtropical / Mediterranean / marine west coast / humid continental / dry continental / subarctic / tundra / polar ice cap).

A `--synthetic` mode generates a simulated climate field zoned by latitude (with physically consistent seasonal temperature and precipitation distribution), enabling offline validation of the full pipeline and class recovery. `--input2` is provided for two-period climate zone change detection.

## 2. Features

Classifies climate zones from monthly mean temperature and monthly precipitation rasters, for applications such as climate mapping, ecological zoning, agro-climatic resource assessment, and climate change monitoring. Two schemes are built in:
- **Köppen-Geiger**: the classic rule tree (Peel et al. 2007 / Kottek et al. 2006). The five main groups A (tropical) / B (arid) / C (temperate) / D (continental) / E (polar) are determined from the coldest/warmest monthly mean temperatures, annual mean temperature, annual precipitation, and seasonal precipitation distribution, with second and third letters refining each group into 30 classes (Af tropical rainforest, Am tropical monsoon, Aw/As tropical savanna, BWh/BWk desert, BSh/BSk steppe, Cfa/Cfb/Cfc, Csa/Csb/Csc, Dfa...Dfd, ET tundra, EF ice cap).
- **Strahler (simplified genetic classification)**: merges thermal belts and moisture conditions into 10 genetic climate types (tropical humid / tropical arid / humid subtropical / Mediterranean / marine west coast / humid continental / dry continental / subarctic / tundra / polar ice cap).

A `--synthetic` mode generates a simulated climate field zoned by latitude (with physically consistent seasonal temperature and precipitation distribution), enabling offline validation of the full pipeline and class recovery. `--input2` is provided for two-period climate zone change detection.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-climate-zone-classification.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `climate_zones.tif` | GeoTIFF (float32) | Climate class code raster (see area_statistics.json for the code table), EPSG:4326 |
| `area_statistics.json` | JSON | Code table + pixel count/fraction/estimated area per class + optional change detection |
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

# 气候区划（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-climate-zone-classification
description: '基于月均温与月降水栅格的气候区划，支持柯本-盖格（Köppen-Geiger）规则树与简化 Strahler 发生分类，输出气候类别码 GeoTIFF + 面积统计 JSON，可选双期变化检测。Climate zone classification from monthly temperature/precipitation rasters (Köppen-Geiger rule tree & simplified Strahler), with area statistics and optional change detection.'
---

# 气候区划 | Climate Zone Classification

对逐月均温与逐月降水栅格执行气候区划分类，用于气候制图、生态分区、农业
气候资源评价与气候变化监测。内置两套方案：

- **Köppen-Geiger（柯本-盖格）**：经典规则树（Peel et al. 2007 / Kottek et al. 2006）。
  由最冷/最热月均温、年均温、年降水及降水季节分配判定 A（热带）/B（干旱）/
  C（温带）/D（大陆性）/E（极地）五大主组，并细分第二、第三字母，共 30 个类别
  （Af 热带雨林、Am 热带季风、Aw/As 热带稀树草原、BWh/BWk 沙漠、BSh/BSk 草原、
  Cfa/Cfb/Cfc、Csa/Csb/Csc、Dfa…Dfd、ET 苔原、EF 冰原）。
- **Strahler（简化发生分类）**：以气温带与水分条件归并为 10 个发生气候类
  （热带多雨/热带干旱/湿润亚热带/地中海/海洋性西海岸/湿润大陆性/干燥大陆性/
  副极地/苔原/极地冰原）。

支持 `--synthetic` 模式生成沿纬度分带的模拟气候场（含物理一致的季节温降与
降水分配），可离线验证全流程与类别恢复。提供 `--input2` 做两期气候区变化检测。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法（仅给 bbox，自动合成，Köppen）

```bash
python geoskill-climate-zone-classification.py --bbox 116.0 39.0 117.0 40.0 --output-dir ./out
```

### 示例 1：合成数据 Strahler 分类

```bash
python geoskill-climate-zone-classification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --classification strahler --output-dir ./strahler
```

### 示例 2：真实 24 波段气候栅格（12 温度 + 12 降水）

```bash
python geoskill-climate-zone-classification.py --input climate.tif --classification koppen --output-dir ./real
```

### 示例 3：双期变化检测

```bash
python geoskill-climate-zone-classification.py --input climate_1990.tif --input2 climate_2020.tif --classification koppen --output-dir ./change
```

### 示例 4：不同区域合成

```bash
python geoskill-climate-zone-classification.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./shanghai
```

### 示例 5：Köppen vs Strahler 对比

```bash
python geoskill-climate-zone-classification.py --bbox 116 39 117 40 --synthetic --classification koppen --output-dir ./cmp_koppen --quiet
python geoskill-climate-zone-classification.py --bbox 116 39 117 40 --synthetic --classification strahler --output-dir ./cmp_strahler --quiet
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `climate_zones.tif` | GeoTIFF (float32) | 气候类别码栅格（码表见 area_statistics.json），EPSG:4326 |
| `area_statistics.json` | JSON | 码表 + 各类别像元数/占比/估算面积 + 可选变化检测 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

- **输入**：本地 24 波段 GeoTIFF（band 1-12 = 1-12 月均温 °C，band 13-24 = 1-12 月降水 mm）
- **合成模式**：本地生成沿纬度分带的月值气候场，无外部数据源
- **分类规则**：Peel, M. C., Finlayson, B. L., McMahon, T. A. (2007), HESS

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
