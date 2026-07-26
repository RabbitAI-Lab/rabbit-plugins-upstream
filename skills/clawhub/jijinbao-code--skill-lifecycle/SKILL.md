---
name: skill-lifecycle
version: 1.0.0
description: 技能退休机制 - 记录使用频次，标记低频/退休技能，支持归档和恢复
metadata:
  author: 小夏
  created: 2026-06-25
  emoji: 📊
  category: workflow
  tags: [skills, lifecycle, retirement, archive, usage-tracking]
---

# 技能退休机制

**核心原则：保持技能库精简，退休技能可恢复**

## 机制概述

| 状态 | 条件 | 处理 |
|------|------|------|
| 🟢 活跃 | 最近100天内有使用 | 正常加载 |
| 🟡 低频 | 100-300天未使用 | 标记，评估价值 |
| 🔴 退休 | >300天未使用 | 归档候选，需确认 |
| 📦 归档 | 用户确认后 | 移至skills-archive/，可恢复 |

## 文件结构

```
skills/skill-lifecycle/
├── SKILL.md              # 本文件
├── record-usage.sh       # 记录技能使用
├── check-retirement.sh   # 检查退休候选
├── archive-skill.sh      # 归档技能
├── restore-skill.sh      # 恢复技能
├── usage.jsonl           # 使用记录（追加式）
├── latest-usage.json     # 最新使用时间（快速查询）
└── retirement-report.md  # 退休检查报告
```

## 使用方式

### 1. 记录技能使用

每次加载/使用技能时调用：
```bash
bash ~/.openclaw/workspace/skills/skill-lifecycle/record-usage.sh <skill-name> [action]
```

action 可选值：
- `loaded` — 技能被加载到会话（默认）
- `used` — 技能被实际使用
- `searched` — 技能被搜索到
- `installed` — 技能被安装
- `updated` — 技能被更新
- `restored` — 技能被恢复

### 2. 检查退休候选

```bash
bash ~/.openclaw/workspace/skills/skill-lifecycle/check-retirement.sh
```

输出报告到 `retirement-report.md`，包含：
- 统计摘要（活跃/低频/退休/无记录）
- 退休候选列表
- 操作建议

### 3. 归档技能

```bash
bash ~/.openclaw/workspace/skills/skill-lifecycle/archive-skill.sh <skill-name>
```

归档后：
- 技能移至 `~/.openclaw/workspace/skills-archive/`
- 保留原始文件和元数据
- 不再被系统加载

### 4. 恢复技能

```bash
bash ~/.openclaw/workspace/skills/skill-lifecycle/restore-skill.sh <skill-name>
```

恢复后：
- 技能移回 `~/.openclaw/workspace/skills/`
- 自动记录使用时间
- 立即可用

## 自动化

### Cron任务
- 每周日10:00自动检查退休候选
- 生成报告并通知用户
- 用户确认后执行归档

### 会话集成
在每次会话结束时，记录本会话使用的技能：
```bash
# 在会话结束钩子中调用
bash ~/.openclaw/workspace/skills/skill-lifecycle/record-usage.sh <skill-name> used
```

## 安全考虑

1. **归档前确认** — 退休技能需用户确认才归档
2. **可恢复性** — 归档目录保留完整文件
3. **元数据保留** — 归档时记录原因和时间
4. **备份建议** — 归档前可选备份到 `~/Archive/`

## 查询当前状态

```bash
# 查看所有技能的最后使用时间
cat ~/.openclaw/workspace/skills/skill-lifecycle/latest-usage.json

# 查看使用历史
tail -20 ~/.openclaw/workspace/skills/skill-lifecycle/usage.jsonl

# 生成退休报告
bash ~/.openclaw/workspace/skills/skill-lifecycle/check-retirement.sh
```

## 与 TOOLS.md 的关系

- TOOLS.md 记录技能使用笔记
- 本机制记录技能使用频次
- 退休报告可帮助更新 TOOLS.md 中的技能索引
