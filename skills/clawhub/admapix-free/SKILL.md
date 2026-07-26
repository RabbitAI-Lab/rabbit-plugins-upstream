---
slug: "admapix-free"
name: "admapix-free"
version: "1.0.0"
displayName: "AdMapix LITE"
summary: "AdMapix基础查询，创意搜索+应用详情+商店榜单"
license: "MIT"
description: |-
  AdMapix 原始数据层基础客户端（免费版）。覆盖广告创意搜索、应用详情查询、商店榜单查询三大基础端点类别.
  作为薄客户端透传 API 返回的原始结构化 JSON，不分析、不总结、不排序、不生成页面.
  支持 X-API-Key 认证、page_size 上限 10 自动钳制、filter-options 元数据发现.
  适用于广告创意搜索、应用信息查询、商店榜单查看等基础场景.
tags:
  - 研发工具
  - Research
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# AdMapix LITE

AdMapix 原始 API 基础客户端（免费版）。获取原始结构化数据并返回 JSON，不分析、不总结、不排序、不生成页面.
## 依赖说明

### 运行环境
- **Agent 平台**: 支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **网络**: 需可访问 `https://api.admapix.com`

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---|---|----|----|
| AdMapix API | 远程 HTTP API | 必需 | https://www.admapix.com 注册获取 |
| ADMAPIX_API_KEY | 环境变量 | 必需 | 控制台 API Keys 创建；仅作 `X-API-Key` 请求头 |
| curl 或等价 HTTP 客户端 | 命令行工具 | 必需 | 系统自带或包管理器安装 |

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令驱动，需 exec 执行 curl 命令）
- **说明**: 基于自然语言指令驱动 Agent 调用 AdMapix API，透传原始结构化 JSON

## 核心能力

### 参数映射

阅读 `references/param-mappings.md` 将自然语言翻译为代码：

- 创意类型（`010`=视频等）、行业（`trade_level1`：`602`=游戏，`607`=金融...）、国家/地区分组、相对日期范围
- 未列出的代码调 `GET /api/data/filter-options` 获取

对于创意 `search` 端点，`page_size` 上限为 **

**处理**: 解析参数映射的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回参数映射的处理结果,包含执行状态码、结果数据和执行日志.
### 输出规则

返回 API 响应的**原始结构化 JSON** — 保留 API 字段名；不重命名、不丢弃、不总结、不排序。调用方 Agent 负责分析.
- 创意搜索返回 `pageIndex` / `pageSize` / `totalSize` / `list`。`totalSize` 在过滤查询时可能为 `null` — 此时以 `list` 长度为准.
- 空 `list` 是合法结果（无匹配），非

**输入**: 用户提供输出规则相关的配置参数、输入数据和处理选项.
#
## 认证

使用 `ADMAPIX_API_KEY` 作为 `X-API-Key` 请求头。永不打印或暴露 Key.
```bash
curl -s "https://api.admapix.com/api/data/{endpoint}?{params}" -H "X-API-Key: ${ADMAPIX_API_KEY}"
curl -s -X POST "https://api.admapix.com/api/data/{endpoint}" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" -d '{...}'
```

## 端点目录（基础端点）

### 创意 / 广告

| 端点 | 方法 | 用途 |
|:-----|:-----|:-----|
| `/api/data/search` | POST | 搜索广告创意 |
| `/api/data/count` | POST | 按条件统计创意数量 |
| `/api/data/filter-options` | GET | 全量筛选元数据（国家码、行业码、创意类型码等） |

### 应用 / 产品

| 端点(续)| 方法 | 用途 |
|---:|---:|---:|
| `/api/data/unified-product-search` | POST | 统一应用/产品搜索 |
| `/api/data/app-detail` | GET | 按 `unifiedProductId` 查应用详情 |

### 榜单

| 端点(续)(续)| 方法 | 用途 |
|:-------:|:-------:|:-------:|
| `/api/data/store-rank` | POST | 应用商店榜单（免费/付费/畅销） |
| `/api/data/store-categories` | GET | 商店类目代码 |

