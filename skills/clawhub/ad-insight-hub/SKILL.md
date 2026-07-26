---
slug: "ad-insight-hub"
name: "ad-insight-hub"
version: 1.0.1
displayName: "广告洞察中枢"
summary: "聚合AdMapix广告情报API，参数翻译/端点编排/缓存/可信度标注四层能力"
license: "Proprietary"
description: |-
  面向广告投放与市场分析场景的结构化广告情报数据中枢。在AdMapix原始API之上叠加参数自然语言翻译、
  端点依赖编排、结果缓存复用、估算数据可信度A/B/C分级标注四层核心能力。支持广告创意搜索/计数/分布、
  应用与开发者画像、商店榜单查询、下载与收入估算（带可信度分级）、参数翻译与端点编排五大能力域.
  适用于买量团队竞品创意监控、出海选品调研、广告素材趋势分析、开发者画像与SDK审计、跨地区投放策略制定.
  内置40+行业码与200+国家码中文映射，端点依赖图自动并行化无依赖调用、串行化有依赖调用，单轮可编排5-10个端点.
tags:
  - 广告情报
  - 数据API
  - 市场分析
  - 信息检索
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# 广告洞察中枢（Ad Insight Hub）

面向广告投放与市场分析场景的结构化广告情报数据中枢。在原始 API 之上叠加参数翻译、依赖编排、缓存复用、可信度标注四层能力，让 Agent 用最少的往返拿到最可用的数据.
## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
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
- **说明**: 基于自然语言指令驱动 Agent 调用 AdMapix API，透传结构化 JSON

### 缓存策略
| 数据类型 | 缓存时长 | 缓存位置 |
|---:|---:|---:|
| 元数据（filter-options 等） | 24 小时 | `~/.admapix-cache/metadata/` |
| 创意搜索结果 | 1 小时 | `~/.admapix-cache/search/` |
| 创意详情 | 7 天 | `~/.admapix-cache/detail/` |
| 下载/收入估算 | 1 天 | `~/.admapix-cache/estimate/` |
| 榜单数据 | 6 小时 | `~/.admapix-cache/rank/` |

## 核心能力

### 1. 广告创意搜索/计数/分布
按关键词、国家、行业、创意类型多维度检索广告创意。`page_size` 上限 10 自动钳制；配额紧张时优先用 `count` 替代 `search` 降低消耗。支持创意分布维度查询（`distribute` / `distribute-dims`）与创意关联应用反查（`item-apps`）.
**输入**: 用户提供广告创意搜索/计数/分布所需的指令和必要参数.
**处理**: 解析广告创意搜索/计数/分布的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回广告创意搜索/计数/分布的处理结果,包含执行状态码、结果数据和执行日志.
### 2. 应用与开发者画像
统一产品搜索（`unified-product-search`）、应用详情（`app-detail`）、开发者详情（`developer-detail`）、相似应用（`similar-apps`）、SDK 详情（`sdk-detail`）；支持从创意 ID 反查关联应用（`item-apps`）。- 验证返回数据的完整性和格式正确性
### 3. 商店榜单查询
应用商店免费/付费/畅销榜单（`store-rank`），按类目与国家筛选；通用榜单（`generic-rank`）支持自定义维度聚合.
**输入**: 用户提供商店榜单查询所需的指令和必要参数.
**处理**: 解析商店榜单查询的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回商店榜单查询的处理结果,包含执行状态码、结果数据和执行日志.
### 4. 下载与收入估算（带可信度分级）
按日期（`download-date` / `revenue-date`）、详情（`download-detail` / `revenue-detail`）、国家（`download-country` / `revenue-country`）维度查询第三方估算数据；强制附 A/B/C 三级可信度标注：
- **A 级**：多源交叉方差 < 10%，可用于定量对比
- **B 级**：单源方差 10%-25%，可用于趋势参考
- **C 级**：长尾方差 > 25%，仅用于方向性判断

