---
name: judging-rubric-grader
slug: judging-rubric-grader
displayName: 赛事评审打分器
version: 1.1.0
category: ai-agent
display_name: 赛事评审打分器
title: 赛事评审打分器
author: 诺律(SynomosAI)
license: MIT
license_scope: 代码依据本包 LICENSE；本 SKILL.md 与其中理论文本不在代码许可覆盖范围内（见文末「License & attribution」）
description: 赛事评审打分器——基于 UIBC 赛事规范的零依赖决策支持工具，JSON IR 输出，覆盖TH-EVT-003域。
tags: [赛事, 判定器, TH-EVT-003, judging-rubric-grader]
---

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

# 赛事评审打分器

> ⚠️ 本工具由 AI 辅助生成，仅供**决策参考**，不构成赛事终裁。输出请人工复核（组委会保留最终裁定权）。

## 一、痛点
赛事规模化运营中，提交校验/赛题生成/评审打分/反作弊/查重等环节人工成本高、标准易漂移。本工具把赛事规范变成可枚举的判定器。

## 二、能力边界
- 仅做**规则判定**，不做赛事终裁；结论须人工复核。
- 规则源：`UIBC 评审规范（rubric 加权）`（以 UIBC 赛事章程最新版为准）。

## 三、用法
```bash
python judging-rubric-grader.py --demo            # 跑内置冒烟案例
```
参数：`criteria / scores / pass_line`

## 四、真机输出（--demo 节选）
```json
{"tool":"judging-rubric-grader","rc":0}
```

## 五、错误码
- `rc=0` 判定完成；`rc=1` 完成但带风险提示（warnings）；`rc=2` 输入不足/无法判定。

## 六、FAQ
- Q：结果能当赛事终裁吗？ A：不能，仅决策支持，以组委会认定为准。
- Q：规则过期怎么办？ A：以 UIBC 章程最新版为准，本工具附规则源便于核对。

## 理论依据
评审须可被问责——rubric 加权即把'凭什么打分'写进可审计的记录。
域站位件：TH-EVT-003 · UIBC 赛事线。

## 延伸阅读
- LGD 理论总账：https://medxpert.cn/theory
- UIBC 赛事官网 / GitHub lgd-theory 仓库

## 家族合集
| 赛事环节 | 工具 | 大使 |
|---|---|---|
| 报名/提交门户 | contest-submission-portal | 诺声 |
| 赛题生成 | problem-set-generator | 诺声 |
| 评审打分 | judging-rubric-grader | 诺律 |
| 反作弊/身份核验 | anti-cheat-identity | 诺卫 |
| 作品查重 | originality-check | 诺源 |

---
诺律@LAW 域首席发声人 · TH-EVT-003 · SynomosAI（AI 辅助生成，非自然人）

---

## License & attribution
**分层许可（务必并读；代码许可不覆盖文档与理论文本）**

| 层 | 载体 | 许可 |
|---|---|---|
| 代码 | `judging-rubric-grader.py` | **见本包 LICENSE** |
| 文档与理论文本 | 本 `SKILL.md`、`README.md`、其中「理论依据」段与一切理论表述 | **不在代码许可覆盖范围内**：保留所有权利（All rights reserved） |

> 即：**代码可依其自身许可使用与再分发；文档与理论文本不因代码许可而默认可自由再发布。**

```
© 2026 赵兴华 / Steven Zhao·China (ORCID 0009-0001-0512-1237). All rights reserved.
理论署名 (attribution) : LGD（Lifecycle Governance Doctrine / 全程治理论）— SynomosAI initiative
名称状态 (name status)  : "SynomosAI" / "MedXpert" — 未申请实体注册、未申请商标注册
                        (not a registered legal entity; no trademark registered)
生产参考部署 (production reference, self-reported) : MedXpert
                    ← 非认证、非背书、非监管认可（not a certification or endorsement）
代码许可 (code license) : 本包未附 LICENSE 文件（许可待定）
                    本文本与理论表述不在任何代码许可覆盖范围内
引用格式 (cite as)      : 本资产无 DOI
```
（上列为《LGD 对外表述规范》§3.2 统一块：**A 段公共段逐字复制、未删改；B 段资产参数段按本包真值填写**；发布 / 重提前须照最新版本复核。）
