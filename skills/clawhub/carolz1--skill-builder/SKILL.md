---
name: skill-builder
description: 制作、修改、优化或审查 Skill 的通用技能，跨平台、不绑定特定 AI 生态。当用户想「把重复工作流/想法做成 skill」「帮我做个 skill」「优化/审查一个 skill」「这个 skill 触发不了帮我看看」，或提到 skill 制作、skill 优化、skill 评分时使用。即使对方没有明确说「skill」这个词，只要在描述一个想固化下来的重复流程，也主动使用本技能。Build, modify, optimize, or review skills; use when the user wants to turn a repetitive workflow or idea into a skill, or to improve/review an existing skill.
version: 1.0.0
agent_created: true
---

# Skill Builder / Skill 制作器

A cross-platform guide for creating skills from scratch and improving existing ones.
跨平台的 Skill 制作器：从零做 skill，或优化已有 skill。

## Environment probe / 环境探测（先探测，不假设）

Before starting, silently probe the host's capabilities. Do not assume you have subagents, a CLI, a browser, or scripts. Each missing capability degrades to a fallback, never a hard failure. Do not report probe results to the user unless it materially changes the experience.

开始前静默探测宿主能力，不默认拥有子代理、CLI、浏览器或脚本。缺什么就降级，不报错。探测结果只在影响体验时才告诉用户。

| Capability 能力 | Has it 有 | Missing → fallback 无 → 降级 |
|---|---|---|
| Parallel subtasks 并行子任务 | 并行跑对照 | 串行跑两遍 |
| CLI model call CLI 模型调用 | 脚本优化触发词 | 用静态清单直接改（默认） |
| Browser/preview 浏览器/预览 | HTML 评测器 | 对话内联展示结果 |
| Python + filesystem Python+文件系统 | 跑打包/校验脚本 | 只给内容和手抄说明 |

## Path selection / 路径选择

默认走「轻量路径」。只有用户明确要生产级评测、benchmark、或 skill 属于「客观可验证输出」且要上生产时，才升到「完整路径」。用户随时可说「走轻量」或「走完整」切换。

Default to the light path. Upgrade to the full path only when the user wants production-grade evaluation, benchmarking, or the skill has objectively verifiable outputs going to production. The user can switch at any time.

- **轻量路径 Light（默认）**：挖需求 → 写 SKILL.md → 快速自测 → 交付。反问 ≤ 2 次。
- **完整路径 Full（可选）**：轻量 + 评测 + 对照 + benchmark。按需反问。

## 交互原则 / Interaction principles

Frequent back-and-forth questions annoy users. Follow these rules to keep it low-friction.

频繁反问会打扰用户。遵守以下规则保持低打扰：

1. **合并提问 / Merge questions**：把「做什么/何时触发/输出格式/要不要测试」压缩成一次结构化确认，不要一轮问一个。
2. **给默认值 / Provide defaults**：测试要不要？按类型默认——文件转换/数据抽取→默认测；写作/艺术→默认不测。一句「默认按 X，要改说一声」即可。
3. **能自己查的不问 / Research don't ask**：依赖、最佳实践、边界情况默认自己去查，查完汇报，不反问。
4. **先跑再评价 / Run then review**：测试用例不必先让用户签字，先跑一版，把结果摆出来让用户评价——评价比预先确认省心。
5. **只问影响下一步的 / Ask only what matters next**：一次只问一个关键问题，已有信息不重复问。

---

## Creating a skill / 制作新 skill

### Step 1: Capture intent / 抓取意图

First, extract intent from the conversation. The current conversation may already contain the workflow the user wants to capture (e.g. "turn this into a skill"). Extract tools used, step sequence, corrections made, and I/O formats observed. Then produce a **one-shot structured confirmation** — fill in defaults yourself, list them once, let the user correct in one pass.

先从对话里抓意图。对话里可能已经有用户想固化的流程（例如「把这个做成 skill」）。抽取用到的工具、步骤顺序、用户纠正、输入输出格式。然后**一次性结构化确认**——自己填好默认值，一次列出，让用户一轮改完。

```
我理解你要做 X，默认这样处理：
- 做什么：______
- 何时触发（用户说什么话）：______
- 输出格式：______
- 测试：默认要/不要（按类型）
哪里不对直接说，一次改完。
```

### Step 2: Fill in the SKILL.md / 填写 SKILL.md

Based on the confirmed intent, write the skill. Follow the structure and writing rules in `references/skill-structure-guide.md`. Read it before writing.

按确认的需求写 skill。先读 `references/skill-structure-guide.md`，遵循其目录结构、渐进披露和写作风格规则。

### Step 3: Write the description / 写触发词

The `description` field is the primary trigger mechanism. Follow `references/trigger-writing-guide.md` to write a description with all four elements (what / when / capability / trigger phrases) and anti-undertrigger wording. Read it before writing.

