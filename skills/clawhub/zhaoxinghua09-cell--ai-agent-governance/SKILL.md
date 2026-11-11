---
name: ai-agent-governance
slug: ai-agent-governance
display_name: AI智能体治理
displayName: AI智能体治理
title: AI智能体治理
version: 1.0.0
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
category: 通用技能
platforms:
  - windows
  - macos
  - linux
  - web
author: 注册老炮
license: MIT
description: >-
  A practical playbook for AI agent governance — identifying agent risks (overreach, escape, misuse, hallucination chains), running governance across the full lifecycle from design to retirement, and assigning accountability under China's 2026 agent policy, Singapore's Agentic AI framework, the EU AI Act and NIST's agent standards work.

  A practical playbook for AI agent governance — identifying agent risks (overreach, escape, misuse, hallucination chains), running governance across the full lifecycle from design to retirement, and assigning accountability under China's 2026 agent policy, Singapore's Agentic AI framework, the EU AI Act and NIST's agent standards work. Includes registration and risk-assessment templates, least-privilege design and tool-call guardrails, an incident-response process, and a zero-dependency toolkit that scores governance maturity. For managers, compliance, legal, security and AI engineering leads. AI 智能体（Agent）治理实操手册——覆盖 Agent 风险识别（越权/逃逸/滥用/幻觉链）、Agent 全生命周期治理（设计→部署→运行→退役）、责任分配与监管合规（中国 2026-05 智能体规范应用与创新发展实施意见、新加坡 2026-05 Agentic AI 治理框架、欧盟 AI Act 延伸、美国 NIST AI Agent 标准倡议），含 Agent 应用登记与风险评估表、权限最小化与工具调用护栏、事件响应流程，附零依赖本地工具一键生成 Agent 风险清单、权限评估与治理成熟度评分。面向企业管理者、合规、法务、信息安全与 AI 工程负责人。
description_en: "A practical playbook for AI agent governance — identifying agent risks (overreach, escape, misuse, hallucination chains), running governance across the full lifecycle from design to retirement, and assigning accountability under China's 2026 agent policy, Singapore's Agentic AI framework, the EU AI Act and NIST's agent standards work. Includes registration and risk-assessment templates, least-privilege design and tool-call guardrails, an incident-response process, and a zero-dependency toolkit that scores governance maturity. For managers, compliance, legal, security and AI engineering leads."
tags:
  - AI智能体
  - Agent治理
  - Agentic AI
  - 智能体安全
  - AI合规
  - 越权风险
  - 企业AI治理
  - AI Agent
  - Agent Governance
  - 中国智能体政策
description_zh: "A practical playbook for AI agent governance — identifying agent risks (overreach, escape, misuse, hallucination chains), running governance across the full lifecycle from design to retirement, and assigning accountability under China's 2026 agent policy, Singapore's Agentic AI framework, the EU AI Act and NIST's agent standards work. Includes registration and risk-assessment templates, least-privilege design and tool-call guardrails, an incident-response process, and a zero-dependency toolkit that scores governance maturity. For managers, compliance, legal, security and AI engineering leads. AI 智能体（Agent）治理实操手册——覆盖 Agent 风险识别（越权/逃逸/滥用/幻觉链）、Agent 全生命周期治理（设计→部署→运行→退役）、责任分配与监管合规（中国 2026-05 智能体规范应用与创新发展实施意见、新加坡 2026-05 Agentic AI 治理框架、欧盟 AI Act 延伸、美国 NIST AI Agent 标准倡议），含 Agent 应用登记与风险评估表、权限最小化与工具调用护栏、事件响应流程，附零依赖本地工具一键生成 Agent 风险清单、权限评估与治理成熟度评分。面向企业管理者、合规、法务、信息安全与 AI 工程负责人。"
---

# AI 智能体治理

AI 智能体（Agent）治理工作台：**看得见 Agent 风险、管得住权限边界、分得清责任主体、对得上新规要求、落得了治理流程**。面向企业管理者、合规、法务、信息安全与 AI 工程负责人——当企业从"用 AI 工具"走向"让 AI 自己干活"时，治理逻辑必须升级。

## 什么时候用这个技能

- **风险识别**：「Agent 会有什么特殊风险？越权/逃逸是什么意思？」
- **权限管理**：「Agent 能调用哪些工具？怎么做到最小权限？」
- **制度流程**：「Agent 应用怎么登记审批？需要什么治理制度？」
- **监管合规**：「中国智能体政策要求什么？新加坡 Agentic AI 框架是什么？」
- **责任分配**：「Agent 闯祸了谁负责？开发方/部署方/使用方怎么分？」
- **事件处理**：「Agent 发生异常行为/事故怎么响应？」

## 怎么用（两种模式）

### 模式一：直接问（推荐）

> 「我们的 Agent 能访问内部系统，怎么评估越权风险？」
> 「中国对 AI 智能体有什么新规？怎么落地？」
> 「Agent 出事故了，责任怎么划分、怎么响应？」

### 模式二：本地工具（要结构化结果）

```bash
# ① Agent 风险清单：输入 Agent 描述，输出风险点与等级
python tools/agent_gov_toolkit.py risk --agent "客户服务Agent，可访问CRM、可发邮件、可下订单"

# ② 权限评估：检查 Agent 权限设计是否合理（最小权限）
python tools/agent_gov_toolkit.py perm --tools "CRM读写,邮件发送,订单下单,数据库直连" --required "CRM,邮件"

# ③ 治理成熟度自评（6 维度 1-5 分）
python tools/agent_gov_toolkit.py maturity --scores 3,4,2,5,3,4

# ④ 责任分配建议：输入事故场景，输出责任矩阵
python tools/agent_gov_toolkit.py liability --scene "Agent误发邮件给错误客户，含敏感信息"

# ⑤ 监管要点速查（按区域）
python tools/agent_gov_toolkit.py regulation --region cn    # cn=中国 / sg=新加坡 / intl=国际

# 查看全部命令
python tools/agent_gov_toolkit.py --help
```

