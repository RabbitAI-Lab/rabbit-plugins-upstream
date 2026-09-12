---
name: api-resilience
slug: api-resilience
display_name: API 韧性（API Resilience）
displayName: API 韧性（API Resilience）
title: API 韧性（API Resilience）
version: 1.1.0
category: ai-agent
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
description: 当用户说『调外部API老超时』『被限流了』『接口抖一动就挂』『怎么给agent加重试退避』，或 agent 依赖的第三方服务(模型/搜索/数据库)不稳定、需要限流/退避/熔断/降级时使用。把外部调用当『会失败的对象』：指数退避+抖动重试、限流计数、熔断降级，失败可恢复不雪崩。理论根基：LGD 三律（有籍·有证·有门禁）。触发词：API重试、限流、退避、熔断、降级、接口抖动、resilience、超时、调用不稳定。
tags: [API韧性, 重试退避, 限流, 熔断, 降级, resilience, 可靠性, 故障恢复, agent优化]
display_name_en: API Resilience
summary: 当用户说『调外部API老超时』『被限流了』『接口抖一动就挂』『怎么给agent加重试退避』，或 agent 依赖的第三方服务(模型/搜索/数据库)不稳定、需要限流/退避/熔断/降级时使用。
agent_created: true
copyright: SynomosAI
read_when: 
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---









# API 韧性（API Resilience） / API 韧性（API Resilience）

**api-resilience** v1.1.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
- **硬失败**：一次 500/超时没兜住，整条 agent 链路崩；
- **限流雪崩**：429 后立刻重试，反而把对方打挂、自己也卡死；
- **无熔断**：依赖服务挂了还猛冲，耗尽资源；
- **无降级**：主路没了，没有备用路，直接报错。

本技能管「agent → 外部服务」这条最脆的链路。

## 能力边界
**能做什么**
- 按本技能定义的规程落地「API 韧性（API Resilience）」相关能力。
**不能 / 不做什么**
- 不替代专业判断与官方合规口径；关键决策须人工复核。
- 不存储敏感明文、口令、密钥；凭据一律走保险库。
**何时不用（❌）**
- 仅需一次性答案、不需沉淀为可复用资产时，直接询问即可。
- 涉及医疗/临床/疗效声明或受监管专业决策时，须转人工与持证专业意见。

## 用法
- **硬失败**：一次 500/超时没兜住，整条 agent 链路崩；
- **限流雪崩**：429 后立刻重试，反而把对方打挂、自己也卡死；
- **无熔断**：依赖服务挂了还猛冲，耗尽资源；
- **无降级**：主路没了，没有备用路，直接报错。

本技能管「agent → 外部服务」这条最脆的链路。

## 输出示例（真机）
（运行上方 `--help` 查看完整参数；带参运行即得确定性输出）

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：API 韧性（API Resilience）能完全自动搞定吗？**
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
npx skills add zhaoxinghua09-cell/agent-skills -g

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone https://github.com/zhaoxinghua09-cell/agent-skills.git
cp -r agent-skills/skills/api-resilience ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/api-resilience/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |
