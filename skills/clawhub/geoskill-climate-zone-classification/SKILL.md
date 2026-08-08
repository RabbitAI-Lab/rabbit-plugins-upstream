---
name: geoskill-climate-zone-classification
description: '基于月均温与月降水栅格的气候区划，支持柯本-盖格（Köppen-Geiger）规则树与简化 Strahler 发生分类，输出气候类别码 GeoTIFF + 面积统计 JSON，可选双期变化检测。Climate zone classification from monthly temperature/precipitation rasters (Köppen-Geiger rule tree & simplified Strahler), with area statistics and optional change detection.'
---

# 气候区划 | Climate Zone Classification

Performs climate zone classification from monthly mean temperature and monthly
precipitation rasters, for climate mapping, ecological zoning, agro-climatic
resource assessment, and climate change monitoring. Two schemes are built in:

- **Köppen-Geiger**: the classic rule tree (Peel et al. 2007 / Kottek et al.
  2006). Determines the five main groups A (tropical) / B (arid) / C
  (temperate) / D (continental) / E (polar) from the coldest/warmest month
  mean temperature, annual mean temperature, annual precipitation, and the
  seasonal distribution of precipitation, then subdivides into second and
  third letters, yielding 30 classes in total (Af tropical rainforest, Am
  tropical monsoon, Aw/As tropical savanna, BWh/BWk desert, BSh/BSk steppe,
  Cfa/Cfb/Cfc, Csa/Csb/Csc, Dfa…Dfd, ET tundra, EF ice cap).
- **Strahler (simplified genetic classification)**: aggregates temperature
  zones and moisture conditions into 10 genetic climate classes (tropical
  humid / tropical arid / humid subtropical / Mediterranean / marine west
  coast / humid continental / dry continental / subarctic / tundra / polar
  ice cap).

Supports a `--synthetic` mode that generates a simulated climate field zoned
along latitude (with physically consistent seasonal temperature cycles and
precipitation distributions) for offline validation of the full workflow and
class recovery. `--input2` enables two-epoch climate zone change detection.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## Usage / 使用方法

### Basic usage (bbox only, auto-synthetic, Köppen)

```bash
python geoskill-climate-zone-classification.py --bbox 116.0 39.0 117.0 40.0 --output-dir ./out
```

### Example 1: synthetic data Strahler classification

```bash
python geoskill-climate-zone-classification.py --bbox 116.0 39.0 117.0 40.0 --synthetic --classification strahler --output-dir ./strahler
```

### Example 2: real 24-band climate rasters (12 temperature + 12 precipitation)

```bash
python geoskill-climate-zone-classification.py --input climate.tif --classification koppen --output-dir ./real
```

### Example 3: two-epoch change detection

```bash
python geoskill-climate-zone-classification.py --input climate_1990.tif --input2 climate_2020.tif --classification koppen --output-dir ./change
```

### Example 4: synthetic data for a different region

```bash
python geoskill-climate-zone-classification.py --bbox 121.0 31.0 122.0 32.0 --synthetic --output-dir ./shanghai
```

### Example 5: Köppen vs Strahler comparison

```bash
python geoskill-climate-zone-classification.py --bbox 116 39 117 40 --synthetic --classification koppen --output-dir ./cmp_koppen --quiet
python geoskill-climate-zone-classification.py --bbox 116 39 117 40 --synthetic --classification strahler --output-dir ./cmp_strahler --quiet
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `climate_zones.tif` | GeoTIFF (float32) | Climate class code raster (code table in area_statistics.json), EPSG:4326 |
| `area_statistics.json` | JSON | Code table + per-class pixel count/fraction/estimated area + optional change detection |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/software versions) |

## Data Source / 数据源 / Source

- **Input**: local 24-band GeoTIFF (bands 1-12 = mean monthly temperature for Jan-Dec in °C, bands 13-24 = monthly precipitation for Jan-Dec in mm)
- **Synthetic mode**: monthly climate field zoned along latitude generated locally; no external data source
- **Classification rules**: Peel, M. C., Finlayson, B. L., McMahon, T. A. (2007), HESS

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default; no network requests are made
- `--synthetic` mode reads no external data
- All computation is performed locally; user data is never uploaded

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

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
