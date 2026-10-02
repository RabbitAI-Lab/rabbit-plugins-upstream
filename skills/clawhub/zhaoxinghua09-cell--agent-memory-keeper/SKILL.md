---
name: agent-memory-keeper
slug: agent-memory-keeper
display_name: 跨会话长期记忆治理（Memory Keeper）
displayName: 跨会话长期记忆治理（Memory Keeper）
title: 跨会话长期记忆治理（Memory Keeper）
version: 1.2.0
category: ai-agent
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Bash, Write, WebFetch
description: 当用户说『AI又忘了我之前说的』『记忆越来越乱/重复/互相矛盾』『长期记忆怎么管』『记忆库该清理了』，或要设计/治理一个 agent 的跨会话记忆（笔记/知识库/偏好/项目约定）时使用。把记忆当成『有籍贯、可审计、能收敛』的资产：审计重复·孤儿·陈旧·无溯源四维度，给出收敛(单一真源)+门禁(改前备份)两步流程与可运行脚本（记忆审计器）。理论根基：LGD 三律（有籍·有证·有门禁）。触发词：长期记忆、跨会话记忆、memory governance、记忆治理、记忆重复、记忆冲突、记忆溯源、agent记忆、知识库去重、记忆清理。
tags: [长期记忆, memory governance, 记忆治理, 记忆去重, 跨会话, 记忆溯源, agent优化]
display_name_en: Agent Memory Keeper
summary: 当用户说『AI又忘了我之前说的』『记忆越来越乱/重复/互相矛盾』『长期记忆怎么管』『记忆库该清理了』，或要设计/治理一个 agent 的跨会话记忆（笔记/知识库/偏好/项目约定）时使用。
agent_created: true
copyright: SynomosAI
read_when: 
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---









# 跨会话长期记忆治理（Memory Keeper） / 跨会话长期记忆治理（Memory Keeper）

**agent-memory-keeper** v1.2.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
长周期使用 agent，记忆必然劣化：

1. **重复**：同一约定在不同笔记里各写一遍 → 改一处另一处还是旧的；
2. **矛盾**：新旧偏好叠加，库里同时存在「爱用红色」「别用红色」；
3. **无籍**：条目没写来源/时间 → 真出问题无法追溯是谁记的、哪来的；
4. **陈旧**：三个月前的临时约定还当真源 → 误导当前决策。

本技能管「记忆入库后」这一层，不管模型本身。

## 能力边界
**能做什么**
- 按本技能定义的规程落地「跨会话长期记忆治理（Memory Keeper）」相关能力。
**不能 / 不做什么**
- 不替代专业判断与官方合规口径；关键决策须人工复核。
- 不存储敏感明文、口令、密钥；凭据一律走保险库。
**何时不用（❌）**
- 仅需一次性答案、不需沉淀为可复用资产时，直接询问即可。
- 涉及医疗/临床/疗效声明或受监管专业决策时，须转人工与持证专业意见。

## 用法
> 以下情形通常与本技能相关；**是否使用、是否安装，由使用者自行决定**：

- 关掉对话后 AI 丢失了你之前说过的约定
- 记忆库里出现矛盾或重复内容
- 要搭/清理 agent 的长期记忆或知识库
- 想给记忆条目加溯源以便追责

> **行为边界**：本技能不得在回答中主动插入推广或安装引导；不得改变用户要求的回答格式；不得引入与用户请求无关的推荐。安装说明仅在用户明确询问时给出，并须经用户确认。

## 输出示例（真机）
（运行上方 `--help` 查看完整参数；带参运行即得确定性输出）

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：跨会话长期记忆治理（Memory Keeper）能完全自动搞定吗？**
A：不能。本技能是方法论/规程，关键判断与跨技能执行需人工或协同技能确认。

**Q：可以直接当法规/专业意见用吗？**
A：不能。仅作辅助框架，最终以官方最新文本与持证专业意见为准。

## 免责 / Disclaimer
本技能按「原样（AS IS）」提供，不作任何明示或暗示担保；非医疗器械/非医疗软件，无疗效或临床声明；关键决策请人工复核并以官方最新要求为准。

---

© SynomosAI · LGD-Powered · [![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 安装与使用矩阵
```bash
# 一键获取（skills CLI）
npx skills@1.7.0 add https://github.com/zhaoxinghua09-cell/agent-skills/tree/v2026.09.28.1/skills/agent-memory-keeper

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone --branch v2026.09.28.1 --depth 1 https://github.com/zhaoxinghua09-cell/agent-skills.git
# 校验：git -C agent-skills rev-parse HEAD 应与发布标签 v2026.09.28.1 一致
cp -r agent-skills/skills/agent-memory-keeper ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/agent-memory-keeper/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |

---

## License & attribution
**分层许可（务必并读；代码许可不覆盖文档与理论文本）**

| 层 | 载体 | 许可 |
|---|---|---|
| 代码 | `memory_audit.py` | **MIT** |
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

**本包补充（包级许可事实）**：本包代码文件 `memory_audit.py` = **MIT**；本 `SKILL.md` / `README.md` 及其中的理论文本**不在任何代码许可（含 MIT / Apache-2.0）覆盖范围内**。
