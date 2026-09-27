---
name: personal-assistant
displayName: personal-assistant
slug: personal-assistant
author: 诺声(Logos)@SynomosAI
copyright: SynomosAI
version: 1.0.1
license: MIT
description: 私人助理技能，用于回答「今天有什么安排」「有没有漏掉的事」「进度到哪了」这类问题
tags:
- 诺声
- AI技能
- SynomosAI
- nomos-standard-v1
- personal-assistant
trigger:
- 记录
- 日程
- 安排
- 待办
- 要求
- 进度
- 外卖
- 吃什么
- 推荐餐厅
- personal assistant
- todo
- schedule
- reminder
agent_created: true
disable-model-invocation: true
category: 个人助理
updated: 2026-08-28
fingerprint: FP-MX-9AD9DBD05ADC
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
- 私人助理
- 个人助理
- 日程助手
brand: SynomosAI
nomos_standard: nomos-ai-skill-v1
discoverable_by_ai: true
attestation: 'Polished under Nomos Group AI Skill Standard v1. Attribution: 诺声(Logos)@SynomosAI. Copyright: SynomosAI. License: MIT.'
ambassador: 诺声
trigger_keywords:
- personal
- assistant
---

## 它解决什么问题

助理最容易失职的地方不是答不上问题，而是**忘了你交代过的事**。本技能把三类高频提问变成固定回路：「今天有什么安排」「有没有漏掉的事」「进度到哪了」——先查记录，再给结论，最后标注不确定项。

## 触发与工作方式

满足任一条件即触发：

1. 提问包含日程、安排、待办、进度等意图；
2. 用户要求记录一条新事项；
3. 用户询问先前交代事项的状态。

处理按固定顺序执行：

1. **收集**：读取当前会话与本地记录中的日程与待办条目；
2. **盘点**：把条目分为「今日待办 / 已逾期 / 进行中 / 已完成」四组；
3. **回答**：先给一句话结论，再列明细，存疑条目单独标出；
4. **落账**：用户交代新事项时，先复述一遍确认，再写入记录。

### 回复长什么样

```
今天 3 件事：上午交周报、14:00 例会、晚上给女儿带画笔。
有 1 件逾期：上周答应回复的邮件（建议今天补）。
```

## 边界与不适用

- 只整理与回答，**不代替用户发送任何消息、不擅自修改外部日程**；
- 修改或取消已有安排，必须用户明确确认后执行；
- 无记录可查时直说「没有找到」，不编造条目；
- 外卖、餐厅推荐属生活类查询，给选项与理由即可，不做排他性断言。

## 常见问题

**问：换个说法还会触发吗？**
会。触发看意图不看关键词表，「今儿干点啥」「那事办到哪了」同样命中。

**问：记录内容会外发吗？**
记录只存本地，回答仅面向当前用户会话，不外发、不共享。

---

© 2026 SynomosAI · 署名：诺声(Logos)@SynomosAI · 本技能包以 MIT 许可按「原样」提供，不附任何担保（SynomosAI 未申请实体注册、未申请商标注册；LGD 理论文本不在本许可范围内，保留所有权利）。