**输入**: 用户提供下载与收入估算（带可信度分级）所需的指令和必要参数.
**处理**: 解析下载与收入估算（带可信度分级）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回下载与收入估算（带可信度分级）的处理结果,包含执行状态码、结果数据和执行日志.
### 5. 参数自然语言翻译与端点编排
内置 40+ 行业码与 200+ 国家码中文映射；端点依赖图自动并行化无依赖调用、串行化有依赖调用，单轮可编排 5-10 个端点.
**输入**: 用户提供参数自然语言翻译与端点编排所需的指令和必要参数.
**输出**: 返回参数自然语言翻译与端点编排的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`参数自然语言翻译与端点编排`的配置文档进行参数调优
#
## 参数映射表

### 行业码（trade_level1）
| 自然语言 | 代码 | 自然语言 | 代码 |
|:---:|:---:|:---:|:---:|
| 游戏 | 602 | 金融 | 607 |
| 电商 | 601 | 工具 | 603 |
| 社交 | 604 | 娱乐 | 609 |

### 国家/地区码
| 国家/地 | 代码 | 自然语言 | 代码 |
|:------|------:|:------|:------|
| 美国 | US | 日本 | JP |
| 韩国 | KR | 德国 | DE |
| 东南亚 | TH/VN/ID/PH/MY | 中东 | SA/AE/TR/EG |
| 拉美 | BR/MX/AR/CO | 视频(创意类型) | 010 |

未列出的参数请调 `GET /api/data/filter-options` 获取最新码表.
## 端点依赖编排

```text
独立可并行（首轮一次性发出）：
  filter-options / distribute-dims / screen-types / page-config
  search / count / count-all / distribute
  market-search / unified-product-search / company-search
# ...
依赖前序结果（必须串行）：
  content-detail    ← 依赖 search 返回的创意 ID
  item-apps         ← 依赖 search 返回的创意 ID
  app-detail        ← 依赖 unified-product-search 或 item-apps 返回的 unifiedProductId
  developer-detail  ← 依赖 app-detail 返回的开发者 ID
  similar-apps / sdk-detail ← 依赖 app-detail
```

**编排规则**：
1. 首轮：把所有无依赖查询一次性并行发出（建议 5-8 个并发）
2. 解析首轮结果，提取 ID
3. 第二轮：基于 ID 的详情查询并行发出
4. 配额紧张时：用 `count` 替代 `search`，用 `count-all` 替代多次 `distribute`

## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及能力 |
|---:|:---|---:|---:|
| 竞品创意监控 | "监控某竞品最近7天在美国的视频创意变化" | 新增创意列表、素材分布变化 | 创意搜索+计数 |
| 出海选品调研 | "对比美国和东南亚三消类游戏的下载与收入" | 多国下载/收入对比表+可信度分级 | 下载/收入估算 |
| 素材趋势分析 | "统计游戏行业近30天创意类型分布" | 创意类型分布饼图数据 | 创意分布 |
| 开发者画像 | "调研某开发者旗下所有应用的SDK使用情况" | SDK矩阵表+供应链风险提示 | 应用画像+SDK |
| 跨地区投放策略 | "查询美国和日韩地区金融类应用的榜单" | 多国榜单对比表 | 商店榜单 |

**不适用于**：H5/落地页/卡片/仪表盘生成、托管式深度研究与自主多步研究、数据分析/推荐（除非用户在收到数据后明确要求）

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

**安全红线**：永不接受/回显/存储来自聊天输入的 Key；永不将 Key 写入日志或链接参数；Key 仅作为 `X-API-Key` 请求头使用.
### Step 3：解析用户意图，翻译为 API 参数
将自然语言中的行业、国家、创意类型等翻译为 API 代码。未列出的参数调 `GET /api/data/filter-options` 获取.
### Step 4：按依赖图编排端点
首轮并行发出无依赖查询，提取 ID 后第二轮并行发出详情查询。配额紧张时切换为 `count` 计数模式.
### Step 5：透传结果并标注可信度
- 原始结构化 JSON 透传，不重命名、不丢弃、不总结、不排序、不评论
- 空列表是合法结果（无匹配），非错误
- 估算数据必须附："本数据为第三方估算，可能存在 10%-30% 偏差，仅供参考" + 可信度分级

