---
slug: "bookmark-intelligence"
name: "bookmark-intelligence"
version: 1.0.1
displayName: "书签智析专业版"
summary: "自动监控X书签、抓取链接文章、AI提取关键概念与行动项,关联个人项目并推送高价值洞察。"
license: "Proprietary"
description: |-
  X(Twitter)书签自动化分析与知识萃取专业版。持续监控你的 X 书签,抓取推文所链接文章的完整正文,
  用 AI 提取关键概念、可执行行动项与实现建议,并关联你在 config.json 中声明的活跃项目.
  核心能力:后台守护进程自动轮询、无限制书签处理、AI 深度分析(非关键词匹配)、
  Telegram 高价值洞察推送、本地可检索知识库沉淀、多项目上下文匹配.
  适用于独立开发者、研究者和内容工作者把收藏夹从"信息坟墓"变成"行动清单".
tags:
  - 信息检索
  - 知识管理
  - 自动化
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# 书签智析专业版

把你 X(Twitter)上的书签自动转化为可执行的知识与行动清单。后台守护进程持续轮询新书签,AI 抓取并分析链接文章正文,关联你的活跃项目,高价值洞察通过 Telegram 推送.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 书签智析专业版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 书签智析专业版自动监控 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 1. 自动监控与轮询
通过 PM2 守护进程按 `checkIntervalMinutes`(默认 60 分钟)轮询新书签,无需手动触发.
```bash
npm run daemon
# 启动后台守护进程,每 60 分钟检查一次新书签
pm2 status bookmark-intelligence   # 查看运行状态
pm2 logs bookmark-intelligence     # 查看分析日志
```

**输出**: 返回自动监控与轮询的处理结果,包含执行状态码、结果数据和执行日志.
### 2. 链接文章正文抓取
不只分析推文本身,还会抓取推文所链接文章的完整正文(博客、新闻、文档),作为 AI 分析的输入源.
**输出**: 返回链接文章正文抓取的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`链接文章正文抓取`的配置文档进行参数调优
### 3. AI 深度分析
对每条书签产出结构化分析:
- **内容摘要**: 文章核心观点的一句话总结
- **关键概念**: 提取 3-5 个关键术语与解释
- **可执行行动项**: 列出可立即执行的具体步骤
- **项目关联**: 与你在 `contextProjects` 中声明的项目一一匹配,给出实现建议
- **优先级**: 标记 `high` / `medium` / `low`,决定是否触发推送

**输出**: 返回AI 深度分析的处理结果,包含执行状态码、结果数据和执行日志.
### 4. 多项目上下文匹配
在 `config.json` 的 `contextProjects` 中声明你的活跃项目,越具体,AI 关联越精准.
```json
{
  "contextProjects": [
    "用 Python 和 Binance API 构建加密货币交易机器人",
    "学习 Rust 做系统编程",
    "把 SaaS 做到月入 1 万美元"
  ]
}
```

**输入**: 用户提供多项目上下文匹配所需的指令和必要参数.
**处理**: 解析多项目上下文匹配的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回多项目上下文匹配的处理结果,包含执行状态码、结果数据和执行日志.
### 5. Telegram 高价值洞察推送
当分析结果为 `priority: "high"` 且 `hasActionableInsights: true` 时,自动推送 Telegram 通知,包含摘要、行动项、关键概念、实现建议与原文链接。- 验证返回数据的完整性和格式正确性
- 参考`Telegram 高价值洞察推送`的配置文档进行参数调优
### 6. 本地知识库沉淀
每条分析结果以 JSON 落盘到 `life/resources/bookmarks/bookmark-<id>.json`,包含原推文(作者、正文、互动数据)、完整分析、实现建议、优先级与时间戳,可被后续检索与导出。- 验证返回数据的完整性和格式正确性
- 参考`本地知识库沉淀`的配置文档进行参数调优
#
## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及能力 |
|:---:|:---:|:---:|:---:|
| 研究资料自动归档 | 书签一条"向量嵌入实现"推文 | 抓取链接文章 + AI 提取关键概念 + 关联"交易机器人"项目并给出实现建议 | 链接抓取+AI分析+项目关联 |
| 高价值洞察即时推送 | 书签一条含可落地技巧的推文 | Telegram 通知(摘要+行动项+原文链接) | 自动监控+优先级推送 |
| 长期知识库构建 | 持续书签数月 | 本地可检索的 bookmark-*.json 知识库,可导出至 Notion/Obsidian | 本地沉淀 |
| 多项目并行跟踪 | 同时在做交易机器人和 Rust 学习 | 同一条书签分别关联两个项目并给出差异化建议 | 多项目上下文匹配 |

