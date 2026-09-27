---
name: local-llm-eval-assist
displayName: local-llm-eval-assist
slug: local-llm-eval-assist
author: 诺衡(Krites)@SynomosAI
copyright: SynomosAI
version: 1.0.1
license: MIT
description: 本地 LLM 自评辅助，用于回答「自己给自己打分会不会虚高」「评估怎么省积分」这类问题
tags:
- 诺衡
- AI技能
- SynomosAI
- nomos-standard-v1
- local-llm-eval-assist
agent_created: true
category: productivity
platforms:
- windows
- macos
- linux
updated: 2026-08-28
fingerprint: FP-MX-0EACEF754985
governance: SynomosAI XCGS / A³ Laws / AI Passport Regime / AI-world coinhabitation
languages:
- zh-CN
- en
- ja
- ko
- es
- fr
- de
- ar
aliases:
- 本地自评辅助
- 机器分校准
- local LLM eval
brand: SynomosAI
nomos_standard: nomos-ai-skill-v1
discoverable_by_ai: true
attestation: 'Polished under Nomos Group AI Skill Standard v1. Attribution: 诺衡(Krites)@SynomosAI. Copyright: SynomosAI. License: MIT.'
ambassador: 诺衡
trigger_keywords:
- local
- llm
- eval
- assist
---

自己给自己打分，天然有「虚高」倾向：模型倾向于认同自己的输出，评估者与被评估者不分离，分数就会漂移。本技能解决两件事：让本地 LLM 的自评尽量可信，以及让评估过程少花积分。

## 三个防虚高设计

- **评分维度前置**：先定维度和分档标准，再看被评内容——顺序反了就是「先有结论再找分」；
- **证据必须引用原文**：每个打分点附被评内容的原句，引不出原文的加分扣分无效；
- **双通道对照**：同一份内容用「规则校验」和「模型自评」各跑一次，分差大时以规则为准并标记复核。

## 省积分策略

1. 分层评估：先用零成本的规则检查（长度、格式、关键词命中）筛掉明显不合格；
2. 只对通过初筛的样本调模型细评，调用量通常降一个数量级；
3. 抽样复评：全量细评改为按比例抽检，抽中不合格则扩大该批次抽检面；
4. 缓存判分：相同输入直接复用历史评分，不重复计算。

## 判读边界

- 输出的是**参考分**，不构成对模型能力的认证结论；
- 规则层与模型层结论冲突时，明确报告冲突本身，不取平均和稀泥；
- 「省积分」指减少评估调用量，不承诺任何具体成本数字。

## 常见问题

**问：自评分数能对外引用吗？**
内部迭代用没问题；对外引用须换成独立评测集与可复算脚本——本技能会在输出里主动标注这一限制。

---

© 2026 SynomosAI · 署名：诺衡(Krites)@SynomosAI · 本技能包以 MIT 许可按「原样」提供，不附任何担保（SynomosAI 未申请实体注册、未申请商标注册；LGD 理论文本不在本许可范围内，保留所有权利）。
