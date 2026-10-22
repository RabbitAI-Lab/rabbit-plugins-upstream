---
name: skill-skeleton-generator
description: One-command generator for LGD-compliant AI skill skeletons (SKILL.md + AGENTS.md + dirs). 一键生成符合 LGD 三律的 AI 技能骨架。
slug: skill-skeleton-generator
title: skill-skeleton-generator
version: 1.0.1
license: MIT
category: AI工程
author: SynomosAI (LGD initiative)
platforms: [windows, macos, linux]
tags: [skill, skeleton, generator]
description_zh: "一键生成符合 LGD 三律/四角度合规的新技能骨架（SKILL.md + AGENTS.md），规范化 frontmatter 起步。"
description_en: "One-command generator for LGD-compliant AI skill skeletons (SKILL.md + AGENTS.md + dirs) with full frontmatter scaffolding."
read_when:
  - 从零一键生成 LGD 三律/四角度合规的新技能骨架
  - 规范化 frontmatter（name/description/license/version/category/tags/slug/risk_tier）起步新技能
risk_tier: medium
ai_protocol: true
spec: usk/1.0
interface:
  type: cli
  entry_point: scripts/skeleton.py
  runtime: python3
  call_pattern: args
input_schema:
  args:
    type: string
    description: CLI arguments per skill usage
    required: false
output_schema:
  stdout: structured result (JSON IR)
  exit_code: rc=0 ok / rc=1 warning / rc=2 bad input
capabilities:
- scaffold
- skeleton
- codegen
permissions:
  network: false
  filesystem: false
  subprocess: false
requirements:
  python_packages: []
  min_python: '3.8'
changelog: '1.0.1: Bilingual rewrite (full EN+ZH, English first); 1.0.0: initial upload (USK v3)'
---

> 凡自治之物 · LGD 治理学 · 创造术家族 ｜ 评测协议：skill-quality-gate

## English

### Capabilities
- Generates SKILL.md with full frontmatter (name/description/license/version).
- Creates a machine-readable AGENTS.md entry and target directories.
- Four-angle (REG / TRUST / SAFE / MACH) compliant by construction.

### When to use
- Generate a new LGD-compliant skill skeleton from scratch (SKILL.md + AGENTS.md).
- Start a new skill with standardized frontmatter.

### Usage
```bash
python scripts/skeleton.py --name my-skill --description "..." [--out dir]
```

### Flow
1. Run `skeleton.py --name <skill> --description <desc> [--cat AI工程] [--out <dir>]`.
2. The script emits a SKILL.md with full frontmatter from an in-built TEMPLATE plus a machine-readable AGENTS.md.
3. Human edits the placeholder content (core capability / verification / usage) before entering the next quality gate.

### Evidence & safety
- Evidence: TBD. Version: 1.0.1. Security: no independent scan (TBD).

## 中文

### 功能
- 生成含完整 frontmatter 的 SKILL.md。
- 创建 AGENTS.md 机器可读入口与目录。
- 天然满足四角度合规（有籍/有证/有门禁/可机器读）。

### 何时用
- 当需要从零一键生成符合 LGD 三律/四角度合规的新技能骨架（SKILL.md + AGENTS.md）时使用本技能。
- 当需要规范化 frontmatter（name/description/license/version/category/tags/slug/risk_tier）起步一个新技能时使用本技能。

### 用法
```bash
python scripts/skeleton.py --name my-skill --description "..." [--out dir]
```

### 流程
1. 运行 `python scripts/skeleton.py --name <技能名> --description <描述> [--cat AI工程] [--out <输出目录>]`。
2. 脚本按内建 TEMPLATE 生成含完整 frontmatter 的 SKILL.md，并生成机器可读 AGENTS.md。
3. 人工编辑生成件中的占位内容（核心能力/验证/用法）后再进入后续质量门。

### 证据与安全声明
- 证据：TBD（暂无评测/徽章链接；产生后在此更新实际链接）
- 版本：1.0.1
- 安全：未做独立安全扫描（TBD），结论待补；补全前不作推荐背书。