**不适用于**: 非 X 平台的书签(Pocket、Chrome 书签等),需要实时毫秒级响应的场景(轮询间隔最短建议 15 分钟).
## 使用流程

### 第一步:运行安装向导
```bash
cd skills/bookmark-intelligence
npm run setup
```
向导依次完成:检测 Node/bird/PM2、引导从浏览器提取 `auth_token` 与 `ct0`、询问活跃项目、配置通知偏好、测试凭证有效性.
### 第二步:首次处理存量书签
```bash
npm start
```
一次性处理最近 `bookmarkCount`(默认 50)条书签并退出,确认分析质量符合预期.
### 第三步:启动后台守护进程
```bash
npm run daemon
```
按 `checkIntervalMinutes` 自动轮询新书签,无需人工介入.
### 第四步:调优项目上下文(可选)
分析结果偏泛泛时,编辑 `config.json` 让 `contextProjects` 更具体(加入技术栈、目标、阶段),重启守护进程:
```bash
pm2 restart bookmark-intelligence
```

#
## 案例展示

### 案例1:研究资料自动归档与项目关联
**场景**: 你在做加密货币交易机器人,书签了一条关于"vector embeddings for AI memory"的推文.
**处理过程**:
1. 守护进程检测到新书签
2. 抓取推文所链接文章的完整正文
3. AI 提取关键概念、行动项,并关联你的"交易机器人"项目

**输出** (`life/resources/bookmarks/bookmark-123.json` 节选):
```json
{
  "bookmarkId": 123,
  "tweet": { "author": "@ai_engineer", "text": "Vector embeddings for AI memory...", "likes": 342 },
  "analysis": {
    "summary": "用向量嵌入把历史市场分析结构化存储,实现相似行情检索",
    "keyConcepts": ["embedding", "cosine similarity", "ANN index"],
    "actionItems": [
      "用 text-embedding-3-small 对每日盘后总结生成嵌入",
      "存入 pgvector 并建 HNSW 索引"
    ],
    "projectRelation": "交易机器人:可用嵌入检索历史相似行情,辅助策略回测",
    "priority": "high",
    "hasActionableInsights": true
  },
  "timestamp": "2026-07-20T10:30:00Z"
}
```
同时触发 Telegram 推送,包含摘要、行动项与原文链接.
### 案例2:高价值洞察即时推送
**场景**: 你书签了一条含可落地技巧的推文,希望第一时间收到提醒.
**触发条件**: 分析结果 `priority: "high"` 且 `hasActionableInsights: true`.
**Telegram 通知内容**:
```text
[高价值书签] Vector embeddings for AI memory
# ...
摘要: 用向量嵌入把历史市场分析结构化存储,实现相似行情检索
# ...
可执行行动项:
1. 用 text-embedding-3-small 对每日盘后总结生成嵌入
2. 存入 pgvector 并建 HNSW 索引
# ...
关键概念: embedding, cosine similarity, ANN index
关联项目: 交易机器人
原文: https://x.com/ai_engineer/status/123456
```

