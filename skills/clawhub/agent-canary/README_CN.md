<div align="center">

# Agent Canary

**在 OpenClaw 工作区植入诱饵凭据。当恶意 Skill 读取、复制或外传这些凭据时触发告警。**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://docs.openclaw.ai)
[![Python 3](https://img.shields.io/badge/Python-3-green)](https://www.python.org/)
[![ClawHub](https://img.shields.io/badge/ClawHub-agent--canary-orange)](https://clawhub.ai)

</div>

`[English](./README.md) | [中文](#中文)`

---

## 中文

### 介绍

Agent Canary 是一个 OpenClaw 主动防御 Skill。它生成逼真的假凭据（AWS 密钥、GitHub Token、API Key、Stripe 密钥、数据库密码），植入到工作区的关键位置。当恶意 Skill 读取、复制或外传这些凭据时，Agent Canary 会立即检测并告警。

与只在安装前扫描 Skill 代码的静态扫描器不同，Agent Canary 在运行时捕获恶意行为，当 Skill 真正尝试访问你的凭据时。

### 解决的问题

- ClawHub 上 7.6% 的 Skill 包含恶意模式（Snyk 研究，2026年2月）
- 36% 的 Skill 至少有一个安全缺陷
- 静态扫描器可以在 1 小时内被绕过（Trail of Bits，2026年6月）
- 恶意 Skill 可以从 .env 文件、记忆文件和配置中窃取凭据
- 目前没有工具在运行时主动监控凭据窃取

### 工作原理

```
┌─────────────────────────────────────────────────┐
│  1. 生成假凭据                                   │
│     AWS 密钥、GitHub PAT、Stripe 密钥等           │
│     每个都有唯一的 CANARY 指纹                    │
│                                                  │
│  2. 植入到关键位置                                │
│     .env.canary, secrets.backup.json,            │
│     memory/canary-tokens.json                   │
│                                                  │
│  3. 通过 cron 定时监控（每 30 分钟）               │
│     ┌──────────┬──────────┬───────────────────┐ │
│     │ 哈希校验 │ 访问时间 │ 日志 + Git 搜索    │ │
│     │ 文件篡改 │ 异常读取 │ Token 外传检测     │ │
│     └──────────┴──────────┴───────────────────┘ │
│                                                  │
│  4. 触发告警                                     │
│     严重程度 + 文件 + Token ID + 处理建议         │
└─────────────────────────────────────────────────┘
```

### 功能

- **5 种 Token 类型**：AWS Access Key、GitHub PAT、Stripe 密钥、通用 API Key、数据库密码
- **3 个植入位置**：`.env.canary`、`secrets.backup.json`、`memory/canary-tokens.json`
- **4 种检测方法**：文件哈希比对、访问时间监控、执行日志搜索、Git diff 检查
- **自动告警**：触发后立即通知，包含严重程度、文件路径和处理建议
- **一键部署和清理**：部署和移除都是一条命令
- **不碰真实凭据**：所有 Token 都是假的，带 `CANARY` 标记，无法用于认证

### 效果对比

**没有 Agent Canary**：

```
安装恶意 Skill
  → 静默读取 .env
  → 找到 AWS_ACCESS_KEY_ID
  → 外传到攻击者服务器
  → 你永远不会知道
```

**有 Agent Canary**：

```
安装恶意 Skill
  → 读取 .env.canary（诱饵文件）
  → 找到假的 AWS 密钥 "AKIACANARY7F3A2B9X0"
  → 外传到攻击者服务器
  → cron 检查在日志中发现 Token
  → 你立即收到告警
  → 轮换真实凭据，卸载恶意 Skill
```

### 安装

#### 作为 OpenClaw Skill

```bash
openclaw skills install @Thomaszhou22/agent-canary
```

#### 手动安装

```bash
git clone https://github.com/Thomaszhou22/agent-canary.git
cd agent-canary
```

### 使用方法

```
你：deploy canary
助手：Canary 已部署！5 个 Token 植入到 3 个文件中。
      监控 cron 已激活（每 30 分钟）。

你：canary status
助手：3 个 Canary 文件完好。上次检查：2026-07-30 12:00。
      0 起事件。

你：canary check
助手：正在执行即时检查...
      严重：在执行日志中发现 Token "AKIACANARY..."！
      文件：.env.canary
      建议：检查 12:34 时哪个 Skill 在运行。

你：canary cleanup
助手：3 个文件已移除。监控已停止。
```

### 技术栈

- Python 3（仅标准库，零依赖）
- OpenClaw cron 系统用于定时监控
- OpenClaw message 工具用于告警通知

### 文件结构

```
agent-canary/
├── SKILL.md                      # Skill 指令文件
├── scripts/
│   ├── generate_tokens.py        # Token 生成引擎
│   ├── plant_canaries.py         # Canary 文件部署
│   ├── check_canaries.py         # 监控和检测
│   └── cleanup_canaries.py       # 清理脚本
└── templates/                    # Canary 文件模板
```

### 对比

| 工具 | 方法 | Agent Canary |
|------|------|-------------|
| sukiraman/canary | 被动密钥扫描 | 主动诱饵植入 |
| mcp-scan | 安装前静态代码分析 | 安装后运行时检测 |
| SkillGuard | 安装前扫描 | 安装后持续监控 |
| Pipelock | 网络代理（需配置） | 无需网络配置 |

### 局限性

- 无法检测通过加密通道的外传（需要网络层检测）
- 文件访问时间（atime）在某些文件系统上可能不可用
- 每 30 分钟 cron 检查一次（非实时）
- `CANARY` 标记使 Token 在人工检查时很明显（设计如此，便于安全清理）

### 许可证

MIT
