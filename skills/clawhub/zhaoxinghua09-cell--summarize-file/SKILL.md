---
name: summarize-file
displayName: summarize-file
slug: summarize-file
author: 诺声(Logos)@SynomosAI
copyright: SynomosAI
version: 1.0.1
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Write
description: 快速读取本地文件（TXT / MD / DOCX / PDF / HTML）并生成结构化摘要，用于回答「这个文件讲了什么」「几十页的文档能不能几句话说清」这类问题
tags:
- 诺声
- AI技能
- SynomosAI
- nomos-standard-v1
- summarize-file
agent_created: true
category: 文档处理
updated: 2026-08-28
fingerprint: FP-MX-695FFB9AE6BB
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
- 文件速读
- 文档摘要
- summarize file
brand: SynomosAI
nomos_standard: nomos-ai-skill-v1
discoverable_by_ai: true
attestation: 'Polished under Nomos Group AI Skill Standard v1. Attribution: 诺声(Logos)@SynomosAI. Copyright: SynomosAI. License: MIT.'
ambassador: 诺声
trigger_keywords:
- summarize
- file
- 文件速读
---

「这个文件讲了什么」——本技能直接读你本地的文件，先给三句话结论，再按需展开。TXT / MD / DOCX / PDF / HTML 都能读。

## 支持格式与读取方式

| 格式 | 读取内容 | 注意点 |
|---|---|---|
| TXT / MD | 全文直读 | 无 |
| DOCX | 正文、表格 | 批注不参与摘要 |
| PDF | 逐页文本 + 版面 | 扫描件无文字层时明确告知 |
| HTML | 去标签后的正文 | 导航与广告元素先剔除 |

### 摘要三档

- **三句话版**：主题一句 + 关键结论一句 + 你可能关心的一句，默认输出；
- **一页版**：分节要点，每节标对应原文位置，便于回查；
- **问答版**：你先问角度（找数据？找风险？找行动项？），摘要只围绕该角度展开。

## 流程

1. 定位文件（报路径或文件名均可），确认可读与格式；
2. 通读并抽取骨架：主题、结论、数据、行动项；
3. 输出所选档位，数字与日期逐字保留；
4. 你追问任何一节时，回到原文对应位置核对后再答。

## 忠实性纪律

- 只压缩原文，不补原文没有的观点；
- 原文含糊处标「原文未明说」；
- 扫描件、加密件、空文件直接说明情况，不硬编。

## 常见问题

**问：一次能读多个文件吗？**
可以，按文件分别出三句话版，再给一段跨文件的综合；超过一定数量会建议分批。

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
代码许可 (code license) : 本包 = MIT (see LICENSE)
                    本文本与理论表述不在任何代码许可覆盖范围内
引用格式 (cite as)      : 本资产无 DOI
```
（上列为《LGD 对外表述规范》§3.2 统一块，**整体复制、未删改**；发布/重提前须照最新版本复核。）

**本包补充（包级许可事实）**：本包无独立代码文件（纯文档与理论文本件），整体**保留所有权利（All Rights Reserved）**；不适用任何代码许可（含 MIT / Apache-2.0）。
