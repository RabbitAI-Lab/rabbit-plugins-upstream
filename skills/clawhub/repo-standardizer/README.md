# GitHub Repo Standardizer

< English | [简体中文](./README.zh.md) >

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/programmingWTF/repo-standardizer)](https://github.com/programmingWTF/repo-standardizer/releases)
[![GitHub issues](https://img.shields.io/github/issues/programmingWTF/repo-standardizer)](https://github.com/programmingWTF/repo-standardizer/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/programmingWTF/repo-standardizer)](https://github.com/programmingWTF/repo-standardizer/pulls)
[![GitHub stars](https://img.shields.io/github/stars/programmingWTF/repo-standardizer)](https://github.com/programmingWTF/repo-standardizer/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/programmingWTF/repo-standardizer)](https://github.com/programmingWTF/repo-standardizer/network)
[![GitHub contributors](https://img.shields.io/github/contributors/programmingWTF/repo-standardizer)](https://github.com/programmingWTF/repo-standardizer/graphs/contributors)

> **One command polishes any GitHub repo's surface — label taxonomy (emoji rating tiers), issue forms, PR template, CI, rulesets, docs. Repo meta & config only, no code logic touched.**
>
> **Agent-agnostic**: works with any skills-enabled agent — Claude Code, Cursor, Copilot, OpenClaw, and more.

Stop pasting the same wall of prompts every time you start a new project. This skill detects the current state of a repository and applies a professional baseline **idempotently**: run it on a fresh repo, or run it on an old repo to fill in what's missing. It never clobbers your content.

---

## ✨ Features

| Module | What it does |
|---|---|
| 🏷️ **Labels** | Idempotent upsert of a full label taxonomy — `P0`–`P3` priority, `impact: security` severity, `bug`, `ready to merge`... (rating tiers always emoji) |
| 📋 **Issue forms** | YAML issue forms for bug / feature / question + `config.yml` |
| 🔀 **PR template** | Structured pull request template with checklist |
| 🤖 **CI workflows** | Auto-detects your test framework (Node / Python / Go / Rust) and adds a matching GitHub Actions workflow |
| 🛡️ **Rulesets** | Branch protection: required PR review, linear history, no deletions, required signatures |
| 📚 **Docs** | README badges, `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`, `CODEOWNERS`, optional MIT license |
| ✅ **Verification** | Re-queries GitHub and prints an `applied / skipped / failed` checklist |

## 🧠 Safety by design

- **Surface-only**: touches labels, templates, CI configs, rulesets, and docs — never source code logic.
- **Auth-first**: checks `gh auth status` before anything; if you're not logged in, it tells you exactly how to log in (or provide a token). No token → no action.
- **Repo-aware**: detects personal vs. organization repos and `public` vs. `private` visibility, and adapts what it does.
- **Idempotent**: run it twice, get the same result. Existing labels are updated, not duplicated; existing templates are diffed, not overwritten.
- **Dry-run first**: shows a plan and asks for confirmation before destructive operations (rulesets, branch rules, deletions).

## 📦 Installation

```bash
# via the skills CLI (works with any agent)
npx skills add programmingWTF/repo-standardizer

# or via OpenClaw
openclaw skills install git:programmingWTF/repo-standardizer@main
```

Requires: `gh` CLI (authenticated), `git`, and `jq` + `python3` for label encoding.

## 🚀 Usage

Just ask your agent:

```text
Standardize the repo programmingWTF/repo-standardizer
```

Or run modules selectively:

```text
Add issue forms and a PR template to my repo
Fix the labels on this repo to match the standard taxonomy
Protect the main branch with a ruleset requiring review
```

<details>
<summary><b>What happens under the hood?</b></summary>

1. **Preflight** — verify login (`gh auth status`), detect repo type
   (`User` vs `Organization`, `PUBLIC` vs `PRIVATE`), audit current state.
2. **Plan** — show a table of what will be created / updated / skipped.
3. **Apply** — run modules in order, each idempotent.
4. **Verify** — re-query GitHub and report the final checklist.

</details>

## 📁 Repository layout

```text
.
├── SKILL.md               # The skill itself
├── templates/             # Reusable templates
│   ├── labels.json        # Label taxonomy (color + description)
│   ├── LABELS.md          # Rating-label documentation template
│   ├── issue-form-*.yml   # Bug / feature / question forms
│   ├── config.yml         # Issue template config
│   ├── PR_TEMPLATE.md     # Pull request template
│   ├── ci-*.yml           # Node / Python / Go / Rust workflows
│   ├── CODEOWNERS         # Default owners file
│   ├── CONTRIBUTING.md    # Contribution guide
│   ├── SECURITY.md        # Security policy
│   ├── CODE_OF_CONDUCT.md # Code of conduct
│   ├── CLAUDE.md          # Claude Code guide template
│   ├── AGENTS.md          # Generic AI-agent guide template
│   ├── VISION.md          # Project vision template
│   ├── CHANGELOG.md       # Keep-a-Changelog skeleton
│   ├── README.md          # README skeleton (English)
│   └── README.zh.md       # README skeleton (简体中文)
├── docs/                  # Project docs
│   └── ARCHITECTURE.md    # Skill architecture
├── AGENTS.md              # AI-agent guidance (root)
├── CLAUDE.md              # symlink → AGENTS.md
├── VISION.md              # Project vision & direction
├── CHANGELOG.md           # Release history
├── THIRD_PARTY_NOTICES.md # Third-party attributions
├── LICENSE
├── README.md              # English (default)
└── README.zh.md           # 简体中文
```

## 🤝 Contributing

PRs welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for conventions.
Found a bug? Use the [bug report form](https://github.com/programmingWTF/repo-standardizer/issues/new?template=bug.yml).

## 📄 License

[MIT](LICENSE) © 2026 [programmingWTF](https://github.com/programmingWTF) & [LiGuiyu-AI](https://github.com/LiGuiyu-AI) — the friendly lobster 🦞
