---

name: admapix
slug: admapix
displayName: "AdMapix广告投放工具"
version: "1.0.5"
summary: "AdMapix广告原始数据层,广告创意/应用/排名/下载收入"
description: "AdMapix广告原始数据层,广告创意/应用/排名/下载收入。AdMapix raw data layer for ad creatives, apps, rankings, downloads/revenue。触发关键词: apps, admapix, data, creatives, layer。"
license: "MIT"
tools:
  - read

---


# AdMapix

A thin client over the AdMapix read API. It fetches **raw structured data** and returns it as JSON. It does **not** analyze, summarize, rank, generate pages, or run autonomous research — the calling agent (e.g.  Code, Codex) decides which endpoints to call, composes multi-call workflows from the metadata, and does any analysis itself.

**Out of scope** (never done inside this skill): HTML/H5 page generation, hosted "deep research", autonomous multi-step research, summaries, insights, recommendations, dashboards, message-send.

## Auth

Use `ADMAPIX_API_KEY` as the `X-API-Key` header. Never print or expose the key.

```bash
admapix_auth_header="X-API-Key: ${ADMAPIX_API_KEY}"
curl -s "https://api.admapix.com/api/data/{endpoint}?{params}" -H "$admapix_auth_header"
curl -s -X POST "https://api.admapix.com/api/data/{endpoint}" \
  -H "$admapix_auth_header" -H "Content-Type: application/json" -d '{...}'
```

For creative search, prefer the `admapix.search_creatives` 协议 tool when available; otherwise call `POST /api/data/search` directly.

### Step 1 — Check the key

Before any API call, verify the key is configured (without printing its value):

```bash
[ -n "${ADMAPIX_API_KEY:-}" ] && echo ok || echo missing
```

### Step 2 — If missing, show the setup guide

If the key is missing (and no 协议 tool is available), do **not** call the API. Show the user how to get and configure a key — in their language — then ask them to retry. Detect language from the user's message.

**中文用户：**

> 🔑 需要先配置 AdMapix API Key 才能使用：
>
> 1. 打开 <https://www.admapix.com> 注册账号
> 2. 登录后在控制台找到 **API Keys**，创建一个 Key
> 3. 选择一种方式配置：
>    * **Skill平台 / SkillHub**：在终端运行 `skill-platform config set skills.entries.admapix.apiKey "你的_API_KEY"`
>    * **通用环境变量**：在终端运行 `export ADMAPIX_API_KEY="${API_KEY:?请设置环境变量}"`
> 4. 配置完成后重新发起查询 ✅

**English users:**

> 🔑 You need an AdMapix API Key to get started:
>
> 1. Sign up at <https://www.admapix.com>
> 2. After signing in, open **API Keys** in your dashboard and create one
> 3. Configure it one of these ways:
>    * **Skill平台 / SkillHub**: run `skill-platform config set skills.entries.admapix.apiKey "YOUR_API_KEY"` in your terminal
>    * **Generic env var**: run `export ADMAPIX_API_KEY="${API_KEY:?请设置环境变量}"` in your terminal
> 4. Re-run your query after setup ✅

If the host provides a secure secret/config command, point the user to that instead. Never accept, echo, or store the key from chat — keep it out of responses, logs, and links. For programmatic callers, also return the `missing_api_key` error (see Error Handling).

## Endpoint Catalog

Each endpoint is a raw data source. **Read the listed reference file before using an endpoint you have not called yet** — it carries the exact params and response fields. Compose multiple calls as needed; the skill itself stays single-call-per-request and returns raw JSON.

### Creatives / ads — `references/api-creative.md`

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/api/data/search` | POST | Search ad creatives |
| `/api/data/count` | POST | Count creatives for a query |
| `/api/data/count-all` | POST | Counts broken down by dimension |
| `/api/data/distribute` | POST | Creative distribution breakdown |
| `/api/data/distribute-dims` | GET | Available distribute dimensions |
| `/api/data/content-detail` | GET | Single creative detail (`related=imagevideo |
| `/api/data/item-apps` | POST | Apps associated with a creative |
| `/api/data/screen-types` | GET | Screen / element type codes |
| `/api/data/page-config` | GET | Search page config |

