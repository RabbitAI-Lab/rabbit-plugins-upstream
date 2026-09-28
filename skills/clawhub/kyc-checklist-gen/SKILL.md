---
name: kyc-checklist-gen
slug: kyc-checklist-gen
display_name: KYC 材料齐备清单
displayName: KYC 材料齐备清单
title: KYC 材料齐备清单
version: 1.1.0
category: ai-agent
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Bash, Write, WebFetch
description: KYC 材料齐备清单 — 一键生成个人/企业 KYC 必备材料清单并核算齐备度，缺项即 FAIL（零依赖）
tags: [诺声, AI技能, SynomosAI, AI 治理, kyc-checklist-gen]
summary: KYC 材料齐备清单 — 一键生成个人/企业 KYC 必备材料清单并核算齐备度，缺项即 FAIL（零依赖）
display_name_en: KYC Checklist Generator
agent_created: true
copyright: SynomosAI
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---








# KYC 材料齐备清单 / KYC 材料齐备清单

**kyc-checklist-gen** v1.1.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
开户/接商户前不知道 KYC 要备什么材料，来回补件浪费时间

## 能力边界
**能做什么**
- 按本技能定义的规程落地「KYC 材料齐备清单」相关能力。
**不能 / 不做什么**
- 不替代专业判断与官方合规口径；关键决策须人工复核。
- 不存储敏感明文、口令、密钥；凭据一律走保险库。
**何时不用（❌）**
- 仅需一次性答案、不需沉淀为可复用资产时，直接询问即可。
- 涉及医疗/临床/疗效声明或受监管专业决策时，须转人工与持证专业意见。

## 用法
```bash
python scripts/kyc_checklist_gen.py --help
```
- 合规 PASS → rc=0；违规 FAIL → rc=1；用法错误 → rc=2
- 支持 --json 机器可读输出

## 输出示例（真机）
（运行上方 `--help` 查看完整参数；带参运行即得确定性输出）

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：KYC 材料齐备清单能完全自动搞定吗？**
A：不能。本技能是方法论/规程，关键判断与跨技能执行需人工或协同技能确认。

**Q：可以直接当法规/专业意见用吗？**
A：不能。仅作辅助框架，最终以官方最新文本与持证专业意见为准。

## 理论依据
本技能是「LGD 三律」在 金融 场景的落地件：让 AI 的每一次输出**有籍可查、有证可依、有门禁可控**。

## 免责 / Disclaimer
本工具为合规初筛辅助，不构成法律/投资/医疗意见；重要决策请咨询持牌专业人士。

---

© SynomosAI · LGD-Powered · [![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 安装与使用矩阵
```bash
# 一键获取（skills CLI）
npx skills@1.7.0 add https://github.com/zhaoxinghua09-cell/agent-skills/tree/v2026.09.28.1/skills/kyc-checklist-gen

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone --branch v2026.09.28.1 --depth 1 https://github.com/zhaoxinghua09-cell/agent-skills.git
# 校验：git -C agent-skills rev-parse HEAD 应与发布标签 v2026.09.28.1 一致
cp -r agent-skills/skills/kyc-checklist-gen ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/kyc-checklist-gen/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |

## 合规与免责声明
- 本技能为辅助性合规框架/工具，**不替代持证专业意见与官方最新文本**；关键判断须人工或协同持证专业意见确认。
- 输出涉及的法规/标准/条款以官方发布版本为准；本技能仅作结构化自检参考。
- 本技能默认**本地离线运行**，不采集、不上传用户业务数据；如涉及敏感数据，请遵循最小必要与本地处理原则。

---

## License & attribution
**分层许可（务必并读；代码许可不覆盖文档与理论文本）**

| 层 | 载体 | 许可 |
|---|---|---|
| 代码 | `kyc_checklist_gen.py` | **MIT** |
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

**本包补充（包级许可事实）**：本包代码文件 `kyc_checklist_gen.py` = **MIT**；本 `SKILL.md` / `README.md` 及其中的理论文本**不在任何代码许可（含 MIT / Apache-2.0）覆盖范围内**。
