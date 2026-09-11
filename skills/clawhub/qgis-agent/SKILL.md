---
name: qgis-agent
description: 驱动本机 QGIS 的 1000+ Processing 算法（矢量地理处理、栅格与地形分析、插值、网络分析、格式转换、渲染出图），让 AI 智能体通过纯 HTTP 直接执行空间分析。架构：Agent --HTTP--> scripts/server.py (PyQGIS) --> QGIS 3.28+/4.x。Drive QGIS's 1000+ processing algorithms from any AI agent over plain HTTP.
---

# QGIS Agent

驱动本机 QGIS 的 1000+ Processing 算法（QGIS 原生 / GDAL / GRASS / SAGA / 3D / 点云），让 AI 直接用自然语言完成空间分析。

架构：`本技能(Agent) --HTTP--> scripts/server.py (PyQGIS) --> QGIS 4.x`

## 前置条件

- Windows 10/11 + **QGIS 3.28 及以上**（免费开源，OSGeo4W 独立安装包）——PyQGIS 需在 QGIS 自带 Python 中运行
- 服务端 HTTP 地址：`http://127.0.0.1:8767`（仅本机监听）

## 第一步：确保服务在运行

先探测服务是否已启动：

```bash
curl -s http://127.0.0.1:8767/health
# {"status":"ok","server":"qgis-agent-server","version":"1.0","algorithms":1000,"providers":6,...}
```

若未启动，后台启动服务（用 QGIS 自带 Python）：

```bash
"C:/Program Files/QGIS 4.0.3/bin/python-qgis.bat" "<本技能目录>/scripts/server.py" 8767
```

Windows 下也可运行 `scripts/start_server.bat`（自动探测 QGIS 安装目录，Ctrl+C 停止）。

## 第二步：调用工具（纯 HTTP，无需 MCP 客户端）

智能体直接用 curl 调用即可：

```bash
# 列出全部算法提供器（provider）及算法数量
curl -s http://127.0.0.1:8767/modules

# 列出某个提供器的全部算法（如 QGIS 原生算法）
curl -s http://127.0.0.1:8767/module/qgis

# 按关键词搜索算法（不确定算法 ID 时必用）
curl -s "http://127.0.0.1:8767/search?q=buffer"

# 查看算法完整参数签名（写 /call 前先查）
curl -s "http://127.0.0.1:8767/tool/native:buffer"

# 执行算法：POST /call  body = {"name": "算法ID", "arguments": {...}}
curl -s -X POST http://127.0.0.1:8767/call -H "Content-Type: application/json" \
  -d '{"name":"native:buffer","arguments":{"INPUT":"C:/data/roads.shp","DISTANCE":500,"OUTPUT":"C:/out/roads_buf.gpkg"}}'
```

调用流程：**/search 找算法 → /tool 查签名 → /call 执行**。算法 ID 格式为 `provider:算法名`，如 `native:buffer`、`gdal:rasterize`、`grass:r.slope.aspect`（QGIS 3.x 中 GRASS 提供器名为 grass7）。

## 模块速查（provider，QGIS 4.0 实测值）

| provider | 算法数(约) | 用途 |
|---|---|---|
| native | 339 | 矢量几何/叠加/分析/筛选/建表、栅格分析、地形分析、插值、制图 |
| grass | 307 | 水文分析、视域、成本路径、网络分配（QGIS 4 中 provider 名为 grass，3.x 为 grass7）|
| gdal | 59 | 格式转换、投影变换（warp）、栅格切片 |
| qgis | 39 | 重分类、坡向、 等 Raster terrain / 插值算法（部分与 native 重复）|
| pdal | 24 | 点云（LiDAR）处理 |
| 3d | 1 | TIN 插值、DEM 生成 |

实际数量以 `/modules` 返回为准（随安装的插件与版本变化）。

## 关键参数约定（重要，实测踩坑）

- **范围（Extent）字符串顺序是 `xmin,xmax,ymin,ymax`**（QGIS Processing 官方顺序），不是 minx,miny,maxx,maxy！
  例：`"483000,513000,4407000,4437000 [EPSG:32650]"`。服务端会自动解析并做 CRS 转换。
- **距离类参数（缓冲半径、间距、坡度阈值等）单位为米**——服务端已强制 Distance 单位为 Meters，即使 CRS 是经纬度也按米解释。
- 输出格式推荐 `.gpkg`（GeoPackage，单文件、无中文路径问题）；传 `"TEMPORARY_OUTPUT"` 生成临时图层。
- 枚举参数（如 TYPE、END_CAP_STYLE）传整数，具体取值查 `/tool/{算法ID}` 的 description。

## 工程 / 渲染 / 代码执行

```bash
# 查看当前工程与图层（含字段列表、要素数、CRS）
curl -s http://127.0.0.1:8767/project

# 打开 / 保存工程
curl -s -X POST http://127.0.0.1:8767/project/open -H "Content-Type: application/json" -d '{"path":"C:/data/demo.qgz"}'
curl -s -X POST http://127.0.0.1:8767/project/save -H "Content-Type: application/json" -d '{"path":"C:/out/demo.qgz"}'

# 渲染当前工程为 PNG（可指定图层与范围）
curl -s -X POST http://127.0.0.1:8767/render -H "Content-Type: application/json" \
  -d '{"output":"C:/out/map.png","width":1024,"height":768}'

# 执行任意 PyQGIS 代码（默认关闭，启动时设 PYQGIS_ENABLE_EXEC=1 开启）
curl -s -X POST http://127.0.0.1:8767/pyqgis -H "Content-Type: application/json" \
  -d '{"code":"print(QgsProject.instance().fileName())"}'
```

## 典型调用链（复合分析）

选址类需求按"缓冲区→叠加→筛选"链条自动拆解为多次 /call，例：
医院选址（距主干道 500m 内、坡度 < 5°）：
1. `native:buffer` 道路 500m → 2. `native:slope` DEM 求坡度 → 3. `qgis:reclassifybytable` 坡度二值化 → 4. `native:intersection` 叠加取交集

更多示例（缓冲区、裁剪、字段计算、坡度坡向、插值、热点分析、渲染出图等）见 `references/examples.md`。

## 错误处理

返回 `{"status":"error","message":"...","suggestion":"..."}`，常见情形：
- `algorithm not found` → 算法 ID 拼写错误，用 `/search?q=` 找正确 ID（同一算法在不同版本中可能挂在 native 或 qgis 下）
- `path outside whitelist` → 路径不在白名单，调整 `QGIS_ALLOWED_PATHS` 或换目录
- 参数不匹配 → 用 `/tool/{算法ID}` 核对参数名与类型
- 输入数据无效 → 确认文件路径存在、格式受 OGR/GDAL 支持

结果中 `elapsed_sec` 含执行耗时；输出为矢量数据时 `result` 内会带 `feature_count`、`geometry_type`、`size_mb`。

## 安全与配置

- 服务只监听 `127.0.0.1`，不会暴露到局域网
- 路径白名单：默认不限制；设置环境变量 `QGIS_ALLOWED_PATHS`（分号分隔多个路径）后，所有请求中的文件路径必须位于白名单目录内
  `set QGIS_ALLOWED_PATHS=C:/GIS-AI-Course/;D:/data/`
- PyQGIS 任意代码执行默认关闭（`/pyqgis` 返回 403），启动时设 `PYQGIS_ENABLE_EXEC=1` 才开启；仅在可信环境使用
- 谨慎执行写操作（覆盖输出）前，向用户确认目标数据
