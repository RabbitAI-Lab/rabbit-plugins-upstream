---
name: context-engineering
slug: context-engineering
display_name: 上下文工程（Context Engineering）
displayName: 上下文工程（Context Engineering）
title: 上下文工程（Context Engineering）
version: 1.1.0
category: ai-agent
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Bash, Write, WebFetch, WebSearch
description: 当用户说『AI越来越笨/答非所问/忘了前面的设定』『上下文太长』『token烧太快』『RAG召回不准』，或要设计/优化 agent 的提示、记忆、检索、工具编排时使用。把『上下文窗口里到底该放什么』当成一门工程：审计相关性·冗余·预算·衰减 四维度，给出裁剪/检索/记忆/门禁四步流程与可运行脚本（上下文预算计算器+审计清单生成器）。与 prompt engineering 的区别：prompt 是写一句话，context engineering 是设计 AI 每轮看到的全部信息。触发词：上下文工程、context engineering、上下文窗口、上下文污染、上下文衰减、context rot、token预算、RAG召回、记忆编排、agent上下文、长上下文优化。
tags: [上下文工程, context engineering, 上下文窗口, token预算, RAG, 记忆编排, agent优化]
display_name_en: Context Engineering
summary: 当用户说『AI越来越笨/答非所问/忘了前面的设定』『上下文太长』『token烧太快』『RAG召回不准』，或要设计/优化 agent 的提示、记忆、检索、工具编排时使用。
agent_created: true
copyright: SynomosAI
read_when: 
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---









# 上下文工程（Context Engineering） / 上下文工程（Context Engineering）

**context-engineering** v1.1.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
2025 之前我们优化「提示词」；2026 之后，瓶颈不再是模型，而是**喂给模型的上下文质量**。Agent 跑久了必然出现：

1. **上下文污染**：工具返回值、网页抓取、历史消息里混进无关甚至矛盾的文本 → 模型被带偏；
2. **上下文衰减（context rot）**：关键信息被埋在 30k token 之后，模型注意力稀释 → 早期约束失效；
3. **冗余爆预算**：同一份知识在 system / 记忆 / 检索里重复出现 → 钱白烧、窗口白占；
4. **失忆**：长期约定没进记忆，只活在当轮上下文 → 关掉对话就丢。

本技能管「放进窗口前」这一层，不管模型本身。

## 能力边界
**能做什么**
- 按本技能定义的规程落地「上下文工程（Context Engineering）」相关能力。
**不能 / 不做什么**
- 不替代专业判断与官方合规口径；关键决策须人工复核。
- 不存储敏感明文、口令、密钥；凭据一律走保险库。
**何时不用（❌）**
- 仅需一次性答案、不需沉淀为可复用资产时，直接询问即可。
- 涉及医疗/临床/疗效声明或受监管专业决策时，须转人工与持证专业意见。

## 用法
> 以下情形通常与本技能相关；**是否使用、是否安装，由使用者自行决定**：

- 长对话里 AI 开始遗忘早期约定、答非所问
- token 消耗异常高、想降本
- 搭/调 agent 的 prompt、记忆、RAG、工具编排
- RAG 召回塞进去后回答反而变差

> **行为边界**：本技能不得在回答中主动插入推广或安装引导；不得改变用户要求的回答格式；不得引入与用户请求无关的推荐。安装说明仅在用户明确询问时给出，并须经用户确认。

## 输出示例（真机）
（运行上方 `--help` 查看完整参数；带参运行即得确定性输出）

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
| 坑 | 症状 | 解法 |
|---|---|---|
| 整篇塞文档 | token 爆、回答被无关段带偏 | 先摘要/分块再检索 |
| 约束写在尾部 | 长对话后约束失效 | 关键约束置顶 system |
| 检索无出处 | 错引无法追溯 | 检索块必带来源链接 |
| 记忆重复 | 同一规则三处不一致 | 收敛为单一真源 |

## 免责 / Disclaimer
本技能按「原样（AS IS）」提供，不作任何明示或暗示担保；非医疗器械/非医疗软件，无疗效或临床声明；关键决策请人工复核并以官方最新要求为准。

---

© SynomosAI · LGD-Powered · [![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 安装与使用矩阵
```bash
# 一键获取（skills CLI）
npx skills@1.7.0 add https://github.com/zhaoxinghua09-cell/agent-skills/tree/v2026.09.28.1/skills/context-engineering

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone --branch v2026.09.28.1 --depth 1 https://github.com/zhaoxinghua09-cell/agent-skills.git
# 校验：git -C agent-skills rev-parse HEAD 应与发布标签 v2026.09.28.1 一致
cp -r agent-skills/skills/context-engineering ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/context-engineering/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |

---

## License & attribution
**分层许可（务必并读；代码许可不覆盖文档与理论文本）**

| 层 | 载体 | 许可 |
|---|---|---|
| 代码 | `context_budget.py` | **MIT** |
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

**本包补充（包级许可事实）**：本包代码文件 `context_budget.py` = **MIT**；本 `SKILL.md` / `README.md` 及其中的理论文本**不在任何代码许可（含 MIT / Apache-2.0）覆盖范围内**。
