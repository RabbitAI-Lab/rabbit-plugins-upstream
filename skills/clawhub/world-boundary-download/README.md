# world-boundary-download

> 给世界上任意地区下载行政区划矢量数据。`SHP` / `GeoJSON` / `GeoPackage` / `TopoJSON`
> 任选输出，按国家 ISO / 名称 / 经纬度框拉数据。
>
> 项目根目录名沿用原作者拼写（`boundry`），SKILL / 包名用下划线版
> `world-boundary-download` / `world_admin_download`，方便与其它 skill 命名规范对齐。

## 安装

```bash
# 必需
pip install requests geopandas shapely pyogrio fiona pyproj pycountry

# 可选：TopoJSON 输出需要
pip install topojson
```

## 5 行极速上手

```bash
# 1. 找到中国的 ISO
python scripts/world_admin_download.py resolve-iso --name 中国

# 2. 列出可下载的等级
python scripts/world_admin_download.py levels --iso CHN

# 3. 拿一份中国的 ADM1 省级边界（Shapefile zip）
python scripts/world_admin_download.py country --iso CHN --level ADM1 --format shp

# 4. 拿一份裁剪到中国南方的 GeoJSON
python scripts/world_admin_download.py region --iso CHN --level ADM1 \
    --bbox "100,20,125,40" --format geojson

# 5. 一次性合并中日韩三国国界
python scripts/world_admin_download.py multi --isos CHN,JPN,KOR \
    --level ADM0 --format geojson
```

## 数据源

默认走 **geoBoundaries**（CC BY 4.0，**可商用**，注明即可）。备选 **GADM 4.1**
（非商用）与 **Natural Earth**（公共域）。详见 [docs/DATA_SOURCES.md](docs/DATA_SOURCES.md)。

自动降级链：`geoBoundaries → GADM → Natural Earth`，可通过 `--source` 强制锁定。

## 输出格式对照

| 格式 | 后缀 | 何时用 |
|---|---|---|
| `shp` | `.zip` | ArcGIS / QGIS 经典格式；字段名被截断到 10 字符 |
| `geojson` | `.geojson` | Web / 通用；字段名完整 |
| `gpkg` | `.gpkg` | 现代 GIS 通用；单文件、字段名完整、支持 SQL |
| `topojson` | `.topojson` | Web 地图，文件最小；需 `topojson` 包 |

## 常见场景速查

```bash
# 国家全境（ADM0/ADM1/ADM2...）
python scripts/world_admin_download.py country --iso CHN --level ADM1 --format shp
python scripts/world_admin_download.py country --iso USA --level ADM2 --format gpkg

# 简化几何（文件更小，适合底图）
python scripts/world_admin_download.py --simplified country --iso CHN --level ADM0 --format geojson

# 按 bbox 裁剪
python scripts/world_admin_download.py region --iso JPN --level ADM1 --bbox "130,30,142,42" --format geojson

# 多国拼接成单文件（区域下载）
python scripts/world_admin_download.py multi --isos CHN,JPN,KOR --level ADM0 --format gpkg
python scripts/world_admin_download.py multi --isos USA,CAN,MEX --level ADM1 --format shp

# 一次性下载某国所有等级
python scripts/world_admin_download.py all-levels --iso CHN --format shp

# 元信息（含 bbox、面积、license）
python scripts/world_admin_download.py info --iso CHN --level ADM1
python scripts/world_admin_download.py info --iso CHN --level ADM1 --expand-km 5

# 缓存管理
python scripts/world_admin_download.py cache-info
python scripts/world_admin_download.py cache-clear
```

## 设计文档

- [docs/DESIGN.md](docs/DESIGN.md) — 完整设计说明
- [docs/DATA_SOURCES.md](docs/DATA_SOURCES.md) — 数据源详细对比

## 引用 / 致谢

公众号产品推文使用本 skill 下载数据时，请按数据源要求注明：

- **geoBoundaries**：
  > "Boundaries are sourced from geoBoundaries (https://www.geoboundaries.org), CC BY 4.0."

- **GADM 4.1**（仅非商用时）：
  > "GADM data, https://gadm.org"

- **Natural Earth**：
  > "Made with Natural Earth. Free vector and raster map data @ naturalearthdata.com."

## License

本 skill 本身按 MIT 发布。**下游使用请遵守所选数据源的授权要求**，默认数据源
geoBoundaries 允许商业使用，注明即可。
