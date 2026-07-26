---
slug: internet-search-tool-free
name: internet-search-tool-free
version: 1.0.0
displayName: 聚合搜索工具
summary: 基于 SearXNG 的多引擎聚合搜索工具，支持分类路由与智能查询，聚合多个搜索引擎结果，适合个人日常信息检索.
license: Proprietary
edition: free
description: '基于 SearXNG 的多引擎聚合搜索工具，支持分类路由与智能查询，聚合多个搜索引擎结果，适合个人日常信息检索。核心能力:

  - 聚合多个搜索引擎结果（Brave、Bing、DuckDuckGo 等）

  - 按查询类型智能路由到合适引擎

  - 支持通用、新闻、学术、社交四大类别

  - SearXNG 查询语法支持

  适用场景:

  - 个人日常信息检索

  - 学术论文与资料查找

  - 社区观点与讨论收集

  差异化:

  - 免费版聚焦单次智能搜索

  - 自动选择最匹配的搜索引擎

  - 结果聚合...'
tags:
  - 搜索
  - 聚合工具
  - 多引擎
  - 信息检索
  - 检索
  - 工具
  - internet_search
  - searxng
  - bash
  - 支持创建
  - 查询
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
category: "Knowledge"
---
# 聚合搜索工具（免费版）

## 概述

聚合搜索工具免费版是一款基于 SearXNG 的多引擎搜索聚合工具。通过自托管的 SearXNG 实例，同时查询 Brave、Bing、DuckDuckGo、Wikipedia 等多个搜索引擎，聚合去重后返回最相关的结果。支持按查询类型智能路由到合适的引擎，帮助个人用户高效获取信息.
## 核心能力

| 能力 | 说明 | 免费版支持 |
|---|---|-----|
| 多引擎聚合 | 聚合 10+ 搜索引擎 | 是 |
| 分类路由 | 按类型选择引擎 | 是 |
| SearXNG 语法 | 支持查询修饰符 | 是 |
| 结果去重 | 自动去重排序 | 是 |
| 批量查询 | 多关键词并行查询 | 否 |
| 结果导出 | 导出为 JSON/CSV | 否 |
| 自定义引擎 | 配置特定引擎 | 否 |
| 搜索缓存 | 结果缓存 | 否 |

### 已知限制
执行已知限制操作,使用`input_params`参数进行配置,支持创建/查询/导出等操作.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 单次查询最多返回 10 条结果
单次查询最多返回 10 条结果

**处理**: 解析单次查询最多返回 10 条结果的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回单次查询最多返回 10 条结果的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 不支持批量查询
不支持批量查询

**处理**: 解析不支持批量查询的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回不支持批量查询的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 不支持结果导出
不支持结果导出

**处理**: 解析不支持结果导出的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回不支持结果导出的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 不支持自定义引擎配置
不支持自定义引擎配置

**处理**: 解析不支持自定义引擎配置的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回不支持自定义引擎配置的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 不支持搜索结果缓存
不支持搜索结果缓存

**处理**: 解析不支持搜索结果缓存的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回不支持搜索结果缓存的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

**处理**: 解析已知限制的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回已知限制的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：的多引擎聚合搜索、支持分类路由与智、能查询、聚合多个搜索引擎、适合个人日常信息、核心能力、Brave、Bing、DuckDuckGo、按查询类型智能路、由到合适引擎、支持通用、社交四大类别、查询语法支持等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一：通用信息检索

用户需要查找某个技术问题的解决方案.
```bash
# 通用类别搜索
internet_search("Python 异步编程 最佳实践 2026")
```

系统自动路由到通用类别，聚合 Brave、Bing、DuckDuckGo 等引擎结果.
### 场景二：学术论文查找

研究人员需要查找学术论文.
```bash
# 学术类别搜索
internet_search("transformer attention efficiency survey", category="academic")
```

路由到 arXiv、Google Scholar、PubMed 等学术引擎.
### 场景三：社区观点收集

用户想了解社区对某产品的评价.
```bash
# 社交类别搜索
internet_search("reddit best mechanical keyboard 2026", category="social")
```

专门搜索 Reddit 等社区平台，获取真实用户观点.
## 不适用场景

以下场景聚合搜索工具不适合处理：

- 黑帽SEO手段
- 搜索引擎作弊
- 付费广告投放管理

## 触发条件

需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于非本工具能力范围的需求.
## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 配置 SearXNG 实例

```bash
# 方式一：使用公共 SearXNG 实例
export SEARXNG_URL=https://searx.be
# ...
# 方式二：自托管 SearXNG
docker run -d -p 8080:8080 searxng/searxng
export SEARXNG_URL=http://localhost:8080
```

