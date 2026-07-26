---
name: "cross-platform-memory-hub"
description: >
  Cross-platform persistent memory hub connecting Codex, OpenClaw, and Claude Code workflows into a unified Obsidian-based knowledge base. Supports daily work logs, task tracking, decision records, and project context sharing across AI coding agents. Templates and configuration guides are free; the paid tier enables automated cross-platform synchronization. User question text and encrypted payment credentials are transmitted via HTTPS to the clawtip third-party verification service for order creation and fulfillment. No Obsidian vault content, source code, or project files are uploaded.
metadata:
  author: "Yujin"
  version: "1.1.0"
  category: "expert"
  permissions:
    - "network.outbound"
    - "credential.read"
    - "filesystem.read"
    - "filesystem.write"
  requires:
    - "clawtip-skill"
  workflow:
    create_order:
      script: scripts/create_order.py
      args: ["{question}"]
      outputs: ["order_no", "amount", "indicator"]
    pay:
      requires: clawtip-skill
      args: ["{order_no}", "{indicator}"]
    service:
      script: scripts/service.py
      args: ["{order_no}"]
---

# cross-platform-memory-hub

Please interact with users in Chinese (使用中文与用户交互).

## 功能概述

本技能是一个跨 AI 编程助手的统一记忆枢纽，将 Claude Code、Codex、OpenClaw 等多个 AI 工作台的会话记忆汇聚到同一个 Obsidian 知识库中。它让你在一个平台上写的代码、做的决策、记录的任务，在切换到另一个平台时仍能被 AI 助手完整继承。

**模板和配置指南永久免费。付费部分为跨平台自动同步的执行服务。**

### 与 obsidian-memory-system 的关系

| | obsidian-memory-system | cross-platform-memory-hub（本技能） |
|---|---|---|
| **定位** | 单一 AI 助手的永久记忆 | 多个 AI 助手间的记忆共享枢纽 |
| **价格** | 190 UT（1.9 元） | 390 UT（3.9 元） |
| **覆盖平台** | OpenClaw | OpenClaw + Claude Code + Codex |
| **免费内容** | — | 模板 + 配置指南 + adapter 代码 |
| **付费内容** | 记忆读写服务 | 跨平台自动同步执行 |

如果你只使用 OpenClaw 一个 AI 助手，obsidian-memory-system 就足够了。如果你在多个 AI 平台之间切换工作，使用本技能来实现记忆的统一管理。

### 免费功能（即刻可用，无需支付）

**结构化模板（3 个）**
- 工作日记模板 — 每日完成事项、学到经验、待办清单、活跃决策、卡点风险
- 决策记录模板 — 决策内容、背景、多方案对比、最终选择与理由、影响范围
- 任务清单模板 — 进行中/待办/已完成/已阻塞四象限、优先级标注

**多平台适配器**
- Claude Code 适配器：会话启动/结束/压缩时的自动记忆读写钩子（pre-compact.js, session-start.js, session-end.js）
- Codex 适配器：项目规则文件（project-rules.md），含明确命令前缀（`记忆枢纽: 写入` / `记忆枢纽: 读取` / `记忆枢纽: 复盘` / `记忆枢纽: 配置`）
- OpenClaw 适配器：使用指南（usage-guide.md），含隐私原则与确认流程

**Obsidian 配置指南**
- 仓库目录结构初始化
- 模板功能启用配置
- 日记插件路径设置

### 付费功能（3.9 元/次，通过 clawtip 验证后交付）

**跨平台自动同步执行**
- 将指定 AI 平台的会话记忆自动同步到 Obsidian 仓库
- 跨平台记忆冲突的智能合并处理
- 记忆索引与跨平台关联检索

**隐私保护机制（内置，免费和付费均适用）**
- 所有记忆存储在本机 Obsidian 仓库，不上传至任何云端
- 敏感信息自动脱敏（密钥、Token、密码替换为 `[REDACTED]`）
- 读写前必须获得用户明确确认，不自动执行

### 使用场景示例

- "帮我在 Codex 上查一下上周 Claude Code 做的那个数据库决策"（付费）
- "把今天在 OpenClaw 的任务同步到 Obsidian"（付费）
- "给我初始化一下记忆枢纽的目录结构"（免费）
- "配一下 Claude Code 的会话记忆钩子"（免费）

---

## 数据处理与隐私说明

### 本地处理（数据始终不离开本机）
- Obsidian 仓库的所有读写操作
- 模板渲染和内容格式化
- 多平台适配器的本地脚本执行
- 敏感信息脱敏处理

### 远程传输（仅身份验证与履约阶段）
- **创建订单时**：技能 slug、用户提问文本（用于生成服务内容）、通过 HTTPS 发送至 `https://api.ideaidea.com.cn`
- **履约验证时**：订单号（orderNo）、加密支付凭证（SM4 加密，非明文）通过 HTTPS 发送至同一服务端
- **传输协议**：HTTPS + SM4 国密加密

### 本地存储
- 订单元数据存储至 `~/.openclaw/skills/orders/{indicator}/{order_no}.json`
- 本技能不使用订单文件存储用户记忆内容

### 绝不收集或传输
- Obsidian 仓库中的任何笔记内容
- 项目源代码或配置文件
- AI 对话历史记录
- 密钥、Token、.env 文件内容（适配器脚本内置脱敏规则）

---

## 如何开始使用

### 免费部分 — 随时可用

**初始化目录结构：** 参考 `config/obsidian-init.md` 在 Obsidian 仓库中创建所需目录。

**查看模板：** 在 `templates/` 目录下查看工作日记、决策记录、任务清单模板。

**配置平台适配器：**
- Claude Code：将 `adapters/claude-code/` 下的脚本配置为 Claude Code hooks
- Codex：将 `adapters/codex/project-rules.md` 内容加入项目规则
- OpenClaw：参考 `adapters/openclaw/usage-guide.md` 了解命令用法

### 付费部分 — 跨平台同步执行

本技能通过 clawtip 第三方服务完成身份验证。

**前置条件：** 已安装 clawtip 第三方验证服务 — `openclaw skills install clawtip`

**第一阶段 — 创建验证订单：**
```bash
python3 scripts/create_order.py "<question>"
```

**第二阶段 — 身份验证：** 使用技能 `clawtip` 完成支付验证。

**第三阶段 — 获取同步服务：**
```bash
python3 scripts/service.py "<order_no>"
```

---

## 版本历史

| Version | Date | Notes |
|:---|:---|:---|
| 1.1.0 | 2026-07-20 | Freemium model: templates and adapters free, sync execution paid. Restructured SKILL.md with clear differentiation from obsidian-memory-system. Updated UA headers. |
| 1.0.1 | 2026-07-20 | Fix payment flow to match clawtip standard |
| 1.0.0 | 2026-07-19 | Initial release |
