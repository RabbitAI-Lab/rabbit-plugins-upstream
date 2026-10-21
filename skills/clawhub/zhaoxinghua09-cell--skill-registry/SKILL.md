---
name: skill-registry
description: 'Generate a single source of truth for your skill collection: scan skills dir into JSON + Markdown registry. 生成技能集合的单一真源：扫描技能目录 → JSON + Markdown 注册表。'
slug: skill-registry
title: skill-registry
version: 1.0.1
license: MIT
category: 治理
author: SynomosAI (LGD initiative)
platforms: [windows, macos, linux]
tags: [skill, registry]
description_zh: "生成技能集合的单一真源：扫描技能目录 → JSON + Markdown 注册表，跟踪 slug/name/version/license/category/risk。"
description_en: "Single source of truth for your skill collection: scan a skills dir into a JSON + Markdown registry tracking slug/name/version/license/category/risk."
read_when:
  - 技能/提示词目录增多，需要一份 SSOT 登记每个技能的元数据
  - 一键把技能目录扫描为 JSON 注册表 + Markdown 总览表
risk_tier: medium
ai_protocol: true
spec: usk/1.0
interface:
  type: cli
  entry_point: scripts/registry.py
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
- registry
- catalog
- governance
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

### Role
The meta-skill layer: manages the skill lifecycle (generate → score → quality gate → registry → monitor).

### Capabilities
- Scan skill folders; parse frontmatter into structured records.
- Emit a JSON registry (SSOT) plus a Markdown overview table.
- Track slug / name / version / license / category / risk for lifecycle governance.

### When to use
- Your skill/prompt directory grows; you need an SSOT recording each skill's metadata.
- One-command scan of a skills dir into a JSON registry + Markdown overview.

### Usage
```bash
python scripts/registry.py <skills-dir> [--out registry.json] [--md registry.md]
```

### Flow
1. Prepare a root directory; each subfolder is a skill (with SKILL.md).
2. Run `registry.py <skills-dir>`; it parses each SKILL.md frontmatter (slug/name/version/license/category/tags/risk_tier).
3. Emit `registry.json` (SSOT, with generated date and count) and `registry.md` (overview table) as the single source of truth.

### Evidence & safety
- Evidence: TBD. Version: 1.0.1. Security: no independent scan (TBD).

## 中文

### 定位
本技能是「AI 用的技能的技能」：管理技能生命周期（生成 → 评分 → 质量门 → 注册表 → 监控）。

### 功能
- 扫描技能目录，解析 frontmatter 为结构化记录。
- 输出 JSON 注册表（SSOT）+ Markdown 总览表。
- 跟踪 slug/名称/版本/许可/类目/风险用于生命周期治理。

### 何时用
- 当技能/提示词目录增多、需要一份单一真源（SSOT）登记每个技能的 slug/name/version/license/category/risk 时使用本技能。
- 当需要把技能目录一键扫描为 JSON 注册表 + Markdown 总览表时使用本技能。

### 用法
```bash
python scripts/registry.py <skills-dir> [--out registry.json] [--md registry.md]
```

### 流程
1. 准备一个根目录，其下每个子目录是一个技能（含 SKILL.md）。
2. 运行 `python scripts/registry.py <skills-dir>`：脚本解析每个 SKILL.md 的 frontmatter（slug/name/version/license/category/tags/risk_tier）。
3. 产出 registry.json（SSOT，含 generated 日期与 count）与 registry.md（Markdown 总览表），作为技能生命周期的单一真源。

### 证据与安全声明
- 证据：TBD（暂无评测/徽章链接；产生后在此更新实际链接）
- 版本：1.0.1
- 安全：未做独立安全扫描（TBD），结论待补；补全前不作推荐背书。
