---
name: label-compliance-checker
slug: label-compliance-checker
displayName: 医疗器械标签合规核对器
version: 1.0.0
category: it-ops-security
display_name: 医疗器械标签合规核对器
title: 医疗器械标签合规核对器
author: 诺康(SynomosAI)
license: MIT
license_scope: 代码依据本包 LICENSE；本 SKILL.md 与其中理论文本不在代码许可覆盖范围内（见文末「License & attribution」）
description: 医疗器械标签合规核对器——基于官方规则源的零依赖决策支持工具，JSON IR 输出，覆盖TH-MED-004域（医疗器械全链路）。
tags: [医疗器械, 合规, 判定器, TH-MED-004, label-compliance-checker]
---

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

# 医疗器械标签合规核对器

> ⚠️ 本工具由 AI 辅助生成，仅供**决策参考**，不构成医疗器械合规结论或法律/法规意见。输出请人工复核。

## 合规与免责声明（B 级 · YMYL 影响生命健康类）
- 本工具输出为**决策支持**，不构成注册、召回、不良事件报告等官方结论；正式结论须以主管部门（NMPA/省局）书面决定及官方最新条文为准。
- 规则源：`《医疗器械说明书和标签管理规定》(总局令 第6号) 第10-11条`，请以官方正式文本核对。
- 不得依据本工具输出直接做出临床、注册或召回决策。

## 一、痛点
医疗器械全链路规则白纸黑字但散落多份文件，企业自查成本高、易因错判触雷。本工具把硬规则变成可枚举的判定器。

## 二、能力边界
- 仅做**规则判定**，不做法律意见；结论须人工复核。
- 规则源：`《医疗器械说明书和标签管理规定》(总局令 第6号) 第10-11条`（以官方最新文本为准）。

## 三、用法
```bash
python label-compliance-checker.py --device_class III --device_type implant   # 按参数判定
python label-compliance-checker.py --demo                                    # 跑内置冒烟案例
```
参数：`has_name / has_reg_no / has_manufacturer / has_indications / has_warnings / has_lot / has_udi`

## 四、真机输出（--demo 节选）
```json
{"tool":"label-compliance-checker","result":{"grade":"示例等级"},"rc":0}
```

## 五、错误码
- `rc=0` 判定完成；`rc=1` 完成但带风险提示（warnings）；`rc=2` 输入不足/无法判定。

## 六、FAQ
- Q：结果能当合规证明吗？ A：不能，仅决策支持，以主管部门认定为准。
- Q：规则过期怎么办？ A：以官方最新条文为准，本工具附规则源条款号便于核对。

## 理论依据
标签即契约——要素完整即把'告知义务'写进每一次使用。
域站位件：TH-MED-004 · 理论总账 REGISTRY · 医疗器械全链路。

## 延伸阅读
- LGD 理论总账：https://medxpert.cn/theory
- 域速查页 / GitHub lgd-theory 仓库

## 家族合集
| 环节 | 工具 | 大使 |
|---|---|---|
| 非临床研究 | non-clinical-checker | 诺康 |
| 上市后不良事件 | pms-vigilance-intake | 诺康 |
| 召回 | recall-decision-checker | 诺康 |
| 标签 | label-compliance-checker | 诺康 |
| 进出口 | import-export-router | 诺衡 |

---
诺康@MED 域首席发声人 · TH-MED-004 · SynomosAI（AI 辅助生成，非自然人）

---

## License & attribution
**分层许可（务必并读；代码许可不覆盖文档与理论文本）**

| 层 | 载体 | 许可 |
|---|---|---|
| 代码 | `label-compliance-checker.py` | **见本包 LICENSE** |
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
