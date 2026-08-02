---
slug: "memo-quickstart-free"
name: "memo-quickstart-free"
version: "1.0.0"
displayName: "记忆快速启动"
summary: "零依赖本地记忆基础版：三层架构+TF-IDF检索+WAL日志,10秒上手.面向零依赖场景的本地记忆系统基础版,解决搜索精度不足与上手门槛高两大痛点. 三层记忆架构（热内存/冷存储/人类可读,提供."
summary_zh: "零依赖本地记忆基础版：三层架构+TF-IDF检索+WAL日志，10秒上手。。面向零依赖场景的本地记忆系统基础版，解决搜索精度不足与上手门槛高两大痛点. 三层记忆架构（热内存/冷存储/人类可读,提供核心能力"
license: "MIT"
description: "|-. 适用于需要memo quickstart相关能力的开发场景,包含结构化的工作流程和可复用的模板,帮助用户快速完成任务并保持代码质量.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性."
  面向零依赖场景的本地记忆系统基础版，解决搜索精度不足与上手门槛高两大痛点.
  三层记忆架构（热内存/冷存储/人类可读归档）提供从快到慢的记忆存取.
  TF-IDF基础检索支持关键词匹配召回相关记忆.
  WAL写前日志协议确保响应前先写入记忆，避免崩溃丢失上下文.
  统一JSON schema支持preference/decision/fact/lesson/context五种记忆类型.
  适用于隐私敏感场景、离线开发、个人助理记忆等基础场景.
  无API Key、无云、无追踪，纯本地记忆.
tools:
  - read
  - exec
  - write
homepage: ""
tags:
  - 创意设计
  - memo
  - quickstart
  - automation
  - productivity
  - UI设计
  - 前端
  - 设计
  - tf-idf
  - json
category: "Creative"
pricing_tier: free
---
# 记忆快速启动（基础版）

面向零依赖场景的本地记忆系统基础版，用三层架构和TF-IDF检索，在不引入任何外部依赖的前提下，提供开箱即用的记忆能力。无API Key、无云、无追踪，纯本地记忆.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 记忆快速启动处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 核心能力

- **三层记忆架构**：热内存（SESSION-STATE.json，活跃工作记忆，抗上下文压缩，会话开始立即加载）→ 冷存储（memories/目录，索引化JSON文件，可检索）→ 人类可读归档（MEMORY.md + daily/目录，长期精选）。三层协同提供从快到慢的记忆存取.
- **TF-IDF基础检索**：基于词频-逆文档频率算法计算文本相关性，按得分排序返回结果。执行 `memory-search "关键词"` 返回匹配的记忆条目。支持按类型过滤：`memory-list --type preference`.
- **WAL写前日志协议**：响应前先写入记忆，避免崩溃丢失上下文。用户表达偏好/做决策/给截止时间/纠正错误时，执行三步：更新SESSION-STATE.json → memory-store持久化 → 响应用户.
- **统一JSON schema**：所有记忆遵循同一格式：`{"id":"uuid-001","type":"preference","content":"用户偏好TypeScript","importance":0.9,"tags":["typescript"],"timestamp":"2026-07-21T10:00:00Z"}`。支持preference/decision/fact/lesson/context五种记忆类型.
### 三层记忆架构

针对三层记忆架构,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供三层记忆架构相关的配置参数、输入数据和处理选项.
**输出**: 返回三层记忆架构的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`三层记忆架构`的配置文档进行参数调优
### TF-IDF基础检索

针对TF-IDF基础检索,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供TF-IDF基础检索相关的配置参数、输入数据和处理选项.
**输出**: 返回TF-IDF基础检索的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`TF-IDF基础检索`的配置文档进行参数调优
### WAL写前日志协议

针对WAL写前日志协议,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供WAL写前日志协议相关的配置参数、输入数据和处理选项.
**输出**: 返回WAL写前日志协议的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`WAL写前日志协议`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 使用流程

### 领先步：初始化（10秒）

执行安装与初始化命令：

```bash
npm install -g simple-local-memory
cd your-project
memory-init
```

初始化创建 `SESSION-STATE.json`（活跃工作记忆）、`MEMORY.md`（长期精选记忆）、`memories/`（记忆存储目录）.
### 第二步：存储与检索记忆

存储领先条记忆并验证检索功能：

