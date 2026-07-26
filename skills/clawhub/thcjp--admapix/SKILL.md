---
slug: "admapix"
name: "admapix"
version: 1.0.31
displayName: "AdMapix"
summary: "AdMapix原始数据层，广告创意/应用/榜单/下载收入查询"
license: "Proprietary"
description: |-
  AdMapix 原始数据层客户端。覆盖广告创意搜索/计数/分布、应用与开发者画像、商店榜单、
  下载与收入估算、应用分发与全球推广、市场级搜索七大端点类别。作为薄客户端透传 API 返回的原始结构化 JSON，
  不分析、不总结、不排序、不生成页面。调用方 Agent 负责决定调用哪些端点、组合多调用工作流并完成分析.
  支持 X-API-Key 认证、page_size 上限 10 自动钳制、参数代码映射（创意类型/行业/国家/日期范围/排序）、
  filter-options 元数据发现。适用于广告创意监控、应用市场调研、竞品 SDK 审计、跨地区下载收入对比等场景.
tags:
  - 研发工具
  - Research
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# AdMapix

AdMapix 原始 API 薄客户端。获取原始结构化数据并返回 JSON，不分析、不总结、不排序、不生成页面。调用方 Agent 决定调用哪些端点、组合多调用工作流并完成分析.
**范围外**（本技能不做）：HTML/H5 页面生成、托管式深度研究、自主多步研究、摘要、洞察、推荐、仪表盘、消息发送.
## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| AdMapix下载收入查询 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent 平台**: 支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **网络**: 需可访问 `https://api.admapix.com`

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| AdMapix API | 远程 HTTP API | 必需 | https://www.admapix.com 注册获取 |
| ADMAPIX_API_KEY | 环境变量 | 必需 | 控制台 API Keys 创建；仅作 `X-API-Key` 请求头 |
| curl 或等价 HTTP 客户端 | 命令行工具 | 必需 | 系统自带或包管理器安装 |
| jq | JSON 处理工具 | 可选 | 提升结果可读性 |

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令驱动，需 exec 执行 curl 命令）
- **说明**: 基于自然语言指令驱动 Agent 调用 AdMapix API，透传原始结构化 JSON

## 核心能力

### 参数映射

阅读 `references/param-mappings.md` 将自然语言翻译为代码：

- 创意类型（`010`=视频等）、行业（`trade_level1`：`602`=游戏，`607`=金融...）、国家/地区分组、相对日期范围、排序、分页大小
- 未在 param-mappings 中列出的代码（子行业、媒体渠道、设备、商店类目等），调 `GET /api/data/filter-op

**处理**: 解析参数映射的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回参数映射的处理结果,包含执行状态码、结果数据和执行日志.
### 输出规则

返回 API 响应的**原始结构化 JSON** — 保留 API 字段名；不重命名、不丢弃、不总结、不排序、不评论。调用方 Agent 负责组合与分析.
- 响应结构因端点而异。通过直接 API 调用的创意搜索返回 `pageIndex` / `pageSize` / `totalSize` / `list`；MCP 工具额外包装 `request` / `page` / `page_size

**输入**: 用户提供输出规则相关的配置参数、输入数据和处理选项.
#
## 认证

使用 `ADMAPIX_API_KEY` 作为 `X-API-Key` 请求头。永不打印或暴露 Key.
```bash
admapix_auth_header="X-API-Key: ${ADMAPIX_API_KEY}"
curl -s "https://api.admapix.com/api/data/{endpoint}?{params}" -H "$admapix_auth_header"
curl -s -X POST "https://api.admapix.com/api/data/{endpoint}" \
  -H "$admapix_auth_header" -H "Content-Type: application/json" -d '{...}'
```

对于创意搜索，优先使用 `admapix.search_creatives` MCP 工具（如可用）；否则直接调 `POST /api/data/search`.
## 端点目录

每个端点是一个原始数据源。**首次调用某端点前请阅读对应参考文件**以获取确切参数和响应字段.
### 创意 / 广告 — `references/api-creative.md`

| 端点 | 方法 | 用途 |
|---:|---:|---:|
| `/api/data/search` | POST | 搜索广告创意 |
| `/api/data/count` | POST | 按条件统计创意数量 |
| `/api/data/count-all` | POST | 按维度分组的创意计数 |
| `/api/data/distribute` | POST | 创意分布维度查询 |
| `/api/data/distribute-dims` | GET | 可用分布维度列表 |
| `/api/data/content-detail` | GET | 单条创意详情（`related=imagevideo`） |
| `/api/data/item-apps` | POST | 创意关联的应用列表 |
| `/api/data/screen-types` | GET | 屏幕/元素类型代码 |
| `/api/data/page-config` | GET | 搜索页面配置 |

