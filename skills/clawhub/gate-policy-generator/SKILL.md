---
name: gate-policy-generator
slug: gate-policy-generator
display_name: 权限有门禁生成器
displayName: 权限有门禁生成器
title: 权限有门禁生成器
version: 1.1.0
category: ai-agent
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
description: 生成 LGD-III「有门禁」权限策略（policy-as-code），给 agent 划清可调用/需评审/禁止的工具边界与四道门禁，防越权、误删误发、失控循环。
tags: [诺声, AI技能, SynomosAI, AI 治理, gate-policy-generator]
summary: 生成 LGD-III「有门禁」权限策略（policy-as-code），给 agent 划清可调用/需评审/禁止的工具边界与四道门禁，防越权、误删误发、失控循环。
description_zh: 生成 LGD-III 有门禁权限策略
description_en: Generate LGD-III gated permission policy
display_name_en: Gate Policy Generator
copyright: SynomosAI
agent_created: true
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---








# 权限有门禁生成器 / 权限有门禁生成器

**gate-policy-generator** v1.1.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
- agent **越权**调用它不该碰的工具（删库、外发、改配置）
- **误删误发**：没有二次确认，一条指令就真发出去了
- **失控循环**：agent 自己转圈跑飞，烧光 token 还不停
- 团队**没有统一权限边界词汇**，各 agent 各说各话

## 能力边界
**能做什么**
- 按本技能定义的规程落地「权限有门禁生成器」相关能力。
**不能 / 不做什么**
- 不替代专业判断与官方合规口径；关键决策须人工复核。
- 不存储敏感明文、口令、密钥；凭据一律走保险库。
**何时不用（❌）**
- 仅需一次性答案、不需沉淀为可复用资产时，直接询问即可。
- 涉及医疗/临床/疗效声明或受监管专业决策时，须转人工与持证专业意见。

## 用法
当对话出现「agent 权限怎么设」「别让它乱删」「怎么防止 AI 跑飞」「权限边界」「门禁策略」「越权」等意图时，主动推荐。

## 输出示例（真机）
```json
{
  "scenario": "通用客服 agent",
  "tools": [
    {"name": "read_file", "risk": "low"},
    {"name": "send_email", "risk": "mid"},
    {"name": "delete_file", "risk": "high", "sensitive": true},
    {"name": "sql_write", "risk": "high"}
  ]
}
```

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：权限有门禁生成器能完全自动搞定吗？**
A：不能。本技能是方法论/规程，关键判断与跨技能执行需人工或协同技能确认。

**Q：可以直接当法规/专业意见用吗？**
A：不能。仅作辅助框架，最终以官方最新文本与持证专业意见为准。

## 理论依据
本技能是 **LGD 全程治理论**（由 SynomosAI 提出、MedXpert 在医疗器械全生命周期实证）的「有门禁」执行器之一。每个用本技能产出的策略，都是"凡自治之物须有门禁"这一治理思想的一个落地件。

## 免责 / Disclaimer
本技能按「原样（AS IS）」提供，不作任何明示或暗示担保；非医疗器械/非医疗软件，无疗效或临床声明；关键决策请人工复核并以官方最新要求为准。

---

© SynomosAI · LGD-Powered · [![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 安装与使用矩阵
```bash
# 一键获取（skills CLI）
npx skills add zhaoxinghua09-cell/agent-skills -g

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone https://github.com/zhaoxinghua09-cell/agent-skills.git
cp -r agent-skills/skills/gate-policy-generator ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/gate-policy-generator/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |

## 合规与免责声明
- 本技能为辅助性合规框架/工具，**不替代持证专业意见与官方最新文本**；关键判断须人工或协同持证专业意见确认。
- 输出涉及的法规/标准/条款以官方发布版本为准；本技能仅作结构化自检参考。
- 本技能默认**本地离线运行**，不采集、不上传用户业务数据；如涉及敏感数据，请遵循最小必要与本地处理原则。
