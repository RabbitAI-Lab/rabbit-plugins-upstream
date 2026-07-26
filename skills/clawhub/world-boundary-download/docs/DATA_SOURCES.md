# 数据源说明

> 详细对比 `geoBoundaries` / `GADM 4.1` / `Natural Earth` 三个候选数据源，
> 以及本 skill 默认的选型逻辑。

## 概览对比

| 维度 | geoBoundaries (gbOpen) | GADM 4.1 | Natural Earth |
|---|---|---|---|
| 官网 | https://www.geoboundaries.org/ | https://gadm.org/ | https://www.naturalearthdata.com/ |
| 覆盖 | 199 实体（UN 成员国 + 4 特殊） | 全球所有 | 全球 |
| ADM 等级 | 0–5（视国家而异） | 0–5 | 0 + 1（部分国家） |
| 商用授权 | **可**（CC BY 4.0，需注明） | **限非商用** | **可**（公共域） |
| 数据精度 | 多源汇总，含 OSM / OCHA / 国家测绘 | 多源汇总，精度较高 | 风格化，比例尺 1:10m/50m/110m |
| API | REST JSON | 无 REST（仅文件下载） | 静态文件 |
| 字段丰富度 | 丰富（年份、来源、license、面积、顶点数） | 基础（边界 ID、ISO） | 基础 |
| 更新频率 | 持续 | 较慢 | 较慢 |
| 体积 | 中（小国几 KB，大国 ADM3 可达 50 MB） | 大（精度高） | 小 |
| 本 skill 默认 | ✅ | 备选 | 兜底 |

## geoBoundaries 详解

### 三个 release 分支

| 分支 | 说明 |
|---|---|
| `gbOpen` | 默认；按各国"自报"边界，可能在争议地区重叠 |
| `gbAuthoritative` | 仅含"权威"边界（去掉了 OSM 等贡献的争议边界） |
| `gbHumanitarian` | 仅含人道主义目的边界（OCHA / HDX） |

默认用 `gbOpen`，覆盖最全。

### API 端点

```
单条元数据：
GET https://www.geoboundaries.org/api/current/{release}/{ISO3}/{ADM}/

批量索引（所有国家所有等级）：
GET https://www.geoboundaries.org/api/current/{release}/ALL/ALL/
```

`release` ∈ `gbOpen`, `gbAuthoritative`, `gbHumanitarian`
`ISO3` ∈ 199 个 ISO 3 字母国家代码（或 `ALL`）
`ADM` ∈ `ADM0`, `ADM1`, `ADM2`, `ADM3`, `ADM4`, `ADM5`（或 `ALL`）

### 元数据关键字段

```json
{
  "boundaryID": "CHN-ADM1-43563684",
  "boundaryName": "China",
  "boundaryISO": "CHN",
  "boundaryYearRepresented": "2019",
  "boundaryType": "ADM1",
  "boundaryCanonical": "People's Republic of China",
  "boundarySource": "geoBoundaries, Wikimedia Commons",
  "boundaryLicense": "Public Domain",
  "licenseDetail": "nan",
  "licenseSource": "commons.wikimedia.org/wiki/File",
  "boundarySourceURL": "...",
  "sourceDataUpdateDate": "Thu Jan 19 07:31:04 2023",
  "buildDate": "Dec 12, 2023",
  "Continent": "Asia",
  "admUnitCount": "34",
  "meanVertices": "173.0",
  "minVertices": "5",
  "maxVertices": "393",
  "meanPerimeterLengthKM": "...",
  "meanAreaSqKM": "...",
  "staticDownloadLink": "https://github.com/wmgeolab/geoBoundaries/raw/.../geoBoundaries-CHN-ADM1-all.zip",
  "gjDownloadURL": "https://github.com/wmgeolab/geoBoundaries/raw/.../geoBoundaries-CHN-ADM1.geojson",
  "tjDownloadURL": "https://github.com/wmgeolab/geoBoundaries/raw/.../geoBoundaries-CHN-ADM1.topojson",
  "imagePreview": "...",
  "simplifiedGeometryGeoJSON": "..."
}
```

### ZIP 内文件结构

实测 `geoBoundaries-CHN-ADM1-all.zip` 包含：

```
geoBoundaries-CHN-ADM1.shp         ← Shapefile
geoBoundaries-CHN-ADM1.shx
geoBoundaries-CHN-ADM1.dbf
geoBoundaries-CHN-ADM1.prj          ← WGS84
geoBoundaries-CHN-ADM1.geojson      ← GeoJSON
geoBoundaries-CHN-ADM1.topojson     ← TopoJSON
geoBoundaries-CHN-ADM1_simplified.geojson  ← 简化版（仅部分国家有）
```

## GADM 4.1 详解

### URL 模式

```
https://geodata.ucdavis.edu/gadm/gadm4.1/shp/gadm41_{ISO3}_{level}.zip
https://geodata.ucdavis.edu/gadm/gadm4.1/gpkg/gadm41_{ISO3}.gpkg
https://geodata.ucdavis.edu/gadm/gadm4.1/gadm_410-levels.zip  (全量 5 级)
```

`ISO3` 大写（如 `CHN`），`level` ∈ `0`..`5`。

### 授权

> "GADM data are freely available for academic and non-commercial use."
> —— GADM 官网许可说明

公众号产品推文属于**公开发布的商业内容**，默认不在 GADM 授权范围内。**本 skill 默认不调用 GADM**，
仅在用户显式 `--source gadm` 时启用，并打印一次 license 提示。

## Natural Earth 详解

### URL 模式

```
https://naciscdn.org/naturalearth/{scale}/cultural/ne_{scale}_admin_0_countries.zip
https://naciscdn.org/naturalearth/{scale}/cultural/ne_{scale}_admin_1_states_provinces.zip
```

`scale` ∈ `10m` / `50m` / `110m`（数字越小越精细，文件越大）。

### 适用场景

- 想要一张世界地图底图（`110m`，很小）
- 需要明确的国名/省名英文标签
- 备份数据源（geoBoundaries / GADM 都失败时）

### 限制

- 多数国家没有 ADM1（ADM1 覆盖不完整）
- 没有 ADM2+ 数据
- 比例尺风格化，几何精度不如 geoBoundaries / GADM

## 选型决策

```
1. 用户 --source 显式指定？
   ├─ 是 → 用指定的
   └─ 否 ↓
2. 默认 geoboundaries
   ├─ 成功 → 返回
   └─ 失败 ↓
3. 备选 gadm（打印 license 警告）
   ├─ 成功 → 返回
   └─ 失败 ↓
4. 兜底 natural_earth（仅 ADM0 / 部分 ADM1）
```

## 引用 / 致谢

公众号产品推文中使用本 skill 下载数据时，请按数据源要求注明：

- **geoBoundaries**：
  > "Boundaries are sourced from geoBoundaries (https://www.geoboundaries.org), CC BY 4.0."

- **GADM 4.1**（仅非商用时）：
  > "GADM data, https://gadm.org"

- **Natural Earth**：
  > "Made with Natural Earth. Free vector and raster map data @ naturalearthdata.com."