### 元数据 / 筛选 — `references/api-creative.md` + `references/param-mappings.md`

| 端点2 | 方法 | 用途 |
|:---:|:---:|:---:|
| `/api/data/filter-options` | GET | 全量筛选元数据：`countries`、`mediaChannels`、`adTypes`、`device`、`tradeLevel(Tree)`、`productModel` 等。拉取此端点可发现任意筛选器的有效代码。 |

### 应用 / 产品 / 公司 — `references/api-product.md`

| 端点3 | 方法 | 用途 |
|:------|------:|:------|
| `/api/data/unified-product-search` | POST | 统一应用/产品搜索 |
| `/api/data/product-search` | POST | 产品搜索 |
| `/api/data/company-search` | POST | 开发者/公司搜索 |
| `/api/data/app-detail` | GET | 按 `unifiedProductId` 查应用详情 |
| `/api/data/developer-detail` | GET | 开发者详情 |
| `/api/data/app-profile` | GET | 应用画像 |
| `/api/data/similar-apps` | POST | 相似应用 |
| `/api/data/sdk-detail` | GET | 应用使用的 SDK 列表 |
| `/api/data/product-content-search` | POST | 某产品的创意列表 |
| `/api/data/product-content-counts` | POST | 某产品的创意计数 |
| `/api/data/product-list` / `for-product-list` / `product-agg-list` | POST | 产品列表/聚合 |

### 榜单 — `references/api-ranking.md`

| 端点4 | 方法 | 用途 |
|---:|:---|---:|
| `/api/data/store-rank` | POST | 应用商店榜单（免费/付费/畅销） |
| `/api/data/generic-rank` | POST | 通用榜单 |
| `/api/data/store-categories` | GET | 商店类目代码 |
| `/api/data/store-countries` | GET | 商店国家代码 |

### 下载与收入（第三方估算） — `references/api-download-revenue.md`

| 端点5 | 方法 | 用途 |
|:------:|--------|:-------|
| `/api/data/download-date` / `download-detail` / `download-country` | GET/POST | 按日期/详情/国家的下载估算 |
| `/api/data/revenue-date` / `revenue-detail` / `revenue-country` | GET/POST | 按日期/详情/国家的收入估算 |

> 下载/收入数据为第三方**估算值**，非官方数据。原始数字按 API 返回透传；调用方 Agent 在展示时需注明为估算数据.
### 分发 — `references/api-distribution.md`

| 端点6 | 方法 | 用途 |
|----|:--:|---:|
| `/api/data/app-distribution` | POST | 应用级分发数据 |
| `/api/data/global-promote` | POST | 全球推广数据 |

### 市场 — `references/api-market.md`

| 端点7 | 方法 | 用途 |
|----|----|----|
| `/api/data/market-search` | POST | 市场级搜索/聚合 |

## 参数映射(补充)

- 创意类型（`010`=视频等）、行业（`trade_level1`：`602`=游戏，`607`=金融...）、国家/地区分组、相对日期范围、排序、分页大小
- 未在 param-mappings 中列出的代码（子行业、媒体渠道、设备、商店类目等），调 `GET /api/data/filter-options` 或端点专属维度接口（如 `store-categories`）获取

对于创意 `search` 端点，`page_size` 上限为 **10**（任何更大的请求自动钳制到 10；用 `page` 翻页获取更多）。其他列表端点使用各自文档中的范围.
## 输出规则(补充)

- 响应结构因端点而异。通过直接 API 调用的创意搜索返回 `pageIndex` / `pageSize` / `totalSize` / `list`；MCP 工具额外包装 `request` / `page` / `page_size`。`totalSize` 在过滤查询时可能为 `null` — 此时以 `list` 长度为准.
- 空 `list` 是合法结果（无匹配），非错误.
- 额外字段（如 `gptCorrect` 拼写建议）原样透传；不静默替换关键词.
**不做**：生成 H5/落地页/卡片/仪表盘、将记录隐藏在链接后、运行托管式深度研究或自主多步研究、在用户收到数据前主动产出分析/推荐.
## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及端点 |
|:-----|:-----|:-----|:-----|
| 竞品创意搜索 | "搜索美国游戏类视频广告" | 创意列表（ID、URL、首次出现时间） | search |
| 应用信息查询 | "查询某应用的详情和SDK" | 应用详情+SDK列表 | unified-product-search, app-detail, sdk-detail |
| 商店榜单查询 | "查询日本免费榜前20" | 应用排名列表 | store-rank, store-categories |
| 下载收入对比 | "对比美国和日本某应用下载量" | 多国下载估算数据 | download-country |
| 创意分布分析 | "统计游戏行业创意类型分布" | 创意类型分布数据 | distribute, distribute-dims |
| 开发者调研 | "查询某开发者旗下所有应用" | 应用列表+开发者详情 | company-search, developer-detail |

