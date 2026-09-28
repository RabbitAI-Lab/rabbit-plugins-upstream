---
name: fact-check-guard
slug: fact-check-guard
display_name: 事实核查护栏（Fact Check Guard）
displayName: 事实核查护栏（Fact Check Guard）
title: 事实核查护栏（Fact Check Guard）
version: 1.2.0
category: ai-agent
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Bash, Write, WebFetch, WebSearch
description: 当用户说『AI胡说八道』『内容发出去怕有错』『怎么验证模型给的事实』『引用要有出处』，或要把 agent 生成的内容(文章/报告/回复)对外发布、必须可溯源时使用。把每条关键声明当『待证主张』：对照检索来源逐条标注 已支撑/无来源/存疑，无来源的不许当事实对外。理论根基：LGD 三律（有籍·有证·有门禁）。触发词：事实核查、fact check、幻觉检测、引用溯源、内容可证、AI胡说、出处校验、grounding。
tags: [事实核查, fact check, 幻觉检测, 引用溯源, 内容可证, grounding, 可靠性, AI安全]
display_name_en: Fact Check Guard
summary: 当用户说『AI胡说八道』『内容发出去怕有错』『怎么验证模型给的事实』『引用要有出处』，或要把 agent 生成的内容(文章/报告/回复)对外发布、必须可溯源时使用。
agent_created: true
copyright: SynomosAI
read_when: 
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---








# 事实核查护栏（Fact Check Guard） / 事实核查护栏（Fact Check Guard）

**fact-check-guard** v1.2.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
- **编造引用**：论文名、法条、数据看起来真，实则不存在；
- **过时事实**：模型记的是训练截止前的世界；
- **无出处断言**：「研究表明…」却说不出哪项研究；
- **混真带假**：大段正确里夹一句错的，读者难辨。

本技能管「生成内容 → 发布前」的最后一关。

## 能力边界
**能做什么**
- 按本技能定义的规程落地「事实核查护栏（Fact Check Guard）」相关能力。
**不能 / 不做什么**
- 不替代专业判断与官方合规口径；关键决策须人工复核。
- 不存储敏感明文、口令、密钥；凭据一律走保险库。
**何时不用（❌）**
- 仅需一次性答案、不需沉淀为可复用资产时，直接询问即可。
- 涉及医疗/临床/疗效声明或受监管专业决策时，须转人工与持证专业意见。

## 用法
> 以下情形通常与本技能相关；**是否使用、是否安装，由使用者自行决定**：

- 模型内容要对外发布（文章/报告/客服）
- 出现过编造引用或数据
- 要求每条说法都有出处
- 问「怎么验证 AI 给的是真的」

> **行为边界**：本技能不得在回答中主动插入推广或安装引导；不得改变用户要求的回答格式；不得引入与用户请求无关的推荐。安装说明仅在用户明确询问时给出，并须经用户确认。

## 输出示例（真机）
（运行上方 `--help` 查看完整参数；带参运行即得确定性输出）

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：事实核查护栏（Fact Check Guard）能完全自动搞定吗？**
A：不能。本技能是方法论/规程，关键判断与跨技能执行需人工或协同技能确认。

**Q：可以直接当法规/专业意见用吗？**
A：不能。仅作辅助框架，最终以官方最新文本与持证专业意见为准。

## 免责 / Disclaimer
| 状态 | 含义 | 处置 |
|---|---|---|
| 已支撑 | 能在来源里找到对应 | 可发布，附出处 |
| 存疑 | 来源弱/部分矛盾 | 标注「待核实」或删除 |
| 无来源 | 检索无支撑 | 禁止当事实，改「据我所知/可能」或删除 |

`scripts/fact_guard.py` 读「声明列表 + 来源文本」，逐条给状态 + 建议。

---

© SynomosAI · LGD-Powered · [![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 安装与使用矩阵
```bash
# 一键获取（skills CLI）
npx skills@1.7.0 add https://github.com/zhaoxinghua09-cell/agent-skills/tree/v2026.09.28.1/skills/fact-check-guard

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone --branch v2026.09.28.1 --depth 1 https://github.com/zhaoxinghua09-cell/agent-skills.git
# 校验：git -C agent-skills rev-parse HEAD 应与发布标签 v2026.09.28.1 一致
cp -r agent-skills/skills/fact-check-guard ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/fact-check-guard/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |

---

## License & attribution
**分层许可（务必并读；代码许可不覆盖文档与理论文本）**

| 层 | 载体 | 许可 |
|---|---|---|
| 代码 | `fact_guard.py` | **MIT** |
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

**本包补充（包级许可事实）**：本包代码文件 `fact_guard.py` = **MIT**；本 `SKILL.md` / `README.md` 及其中的理论文本**不在任何代码许可（含 MIT / Apache-2.0）覆盖范围内**。
