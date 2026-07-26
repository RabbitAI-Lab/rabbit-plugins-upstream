---
name: agent-orchestrator
description: "多代理协同编排系统。源自 Claude Code 的 AgentTool / forkSubagent / spawnMultiAgent / TeamCreate/Delete / mailbox 架构。支持三种后端（tmux split-pane、tmux separate-window、in-process）、扇出并行、串行流水线、代理团队、任务分配与结果汇聚。使用 sessions_spawn 作为 OpenClaw 的 in-process 后端。"
metadata:
  openclaw:
    emoji: "🐙"
    requires:
      bins: []
---

# Agent Orchestrator 🐙

> 源自 Claude Code 的多代理系统源码（1900+ 文件，51万行）。
> Claude Code 使用三种 spawn 后端：tmux 分屏 / tmux 独立窗口 / 同进程(in-process)。
> 在 OpenClaw 中，`sessions_spawn` 就是 in-process 模式。

## Claude Code 的 spawn 架构

### 三种 spawn 模式

| 模式 | 实现 | 特点 | 适用场景 |
|------|------|------|---------|
| **in-process** | 同一 Node.js 进程运行子代理 | 轻量、无缝、无终端开销 | 简单子任务、快速并行 |
| **split-pane** | tmux/iTerm2 分屏 | 可视化、可交互 | 需要观察子代理实时输出 |
| **separate-window** | tmux 独立窗口 | 隔离性强 | 长时间运行的后台任务 |

### 子代理生命周期

1. **创建**: spawnTeammate(name, prompt, config)
2. **注册**: 写入 team file (JSON) + 注册到 appState.teamContext
3. **沟通**: mailbox 系统（基于文件的消息队列）
4. **跟踪**: Task 系统（registerTask）
5. **清理**: 任务完成后自动清理

### 团队系统

```
TeamCreate(name, description)
  ├── 创建 team file (~/.claude/teams/<name>.json)
  ├── 每个成员有: agentId, name, color, model, prompt, role
  ├── 团队成员通过 mailbox 收发消息
  └── TeamDelete(name) 销毁团队
```

---

## OpenClaw 实现

### 模式1: 扇出并行 (Fan-Out)

```python
# 伪代码 - 用 sessions_spawn 实现
# 主代理分配 N 个子任务
子代理结果 = [sessions_spawn(task_i) for i in range(N)]
# 汇总结果
最终输出 = 汇总(子代理结果)
```

**触发词**: "并行分析", "同时查", "分开处理", "扇出"

### 模式2: 串行流水线 (Pipeline)

```python
步骤1结果 = sessions_spawn(任务1)
步骤2结果 = sessions_spawn(任务2, context=步骤1结果)
步骤3结果 = sessions_spawn(任务3, context=步骤2结果)
```

**触发词**: "先...再...", "然后", "依次", "流水线"

### 模式3: 主控协调 (Coordinator)

```python
# 主代理分配任务给专业子代理
搜索代理 = sessions_spawn("搜索任务")
分析代理 = sessions_spawn("分析任务")
写作代理 = sessions_spawn("写作任务")
# 等待所有完成
全部结果 = 收集结果([搜索代理, 分析代理, 写作代理])
```

**触发词**: "分配任务", "组建团队", "分工协作"

---

## Claude Code 的关键设计模式

### 1. 工具权限传播
子代理继承主代理的权限模式（bypass/acceptEdits/auto），但 plan mode 优先级更高。

### 2. 模型继承
子代理默认使用主代理的模型，但可以单独指定。

### 3. 邮箱系统 (Mailbox)
```
主代理 --mailbox--> 子代理: 分配任务
子代理 --mailbox--> 主代理: 报告进度
子代理 --mailbox--> 子代理: 横向通信
```

### 4. 颜色编码
每个子代理分配唯一颜色，便于在终端UI中区分。

---

## 使用示例

### 示例1: "帮我并行分析这三个文件"
```
sessions_spawn("分析文件A.py")
sessions_spawn("分析文件B.py")
sessions_spawn("分析文件C.py")
→ 汇总三个结果
```

### 示例2: "先调研技术方案，再写代码，最后生成文档"
```
研究 → sessions_spawn("研究技术方案")
代码 → sessions_spawn("写代码", context=研究结果)
文档 → sessions_spawn("生成文档", context=代码)
```

## 注意事项

- 扇出不超过 5 个子代理（token 开销与上下文污染）
- 子代理任务描述要精确，包含必要的上下文
- 状态检查用 `sessions_list` + `process(poll)` 避免忙等待
- 不要用多代理做简单的单步骤任务