**不适用于**：H5/落地页/仪表盘生成、托管式深度研究、自主多步研究、数据分析/推荐（除非用户在收到数据后明确要求）

## 使用流程

### Step 1：检查 API Key（永不打印值）
```bash
[ -n "${ADMAPIX_API_KEY:-}" ] && echo ok || echo missing
```

### Step 2：缺失时引导配置
> 需要先配置 AdMapix API Key：
> 1. 访问 https://www.admapix.com 注册并登录
> 2. 在控制台 **API Keys** 创建 Key
> 3. 终端环境变量：`export ADMAPIX_API_KEY="你的Key"`
> 4. 配置完成后重新发起查询

**安全红线**：永不接受/回显/存储来自聊天输入的 Key；永不将 Key 写入日志或链接参数.
### Step 3：首次调用前拉取元数据
```bash
# 获取全量筛选元数据（国家码、行业码、创意类型码等）
curl -s "https://api.admapix.com/api/data/filter-options" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}"
```

### Step 4：按需调用端点，透传原始 JSON
- 每次请求调用单个端点，返回原始结构化 JSON
- 空 `list` 是合法结果，非错误
- `page_size` 上限 10 自动钳制，翻页用 `page` 参数

### Step 5：估算数据声明
下载/收入端点返回的数据，调用方 Agent 展示时须注明："本数据为第三方估算，非官方披露".
#
## 案例展示

### 案例1：竞品创意搜索与详情
**场景**：广告投放团队需要搜索美国地区游戏类视频广告创意并查看详情

```bash
# Step 1: 搜索创意
curl -s -X POST "https://api.admapix.com/api/data/search" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" \
  -d '{"keyword":"rpg","countries":["US"],"trade_level1":["602"],"adTypes":["010"],"page":1,"page_size":10}'
# ...
# Step 2: 查看某条创意详情
curl -s "https://api.admapix.com/api/data/content-detail?id=ad_001&related=imagevideo" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}"
# ...
# Step 3: 查看该创意关联的应用
curl -s -X POST "https://api.admapix.com/api/data/item-apps" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" \
  -d '{"creativeIds":["ad_001"]}'
```

**输出**：
```json
{
  "pageIndex": 1,
  "pageSize": 10,
  "totalSize": 234,
  "list": [
    {"id": "ad_001", "url": "https://...", "first_seen": "2026-07-15", "type": "video", "duration": 30}
  ]
}
```

**分析**：共找到 234 条匹配创意，当前返回前 10 条。`content-detail` 可查看创意素材详情，`item-apps` 可反查该创意关联的投放应用.
### 案例2：商店榜单与下载收入对比
**场景**：出海团队需要查询日本免费榜前 20 名应用的下载与收入估算

```bash
# Step 1: 查询商店类目代码
curl -s "https://api.admapix.com/api/data/store-categories" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}"
# ...
# Step 2: 查询日本免费榜
curl -s -X POST "https://api.admapix.com/api/data/store-rank" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" \
  -d '{"countries":["JP"],"rankType":"free","category":"games","page":1,"page_size":20}'
# ...
# Step 3: 查询Top1应用的下载估算
curl -s -X POST "https://api.admapix.com/api/data/download-country" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" \
  -d '{"unifiedProductId":"app_001","countries":["JP"],"dateRange":"30d"}'
# ...
# Step 4: 查询Top1应用的收入估算
curl -s -X POST "https://api.admapix.com/api/data/revenue-country" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" \
  -d '{"unifiedProductId":"app_001","countries":["JP"],"dateRange":"30d"}'
```

**输出**：日本免费榜前 20 名列表 + Top1 应用的下载/收入估算数据（第三方估算）

### 案例3：开发者画像与 SDK 审计
**场景**：调研团队需要查询某开发者旗下所有应用的 SDK 使用情况

