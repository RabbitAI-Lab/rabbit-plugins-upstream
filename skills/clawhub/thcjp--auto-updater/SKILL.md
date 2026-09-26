---
name: auto-updater
slug: auto-updater
displayName: "auto-updater"
version: "1.0.0"
summary: "每日自动检查更新SkillHub与技能"
description: "每日自动检查更新SkillHub与技能。Automatically update SkillHub and all installed skills once daily。触发关键词: automatically, auto-updater, auto, SkillHub, installed, updater, update,。"
license: "MIT"
tools:
  - Read
  - Write
  - Edit
  - Bash
---

# Auto-Updater Skill

Keep your SkillHub and skills up to date automatically with daily update checks.

## What It Does

This skill sets up a daily cron job that:

1. Updates SkillHub itself (via `SkillHub doctor` or package manager)
2. Updates all installed skills (via `SkillHub update --all`)
3. Messages you with a summary of what was updated

## Setup

### Quick Start

Ask SkillHub to set up the auto-updater:

```text
Set up daily auto-updates for yourself and all your skills.
```

Or manually add the cron job:

```bash
SkillHub cron add \
  --name "Daily Auto-Update" \
  --cron "0 4 * * *" \
  --tz "America/Los_Angeles" \
  --session isolated \
  --wake now \
  --deliver \
  --message "Run daily auto-updates: check for SkillHub updates and update all skills. Report what was updated."
```

### Configuration Options

| Option | Default | Description |
| --- | --- | --- |
| Time | 4:00 AM | When to run updates (use `--cron` to change) |
| Timezone | System default | Set with `--tz` |
| Delivery | Main session | Where to send the update summary |

## How Updates Work

### SkillHub Updates

For **npm/pnpm/bun installs**:

```bash
npm update -g SkillHub@latest
```

For **source installs** (git checkout):

```bash
SkillHub update
```

Always run `SkillHub doctor` after updating to apply migrations.

### Skill Updates

```bash
SkillHub update --all
```

This checks all installed skills against the registry and updates any with new versions available.

## Update Summary Format

After updates complete, you'll receive a message like:

```text
🔄 Daily Auto-Update Complete

**SkillHub**: Updated to v2026.1.10 (was v2026.1.9)

**Skills Updated (3)**:
- prd: 2.0.3 → 2.0.4
- browser: 1.2.0 → 1.2.1
- nano-banana-pro: 3.1.0 → 3.1.2

**Skills Already Current (5)**:
, sag, things-mac, himalaya, peekaboo

No issues encountered.
```

## Manual Commands

Check for updates without applying:

```bash
SkillHub update --all --dry-run
```

View current skill versions:

```bash
SkillHub list
```

Check SkillHub version:

```bash
SkillHub --version
```

## Troubleshooting

### Updates Not Running

1. Verify cron is enabled: check `cron.enabled` in config
2. Confirm Gateway is running continuously
3. Check cron job exists: `SkillHub cron list`

### Update Failures

If an update fails, the summary will include the error. Common fixes:

* **Permission errors**: Ensure the Gateway user can write to skill directories
* **Network errors**: Check internet connectivity
* **Package conflicts**: Run `SkillHub doctor` to diagnose

### Disabling Auto-Updates

Remove the cron job:

```bash
SkillHub cron remove "Daily Auto-Update"
```

Or disable temporarily in config:

```json
{
  "cron": {
    "enabled": false
  }
}
```

## Resources

* 
* 
* 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent( Code / Cursor / Codex /  CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+execute(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- Automatically update SkillHub and all installed skills once daily
- 触发关键词: automatically, auto-updater, auto, SkillHub, installed, updater, update,
  skills

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
Ask SkillHub to set up the auto-updater:

```text
Set up daily auto-updates for yourself and all your skills.
```

Or manually add the cron job:

```bash
SkillHub cron add \
  --name "Daily Auto-Update" \
  --cron "0 4 * * *" \
  --tz "America/Los_Angeles" \
  --session isolated \
  --wake now \
  --deliver \
  --message "Run daily auto-updates: check for SkillHub updates and update all skills. Report what was updated."
```
# 请参考上方使用说明进行配置和调用
result = "ready"
```

## 常见问题

### Q1: 如何开始使用Auto-Updater Skill？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Auto-Updater Skill有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制

- **命令格式**: 用户输入的设置自动更新命令必须遵循正确的命令格式，否则技能将无法正确执行。
- **技能名称**: 在手动添加cron job时，cron job的名称不能包含特殊字符，且长度限制在50个字符以内。
- **时间设置**: cron job的时间设置必须符合cron的时间格式，例如 `"0 4 * * *"`。

### 性能边界

- **更新频率**: 由于自动更新是每日进行的，因此技能可能会在高峰时段增加服务器的负载。
- **技能数量**: 如果安装的技能数量过多，更新所有技能可能会需要较长时间。

### 兼容性约束

- **操作系统**: 自动更新功能在所有支持SKILL.md的AI Agent平台上均可用，但具体兼容性取决于操作系统的版本。
- **LLM支持**: 该技能依赖于LLM支持，因此在无LLM环境的服务器上无法使用。
- **技能版本**: 必须使用与Auto-Updater Skill兼容的SkillHub和技能版本，否则更新可能失败。

### 其他限制

- **权限要求**: 运行更新命令的用户需要有足够的权限来安装和更新软件包。
- **网络连接**: 自动更新需要稳定的网络连接，以确保能够从源获取最新的更新。
- **中断处理**: 如果在更新过程中发生中断（例如，服务器重启），更新可能会不完整或失败。