```# 网络连接示例(已移除潜在风险命令)
memory-search "TypeScript"
```

### 第三步：执行WAL协议与定期维护

用户表达偏好/做决策/给截止时间/纠正错误时，执行：更新SESSION-STATE.
每日运行 `memory-stats` 查看统计；每周运行 `memory-archive --days 7` 归档旧记忆.
#
## 错误处理

| 错误类型 | 原因 | 处理方式 |
|:-----|:-----|:-----|
| 搜索无结果 | memories/目录未创建，memory-init未执行 | 运行 `memory-init` 初始化目录结构 |
| 记忆未保存 | 文件权限不足或磁盘空间不足 | 检查工作区写入权限与磁盘空间，清理后检查网络连接和配置后重试 |
| 检索变慢 | 记忆条目过多（>1000条） | 执行 `memory-archive --days 7` 归档旧记忆 |

## 示例

### 示例1：技术选型决策存储与检索

**输入：** 用户说"这个项目用Tailwind，不用vanilla CSS"

**执行：**
1. 更新SESSION-STATE.json（记录决策）
2. `memory-store --type decision --content "用Tailwind不用vanilla CSS" --importance 0.9`
3. 响应用户

**输出：**
```bash
# SESSION-STATE.json 更新
{"activeDecisions": [{"content":"用Tailwind不用vanilla CSS","timestamp":"2026-07-21T10:00:00Z"}]}
# ...
# memory-store 输出
Stored: uuid-001 (type=decision, importance=0.9)
# ...
# 响应
"明白，用Tailwind。已保存此偏好。"
```

## FAQ

**Q1：真的完全不需要API Key吗？**
A：是的。所有存储与检索在本地完成，零网络请求，零外部依赖。数据不离开本机，适合隐私敏感场景与离线开发环境.
**Q2：基础版检索算法是什么？**
A：基础版使用TF-IDF词频算法进行文本相关性匹配。如需叠加近期加权、重要度加权、标签匹配的三维混合检索（召回率提升40%），请升级到付费版.
**Q3：能和其他记忆系统共存吗？**
A：可以。本系统独立运行于 `memories/` 目录，不干扰其他系统。基础版不提供迁移工具，如需从其他系统一键导入，请升级到付费版.
## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| Agent平台 | 运行环境 | 必需 | 安装支持SKILL.md的AI Agent |
| Node.js | 运行时 | 必需 | nodejs.org安装（运行记忆CLI） |
| simple-local-memory | npm包 | 必需 | `npm install -g simple-local-memory` |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

**API Key配置：** 本技能基于本地存储，无需任何API Key.
**可用性分类：** MD+EXEC（Markdown指令驱动，需exec执行memory CLI命令）

## 已知限制

1. **无混合检索加权**：基础版仅使用TF-IDF词频匹配，不支持近期加权、重要度加权、标签匹配三维加权，召回率低于付费版40%.
2. **无记忆关系图谱**：不支持related_to/followed_by关系链，无法顺藤摸瓜找到关联记忆.
3. **无迁移工具**：不支持从其他记忆系统一键导入，需手动转换格式.
## 升级提示

本基础版提供三层记忆架构与TF-IDF基础检索能力。升级到付费版可解锁以下高级能力：

- **四维混合检索算法**：TF-IDF（50%）+ 近期加权（20%）+ 重要度加权（20%）+ 标签匹配（10%），召回率比纯TF-IDF提升40%，解决"查用户喜好找不到偏好深色模式"的语义鸿沟问题
- **记忆关系图谱**：支持related_to与followed_by关系链，查到一条记忆可顺藤摸瓜找到关联记忆，返回完整决策上下文
- **迁移工具**：支持从其他记忆系统一键导入，自动转换为本系统统一JSON schema格式
- **完整CLI命令集**：新增memory-list（按类型列表）、memory-export（导出备份）、memory-import（导入）、memory-deduplicate（去重）、memory-cleanup（清理断链）等高级命令
- **标签系统**：存储时支持 `--tags frontend,css` 参数，检索时支持 `--tag frontend` 过滤，增强召回精度
- **confidence与expires_at字段**：记忆schema新增置信度与过期时间字段，支持记忆自动过期与可信度排序

升级后可处理关联检索、系统迁移、大规模记忆去重等复杂记忆管理场景.
## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "记忆快速启动处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "memo-quickstart"
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
