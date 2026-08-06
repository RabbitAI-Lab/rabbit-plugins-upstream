on:
  schedule:
    - cron: '0 0 1 * *'  # Monthly
jobs:
  download:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install requests
      - run: |
          python scripts\osm-data-download.py download \
            --feature building --bbox 116.0 39.8 116.8 40.2 \
            --output data/beijing_buildings.geojson
```

### PostGIS Import
```bash
python scripts\osm-data-download.py download   --feature building --bbox 116.0 39.8 116.8 40.2   --output buildings.geojson

ogr2ogr -f PostgreSQL PG:"dbname=gis_db" buildings.geojson -nln osm_buildings
```

### Performance Tips
- Add `--rate-delay 2` for complex queries to avoid rate limiting
- Use `--timeout 300` for large country-sized queries
- Custom Overpass QL: use `--query` with raw QL for unsupported feature types

---

## 中文说明

通过 Overpass API 下载 OpenStreetMap 数据。按边界框、原始标签、**语义预设**（water/road/building/green）或**行政区名称**（如 `北京市朝阳区`）下载，输出 GeoJSON 和/或 Shapefile，可选自动 zip 打包、跨界裁剪与 QA 摘要。

## 功能特性

- **按 bbox + 标签**：下载道路、建筑、POI、土地利用、自然地物
- **按行政区名称（新）**：`download-place --place "北京市朝阳区" --preset water` 自动解析行政区多边形、查询并裁剪、输出 QA
- **语义预设（新）**：`water` / `road` / `building` / `green` 一次合并多组标签
- **多格式导出（新）**：`--formats geojson,shapefile` 同时输出；混合几何自动拆分
- **Shapefile 打包（新）**：`--zip-shapefile` 输出含 `.shp/.shx/.dbf/.prj/.cpg` 的完整 zip
- **跨界裁剪（新）**：自动把跨边界几何裁剪到行政多边形，输出严格匹配目标区
- **QA 摘要（新）**：`--qa` 写出要素数量、几何类型统计、bbox、CRS、解析到的 OSM 关系 ID、行政层级、Overpass 查询和输出文件清单
- **UTF-8 DBF + .cpg**：中文名可被 QGIS / ArcGIS 正确读取
- **端点 fallback**：429/504 时自动尝试备用 Overpass 镜像
- **自定义 Overpass QL**：运行自定义查询
- **多种输出**：GeoJSON 和 Shapefile
- **速率限制**：内置延迟，尊重 API 限制
- **标签参考**：内置常见 OSM 标签列表

## 常见要素类型

| 类型 | OSM 标签 | 示例 |
|------|---------|------|
| 道路 | `highway=*` | motorway, primary, residential |
| 建筑 | `building=*` | yes, residential, commercial |
| POI | `amenity=*` | restaurant, school, hospital |
| 土地利用 | `landuse=*` | residential, forest, farmland |
| 自然地物 | `natural=*` | water, wood, grassland |
| 水系 | `waterway=*` | river, stream, canal |

## 使用示例

### 按 bbox 下载
```bash
python scripts\osm-data-download.py download \
  --bbox "116.0,39.5,116.8,40.2" \
  --feature highway --output roads.geojson
```

### 按行政区名下载（新）
```bash
python scripts\osm-data-download.py download-place \
  --place "北京市朝阳区" \
  --preset water \
  --formats "geojson,shapefile" \
  --zip-shapefile \
  --qa \
  -o chaoyang_water
```
一次性输出：
- `chaoyang_water.geojson`（所有要素）
- `chaoyang_water_Point.shp` + sidecars
- `chaoyang_water_LineString.shp` + sidecars
- `chaoyang_water_Polygon.shp` + sidecars
- `chaoyang_water.zip`（完整 Shapefile 套件）
- `chaoyang_water.qa.json`（QA 摘要）

### 按行政区 + 原始 feature
```bash
python scripts\osm-data-download.py download-place \
  --place "成都市武侯区" \
  --feature highway \
  -o wuhou_roads.geojson
```

### 自定义查询
```bash
python scripts\osm-data-download.py query \
  --query '[out:json][timeout:60];(node["amenity"="restaurant"](39.8,116.3,40.0,116.5););out body;' \
  --output restaurants.geojson
```

### 列出常见标签和预设
```bash
python scripts\osm-data-download.py list-tags
```

## 安装

```bash
pip install requests>=2.28.0 tqdm>=4.64.0
# 或: pip install -r scripts/requirements.txt
```

## 参数说明

- `--bbox`: 边界框 `lon_min,lat_min,lon_max,lat_max`
- `--feature`: 要素类型
- `--value`: 特定标签值（如 `restaurant`）
- `--output`: 输出文件路径
- `--format`: 输出格式（`geojson`, `shapefile`）
- `--query`: 自定义 Overpass QL 查询
- `--timeout`: API 超时秒数（默认: 60）
- `--rate-delay`: 请求间隔秒数（默认: 1.0）

## 输出结果

- **GeoJSON**: 标准 GeoJSON，OSM 标签作为属性
- **Shapefile**: ESRI Shapefile 含属性表

## API 信息

- **端点**: `https://overpass-api.de/api/interpreter`
- **无需 API 密钥**
- **速率限制**: 请合理使用，大查询可能需要时间
- **数据许可**: ODbL (OpenStreetMap contributors)

