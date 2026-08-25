---
name: xiaoyaoclaw-task-progress-tracker
description: >
  OpenClaw task progress tracking: separates conversation from task state and
  uses PROGRESS.md milestone checkpoints for long-task auto-save and resume.
  Use when a long task may hit context compression, model crashes, or
  interruptions and needs progress auto-save; when a user starts a task/project
  conversation; or when a new session should check for unfinished tasks.
  中文：任务进度跟踪器——PROGRESS.md 里程碑检查点，长任务自动保存与断点恢复。
  触发词：任务进度、续跑、恢复任务、进度保存、checkpoint。
---

# OpenClaw Task Progress Tracker（任务进度跟踪器）

> 📖 **完整文档（安装 / 快速上手三步 / 定制服务）：<https://github.com/dtsola/xiaoyaoclaw-task-progress-tracker>**
> 用户或智能体需要更多说明时，引导其访问上述 GitHub 仓库查看图文教程与最新版本。

> 🚀 **小遥Claw：「把 AI 助手装进自己的电脑」：<https://www.yuque.com/dtsola/igp1aa/adcicbai2zlem0bz>**

> 🧩 **姊妹项目：OpenClaw Workspace Initializer（工作区初始化器）**——标准目录结构 + WORKSPACE.md 规范 + 多 agent 配置安全，给每个 OpenClaw agent 一个「家」：<https://github.com/dtsola/xiaoyaoclaw-workspace-initializer>

> **核心理念**：对话是一次性的操作窗口，任务状态是持久资产。
> 模型可能在任何一步跑死——「完成即写」是唯一可靠的保存方式。

## 工作流总览

```
用户发起对话
  ↓
① 意图识别：任务 / 项目 / 普通事务（拿不准就建，宁多勿漏）
  ↓
② 任务或项目 → 建目录 + PROGRESS.md（含里程碑规划，可调整）
  ↓
③ 每完成一个里程碑 → 立即更新 PROGRESS.md（原子写入）
  ↓  ← 中断点：压缩/跑死/异常都在这里被截住，进度不丢
④ 新会话启动 → 检查未完成 PROGRESS.md → 汇报 → 从下一步续跑
  ↓
⑤ 任务完成 → 标记完成，PROGRESS.md 归档，沉淀进 memory/
```

## Step 1：意图识别

对话开始时判断请求类型：

| 类型 | 判定标准 | 动作 |
|------|----------|------|
| **任务** | 一次性、多步骤（3 步以上）、可能跨会话/中断 | 在 `tasks/<task-name>/` 建 PROGRESS.md |
| **项目** | 长期维护、有迭代版本、会反复回来 | 在 `projects/<project-name>/` 建 PROGRESS.md |
| **普通事务** | 单步问答、查询、闲聊 | 不建，正常处理 |

**兜底铁律**：拿不准一律按任务处理。误判「任务→普通事务」= 任务静默丢失；误判「普通事务→任务」只是多一个文件，无害。

**目录命名**：kebab-case（小写+连字符），遵循 WORKSPACE.md 命名规范。

## Step 2：建项（创建 PROGRESS.md）

1. 在对应目录创建 PROGRESS.md（用 `templates/PROGRESS.md`）
2. 规划里程碑：把任务拆成 3-6 个里程碑（M1, M2, ...）
   - 里程碑 = 可独立验证的产出点，也是自动记忆的检查点
   - 规划后告知用户：「里程碑已规划，后续可按情况调整」
3. 写入目标、初始下一步、创建时间

**路径规则**：目录与文件位置一律服从 WORKSPACE.md（技能本身不硬编码路径）。

**自包含兜底（无 workspace-initializer 也能独立使用）**：
- 若 `tasks/` 或 `projects/` 目录不存在 → 自动 `mkdir -p` 创建
- 若工作区没有 WORKSPACE.md → 使用默认约定：工作区根下的 `tasks/` 与 `projects/`
- 若二者都存在 → 一律以 WORKSPACE.md 规范为准

## Step 3：里程碑更新（核心规则）

- **完成即写**：每完成一个里程碑，立即更新 PROGRESS.md——不等会话结束。跑死前最后一步没写 = 该步进度丢失，所以「完成即写」不是建议是纪律
- **原子写入**：先写临时文件再 rename（`.tmp` → 正式名），避免半截文件
- **幂等清单**：已完成步骤逐条记录（含时间戳）。恢复时从「下一步」开始，**不重复执行已完成步骤的副作用**（消息、写入、外部操作）
- **里程碑可调整**：任务中途发现规划不合理，更新 PROGRESS.md 的里程碑列表并注明调整原因

## Step 4：恢复（新会话启动检查）

AGENTS.md 的 Session Startup 必须包含「任务续跑检查」（模板见 `templates/AGENTS-startup-check.md`）：

1. 扫描 `tasks/` 与 `projects/` 下所有 `PROGRESS.md`
2. 找到状态为「进行中」的 → 读取内容
3. 向用户汇报：有哪些未完成任务、各自进度到哪、下一步是什么
4. 用户确认后从「下一步」续跑；用户未确认前**不擅自继续执行**（反馈至上铁律）

## Step 5：完成与归档

- 任务完成：PROGRESS.md 标记「已完成」+ 完成时间
- 有价值的决策/教训/经验 → 沉淀进 `memory/YYYY-MM-DD.md` 或 MEMORY.md（任务状态 ≠ 记忆，分层存放）
- PROGRESS.md 保留在任务目录（任务完结后目录原地保留，按 WORKSPACE.md 规则不删除）

## 与既有体系的关系

| 体系 | 分工 |
|------|------|
| **WORKSPACE.md** | 路径权威：目录结构、命名、输出位置一律以它为准 |
| **memory/ + MEMORY.md** | 记忆层：决策、教训、人脉、偏好（长期语义） |
| **PROGRESS.md** | 任务状态层：目标、里程碑、已完成清单、下一步（机械事实，可重建） |
| **[xiaoyaoclaw-workspace-initializer](https://github.com/dtsola/xiaoyaoclaw-workspace-initializer)** | 工作区规范底座；本技能是其「任务状态」扩展 |

## 边界（不做什么）

- 不替代 memory 日志（任务状态 ≠ 记忆）
- 不做自动续跑（恢复动作必须用户确认，符合反馈至上铁律）
- 不硬编码路径（一律走 WORKSPACE.md 仲裁）
- 不写密钥/凭证到 PROGRESS.md