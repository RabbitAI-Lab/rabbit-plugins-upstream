---
slug: "ad-insight-hub-free"
name: "ad-insight-hub-free"
version: "1.0.0"
displayName: "广告洞察中枢LITE"
summary: "AdMapix广告情报API基础查询，参数翻译+创意搜索+应用画像"
license: "MIT"
description: |-
  面向广告投放场景的广告情报数据查询工具（免费版）。在AdMapix原始API之上提供参数自然语言翻译与
  基础创意搜索能力。支持广告创意搜索/计数、应用与开发者画像查询两大基础能力域.
  内置高频行业码与国家码中文映射，支持单端点查询与基础参数翻译.
  适用于买量团队竞品创意监控、应用信息查询等基础场景.
tags:
  - 广告情报
  - 数据API
  - 信息检索
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# 广告洞察中枢 LITE（Ad Insight Hub Free）

面向广告投放场景的广告情报数据查询工具（免费版）。提供参数翻译与基础创意搜索能力.
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
- **说明**: 基于自然语言指令驱动 Agent 调用 AdMapix API，透传结构化 JSON

## 核心能力

### 1. 广告创意搜索/计数
按关键词、国家、行业、创意类型多维度检索广告创意。`page_size` 上限 10 自动钳制。支持创意搜索（`search`）与计数（`count`）.
**输入**: 用户提供广告创意搜索/计数所需的指令和必要参数.
**输出**: 返回广告创意搜索/计数的处理结果,包含执行状态码、结果数据和执行日志.
### 2. 应用与开发者画像
统一产品搜索（`unified-product-search`）、应用详情（`app-detail`）、开发者详情（`developer-detail`）.
> **升级提示**：创意分布查询、商店榜单、下载/收入估算（带可信度分级）、端点依赖编排、结果缓存复用等高级功能仅在 [ad-insight-hub 付费版](#) 中提供.
#
## 参数映射表

### 高频行业码（trade_level1）
| 自然语言 | 代码 | 自然语言 | 代码 |
|:-----|:-----|:-----|:-----|
| 游戏 | 602 | 金融 | 607 |
| 电商 | 601 | 工具 | 603 |
| 社交 | 604 | 娱乐 | 609 |

### 高频国家码
| 高频国家 | 代码 | 自然语言 | 代码 |
|---:|---:|---:|---:|
| 美国 | US | 日本 | JP |
| 韩国 | KR | 德国 | DE |
| 视频(创意类型) | 010 | - | - |

未列出的参数请调 `GET /api/data/filter-options` 获取最新码表.
## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及能力 |
|:---:|:---:|:---:|:---:|
| 竞品创意搜索 | "搜索美国地区游戏类视频广告创意" | 创意列表（ID、URL、首次出现时间） | 创意搜索 |
| 应用信息查询 | "查询某应用的详细信息" | 应用名称、开发者、分类等详情 | 应用画像 |
| 创意数量统计 | "统计某行业近7天的创意数量" | 创意总数 | 创意计数 |

**不适用于**：下载/收入估算查询、商店榜单查询、创意分布分析、端点依赖编排（需升级付费版）

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
### Step 3：解析用户意图，翻译为 API 参数
将自然语言中的行业、国家、创意类型等翻译为 API 代码。未列出的参数调 `GET /api/data/filter-options` 获取.
### Step 4：透传结果
- 原始结构化 JSON 透传，不重命名、不丢弃、不总结
- 空列表是合法结果（无匹配），非错误

#
## 案例展示

### 案例1：竞品创意搜索
**场景**：买量团队需要搜索美国地区游戏类视频广告创意

```bash
# 搜索美国地区游戏类视频广告创意
curl -s -X POST "https://api.admapix.com/api/data/search" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" \
  -d '{"keyword":"puzzle","countries":["US"],"trade_level1":["602"],"adTypes":["010"],"page":1,"page_size":10}'
```

**输出**：
```json
{
  "pageIndex": 1,
  "pageSize": 10,
  "totalSize": 156,
  "list": [
    {"id": "ad_001", "url": "https://...", "first_seen": "2026-07-15", "type": "video"},
    {"id": "ad_002", "url": "https://...", "first_seen": "2026-07-16", "type": "video"}
  ]
}
```

**分析**：共找到 156 条匹配创意，当前返回前 10 条。翻页请用 `page` 参数递增.
### 案例2：应用信息查询
**场景**：开发者需要查询某应用的详细信息

```bash
# 先搜索应用获取 unifiedProductId
curl -s -X POST "https://api.admapix.com/api/data/unified-product-search" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" \
  -d '{"keyword":"应用名称","page":1,"page_size":10}'
# ...
# 再查应用详情
curl -s "https://api.admapix.com/api/data/app-detail?unifiedProductId=xxx" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}"
```

**输出**：
```json
{
  "unifiedProductId": "app_001",
  "name": "示例应用",
  "developer": "示例开发者",
  "category": "Games",
  "countries": ["US", "JP"]
}
```

## 错误处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:------|------:|:------|:------|
| 401 INVALID_API_KEY | `{"code":"INVALID_API_KEY"}` | Key 缺失/格式错/已禁用 | 检查网络连接和配置后重试，引导用户检查 Key；永不打印 Key |
| 403 FORBIDDEN | `{"code":"FORBIDDEN"}` | 权限不足或套餐限制 | 检查网络连接和配置后重试，提示用户升级 AdMapix 套餐 |
| 429 RATE_LIMITED | `{"code":"RATE_LIMITED"}` | 触发限流 | 等待 1 秒后检查网络连接和配置后重试，最多 3 次 |
| 400 INVALID_PARAM | `{"code":"INVALID_PARAM"}` | 国家/行业码错误 | 检查网络连接和配置后重试，对照 `filter-options` 检查参数代码 |
| 一直返回空 list | `{"list":[]}` | 参数代码错误或无匹配 | 调 `filter-options` 核对国家/行业码 |
| 详情接口 404 | `{"code":"NOT_FOUND"}` | 创意已下线或应用 ID 不存在 | 跳过该 ID，记录到失败列表 |

## 常见问题

### Q1：为什么我的 `page_size=50` 被改成了 10？
A：创意搜索端点强制上限 10，本技能自动钳制。翻页请用 `page` 参数递增.
### Q2：`totalSize` 为什么是 null？
A：过滤查询时 `totalSize` 可能为 null，此时以 `list` 长度为准，或单独调 `count` 端点获取准确总数.
### Q3：免费版和付费版有什么区别？
A：免费版（LITE）包含创意搜索/计数和应用画像查询两大基础功能。付费版（广告洞察中枢）额外提供：
- 创意分布查询（distribute / distribute-dims）
- 商店榜单查询（store-rank / generic-rank）
- 下载与收入估算（带 A/B/C 可信度分级）
- 端点依赖编排（自动并行/串行调度，单轮 5-10 个端点）
- 结果缓存复用（元数据 24h、搜索 1h、详情 7d）
- 3 个完整案例（vs 免费版 2 个基础案例）
- 9 种错误处理（vs 免费版 6 种）

### Q4：如何获取完整的行业码和国家码？
A：调 `GET /api/data/filter-options` 获取最新码表，包含 `countries`、`mediaChannels`、`adTypes`、`tradeLevel(Tree)` 等全部筛选维度.
## 已知限制

1. **基础功能**：仅支持创意搜索/计数和应用画像，不支持下载/收入估算、商店榜单、创意分布（需升级付费版）
2. **无端点编排**：不支持自动并行/串行编排，需手动逐个调用（付费版支持单轮编排 5-10 个端点）
3. **无缓存**：每次查询均发起 API 请求，不缓存结果（付费版支持多级缓存策略）
4. **`page_size` 硬上限 10**：翻页 100 条需 10 次请求
5. **不做分析与推荐**：仅透传结构化数据，不生成分析报告