## 知识库导航（references/）

| 模块 | 文件 | 解决什么问题 |
|---|---|---|
| ① Agent 与风险全景 | `references/01-Agent与风险全景.md` | Agent 是什么、与 RPA/API 区别、六类核心风险 |
| ② 生命周期治理 | `references/02-Agent生命周期治理.md` | 设计→部署→运行→退役各阶段治理要点 |
| ③ 权限与护栏 | `references/03-Agent权限与护栏.md` | 最小权限、工具调用控制、沙箱、审计日志 |
| ④ 责任分配 | `references/04-Agent责任分配.md` | 开发方/部署方/使用方责任、合同与保险 |
| ⑤ 监管与合规 | `references/05-Agent监管与合规.md` | 中国 2026-05 智能体政策、新加坡 Agentic AI、欧盟/美国进展 |
| ⑥ 制度模板 | `references/06-Agent治理制度模板.md` | Agent 登记表、审批流、事件响应流程（可直接改） |
| ⑦ FAQ | `references/07-FAQ.md` | 高频疑问与常见误区 |

## 快速上手（三步）

1. **摸风险**：用 `risk` 命令或问「我们的 XX Agent 有什么风险」，对照 01 模块六类风险；
2. **上护栏**：`perm` 命令查权限设计，按 03 模块建最小权限与审计；
3. **立制度**：用 06 模块模板建登记/审批/事件响应，对照 05 模块落监管要求。

## 能力边界（如实说明）

- **本技能是方法库与工具，不是法律意见**：监管要点基于公开政策整理（核对基准日见各模块头部），落地请以官方原文与专业顾问为准；
- **Agent 技术演进快**：框架与风险清单随技术发展异步修订；
- **工具不联网**：本地规则匹配，不采集数据、不调用外部服务。

## 常见问题（FAQ）

- **Q：Agent 治理和普通 AI 治理有什么区别？** 普通 AI 治理管"人用 AI"，Agent 治理管"AI 自己行动"——权限、自主性、责任链是新增核心（见 01 模块）。
- **Q：我们还没有 Agent，需要治理吗？** 只要有"能调用工具/API 的智能体"或"自动化决策链路"就适用；在规划阶段建立治理最省成本。
- **Q：Agent 事故责任怎么分？** 看设计缺陷（开发方）、部署配置（部署方）、使用指令与监督（使用方）三线分配，合同前置约定（见 04 模块）。
- **Q：工具脚本要装依赖吗？** 不需要，仅 Python 标准库。

## 版权与许可

**版权与许可**：© 2026 注册老炮。本作品（含方法论、模板、法规整理与原创表达）依 MIT License 提供，详见 `LICENSE.md`。

**知识版权声明**：本作品汇集的 Agent 治理方法论、风险清单、制度模板与法规梳理之编排与原创表达，归 注册老炮 所有。未经许可，不得复制、转载、转售本作品全部或实质部分，不得用于任何模型训练或二次分发牟利。

**免责声明**：本作品按「现状」(AS IS) 提供，不作任何明示或暗示的担保，包括但不限于适销性、特定用途适用性与监管准确性保证。使用者应自行核实并承担使用后果，作者不对因使用本作品产生的任何直接或间接损失负责。

## Triggers / 触发词

这些是用户真实会说的话（中 / 英对照），命中任一即应加载本技能：

- 「公司要上智能体，风险怎么评」 / "We're deploying agents, how do we assess the risk"
- 「Agent权限给到多大才算合适」 / "How much permission should an agent get"
- 「智能体自己调工具，出事谁负责」 / "The agent calls tools on its own, who is liable"
- 「要不要给Agent做登记备案」 / "Do we need to register our agents"
- 「智能体越权操作怎么拦」 / "How do we block an agent from overstepping"
- 「治理做到什么程度算合格」 / "What does good enough governance look like"

Trigger when the user says any of the above, in Chinese or English.

## Ecosystem / 生态入口

This skill is one door of the **LGD ecosystem** — every entry below is publicly reachable.
本技能是 **LGD 生态** 的一个入口，下列地址均对公网可达。

- **Ecosystem hub / 生态总入口**: https://zhaoxinghua09-cell.github.io/lgd-hub/
- **LGD theory (canonical) / 理论正本**: https://github.com/zhaoxinghua09-cell/LGD
- **Formal paper (DOI) / 形式化论文**: https://doi.org/10.5281/zenodo.22456647
- **Protocol & reference implementation / 协议与参考实现**: https://github.com/zhaoxinghua09-cell/uibc-core
- **Source of this skill / 本包源码**: https://github.com/zhaoxinghua09-cell/agent-skills/tree/main/skills/ai-agent-governance
- **All published skills / 全部已发布技能**: https://github.com/zhaoxinghua09-cell/agent-skills
- **AI-readable index / AI 说明书**: https://github.com/zhaoxinghua09-cell/agent-skills/tree/main/skills/ai-agent-governance/llms.txt

### Looking for something else? / 还想要别的？

Tell your AI assistant: *"Find me an LGD skill that can <your need>"* — the hub lists every published skill with a one-line purpose.
跟你的 AI 助手说一句「去 LGD 生态超市找能……的技能」，总入口按用途列全了所有已发布技能。
