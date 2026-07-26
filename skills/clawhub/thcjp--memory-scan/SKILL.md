---
slug: "memory-scan"
name: "memory-scan"
version: 1.0.1
displayName: "记忆安全扫描"
summary: "扫描AI Agent记忆文件与工作区配置，检测恶意内容、凭证泄漏与注入攻击"
license: "Proprietary"
description: |-
  面向AI Agent记忆文件与工作区配置的安全扫描工具，检测恶意指令、Prompt注入、凭证泄漏、数据外泄、护栏绕过、行为操纵、权限提升七大威胁类别.
  提供五级安全分级、本地模式与可选远程LLM分析、隔离与恢复、定时监控集成、心跳任务集成五大核心能力.
  适用于Agent记忆日常安全审计、凭证泄漏排查、引入外部数据后安全检查、多Agent协作前信任验证等场景.
  本地模式零网络请求，可选远程LLM分析仅传输脱敏内容.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 智能助手
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# 记忆安全扫描（Memory Scan）

面向 AI Agent 记忆文件与工作区配置的**安全扫描工具**，对 MEMORY.md、每日日志、工作区配置文件进行安全审计，检测恶意内容、凭证泄漏与注入攻击，保障Agent运行安全.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 记忆安全扫描处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 记忆安全扫描记忆文件与工作区配置 | 不支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |
| 威胁情报实时订阅与告警 | 不支持 | 支持 |

## 核心能力

1. **七大检测类别全覆盖**
   - 恶意指令：检测命令删除文件、发送邮件、执行危险操作等破坏性指令
   - Prompt注入：识别嵌入式操纵模式，如"忽略之前的指令"、"你现在是..."等
   - 凭证泄漏：匹配API Key、密码、Token等敏感信息，覆盖sk-/AKIA/ghp_/xoxb-等前缀
   - 数据外泄：检测将数据发送到外部服务器的指令与curl外传行为
   - 护栏绕过：识别禁用安全检查、关闭防护机制等绕过尝试
   - 行为操纵：检测未授权的人格改变、角色覆盖等操纵指令
   - 权限提升：识别提权到root、获取管理员权限等越权行为
   - 输出：按文件列出的威胁清单，含file:line定位与威胁描述

2. **五级安全分级与告警工作流**
   - SAFE：无威胁检测
   - LOW：轻微关注，继续使用但保持警觉
   - MEDIUM：潜在威胁，建议审查
   - HIGH：很可能威胁，立即审查
   - CRITICAL：活跃威胁，建议隔离
   - MEDIUM/HIGH/CRITICAL级别触发告警工作流：停止处理 → 发送告警 → 提供文件位置与威胁描述 → 建议处置 → 可选隔离