#
## 案例展示

### 案例1：竞品创意监控
**场景**：买量团队需要监控某竞品最近 7 天在美国的视频创意变化

**编排**：
1. `POST /api/data/product-search` → 拿到竞品 `unifiedProductId`
2. `POST /api/data/product-content-search`（filter: 7d, US, video=010）
3. `POST /api/data/product-content-counts`（同条件）→ 拿到总量
4. 对比上次缓存的创意 ID 列表，仅对新增项调 `content-detail`

```bash
# Step 1: 搜索竞品产品
curl -s -X POST "https://api.admapix.com/api/data/product-search" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" \
  -d '{"keyword":"竞品名称","page":1,"page_size":10}'
# ...
# Step 2: 查询近7天美国视频创意
curl -s -X POST "https://api.admapix.com/api/data/product-content-search" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" \
  -d '{"unifiedProductId":"xxx","countries":["US"],"adTypes":["010"],"dateRange":"7d","page":1,"page_size":10}'
```

**输出**：
```json
{
  "new_creatives_count": 12,
  "creatives": [
    {"id": "ad_001", "url": "https://...", "first_seen": "2026-07-15", "type": "video"},
    {"id": "ad_002", "url": "https://...", "first_seen": "2026-07-16", "type": "video"}
  ],
  "distribution_change": {"video": "+8", "image": "+4"}
}
```

**分析**：7 天内新增 12 条视频创意，视频类创意增长 8 条，图片类增长 4 条，竞品正在加大视频素材投放力度.
### 案例2：跨地区选品对比
**场景**：出海团队需要对比美国和东南亚三消类游戏的下载与收入

**编排（首轮 4 个请求并行）**：
```bash
# 美国下载估算
curl -s -X POST "https://api.admapix.com/api/data/download-country" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" \
  -d '{"countries":["US"],"trade_level1":["602"],"genre":["match3"],"dateRange":"30d"}'
# ...
# 东南亚下载估算（多国合并）
curl -s -X POST "https://api.admapix.com/api/data/download-country" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" \
  -d '{"countries":["TH","VN","ID","PH","MY"],"trade_level1":["602"],"genre":["match3"],"dateRange":"30d"}'
# ...
# 美国收入估算
curl -s -X POST "https://api.admapix.com/api/data/revenue-country" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" \
  -d '{"countries":["US"],"trade_level1":["602"],"genre":["match3"],"dateRange":"30d"}'
# ...
# 东南亚收入估算
curl -s -X POST "https://api.admapix.com/api/data/revenue-country" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" \
  -d '{"countries":["TH","VN","ID","PH","MY"],"trade_level1":["602"],"genre":["match3"],"dateRange":"30d"}'
```

**输出**：表格对比，每行附可信度分级

| 地区 | 月下载量 | 月收入 | 可信度 |
|:------:|--------|:-------|:------:|
| 美国 | 12,500,000 | $3,200,000 | A 级（多源交叉方差 < 10%） |
| 东南亚 | 8,700,000 | $680,000 | C 级（长尾方差 > 25%） |

**分析**：美国市场下载量与收入均显著高于东南亚，ARPU 差距约 5 倍。东南亚数据为 C 级可信度，仅用于趋势判断.
### 案例3：开发者画像与 SDK 审计
**场景**：投资调研团队需要调研某开发者旗下所有应用的 SDK 使用情况

**编排**：
1. `POST /api/data/company-search` → 拿到开发者 ID
2. `GET /api/data/developer-detail` → 拿到旗下应用列表
3. （并行）对每个应用 `GET /api/data/sdk-detail`
4. 聚合：SDK 使用频次、共享 SDK、独家 SDK

```bash
# Step 1: 搜索开发者
curl -s -X POST "https://api.admapix.com/api/data/company-search" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" -H "Content-Type: application/json" \
  -d '{"keyword":"开发者名称","page":1,"page_size":10}'
# ...
# Step 3: 并行查询每个应用的SDK（示例）
curl -s "https://api.admapix.com/api/data/sdk-detail?unifiedProductId=app_001" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}"
```

