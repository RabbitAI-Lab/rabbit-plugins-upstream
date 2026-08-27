---
name: ppap-submission
description: Build and review AIAG PPAP Level 3 submission packages (18 elements, PSW, Cpk/Ppk) for automotive and electronics parts.
description_zh: "按 AIAG PPAP 第四版 Level 3 编制与审核汽车/电子零部件提交包，覆盖 18 项要素、PSW、Cpk/Ppk 与初始过程研究。"
description_en: "Build and review AIAG PPAP 4th-edition Level 3 submission packages for automotive and electronics parts: 18 elements, PSW, Cpk/Ppk, initial process studies."
display_name: "PPAP 提交包专家（AIAG Level 3）"
display_name_en: "PPAP Submission Package Expert (AIAG Level 3)"
version: 1.0.0
visibility: "public"
user-invocable: true
metadata:
  openclaw:
    emoji: "📦"
---

# PPAP 提交包专家（AIAG PPAP 4th Ed / Level 3）

## 概述

依据 AIAG PPAP 第四版标准，协助完成 PPAP 提交包的编制、自查与送审。覆盖 **18 项标准要素**、Level 1–5 提交等级、PSW（零件提交保证书）签署，以及客户特殊要求（如 Harman RBA、Lamborghini 等）的差异化核对。默认按 **Level 3**（最常用、最完整）编制。

## 审核触发条件

当用户提供以下内容时，自动触发此技能：
- 新项目 PPAP 提交包编制（如 8740519 A110BT-Lamborghini PPAP V15）
- 提交等级（Level 1–5）与应提交文件清单核对
- 18 项要素完整性 / 一致性审查（PFMEA ↔ 控制计划 ↔ 作业指导书 ↔ SIPOC）
- 初始过程能力评估（Cpk/Ppk ≥ 1.33）、MSA（GRR < 10% 优秀 / < 30% 可接受）
- PSW（零件提交保证书）填写 / 审核

---

## 第一部分：18 项标准要素（必须提交项）

| # | 要素 | 说明 |
|---|------|------|
| 1 | 设计记录（Design Record） | 图纸 / 数模，含最新版本号 |
| 2 | 授权工程变更文件（EWO/ECN） | 变更单及审批 |
| 3 | 顾客工程批准 | 客户签核的样件/偏差批准 |
| 4 | DFMEA | 设计责任方须提交 |
| 5 | 过程流程图（Process Flow） | 全流程含检验/返工 |
| 6 | PFMEA | 过程失效模式与后果分析 |
| 7 | 控制计划（Control Plan） | 试产/量产控制计划 |
| 8 | 测量系统分析（MSA） | GRR、偏倚、线性、稳定性 |
| 9 | 尺寸结果（Dimensional Results） | 全尺寸实测记录 |
| 10 | 材料/性能试验记录 | 材质证明、性能测试 |
| 11 | 初始过程研究（Cpk/Ppk） | 关键/重要特性能力 |
| 12 | 合格实验室文件 | 内部/外部实验室资质 |
| 13 | 外观批准报告（AAR） | 外观件适用 |
| 14 | 生产件样品 | 按等级提交数量 |
| 15 | 标准样品（Master Sample） | 封样留存 |
| 16 | 检查辅具（Checking Aids） | 检具/治具及校准 |
| 17 | 顾客特殊要求（CSR） | 客户附加清单 |
| 18 | 零件提交保证书（PSW） | 正式提交签署文件 |

> 详见 `references/ppap-elements.md`（每项提交要点与常见缺失）。

---

## 第二部分：提交等级矩阵（Level 1–5）

- **Level 1**：仅提交 PSW（及客户指定的少数文件）
- **Level 2**：PSW + 有限支持数据（复印件）
- **Level 3**：PSW + 完整数据 + 样品（**最常用，默认采用**）
- **Level 4**：PSW + 客户指定的其他要求
- **Level 5**：PSW + 现场评审（在供应商现场）

默认按 **Level 3** 编制完整提交包。勾选清单见 `references/level3-filelist.md`，每项列出：要素 / 应提交文件 / 责任人 / 完成日期 / 状态。

---

## 第三部分：审核要点（一致性核对）

1. **版本一致性**：设计记录版本号 ↔ DFMEA ↔ PFMEA ↔ 控制计划 ↔ 作业指导书 ↔ 检验规范 全部一致
2. **特性传递闭环**：图纸特殊特性 → PFMEA（失效） → 控制计划（控制） → 检验/尺寸记录 可追溯
3. **能力证据**：关键/重要特性 Cpk ≥ 1.33；MSA GRR 达标；初始研究样本量、日期合理
4. **时间逻辑**：试产日期 → MSA/初始研究日期 → PSW 签署日期 顺序合理、无矛盾
5. **客户特殊要求**：Harman/RBA、Lamborghini 等附加清单（如 RBA Risk SAQ、CDP）有无遗漏

---

## 第四部分：输出格式（严格执行）

完成编制 / 审核后，按以下结构输出：

```
【一、PPAP 提交包清单（Level 3）】
要素 | 应提交文件 | 状态（✅已备/⚠️缺失/🔄进行中） | 责任人 | 完成日期
1 设计记录 | ... | ... | ... | ...
... （逐项到 18）

【二、缺口与风险清单】
- 缺项：[要素 + 文件 + 影响]
- 不一致：[两张文件冲突点]
- 能力不达标：[特性 + Cpk 值 + 整改方向]

【三、PSW 关键字段核对】
零件号：[ ]  工程变更等级：[ ]  提交等级：[ ]  结果：[批准/临时批准/拒收]
```

---

## 审核执行流程

1. **接收需求** → 识别项目、客户、提交等级（默认 Level 3）
2. **要素核对** → 按第一部分 18 项逐项确认文件齐备
3. **一致性审查** → 执行第三部分 5 项核对
4. **能力评估** → 检查 Cpk/Ppk、MSA 是否达标
5. **输出结果** → 严格按第四部分格式输出清单与风险项

---

## 审核依据标准

- AIAG PPAP 第四版
- IATF 16949:2016 — 8.3.4.4（PFMEA/控制计划）、8.5.6（变更）
- 顾客特定要求（CSR，如 Harman、Lamborghini）
