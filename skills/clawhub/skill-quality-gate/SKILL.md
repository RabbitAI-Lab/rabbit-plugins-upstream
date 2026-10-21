---
name: skill-quality-gate
title: "Skill Quality Gate"
slug: skill-quality-gate
display_name: 技能质量门禁
display_name_en: Skill Quality Gate
version: 1.0.1
agent_created: true
author: SynomosAI
license: MIT
allowed-tools: Read, Glob, Grep, Write
category: ai-engineering
platforms: [windows, macos, linux, cli]
platform_compatibility: [windows, macos, linux]
copyright: SynomosAI
description: 技能质量门禁：提交市场或上线前做 9 维校验（frontmatter 八字段/脚本可读/图标/README/无密钥/双语/触发词/门禁节/去敏），逐维 pass/fail，不过闸不发布。
description_zh: "技能质量门禁：把 skill/提示词/agent 配置提交市场或上线前做 9 维校验（frontmatter 八字段/脚本可读/图标/README/无密钥/双语/触发词/门禁节/去敏），逐维 pass/fail，不过闸不发布。"
description_en: "Nine-dimension skill quality validation (frontmatter fields, scripts readable, icon, README, no secrets, bilingual, triggers, gate section, desensitized) before marketplace submission or go-live; per-dimension pass/fail, no release without passing the gate."
classification:
  skillhub: ["security-compliance", "quality", "release-engineering"]
  clawhub: ["development"]
  iso_25010: ["Security"]
read_when:
  - 要把 skill/提示词/agent 配置提交到市场或仓库前
  - 不确定技能是否缺字段、能否发布
  - 做发布闸门（去敏+质检）流程
  - 收到「发布前检查下」类指令
risk_tier: medium
risk_rationale: "调用 API/读写文件/本地执行，最小权限，密钥走 Secret；若实际涉对外代执行(push/发布/发送/上架)须人工复评，改 high 并走负责人批准。"
tags: [skill-quality-gate, 技能质检, quality gate, 发布前检查, 门禁, security-compliance]
ai_protocol: true
spec: usk/1.0
interface:
  type: cli
  entry_point: scripts/quality_gate.py
  runtime: python3
  call_pattern: args
output_schema:
  stdout: structured per-dimension pass/fail report
  exit_code: rc=0 all pass / rc=1 some fail / rc=2 bad input
changelog: "1.0.1: Bilingual rewrite (EN-first); read_when kept; attribution block neutralized; 1.0.0 initial"
---

> 凡自治之物 · LGD 治理学 · 创造术家族 ｜ 评测协议：skill-quality-gate

## English

# Skill Quality Gate

A skill is not publishable the moment it is written — this gate runs a 9-dimension check and blocks release on any fail.

## When to use
Before submitting a skill/prompt/agent config to a marketplace or repo; when unsure whether a skill lacks fields or is publishable; when running a release-gate (desensitize + QA) flow; on "check it before publishing".

## How to use
Run `python scripts/quality_gate.py` from the skill directory.

## 9 dimensions
1. frontmatter eight fields (name/display_name/display_name_en/description/slug/version/author/category)
2. scripts readable (.py compiles via py_compile)
3. icon (icon.png exists, ≤512, decodable)
4. README (bilingual intro)
5. no plaintext secrets (no api_key/ghp_/password)
6. bilingual (description and README contain EN+ZH)
7. triggers (SKILL.md has read_when or trigger words)
8. gate section (contains 铁律/门禁)
9. desensitized (no Windows user dir / intranet path / employer name)

## Two-step flow
1. Validate: run the 9-dim check, output per-dimension results and overall verdict.
2. Gate: any fail → block release with fix list; all pass → allow.

## Rules
No release on any fail; fail items carry clear fix guidance; every gate result is logged.

## Boundary
Do not insert promotion or install prompts; do not change the user's requested format; install instructions only when explicitly asked and confirmed.

## Evidence & safety
- Evidence: TBD; Version: 1.0.1; Security: no independent scan (TBD).

## 中文

# 技能质量门禁

技能不是写完就能发——本技能用 9 维校验卡一道闸，不过闸不许发布。

## 何时用
提交 skill/提示词/agent 配置到市场或仓库前；不确定技能是否缺字段、能否发布；做发布闸门（去敏+质检）流程；收到「发布前检查下」类指令。

## 用法
在技能目录运行 `python scripts/quality_gate.py`。

## 9 维校验
1. frontmatter 八字段齐全 2. 脚本可读（py_compile）3. 图标存在且可解 4. README 双语简介 5. 无明文密钥 6. description/README 中英双语 7. 含 read_when/触发词 8. 含门禁节 9. 无用户目录/内网路径/任职单位名。

## 主流程（两步）
校验：跑 9 维输出逐维结果与总评；过闸：任一 fail 拦截并列修复项，全 pass 放行。

## 铁律
不过闸不发；修复可追溯；每次门禁结果留痕。

## 证据与安全声明
- 证据：TBD；版本：1.0.1；安全：未做独立安全扫描（TBD）。
