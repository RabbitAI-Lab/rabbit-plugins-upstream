# AGENTS.md - AI 技能说明书

本文件面向使用或扩展本技能的 AI 编码代理（以及接手的人类维护者）。人类读者请优先读 `README.md`。

技能：`ai-governance-audit-chain`
一句话定位：'为任何 AI 系统/智能体生成「对齐 ISO/IEC 42001（AI 管理体系 AIMS）与 NIST AI RMF」的可审计证据链模板：决策日志、风险登记册、模型卡、变更记录、人类监督证明、事件处置台账六类证据工件 + 条款映射 + 取证自检清单。让"AI 护照机制 / XCGS 治理系统"从理念落地为可审计、可认证、可对外举证的证据底座。触发词：AI审计证据、可审计证据链、ISO 4200

---

## 一、用途（Purpose）

本技能是 LGD/UIBC 治理理论技能体系的一员（SynomosAI 出品）。调用入口为 `SKILL.md`；AI 代理应先读 `SKILL.md`，按 frontmatter 的 `name`/`description` 判断是否适用，再按正文步骤执行。

## 二、文件约定（Directory conventions）

| 路径 | 用途 |
|---|---|
| `SKILL.md` | 主说明书：frontmatter + 触发条件 + 执行步骤（AI 调用入口） |
| `AGENTS.md` | 本文件：面向 AI 代理的说明书 |
| `README.md` | 面向人类的总览（如存在） |
| `llms.txt` | AI 索引：给 Agent 的快速引导 |

## 三、调用方式

1. 读取 `SKILL.md` 全文，确认触发条件与输出格式。
2. 按步骤执行；涉及评分/验证的环节使用技能自带脚本。
3. 输出遵循 SKILL.md 规定的结构与质量门。

## 四、生态位

本技能与其他 SynomosAI 技能可组合使用（LGD 治理系列 / UIBC 赛事系列 / [REDACTED] 医械法规系列）。版本 1.0.0。