`description` 是首要触发机制。先读 `references/trigger-writing-guide.md`，按四要素 + 反欠触发写法写 description。

### Step 4: Quick self-test / 快速自测（轻量路径）

Light path: read the SKILL.md yourself once, then verify with 1—2 real prompts that it would trigger and its steps are followable. No benchmark, no baseline comparison.

轻量路径：自己通读一遍 SKILL.md，再用 1—2 个真实 prompt 验证「能触发、步骤能走通」。不做 benchmark，不做对照。

Full path: see "Evaluation" below.

完整路径：见下方「评测」。

### Step 5: Quality check / 质量自检

Run the checklist in `references/quality-checklist.md`. Light path does the core items; full path does all items.

跑 `references/quality-checklist.md` 的自检。轻量路径做核心项，完整路径做全部项。

---

## Improving an existing skill / 优化已有 skill

When the user brings an existing skill draft or finished skill, don't re-ask "what do you want to make". Jump straight to review.

用户带着成品或草稿来时，不要重新问「你想做什么」，直接进入审查。

1. **Read it / 通读**：读 SKILL.md 全文，理解定位、流程和边界。
2. **Diagnose / 诊断**：按 `references/quality-checklist.md` 逐项检查，找出具体问题，用「文件+证据」说话，不空泛好评。
3. **Prioritize / 分级**：给 P1（阻断）/ P2（应修）/ P3（建议）清单，每条附直接证据和改法。
4. **Confirm before editing / 修改前确认**：展示修复项、目标文件、影响和回滚方式，用户确认后再改。只修确认过的问题，不顺手重构。
5. **Re-test / 复测**：改完重跑相关检查，输出前后对照。

Key discipline / 关键纪律：修改前先备份旧版；只保留当前有效规则，不留改动痕迹、版本标注或历史 log。

---

## Evaluation / 评测（完整路径专属 / full path only）

Only run this when on the full path. Skip entirely on the light path.

只在完整路径执行，轻量路径跳过。

1. Write 2—3 realistic test prompts (real user wording) + 1—2 near-miss prompts. Save to `evals/evals.json` (prompts only, no assertions yet).
   写 2—3 条真实测试 prompt + 1—2 条 near-miss，存 `evals/evals.json`（先只写 prompt，不写断言）。
2. Run each prompt with the skill and without the skill (baseline). Use parallel subtasks if available, otherwise run twice serially.
   每条 prompt 跑「带 skill」和「不带 skill」两个版本。有并行就并行，没有就串行跑两遍。
3. Grade results: does the with-skill output show observable improvement (completeness, structure, fewer questions, gotchas handled)? Present results inline in the conversation — do not require a browser.
   评分：带 skill 的输出是否有可观察增量（完整度、结构、追问数、坑处理）？结果在对话内联展示，不强制浏览器。
4. Summarize findings and improve the skill based on feedback. Then rerun.
   汇总发现，据此改进 skill，再重跑。

Baseline rule / 基线规则：新建 skill 的基线是「无 skill」；优化已有 skill 的基线是「旧版本」（先快照备份旧版）。

---

## 交付 / Delivery

1. Run the quality checklist once more.
   再跑一遍质量自检。
2. Present the finished skill folder to the user. If a packaging script is available, package it; otherwise just give the folder path and file list.
   把完成的 skill 文件夹交给用户。有打包脚本就打包，没有就只给目录路径和文件清单。
3. Offer installation (see below).
   随后询问是否安装（见下）。

## 安装 / Installation

- Target location is always user-level `~/.workbuddy/skills/<name>/`.
  安装位置统一为用户级 `~/.workbuddy/skills/<name>/`。
- Before installing, show a preview: target path, what gets overwritten, backup location, rollback method. Install only after the user's separate install confirmation.
  安装前先预览：目标路径、覆盖对象、备份位置、回滚方式。用户独立确认后才执行。
- Same-name update: verify version incremented, back up first, then atomically replace; roll back on failure.
  同名更新：确认 version 自增、先备份、原子替换，失败回滚。

---

## Reference files / 参考文件

Load these on demand — only when writing or reviewing.

按需加载，仅在写作或审查时读取：

- `references/trigger-writing-guide.md` —— 触发词静态清单（写 description 时读）
- `references/skill-structure-guide.md` —— 目录结构、渐进披露、写作风格（写正文时读）
- `references/quality-checklist.md` —— 自检清单（交付前读）

## 核心循环回顾 / The core loop, restated

- Figure out what the skill is about / 弄清 skill 要做什么
- Draft or edit the skill / 起草或修改
- Run a quick self-test (light) or full evaluation (full) / 快速自测（轻量）或完整评测（完整）
- Improve with the user, keep questions minimal / 与用户一起改进，反问最少化
- Deliver and offer install / 交付并询问安装