### 案例3:多项目并行跟踪
**场景**: 你同时在学 Rust 和做交易机器人,书签了一条关于"wasm 性能优化"的推文.
**处理过程**: AI 检测到该内容同时关联两个项目,产出差异化建议:
```json
{
  "projectRelations": [
    { "project": "学习 Rust", "suggestion": "用 wasm-bindgen 把 Rust 编译为 wasm,在浏览器跑基准" },
    { "project": "交易机器人", "suggestion": "把回测引擎的 Rust 核心编译为 wasm,在前端实时可视化" }
  ]
}
```
一条书签同时滋养两个项目,避免重复阅读.
## 异常处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:------|------:|:------|:------|
| 凭证缺失 | `Missing Twitter credentials` | 未运行 setup 或 `.env` 不存在 | 运行 `npm run setup`,确认 `.env` 含 `AUTH_TOKEN=` 与 `CT0=` 两行 |
| Cookie 过期 | `No bookmarks fetched` / `unauthorized` | X 的 auth_token/ct0 已失效(通常数周过期) | 重新从浏览器提取 cookie 更新 `.env`,用 `npm test` 验证 |
| bird 未安装 | `bird: command not found` | 未全局安装 bird CLI | 执行 `npm install -g bird` |
| 守护进程停止 | PM2 列表中进程 offline | PM2 未安装或守护崩溃 | `npm install -g pm2` 后 `npm run daemon` 重启,查 `pm2 logs` 定位崩溃 |
| 分析结果泛泛 | 输出与项目无关 | `contextProjects` 描述太笼统 | 编辑 `config.json` 加入技术栈、目标、阶段等具体描述,`pm2 restart` |
| 文章抓取失败 | `failed to fetch linked article` | 链接需付费墙/被风控/已删除 | 脚本自动降级为仅分析推文正文,不影响整体流程 |
| 限流 | X 返回 429 | `bookmarkCount` 过大或轮询过频 | 降低 `bookmarkCount`(如 30)、增大 `checkIntervalMinutes`(如 120) |
| 无 LLM 降级 | 分析退化为关键词匹配 | 运行环境无 AI 后端 | 在 Agent 平台内运行以启用 LLM,或接受关键词启发式分析(质量较低) |

## 常见问题

### Q1: Cookie 安全吗?会被上传吗?
A: 凭证仅存储在本地 `.env`(权限 600,已加入 `.gitignore`),不会离开你的机器。数据仅在调用 X 抓取书签、调用 AI 分析时按需发送给 X 和 AI 服务商,无任何第三方遥测.
### Q2: 分析结果质量不高、和我的项目无关怎么办?
A: 核心在 `contextProjects` 的具体程度。把"trading bot"改成"用 Python 和 Binance API 构建加密货币交易机器人,当前在做回测引擎",AI 关联精度会显著提升。改完执行 `pm2 restart bookmark-intelligence`.
### Q3: 守护进程会一直占用资源吗?
A: 不会。PM2 守护进程在两次轮询之间处于空闲等待,仅在每个 `checkIntervalMinutes` 周期唤醒一次抓取与分析。默认 60 分钟间隔下,日均 CPU 占用可忽略.
### Q4: 能否把分析结果导出到 Notion 或 Obsidian?
A: 可以。每条分析是结构化 JSON,可在 `scripts/` 下自建导出脚本(如 `export-to-notion.js`)读取 `life/resources/bookmarks/*.json` 并写入目标平台。JSON 结构稳定,适配各平台 API.
### Q5: 没有接入 Agent 平台能用吗?
A: 能。脚本可独立运行,但会降级为关键词启发式分析(无 AI 深度分析),且无 Telegram 推送。要获得完整能力需在支持 LLM 的 Agent 平台内运行.
### Q6: 超出处理上限会怎样?
A: 专业版为无限制书签处理,不会触顶。如使用免费版超限(每月 10 条),处理在第 10 条后停止并提示升级,已分析数据不受影响.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **仅支持 X 平台**: 不覆盖 Pocket、Chrome 书签、Raindrop 等其他收藏源
- **依赖 X Cookie**: Cookie 数周过期一次,需定期更新 `.env`
- **付费墙文章抓取受限**: 遇付费墙会自动降级为仅分析推文正文
- **轮询非实时**: 最短建议间隔 15 分钟,不适合需要秒级响应的场景
- **AI 分析质量依赖 LLM**: 无 LLM 环境下降级为关键词匹配,洞察深度下降
- **单机许可**: 一个 license key 绑定一台机器,换机需联系支持转移
- **X 限流风险**: 短时间高频抓取可能触发 X 的 429 限流,需配合 `bookmarkCount` 与轮询间隔调优
