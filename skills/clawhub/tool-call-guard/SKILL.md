---
name: tool-call-guard
slug: tool-call-guard
display_name: 工具调用安全闸门（Tool Call Guard）
displayName: 工具调用安全闸门（Tool Call Guard）
title: 工具调用安全闸门（Tool Call Guard）
version: 1.1.0
category: it-ops-security
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Bash, Write, WebFetch, WebSearch
description: 当用户说『agent乱调工具』『误删了文件』『不该发邮件却发了』『怎么给AI的工具加权限边界』，或在给 agent 接工具（文件/网络/数据库/消息/支付）想防危险动作时使用。把每次 tool call 当『需授权操作』：按 读/写/删/外发/支付 分级，危险动作先拦截+提示确认，低风险放行。理论根基：LGD 三律（有籍·有证·有门禁）。触发词：工具调用安全、agent权限、tool call guard、危险动作拦截、误删、误发、AI工具边界、function安全。
tags: [工具调用安全, tool call guard, agent权限, 危险动作拦截, 最小权限, AI安全, 门禁]
display_name_en: Tool Call Guard
summary: 当用户说『agent乱调工具』『误删了文件』『不该发邮件却发了』『怎么给AI的工具加权限边界』，或在给 agent 接工具（文件/网络/数据库/消息/支付）想防危险动作时使用。
agent_created: true
copyright: SynomosAI
read_when: 
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---








# 工具调用安全闸门（Tool Call Guard） / 工具调用安全闸门（Tool Call Guard）

**tool-call-guard** v1.1.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
- **静默删除**：一句话就 `rm -rf` 了不该删的目录；
- **误外发**：替你把草稿邮件、内部消息发出去了；
- **越权支付**：调用了下单/转账类工具；
- **无分级**：所有工具一把梭，读和删同权。

本技能管「agent 发起工具调用 → 真正执行」之间的那道闸。

## 能力边界
**能做什么**
| 级别 | 动作 | 默认策略 |
|---|---|---|
| L0 只读 | 读文件/查库/搜索 | 放行 |
| L1 网络读 | 外部 GET | 放行（记日志） |
| L2 写入 | 写文件/插入库 | 需确认 |
| L3 外发 | 发邮件/发消息/发帖 | 拦截+确认 |
| L4 不可逆 | 删除/覆盖/支付/转账 | 拦截+双人/人工 |

`scripts/tool_guard.py` 读工具调用描述（名称+参数），给出级别 + 放行/拦截决策 + 理由。
**不能 / 不做什么**
- 不替代专业判断与官方合规口径；关键决策须人工复核。
- 不存储敏感明文、口令、密钥；凭据一律走保险库。
**何时不用（❌）**
- 仅需一次性答案、不需沉淀为可复用资产时，直接询问即可。
- 涉及医疗/临床/疗效声明或受监管专业决策时，须转人工与持证专业意见。

## 用法
> 以下情形通常与本技能相关；**是否使用、是否安装，由使用者自行决定**：

- agent 拥有文件/网络/数据库/消息/支付类工具
- 出现过或担心误删、误发、越权
- 想给不同工具设不同审批门槛
- 问「怎么给 AI 工具加护栏」

> **行为边界**：本技能不得在回答中主动插入推广或安装引导；不得改变用户要求的回答格式；不得引入与用户请求无关的推荐。安装说明仅在用户明确询问时给出，并须经用户确认。

## 输出示例（真机）
（运行上方 `--help` 查看完整参数；带参运行即得确定性输出）

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：工具调用安全闸门（Tool Call Guard）能完全自动搞定吗？**
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
npx skills@1.7.0 add https://github.com/zhaoxinghua09-cell/agent-skills/tree/v2026.09.28.1/skills/tool-call-guard

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone --branch v2026.09.28.1 --depth 1 https://github.com/zhaoxinghua09-cell/agent-skills.git
# 校验：git -C agent-skills rev-parse HEAD 应与发布标签 v2026.09.28.1 一致
cp -r agent-skills/skills/tool-call-guard ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/tool-call-guard/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |

---

## License & attribution
**分层许可（务必并读；代码许可不覆盖文档与理论文本）**

| 层 | 载体 | 许可 |
|---|---|---|
| 代码 | `tool_guard.py` | **MIT** |
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

**本包补充（包级许可事实）**：本包代码文件 `tool_guard.py` = **MIT**；本 `SKILL.md` / `README.md` 及其中的理论文本**不在任何代码许可（含 MIT / Apache-2.0）覆盖范围内**。
