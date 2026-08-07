---
name: geoskill-lulc-change-matrix
description: '两期土地覆被分类栅格逐像元交叉制表，输出转移矩阵、变化面积统计与 Sankey 流向数据'
---

# 土地覆被转移矩阵 | Land Cover Transition Matrix

Perform pixel-by-pixel cross-tabulation of two land cover classification rasters (integer classes) to quantify transitions between classes. Outputs a transition matrix (rows = earlier epoch t1, columns = later epoch t2, cell values = pixel counts), per-class gross loss / gross gain / net change and area statistics, as well as nodes + links data ready to be used directly in a Sankey flow diagram.

Typical applications: cropland loss / built-up expansion monitoring, land use transition analysis, and national land change ledgers. Diagonal cells are unchanged pixels, while off-diagonal cells are pixels that have transitioned; combined with the bbox, pixel counts can be converted to square kilometers. Synthetic mode injects a known number of class transitions (e.g., cropland → built_up) so that "detected change = injected change" can be verified offline.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'pandas'
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-lulc-change-matrix.py --bbox 116.0 39.0 117.0 40.0 --n-classes 5
```

### Example 1 (synthetic data, offline)

```bash
python geoskill-lulc-change-matrix.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (read two local classification rasters)

```bash
python geoskill-lulc-change-matrix.py --t1 cls_2015.tif --t2 cls_2020.tif --output-dir ./out
```

### Example 3 (different area + quiet mode)

```bash
python geoskill-lulc-change-matrix.py --bbox 121.0 31.0 122.0 32.0 --synthetic --quiet --output-dir ./out
```

### Example 4 (3-class scenario)

```bash
python geoskill-lulc-change-matrix.py --bbox 116 39 117 40 --synthetic --n-classes 3 --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `transition_matrix.csv` | CSV | Transition matrix (with row and column totals) |
| `change_areas.json` | JSON | Per-class gross loss/gain/net change + area in km² |
| `sankey.json` | JSON | Sankey flow nodes + links |
| `change_map.tif` | GeoTIFF (int32) | Change map (0 = unchanged, 1 = changed) |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- Two local classification GeoTIFFs (integer classes, spatially aligned);
- `--synthetic` generates a two-epoch classification pair offline (no network, no account required).

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is performed locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
