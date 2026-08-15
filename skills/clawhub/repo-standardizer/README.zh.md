# GitHub Repo Standardizer

< [English](./README.md) | 简体中文 >

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/programmingWTF/repo-standardizer)](https://github.com/programmingWTF/repo-standardizer/releases)
[![GitHub issues](https://img.shields.io/github/issues/programmingWTF/repo-standardizer)](https://github.com/programmingWTF/repo-standardizer/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/programmingWTF/repo-standardizer)](https://github.com/programmingWTF/repo-standardizer/pulls)
[![GitHub stars](https://img.shields.io/github/stars/programmingWTF/repo-standardizer)](https://github.com/programmingWTF/repo-standardizer/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/programmingWTF/repo-standardizer)](https://github.com/programmingWTF/repo-standardizer/network)
[![GitHub contributors](https://img.shields.io/github/contributors/programmingWTF/repo-standardizer)](https://github.com/programmingWTF/repo-standardizer/graphs/contributors)

> **一个 Skill，一键把任何裸奔的 GitHub 仓库变成专业仓库——标签体系（段位强制 Emoji）、issue 表单、PR 模板、CI、规则集、文档，一条命令搞定。**
>
> **与 Agent 无关**：任何支持 skills 的 agent 都能用——Claude Code、Cursor、Copilot、OpenClaw 等。

别再每次开新项目都粘贴一大坨提示词了。这个 Skill 会检测仓库现状，然后幂等地应用一套专业基线：新仓库直接跑，老仓库也能补课。它永远不会覆盖你的内容。

---

## ✨ 功能

| 模块 | 作用 |
|---|---|
| 🏷️ **标签** | 完整标签体系的幂等 upsert——`P0`–`P3` 优先级、`impact: security` 影响评级、`bug`、`ready to merge`...（段位标签强制 Emoji），按项目画像定制 |
| 📋 **Issue 表单** | bug / feature / question 的 YAML 表单 + `config.yml` |
| 🔀 **PR 模板** | 带清单的结构化 PR 模板 |
| 🤖 **CI 工作流** | 自动探测测试框架（Node / Python / Go / Rust）并添加匹配的 GitHub Actions |
| 🛡️ **规则集** | 分支保护：强制 PR 审查、线性历史、禁止删除、强制签名 |
| 📚 **文档** | README（多语言）、`CONTRIBUTING.md`、`SECURITY.md`、`CODE_OF_CONDUCT.md`、`CHANGELOG.md`、`CODEOWNERS`、可选 MIT 许可证 |
| 🤖 **AI 指南** | 为仓库生成 `CLAUDE.md` 和 `AGENTS.md`，让 AI 助手一进来就知道规矩 |
| ✅ **验证** | 重新查询 GitHub 并输出 `applied / skipped / failed` 清单 |

## 🧠 安全设计

- **只动门面**：只碰标签、模板、CI 配置、规则集和文档——绝不碰源码逻辑。
- **登录优先**：动手前先查 `gh auth status`；没登录会明确告诉你怎么登录（或提供 token）。没 token 就不动。
- **仓库感知**：检测个人 vs 组织仓库、`public` vs `private` 可见性，并相应调整行为。
- **幂等**：跑两次结果一样。已有标签只更新不重复，已有模板先 diff 再决定，绝不覆盖。
- **先干跑后动手**：破坏性操作（规则集、分支规则、删除）前先给计划、要确认。

## 📦 安装

```bash
# 通过 skills CLI（任何 agent 都能用）
npx skills add programmingWTF/repo-standardizer

# 或通过 OpenClaw
openclaw skills install git:programmingWTF/repo-standardizer@main
```

依赖：`gh` CLI（已登录）、`git`、`jq` + `python3`（用于标签 URL 编码）。

## 🚀 使用

直接对你的 AI 说：

```text
Standardize the repo programmingWTF/repo-standardizer
```

或单独跑某个模块：

```text
Add issue forms and a PR template to my repo
Fix the labels on this repo to match the standard taxonomy
Protect the main branch with a ruleset requiring review
```

<details>
<summary><b>底层发生了什么？</b></summary>

1. **Preflight** — 验证登录（`gh auth status`）、检测仓库类型（`User` vs `Organization`、`PUBLIC` vs `PRIVATE`）、审计现状。
2. **Plan** — 展示一张表格：将创建 / 更新 / 跳过什么。
3. **Apply** — 按顺序执行各模块，每个都幂等。
4. **Verify** — 重新查询 GitHub 并输出最终清单。

</details>

## 📁 仓库结构

```text
.
├── SKILL.md               # Skill 本体
├── templates/             # 可复用模板
│   ├── labels.json        # 标签体系（颜色 + 描述）
│   ├── LABELS.md          # 段位标签说明文档模板
│   ├── issue-form-*.yml   # bug / feature / question 表单
│   ├── config.yml         # Issue 模板配置
│   ├── PR_TEMPLATE.md     # PR 模板
│   ├── ci-*.yml           # Node / Python / Go / Rust 工作流
│   ├── CODEOWNERS         # 默认负责人文件
│   ├── CONTRIBUTING.md    # 贡献指南
│   ├── SECURITY.md        # 安全政策
│   ├── CODE_OF_CONDUCT.md # 行为准则
│   ├── CLAUDE.md          # Claude Code 仓库指南模板
│   ├── AGENTS.md          # 通用 AI 助手指南模板
│   ├── VISION.md          # 项目愿景模板
│   ├── CHANGELOG.md       # Keep a Changelog 骨架
│   ├── README.md          # 新仓库 README 骨架（英文）
│   └── README.zh.md       # 新仓库 README 骨架（中文）
├── docs/                  # 项目文档
│   └── ARCHITECTURE.md    # Skill 架构说明
├── AGENTS.md              # AI 助手指南（根）
├── CLAUDE.md              # 指向 AGENTS.md 的软链接
├── VISION.md              # 项目愿景与方向
├── CHANGELOG.md           # 版本历史
├── THIRD_PARTY_NOTICES.md # 第三方声明
├── LICENSE
├── README.md              # 英文（默认）
└── README.zh.md           # 简体中文
```

## 🤝 贡献

欢迎 PR！提交规范参见 [CONTRIBUTING.md](CONTRIBUTING.md)（`type(scope): description`）。
发现 bug？用 [bug 表单](https://github.com/programmingWTF/repo-standardizer/issues/new?template=bug.yml) 报告。

## 📄 许可证

[MIT](LICENSE) © 2026 [programmingWTF](https://github.com/programmingWTF) & [LiGuiyu-AI](https://github.com/LiGuiyu-AI) — 桂鱼养的龙虾 🦞
