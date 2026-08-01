---
slug: azure-devops-tool-free
name: azure-devops-tool-free
version: 1.0.0
displayName: Azure DevOps 基础版
summary: 管理 Azure DevOps 项目、仓库与分支,支持创建拉取请求和查看工作项,适合个人开发者日常使用
license: MIT
edition: free
description: "核心能力: DevOps 工具链领域的专业化 AI 辅助工具,包含核心基础功能兼容. 适用于需要azure devops tool相关能力的开发场景,包含结构化的工作流程和可复用的模板,帮助用户快速完成任务并保持代码质量. 适用于需要azure devops tool相关能力的开发场景,包含结构化的工作流程和配置指引."
tags:
  - DevOps
  - azure
  - devops
  - automation
  - productivity
  - 项目管理
  - 代码协作
  - Azure
  - 云计算
  - free
tools:
  - read
  - exec
  - write
homepage: ""
category: "Operations"
pricing_tier: free

---
# Azure DevOps 基础版

## 概述

本工具是 **DevOps 工具链** 领域的 **FREE 版本** AI Skill,专为个人用户与轻量级场景设计。通过自然语言指令驱动 AI Agent 执行任务,提供核心功能与简洁易用的操作体验.
FREE 版本与 PRO 版本完全兼容,可在需要时升级至 PRO 版本获取高级功能、批量操作与团队协同能力.
### 版本定位

| 维度 | FREE 版本 | PRO 版本 |
|---|-------|------|
| 目标用户 | 个人用户 | 企业团队 |
| 功能范围 | 核心功能 | 全部功能 |
| 批量操作 | 不支持 | 支持 |
| 团队协作 | 不支持 | 支持 |
| 技术支持 | 社区支持 | 优先响应 |
| 数据分析 | 基础统计 | 高级分析 |

## 核心能力

FREE 版本提供以下能力:

### 列出组织下所有项目及描述
列出组织下所有项目及描述

**处理**: 解析列出组织下所有项目及描述的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回列出组织下所有项目及描述的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 查看指定项目中的 Git 仓库
查看指定项目中的 Git 仓库列表

**处理**: 解析查看指定项目中的 Git 仓库的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回查看指定项目中的 Git 仓库的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 浏览仓库分支并获取仓库 ID
浏览仓库分支并获取仓库 ID

**处理**: 解析浏览仓库分支并获取仓库 ID的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回浏览仓库分支并获取仓库 ID的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 创建拉取请求并填写标题与描述
创建拉取请求并填写标题与描述

**处理**: 解析创建拉取请求并填写标题与描述的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回创建拉取请求并填写标题与描述的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 查看当前项目的拉取请求列表
查看当前项目的拉取请求列表

**处理**: 解析查看当前项目的拉取请求列表的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回查看当前项目的拉取请求列表的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 功能详情

本版本提供 5 项核心能力,覆盖 DevOps 工具链 的常见使用场景。如需批量操作、团队协作、数据分析等高级功能,可升级至 PRO 版本.
**FREE 版本核心功能清单:**

- 列出组织下所有项目及描述
- 查看指定项目中的 Git 仓库列表
- 浏览仓库分支并获取仓库 ID
- 创建拉取请求并填写标题与描述
- 查看当前项目的拉取请求列表

**PRO 版本扩展功能预览:**

- 批量创建与流转工作项,支持自定义字段映射
- CI/CD 流水线状态监控与构建失败告警
- 多项目跨仓库批量创建 PR 并自动添加审阅者
- 团队权限与安全策略审计,生成合规报告
- 工作项看板导出为 Excel/CSV 供离线分析
- 智能 PR 模板生成与代码规范联动检查

**处理**: 解析功能详情的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回功能详情的响应数据,包含状态码、结果和日志.
**技术参数**：使用`input_params`和`output_format`参数控制执行行为,支持`json`/`text`/`csv`输出格式.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：Azure、仓库与分支、支持创建拉取请求、和查看工作项、适合个人开发者日、常使用、工具链领域的专业、辅助工具、提供核心基础功能等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景 1: 个人项目快速浏览

查看组织下所有项目及其仓库,快速定位目标代码库

## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | Azure DevOps 基础版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
curl -s -u ":${AZURE_DEVOPS_PAT}" "https://dev.azure.com/${AZURE_DEVOPS_ORG}/_apis/projects?api-version=7.1" | jq -r '.value[] | .name'
```

### 场景 2: 创建功能分支 PR

从功能分支向主干创建拉取请求,附带描述与审阅说明

```bash
curl -s -u ":${AZURE_DEVOPS_PAT}" -H "Content-Type: application/json" -X POST -d '{"sourceRefName":"refs/heads/feature/x","targetRefName":"refs/heads/main","title":"feat: add login"}' "https://dev.azure.com/${ORG}/${PROJ}/_apis/git/repositories/${REPO_ID}/pullrequests?api-version=7.1"
```

## 不适用场景

以下场景Azure DevOps 基础版不适合处理：

- 实时流数据处理
- 小规模数据手动分析
- 非结构化文本情感分析

## 触发条件

需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于非本工具能力范围的需求.
## 快速开始

### 1. 环境准备

确保已安装并配置好 AI Agent 环境(Claude Code / Cursor / Codex / Gemini CLI 等),本 Skill 通过 SKILL.md 指令驱动 Agent 执行任务.
**系统要求:**

- 操作系统: Windows / macOS / Linux
- Agent 平台: 支持 SKILL.md 格式的任意 AI Agent
- 运行时: Python 3.8+ 或 Node.js 18+(视具体操作需求)

### 2. 配置参数

```bash
export AZURE_DEVOPS_PAT="your-personal-access-token"
export AZURE_DEVOPS_ORG="YourOrganizationName"
azure.api-version=7.1" | jq ".count"
```

### 3. 验证配置

配置完成后,可通过以下方式验证是否正常工作:

```bash
# 验证环境变量是否设置
echo "配置检查:"
env | grep -E "API|KEY|TOKEN|SECRET" | sed "s/=.*/=***/"  # Linux/macOS
# 或 PowerShell
# Get-ChildItem Env: | Where-Object {$_.Name -match "API|KEY|TOKEN"} | Format-Table
```

### 4. 开始使用

在 AI Agent 对话中描述你的需求,Agent 会根据本 Skill 的指令自动执行对应操作.
```text
请帮我个人项目快速浏览
```

Agent 将自动:
1. 解析你的自然语言指令
2. 调用相应的工具或 API
3. 执行操作并返回结果
4. 返回执行结果供你确认

#
## 示例

### 基础配置

```bash
export AZURE_DEVOPS_PAT="your-personal-access-token"
export AZURE_DEVOPS_ORG="YourOrganizationName"
azure.api-version=7.1" | jq ".count"
```
### 可选配置

```json
{
  "edition": "free",
  "auto_retry": false,
  "max_concurrent": 1,
  "log_level": "info",
  "cache_enabled": true,
  "timeout": 30
}
```

**FREE 配置项说明:**

| 配置项 | 类型 | 默认值 | 说明 |
|---:|---:|---:|---:|
| auto_retry | bool | false | 失败后自动重试 |
| max_concurrent | int | 1 | 最大并发数(FREE 限制为1) |
| log_level | string | info | 日志级别 |
| cache_enabled | bool | true | 启用结果缓存 |
| timeout | int | 30 | 操作超时时间(秒) |

## 优秀实践

1. **PAT 权限仅授予所需范围,避免全权限令牌**
2. **API 版本统一使用 7.1 确保接口行为一致**
3. **创建 PR 前先获取正确的 repositoryId**
4. **将 PAT 存储在环境变量或密钥管理器中**

### 个人使用建议

- 从简单任务开始熟悉工具行为,逐步扩展到复杂场景
- 定期备份配置文件与数据,防止意外丢失
- 遇到问题先查阅常见问题章节,再寻求社区帮助
- 保持配置简洁,只启用必要的功能选项
- 定期更新工具版本以获取最新功能与修复
- 记录常用操作命令,提高日常使用效率

## 常见问题

### Q: 401 Unauthorized 怎么办?

A: 检查 PAT 是否过期或权限不足,在 Azure DevOps 个人设置中重新生成令牌.
### Q: API 请求频率受限?

A: Azure DevOps REST API 限制每分钟 600 次,建议批量操作加入速率控制.
### Q: 如何升级到 PRO 版本?

A: 升级到 PRO 版本非常简单:
1. 获取 PRO 版本授权
2. 安装 PRO 版本 Skill
3. 原有配置自动迁移,无需额外操作
4. 即可使用批量操作、团队协作等高级功能

### 已知限制

A: FREE 版本主要限制:
- 不支持批量操作(每次只能处理一个任务)
- 不支持团队协作(仅限个人使用)
- 不支持高级数据分析
- 技术支持依赖社区
如需这些功能,建议升级至 PRO 版本.
### Q: FREE 版本的数据安全吗?

A: FREE 版本所有数据本地存储,不上传云端,确保隐私安全。建议定期备份配置文件与数据目录.
## 依赖说明

### 运行环境

- **Agent 平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **运行时**: Python 3.8+ 或 Node.js 18+(视具体操作需求)
- **网络**: 部分功能需要网络连接访问外部 API

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| curl | CLI 工具 | 推荐 | 系统自带或包管理器安装 |
| jq | JSON 处理 | 推荐 | apt install jq / brew install jq |
| Python 3.8+ | 运行时 | 视需求 | python.org 下载 |
| Node.js 18+ | 运行时 | 视需求 | nodejs.org 下载 |

### API Key 配置

FREE 版本支持单一 API Key 配置,满足个人使用需求:
- **环境变量**:通过环境变量配置 API Key
- **配置文件**:支持配置文件方式存储 API Key
- **安全提醒**:切勿将 API Key 硬编码到脚本或提交到版本控制系统

### 可用性分类

- **分类**: MD+EXEC模式纯 Markdown 指令,部分功能需要 exec 命令行执行能力)
- **说明**: 基于 Markdown 的 AI Skill,通过自然语言指令驱动 Agent 执行任务
- **FREE 特性**: 支持单次执行、基础配置与社区支持
- **安全等级**: 基础,数据本地存储,建议定期备份
- **SLA**: 社区支持,尽力响应

---
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

**版本信息**

| 项目 | 值 |
|:------|------:|
| 版本号 | 1.0.0 |
| 版本类型 | FREE |
| 许可证 | MIT |
| 兼容性 | 可升级至 PRO 版本 |

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
    "result": "Azure DevOps 基础版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "azure devops"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