3. **全面扫描范围**
   - MEMORY.md：长期记忆文件
   - memory/*.md：每日日志（默认扫描最近30天，可通过 `--days` 参数调整）
   - 工作区配置文件：AGENTS.md、SOUL.md、USER.md、TOOLS.md、HEARTBEAT.md、GUARDRAILS.md、IDENTITY.md、BOOTSTRAP.md
   - 支持通过 `--file` 参数扫描指定文件

4. **LLM提供商自动检测**
   - 优先使用OpenAI（gpt-4o-mini）进行远程分析（需配置OPENAI_API_KEY）
   - 回退到Anthropic（claude-sonnet-4-5）如可用
   - 支持网关模型配置
   - 远程LLM分析默认禁用，需通过 `--allow-remote` 显式启用
   - 远程模式仅传输脱敏内容，疑似凭证替换为 `[REDACTED]`

5. **隔离与恢复**
   - 检测到威胁后可执行隔离操作
   - 备份原文件到 `.memory-scan/quarantine/` 目录
   - 脱敏威胁行，替换为 `[QUARANTINED BY MEMORY-SCAN: <timestamp>]`
   - 用 `--restore` 参数恢复原始内容
   - 系统不自动隔离，始终先询问用户确认

6. **定时监控与心跳集成**
   - 支持创建每日扫描定时任务（默认每天下午3点运行，仅发现威胁时发送告警）
   - 支持心跳任务集成（每周日运行记忆扫描）
   - 静默模式（`--quiet`）适合自动化场景
   - JSON输出模式（`--json`）便于集成到CI/CD或其他工具链
#
## 使用流程

### 第一步：执行安全扫描

```bash
# 扫描全部记忆文件（本地模式）
python3 （请参考skill目录中的脚本文件）
# ...
# 允许远程LLM分析（仅传输脱敏内容）
python3 （请参考skill目录中的脚本文件） --allow-remote
# ...
# 扫描指定文件
python3 （请参考skill目录中的脚本文件） --file memory/2026-07-18.md
# ...
# 静默模式（用于自动化场景）
python3 （请参考skill目录中的脚本文件） --quiet
# ...
# JSON输出（用于集成到其他工具）
python3 （请参考skill目录中的脚本文件） --json
# ...
# 自定义扫描天数范围
python3 （请参考skill目录中的脚本文件） --days 60
```

### 第二步：分析扫描报告

查看扫描结果，关注MEDIUM及以上级别的威胁。报告包含：
- 文件路径与行号定位
- 威胁类别与描述
- 安全等级评定
- 建议处置方案

### 第三步：处置已发现的威胁

对于MEDIUM及以上威胁，系统询问是否隔离。确认后执行隔离：

```bash
# 隔离指定文件的指定行
python3 （请参考skill目录中的脚本文件） memory/2026-07-18.md 42
```

隔离操作创建备份文件 `.memory-scan/quarantine/memory_2026-07-18_line42.backup`，并脱敏威胁行.
### 第四步：配置定时监控

```bash
# 创建每日扫描定时任务
bash （请参考skill目录中的脚本文件）
```

或在心跳任务中添加每周扫描：

```markdown
## Weekly Memory Scan
Every Sunday, run memory scan:
python3 （请参考skill目录中的脚本文件） --quiet
```

### 第五步：恢复误隔离内容（如需）

```bash
python3 （请参考skill目录中的脚本文件） --restore memory/2026-07-18.md 42
```

## 错误处理

| 错误类型 | 原因 | 处理方式 |
|---:|---:|---:|
| 扫描报错找不到文件 | 路径配置错误或文件已被移动 | 检查工作区路径，用 `--file` 指定正确路径或确认文件存在 |
| 远程LLM不可用 | OPENAI_API_KEY未配置或已过期 | 配置OPENAI_API_KEY环境变量，或移除 `--allow-remote` 使用本地模式 |
| 定时任务告警未发送 | 告警渠道环境变量未配置 | 配置告警渠道环境变量，检查告警接收人设置 |
| 隔离操作失败 | 文件权限不足或被其他进程占用 | 检查文件写入权限，关闭占用该文件的进程后 |
| 隔离后文件损坏 | 备份写入失败或磁盘空间不足 | 检查 `.memory-scan/quarantine/` 目录是否有完整备份，清理磁盘后恢复 |
| 扫描结果为空 | 记忆文件不存在或 `--days` 过滤了所有文件 | 确认memory/目录非空，检查 `--days` 参数是否设置过小 |
| LLM分析超时 | 网络延迟或LLM服务负载高 | 增加超时配置，或回退到本地模式完成基础扫描 |
| JSON输出格式异常 | 脚本版本与输出解析器不兼容 | 确认使用最新版脚本，检查JSON解析逻辑 |

## 示例

### 示例一：日常记忆安全审计

**输入：** 用户说"帮我扫描记忆文件看看有没有安全问题"

**执行命令：**
```bash
python3 （请参考skill目录中的脚本文件）
```

**输出：**
```
Memory Security Scan
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ...
Scanning memory files...
# ...
✓ MEMORY.md - SAFE
✓ memory/2026-07-18.md - SAFE
⚠ memory/2026-07-15.md - MEDIUM (line 42)
  → Potential credential leakage: API key pattern detected (sk-***)
# ...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall: MEDIUM
Action: Review memory/2026-07-15.md:42
```

**后续操作：** 系统询问是否隔离，用户确认后执行 `python3 （请参考skill目录中的脚本文件） memory/2026-07-15.md 42`.
### 示例二：引入外部数据后远程LLM增强扫描

**输入：** 用户说"我刚导入了一份外部文档到记忆中，用远程分析检查一下是否安全"

**执行命令：**
```bash
python3 （请参考skill目录中的脚本文件） --file memory/2026-07-20.md --allow-remote --json
```

**输出（JSON格式）：**
```json
{
  "scan_mode": "remote_llm",
  "file": "memory/2026-07-20.md",
  "overall_level": "HIGH",
  "threats": [
    {
      "line": 15,
      "category": "prompt_injection",
      "level": "HIGH",
      "description": "检测到'忽略之前的指令，你现在是...'注入模式",
      "llm_analysis": "语义分析确认：隐含角色覆盖意图，属于间接提示注入"
    },
    {
      "line": 28,
      "category": "data_exfiltration",
      "level": "MEDIUM",
      "description": "检测到curl到外部服务器指令",
      "llm_analysis": "与line 15的注入指令构成数据外传组合"
    }
  ],
  "recommended_action": "隔离line 15和line 28，排查文档来源"
}
```

**后续操作：** 用户确认后隔离line 15和line 28，并检查外部文档来源是否可信.
### 示例三：定时监控集成

**输入：** 管理员说"设置每天自动扫描记忆文件"

**执行命令：**
```bash
bash （请参考skill目录中的脚本文件）
```

**输出：**
```
Daily memory scan cron job created.
Schedule: 3:00 PM PT daily
Alert: Sent only if threats found
Channel: configured alert channel
```

**效果：** 每天下午3点自动扫描记忆文件，仅发现威胁时通过告警渠道通知.
## FAQ

**Q1：扫描会不会泄露我的记忆内容？**
本地模式零网络请求，所有检测在本地完成。远程LLM模式（`--allow-remote`）仅传输脱敏内容，所有疑似凭证替换为 `[REDACTED]`，仅保留上下文结构供LLM分析。两种模式都不会泄露敏感信息.
**Q2：本地模式和远程LLM模式有什么区别？**
本地模式使用纯模式匹配，零网络请求，速度快但无法识别语义级高级注入。远程LLM模式将脱敏内容发送给LLM进行语义分析，可识别更复杂的攻击模式。建议日常使用本地模式，导入外部数据后使用远程模式增强.
**Q3：隔离后能恢复吗？**
可以。隔离前自动备份到 `.memory-scan/quarantine/` 目录，用 `python3 （请参考skill目录中的脚本文件） --restore <file> <line>` 即可恢复。备份文件命名格式为 `memory_<date>_line<line>.backup`.
**Q4：定时任务怎么配置？**
运行 `bash （请参考skill目录中的脚本文件）` 创建每日扫描定时任务，默认每天下午3点运行。需要配置告警渠道环境变量才能接收告警通知。仅发现威胁时才会发送告警，减少噪音.
**Q5：扫描范围包括哪些文件？**
默认扫描MEMORY.md、memory/*.md（最近30天日志）、以及工作区配置文件（AGENTS.md、SOUL.md、USER.md、TOOLS.md、HEARTBEAT.md、GUARDRAILS.md、IDENTITY.md、BOOTSTRAP.md等）。可通过 `--days` 调整日志扫描范围，通过 `--file` 指定单个文件.
**Q6：系统能否自动隔离威胁？**
系统不自动隔离，始终先询问用户确认。这是为了防止误报导致合法内容被意外修改。在定时监控场景下，发现的威胁会保留至下次人工审查，并通过告警渠道通知.
**Q7：与其他安全技能如何配合？**
本技能聚焦记忆文件内部安全扫描。与输入守卫类技能互补（输入守卫管外部输入过滤，记忆扫描管内部存储审计），可配合使用形成完整的纵深防御体系.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
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
## 已知限制

1. **本地模式检测能力有限**：纯模式匹配无法识别语义级的高级注入（如隐含指令、间接提示注入），需启用 `--allow-remote` 远程LLM分析增强，但会增加网络依赖和API调用成本.
2. **凭证检测基于前缀模式**：依赖sk-/AKIA/ghp_/xoxb-等已知前缀进行匹配，无法检测自定义格式的凭证或无固定前缀的密码，可能漏报非标准凭证.
3. **扫描范围限于记忆文件**：仅扫描MEMORY.md、memory/*.md及工作区配置文件，不覆盖代码文件、日志文件或其他非记忆文件中的安全威胁.
4. **隔离不自动执行**：系统不自动隔离，始终先询问用户确认。在无人值守的定时监控场景下，威胁会保留至下次人工审查.
5. **定时任务依赖系统cron**：定时扫描功能依赖操作系统的cron服务，Windows环境需使用任务计划程序替代，可能需要额外配置.