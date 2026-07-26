# Skill 维护指南（agentskills.io 对齐）

> 给人 / 维护 Agent 读。运行时用户任务**不要**加载本文件。

对齐：[Agent Skills Specification](https://agentskills.io/specification)、[Best practices](https://agentskills.io/skill-creation/best-practices)、[Optimizing descriptions](https://agentskills.io/skill-creation/optimizing-descriptions)、[Evaluating skills](https://agentskills.io/skill-creation/evaluating-skills)。

## 四层职责（禁止写错层）

| 层 | 写什么 | 禁止写什么 |
| -- | ------ | ---------- |
| 1 `SKILL.md` | 意图路由表、即时规范（Gotchas）、加载一句话 | 安装长文、完整参数表、业务流程细节、双规范路径 |
| 2 `agent-conventions.md` | 加载纪律、数据处理、时间/币种、自检、**§十四怎么回复用户** | 具体 CLI 选项表、某 P/W 的编号步骤 |
| 3 命令 reference | CLI 语法、选项表、字段/JSON 路径、易错口径；文首「流程见 playbooks/workflows Xxx」 | 「先做 A 再做 B」长流程、完整报告纲要、用户话术模板 |
| 4 playbooks/workflows | `触发 / 必读 / 编号步骤 / 产物`；步骤只写命令名+关键 flag | 完整参数表、重复 conventions 正文、suggestion chips 全文清单 |

报告结构细节仍在 `report-templates/*.md`（由层 4「必读」指向）。`intent-routing.md` 只做消歧，不进层 2。

## 硬约束

| 项 | 规则 |
| -- | ---- |
| `name` | 小写+连字符，与安装目录一致，≤64 |
| `description` | ≤1024 字符；第三人称；WHAT + WHEN + 负向触发；细则路由放 body / `intent-routing.md`，**勿塞进 description** |
| `SKILL.md` | 建议 <200 行本仓库目标 / 官方 <500 行；只做层 1 |
| 引用深度 | 从 `SKILL.md` **一层**指向 `references/*`；避免 A→B→C 嵌套链 |
| 长 reference | >100 行须有 `## Contents`；按域拆成 2–3 个聚焦模块优于巨型单文件 |
| 脚本 | 脆弱/重复逻辑放 CLI 或 `scripts/`，勿让模型每次重写 |
| 沟通规范 | 只维护在 `agent-conventions.md` §十四；`user-communication-guide.md` 仅 stub |

## 本仓库编辑流

1. 只改 `tso-cli/assets/siluzan-ads/`（勿改安装副本）。
2. 改 `SKILL.md.tmpl` 或 `snippets/agent-preamble.md` 后：`node scripts/gen-skill-docs.mjs`。
3. 业务细则进对应域 `references/`（层 3）；工作流卡片进 `playbooks.md` / `workflows.md`（层 4）。
4. 通用纪律与沟通只写在 `agent-conventions.md`（层 2），其他文档单行指向。
5. 验证：`skills-ref validate`（若已装）+ `pnpm run eval:skill -- --stub` 相关场景。

## Progressive disclosure（本 skill）

1. L1 触发：`name` + `description`
2. 层 1 body：`SKILL.md` 路由表 + 即时规范
3. 层 2–4：按路由表 Read conventions（按需）+ **一个**工作流卡片 + **一个** leaf 命令 reference

## 评测建议

- Description：准备 should-trigger / should-not-trigger 查询（见官方 optimizing-descriptions）。
- 输出：`tso-cli/eval/cases/*.scenario.json` + skill-eval harness；改路由后跑相关 stub 场景防回归。
