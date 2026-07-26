---
slug: "bookmark-intelligence-free"
name: "bookmark-intelligence-free"
version: "1.0.0"
displayName: "书签智析基础版"
summary: "X书签基础监控版,每月10条限额,手动运行,基于关键词启发式分析,无AI与推送。"
license: "MIT"
description: |-
  X(Twitter)书签分析与知识萃取基础版(免费)。手动运行抓取最近的 X 书签,用关键词启发式提取摘要并落盘为本地 JSON.
  核心能力:每月 10 条书签处理、手动触发运行、关键词启发式分析、本地 JSON 沉淀.
  适用于先体验产品能力。如需无限制书签处理、AI 深度分析、后台守护进程自动监控与 Telegram 推送,请升级至 bookmark-intelligence 付费版.
tags:
  - 信息检索
  - 知识管理
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# 书签智析基础版

把你 X(Twitter)上的书签手动转化为本地知识卡片。免费版每月可处理 10 条书签,使用关键词启发式分析(无 AI),结果落盘为本地 JSON 供后续检索.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 书签智析基础版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
本Skill无需额外API Key（LLM能力由Agent平台内置提供）

### 可用性分类
- **分类**: MD+EXEC（）

## 核心能力

### 1. 手动运行抓取书签
手动触发一次抓取,处理最近的 X 书签(受每月 10 条限额约束),处理后退出.
```bash
npm start
```

**输出**: 返回手动运行抓取书签的处理结果,包含执行状态码、结果数据和执行日志.
### 2. 关键词启发式分析
免费版不接入 AI 后端,使用关键词匹配提取摘要与基础标签。分析深度有限,适合快速浏览书签主题.
**输入**: 用户提供关键词启发式分析所需的指令和必要参数.
**输出**: 返回关键词启发式分析的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`关键词启发式分析`的配置文档进行参数调优
### 3. 本地 JSON 沉淀
每条分析结果以 JSON 落盘到 `life/resources/bookmarks/bookmark-<id>.json`,包含原推文(作者、正文、互动数据)与基础分析,可被后续检索.
> **升级提示**: 无限制书签处理、AI 深度分析(关键概念+行动项+项目关联)、后台守护进程自动监控与 Telegram 高价值洞察推送仅在 [bookmark-intelligence 付费版](#) 中提供。- 验证返回数据的完整性和格式正确性
- 参考`本地 JSON 沉淀`的配置文档进行参数调优
#
## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及能力 |
|---:|---:|---:|---:|
| 手动归档书签 | 运行 `npm start` | 最近 10 条书签的本地 JSON 文件 | 手动运行+关键词分析 |
| 主题快速浏览 | 一批新书签 | 按关键词匹配的主题标签 | 关键词启发式分析 |

**不适用于**: 需要 AI 深度分析(关键概念、行动项、项目关联)的场景(需付费版),需要后台自动监控与推送的场景(需付费版守护进程),月处理量超过 10 条的场景(需付费版无限制).
## 使用流程

### 第一步:运行安装向导
```bash
cd skills/bookmark-intelligence
npm run setup
```
向导依次完成:检测 Node/bird、引导从浏览器提取 `auth_token` 与 `ct0`、测试凭证有效性.
### 第二步:手动运行处理书签
```bash
npm start
```
处理最近的书签(受每月 10 条限额约束),结果落盘到 `life/resources/bookmarks/`.
### 第三步:查看结果
直接打开 `life/resources/bookmarks/bookmark-*.json` 查看分析结果,或在终端用 `jq` 检索:
```bash
jq '.analysis.summary' life/resources/bookmarks/bookmark-*.json
```

## 案例展示

### 案例1:手动归档一批书签
**场景**: 你刚收藏了几条推文,想快速归档到本地.
**处理过程**:
1. 运行 `npm start`
2. 脚本抓取最近书签(本月额度内)
3. 关键词匹配生成基础分析

**输出** (`life/resources/bookmarks/bookmark-123.json` 节选):
```json
{
  "bookmarkId": 123,
  "tweet": { "author": "@ai_engineer", "text": "Vector embeddings for AI memory...", "likes": 342 },
  "analysis": {
    "summary": "关于 vector embeddings 与 AI memory 的推文",
    "tags": ["AI", "embedding", "memory"],
    "priority": "low"
  },
  "timestamp": "2026-07-20T10:30:00Z"
}
```
注意:免费版为关键词匹配,无行动项与项目关联,洞察深度有限.
## 异常处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:---:|:---:|:---:|:---:|
| 凭证缺失 | `Missing Twitter credentials` | 未运行 setup 或 `.env` 不存在 | 运行 `npm run setup`,确认 `.env` 含 `AUTH_TOKEN=` 与 `CT0=` 两行 |
| Cookie 过期 | `No bookmarks fetched` / `unauthorized` | X 的 auth_token/ct0 已失效 | 重新从浏览器提取 cookie 更新 `.env`,用 `npm test` 验证 |
| bird 未安装 | `bird: command not found` | 未全局安装 bird CLI | 执行 `npm install -g bird` |
| 超出月度限额 | `monthly limit reached: 10/10` | 免费版每月 10 条已用完 | 等待下月重置,或升级付费版解锁无限制处理 |
| 限流 | X 返回 429 | 短时间高频运行触发风控 | 降低运行频率(免费版每小时限 1 次) |

## 常见问题

### Q1: 免费版每月 10 条够用吗?
A: 适合先体验产品能力。如果你每周书签超过 2-3 条、希望持续自动归档,建议升级付费版解锁无限制处理与后台守护进程.
### Q2: 为什么分析结果比较浅?
A: 免费版使用关键词启发式分析(无 AI),仅做主题标签与摘要匹配。AI 深度分析(关键概念、行动项、项目关联)在付费版中提供.
### Q3: 能不能后台自动运行?
A: 免费版仅支持手动运行 `npm start`,不支持 PM2 守护进程自动监控。后台自动轮询在付费版中提供.
### Q4: Cookie 安全吗?
A: 凭证仅存储在本地 `.env`(权限 600,已加入 `.gitignore`),不会离开你的机器。数据仅在调用 X 抓取书签时发送给 X,无任何第三方遥测.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接和配置后重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **每月 10 条限额**: 超出后停止处理,需等下月重置或升级付费版
- **无 AI 分析**: 仅关键词启发式匹配,无关键概念提取与行动项生成
- **无项目关联**: 不支持 `contextProjects` 多项目上下文匹配
- **无自动监控**: 不支持 PM2 后台守护进程,需手动运行
- **无推送通知**: 不支持 Telegram 高价值洞察推送
- **限频**: 每小时限运行 1 次,避免触发 X 风控

---

> 想要无限制书签处理、AI 深度分析、后台守护进程自动监控与 Telegram 推送?升级至 [bookmark-intelligence 付费版](#),把收藏夹变成行动清单.