---
name: publish-quality-gate
title: "Publish Quality Gate"
slug: publish-quality-gate
display_name: 发布质量门禁
display_name_en: Publish Quality Gate
version: 1.0.2
agent_created: true
author: SynomosAI
copyright: SynomosAI
license: MIT
allowed-tools: Read, Glob, Grep, Bash, Write, Edit
category: security
platforms: [windows, macos, linux, cli]
platform_compatibility: [windows, macos, linux]
description: 发布质量门禁：发布任何 Skill/专家包/文档/工具到外部前后的质量检查——发布前四层敏感信息检查，发布后 TRACE 五维 AI 自测。
description_zh: "发布质量门禁：发布任何 Skill/专家包/文档/工具到外部前后做质量检查——发布前四层敏感信息检查（公司→本机→个人→机密），发布后按 TRACE 五维（Trust/Reliability/Adaptability/Convention/Effectiveness）AI 自测。"
description_en: "Pre- and post-publish quality gate for any skill, expert pack, document or tool: four-layer sensitive-info checks (company → machine → personal → confidential) before release and TRACE five-dimension review after."
classification:
  skillhub: ["security-compliance", "release-engineering", "quality"]
  clawhub: ["development", "data-analytics"]
  iso_25010: ["Security"]
read_when:
  - 用户说「准备发布/发布前检查/检查一下发布物/脱敏检查」时
  - 发布任何 Skill/专家包/文档/工具到外部（分享/上架市场）前后
  - 需要对发布物做四层敏感信息审查与 TRACE 五维 AI 自测
risk_tier: medium
risk_rationale: "调用 API/读写文件/本地执行，最小权限，密钥走 Secret；若实际涉对外代执行(push/发布/发送/上架)须人工复评，改 high 并走负责人批准。"
tags: [publish-quality-gate, 发布质量, 发布前检查, 敏感扫描, 脱敏, TRACE, security-compliance]
ai_protocol: true
spec: usk/1.0
interface:
  type: cli
  entry_point: scripts/check_release.py
  runtime: python3
  call_pattern: args
output_schema:
  stdout: structured quality report (pass/fail per layer)
  exit_code: rc=0 ok / rc=1 warning / rc=2 bad input
changelog: "1.0.2: Bilingual rewrite (EN-first) + read_when added; risk_rationale ref neutralized; 1.0.1 prior"
---

> 凡自治之物 · LGD 治理学 · 创造术家族 ｜ 评测协议：skill-quality-gate

## English

# Publish Quality Gate

## When to use
1. When a skill, expert pack, document, or tool is about to be distributed externally (shared or listed on a marketplace).
2. When the conversation hits triggers like "ready to publish", "desensitization check", or "TRACE review".
3. When four-layer sensitive-info review and TRACE five-dimension pre/post-publish validation are needed.

## How to use
- Core script: `python scripts/check_release.py`.
- Args: `--release_type` (content type) and `--mode` (pre/post publish).
- Trigger via natural language ("start desensitization") or by providing the artifact path.

## Workflow
1. Capture intent and confirm triggers.
2. Run four-layer sensitive-info checks (company → machine → personal → confidential) and block violations.
3. If post-publish, run the TRACE five-dimension (Trust/Reliability/Adaptability/Convention/Effectiveness) self-test.
4. Summarize results into a quality report with pass/fail status.
5. Report the final verdict and log the full detection record.

## Evidence & safety
- Evidence: TBD; Version: 1.0.2; Security: no independent scan (TBD).

## 中文

# 发布质量门禁

## 何时用
1. 用户计划把 Skill、专家包、文档或工具分发到外部平台（分享、上架市场）时。
2. 对话中出现「准备发布」「脱敏检查」「TRACE 评测」等触发词时。
3. 需要对发布物做四层敏感信息审查与 TRACE 五维 AI 自测的前后验证。

## 用法
- 核心脚本：`python scripts/check_release.py`。
- 参数：`--release_type`（内容类型）、`--mode`（发布前后）。
- 通过自然语言指令触发，或提供发布物路径。

## 流程
捕获意图并确认触发 → 执行四层敏感信息检查（公司→本机→个人→机密）并拦截违规 → 发布后启动 TRACE 五维 AI 自测 → 汇总生成质量报告标记通过/失败 → 反馈结论并记录检测日志。

## 证据与安全声明
- 证据：TBD；版本：1.0.2；安全：未做独立安全扫描（TBD）。
