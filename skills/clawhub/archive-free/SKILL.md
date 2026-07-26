---
slug: "archive-free"
name: "archive-free"
version: 1.0.1
displayName: "智能内容归档免费版"
summary: "免费版内容归档工具，支持文章、视频、推文的内容提取与标签管理。"
license: "MIT"
description: |-
  内容归档工具免费版，将外部内容捕获为本地快照.
  支持文章、视频、推文的基本内容提取与标签管理.
  提供基于关键词的搜索能力.
  适用于个人知识管理与研究资料收集.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 通用办公

---
# 智能内容归档（免费版）

将外部内容捕获为本地快照，支持文章、视频、推文的内容提取与标签管理.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 智能内容归档免费版处理的输入数据或指令 |
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
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 全文内容提取
当归档内容时，提取完整内容而非仅保存链接：

- 提取正文全文、作者、发布日期等元数据
- 生成内容摘要
- 识别关键引用与数据点
- 每个归档项存储为独立的Markdown文件

**处理**: 解析全文内容提取的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 文章与网页归档（Article/Webpage）
将网页文章保存为本地快照：

- 提取文章全文、作者、日期、关键引用
- 保留原始URL用于溯源
- 处理PDF与学术论文：提取标题、作者、摘要

**输入**: 用户提供文章与网页归档（Article/Webpage）所需的指令和必要参数.
### 视频与推文归档（Video/Tweet）
针对视频与推文内容进行结构化归档：

- YouTube视频：提取标题、创作者、时长、关键时间戳
- 推文/线程：提取全文、作者、上下文
- 保留原始链接以便回溯

**输入**: 用户提供视频与推文归档（Video/Tweet）所需的指令和必要参数.
**处理**: 解析视频与推文归档（Video/Tweet）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回视频与推文归档（Video/Tweet）的处理结果,包含执行状态码、结果数据和执行日志。### 标签管理与搜索

为归档项分配标签并支持搜索：

- 根据内容自动生成标签
- 支持按标签与关键词搜索
- 存储至 `~/archive/items/{date}_{slug}.md`

#
## 使用流程

1. 首次使用时创建归档目录：`mkdir -p ~/archive/items ~/archive/projects`
2. 将需要归档的内容（URL、文本）发送给Agent
3. Agent提取完整内容并生成摘要与标签
4. 内容保存至 `~/archive/items/{date}_{slug}.md`
5. 需要检索时使用关键词或标签描述进行搜索

#
## 示例

### 示例1：归档一篇文章

```
用户: 帮我归档这篇文章 https://example.com/saas-pricing
# ...
Agent: 已归档！
- 类型: article
- 标题: The Complete Guide to SaaS Pricing
- 作者: Jane Doe
- 摘要: 文章探讨了三种主流SaaS定价模型...
- 标签: [pricing, saas, strategy]
- 存储位置: ~/archive/items/2026-02-16_saas-pricing.md
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 归档目录不存在 | 首次使用未创建目录 | 执行 `mkdir -p ~/archive/items ~/archive/projects` 创建目录 |
| 内容提取失败 | 网页有反爬虫机制 | 提示用户提供内容文本；记录失败URL |
| 搜索无结果 | 关键词未匹配 | 尝试同义词；检查标签拼写 |

## 常见问题

### Q1: 免费版与付费版有什么区别？
A: 免费版提供基础的内容提取、标签管理与关键词搜索功能。付费版额外提供语义搜索、主动浮现、视频时间戳提取等高级功能.
### Q2: 支持哪些内容类型？
A: 支持文章/网页、YouTube视频、推文/线程、PDF/论文等基本类型的内容归档.
### Q3: 归档内容存储在哪里？
A: 所有归档内容存储在本地 `~/archive/` 目录下，每个归档项为独立的Markdown文件.
## 已知限制

- 仅支持基于关键词的搜索，不支持语义搜索
- 不支持主动浮现机制
- 不支持跨设备同步（需手动同步目录）
- 媒体文件仅保存描述与元数据，不保存原始二进制文件

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "智能内容归档免费版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "archive"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
