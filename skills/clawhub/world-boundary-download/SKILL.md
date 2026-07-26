---
description: 'Download global administrative boundary vector data (Shapefile / GeoJSON
  /

  GeoPackage / TopoJSON) for any country or multi-country region. Backed by

  geoBoundaries (CC BY 4.0, default) with GADM 4.1 and Natural Earth as

  fallbacks. Supports bbox clipping, multi-country merge, and a rich

  metadata API (year, source, license, area, vertex count).

  '
name: world-boundary-download
---

# 全球行政区划下载（world-boundary-download）

> 给世界上任意地区（中国除外，另有 `china-admin-divisions` skill 负责）按
> ISO/名称/经纬度框下载行政区划矢量数据。默认数据源是 geoBoundaries
> （CC BY 4.0，**可商用**），备选 GADM 4.1 与 Natural Earth。

## Quickstart

```bash
# 1) 搜索国家（中文 / 英文 / ISO 代码均可）
python scripts/world_admin_download.py search 锦江   # 模糊搜索（任何关键词）
python scripts/world_admin_download.py search 美利坚
python scripts/world_admin_download.py resolve-iso --name 中国

# 2) 列出某国家在数据源中可下载的 ADM 等级
python scripts/world_admin_download.py levels --iso CHN
python scripts/world_admin_download.py levels --name 日本

# 3) 元信息（含 bbox、面积、来源、license）
python scripts/world_admin_download.py info --iso CHN --level ADM1
python scripts/world_admin_download.py info --iso CHN --level ADM1 --expand-km 1

# 4) 下载单个矢量（默认 zip 格式 = ESRI Shapefile）
python scripts/world_admin_download.py --format shp country --iso CHN --level ADM1
python scripts/world_admin_download.py --format geojson country --iso CHN --level ADM1
python scripts/world_admin_download.py --format gpkg country --iso CHN --level ADM1

# 5) 按经纬度框选并裁剪
python scripts/world_admin_download.py --format geojson region --iso CHN --level ADM1 --bbox "100,20,125,40"

# 6) 多国拼接（区域下载）
python scripts/world_admin_download.py --format geojson multi --isos CHN,JPN,KOR --level ADM0

# 7) 一次性下载某国所有等级
python scripts/world_admin_download.py --format shp all-levels --iso CHN

# 8) 简化版（geoBoundaries 提供的简化几何，文件更小）
python scripts/world_admin_download.py --simplified country --iso CHN --level ADM0 --format geojson

# 9) 强制使用某个数据源（跳过自动降级链）
python scripts/world_admin_download.py --source gadm country --iso CHN --level ADM1 --format shp
python scripts/world_admin_download.py --source natural_earth country --iso CHN --level ADM0 --format shp

# 10) 缓存管理
python scripts/world_admin_download.py cache-info
python scripts/world_admin_download.py cache-clear
```

## 子命令

| 子命令 | 用途 | 主要参数 |
|---|---|---|
| `search` | 模糊搜索国家（中文 / 英文） | `keyword` [--limit] |
| `resolve-iso` | 国家名 ↔ ISO 转换 | `--name` 或 `--iso` |
| `list-sources` | 列出可用数据源 | (无) |
| `levels` | 列出某国家在每个数据源中可下载的 ADM 等级 | `--iso` 或 `--name` [--source] |
| `info` | 单个边界的元信息（bbox、面积、来源、license） | `--iso` + `--level` [--source] [--expand-km] |
| `bbox` | 只看 bbox + 面积 | `--iso` + `--level` [--expand-km] |
| `country` | 下载一个国家的某 ADM 等级 | `--iso` 或 `--name` + `--level` + `--format` + `--out` |
| `region` | 按 bbox 框选并裁剪某国家 | `--iso` + `--level` + `--bbox W,S,E,N` + `--format` + `--out` |
| `multi` | 多国拼接成单文件 | `--isos` + `--level` + `--format` + `--out` |
| `all-levels` | 一次性下载某国家所有等级 | `--iso` 或 `--name` + `--out` (dir) |
| `cache-info` | 显示缓存信息 | (无) |
| `cache-clear` | 清除缓存 | (无) |

## 通用参数