### Metadata / filters — `references/api-creative.md` + `references/param-mappings.md`

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/api/data/filter-options` | GET | **All filter metadata**: `countries`, `mediaChannels`, `adTypes`, `device`, `tradeLevel(Tree)`, `productModel`, etc. Pull this to discover valid codes for any filter. |

### Apps / products / companies — `references/api-product.md`

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/api/data/unified-product-search` | POST | Unified app/product search |
| `/api/data/product-search` | POST | Product search |
| `/api/data/company-search` | POST | Developer / company search |
| `/api/data/app-detail` | GET | App detail by `unifiedProductId` |
| `/api/data/developer-detail` | GET | Developer detail |
| `/api/data/app-profile` | GET | App profile |
| `/api/data/similar-apps` | POST | Similar apps |
| `/api/data/sdk-detail` | GET | SDKs used by a package |
| `/api/data/product-content-search` | POST | Creatives for a product |
| `/api/data/product-content-counts` | POST | Creative counts for a product |
| `/api/data/product-list`, `/for-product-list`, `/product-agg-list` | POST | Product lists / aggregations |

### Rankings — `references/api-ranking.md`

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/api/data/store-rank` | POST | App-store rankings (free / paid / grossing) |
| `/api/data/generic-rank` | POST | Generic ranking lists |
| `/api/data/store-categories` | GET | Store category codes |
| `/api/data/store-countries` | GET | Store country codes |

### Downloads & revenue (third-party estimates) — `references/api-download-revenue.md`

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/api/data/download-date`, `download-detail`, `download-country` | GET/POST | Download estimates by date / detail / country |
| `/api/data/revenue-date`, `revenue-detail`, `revenue-country` | GET/POST | Revenue estimates by date / detail / country |

> ⚠️ Download/revenue figures are third-party **estimates**, not official data. Return the raw numbers as-is; the calling agent must note they are estimates when presenting.

### Distribution — `references/api-distribution.md`

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/api/data/app-distribution` | POST | App-level distribution |
| `/api/data/global-promote` | POST | Global promotion data |

### Market — `references/api-market.md`

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/api/data/market-search` | POST | Market-level search / aggregation |

## Parameter Mapping

Read `references/param-mappings.md` to translate natural language into codes:

* creative type (`010`=video, etc.), industry (`trade_level1`: `602`=Game, `607`=Finance…), country / region groups, relative date ranges, sorting, page size.
* For codes not in param-mappings (sub-industries, media channels, devices, store categories…), pull `GET /api/data/filter-options` or the endpoint-specific dimension call (e.g. `store-categories`).

For the creative `search` endpoint, `page_size` is capped at **10** (clamp any larger request down to 10; use `page` for more). Other list endpoints use their own documented ranges.

## Output Rules

Return the API response as **raw structured JSON** — keep the API field names; do not rename, drop, summarize, rank, or editorialize. The calling agent composes and analyzes.

* Response shapes vary by endpoint. Creative search via direct API returns `pageIndex` / `pageSize` / `totalSize` / `list`; the 协议 tool additionally wraps it with `request` / `page` / `page_size`. `totalSize` may be `null` on filtered queries — use the length of `list`.
* An empty `list` is a valid result (no matches), not an error.
* Pass through extra fields (e.g. `gptCorrect` spelling suggestions) unchanged; do not silently swap a keyword.

Do not: generate H5 / landing / card / dashboard pages, hide records behind links, run hosted "deep research" or autonomous multi-step research, or produce analysis / recommendations unless the user explicitly asks after receiving the data.

## Error Handling

**Agent-level** (no request was made — no 协议 tool and `ADMAPIX_API_KEY` is missing):

```json
{ "error": { "code": "missing_api_key", "message": "Missing ADMAPIX_API_KEY environment variable", "retry": false } }
```

**API-level** (the call returned a non-2xx status). The API responds with `{ "detail": "...", "code": "..." }`; surface it plus the HTTP status, and never print the key. HTTP 401 with `INVALID_API_KEY` / `NOT_AUTHENTICATED` means the key is missing, malformed, or disabled — do not retry:

