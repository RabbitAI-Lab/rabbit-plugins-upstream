---
name: prompt-injection-guard
description: Detect prompt injection, hardcoded secrets, destructive commands and exfiltration patterns in any text or file. 检测提示注入、硬编码密钥、破坏性命令与数据外泄模式。
slug: prompt-injection-guard
title: prompt-injection-guard
version: 1.0.1
license: MIT
category: 安全
author: SynomosAI (LGD initiative)
platforms: [windows, macos, linux]
tags: [prompt, injection, guard]
description_zh: "八类威胁静态扫描（提示注入/硬编码密钥/破坏性命令/数据外泄等），输出风险报告 + SAFE 徽章，fail-closed 退出码，零依赖。"
description_en: "Static scan for 8 threat categories (prompt injection, hardcoded secrets, destructive commands, exfiltration, crypto-mining, privesc, persistence, obfuscation); outputs risk report + SAFE badge, fail-closed, zero-dependency."
read_when:
  - 对任意文本/文件做提示注入/硬编码密钥/破坏性命令/数据外泄等威胁静态扫描
  - 生成 LGD SAFE 徽章或机器可读风险报告（fail-closed 退出码）
risk_tier: medium
ai_protocol: true
spec: usk/1.0
interface:
  type: cli
  entry_point: scripts/prompt_guard.py
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
- prompt-injection
- security
- scanner
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
- 8-category threat taxonomy (injection / secrets / destructive / exfil / crypto-mining / privesc / persistence / obfuscation).
- Outputs risk report + SAFE badge, fail-closed exit code.
- Zero-dependency; works on any text or file.

### When to use
- Static scan for prompt injection, hardcoded secrets, destructive commands, data exfiltration across 8 threat categories.
- Generate an LGD SAFE badge or machine-readable risk report (fail-closed exit code).

### Usage
```bash
python scripts/prompt_guard.py <file|text> [--json] [--badge out.svg]
```

### Flow
1. Run `prompt_guard.py <file|text> [--json] [--badge out.svg]`.
2. Scan per the 8-category taxonomy; each hit carries a fragment of evidence.
3. Output SAFE / MACH / TOTAL scores and verdict (TOTAL ≥ 60 = PASS); `--badge out.svg` emits an LGD SAFE SVG; FAIL → exit 1 (fail-closed).

### Safety boundary
- Static analysis only; never auto-executes external commands.
- On risk detection → FAIL; human decides.
- Does not delete / modify / publish anything.

### Evidence & safety
- Evidence: TBD. Version: 1.0.1. Security: no independent scan (TBD).

## 中文

### 功能
- 八类威胁分类法（注入/密钥/破坏/外泄/挖矿/提权/持久化/混淆）。
- 输出风险报告 + SAFE 徽章，fail-closed 退出码。
- 零依赖，任意文本/文件可用。

### 何时用
- 当需要对任意文本或文件做提示注入、硬编码密钥、破坏性命令、数据外泄等八类威胁静态扫描时使用本技能。
- 当需要生成 LGD SAFE 徽章或机器可读风险报告（fail-closed 退出码）时使用本技能。

### 用法
```bash
python scripts/prompt_guard.py <file|text> [--json] [--badge out.svg]
```

### 流程
1. 运行 `python scripts/prompt_guard.py <file|text> [--json] [--badge out.svg]`。
2. 脚本按八类威胁分类法（prompt_injection / hardcoded_secret / destructive_command / data_exfiltration / crypto_mining / privilege_escalation / persistence / obfuscation）扫描，每类命中附片段证据。
3. 输出 SAFE/MACH/TOTAL 分与判定（TOTAL≥60 为 PASS）；带 `--badge out.svg` 时生成 LGD SAFE SVG；FAIL 时退出码为 1（fail-closed）。

### 安全边界
- 只做静态分析，不自动执行任何外部命令。
- 检出风险即 FAIL（fail-closed），由人决策。
- 不代用户删除/修改/发布任何内容。

### 证据与安全声明
- 证据：TBD（暂无评测/徽章链接；产生后在此更新实际链接）
- 版本：1.0.1
- 安全：未做独立安全扫描（TBD），结论待补；补全前不作推荐背书。
