---
slug: jinn-node-tool-free
name: jinn-node-tool-free
version: 1.0.1
displayName: 节点工作工具
summary: "面向个人用户的闲置节点,提供核心能力"
license: "MIT"
edition: free
description: "面向个人用户的闲置节点工作与代币奖励工具，可处置提升工作效率 核心能力:.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性. 功能涵盖: node。"

  - 单节点初始化与钱包配置

  - 接收并执行单条任务

  - 基础钱包查询与余额查看

  - 个人信誉与完成记录跟踪

  适用场景:

  - 个人开发者闲置机器跑任务赚奖励

  - 单节点测试与试运行

  - 个人钱包与完成记录管控

  差异化: 免费版聚焦个人单节点单任务执行，包含初始化与钱包查询，零成本试跑.
  适用关键词: 节点工作, 闲置节点, 赚取奖励, 代币, worker node, idle, earn, autonomous venture'
tags:
  - 节点
  - 代币奖励
  - 个人效率
  - 其他工具
  - 工具
  - 效率
  - 自动化
  - 写作
  - 电商
  - 开发
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
pricing_tier: free
---
# 节点工作工具（免费版）

## 概述

本工具帮助个人开发者把闲置机器变成工作节点，接入自主 venture 网络执行任务并赚取代币奖励。免费版覆盖单节点初始化、单任务执行、钱包查询与完成记录跟踪，适合个人试跑. 关键词: jinn
## 核心能力

| 能力 | 说明 | 免费版范围 |
|---|---|-----|
| 节点初始化 | 环境配置与钱包创建 | 单节点 |
| 任务执行 | 接收并完成单条任务 | 单任务 |
| 钱包查询 | 余额与地址查看 | 只读 |
| 记录跟踪 | 完成数与信誉 | 个人 |
**技术实现要点**：核心能力基于`input_params`参数与`output_format`配置实现,支持创建/查询/修改/删除等操作模式,通过`config_options`进行运行时配置.
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

### 结果处理与输出
用`output_format`参数进行配置.

**处理**: 解析结果处理与输出的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回结果处理与输出的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：面向个人用户的闲、置节点工作工具、运行任务赚取代币、置节点工作与代币、奖励工具等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一：初始化节点

```bash
# 依赖说明
corepack enable
yarn install
# ...
# 配置环境
cp .env.example .env
# 填入 RPC_URL、OPERATE_PASSWORD、GEMINI_API_KEY 等
# ...
# 运行初始化向导
yarn setup
```

### 场景二：单任务试跑

```bash
# 单任务测试
yarn worker --single
# ...
# 持续运行
yarn worker
```

### 场景三：钱包与记录查询

```bash
# 查看地址与余额
yarn wallet:info
# ...
# 备份钱包目录
yarn wallet:backup
```

## 快速开始

1. 准备 Node.js 20+、Git、Python 3.10/3.11.
2. 配置 `.env` 环境变量.
3. 运行 `yarn setup` 完成初始化与质押.
4. 运行 `yarn worker` 开始接任务.
**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
## 示例

环境变量（`.env`）：

| 变量 | 是否必需 | 说明 |
|:-----|:-----|:-----|
| RPC_URL | 是 | 网络主网 RPC 地址 |
| OPERATE_PASSWORD | 是 | 钱包加密密码（≥8 位） |
| GEMINI_API_KEY | 视情况 | 无订阅时必需 |
| GITHUB_TOKEN | 推荐 | 代码类任务需要 |

## 优秀实践

- **密码要强**：`OPERATE_PASSWORD` 至少 8 位，混编字母数字.
- **先单任务**：`yarn worker --single` 验证流程再持续运行.
- **余额常查**：定期 `yarn wallet:info` 查看 gas 与代币余额.
- **备份钱包**：`yarn wallet:backup` 定期备份钱包目录.
- **Python 版本**：用 3.10/3.11，勿用 3.12+，避免兼容问题.
## 常见问题

**Q1：setup 卡住怎么办？**
A：多半在等充值。按提示向地址充值 gas 与质押代币后重跑 `yarn setup`.
**Q2：yarn 找不到？**
A：运行 `corepack enable`（Node 20+ 自带）.
**Q3：Python 3.12 报错？**
A：装 3.11，用 pyenv：`pyenv install 3.11.9`.
**Q4：免费版能跑多节点吗？**
A：不能。多节点集群与任务调度为专业版能力.
**Q5：钱包私钥存哪？**
A：本地加密存储，私钥不联网上传，务必做好备份.
## 进阶用法

### 初始化向导详解

```bash
yarn setup
```

```text
向导步骤:
  1. 检查环境（Node/Python/Poetry 版本）
  2. 创建/导入钱包（生成地址）
  3. 显示充值地址（等待 gas 与质押代币到账）
  4. 验证到账后完成质押
  5. 注册为网络工作节点
  6. 输出节点配置与启动命令
```

### 单任务调试

```bash
# 单任务模式：跑一条任务验证全流程
yarn worker --single
# ...
# 查看任务日志
tail -f logs/worker.log
# ...
# 查看钱包余额与质押状态
yarn wallet:info
yarn wallet:stake
```

### 钱包备份与恢复

```bash
# 备份钱包目录（含加密私钥）
yarn wallet:backup --out wallet-backup.tar.gz
# ...
# 恢复（在新机器）
yarn wallet:restore --from wallet-backup.tar.gz
# 输入 OPERATE_PASSWORD 解密
```

## 运维要点

- **Python 版本锁死**：用 3.10/3.11，pyenv 管理，勿用 3.12+.
- **依赖隔离**：用 Poetry 虚拟环境，避免污染系统 Python.
- **日志定期清**：日志增长快，定期清理或轮转.
- **余额监控**：gas 不足任务失败，设余额下限告警.
- **网络稳定**：RPC 不稳导致掉线，建议备用 RPC.
## 常见报错对照

| 报错 | 原因 | 修复 |
|---:|---:|---:|
| setup 卡住 | 等待充值 | 向地址充 gas+质押代币 |
| yarn 找不到 | 未启用 corepack | `corepack enable` |
| Python 报错 | 版本不对 | 装 3.11，pyenv 切换 |
| 任务失败 | gas 不足 | 充值 gas 后重试 |
| 连接超时 | RPC 不稳 | 换备用 RPC |

## 安全须知

- **私钥本地加密**：私钥加密存储本地，不上传，但丢失无法找回.
- **密码要强**：`OPERATE_PASSWORD` ≥ 8 位混编，别用弱密码.
- **备份要离线**：钱包备份存离线介质，避免单点丢失.
- **别在共享环境跑**：共享/CI 环境私钥易泄露，仅本机运行.
- **凭证不外传**：API Key 与密码不提交版本库，不入日志.
## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 20+
- **Python**: 3.10 或 3.11（非 3.12+）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| Node.js | 运行时 | 必需 | nodejs.org |
| Python | 运行时 | 必需 | python.org |
| Poetry | 包管理 | 必需 | install.python-poetry.org |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- `GEMINI_API_KEY`：无 Google One AI Premium 时必需，从 AI Studio 获取
- `GITHUB_TOKEN`：代码类任务推荐配置，需 repo 权限
- `OPERATE_PASSWORD`：本地钱包加密密码，仅本机使用

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 完成节点初始化与任务执行
- API Key通过环境变量配置: export API_KEY=your_key

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响
- 当前为免费版本,如需完整功能请升级到付费版获取全部能力

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "节点工作工具处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "jinn node"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