**输出**：SDK 矩阵表（应用 x SDK）+ 供应链风险提示

| 应用 | Firebase | AppsFlyer | Unity Ads | 独家SDK |
|----|:--:|---:|----|:--:|
| App A | Yes | Yes | Yes | IRONSOURCE |
| App B | Yes | Yes | No | - |
| App C | Yes | No | Yes | CHARTBOOST |

**分析**：Firebase 被 3 个应用共享，若下线影响范围最广；App C 未集成 AppsFlyer，归因数据可能不完整.
## 错误处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|----|----|----|----|
| 401 INVALID_API_KEY | `{"code":"INVALID_API_KEY"}` | Key 缺失/格式错/已禁用 | 引导用户检查 Key；永不打印 Key |
| 403 FORBIDDEN | `{"code":"FORBIDDEN"}` | 权限不足或套餐限制 | 提示用户升级 AdMapix 套餐 |
| 429 RATE_LIMITED | `{"code":"RATE_LIMITED"}` | 触发限流 | （1s/2s/4s），最多 3 次；降低并发到 3 |
| 400 INVALID_PARAM | `{"code":"INVALID_PARAM"}` | 国家/行业码错误 | 对照 `filter-options` 检查参数代码 |
| 5xx INTERNAL | HTTP 500/502/503 | AdMapix 服务端错误 | 最多 2 次 |
| 一直返回空 list | `{"list":[]}` | 参数代码错误或无匹配 | 调 `filter-options` 核对国家/行业码；空列表是合法结果 |
| 详情接口 404 | `{"code":"NOT_FOUND"}` | 创意已下线 | 跳过该 ID，记录到失败列表 |
| 估算数据明显异常 | 下载数为 0 或负数 | 长尾地区样本稀疏 | 标注 C 级可信度，仅供方向性参考 |
| 配额剩余 < 10% | `{"quota_remaining":<10}` | 接近调用上限 | 切换为 `count` 计数模式，元数据查询命中本地缓存 |

## 常见问题

### Q1：为什么我的 `page_size=50` 被改成了 10？
A：创意搜索端点强制上限 10，本技能自动钳制。翻页请用 `page` 参数递增，建议配合缓存避免重复消耗配额.
### Q2：下载/收入数字和官方财报对不上？
A：本数据为第三方估算，非官方披露。请参考可信度分级（A/B/C），C 级数据仅用于趋势判断，不用于精确决策。长尾地区偏差可达 30%+.
### Q3：如何批量导出某竞品全部创意？
A：先用 `product-content-counts` 拿到总量，再分页 `product-content-search`（每页 10），结果写入本地文件。建议在夜间低峰执行，避免限流。100 条创意需 10 次请求.
### Q4：`totalSize` 为什么是 null？
A：过滤查询时 `totalSize` 可能为 null，此时以 `list` 长度为准，或单独调 `count` 端点获取准确总数.
### Q5：多个国家的数据能一次请求拿到吗？
A：`search` / `distribute` 支持 `countries` 数组，但结果会合并。如需分别对比，请并行发多个单国家请求，首轮并发 5-8 个.
### Q6：缓存数据过期了怎么办？
A：元数据缓存 24 小时、搜索结果 1 小时、详情 7 天。过期后自动重新拉取。如需强制刷新，删除 `~/.admapix-cache/` 对应目录.
## 已知限制

1. **单次请求单端点**：本技能保持薄客户端语义，多端点编排由 Agent 层完成，不内置批量端点聚合
2. **估算数据非官方**：下载/收入均为第三方估算，长尾地区偏差可达 30%+，不可作为财务依据
3. **`page_size` 硬上限 10**：翻页 100 条需 10 次请求，配额消耗较快，需配合缓存策略
4. **元数据需定期刷新**：行业码/国家码映射表为内置快照，未列出的参数需调 `filter-options` 获取最新
5. **不做分析与推荐**：仅透传结构化数据，不生成 H5/仪表盘/深度研究报告，分析与推荐需用户明确要求后另起
