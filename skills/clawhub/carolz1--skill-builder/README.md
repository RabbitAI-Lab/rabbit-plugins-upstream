# Skill Builder / Skill 制作器

> Build, modify, optimize, or review AI agent skills — cross-platform and ecosystem-agnostic, with a low-friction interaction model. / 跨平台、不绑定生态的 Skill 制作器：创建、优化、审查智能体技能，交互低打扰。

**English** | [中文说明](#中文说明)

## What it is

A meta-skill for making skills. It turns repetitive workflows and ideas into well-structured skill packages, improves existing ones, and reviews drafts — following the philosophy of minimal back-and-forth and capability-probing with graceful degradation.

## Two paths

- **Light path (default) / 轻量路径（默认）** — capture intent → write SKILL.md → quick self-test → deliver. At most 2 clarifying questions, with sensible defaults stated up front
- **Full path (optional) / 完整路径（可选）** — adds evaluation: real test prompts, with-skill vs. without-skill baseline comparison, benchmark reruns. Only for production-grade skills with objectively verifiable outputs

## Key features

- **Environment probing / 环境探测** — silently detects host capabilities (parallel subtasks, CLI model calls, browser preview, Python filesystem); anything missing degrades to a fallback instead of failing
- **Low-friction interaction / 低打扰交互** — merge questions into one structured confirmation; provide defaults by skill type; research instead of asking; run first, review after
- **Trigger-word engineering / 触发词工程** — the `description` field is the primary trigger mechanism; a dedicated guide covers the four elements (what / when / capability / trigger phrases) and anti-undertrigger wording
- **Structure guide / 结构指南** — directory layout, progressive disclosure, writing style for SKILL.md bodies
- **Quality checklist / 质量自检** — run before delivery; light path checks core items, full path checks all
- **Safe improvement / 安全优化** — existing skills get diagnosed with evidence (P1/P2/P3), confirmed before editing, backed up before changes, re-tested after

## Repository structure

```
├── SKILL.md                            # Main skill instructions / 主指令
└── references/
    ├── skill-structure-guide.md        # Structure & writing style / 结构与写作风格
    ├── trigger-writing-guide.md        # Description/trigger writing / 触发词写作
    └── quality-checklist.md            # Pre-delivery checklist / 交付前自检
```

## Usage

Drop the folder into your agent's skills directory. Use when you want to "turn this workflow into a skill", "帮我做个 skill", optimize or review an existing skill — even if the word "skill" is never mentioned.

---

# 中文说明

## 这是什么

一个「做技能的技能」。把重复工作流和想法固化为结构良好的 skill 包，也能优化和审查已有 skill。设计哲学：交互低打扰、先探测能力再降级。

## 两条路径

- **轻量路径（默认）**：抓意图 → 写 SKILL.md → 快速自测 → 交付。反问 ≤ 2 次，默认值先给足
- **完整路径（可选）**：加评测——真实测试 prompt、带/不带 skill 基线对照、benchmark 重跑。只用于要上生产、输出客观可验证的 skill

## 核心特性

- **环境探测**：静默探测宿主能力（并行子任务、CLI 调用、浏览器、Python），缺什么就降级，不报错
- **低打扰交互**：问题合并成一次结构化确认；按类型给默认值；能查不问；先跑再评价
- **触发词工程**：`description` 是首要触发机制，专门指南覆盖四要素与反欠触发写法
- **结构指南**：目录结构、渐进披露、SKILL.md 写作风格
- **质量自检**：交付前必跑；轻量查核心项，完整查全部
- **安全优化**：证据说话（P1/P2/P3 分级）、改前确认、改前备份、改后复测

## 使用方式

放入智能体 skills 目录。想「把重复流程做成 skill」「帮我做个 skill」「优化/审查一个 skill」时使用——即使没说出 skill 这个词。
