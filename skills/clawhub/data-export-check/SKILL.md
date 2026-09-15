---
name: data-export-check
slug: data-export-check
display_name: 数据出境合规自检
displayName: 数据出境合规自检
title: 数据出境合规自检
version: 1.1.0
category: ai-agent
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
description: 数据出境合规自检 — 数据出境前五项义务自检（分级/单独同意/PIA/标准合同或安全评估/留痕），缺项即 FAIL（零依赖）
tags: [诺声, AI技能, SynomosAI, AI 治理, data-export-check]
summary: 数据出境合规自检 — 数据出境前五项义务自检（分级/单独同意/PIA/标准合同或安全评估/留痕），缺项即 FAIL（零依赖）
display_name_en: Data Export Check
agent_created: true
copyright: SynomosAI
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---









# 数据出境合规自检 / 数据出境合规自检

**data-export-check** v1.1.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
用境外SaaS/云就等于数据出境，义务没走完就是监管风险

## 能力边界
**能做什么**
- 按本技能定义的规程落地「数据出境合规自检」相关能力。
**不能 / 不做什么**
- 不替代专业判断与官方合规口径；关键决策须人工复核。
- 不存储敏感明文、口令、密钥；凭据一律走保险库。
**何时不用（❌）**
- 仅需一次性答案、不需沉淀为可复用资产时，直接询问即可。
- 涉及医疗/临床/疗效声明或受监管专业决策时，须转人工与持证专业意见。

## 用法
```bash
python scripts/data_export_check.py --help
```
- 合规 PASS → rc=0；违规 FAIL → rc=1；用法错误 → rc=2
- 支持 --json 机器可读输出

## 输出示例（真机）
（运行上方 `--help` 查看完整参数；带参运行即得确定性输出）

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：数据出境合规自检能完全自动搞定吗？**
A：不能。本技能是方法论/规程，关键判断与跨技能执行需人工或协同技能确认。

**Q：可以直接当法规/专业意见用吗？**
A：不能。仅作辅助框架，最终以官方最新文本与持证专业意见为准。

## 理论依据
本技能是「LGD 三律」在 数据合规/政务 场景的落地件：让 AI 的每一次输出**有籍可查、有证可依、有门禁可控**。

## 免责 / Disclaimer
本工具为合规初筛辅助，不构成法律/投资/医疗意见；重要决策请咨询持牌专业人士。

---

© SynomosAI · LGD-Powered · [![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 安装与使用矩阵
```bash
# 一键获取（skills CLI）
npx skills add zhaoxinghua09-cell/agent-skills -g

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone https://github.com/zhaoxinghua09-cell/agent-skills.git
cp -r agent-skills/skills/data-export-check ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/data-export-check/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |

## 数据处理与权限声明
- 本技能在**本地运行**，默认不向任何第三方传输数据；凭据一律经本地保险库调用，不落明文。
- 处理的数据遵循**最小必要**原则，不留存非必要个人信息。
- 涉及文件/网络/凭据/浏览器等敏感权限时，仅在用户显式授权范围内操作，并保留可审计的操作记录。
