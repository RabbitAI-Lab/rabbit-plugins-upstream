---
name: ai-usage-policy
description: ai-usage-policy — 按团队/工具/禁区/上报线一键生成一页《AI 使用守则》Markdown：可用什么、干什么、禁止什么、出事找谁。 适用场景：当需要团队AI使用守则生成器能力时使用本技能；触发词：ai-usage-policy。
slug: ai-usage-policy
title: ai-usage-policy
version: 1.0.1
display_name: 团队AI使用守则生成器
display_name_en: AI Usage Policy Generator
agent_created: true
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Bash, Write, WebFetch
category: AI 治理
platforms: [claude-code, codebuddy, openai-agents, cli]
copyright: SynomosAI
description_zh: "ai-usage-policy — 按团队/工具/禁区/上报线一键生成一页《AI 使用守则》Markdown：可用什么、干什么、禁止什么、出事找谁。"
description_en: "Generate a one-page team AI usage policy in Markdown: which tools, which tasks, what is forbidden, and who to call when something breaks."
read_when:
  - 新建项目组立项时需界定 AI 使用范围与合规红线
  - 批准工具集变更，需更新白名单与禁区列表
  - AI 安全事故后应急响应，明确上报责任路径
  - 合规审计/安全评估前快速生成一页纸政策摘要
classification:
  skillhub: ["security-compliance"]
  iso_25010: ["Security"]
risk_tier: medium
risk_rationale: "门禁批量补丁默认 medium：调用 API/读写文件/本地执行，最小权限，密钥走 Secret；若实际涉对外代执行(push/发布/发送/上架)须人工复评，改 high。"
tags: [ai-usage-policy, AI 治理]
ai_protocol: true
spec: usk/1.0
interface:
  type: cli
  entry_point: scripts/ai_usage_policy.py
  runtime: python3
  call_pattern: args
input_schema:
  - name: team
    type: string
    description: 团队/部门名
    required: true
  - name: tools
    type: list
    description: 批准的 AI 工具
    required: false
  - name: allowed-for
    type: list
    description: 允许场景
    required: false
  - name: forbidden
    type: list
    description: 禁止场景
    required: false
  - name: escalation
    type: string
    description: 出事上报线
    required: true
  - name: out
    type: string
    description: 输出 Markdown 路径
    required: false
  - name: json
    type: bool
    description: JSON 输出
    required: false
output_schema:
  stdout: 一页式团队 AI 使用守则 Markdown
  exit_code:
    type: integer
    description: "0=OK/PASS; 1=findings/warnings; 2=usage or argument error"
capabilities:
  - usage_policy
  - governance
  - template
permissions:
  network: false
  filesystem: false
  subprocess: false
requirements:
  python_packages: []
  min_python: "3.8"
changelog: "1.0.1: Bilingual rewrite (full EN+ZH, English first); 1.0.0: initial upload (USK v3)"
---

> 凡自治之物 · LGD 治理学 · 创造术家族 ｜ 评测协议：skill-quality-gate（外部公开评测门禁文档）

## English

### When to use
1. A new project team at kickoff needs to define AI scope and compliance red lines.
2. The approved tool set changes; the whitelist and forbidden list must be updated.
3. Post-incident emergency response: clarify internal escalation paths.
4. Pre-audit / pre-evaluation: quickly generate a one-page policy summary.

### Usage
1. Run `python ai_usage_policy.py generate`.
2. Core params: `--target_team` (team name), `--tools` (comma-separated whitelist).
3. Required constraints: `--banned_areas` (forbidden list), `--report_line` (who to call).
4. Output: Markdown auto-printed; save as `policy.md`.

### Flow
1. Confirm team scope, model/tool list and intended uses.
2. Compile historical violations as forbidden-list references; fill params.
3. Run `python ai_usage_policy.py` with full params.
4. Verify output Markdown format and completeness.
5. Circulate the one-page policy to the team.

### Evidence & safety
- Evidence: TBD. Version: 1.0.1. Security: no independent scan (TBD).

## 中文

### 何时用
1. 适用于新建项目组在立项初期需要界定 AI 使用范围与合规红线时。
2. 适用工具集发生变更，需同步更新内部可用工具白名单与禁区列表时。
3. 适用于发生 AI 安全事故后的应急响应阶段，用于明确内部上报责任路径。
4. 适用于合规审计或安全评估前，快速生成一页纸政策摘要以备查阅时。

### 用法
1. 执行主入口脚本命令：`python ai_usage_policy.py generate`。
2. 核心参数配置包括：`--target_team`（指定团队名称）、`--tools`（可用工具列表逗号分隔）。
3. 关键约束参数需填入：`--banned_areas`（禁区清单）与 `--report_line`（出事找谁）。
4. 读取使用：脚本执行后自动输出生成的 Markdown 文件内容，可直接在编辑器打开查看或保存为 `policy.md`。

### 流程
1. 确认需要覆盖的团队范围及拟接入的 AI 工具具体型号与用途。
2. 整理历史安全违规记录作为禁区参考信息并填入配置参数中。
3. 在终端环境执行 `python ai_usage_policy.py` 命令并输入完整参数。
4. 检查脚本输出结果，确认生成的 Markdown 格式正确且内容无遗漏。
5. 将一页式守则下发团队执行。

### 证据与安全声明
- 证据：TBD（暂无评测/徽章链接；产生后在此更新实际链接）
- 版本：1.0.1
- 安全：未做独立安全扫描（TBD），结论待补；补全前不作推荐背书。