## 依赖库

```
requests>=2.28.0
tqdm>=4.64.0
```

## 几何类型

OSM 要素有三种几何类型 — 根据用途选择：

| 类型 | OSM 元素 | 典型要素 | 用途 |
|------|---------|---------|------|
| 点 | `node` | POI、设施、商铺 | 点分析、热力图 |
| 线 | `way`（开放） | 道路、河流、边界 | 网络分析、路径规划 |
| 面 | `way`（闭合）、`relation` | 建筑、土地利用、湖泊 | 面积计算、空间连接 |

工具自动检测几何类型。使用 `--geometry-type` 过滤。

## 最大边界框尺寸

过大的边界框会导致超时和过量数据：

| 区域大小 | 建议 |
|---------|------|
| <0.25°×0.25° | 大多数查询安全 |
| 0.25°–0.5°×0.25°–0.5° | 密集城区建议最大值 |
| >0.5°×0.5° | 分割为小块；使用 `--split-bbox 4` |

```bash
# 自动将大边界框拆分为 4 个子查询
python scripts\osm-data-download.py download \
  --bbox "115.5,39.0,117.5,41.0" \
  --feature building --output buildings.geojson --split-bbox 4
```

## Shapefile 输出

直接导出为 ESRI Shapefile 格式：

```bash
python scripts\osm-data-download.py download \
  --bbox "116.3,39.8,116.5,40.0" \
  --feature building --output buildings.shp --format shapefile
```

**注意**：Shapefile 列名截断为 10 字符。需要完整属性名时请使用 `--format geojson`。

## 字符编码

Shapefile 属性表默认使用 UTF-8 编码。如在 ArcGIS 中显示乱码：

- 设置环境变量：`SHAPE_ENCODING=UTF-8`
- 或在 QGIS 中打开（原生支持 UTF-8）
- GeoJSON 输出始终为 UTF-8

## 错误处理与重试逻辑

工具自动处理常见 HTTP 错误：

| HTTP 代码 | 含义 | 工具行为 |
|-----------|------|---------|
| 400 | 查询语法错误 | 报告错误，建议修复 |
| 429 | 超出速率限制 | 等待 60 秒，最多重试 3 次 |
| 504 | 服务器超时 | 增加超时，最多重试 3 次 |
| 500 | 服务器错误 | 等待 30 秒，重试 |

使用 `--max-retries 5` 和 `--retry-delay 120` 自定义重试行为。

## 备用 Overpass 端点

主端点缓慢或不可用时：

| 端点 | 位置 | 说明 |
|------|------|------|
| `https://overpass-api.de/api/interpreter` | 德国 | 默认，最稳定 |
| `https://z.overpass-api.de/api/interpreter` | 德国 | 镜像 |
| `https://lz4.overpass-api.de/api/interpreter` | 德国 | 镜像 |
| `https://overpass.kumi.systems/api/interpreter` | 芬兰 | 备用 |
| `https://overpass.openstreetmap.ru/api/interpreter` | 俄罗斯 | 备用 |

使用 `--endpoint https://overpass.kumi.systems/api/interpreter` 指定。

## 空结果处理

如果查询无要素：

1. 验证边界框坐标（lon/lat 顺序、符号）
2. 检查标签拼写（对照 OSM Wiki）
3. 尝试更大的边界框 — 该区域可能无映射要素
4. 使用 `list-tags` 查看区域内可用要素

工具在空结果时打印警告并正常退出。

## 引用格式

使用 OSM 数据时请引用（ODbL 许可要求）：

```bibtex
@misc{osm_contributors,
  author       = {{OpenStreetMap contributors}},
  title        = {OpenStreetMap Data},
  howpublished = {\url{https://www.openstreetmap.org}},
  year         = {2024},
  note         = {ODbL License}
}

@software{osm_data_download,
  author  = {ruiduobao},
  title   = {OSM Data Download Tool},
  url     = {https://github.com/ruiduobao/osm-data-download},
  version = {0.1.0},
  year    = {2024},
}
```

使用 OSM 数据时请显示：`© OpenStreetMap contributors (ODbL)`。

## 故障排除

| 错误 | 原因 | 解决方案 |
|------|------|---------|
| `ConnectionError` | 网络问题 | 检查网络，重试 |
| `HTTP 429` | 速率限制 | 等待 60 秒后重试 |
| `ValueError` | 边界框格式错误 | 检查 `lon_min,lat_min,lon_max,lat_max` |
| 无输出 | 区域内无要素 | 验证边界框，检查标签拼写 |
| `ModuleNotFoundError` | 缺少依赖 | 运行 pip install |
| `HTTP 504` | 服务器超时 | 缩小边界框，增加 `--timeout` |
| ArcGIS 中乱码 | 编码问题 | 使用 UTF-8 或输出 GeoJSON |

## 数据来源

OpenStreetMap via Overpass API. 数据 © OpenStreetMap contributors (ODbL)。
