# `world-boundary-download` Skill — Design Document

> 目标：给世界上任意地区（中国除外，另有 `china-admin-divisions` skill 负责）按 ISO/名称/经纬度框下载行政区划矢量
> 数据，输出 Shapefile / GeoJSON / GeoPackage / TopoJSON 任一格式，可选 GeoJSON bbox + 面积。

---

## 1. 背景与定位

公众号「我的产品推文」下的「下载/工具类」产品。跟现有 `china-admin-divisions` skill 形成互补：
`china-admin-divisions` 专做中国大陆 5 级精细区划（瑞朵豹 API），本 skill 覆盖**全球**任意地区的多级
行政区划，目标是**一站式、轻量、可商用**。

`boundry` 是有意拼错的目录名（项目名 `world_boundry_download`），保留原貌以便与用户原文保持一致。

## 2. 数据源选型

| 优先级 | 数据源 | 覆盖 | 等级深度 | 商用 | 备注 |
|---|---|---|---|---|---|
| **P0（默认）** | [geoBoundaries](https://www.geoboundaries.org/) (gbOpen) | 199 个实体（所有 UN 成员国 + 格陵兰 / 台湾 / 纽埃 / 科索沃） | ADM0–ADM5（视国家而异，常有 0–4） | **可**，CC BY 4.0，需注明 | JSON API + GitHub LFS 静态下载，gbOpen/Authoritative/Humanitarian 三个分支可切换 |
| **P1（备选）** | [GADM 4.1](https://gadm.org/) | 全球 | ADM0–ADM5 | **限非商业** | 数据更细，但商用需授权 |
| **P2（兜底）** | [Natural Earth](https://www.naturalearthdata.com/) | 全球 | ADM0 + 部分 ADM1（10m/50m/110m） | **可**，公共域 | 风格化、轻量、适合底图；不作为精细数据源 |

主选 **geoBoundaries** 的理由：
- **商用授权清晰**（CC BY 4.0 — 注明即可），公众号产品推文会公开发布，可避免 GADM 的合规风险
- **API 直接出 SHP / GeoJSON / TopoJSON**，免去后处理
- **元数据完整**（边界 ID、年份、来源、license 文本、面积、顶点数等），可以原样转发
- **粒度对绝大多数用户够用**（基本所有国家都有 ADM0–ADM2，很多有 ADM3–ADM4）

降级链：`geoBoundaries → GADM → Natural Earth`，在用户指定 `--source` 时跳过降级。

## 3. 功能边界

### 3.1 范围内
- 任意国家的 ADM0–ADM5 矢量下载（默认 gbOpen）
- 按国家名（英文 / 中文别名）→ ISO3 自动解析
- 按 bbox 框选裁剪某国家矢量后导出
- 多国拼接（区域下载，bbox 覆盖多国时）
- 输出 SHP（zip）/ GeoJSON / GPKG / TopoJSON
- 元信息查询：bbox、面积（km²，按 WGS84 椭球精确计算 + 1 km 缓冲）
- 列出某国家在数据源中实际可用的等级
- 缓存：同一文件不重复下载

### 3.2 范围外
- 国家级以下的中文地名/别名表（依赖国家统计局数据，超出本 skill 范围）
- 街道级 / 邮政编码级（用 OSM Overpass，不在此 skill）
- 在线预览地图 / 矢量瓦片（用 `mbtiles` 或独立服务）
- 数据源数据本身的纠错（直接信源标注）

## 4. 目录结构

```
world_boundry_download/
├── SKILL.md                       # Mavis skill 入口
├── README.md                      # 用户文档
├── docs/
│   ├── DESIGN.md                  # 本设计文档
│   └── DATA_SOURCES.md            # 数据源详细说明与对比
├── scripts/
│   ├── world_admin_download.py    # CLI 入口
│   ├── core/                      # 核心模块
│   │   ├── __init__.py
│   │   ├── geoboundaries.py       # geoBoundaries API 客户端 + 下载
│   │   ├── gadm.py                # GADM 4.1 下载
│   │   ├── natural_earth.py       # Natural Earth 下载
│   │   ├── iso_resolver.py        # 国家名 ↔ ISO 解析（含中文别名）
│   │   ├── sources.py             # 数据源注册 + 降级链
│   │   ├── format.py              # 格式转换（下载 zip → 解压/转码 → 输出）
│   │   ├── geometry.py            # bbox / 面积 / 裁剪
│   │   ├── cache.py               # HTTP 缓存
│   │   ├── exceptions.py          # 异常类
│   │   └── countries.py           # 内置国家名 / ISO 表（pycountry 兜底）
│   └── __init__.py
├── tests/
│   ├── conftest.py
│   ├── test_iso_resolver.py
│   ├── test_geoboundaries.py
│   ├── test_gadm.py
│   ├── test_format.py
│   └── test_geometry.py
└── examples/
    └── demo.ipynb                 # 可选：可视化示例
```

## 5. CLI 设计

参考 `china-admin-divisions` 的 CLI 风格，保持子命令统一、易记。

```
python scripts/world_admin_download.py <subcommand> [args...]
```

### 5.1 子命令清单

| 子命令 | 用途 | 主要参数 |
|---|---|---|
| `search` | 模糊搜索国家（英文 / 中文） | `keyword` [--limit] |
| `resolve-iso` | 国家名 ↔ ISO 转换 | `name` 或 `--iso XXX` |
| `list-sources` | 列出可用数据源 | (无) |
| `levels` | 列出某国家在指定数据源中可下载的 ADM 等级 | `--iso` 或 `--name` [--source] |
| `info` | 单个边界的元信息（bbox、面积、来源、license） | `--iso` + `--level` [--source] |
| `bbox` | 只看 bbox + 面积（不下载） | `--iso` + `--level` [--expand-km] |
| `country` | 下载一个国家的某 ADM 等级 | `--iso` 或 `--name` + `--level` + `--format` + `--out` |
| `region` | 按 bbox 框选并裁剪某国家 | `--iso` + `--level` + `--bbox W,S,E,N` + `--format` + `--out` |
| `multi` | 多国拼接成单文件（区域下载） | `--isos` + `--level` + `--format` + `--out` |
| `all-levels` | 一次性下载某国家所有等级 | `--iso` + `--out` (dir) |

### 5.2 通用参数

- `--source` — 数据源选择 `geoboundaries`（默认）/ `gadm` / `natural_earth`
- `--format` — `shp`（zip）/ `geojson` / `gpkg` / `topjson`，默认 `shp`
- `--out` — 输出路径（默认当前目录；文件夹时按需自动建子目录）
- `--simplified` — 使用简化版（geoBoundaries 提供的简化 GeoJSON，文件更小，适合底图）
- `--expand-km` — bbox 扩展公里数（默认 0）
- `--cache-dir` — 缓存目录（默认 `~/.cache/world-boundary-download/`）
- `--no-cache` — 跳过缓存
- `--plain` — 输出非 JSON 文本（人类可读）

### 5.3 输出契约

`info` / `bbox` 子命令返回 JSON：

```json
{
  "boundary_id": "CHN-ADM1-43563684",
  "name": "China",
  "iso3": "CHN",
  "level": "ADM1",
  "year": "2019",
  "source": "geoboundaries",
  "release": "gbOpen",
  "license": "Public Domain",
  "license_source": "commons.wikimedia.org/wiki/File",
  "contributor": "geoBoundaries, Wikimedia Commons",
  "build_date": "Dec 12, 2023",
  "adm_unit_count": 34,
  "download_url": "https://github.com/wmgeolab/geoBoundaries/raw/.../geoBoundaries-CHN-ADM1-all.zip",
  "bbox_wgs84": [73.5, 18.16, 134.77, 53.56],
  "bbox_wgs84_expanded": [72.46, 17.31, 135.81, 54.41],
  "area_km2": 9562911.0,
  "area_km2_expanded": 10322990.0
}
```

`country` / `region` / `multi` 完成后打印一行：

```json
{"ok": true, "saved": "D:/data/CHN_ADM1.zip", "size_bytes": 1234567, "format": "shp", "source": "geoboundaries"}
```

## 6. 核心模块设计

### 6.1 `geoboundaries.py`

- `fetch_metadata(iso, adm, release="gbOpen") -> dict` — 调 API 拿元数据
- `fetch_all_metadata(release="gbOpen") -> list[dict]` — 一次性拉全部索引，缓存到本地
- `download(iso, adm, *, release, simplified, out_dir) -> Path` — 下载并解压到指定目录
- `download_direct(iso, adm, *, release, fmt) -> bytes` — 原始字节（用于格式转换）

API URL 模板：

```
https://www.geoboundaries.org/api/current/{release}/{ISO3}/{ADM}/
https://www.geoboundaries.org/api/current/{release}/ALL/ALL/
```

ZIP 内文件结构（实测经验）：
```
geoBoundaries-{ISO}-{ADM}-all.zip
├── geoBoundaries-{ISO}-{ADM}.shp
├── geoBoundaries-{ISO}-{ADM}.shx
├── geoBoundaries-{ISO}-{ADM}.dbf
├── geoBoundaries-{ISO}-{ADM}.prj
├── geoBoundaries-{ISO}-{ADM}.geojson
├── geoBoundaries-{ISO}-{ADM}.topojson
└── geoBoundaries-{ISO}-{ADM}_simplified.geojson  (可选)
```

### 6.2 `gadm.py`

- `download_country(iso3, level, *, fmt="shp", out_dir) -> Path`
- 拼接 URL：`https://geodata.ucdavis.edu/gadm/gadm4.1/shp/gadm41_{ISO3}_{level}.zip`
- level 范围 0–5，GADM 提供 .shp + .gpkg
- 仅供非商用，调用前打印 license 提示

### 6.3 `natural_earth.py`

- 通过 `https://www.naturalearthdata.com/` 跳转到 naciscdn.org 静态文件
- ADM0（countries）+ ADM1（states/provinces），1:10m / 1:50m / 1:110m 三种 scale
- 仅作兜底，文档中说明

### 6.4 `iso_resolver.py`

- **主表**：内置 `pycountry` 提供的 250 个国家（en / fr / es 等），含常见中文别名（中国、China、CN、CHN、中华人民共和国）
- **不依赖网络**：核心 ISO 解析用 `pycountry` 离线查询
- **加分项**：内置「中文国家名 / 地区别名 → ISO3」表（覆盖：CN=中国，HK=中国香港，MO=中国澳门，TW=中国台湾；US=美国/美利坚合众国；UK=英国/大不列颠等）
- **未匹配**：返回候选列表 + 提示用户用 `--iso`

### 6.5 `sources.py`

数据源注册表 + 降级链：

```python
SOURCES = {
    "geoboundaries": GeoBoundariesSource(),
    "gadm": GadmSource(),
    "natural_earth": NaturalEarthSource(),
}

DEFAULT_FALLBACK_CHAIN = ["geoboundaries", "gadm", "natural_earth"]
```

### 6.6 `format.py`

负责把原始下载（geoBoundaries 的 zip 含 shp + geojson）转成用户要求的格式：

- 输入：本地 zip 路径或内存 bytes
- 处理：
  - `shp`：直接重命名 zip，挑选 shp/shx/dbf/prj/cpg 重新打包
  - `geojson`：读 zip 内 .geojson，写出
  - `gpkg`：用 `geopandas` 读 shp → 写 gpkg
  - `topjson`：读 zip 内 .topojson，写出

### 6.7 `geometry.py`

- `bbox(gdf) -> (minx, miny, maxx, maxy)`
- `bbox_expanded(bbox, km) -> bbox` — 1 km ≈ `1/110.574` 度（lat），经度按 cos(mid_lat) 修正
- `area_km2(gdf) -> float` — 用 WGS84 椭球精确面积（`geopandas.GeoSeries.to_crs(epsg=6933).area / 1e6` 或更精确的 `pyproj`）
- `clip_to_bbox(gdf, bbox) -> gdf`

### 6.8 `cache.py`

- 基于 URL + etag 的磁盘缓存
- 默认 `~/.cache/world-boundary-download/`
- `--no-cache` 跳过

## 7. 错误与边界

| 场景 | 处理 |
|---|---|
| 输入国名无匹配 | 返回候选列表，提示加 `--iso` |
| ISO 不存在 / ADM 等级数据源没有 | 报错并列出该国可用等级 |
| 网络失败 | 指数退避重试 3 次后报错；缓存命中时跳过 |
| 下载的 zip 损坏 / 不是合法 SHP | 用 `fiona.open` 校验，失败则报错 |
| 经度跨 ±180° 边界 | bbox 工具内部做处理（不切片，提示用户） |
| GADM 商用警告 | 调用 GADM 之前打印一次 license 提示 |
| 自然地球多 parts shapefile | 保留多 parts 写出 |

## 8. 测试策略

- **单元**：
  - `test_iso_resolver` — 中国、China、CN、CHN、USA、United States 各种别名都能解析
  - `test_geometry` — bbox/area 计算已知答案（如 USA bbox 应包含 [-125, 24, -66, 49]）
- **集成（跑真网络，离线时 skip）**：
  - `test_geoboundaries` — `info --iso CHN --level ADM1` 应返回非空元数据
  - `test_gadm` — `country --iso CHN --level ADM0 --format geojson --out /tmp/x.geojson` 应产出可读 GeoJSON
  - `test_format` — 下载 → 转 gpkg → 重读几何数一致
- **手工冒烟**：
  - `country --iso CHN --level ADM1 --format shp` → 用 `ogrinfo` 验证 .shp 可读

测试网络调用标记 `@pytest.mark.network`，本地无网时自动 skip。

## 9. 性能与体积

- 缓存：避免重复下载同 URL（按 SHA1(url) 作 key）
- 流式下载：HTTP 用 `stream=True` + 写临时文件 + `os.replace`（避免大文件占用内存）
- 大文件：geoBoundaries 的 ADM2 / ADM3 shp zip 单文件可能 5–50 MB，没问题
- 多国拼接：每个国家并发下载（`concurrent.futures.ThreadPoolExecutor`，max_workers=4）

## 10. 依赖

- 必需：`requests`, `geopandas`, `shapely`, `pyogrio`（或 `fiona`）, `pyproj`
- 推荐：`pycountry`（ISO 离线表）、`pytest`（测试）

均已在当前环境（Python 3.12, geopandas 1.1.1）验证可用。

## 11. 交付清单

- [x] `docs/DESIGN.md`（本文件）
- [x] `docs/DATA_SOURCES.md`（数据源说明）
- [x] `scripts/world_admin_download.py`（CLI 入口）
- [x] `scripts/core/*.py`（核心模块）
- [x] `tests/*.py`（单元 + 集成测试）
- [x] `SKILL.md`（Mavis 入口）
- [x] `README.md`（用户文档）
- [x] 真实下载端到端验证

## 12. 风险与备注

- `boundry` 拼写是用户的目录命名，保留不改。SKILL / Python 包名用 `world-boundary-download`（中划线）和 `world_admin_download`（下划线）。
- geoBoundaries 的 GitHub LFS 偶有 502，代码需有重试。
- 公众号产品推文场景下，GADM 的「非商用」约束是必须明示的硬性限制；默认数据源坚持用 geoBoundaries，避开这个雷。
- 中国/台湾/香港：geoBoundaries 把它们视作独立 ISO（CHN/HKG/MAC/TWN），下到台湾时按用户意图，默认会下载；不在这里加额外政治过滤器（不必要、且后续麻烦）。
