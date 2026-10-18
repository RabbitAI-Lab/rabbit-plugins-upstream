---
name: fact-check-guard
display_name: 事实核查护栏（Fact Check Guard）
display_name_en: "Fact Check Guard"
description: "当用户说『AI胡说八道』『内容发出去怕有错』『怎么验证模型给的事实』『引用要有出处』，或要把 agent 生成的内容(文章/报告/回复)对外发布、必须可溯源时使用。把每条关键声明当『待证主张』：对照检索来源逐条标注 已支撑/无来源/存疑，无来源的不许当事实对外。理论根基：LGD 三律（有籍·有证·有门禁）。触发词：事实核查、fact check、幻觉检测、引用溯源、内容可证、AI胡说、出处校验、grounding。"
version: 1.1.1
agent_created: true
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Write, WebSearch
category: AI工程方法
platforms: [windows, macos, linux]
read_when:
  - 模型生成的内容要对外发布（文章/报告/客服回复）
  - 出现过事实错误、编造引用或数据
  - 要求「每条关键说法都有出处」
  - 用户问「怎么验证 AI 给的是真的」
tags: [事实核查, fact check, 幻觉检测, 引用溯源, 内容可证, grounding, 可靠性, AI安全]
slug: fact-check-guard
title: 事实核查护栏（Fact Check Guard）
copyright: SynomosAI
description_zh: "当用户说『AI胡说八道』『内容发出去怕有错』『怎么验证模型给的事实』『引用要有出处』，或要把 agent 生成的内容(文章/报告/回复)对外发布、必须可溯源时使用。把每条关键声明当『待证主张』：对照检索来源逐条标注 已支撑/无来源/存疑，无来源的不许当事实对外。理论根基：LGD 三律（有籍·有证·有门禁）。触发词：事实核查、fact check、幻觉检测、引用溯源、内容可证、AI胡说、出处校验、grounding。"
description_en: "Fact-check guard for AI-generated content: turn key claims into verifiable propositions and tag each against retrieved sources as supported, refuted or unverifiable before publishing."
classification:
  skillhub: ["security-compliance"]
  iso_25010: ["Security"]
risk_tier: medium
risk_rationale: "门禁批量补丁默认 medium（按默认策略设计为中等风险）：调用 API/读写文件/本地执行，最小权限，密钥走 Secret；若实际涉对外代执行(push/发布/发送/上架)须人工复评，改 high 并走人工批准。"
ai_protocol: true
spec: usk/1.0
interface:
  type: cli
  entry_point: scripts/fact_guard.py
  runtime: python3
  call_pattern: args
input_schema:
  args:
    type: string
    description: "命令行参数透传给主脚本，具体取值见各包 --help"
    required: false
output_schema:
  stdout:
    type: string
    description: "标准输出为 JSON 结果，含逐项检查与总体结论"
  exit_code:
    type: integer
    description: "0=PASS/完成；1=FAIL/有警告或待补强；2=用法或参数错误"
capabilities:
  - cli_tool
permissions:
  network: false
  filesystem: false
  subprocess: false
requirements:
  python_packages: []
  min_python: "3.8"
changelog: "1.1.1: Bilingual rewrite (full EN+ZH, English first); 1.0.0: initial upload (USK v3)"

---

> 凡自治之物 · LGD 治理学 · 创造术家族 ｜ 评测协议：见平台质量门禁规范

## English

### When to use
1. When the user questions the truthfulness of generated content, or voices worries like "the AI talks nonsense" or "I'm afraid of errors before this goes out".
2. When factual claims in the model's answer must be verified, and concrete sources / citation tracing are required.
3. When agent-generated articles, reports or replies are about to be published externally and must be verifiable and traceable.

### Usage
1. Run: `python fact_guard.py --input <text-to-check>`
2. Enable strict-mode checking: `fact_guard check --mode strict --rules lgd_three_laws`
3. Read a file and analyze its provenance: `fact_guard analyze --file <report-path> --cache __pycache__`
*Parameters*: `--input` is the text to verify; `--mode` accepts `normal/strict`, or `lgd_three_laws` to engage the theoretical root.

### Workflow
1. **Extract claims**: identify the key statements in the input and mark them as "claims to be proven".
2. **Retrieve evidence**: run the script to search retrieved sources, looking for matching external knowledge bases or documents.
3. **Compare & label**: per the results, tag each claim as "supported / unsourced / dubious".
4. **Gate**: content tagged "unsourced" is forbidden from going out as fact.
5. **Report**: emit a verdict with confidence levels and citation links for decision-making.

### Evidence & safety statement
- Evidence: TBD (no evaluation / badge link yet; update here once it is produced)
- Version: 1.1.1
- Security: no independent security scan has been performed (TBD); the conclusion is pending and no endorsement is given until it is completed.

## 中文

### 何时用
1. 当用户质疑生成内容的真实性，或表达「AI 胡说八道」、「内容发出去怕有错」等担忧时。
2. 需要验证模型回答中的事实主张，并要求提供具体出处、出处校验或引用溯源证据时。
3. 在将 Agent 生成的文章、报告或回复准备对外发布、需确保内容可证及可追溯时使用。

### 用法
1. 调用命令：`python fact_guard.py --input <待核查文本>`
2. 启用严格模式校验：`fact_guard check --mode strict --rules lgd_three_laws`
3. 读取文件分析溯源：`fact_guard analyze --file <报告路径> --cache __pycache__`
*参数说明*：`--input` 为待验证文本；`--mode` 可选 `normal/strict` 或 `lgd_three_laws` 启用理论根基。

### 流程
1. **提取主张**：识别输入中的关键陈述并标记为「待证主张」。
2. **检索证据**：执行脚本对照检索来源，查找匹配的外部知识库或文档。
3. **比对标注**：依据结果将每条声明标注为「已支撑/无来源/存疑」。
4. **门禁控制**：对标记为「无来源」的内容禁止作为事实对外输出。
5. **生成报告**：输出含置信度等级与引用链接的核查结论供决策参考。

### 证据与安全声明
- 证据：TBD（暂无评测/徽章链接；产生后在此更新实际链接）
- 版本：1.1.1
- 安全：未做独立安全扫描（TBD），结论待补；补全前不作推荐背书。
