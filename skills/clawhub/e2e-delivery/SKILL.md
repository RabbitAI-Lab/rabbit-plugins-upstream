---
name: e2e-delivery
description: >
  端到端需求/缺陷交付驱动器：给定一个 PingCode 工作项 URL/ID 或自然语言描述，自动串联"准备→开发→提交→验证→交付"五个阶段，
  并沿路埋点，流程结束时产出 Markdown 报告并同步到 REDoc。
  触发条件（满足任一即触发）：
  (1) 用户说「帮我交付需求 xxx」「跑一遍端到端交付」「driver e2e」；
  (2) 用户给出 PingCode 工作项链接/ID 并表达"从头做到尾"的意图；
  (3) 用户自然语言描述一个新需求/缺陷、希望一站式完成。
  不触发：仅查看工作项详情（由 pingcode-assistant-pro 处理）、仅创建 MR（由 yunxiao-assistant 处理）、
  只想跑单一步骤（如只提测、只合并）。
metadata:
  openclaw:
    requires:
      bins:
        - ee-cli
        - hi
        - git
---

# e2e-delivery — 端到端交付驱动器

## 核心理念

给定一个需求（PingCode URL/ID 或自然语言描述），本 skill 按固定五阶段推进：**准备 → 开发 → 提交 → 验证 → 交付**。全流程的每一步都会写入 session 文件；遇到人工必需的节点（部署、CR 触发）阻塞等待用户回复"继续"；流程结束自动出报告。

## 入口识别

启动时首先判断输入模式：

- **模式 A**：输入是 URL（如 `https://pingcode2.devops.xiaohongshu.com/work-item-detail/951526`）或纯数字 ID（如 `951526`）→ 直接 `ee-cli pingcode workitem get <id>` 获取详情
- **模式 B**：输入是自然语言描述（如"帮我做一个 xxx 功能"）→ 委托 `pingcode-assistant-pro` 走"创建工作项"流程，拿到 ID 后进入主流程；session 标记 `workItem.createdBySkill: true`

## Session 文件规约

**路径**：`~/.claude/e2e-sessions/<workitem-id>.json`

**首启动**：
1. 若 workitem 已有 session 文件 → 询问用户"发现历史 session（在 xx 阶段），是恢复还是重开？"
2. 恢复 → 从 `currentPhase` 起点重放；重开 → 备份旧文件为 `<id>.json.bak.<timestamp>`，重新初始化
3. 无 session → 初始化新文件（结构见 `references/session-schema.md`）

**写规约（硬约束）**：
- **所有对 session 的写操作必须走 `scripts/session.py` 脚本**，禁止 inline python 手拼 JSON
- 每步执行前 `session.py step-start`，执行后 `step-end`（`--result` 必填）
- 遇到人工阻塞 `gate-wait`，用户回复继续时 `gate-resume`
- 阶段切换 `phase-start` / `phase-end`
- 命令详情见 `references/session-schema.md`「写入操作」章节
- 手写 JSON 会导致 `durationMs`、`updatedAt`、`waitDurationMs` 等字段缺失，直接影响报告质量

**详细 schema**：见 `references/session-schema.md`。

## 五阶段流程

| 阶段 | 目标 | 关键动作 |
|------|------|---------|
| ① 准备 | 有一个可开发的工作项 | 环境预检、载入 session、工作项就绪 |
| ② 开发 | 代码已推送到远端 | 切分支、编码、本地检查、提交推送 |
| ③ 提交 | 代码进入评审 & 测试通道 | 创建 MR、关联工作项、发起提测 |
| ④ 验证 | 功能可用 + 代码经过 review | 部署（人工）、状态确认、功能验证、CR review |
| ⑤ 交付 | 交付完成，留下可追溯的报告 | Approve、合并、状态流转、生成报告 |

**每阶段的详细步骤、决策点、命令示例**：见 `references/flow.md`。

## 关键行为约定

1. **阻塞式人工介入**：遇到 CLI 无法自动完成的节点（如提测单处于"测试中"需等测试人完成、非本人拥有的资源需授权者操作），落 `human_gate_waiting` 事件后交出控制权，明确告诉用户该做什么、如何回复继续。
2. **失败即中断**：任何 step 失败，中断流程，向用户展示错误、当前进度、已完成步骤，让用户决定继续/重试/放弃。已完成事件已落盘，下次可从 session 恢复。
3. **CLI 优先**：能用 ee-cli / hi 直接完成的，不要包一层子 skill 调用。子 skill 只在需要"决策智慧"时触发（例如创建工作项、创建 REDoc 文档）。
4. **workitem 类型校验**：模式 A 拿到 workitem 后，若类型是 `task`（需求），到「关联工作项」这一步会阻断——云效要求 MR 只能关联子任务/缺陷。此时 skill 自动创建服务端子任务（沿用父需求的 workspace/owner/business_line 默认值）并关联，避免人工介入。
5. **合并前双重硬校验**（`flow.md` Step 5.0 + Step 5.2）：`cr merge` 之前必须先 `test-submission get` 校验提测单状态（Step 5.0），再 `cr checklist` 复核所有服务端卡点（Step 5.2）。任一未通过一律阻塞。**违反此约束会导致代码在测试未通过 / 卡点未清情况下合入，是严重流程 bug。**

## 环境预检

**必须在流程开始前完成**。详见 `references/env-precheck.md`。要点：

- CLI（ee-cli、hi）未安装 → 主动安装；非最新 → 主动升级
- Skill（pingcode-assistant-pro、yunxiao-assistant、hi-docs）未安装/非最新 → 主动安装/升级
- SSO 认证失效 → 引导 `ee-cli login`
- 无法自动修复 → 报清晰错误阻断，绝不静默降级

## 子 skill 调用规约

- 能用 CLI 直接完成就用 CLI，不套 `Skill(...)` 二次调用
- **pingcode-assistant-pro**：仅在"创建工作项"（模式 B）时调用
- **hi-docs**：仅在"生成报告并同步 REDoc"时调用
- **yunxiao-assistant**：一般不主动调用；仅在遇到复杂决策（如 AI 评论标记的准出逻辑）需引导 AI 深入了解时提示

## 报告生成

在 ⑤ 交付阶段的最后一步触发。渲染逻辑与模板见 `references/report-template.md`。要点：

- 本地 MD 写入 `docs/e2e-reports/<workitem-id>-<yyyymmdd>.md`（相对当前项目根目录）
- 同步到 REDoc（用户配置的 `redocParentId`，见 `~/.claude/e2e-delivery/config.json`）
- REDoc 失败不阻断本地 MD 产出

## 常见问题

见 `references/troubleshooting.md`。
