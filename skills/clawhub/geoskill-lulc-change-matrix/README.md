# Land Cover Transition Matrix (geoskill-lulc-change-matrix)

> Pixel-wise cross-tabulation of two land cover classification rasters, producing a transition matrix, change area statistics, and Sankey flow data

---

## 1. Overview

Performs pixel-wise cross-tabulation of two land cover classification rasters (integer classes) to quantify transitions between classes. Outputs a transition matrix (rows = earlier epoch t1, columns = later epoch t2, cells = pixel counts), per-class gross loss / gross gain / net change with area statistics, and nodes + links data ready for Sankey flow diagrams. Typical applications: cropland loss / built-up expansion monitoring, land use transition analysis, and national land-change ledgers. Diagonal cells are unchanged pixels; off-diagonal cells are pixels that changed class; combined with a bbox, pixel counts can be converted to square kilometers. Synthetic mode injects a deterministic number of class transitions (e.g. cropland → built_up), so that "detected change = injected change" can be verified offline.

## 2. Features

Performs pixel-wise cross-tabulation of two land cover classification rasters (integer classes) to quantify transitions between classes. Outputs a transition matrix (rows = earlier epoch t1, columns = later epoch t2, cells = pixel counts), per-class gross loss / gross gain / net change with area statistics, and nodes + links data ready for Sankey flow diagrams. Typical applications: cropland loss / built-up expansion monitoring, land use transition analysis, and national land-change ledgers. Diagonal cells are unchanged pixels; off-diagonal cells are pixels that changed class; combined with a bbox, pixel counts can be converted to square kilometers. Synthetic mode injects a deterministic number of class transitions (e.g. cropland → built_up), so that "detected change = injected change" can be verified offline.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-lulc-change-matrix.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `transition_matrix.csv` | CSV | Transition matrix (with row/column totals) |
| `change_areas.json` | JSON | Per-class gross loss / gain / net change + area in km² |
| `sankey.json` | JSON | Sankey flow nodes + links |
| `change_map.tif` | GeoTIFF (int32) | Change map (0=unchanged, 1=changed) |
| `output-manifest.json` | JSON | Run manifest |


## 6. Technical Principle

(See SKILL.md for details.)

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 土地覆被转移矩阵（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-lulc-change-matrix
description: '两期土地覆被分类栅格逐像元交叉制表，输出转移矩阵、变化面积统计与 Sankey 流向数据'
---

# 土地覆被转移矩阵 | Land Cover Transition Matrix

对两期土地覆被分类栅格（整数类别）做逐像元交叉制表，量化类别之间的
转移关系。输出转移矩阵（行=前期 t1，列=后期 t2，元素为像元数）、
逐类毛损失/毛增益/净变化与面积统计，以及可直接用于 Sankey 流向图的
nodes + links 数据。

典型应用：耕地流失/建设用地扩张监测、土地利用转型分析、国土变化台账。
对角线为未变化像元，非对角线即发生转移的像元；结合 bbox 可把像元数
换算为平方公里。合成模式会注入确定数量的类别转移（如 cropland → built_up），
便于离线验证「检测到的变化量 = 注入量」。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'pandas'
```

## 使用方法

### 基本用法

```bash
python geoskill-lulc-change-matrix.py --bbox 116.0 39.0 117.0 40.0 --n-classes 5
```

### 示例 1（合成数据，离线）

```bash
python geoskill-lulc-change-matrix.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（读取两期本地分类栅格）

```bash
python geoskill-lulc-change-matrix.py --t1 cls_2015.tif --t2 cls_2020.tif --output-dir ./out
```

### 示例 3（不同区域 + 静默）

```bash
python geoskill-lulc-change-matrix.py --bbox 121.0 31.0 122.0 32.0 --synthetic --quiet --output-dir ./out
```

### 示例 4（3 类场景）

```bash
python geoskill-lulc-change-matrix.py --bbox 116 39 117 40 --synthetic --n-classes 3 --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `transition_matrix.csv` | CSV | 转移矩阵（含行列合计） |
| `change_areas.json` | JSON | 逐类毛损失/增益/净变化 + 面积 km² |
| `sankey.json` | JSON | Sankey 流向 nodes + links |
| `change_map.tif` | GeoTIFF (int32) | 变化图（0=未变，1=变化） |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- 本地两期分类 GeoTIFF（整数类别，空间对齐）；
- `--synthetic` 离线合成两期分类对（无需网络、无需账号）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
