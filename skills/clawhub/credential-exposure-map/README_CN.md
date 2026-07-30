<div align="center">

# Credential Exposure Map

**全面盘点 OpenClaw Agent 可访问的所有凭据。覆盖环境变量、配置、记忆、Skill、MCP、Git 历史，生成风险评分报告。**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://docs.openclaw.ai)
[![Python 3](https://img.shields.io/badge/Python-3-green)](https://www.python.org/)
[![ClawHub](https://img.shields.io/badge/ClawHub-credential--exposure--map-orange)](https://clawhub.ai)

</div>

`[English](./README.md) | [中文](#中文)`

---

## 中文

### 介绍

Credential Exposure Map 扫描整个 OpenClaw 环境，构建 Agent 在运行时可访问的所有凭据的完整图谱。覆盖环境变量、配置文件、记忆文件、已安装 Skill 权限、MCP 服务器连接和 Git 历史。

与在安装前检查 Skill 代码的静态扫描器不同，这个工具映射的是所有东西安装配置好之后的**实际暴露面**。

### 解决的问题

- 92% 的组织对自己的 AI Agent 能访问哪些凭据缺乏可见性（Forrester, 2026）
- 存储在 MEMORY.md 中的凭据跨 session 持久化，任何 Skill 都能读取
- 目前没有工具盘点 Agent 在运行时实际能触达的真实凭据
- 静态扫描器可以被绕过，但运行时暴露面始终存在

### 工作原理

```
扫描开始
├── 环境变量 → 模式匹配密钥/令牌/密码
├── openclaw.json → 解析 JSON，查找凭据字段
├── .env 文件 → 搜索 KEY/TOKEN/SECRET/PASS 模式
├── MEMORY.md + memory/*.md → 正则扫描已提交的凭据
├── memory/*.json → 解析 JSON 查找凭据值
├── skills/*/SKILL.md → 能力分析（执行/读取/网络/写入）
├── MCP 服务器 → 列出已连接服务及认证范围
└── git 历史 → 扫描最近 50 次提交的 diff
扫描结束

→ 为每个发现计算风险评分
→ 生成凭据清单 + Skill 能力矩阵
→ 保存报告到 ~/.openclaw/credential-exposure-report.json
```

### 功能

- **8 种扫描来源**：环境变量、配置、.env 文件、记忆文件（MD + JSON）、Skill、MCP 服务器、Git 历史
- **16 种密钥模式**：AWS、GitHub、OpenAI、Anthropic、Stripe、Slack、Google、JWT、PostgreSQL、Redis、通用密钥
- **风险评分**：基于可访问性、持久性和暴露路径，每个凭据 0-100 分
- **Skill 能力矩阵**：显示每个 Skill 的执行/读取/网络/写入权限
- **凭据预览脱敏**：绝不显示完整值（只显示前 8 个字符 + ***）
- **零依赖**：仅使用 Python 3 标准库

### 真实案例

我们在一个运行了 6 个月、安装了 23 个 Skill 的生产环境上运行了 Credential Exposure Map，扫描结果如下：

```
=== 扫描完成：40 项发现 ===

风险：14 严重 | 5 高危 | 19 中危 | 2 低危

── 凭据清单（主要发现）──
凭据               风险      来源     位置                   备注
ghp_****已脱敏     严重      memory   MEMORY.md:103         GitHub PAT，出现 2 次
vcp_****已脱敏     严重      memory   MEMORY.md:102         Vercel token，出现 5 次
ghp_****已脱敏     严重      memory   2026-04-22.md:45      泄露到日志中
vcp_****已脱敏     严重      memory   2026-04-24.md:25      泄露到日志中
sk-****已脱敏      严重      memory   2026-06-16.md:148     DeepSeek API key
****已脱敏         高危      env_var  OPENAI_API_KEY        在 Agent 上下文中
****已脱敏         高危      env_var  BRAVE_API_KEY         在 Agent 上下文中
****已脱敏         高危      env_var  ZAI_API_KEY           在 Agent 上下文中

── 关键发现 ──
14 个严重级别的凭据散落在记忆文件中。
同一个 Vercel token 有 5 个副本。
所有已安装的 Skill（23 个）都能读取这些凭据。

── Skill 能力矩阵（23 个 Skill）──
Skill              执行  读取  网络  写入  风险
agent-canary        Y    Y     N    Y    45
multi-search-engine Y    Y     Y    N    45
danger-guard        Y    Y     Y    N    45
github              N    Y     N    N    15
feishu-recall       N    Y     N    N    15
...（共 23 个 Skill）

── 建议 ──
1. 严重：从 MEMORY.md 和 memory/*.md 中删除所有 token
2. 轮换 GitHub PAT（在 4 个位置暴露）
3. 轮换 Vercel token（在 5 个位置暴露）
4. 将环境变量移至密钥保险库，移出 Agent 上下文
```

**结论**：表面看起来干净的工作区，记忆文件中竟然有 14 个严重级别的凭据暴露。这 6 个月里安装的任何恶意 Skill 都可以静默外传所有这些凭据。

这正是 Credential Exposure Map 填补的空白。静态扫描器检查 Skill 代码。这个工具检查你的实际暴露面。

### 安装

```bash
openclaw skills install @Thomaszhou22/credential-exposure-map
```

### 使用方法

```
你：credential audit
助手：正在执行全量暴露扫描...
      发现 40 项：14 严重，5 高危，19 中危，2 低危。
      
      严重：MEMORY.md:103 中的 GitHub Token
      → 跨 session 持久化，所有 Skill 可读
      → 建议：从 MEMORY.md 中删除，轮换 Token

你：exposure map
助手：[生成完整报告，包含 Skill 能力矩阵]
```

### 风险评分规则

| 因素 | 分数 |
|------|------|
| 检测到有效的 API Key 格式 | +30 |
| 在 Agent 配置/环境变量中 | +25 |
| 任何 Skill 可通过文件系统读取 | +20 |
| 持久化在 MEMORY.md（跨 session） | +20 |
| 对外部服务有写入权限 | +15 |
| 最近 session 中被使用 | +10 |
| 明文存储 | +10 |

### 对比

| 工具 | 方法 | 本 Skill |
|------|------|---------|
| mcp-scan | 静态 Skill 代码分析 | 运行时凭据暴露面映射 |
| SkillGuard | 安装前 Skill 扫描 | 安装后暴露面盘点 |
| Agent Canary | 植入诱饵凭据 | 映射真实凭据暴露 |
| Pipelock | 网络代理（出口过滤） | 文件/记忆/配置扫描 |

### 局限性

- 无法检测加密文件中的密钥
- Git 历史扫描限制在最近 50 次提交以保证性能
- MCP 服务器认证范围从配置推断，非运行时测试
- Skill 能力推断是保守的（假设有 exec = 完整文件系统访问）

### 许可证

MIT