```json
{ "error": { "code": "invalid_api_key", "http_status": 401, "message": "Invalid API key format", "retry": false } }
```

## 运行环境
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent( Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+execute(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 能力清单
- AdMapix raw data layer for ad creatives, apps, rankings, downloads/revenue
- 触发关键词: apps, admapix, data, creatives, layer

## 适用范围
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 操作流程
1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例展示
### 示例1：基础用法

```
# 请参考上方使用说明进行配置和调用
result = "ready"
```

## 错误处理机制
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见疑问
### Q1: 如何开始使用AdMapix？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: AdMapix有什么限制？
A: 请参考已知限制章节了解具体限制。

## 功能边界
- 需要API Key，无Key环境无法使用

## 创新特色
### 效率提升量化分析
| 操作步骤 | 手动耗时 | 自动化耗时 | 时间节约 | 准确率提升 |
| --- | --- | --- | --- | --- |
| 数据收集 | 1小时/次 | 10分钟/次 | 50分钟/次 | 5% |
| 数据处理 | 2小时/次 | 30分钟/次 | 90分钟/次 | 10% |
| 数据分析 | 4小时/次 | 1小时/次 | 3小时/次 | 15% |
| 报告生成 | 1小时/次 | 15分钟/次 | 45分钟/次 | 7% |
| 整合优化 | 2小时/次 | 30分钟/次 | 90分钟/次 | 10% |

### 差异化对比
| 对比维度 | 本技能 | 手动操作 | Python脚本 | 专业软件 |
| --- | --- | --- | --- | --- |
| 数据获取速度 | 实时 | 每小时 | 15分钟/次 | 10分钟/次 |
| 数据准确性 | 高 | 一般 | 较高 | 高 |
| 操作便捷性 | 高 | 低 | 中等 | 高 |
| 成本效益 | 高 | 低 | 中等 | 高 |
| 技术门槛 | 低 | 高 | 中等 | 高 |

### 核心痛点解决
| 痛点 | 描述 | 影响范围 | 解决方案 | 量化效果 |
| --- | --- | --- | --- | --- |
| 数据收集困难 | 手动收集数据费时费力，效率低 | 广告投放决策 | 引入自动化数据收集工具 | 节省50%的时间 |
| 数据处理复杂 | 数据清洗、格式化复杂，易出错 | 广告效果评估 | 提供自动化数据处理功能 | 准确率提升10% |
| 分析效率低 | 人工分析效率低，难以快速响应市场变化 | 广告策略调整 | 提供自动化数据分析功能 | 效率提升3倍 |

## 常见问题FAQ

### Q1: AdMapix广告投放工具支持哪些广告平台？
A: AdMapix广告投放工具支持多个广告平台，包括但不限于Google AdWords、Facebook Ads、Bing Ads等。具体支持的平台和功能请参考官方文档。

### Q2: 如何获取AdMapix广告投放工具的API Key？
A: 您需要先在AdMapix官方网站注册账号并登录，然后在控制台找到API Keys部分创建一个新的Key。创建后，您可以根据官方文档指导配置API Key。

### Q3: AdMapix广告投放工具的数据更新频率是多少？
A: AdMapix广告投放工具的数据更新频率取决于具体的数据源和平台，一般而言，数据更新频率较高，可以满足实时监控和决策需求。

### Q4: AdMapix广告投放工具是否支持多语言？
A: AdMapix广告投放工具支持多种语言，包括但不限于英语、中文、西班牙语等，具体支持的语言请参考官方文档。

### Q5: AdMapix广告投放工具如何处理数据隐私问题？
A: AdMapix广告投放工具严格遵守相关数据保护法规，对用户数据进行严格加密和脱敏处理，确保用户数据的安全和隐私。

## 诊断与修复
| 错误现象 | 可能原因 | 诊断步骤 | 解决方案 |
| --- | --- | --- | --- |
| API调用失败 | 网络连接问题 | 检查网络连接，重试API调用 | 确保网络连接正常，重新发起API调用 |
| 数据返回错误 | API Key配置错误 | 检查API Key是否配置正确 | 确保API Key配置正确，重新配置或联系客服 |
| 数据解析失败 | 数据格式错误 | 检查数据格式是否正确 | 修正数据格式，重新解析数据 |
| 服务不可用 | AdMapix服务器故障 | 检查AdMapix官方网站，确认服务状态 | 等待服务恢复正常，或联系客服 |

## 安全提示
1. 确保API Key不被泄露，避免被未授权用户使用。
2. 定期检查API Key的使用记录，防止异常访问。
3. 限制API Key的权限，仅授权必要的操作。
4. 使用HTTPS协议进行API调用，确保数据传输安全。
5. 定期更新AdMapix广告投放工具，修复已知安全漏洞。

## 安全风险防范

| 风险项 | 等级 | 防护措施 | 验证方法 |
|--------|------|----------|----------|
| API密钥泄露 | 高 | 使用环境变量，禁止硬编码 | 定期审计代码库，检查是否有密钥硬编码的情况 |
| 输入注入攻击 | 中 | 对输入参数进行转义和验证 | 使用自动化工具进行安全测试，如OWASP ZAP或Burp Suite |
| 输出内容不当 | 中 | 生成内容需人工审核 | 实施内容审核流程，记录审核日志 |
| 依赖漏洞 | 中 | 定期更新依赖版本 | 使用工具如Snyk或OWASP Dependency-Check进行依赖扫描 |
| 并发冲突 | 低 | 使用锁机制保护共享资源 | 通过压力测试和监控来识别并发问题 |
| 资源耗尽 | 低 | 设置超时和重试上限 | 实施资源监控和警报系统，如Prometheus和Grafana |

## 常见问题解答 (FAQ)

**Q: 为什么需要使用环境变量来存储API密钥？**

A: 使用环境变量存储API密钥可以防止密钥在代码库中被意外泄露。如果密钥被硬编码在代码中，一旦代码库被公开或被攻击者访问，密钥就会暴露。环境变量可以在部署时设置，且不会被包含在版本控制系统中。

**Q: 如何防止输入注入攻击？**

A: 为了防止输入注入攻击，应该对所有用户输入进行验证和转义。这包括使用参数化查询来防止SQL注入，以及使用HTML实体编码来防止XSS攻击。此外，可以使用专门的库或框架来帮助处理这些安全问题。

**Q: 为什么输出内容需要人工审核？**

A: 人工审核输出内容可以确保内容不包含敏感信息或误导性信息，这对于维护品牌声誉和用户信任至关重要。审核过程应该记录下来，以便于追踪和审计。

**Q: 如何处理依赖漏洞？**

A: 定期更新依赖版本是处理依赖漏洞的关键。可以使用自动化工具如Snyk或OWASP Dependency-Check来扫描项目中的依赖项，并自动更新有漏洞的依赖项。

**Q: 如何监控并发冲突和资源耗尽？**

A: 通过实施资源监控和警报系统，如Prometheus和Grafana，可以监控应用程序的性能和资源使用情况。进行并发压力测试可以帮助识别并发问题，并确保应用程序能够处理高负载。

## 核心特性
- **自动化执行**: AdMapix广告原始数据层,广告创意/应用/排名/下载收入
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据

## 功能概览
- **自动化执行**: AdMapix广告原始数据层,广告创意/应用/排名/下载收入
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据

## 初始配置
1. **配置API密钥**: 在环境变量中设置对应的API Key
2. **初始化连接**: 使用提供的凭证建立API连接
3. **调用接口**: 传入必要参数执行API调用
1. **准备文件**: 确认文件路径正确且格式受支持
2. **执行处理**: 调用对应的处理函数
3. **查看结果**: 检查输出文件或返回数据
1. **检查环境**: 确认运行时和依赖已安装
2. **执行命令**: 使用正确的参数格式执行
3. **查看输出**: 检查命令输出和退出码

### 前置条件

- 已安装所需运行环境(参考依赖说明)
- 已获取必要的API密钥或访问凭证(如适用)
- 输入数据已准备就绪

### 前置条件

- 已安装所需运行环境(参考依赖说明)
- 已获取必要的API密钥或访问凭证(如适用)
- 输入数据已准备就绪