- `--source` — 数据源选择 `geoboundaries`（默认）/ `gadm` / `natural_earth`
- `--format` — `shp`（zip）/ `geojson` / `gpkg` / `topjson`，默认 `shp`
- `--out` — 输出路径（默认当前目录；文件夹时按需自动建子目录）
- `--simplified` — 使用简化版（geoBoundaries 提供的简化 GeoJSON，文件更小，适合底图）
- `--expand-km` — bbox 扩展公里数（默认 0）
- `--cache-dir` — 缓存目录（默认 `~/.cache/world-boundary-download/`）
- `--no-cache` — 跳过缓存
- `--plain` — 输出非 JSON 文本（人类可读）

## 支持的下载格式

| `--format` | 输出后缀 | 备注 |
|---|---|---|
| `shp` | `.zip` | ESRI Shapefile（zip 内含 .shp/.shx/.dbf/.prj/.cpg） |
| `geojson` | `.geojson` | 标准 GeoJSON，单文件 |
| `gpkg` | `.gpkg` | GeoPackage，OGC 标准 |
| `topojson` | `.topojson` | TopoJSON，文件最小，需安装 `topojson` 包 |

## 数据源

| 数据源 | 覆盖 | 等级深度 | 商用授权 | 默认 |
|---|---|---|---|---|
| **geoBoundaries** | 全球 199 实体 | ADM0–ADM5（视国家） | **可**（CC BY 4.0） | ✅ |
| **GADM 4.1** | 全球 | ADM0–ADM5 | **限非商业** | 备选 |
| **Natural Earth** | 全球 | ADM0 + 部分 ADM1 | **可**（公共域） | 兜底 |

详细的对比与决策请见 [docs/DATA_SOURCES.md](docs/DATA_SOURCES.md)。

## 默认行为：自动降级链

不指定 `--source` 时，按优先级依次尝试：

```
geoboundaries → gadm → natural_earth
```

`geoboundaries` 失败（罕见，通常是 GitHub LFS 502）会接着试 `gadm`，再失败
用 `natural_earth` 兜底。调用结果里 `source` 字段会标明实际用到的源。

## Permissions

- **网络出口**：
  - `https://www.geoboundaries.org/` + `https://github.com/wmgeolab/...` (geoBoundaries)
  - `https://geodata.ucdavis.edu/gadm/...` (GADM)
  - `https://naciscdn.org/naturalearth/...` (Natural Earth)
- **环境变量读取**：无。
- **文件读取**：无（除脚本自身）。
- **文件写入**：CLI 输出目录（`--out` 指定的路径或当前目录）+ 缓存目录
  `~/.cache/world-boundary-download/`。

## Notes

- bbox 框选用平面近似：`1° lat ≈ 110.574 km`，`1° lon ≈ 111.320·cos(mid_lat) km`。
  `--expand-km` 用同样的近似。极地 / 跨 180° 经线会失真，但五级区划范围
  通常不会触发。
- Shapefile 字段名被截断到 10 字符（DBF 限制），多列名带 `_1` / `_2`
  后缀，与原名无强对应关系。如需保留完整字段名，使用 `--format gpkg`
  或 `--format geojson`。
- 默认缓存目录 `~/.cache/world-boundary-download/` 永久保存，每次运行
  都会先查缓存命中。可用 `cache-clear` 清理。
- GADM 4.1 在每次首次调用时会打印一次 license 提示；只有显式
  `--source gadm` 才会触发。

## Output Contract

`info` / `bbox` 子命令返回的 JSON 字段（节选）：

```json
{
  "boundary_id": "CHN-ADM1-43563684",
  "name": "China",
  "iso3": "CHN",
  "level": "ADM1",
  "year": "2019",
  "source": "geoboundaries",
  "license": "Public Domain",
  "license_source": "commons.wikimedia.org/wiki/File",
  "build_date": "Dec 12, 2023",
  "adm_unit_count": 34,
  "download_url": "https://github.com/wmgeolab/geoBoundaries/raw/.../geoBoundaries-CHN-ADM1-all.zip",
  "bbox_wgs84": [73.6, 18.17, 134.74, 53.57],
  "area_km2": 11917028.4,
  "feature_count": 34
}
```

`country` / `region` / `multi` 完成后打印：

```json
{
  "ok": true,
  "saved": "Z://tmp//world_test//chn_adm1.zip",
  "size_bytes": 59520,
  "format": "shp",
  "iso3": "CHN",
  "level": "ADM1",
  "source": "geoboundaries"
}
```

## 设计文档

详见 [docs/DESIGN.md](docs/DESIGN.md) 与 [docs/DATA_SOURCES.md](docs/DATA_SOURCES.md)。
