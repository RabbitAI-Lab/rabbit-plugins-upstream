---
name: todo-tracker
displayName: todo-tracker
slug: todo-tracker
author: 诺声(Logos)@SynomosAI
copyright: SynomosAI
version: 1.0.1
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep
description: 创建、查看、更新、完成任务，用于回答「我有哪些待办」「这件事卡在哪」「先做哪个」这类问题
tags:
- 诺声
- AI技能
- SynomosAI
- nomos-standard-v1
- todo-tracker
agent_created: true
category: 任务管理
updated: 2026-08-28
fingerprint: FP-MX-7E361479DE01
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
- 待办追踪
- 任务清单
- todo tracker
brand: SynomosAI
nomos_standard: nomos-ai-skill-v1
discoverable_by_ai: true
attestation: 'Polished under Nomos Group AI Skill Standard v1. Attribution: 诺声(Logos)@SynomosAI. Copyright: SynomosAI. License: MIT.'
ambassador: 诺声
trigger_keywords:
- todo
- tracker
- 任务跟踪
---

待办管理失败通常不是因为记性差，而是清单里堆着写不清、分不动、查不了的任务。本技能用四个基本动作把清单管活。

## 四个基本动作

1. **建**：任务 + 一句完成判据，缺判据的先补再入账；
2. **查**：按状态（待办 / 进行中 / 卡住 / 完成）或按关键词过滤；
3. **改**：更新状态与备注，谁改的、何时改的留痕；
4. **销**：完成后标记归档，不物理删除——复盘时用得上。

### 优先级怎么排

三问定序，答不出来的先放后面：

- 不做会怎样？（后果重的优先）
- 是不是别人在等？（被依赖的优先）
- 现在做成本最低吗？（窗口期性的优先）

## 卡住了怎么办

1. 在任务上写明卡点：等谁、缺什么、卡在哪一步；
2. 判断是「等外部」还是「缺信息」——等外部就设个跟进提醒，缺信息就列出要补的信息项；
3. 卡住超过预设期限的任务自动浮到清单顶部，不许沉底装看不见。

## 纪律

- 一条任务只装一件事，「顺便再帮我……」拆成新条目；
- 完成判据没达成就不算完成，宁可标「卡住」；
- 清单是给你看的，不是给 anxiety 用的——每周可清一次「不做也死不了」的条目。

## 常见问题

**问：和日历提醒有什么区别？**
日历管「什么时候做」，本技能管「有哪些事、各自什么状态、先做哪个」，两者配合不重复。

---

© 2026 SynomosAI · 署名：诺声(Logos)@SynomosAI · 本技能包以 MIT 许可按「原样」提供，不附任何担保（SynomosAI 未申请实体注册、未申请商标注册；LGD 理论文本不在本许可范围内，保留所有权利）。

---

## License & attribution
**分层许可（务必并读；代码许可不覆盖文档与理论文本）**

| 层 | 载体 | 许可 |
|---|---|---|
| 代码 | 本包无独立代码文件（纯文档/理论件） | — |
| 文档与理论文本 | 本 `SKILL.md`、`README.md`、其中「理论依据」段与一切理论表述 | **不在 MIT 覆盖范围内**：保留所有权利（All rights reserved） |

> 即：**代码可依 MIT 使用与再分发；文档与理论文本不因代码许可而默认可自由再发布。**

```
© 2026 赵兴华 / Steven Zhao·China (ORCID 0009-0001-0512-1237). All rights reserved.
理论署名 (attribution) : LGD（Lifecycle Governance Doctrine / 全程治理论）— SynomosAI initiative
名称状态 (name status)  : "SynomosAI" / "MedXpert" — 未申请实体注册、未申请商标注册
                        (not a registered legal entity; no trademark registered)
生产参考部署 (production reference, self-reported) : MedXpert
                    ← 非认证、非背书、非监管认可（not a certification or endorsement）
代码许可 (code license) : uibc-core = Apache-2.0 (see repo LICENSE)
                    本文本与理论表述不在 Apache-2.0 覆盖范围内
引用格式 (cite as)      : uibc-core/CITATION.cff · concept DOI 10.5281/zenodo.22821834
首次公开锚 (first public): 2026-09-17 13:31:45 UTC (commit cb6f11b)
                    外锚 (external anchor): Sigstore Rekor logIndex 2883389783
```
（上列为《LGD 对外表述规范》§3.2 统一块，**整体复制、未删改**；发布/重提前须照最新版本复核。）

**本包补充（包级许可事实）**：本包无独立代码文件（纯文档与理论文本件），整体**保留所有权利（All Rights Reserved）**；不适用任何代码许可（含 MIT / Apache-2.0）。
