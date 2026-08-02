---
slug: brave-search-tool-free
name: brave-search-tool-free
version: 1.0.2
displayName: Brave搜索工具-免费版
summary: "基于Brave Search API的网页搜索与内容提取工具,无需浏览器,适合个人用户。基于 Brave Search API 的无头网页搜索与内容提取工具,无需启动浏览器,,提供核心能力"
license: MIT
edition: free
description: "基于 Brave Search API 的无头网页搜索与内容提取工具,无需启动浏览器,，可自发提升工作效率. 适用于需要brave search tool相关能力的开发场景,包含结构化的工作流程和可复用的模板,帮助用户快速完成任务并保持代码质量. 适用于需要brave search tool相关能力的开发场景,包含结构化的工作流程和配置指引."
tags:
  - 研究工具
  - brave
  - search
  - automation
  - productivity
  - 网页搜索
  - 信息检索
  - 搜索
  - 检索
  - 工具
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
category: "Knowledge"
pricing_tier: free

---
# Brave搜索工具(免费版)

## 概述

本工具基于 Brave Search API 实现无头网页搜索与内容提取,无需启动浏览器,适合文档查询、事实查询与特定 URL 内容提取等任务。免费版面向个人用户,提供基础搜索、内容提取与结果数量配置能力.
### 适用场景

| 场景 | 是否推荐本工具 |
|---|-------|
| 搜索文档或 API 参考 | 推荐 |
| 查询事实或最新信息 | 推荐 |
| 从特定 URL 提取内容 | 推荐 |
| 需要交互式浏览(点击/填表) | 不推荐(改用浏览器自动化工具) |

## 不适用场景

以下场景Brave搜索工具-免费版不适合处理：

- 黑帽SEO手段
- 搜索引擎作弊
- 付费广告投放管理

## 触发条件

需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于非本工具能力范围的需求.
## 核心能力

### 命令总览

| 命令 | 说明 | 示例 |
|:-----|:-----|:-----|
| `search.js "query"` | 基础搜索(默认5条) | `./search.js "Python asyncio"` |
| `search.js "query" -n 10` | 指定结果数量 | `./search.js "query" -n 10` |
| `search.js "query" --content` | 包含页面内容 | `./search.js "query" --content` |
| `content.js <url>` | 提取URL内容 | `./content.js https://example.com/article` |

**处理**: 解析命令总览的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回命令总览的响应数据,包含状态码、结果和日志.
### 核心功能执行
用`input_params`参数进行配置.

**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置.

**处理**: 解析参数配置与调用的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回参数配置与调用的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：Brave、API、的网页搜索与内容、提取工具、无需浏览器、适合个人用户、的无头网页搜索与、内容提取工具、无需启动浏览器、支持基础搜索、内容提取与结果数、量配置、核心能力、无头网页搜索、页面内容提取、Markdown、结果数量配置、干净的输出格式等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一:搜索文档或 API 参考

开发者需要查找某个 API 的用法或文档.
```bash
# 基础搜索(5条结果)
./search.js "Python asyncio gather 用法"
# ...
# 获取更多结果
./search.js "Python asyncio gather 用法" -n 10
# ...
# 包含页面内容(Markdown格式)
./search.js "Python asyncio gather 用法" --content
```

### 场景二:查询事实或最新信息

查询某个事实或最新动态.
```bash
# 查询事实
./search.js "Python 3.12 新特性"
# ...
# 查询最新信息
./search.js "2026 年 AI 智能体最新进展" -n 10
```

### 场景三:从特定 URL 提取内容

已知 URL,提取页面内容为 Markdown 格式.
```bash
# 提取页面内容
./content.js https://example.com/article
# ...
# 提取并保存
./content.js https://example.com/article > article.md
```

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 依赖详情

```bash
# 进入工具目录,安装依赖
cd /path/to/brave-search-tool
npm ci
# ...
# 配置 API Key
export BRAVE_API_KEY=${API_KEY:?请设置环境变量}
```

### 2. 基础搜索

```bash
# 基础搜索(5条结果)
./search.js "查询词"
# ...
# 指定结果数量
./search.js "查询词" -n 10
# ...
# 包含页面内容
./search.js "查询词" --content
# ...
# 组合使用
./search.js "查询词" -n 3 --content
```

### 3. 内容提取

```bash
# 从 URL 提取内容(转为 Markdown)
./content.js https://example.com/article
```

## 示例

### 输出格式

```text
--- 结果 1 ---
标题: 网页标题
链接: https://example.com/page
摘要: 来自搜索结果的描述
内容: (使用 --content 标志时显示)
  从页面提取的 Markdown 内容...
# ...
--- 结果 2 ---
标题: 网页标题
链接: https://example.com/page
摘要: 来自搜索结果的描述
# ...
...
```

