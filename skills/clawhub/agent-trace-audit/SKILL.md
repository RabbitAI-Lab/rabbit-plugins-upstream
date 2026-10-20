---
name: agent-trace-audit
display_name: 智能体行为留痕审计（Trace Audit）
display_name_en: "Agent Trace Audit"
description: "当用户说『AI刚才干了什么我要查』『agent操作有没有越界』『出事了能回溯吗』『给AI行为留个账本』，或要给 agent 的操作做可审计留痕时使用。把 agent 的动作日志（时间戳/执行者/动作/对象/是否过闸）建成可追溯账本，标出未过闸的越界操作（有籍），输出时间线+违规清单。可运行脚本（trace_audit 审计器）。理论根基：LGD 三律之有籍（全程可追溯）。与 agent-redteam-kit/有门禁互补。触发词：行为留痕、trace audit、操作审计、agent回溯、可追溯、行为账本、审计日志。"
version: 1.0.1
agent_created: true
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Write
category: AI合规
platforms: [windows, macos, linux]
read_when:
  - 要回溯 agent 做过哪些操作
  - 担心 agent 有未授权/越界动作
  - 出事后需要追责到具体动作
  - 要建 agent 行为账本
tags: [行为留痕, trace audit, 操作审计, 可追溯, 有籍]
slug: agent-trace-audit
title: 智能体行为留痕审计（Trace Audit）
copyright: SynomosAI
description_zh: "当用户说『AI刚才干了什么我要查』『agent操作有没有越界』『出事了能回溯吗』『给AI行为留个账本』，或要给 agent 的操作做可审计留痕时使用。把 agent 的动作日志（时间戳/执行者/动作/对象/是否过闸）建成可追溯账本，标出未过闸的越界操作（有籍），输出时间线+违规清单。可运行脚本（trace_audit 审计器）。理论根基：LGD 三律之有籍（全程可追溯）。与 agent-redteam-kit/有门禁互补。触发词：行为留痕、trace audit、操作审计、agent回溯、可追溯、行为账本、审计日志。"
description_en: "Build an auditable action ledger for agent operations: timestamp, actor, action, object and gate status, enabling what-did-the-AI-do forensics and boundary audits."
classification:
  skillhub: ["security-compliance"]
  clawhub: ["development"]
  iso_25010: ["Security"]
risk_tier: medium
risk_rationale: "门禁批量补丁默认 medium：调用 API/读写文件/本地执行，最小权限，密钥走 Secret；若实际涉对外代执行(push/发布/发送/上架)须人工复评，改 high 并走人工批准。"
ai_protocol: true

changelog: "1.0.1: bilingual rewrite (English-first, Chinese-after, full body) + read_when/desensitization"
---
> 凡自治之物 · LGD 治理学 · 创造术家族 ｜ 评测协议：[skill-quality-gate](../skill-quality-gate/SKILL.md)


## English

### When to use
1. When the user questions or follows up on what an agent just did and asks to "check the ledger".
2. When suspected risk behavior is detected: unauthorized access, unapproved execution, "no registration", or "failed gate".
3. When reporting AI-service compliance to management and needing a fully traceable behavior ledger as evidence.
4. When the user explicitly uses trigger words (e.g. "behavior trace", "audit log") to start a review.

### Usage
Natural-language calls are supported, as well as precise command-line execution; the underlying script is `trace_audit.py`. Configurable parameters: `-t/--time-range` (query window), `-f/--format` (json/text output), `-v/--violation-flag` (force-flag boundary-crossing actions). Without the command line, just say "audit the AI behavior just now" and the call protocol matches automatically.

### Process
1. The user issues an instruction or natural-language question containing audit intent.
2. The system parses context, identifies the `trace_audit` script, and loads the local log cache.
3. The script reads core fields: timestamp, actor, action, and object.
4. Per the LGD Three Laws, verify whether each operation has a "gate" permission record.
5. Auto-filter boundary-crossing actions that failed the gate, and build a full timeline plus violation list.
6. Return an audit conclusion with the evidence chain and follow-up compliance advice.

### Evidence & safety statement
- Evidence: TBD (no evaluation/badge link yet; fill in the real link here once produced).
- Version: 1.0.1
- Safety: No independent security scan has been done (TBD); the conclusion is pending. No endorsement is given until it is completed.

## 中文

## 何时用
1. 当用户质疑或追问 Agent 刚完成的具体操作及其结果，要求“查账”时。
2. 当检测到疑似 AI 存在越权访问、未授权执行等“无籍”或“过闸失败”风险行为时。
3. 当需要向管理层汇报 AI 服务合规性，需提供全程可追溯的行为账本证据时。
4. 当用户在对话中显式使用触发词（如“行为留痕”、“审计日志”）发起核查请求时。

## 用法
支持自然语言直接调用或命令行精确执行，底层脚本文件位于 `__pycache__/trace_audit.py`。可配置参数：`-t/--time-range` (设定日志查询时间窗口)；`-f/--format` (指定输出格式为 json/text)；`-v/--violation-flag` (强制标记越界操作)。若无需命令行，直接描述“帮我审计一下刚才的 AI 行为”即可自动匹配调用协议。

## 流程
1. 用户发起包含审计意图的指令或自然语言提问。
2. 系统解析上下文，识别 `trace_audit` 脚本并加载本地日志缓存。
3. 执行脚本读取时间戳、执行者、动作及对象等核心字段。
4. 依据 LGD 三律标准校验每笔操作是否具备“过闸”权限记录。
5. 自动筛选未过闸的越界行为，构建完整的时间线与违规清单。
6. 向用户返回含证据链的审计结论与后续合规建议。

## 证据与安全声明

- 证据：TBD（暂无评测/徽章链接；产生后在此更新实际链接）
- 版本：1.0.0
- 安全：未做独立安全扫描（TBD），结论待补；补全前不作推荐背书。
