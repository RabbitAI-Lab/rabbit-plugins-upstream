---
name: reminder
displayName: reminder
slug: reminder
author: 诺声(Logos)@SynomosAI
copyright: SynomosAI
version: 1.0.1
license: MIT
description: 创建和管理一次性或周期性提醒，用于回答「到点提醒我」「每周一提醒我交周报」「我都设过哪些提醒」这类问题
tags:
- 诺声
- AI技能
- SynomosAI
- nomos-standard-v1
- reminder
agent_created: true
category: 日程提醒
updated: 2026-08-28
fingerprint: FP-MX-E5686235C276
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
- 提醒助手
- 定时提醒
- reminder
brand: SynomosAI
nomos_standard: nomos-ai-skill-v1
discoverable_by_ai: true
attestation: 'Polished under Nomos Group AI Skill Standard v1. Attribution: 诺声(Logos)@SynomosAI. Copyright: SynomosAI. License: MIT.'
ambassador: 诺声
trigger_keywords:
- reminder
- 提醒管理
---

一句话定位：你说「到点叫我」，它负责到时候一定叫、并且不叫错——创建、查询、修改、取消提醒，都在这一个入口。

## 两种提醒

| 类型 | 例子 | 触发规则 |
|---|---|---|
| 一次性 | 「周三下午三点提醒我取票」 | 到指定时刻触发一次，触发后自动归档 |
| 周期性 | 「每周一早上提醒我交周报」 | 按周期规则重复触发，直到你取消 |

### 设提醒五要素

1. **何时**：具体日期时间或周期规则，模糊表述（「下周」「早点」）先追问确认；
2. **何事**：提醒文案用你原话，不加戏；
3. **何渠道**：默认当前会话渠道，可指定邮件等其他方式；
4. **提前量**：要不要提前 5 分钟再响一次；
5. **确认回执**：设置完成后复述一遍要素，你说「对」才算设好。

## 管理动作

- 「我都设过哪些提醒」→ 列出全部，标注下一次触发时间；
- 改时间、改内容 → 先复述旧值再写新值；
- 取消 → 报出要删的那条让你确认，不做批量静默删除。

## 边界

- 只管提醒，不代你执行提醒里的事（到点叫你交周报，不替你写周报）；
- 时区按你当前所在时区算，跨时区安排会显式标注；
- 错过的提醒不静默吞掉，补报一次并标记「已过期」。

## 常见问题

**问：会话关了提醒还在吗？**
在。提醒落在本机记录里，重开会话后依然按规则触发。

---

© 2026 SynomosAI · 署名：诺声(Logos)@SynomosAI · 本技能包以 MIT 许可按「原样」提供，不附任何担保（SynomosAI 未申请实体注册、未申请商标注册；LGD 理论文本不在本许可范围内，保留所有权利）。