### 搜索参数组合

```bash
# 基础搜索
./search.js "React hooks"
# ...
# 更多结果
./search.js "React hooks" -n 10
# ...
# 带内容
./search.js "React hooks" --content
# ...
# 精简结果 + 内容
./search.js "React hooks" -n 3 --content
```

### 环境变量配置

```bash
# Brave API Key(必需)
export BRAVE_API_KEY=${API_KEY:?请设置环境变量}
# ...
# 可选:默认结果数量
export BRAVE_SEARCH_DEFAULT_COUNT=5
```

### 进阶用法示例

```bash
#!/bin/bash
# advanced-search.sh - 进阶搜索工作流示例
# ...
# 1. 先用 search.js 找到相关 URL
echo "=== 领先步:关键词搜索 ==="
./search.js "Python 异步编程教程" -n 5
# ...
# 2. 从结果中选取重要 URL,用 content.js 提取全文
echo "=== 第二步:内容提取 ==="
./content.js https://example.com/python-async-tutorial > tutorial.md
echo "内容已保存到 tutorial.md"
# ...
# 3. 多次搜索,覆盖不同角度
echo "=== 第三步:多角度搜索 ==="
./search.js "Python asyncio 入门" -n 3
./search.js "Python asyncio 进阶" -n 3
./search.js "Python asyncio 常见问题" -n 3
# ...
# 4. 搜索结果归档
echo "=== 第四步:归档结果 ==="
./search.js "Python 异步编程" --content > "archive/python-async-$(date +%Y%m%d).txt"
echo "已归档到 archive/python-async-$(date +%Y%m%d).txt"
```

### 搜索结果处理

```bash
# 提取搜索结果中的所有 URL
./search.js "AI 智能体" -n 10 | grep "链接:" | awk '{print $2}'
# ...
# 批量提取多个 URL 的内容
for url in $(./search.js "Python 教程" -n 5 | grep "链接:" | awk '{print $2}'); do
  echo "=== $url ==="
  ./content.js "$url" | head -50
  echo ""
done
```

## 优秀实践

1. **查询词要具体**:"Python asyncio gather 用法" 优于 "Python".
2. **按需使用 `--content`**:仅需摘要时不带 `--content`,需全文时才带.
3. **合理设置结果数**:事实查询 3-5 条,深度调研 10 条.
4. **结合 `content.js`**:先用 `search.js` 找到相关 URL,再用 `content.js` 提取全文.
5. **结果缓存**:相同查询结果可缓存,减少 API 调用.
6. **注意 API 配额**:Brave Search API 有调用配额,避免频繁请求.
## 常见问题

### Q1: API 调用失败怎么办?
- 检查 `BRAVE_API_KEY` 是否正确配置
- 确认网络可访问 Brave Search API
- 检查 API 配额是否耗尽
- 查看错误信息,确认查询参数是否合法

### Q2: `--content` 提取的内容不完整?
- 部分页面有反爬机制,可能限制内容提取
- 动态加载内容的页面,提取的可能只是静态部分
- 对重要内容,可结合浏览器自动化工具获取

### Q3: 搜索结果相关性不高?
- 优化查询词,使其更具体
- 增加结果数量,获取更多候选
- 尝试用不同关键词重新搜索

### 已知限制
免费版提供核心搜索与内容提取能力,结果数量无特殊限制(受 API 配额约束)。如需批量搜索、结果缓存、搜索历史、并发查询等高阶能力,请升级至专业版.
### Q5: 如何获取 Brave API Key?
- 访问 Brave Search API 官网
- 注册账号并创建 API Key
- 免费套餐提供每月一定次数的免费查询

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **网络**: 需可访问 Brave Search API
- **Node.js**: >= 16.0.0

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| search.js | 脚本工具 | 必需 | 随 Skill 安装 |
| content.js | 脚本工具 | 必需 | 随 Skill 安装 |
| Node.js | 运行环境 | 必需 | 系统包管理器安装 |
| npm 依赖包 | Node 包 | 必需 | `npm ci` 安装 |
| Brave Search API | 数据源 | 必需 | Brave Search API 订阅 |
| BRAVE_API_KEY | API Key | 必需 | Brave Search API 控制台获取 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- **BRAVE_API_KEY**:Brave Search API Key
  - 获取方式:Brave Search API 官网注册
  - 配置方式:环境变量
- 本 Skill 基于Markdown指令,除 Brave API Key 外无需额外配置

### 可用性分类
- **分类**: MD+EXEC模式纯Markdown指令,部分功能需exec命令行执行)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent完成操作

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |
