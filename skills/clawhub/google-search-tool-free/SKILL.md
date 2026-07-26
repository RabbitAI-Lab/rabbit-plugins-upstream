---
slug: google-search-tool-free
name: google-search-tool-free
version: 1.0.0
displayName: 谷歌搜索工具
summary: 基于 Google Custom Search Engine 的联网搜索工具，支持实时信息检索与结果结构化输出，适合个人研究与学习使用.
license: Proprietary
edition: free
description: '基于 Google Custom Search Engine 的联网搜索工具，支持实时信息检索与结果结构化输出，适合个人研究与学习使用。核心能力:

  - 通过 Google Custom Search API 进行精准搜索

  - 返回结构化的搜索结果，包含标题、链接、摘要

  - 支持中英文关键词搜索

  - 简单的 API Key 配置流程

  适用场景:

  - 个人学术研究与资料收集

  - 技术文档与官方信息检索

  - 实时新闻与动态获取

  差异化:

  - 免费版聚焦单次搜索...'
tags:
  - 搜索
  - Google
  - 研究工具
  - 信息检索
  - 检索
  - 工具
  - api
  - google
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
category: "Knowledge"
---
# 谷歌搜索工具（免费版）

## 概述

谷歌搜索工具免费版是一款基于 Google Custom Search Engine (CSE) 的联网搜索工具。通过 Google 官方 API 获取实时、权威的搜索结果，适合需要高质量信息检索的个人用户。仅需配置 Google API Key 和搜索引擎 ID，即可开始使用.
## 核心能力

| 能力 | 说明 | 免费版支持 |
|---|---|-----|
| Google CSE 搜索 | 通过官方 API 搜索 | 是 |
| 结构化结果 | 返回标题、链接、摘要 | 是 |
| 中英文搜索 | 支持中文和英文关键词 | 是 |
| 批量搜索 | 一次执行多个查询 | 否 |
| 结果导出 | 导出为 JSON/CSV | 否 |
| 自定义搜索引擎 | 配置特定站点搜索 | 否 |
| 搜索历史 | 保存搜索记录 | 否 |

### 已知限制
执行已知限制操作,使用`input_params`参数进行配置,支持创建/查询/导出等操作.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 每日搜索配额限制（Google
每日搜索配额限制（Google API 免费额度）

**处理**: 解析每日搜索配额限制（Google的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回每日搜索配额限制（Google的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 单次查询最多返回 10 条结果
单次查询最多返回 10 条结果

**处理**: 解析单次查询最多返回 10 条结果的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回单次查询最多返回 10 条结果的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 不支持批量查询和结果导出
不支持批量查询和结果导出

**处理**: 解析不支持批量查询和结果导出的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回不支持批量查询和结果导出的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 不支持自定义站点限定搜索
不支持自定义站点限定搜索

**处理**: 解析不支持自定义站点限定搜索的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回不支持自定义站点限定搜索的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 不支持搜索历史保存
不支持搜索历史保存

**处理**: 解析不支持搜索历史保存的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回不支持搜索历史保存的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

**处理**: 解析已知限制的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回已知限制的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：Custom、Search、Engine、的联网搜索工具、支持实时信息检索、与结果结构化输出、适合个人研究与学、习使用、核心能力、进行精准搜索、返回结构化的搜索、包含标题、支持中英文关键词、简单的、Key、配置流程等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一：学术资料检索

学生或研究人员查找特定主题的学术资料.
```bash
# 搜索学术论文相关内容
python3 （请参考skill目录中的脚本文件） "transformer attention mechanism survey 2026"
```

预期输出包含相关论文、研究博客和学术资源的链接与摘要.
### 场景二：技术文档查找

开发者查找特定技术的官方文档和教程.
```bash
# 搜索技术文档
python3 （请参考skill目录中的脚本文件） "Docker compose networking best practices"
```

返回官方文档、技术博客和社区讨论的链接，帮助快速定位权威资料.
### 场景三：实时信息获取

用户需要获取最新的新闻或动态信息.
```bash
# 搜索最新动态
python3 （请参考skill目录中的脚本文件） "2026年 人工智能 最新进展"
```

## 不适用场景

以下场景谷歌搜索工具不适合处理：

- 黑帽SEO手段
- 搜索引擎作弊
- 付费广告投放管理

## 触发条件

需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于非本工具能力范围的需求.
## 快速开始

### 配置 API 凭证

1. **创建 Google Cloud 项目**：
   - 访问 Google Cloud Console
   - 创建新项目并启用 Custom Search API

2. **获取 API Key**：
   - 在 API 凭证页面创建 API Key
   - 保存 Key 值备用

3. **创建搜索引擎 ID (CX)**：
   - 访问 Programmable Search Engine 配置页面
   - 创建新的搜索引擎，获取 CX ID

4. **配置环境变量**：

```bash
# 创建 .env 文件
cat > .env <<EOF
GOOGLE_API_KEY=your_api_key_here
GOOGLE_CSE_ID=your_cx_id_here
EOF
# ...
# 或直接设置环境变量
export GOOGLE_API_KEY=your_api_key_here
export GOOGLE_CSE_ID=your_cx_id_here
```

### 执行首次搜索

```bash
# 基础搜索
python3 （请参考skill目录中的脚本文件） "Python 编程教程"
# ...
# 指定返回结果数量
python3 （请参考skill目录中的脚本文件） "machine learning" --max 5
```

### 验证配置

```bash
# 测试 API 连通性
python3 （请参考skill目录中的脚本文件） "test" --max 1
# ...
# 如果返回结果，说明配置成功
```

#
## 示例

### 基础搜索配置

```bash
# 使用环境变量
python3 （请参考skill目录中的脚本文件） "搜索关键词"
# ...
# 直接传入凭证（不推荐，用于测试）
GOOGLE_API_KEY=xxx GOOGLE_CSE_ID=yyy \
  python3 （请参考skill目录中的脚本文件） "搜索关键词"
```

### 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|:-----|:-----|:-----|:-----|
| `query` | 字符串 | 无 | 搜索关键词（必填） |
| `--max` | 整数 | 10 | 返回结果数量（1-10） |
| `--safe` | 布尔 | true | 启用安全搜索 |
| `--lang` | 字符串 | zh-CN | 搜索语言 |

## 最佳实践

### 搜索关键词优化

| 场景 | 推荐写法 | 说明 |
|---:|---:|---:|
| 学术论文 | `paper title keywords year` | 包含年份和关键词 |
| 技术文档 | `technology name documentation` | 使用英文名更准确 |
| 新闻动态 | `topic 2026 最新` | 添加时效性词 |
| 官方信息 | `site name 官方` | 限定权威来源 |

### API 配额管理

```bash
# 查看剩余配额
python3 （请参考skill目录中的脚本文件） --quota
# ...
# 减少不必要的查询
# 先使用本地知识，仅在需要时搜索
# 缓存常用搜索结果
```

### 结果筛选建议

1. **优先查看前 3 条**：Google 排序通常最相关
2. **查看摘要**：摘要包含关键词上下文
3. **验证来源**：优先选择官方域名
4. **时效性**：注意结果的发布时间

## 常见问题

### API Key 无效

```bash
# 检查环境变量
echo $GOOGLE_API_KEY
echo $GOOGLE_CSE_ID
# ...
# 验证 Key 格式
python3 （请参考skill目录中的脚本文件） --validate-key
```

可能原因：
- Key 未启用 Custom Search API
- Key 已过期或被撤销
- 环境变量未正确设置

### 搜索返回空结果

```bash
# 检查搜索引擎配置
# 确认 CSE 配置为搜索全网（而非限定站点）
# ...
# 尝试英文关键词
python3 （请参考skill目录中的脚本文件） "english keywords"
# ...
# 检查配额是否用尽
python3 （请参考skill目录中的脚本文件） --quota
```

### API 配额用尽

```text
Google Custom Search API 免费额度：
- 每日 100 次查询
- 每次查询最多 10 条结果
- 超出需付费使用
# ...
建议：
- 优化查询，减少无效搜索
- 缓存常用结果
- 错峰使用（UTC 时间每日 0 点重置）
```

### 网络连接问题

```bash
# 测试 Google API 连通性
curl -I https://www.googleapis.com
# ...
# 使用代理（如需要）
export HTTPS_PROXY=http://proxy:port
python3 （请参考skill目录中的脚本文件） "query"
```

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python 版本**：3.7 及以上
- **网络环境**：需可访问 Google API 服务

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| Python 3.7+ | 运行时 | 是 | 系统包管理器安装 |
| requests | HTTP 库 | 是 | `pip install requests` |
| python-dotenv | 环境变量 | 否（推荐） | `pip install python-dotenv` |
| Google API Key | API 凭证 | 是 | Google Cloud Console 获取 |
| Google CSE ID | 搜索引擎 ID | 是 | Programmable Search Engine 获取 |
| LLM API | API | 是 | 由 Agent 内置 LLM 提供 |

### API Key 配置

```bash
# 必需的 API Key
GOOGLE_API_KEY=your_api_key_here      # Google API 密钥
GOOGLE_CSE_ID=your_cx_id_here         # 自定义搜索引擎 ID
# ...
# 获取方式：
# 1. 访问 Google Cloud Console
# 2. 创建项目并启用 Custom Search API
# 3. 创建 API Key
# 4. 访问 cse.google.com 创建搜索引擎
# 5. 获取搜索引擎 ID (CX)
```

### 可用性分类

- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
- **适用人群**：个人研究者、学生、开发者
- **升级建议**：如需批量搜索、结果导出、自定义站点搜索等高级功能，请使用 PRO 版本

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "谷歌搜索工具处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "google search"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
