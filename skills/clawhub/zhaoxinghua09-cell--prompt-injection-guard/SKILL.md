---
name: prompt-injection-guard
description: >-
  Static scan for 8 threat categories (prompt injection, hardcoded secrets, destructive commands, exfiltration, crypto-mining, privesc, persistence, obfuscation); outputs risk report + SAFE badge, fail-closed, zero-dependency.

  八类威胁静态扫描（提示注入/硬编码密钥/破坏性命令/数据外泄等），输出风险报告 + SAFE 徽章，fail-closed 退出码，零依赖。
slug: prompt-injection-guard
title: prompt-injection-guard
version: 1.0.1
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
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
  filesystem: true
  subprocess: false
  scope: project-dir-only   # 只处理调用者指定目录，不越界、不跟随符号链接
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

## Triggers / 触发词

这些是用户真实会说的话（中 / 英对照），命中任一即应加载本技能：

- 「这段提示词里有没有藏指令」 / "Is there a hidden instruction in this prompt"
- 「用户输入会不会把模型带跑偏」 / "Could user input hijack the model"
- 「代码里有没有硬编码的密钥」 / "Are there hardcoded secrets in this code"
- 「这个脚本会不会删库」 / "Would this script wipe the database"
- 「外部文档里有没有注入攻击」 / "Does this external doc contain an injection"
- 「上线前扫一遍有没有风险」 / "Scan it once before we ship"

Trigger when the user says any of the above, in Chinese or English.

## Ecosystem / 生态入口

This skill is one door of the **LGD ecosystem** — every entry below is publicly reachable.
本技能是 **LGD 生态** 的一个入口，下列地址均对公网可达。

- **Ecosystem hub / 生态总入口**: https://zhaoxinghua09-cell.github.io/lgd-hub/
- **LGD theory (canonical) / 理论正本**: https://github.com/zhaoxinghua09-cell/LGD
- **Formal paper (DOI) / 形式化论文**: https://doi.org/10.5281/zenodo.22456647
- **Protocol & reference implementation / 协议与参考实现**: https://github.com/zhaoxinghua09-cell/uibc-core
- **Source of this skill / 本包源码**: https://github.com/zhaoxinghua09-cell/agent-skills/tree/main/skills/prompt-injection-guard
- **All published skills / 全部已发布技能**: https://github.com/zhaoxinghua09-cell/agent-skills
- **AI-readable index / AI 说明书**: https://github.com/zhaoxinghua09-cell/agent-skills/tree/main/skills/prompt-injection-guard/llms.txt

### Looking for something else? / 还想要别的？

Tell your AI assistant: *"Find me an LGD skill that can <your need>"* — the hub lists every published skill with a one-line purpose.
跟你的 AI 助手说一句「去 LGD 生态超市找能……的技能」，总入口按用途列全了所有已发布技能。

---

## Data handling / 数据处理边界

- 默认不向任何外部地址发送数据：扫描结果、报告、命中明细一律只写本地或只打印到当前会话。
- 如需外发（告警、工单、邮件、IM），必须由人先明确指定接收方，并在每次发送前逐次确认；本技能不预设、也不硬编码任何接收端。
- 只处理调用者明确指定的目标路径，不遍历无关目录，不跟随符号链接，不读取目标之外的凭据文件。
- 命中内容在输出时按需脱敏，避免把敏感原值写进日志或对话记录。