```bash
# Step 1: 搜索开发者
curl -s -X POST "https://api.admapix.com/api/data/company-search" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" \
  -d '{"keyword":"开发者名称","page":1,"page_size":10}'
# ...
# Step 2: 查询开发者详情（含旗下应用列表）
curl -s "https://api.admapix.com/api/data/developer-detail?developerId=dev_001" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}"
# ...
# Step 3: 查询每个应用的SDK（并行）
curl -s "https://api.admapix.com/api/data/sdk-detail?unifiedProductId=app_001" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}"
curl -s "https://api.admapix.com/api/data/sdk-detail?unifiedProductId=app_002" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}"
# ...
# Step 4: 查询相似应用
curl -s -X POST "https://api.admapix.com/api/data/similar-apps" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" \
  -d '{"unifiedProductId":"app_001","page":1,"page_size":10}'
```

**输出**：开发者详情 + 旗下应用列表 + 每个应用的 SDK 列表 + 相似应用推荐

## 错误处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|---:|---:|---:|---:|
| missing_api_key | `{"error":{"code":"missing_api_key"}}` | 环境变量 `ADMAPIX_API_KEY` 未设置 | 不调 API，引导用户配置 Key；永不打印 Key |
| 401 INVALID_API_KEY | `{"detail":"...","code":"INVALID_API_KEY"}` | Key 格式错误或已禁用 | 引导用户检查 Key 格式 |
| 401 NOT_AUTHENTICATED | `{"code":"NOT_AUTHENTICATED"}` | Key 缺失或认证失败 | 引导用户重新配置 Key |
| 403 FORBIDDEN | `{"code":"FORBIDDEN"}` | 套餐权限不足，端点不在套餐范围内 | 提示用户升级 AdMapix 套餐 |
| 429 RATE_LIMITED | `{"code":"RATE_LIMITED"}` | API 调用频率超限 | （1s/2s/4s），最多 3 次 |
| 400 INVALID_PARAM | `{"code":"INVALID_PARAM"}` | 国家/行业/创意类型码错误 | 调 `filter-options` 核对参数代码 |
| 5xx INTERNAL | HTTP 500/502/503 | AdMapix 服务端错误 | 最多 2 次 |
| 空 list 返回 | `{"list":[],"totalSize":null}` | 参数无匹配或代码错误 | 空列表是合法结果；调 `filter-options` 核对代码 |
| content-detail 404 | `{"code":"NOT_FOUND"}` | 创意已下线或 ID 无效 | 跳过该 ID，记录到失败列表 |

## 常见问题

### Q1：`page_size=50` 为什么只返回了 10 条？
A：创意 `search` 端点 `page_size` 硬上限为 10，任何更大的值会被自动钳制到 10。翻页请用 `page` 参数递增（page=1, 2, 3...）。其他列表端点使用各自文档中的范围.
### Q2：下载/收入数据和官方财报对不上？
A：下载/收入为第三方**估算值**，非官方披露数据。长尾地区偏差可达 30%+。API 原样返回数字，调用方 Agent 展示时须注明"本数据为第三方估算，非官方披露".
### Q3：`totalSize` 为什么是 null？
A：过滤查询时 `totalSize` 可能为 null。此时以 `list` 长度为准，或单独调 `count` 端点获取准确总数。MCP 工具返回会额外包装 `page` / `page_size` 字段.
### Q4：如何获取有效的国家码和行业码？
A：调 `GET /api/data/filter-options` 获取全量筛选元数据，包含 `countries`、`mediaChannels`、`adTypes`、`device`、`tradeLevel(Tree)`、`productModel` 等全部维度。商店类目调 `store-categories`，商店国家调 `store-countries`.
### Q5：创意搜索和产品创意搜索有什么区别？
A：`/api/data/search` 按关键词、国家、行业等条件全局搜索广告创意；`/api/data/product-content-search` 针对特定产品（需 `unifiedProductId`）搜索其关联创意。如需先找到产品 ID，用 `unified-product-search` 或 `product-search`.
### Q6：能否一次请求查多个国家的数据？
A：`search` / `distribute` / `download-country` 等端点支持 `countries` 数组，但结果会合并。如需分别对比各国数据，请并行发多个单国家请求.
## 已知限制

1. **薄客户端**：仅透传原始结构化 JSON，不分析、不总结、不排序、不生成页面。多端点编排与分析由调用方 Agent 完成
2. **单次请求单端点**：每次 API 调用仅请求一个端点，不内置批量端点聚合
3. **估算数据非官方**：下载/收入均为第三方估算，长尾地区偏差可达 30%+，不可作为财务依据
4. **`page_size` 硬上限 10**：创意搜索翻页 100 条需 10 次请求，其他端点使用各自范围
5. **不做分析与推荐**：仅透传结构化数据，不生成 H5/仪表盘/深度研究报告，分析与推荐需用户明确要求后另起
