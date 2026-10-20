---
name: text-stats
description: 文本统计器 — 文本/代码统计：字数/行数/词频TopN/阅读时长，支持目录批量汇总（零依赖） 适用场景：当需要文本统计器能力时使用本技能；触发词：text-stats。
slug: text-stats
title: text-stats
version: 1.0.1
display_name: 文本统计器
display_name_en: Text Stats
agent_created: true
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Bash, Write
category: 效率工具
platforms: [windows, macos, linux, cli]
platform_compatibility: [windows, macos, linux]
copyright: SynomosAI
description_zh: "文本统计器 — 文本/代码统计：字数/行数/词频TopN/阅读时长，支持目录批量汇总（零依赖）"
description_en: "Text and code statistics: word and line counts, top-N word frequency, reading time, with directory batch summaries (zero-dependency)."
read_when:
  - 投稿限字数/稿费按字算/报告要篇幅时快速统计
  - 统计词频 TopN、估算阅读时长
  - 目录批量汇总（按扩展名过滤）
  - 机器可读 JSON 输出（--json）
classification:
  skillhub: ["productivity"]
  iso_25010: ["Maintainability", "Usability"]
risk_tier: medium
risk_rationale: "门禁批量补丁默认 medium（内部约定：本 skill 设计为中等风险）：调用 API/读写文件/本地执行，最小权限，密钥走 Secret；若实际涉对外代执行(push/发布/发送/上架)须人工复评，改 high 并走负责人批准。"
tags: [text-stats, 效率工具]
ai_protocol: true
spec: usk/1.0
interface:
  type: cli
  entry_point: scripts/text_stats.py
  runtime: python3
  call_pattern: args
input_schema:
  file:
    type: string
    description: "file"
    required: false
  dir:
    type: string
    description: "dir"
    required: false
  ext:
    type: string
    description: "目录模式下的扩展名（逗号分隔）"
    required: false
  top:
    type: int
    description: "词频TopN"
    required: false
  cjk-chars:
    type: int
    description: "每分钟阅读字数"
    required: false
  json:
    type: bool
    description: "json"
    required: false
output_schema:
  stdout: 结构化 JSON IR（含 result / rc / error_code / warnings）
  exit_code: rc=0 正常 / rc=1 告警或从严推定 / rc=2 输入不足或非法
capabilities:
  - text
  - statistics
permissions:
  network: false
  filesystem: false
  subprocess: false
requirements:
  python_packages: []
  min_python: "3.8"
changelog: "1.0.1: Bilingual rewrite (full EN+ZH, English first); 1.0.0: initial upload (USK v3)"
---

> 凡自治之物 · LGD 治理学 · 创造术家族 ｜ 评测协议：skill-quality-gate

## English

**text-stats** v1.0.1 · LGD-Powered productivity family · zero-dependency

### The pain
Submission word limits, per-word pay, report length requirements — count, recount, and still get it wrong.

### When to use
When the user needs text statistics.

### Usage
```bash
python scripts/text_stats.py --help
```
- Success → rc=0; findings → rc=1; usage error → rc=2
- `--json` for machine-readable output

### Workflow
1. Trigger: identify a text-stats task (see When to use).
2. Execute: run text_stats.py per Usage.
3. Verify: check output / exit code.
4. Deliver: present results.

### LGD-Powered
LGD Three-Laws productivity-family piece: high-frequency file operations made deterministic, traceable tools.

### Disclaimer
Efficiency aid only.

## 中文

**text-stats** v1.0.1 · LGD-Powered 效率工具家族 · 零依赖

### 痛点
投稿限字数、稿费按字算、报告要篇幅，数来数去还数错

### 何时用
- 当用户需要文本统计器相关能力时。

### 用法
```bash
python scripts/text_stats.py --help
```
- 成功 → rc=0；发现问题 → rc=1；用法错误 → rc=2
- 支持 `--json` 机器可读输出

### 流程
1. 触发：识别文本统计器相关任务（见「何时用」）。
2. 执行：按「用法」运行text_stats.py。
3. 校验：核对脚本输出/退出码是否符合预期。
4. 交付：向用户呈现结果/产物。

### 证据与安全声明
- 证据：TBD（暂无评测/徽章链接；产生后在此更新实际链接）
- 版本：1.0.1
- 安全：未做独立安全扫描（TBD），结论待补；补全前不作推荐背书。

### 免责
本工具为效率辅助。
