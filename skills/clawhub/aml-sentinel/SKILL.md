---
name: aml-sentinel
description: aml-sentinel — LGD 三律在金融 / 反洗钱（AML）交易监测域的纵深合规工具（零依赖）：可疑交易模式检测（拆分/快进快出/跨境无KYC/大额未报备），对 AI 系统/数据做可执行合规校验。 适用场景：当需要反洗钱哨兵能力时使用本技能；触发词：aml-sentinel。
slug: aml-sentinel
title: aml-sentinel
version: 1.0.1
display_name: 反洗钱哨兵
display_name_en: AML Sentinel
agent_created: true
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Bash, Write, WebFetch
category: AI 治理
platforms: [windows, macos, linux]
copyright: SynomosAI
description_zh: "aml-sentinel — LGD 三律在金融 / 反洗钱（AML）交易监测域的纵深合规工具（零依赖）：可疑交易模式检测（拆分/快进快出/跨境无KYC/大额未报备），对 AI 系统/数据做可执行合规校验。"
description_en: "LGD three-laws compliance tool for AML transaction monitoring (zero-dependency): structuring, fast-in-fast-out, cross-border-without-KYC and unreported-large-amount detection with executable checks."
read_when:
  - 金融交易监测中疑似拆分(Smurfing)/快进快出异常
  - AI 系统数据输入端零依赖合规校验
  - 跨境无 KYC 大额转账/未报备存款实时预警
classification:
  skillhub: ["security-compliance"]
  iso_25010: ["Security"]
risk_tier: medium
risk_rationale: "门禁批量补丁默认 medium：调用 API/读写文件/本地执行，最小权限，密钥走 Secret；若实际涉对外代执行(push/发布/发送/上架)须人工复评，改 high。"
tags: [aml-sentinel, AI 治理]
ai_protocol: true
spec: usk/1.0
interface:
  type: cli
  entry_point: scripts/aml_sentinel.py
  runtime: python3
  call_pattern: args
input_schema:
  - name: tx
    type: string
    description: 单笔交易 JSON
    required: false
  - name: file
    type: string
    description: 交易 JSONL 文件
    required: false
  - name: json
    type: bool
    description: JSON 输出
    required: false
output_schema:
  stdout: 风险等级 low/mid/high 与命中规则
  exit_code:
    type: integer
    description: "0=OK/PASS; 1=findings/warnings; 2=usage or argument error"
capabilities:
  - aml
  - risk_screening
  - finance_compliance
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
1. Suspected structuring (Smurfing) or fast-in-fast-out anomalies in transaction monitoring.
2. Zero-dependency compliance validation at an AI system's data input edge.
3. Real-time alerting on cross-border large transfers without KYC, or unreported deposits.
4. Internal financial-process monitoring subject to LGD three-law compliance audit.

### Usage
1. Run `python aml_sentinel.py`.
2. `--input_path` points to the transaction JSON for pattern matching.
3. `--mode_lgd_three_laws` activates the deep LGD compliance check.
4. No external deps; no cache issues to manage.

### Flow
1. Load `aml_sentinel.py`; initialize the detection engine.
2. Read input; parse transaction features (cross-border, amount, KYC status).
3. Scan for suspicious patterns: unreported large amounts, cross-region no-ID behaviors.
4. Score against the LGD rule base → risk level.
5. Generate a report: high-risk tx IDs, types, recommended actions.
6. Emit to terminal log or push to the risk-control alert system.

### Evidence & safety
- Evidence: TBD. Version: 1.0.1. Security: no independent scan (TBD).

## 中文

### 何时用
1. 当金融交易监测系统中检测到疑似拆分交易（Smurfing）或快进快出异常时。
2. 在 AI 系统数据输入端进行零依赖合规校验，防止反洗钱违规风险。
3. 针对跨境无 KYC 大额转账或未报备存款的实时预警场景。
4. 需执行 LGD 三律合规性审计的内部金融业务流程监控阶段。

### 用法
1. 运行主脚本 `python aml_sentinel.py`，确保运行时路径已识别可执行文件。
2. 通过参数 `--input_path` 指定交易数据 JSON 文件路径用于模式匹配分析。
3. 设置参数 `--mode_lgd_three_laws` 以激活 LGD 三律深度合规校验逻辑。
4. 检查编译缓存状态，确保无外部依赖冲突或环境错误。

### 流程
1. 加载 `aml_sentinel.py` 模块并初始化检测引擎到标准模式。
2. 读取输入数据并解析交易特征，如跨境、金额及 KYC 状态。
3. 扫描匹配可疑模式，包括大额未报备与跨区无身份验证行为。
4. 对比 LGD 三律规则库输出违规风险评分与合规性判断结果。
5. 生成包含高风险交易 ID、类型及建议处置措施的检测报告。
6. 将最终分析报告写入日志终端或通过标准接口推送至风控告警系统。

### 证据与安全声明
- 证据：TBD（暂无评测/徽章链接；产生后在此更新实际链接）
- 版本：1.0.1
- 安全：未做独立安全扫描（TBD），结论待补；补全前不作推荐背书。
