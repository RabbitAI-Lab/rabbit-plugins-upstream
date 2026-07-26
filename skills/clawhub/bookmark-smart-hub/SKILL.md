---
slug: "bookmark-smart-hub"
name: "bookmark-smart-hub"
version: 1.0.1
displayName: "书签智能中心专业版"
summary: "自动化书签监控与 AI 深度分析平台，支持后台守护、多渠道通知与知识库全文检索。"
license: "Proprietary"
edition: "pro"
description: |-
  面向知识工作者与团队的自动化书签监控与 AI 分析平台.
  核心能力: 后台自动监控、AI 深度分析、多渠道通知、知识库全文检索、趋势发现、数据导出、团队共享.
  适用场景: 知识管理自动化、研究素材收集、行业趋势跟踪、团队知识沉淀、内容灵感挖掘.
  差异化: 专业版在免费版基础上新增自动化监控与 AI 分析，兼容免费版存储格式与配置.
tags:
  - 书签管理
  - AI分析
  - 自动化监控
  - 知识库
  - 团队协作
  - 趋势发现
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# 书签智能中心专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 书签智能中心专业版自动化书签监控 | 不支持 | 支持 |
| 书签智能中心专业版深度分析 | 不支持 | 支持 |
| 书签智能中心专业版通知与知识库全文检索 | 不支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |

## 核心能力

| 能力 | 免费版 | 专业版 |
|:-----|:-----|:-----|
| 书签抓取 | 支持 | 支持 |
| 文章全文提取 | 支持 | 支持 |
| 关键词分析 | 支持 | 支持 |
| AI 深度分析 | - | 支持 |
| 后台自动监控 | - | 支持 |
| 多渠道通知 | - | 支持 |
| 知识库全文检索 | - | 支持 |
| 跨书签趋势发现 | - | 支持 |
| 数据导出 | - | 支持 |
| 团队知识共享 | - | 支持 |
| 自定义 AI 模型 | - | 支持 |
| 处理上限 | 20 条/次 | 无限制 |
### 书签抓取

针对书签抓取,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供书签抓取相关的配置参数、输入数据和处理选项.
**输出**: 返回书签抓取的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`书签抓取`的配置文档进行参数调优
### 文章全文提取

针对文章全文提取,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供文章全文提取相关的配置参数、输入数据和处理选项.
**输出**: 返回文章全文提取的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`文章全文提取`的配置文档进行参数调优
### 关键词分析

针对关键词,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供关键词分析相关的配置参数、输入数据和处理选项.
**输出**: 返回关键词分析的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`关键词分析`的配置文档进行参数调优
#
## 适用场景

### 场景一：自动化后台监控与通知

专业版以后台守护进程运行，自动监控新书签并实时推送高价值洞察.
```bash
# 启动后台守护进程
npm run daemon
# ...
# 管理守护进程
pm2 status bookmark-smart-hub      # 查看运行状态
pm2 logs bookmark-smart-hub        # 查看日志
pm2 restart bookmark-smart-hub     # 重启
pm2 stop bookmark-smart-hub        # 暂停
```

**通知示例（Telegram 推送）**

```text
📚 高价值洞察发现
# ...
🎯 内容: 向量数据库在 RAG 系统中的实践
📝 作者: @aiengineer
🔗 链接: example.com/vector-rag
# ...
💡 核心概念:
- 向量索引优化策略
- 混合检索（向量+关键词）
- 上下文窗口管理
# ...
🔨 对你的项目建议:
- 交易机器人: 用向量存储历史行情模式
- Agent 记忆: 将对话历史向量化检索
# ...
⭐ 优先级: 高
```

### 场景二：AI 深度分析与项目关联

AI 不仅提取关键词，还分析内容与用户项目的关联，给出可执行建议.
```python
# 示例
import json
# ...
# 模拟 AI 分析结果
analysis = {
    "bookmarkId": "bookmark-042",
    "title": "向量数据库在 RAG 系统中的实践",
    "aiAnalysis": {
        "summary": "探讨了向量数据库在检索增强生成系统中的架构设计与性能优化",
        "keyConcepts": [
            "向量索引（HNSW/IVF）",
            "混合检索策略",
            "上下文窗口管理",
            "重排序算法"
        ],
        "actionableItems": [
            "评估 HNSW 索引参数对召回率的影响",
            "实现向量与关键词混合检索",
            "设计上下文压缩策略降低 Token 消耗"
        ],
        "projectRelations": {
            "交易机器人": "用向量存储历史行情模式，实现相似场景检索",
            "Agent 记忆": "将对话历史向量化，支持语义检索而非时间排序"
        },
        "priority": "high",
        "hasActionableInsights": True
    }
}
# ...
print(json.dumps(analysis, ensure_ascii=False, indent=2))
```

### 场景三：知识库全文检索与趋势发现

跨书签搜索已积累的知识，发现反复出现的主题趋势.
```bash
# 全文检索知识库
node （请参考skill目录中的脚本文件） --query "向量检索" --limit 10
# ...
# 输出示例
# 🔍 搜索结果: "向量检索"
# 1. [高] 向量数据库入门指南 (bookmark-001)
#    相关度: 0.95 | 日期: 2026-07-15
# 2. [高] 向量数据库在 RAG 系统中的实践 (bookmark-042)
#    相关度: 0.92 | 日期: 2026-07-18
# 3. [中] embedding 技术全景 (bookmark-015)
#    相关度: 0.78 | 日期: 2026-07-10
```