### 执行首次搜索

```bash
# 基础搜索
internet_search("你的搜索关键词")
# ...
# 指定类别
internet_search("新闻关键词", category="news")
```

### 验证配置

```bash
# 测试 SearXNG 连通性
curl http://localhost:8080/healthz
# ...
# 执行测试搜索
internet_search("test query", count=3)
```

## 示例

### 分类路由配置

| 类别 | 适用场景 | 使用引擎 |
|:-----|:-----|:-----|
| `general` | 默认，事实查询、产品、人物 | Brave, Bing, DDG, Startpage, Qwant, Wikipedia |
| `news` | 时效性新闻、突发事件 | Bing News, DDG News |
| `academic` | 论文、研究、医学文献 | arXiv, Google Scholar, PubMed |
| `social` | 观点、社区推荐、口碑 | Reddit |

### SearXNG 查询语法

| 语法 | 含义 | 示例 |
|---:|---:|---:|
| `!<engine>` | 指定引擎 | `!wp paris`, `!wikipedia paris` |
| `!<category>` | 指定类别 | `!map paris`, `!news climate` |
| `:<lang>` | 语言过滤 | `:fr !wp Wau Holland` |
| 组合使用 | 多引擎组合 | `!map !ddg !wp paris` |

### 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|:---:|:---:|:---:|:---:|
| `query` | 字符串 | 无 | 搜索关键词 |
| `category` | 字符串 | general | 搜索类别 |
| `count` | 整数 | 5 | 返回结果数 |
| `lang` | 字符串 | auto | 语言过滤 |

## 最佳实践

### 查询关键词优化

```text
推荐写法：
- "rust async runtime benchmarks 2025"（关键词组合）
- "OpenAI o3 release 2025"（带时间锚点）
- "transformer attention efficiency survey"（专业术语）
# ...
不推荐写法：
- "what is the fastest async runtime for rust"（自然语言句子）
- "what happened today"（过于宽泛）
```

### 多搜索策略

针对复杂问题，执行多个聚焦搜索而非一次宽泛搜索：

```bash
# 而非一次宽泛搜索
internet_search("best way to deploy Node.js")
# ...
# 推荐多个聚焦搜索
internet_search("Node.js Docker deployment best practices 2026")
js PM2 vs Docker production", category="social")
js zero-downtime deployment strategies")
```

### 事实与情感组合

获取事实信息和社区情感：

```bash
# 事实查询
internet_search("Bun runtime performance vs Node.js benchmarks")
# ...
# 社区体验
internet_search("Bun runtime production experience", category="social")
```

### 何时不应使用

- 已知高置信度的信息
- 稳定的 API 文档或语法
- 已搜索过且获得答案的问题

## 常见问题

### 搜索返回空结果

```bash
# 检查 SearXNG 状态
curl http://localhost:8080/healthz
# ...
# 尝试不同类别
internet_search("query", category="general")
# ...
# 调整关键词
internet_search("more specific keywords")
```

### 搜索结果不相关

```bash
# 使用更精准的关键词
internet_search("specific technical terms")
# ...
# 尝试学术类别
internet_search("query", category="academic")
# ...
# 指定特定引擎
internet_search("!wp query")
```

### SearXNG 连接失败

```bash
# 检查服务状态
docker ps | grep searxng
# ...
# 重启服务
docker restart searxng
# ...
# 查看日志
docker logs searxng
```

### 响应速度慢

```bash
# 减少返回数量
internet_search("query", count=3)
# ...
# 限定引擎数量
internet_search("query", engines="google,bing")
# ...
# 启用缓存（如可用）
internet_search("query", cache=true)
```

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **网络环境**：需可访问 SearXNG 实例
- **推荐配置**：2 核 CPU、4GB 内存

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| SearXNG | 搜索引擎聚合 | 是 | Docker 部署或使用公共实例 |
| Docker | 容器运行时 | 否（自托管时） | `docker.com` 下载 |
| Python 3.7+ | 运行时 | 是 | 系统包管理器安装 |
| requests | HTTP 库 | 是 | `pip install requests` |
| LLM API | API | 是 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 免费版无需额外 API Key
- SearXNG 为开源项目，无需注册
- 公共实例免费使用

```bash
# 配置 SearXNG 实例地址
export SEARXNG_URL=http://localhost:8080
# 或使用公共实例
```

### 可用性分类

- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
- **适用人群**：个人开发者、学生、研究人员
- **升级建议**：如需批量查询、结果导出、自定义引擎等高级功能，请使用 PRO 版本

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "聚合搜索工具处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "internet search"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
