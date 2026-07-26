# Daily Planner — 每日效率规划师

> 一个 WorkBuddy / CodeBuddy Skill，帮你用番茄工作法 + 时间块法自动生成每日日程规划。

## ✨ 功能特性

- **优先级排序**：基于艾森豪威尔矩阵（重要/紧急四象限）自动排序任务
- **时间块日程**：按精力曲线自动分配时间段，上午高难度、下午协作类
- **番茄钟安排**：25分钟工作 + 5分钟休息，每4组长休息15分钟
- **午休保护**：自动在 12:00-13:30 安排午餐休息
- **可勾选清单**：生成 Markdown 格式的待办清单，方便跟踪进度
- **一键导出**：支持保存为 `.md` 文件

## 📦 安装方式

### 方式一：通过 zip 文件安装
1. 下载 `daily-planner.zip`
2. 解压到 `~/.workbuddy/skills/` 目录（用户级）或项目 `.workbuddy/skills/` 目录（项目级）
3. 重启 WorkBuddy，在技能管理中确认已启用

### 方式二：文件夹手动安装
将技能文件夹放到：
```
~/.workbuddy/skills/daily-planner/
```

## 🚀 使用方法

### 自然语言触发
在 WorkBuddy 对话中直接说：
- "帮我规划今天的日程"
- "安排一下今天的时间"
- "做个今日计划"
- "我有这些任务，帮我排个时间表"

### 脚本直接运行
```bash
# 演示模式
python scripts/generate_schedule.py

# JSON 输入模式
python scripts/generate_schedule.py --tasks '{"tasks": [{"name": "写报告", "priority": "high", "duration": 90, "deadline": "14:00"}], "start": "09:00", "end": "22:00"}'

# 交互模式
python scripts/generate_schedule.py --interactive

# 保存到文件
python scripts/generate_schedule.py --output daily-plan.md
```

## 📁 项目结构

```
daily-planner/
├── SKILL.md                        # 核心技能定义（触发条件 + 工作流程 + 输出模板）
├── scripts/
│   └── generate_schedule.py        # 时间块日程生成脚本（Python）
├── references/
│   └── time_management.md          # 时间管理方法论参考
└── README.md                       # 本文件
```

## 📋 输出示例

```markdown
# 📅 今日效率规划 — 2026-07-16

## 🎯 今日目标
完成 1 项核心任务：写项目报告

## 📊 优先级矩阵
| 优先级 | 任务 | 预计时长 | 截止时间 |
|--------|------|----------|----------|
| 🔴 紧急重要 | 写项目报告 | 90分钟 | 14:00 |
| 🟡 重要 | 回复邮件 | 30分钟 | — |

## ⏰ 时间块日程
| 时间 | 任务 | 番茄钟 | 状态 |
|------|------|--------|------|
| 09:00-09:25 | 写项目报告 | 🍅 #1 | ⬜ |
| 09:25-09:30 | ☕ 休息 | — | ⬜ |
| 09:30-09:55 | 写项目报告 | 🍅 #2 | ⬜ |
```

## 🛠️ 技术栈

- **Python 3.10+**：日程生成脚本
- **Markdown**：输出格式
- **无外部依赖**：纯标准库实现

## 📄 许可证

MIT License

## 👤 作者

**zhijie-liang** — WorkBuddy Skill

授权许可：MIT License
