---
name: evid-four-check
slug: evid-four-check
displayName: 电子证据四性审查判定器
version: 1.0.0
category: it-ops-security
display_name: 电子证据四性审查判定器
title: 电子证据四性审查判定器
author: 诺律(SynomosAI)
license: MIT
license_scope: 代码依据本包 LICENSE；本 SKILL.md 与其中理论文本不在代码许可覆盖范围内（见文末「License & attribution」）
description: 电子证据四性审查判定器——基于官方规则源的零依赖决策支持工具，JSON IR 输出，覆盖TH-LAW-001域。
tags: [合规, 判定器, TH-LAW-001, evid-four-check]
---

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

# 电子证据四性审查判定器

> ⚠️ 本工具由 AI 辅助生成，仅供**决策参考**，不构成专业/法律意见。输出请人工复核。

## 一、痛点
监管规则白纸黑字但散落多份文件，企业/个人自查成本高、易因错判触雷。本工具把硬规则变成可枚举的判定器。

## 二、能力边界
- 仅做**规则判定**，不做法律意见；结论须人工复核。
- 规则源：`最高法《关于民事诉讼证据的若干规定》第14/93-95条 + 《人民法院在线诉讼规则》第12-18条`（以官方最新文本为准）。

## 三、用法
```bash
python evid-four-check.py --mtow 5          # 按参数判定
python evid-four-check.py --demo            # 跑内置冒烟案例
```
参数：`type / has_signature / source_verifiable / integrity_check / relevance`

## 四、真机输出（--demo 节选）
```json
{"tool":"evid-four-check","result":{"grade":"示例等级"},"rc":0}
```

## 五、错误码
- `rc=0` 判定完成；`rc=1` 完成但带风险提示（warnings）；`rc=2` 输入不足/无法判定。

## 六、FAQ
- Q：结果能当合规证明吗？ A：不能，仅决策支持，以主管部门认定为准。
- Q：规则过期怎么办？ A：以官方最新条文为准，本工具附规则源条款号便于核对。

## 理论依据
证据须可被问责——四性审查即把'可信'写进每一次举证。
域站位件：TH-LAW-001 · 理论总账 REGISTRY。

## 延伸阅读
- LGD 理论总账：https://medxpert.cn/theory
- 域速查页 / GitHub lgd-theory 仓库

## 家族合集
| 域 | 工具 | 大使 |
|---|---|---|
| UAS 低空 | uas-ops-checker | 诺卫 |
| AUT 驾驶 | aut-grade-checker | 诺卫 |
| DAT 数据 | data-grade-checker | 诺源 |
| BIO 生物 | hgrac-route-checker | 诺康 |
| FIN 金融 | fin-ai-classifier | 诺丰 |
| LAW 法律 | evid-four-check | 诺律 |

---
诺律@LAW 域首席发声人 · TH-LAW-001 · SynomosAI（AI 辅助生成，非自然人）

---

## License & attribution
**分层许可（务必并读；代码许可不覆盖文档与理论文本）**

| 层 | 载体 | 许可 |
|---|---|---|
| 代码 | `evid-four-check.py` | **见本包 LICENSE** |
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