> **升级提示**：创意分布查询、创意详情、SDK 审计、开发者画像、下载/收入估算、应用分发、市场级搜索等高级端点仅在 [admapix 付费版](#) 中提供.
## 参数映射(补充)

对于创意 `search` 端点，`page_size` 上限为 **10**（更大的值自动钳制到 10；用 `page` 翻页）.
## 输出规则(补充)

- 创意搜索返回 `pageIndex` / `pageSize` / `totalSize` / `list`。`totalSize` 在过滤查询时可能为 `null` — 此时以 `list` 长度为准.
- 空 `list` 是合法结果（无匹配），非错误.
## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及端点 |
|:------|------:|:------|:------|
| 竞品创意搜索 | "搜索美国游戏类视频广告" | 创意列表（ID、URL、首次出现时间） | search |
| 应用信息查询 | "查询某应用的详细信息" | 应用名称、开发者、分类等详情 | unified-product-search, app-detail |
| 商店榜单查看 | "查询日本免费榜前20" | 应用排名列表 | store-rank |

**不适用于**：下载/收入估算、创意分布分析、SDK 审计、开发者画像、应用分发（需升级付费版）

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

**安全红线**：永不接受/回显/存储来自聊天输入的 Key；Key 仅作为 `X-API-Key` 请求头使用.
### Step 3：首次调用前拉取元数据
```bash
curl -s "https://api.admapix.com/api/data/filter-options" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}"
```

### Step 4：按需调用端点，透传原始 JSON
- 每次请求调用单个端点，返回原始结构化 JSON
- 空 `list` 是合法结果，非错误
- `page_size` 上限 10 自动钳制，翻页用 `page` 参数

#
## 案例展示

### 案例1：竞品创意搜索
**场景**：广告投放团队需要搜索美国地区游戏类视频广告创意

```bash
# 搜索美国地区游戏类视频广告创意
curl -s -X POST "https://api.admapix.com/api/data/search" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" \
  -d '{"keyword":"rpg","countries":["US"],"trade_level1":["602"],"adTypes":["010"],"page":1,"page_size":10}'
```

**输出**：
```json
{
  "pageIndex": 1,
  "pageSize": 10,
  "totalSize": 234,
  "list": [
    {"id": "ad_001", "url": "https://...", "first_seen": "2026-07-15", "type": "video", "duration": 30},
    {"id": "ad_002", "url": "https://...", "first_seen": "2026-07-16", "type": "video", "duration": 15}
  ]
}
```

**分析**：共找到 234 条匹配创意，当前返回前 10 条。翻页请用 `page` 参数递增.
### 案例2：商店榜单查询
**场景**：出海团队需要查询日本免费榜前 20 名应用

```bash
# 查询日本免费游戏榜
curl -s -X POST "https://api.admapix.com/api/data/store-rank" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" \
  -d '{"countries":["JP"],"rankType":"free","category":"games","page":1,"page_size":20}'
```

**输出**：
```json
{
  "list": [
    {"rank": 1, "appName": "示例应用A", "unifiedProductId": "app_001", "developer": "Dev A"},
    {"rank": 2, "appName": "示例应用B", "unifiedProductId": "app_002", "developer": "Dev B"}
  ]
}
```

## 错误处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|---:|:---|---:|---:|
| missing_api_key | `{"error":{"code":"missing_api_key"}}` | 环境变量 `ADMAPIX_API_KEY` 未设置 | 不调 API，引导用户配置 Key；永不打印 Key |
| 401 INVALID_API_KEY | `{"code":"INVALID_API_KEY"}` | Key 格式错误或已禁用 | 检查网络连接和配置后重试，引导用户检查 Key 格式 |
| 403 FORBIDDEN | `{"code":"FORBIDDEN"}` | 套餐权限不足，端点不在套餐范围内 | 检查网络连接和配置后重试，提示用户升级 AdMapix 套餐 |
| 429 RATE_LIMITED | `{"code":"RATE_LIMITED"}` | API 调用频率超限 | 等待 1 秒后检查网络连接和配置后重试，最多 3 次 |
| 400 INVALID_PARAM | `{"code":"INVALID_PARAM"}` | 国家/行业/创意类型码错误 | 检查网络连接和配置后重试，调 `filter-options` 核对参数代码 |
| 空 list 返回 | `{"list":[],"totalSize":null}` | 参数无匹配或代码错误 | 空列表是合法结果；调 `filter-options` 核对代码 |

## 常见问题

### Q1：`page_size=50` 为什么只返回了 10 条？
A：创意 `search` 端点 `page_size` 硬上限为 10，任何更大的值会被自动钳制到 10。翻页请用 `page` 参数递增（page=1, 2, 3...）.
### Q2：`totalSize` 为什么是 null？
A：过滤查询时 `totalSize` 可能为 null。此时以 `list` 长度为准，或单独调 `count` 端点获取准确总数.
### Q3：免费版和付费版有什么区别？
A：免费版（LITE）包含创意搜索、应用详情查询、商店榜单查询三大基础端点。付费版（AdMapix）额外提供：
- 创意分布查询（distribute / distribute-dims）与创意详情（content-detail）
- 开发者画像（company-search / developer-detail）与 SDK 审计（sdk-detail）
- 下载与收入估算（download-date / revenue-country 等 6 个端点）
- 应用分发（app-distribution / global-promote）与市场级搜索（market-search）
- 3 个完整案例（vs 免费版 2 个基础案例）
- 9 种错误处理（vs 免费版 6 种）

### Q4：如何获取有效的国家码和行业码？
A：调 `GET /api/data/filter-options` 获取全量筛选元数据，包含 `countries`、`mediaChannels`、`adTypes`、`tradeLevel(Tree)` 等全部维度。商店类目调 `store-categories`.
## 已知限制

1. **基础端点**：仅支持创意搜索、应用详情、商店榜单，不支持下载/收入估算、创意分布、SDK 审计、开发者画像（需升级付费版）
2. **薄客户端**：仅透传原始结构化 JSON，不分析、不总结、不排序
3. **单次请求单端点**：每次 API 调用仅请求一个端点
4. **`page_size` 硬上限 10**：创意搜索翻页 100 条需 10 次请求
5. **不做分析与推荐**：仅透传结构化数据，不生成分析报告
