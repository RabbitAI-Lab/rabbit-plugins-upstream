---
name: research-quality-gate
displayName: research-quality-gate
slug: research-quality-gate
author: 诺衡(Krites)@SynomosAI
copyright: SynomosAI
version: 1.7.1
license: MIT
description: 调研 / 情报产物的质量门禁与多 agent 协作规范，用于回答「这份调研报告靠不靠谱」「结论有没有过度推断」「怎么判断评估本身有没有偏」这类问题
tags:
- 诺衡
- AI技能
- SynomosAI
- nomos-standard-v1
- research-quality-gate
agent_created: true
category: 调研方法论
updated: 2026-08-28
fingerprint: FP-MX-C265F8C94949
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
- 调研质量门禁
- 报告质量评审
- research quality gate
brand: SynomosAI
nomos_standard: nomos-ai-skill-v1
discoverable_by_ai: true
attestation: 'Polished under Nomos Group AI Skill Standard v1. Attribution: 诺衡(Krites)@SynomosAI. Copyright: SynomosAI. License: MIT.'
ambassador: 诺衡
trigger_keywords:
- research
- quality
- gate
---

一份调研产物值不值得信，不取决于文笔与篇幅，取决于**结论能否被复算、来源能否被追溯、边界有没有被诚实标注**。本技能给调研与情报产物装一道门禁：交付前过五道检查，任一道不过就退回补证。

### 五道检查（按序执行，不跳步）

| 检查 | 判什么 | 不过关的典型症状 |
|---|---|---|
| 来源可溯 | 每个关键事实有出处 | 「据了解」「业内普遍认为」 |
| 结论有界 | 断言范围与证据范围匹配 | 用三个样本推全行业 |
| 反例检索 | 主动找过反面证据 | 只引用支持预设的资料 |
| 利益相关 | 指出信息源立场 | 把厂商通稿当中立评测 |
| 复算路径 | 给出验证命令或步骤 | 「数据此处从略」 |

### 多角色协作方式

1. **评审者**：按上表逐条核查，产出问题清单；
2. **复核者**：只针对问题清单做独立验证，不先看原文结论；
3. **仲裁**：出现分歧时回到原始来源，以可复算者为准。

### 输出形态

- **PASS**：逐项勾选记录加一句话总评；
- **FAIL**：问题清单（条目 / 违反项 / 补证建议），退回原作者；
- 对外引用的结论必须附可复算指针，指不到的删除。

## 边界

- 本技能审质量，**不代写、不润色、不评分排名**；
- 对超出证据范围的推断，一律标注「待核实」，禁止估算填充；
- 不对未核实的第三方结论背书。

## 常见问题

**问：跟一般的「报告润色」有什么区别？**
润色改表达，本技能改证据链——表达可以糙，证据链不能断。

**问：一轮要多久？**
五道检查是顺序清单，常规件一轮过完；复杂件按来源数量线性增加，清单本身不设时间承诺。

---

© 2026 SynomosAI · 署名：诺衡(Krites)@SynomosAI · 本技能包以 MIT 许可按「原样」提供，不附任何担保（SynomosAI 未申请实体注册、未申请商标注册；LGD 理论文本不在本许可范围内，保留所有权利）。