```bash
# 发现趋势主题
node （请参考skill目录中的脚本文件） --period "30d"
# ...
# 输出示例
# 📈 近30天趋势主题:
# 1. 向量数据库 (出现 8 次, 上升趋势 ↑)
# 2. RAG 系统 (出现 6 次, 上升趋势 ↑)
# 3. Agent 架构 (出现 5 次, 稳定 →)
# 4. 提示工程 (出现 3 次, 下降趋势 ↓)
```

## 使用流程

1. 安装依赖与 PM2（后台守护需要）.
```bash
cd skills/bookmark-smart-hub
npm install
npm install -g pm2
```

2. 运行配置向导.
```bash
npm run setup
```

向导将引导你完成：
- 社交平台凭证配置
- AI 分析模型选择（默认 GPT-4o-mini）
- 通知渠道配置（Telegram / Slack / Discord）
- 个人项目与兴趣描述（提升 AI 关联精准度）
- 监控频率设置

3. 启动后台守护进程.
```bash
npm run daemon
```

4. 验证运行状态.
```bash
pm2 status bookmark-smart-hub
pm2 logs bookmark-smart-hub --lines 20
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | bookmark-smart-hub处理的内容输入 |,  |
| content | string | 否 | bookmark-smart-hub处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "hub 相关配置参数",
    result: "hub 相关配置参数",
    result: "hub 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **运行时**：Node.js v16+

### 依赖说明(补充)

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| Node.js v16+ | 运行时 | 必需 | nodejs.org 官方下载 |
| bird CLI | 命令行工具 | 必需 | `npm install -g bird` |
| PM2 | 进程管理 | 必需 | `npm install -g pm2`（后台守护需要） |
| 社交平台凭证 | API 凭证 | 必需 | 浏览器开发者工具获取 |
| AI API Key | API 凭证 | 必需 | OpenAI / Anthropic 等平台申请 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| 数据库 | 存储 | 可选 | 全文检索索引（可选，默认文件存储） |

### API Key 配置

- 在 `.env` 文件中配置社交平台凭证（`AUTH_TOKEN` 与 `CT0`）.
- 在 `config.json` 的 `aiApiKey` 字段配置 AI 分析模型 API Key.
- 通知渠道凭证（Telegram Bot Token、Slack Webhook 等）在对应通知配置中填入.
```bash
# .env 环境变量示例
AUTH_TOKEN=your_social_auth_token
CT0=your_social_ct0_token
AI_API_KEY=your_ai_api_key
TG_BOT_TOKEN=your_telegram_bot_token
SLACK_WEBHOOK_URL=your_slack_webhook_url
```

### 可用性分类

- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务。专业版在免费版基础上新增自动化监控、AI 深度分析与多渠道通知，存储格式与配置向后兼容免费版.
## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

## 常见问题

### Q1：专业版如何兼容免费版？

专业版与免费版使用相同的存储格式。免费版创建的 JSON 文件可直接被专业版读取，AI 分析结果会自动补全至 `aiAnalysis` 字段，不影响原有的关键词分析数据.
### Q2：后台守护进程意外停止怎么办？

```bash
pm2 status                          # 查看状态
pm2 logs bookmark-smart-hub         # 查看错误日志
pm2 restart bookmark-smart-hub      # 重启
```

若频繁崩溃，检查凭证是否过期、磁盘空间是否充足、网络是否正常.
### Q3：AI 分析结果不够精准？

- 将 `contextProjects` 填写得更具体（包含技术栈、目标、当前阶段）.
- 尝试更换 AI 模型（如从 `gpt-4o-mini` 升级至 `gpt-4o`）.
- 检查文章全文提取是否完整，内容不完整会导致分析偏差.
### Q4：支持哪些通知渠道？

专业版支持 Telegram、Slack、Discord 三种通知渠道，可同时开启多个。通知仅在内容优先级达到 `notifyThreshold` 时触发.
### Q5：全文检索支持中文吗？

支持。专业版内置中文分词，支持中英文混合全文检索.
### Q6：趋势发现是如何工作的？

系统定期分析知识库中的书签，按主题聚类统计出现频率，计算上升/稳定/下降趋势。趋势周期可在 `trends.analysisPeriod` 中配置（如 `7d`、`30d`、`90d`）.
### Q7：可以自定义 AI 模型吗？

可以。在配置中设置 `aiModel` 与 `aiApiKey`。企业用户可配置自有 API 端点，支持 OpenAI、Anthropic 及兼容 OpenAI 接口的自部署模型.
### Q8：处理的书签会重复分析吗？

不会。系统通过 `bookmarks.json` 状态文件记录已处理的书签 ID，重复运行时自动跳过已分析的书签.
### Q9：数据隐私如何保障？

- 凭证存储在本地 `.env`（权限 600），不上传任何第三方.
- 书签内容存储在本地知识库.
- AI 分析调用外部 LLM API 时仅发送文章文本，不发送个人凭证.
- 无遥测、无回传.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

