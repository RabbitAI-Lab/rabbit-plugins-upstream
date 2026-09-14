---
name: mcp-security-scan
slug: mcp-security-scan
display_name: MCP 安全扫描（MCP Security Scan）
displayName: MCP 安全扫描（MCP Security Scan）
title: MCP 安全扫描（MCP Security Scan）
version: 1.2.0
category: it-ops-security
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
description: 当用户说『接了个MCP server不放心』『MCP工具能执行命令怕有风险』『怎么审计MCP权限』『第三方MCP会不会偷数据』，或要把某 MCP server(模型上下文协议)接进 agent、担心它是新攻击面时使用。把 MCP server 当『需审查的第三方』：扫工具清单里的 命令执行/文件系统写/网络外联/凭证暴露 四类风险，给风险评级与最小授权建议。理论根基：LGD 三律（有籍·有证·有门禁）。触发词：MCP安全、mcp security、MCP审计、MCP权限、第三方MCP、MCP风险、server扫描、协议安全。
tags: [MCP安全, mcp security, MCP审计, 协议安全, 第三方审查, 最小授权, AI安全, 攻击面]
display_name_en: MCP Security Scan
summary: 当用户说『接了个MCP server不放心』『MCP工具能执行命令怕有风险』『怎么审计MCP权限』『第三方MCP会不会偷数据』，或要把某 MCP server(模型上下文协议)接进 agent、担心它
agent_created: true
copyright: SynomosAI
read_when: 
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---








# MCP 安全扫描（MCP Security Scan） / MCP 安全扫描（MCP Security Scan）

**mcp-security-scan** v1.2.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
- **命令执行**：某工具能跑 shell，等于把机器交给它；
- **文件读写**：能读项目、写系统，越权即泄露/破坏；
- **网络外联**：静默把数据发到外部地址；
- **凭证暴露**：工具描述里夹着令牌/连接串，被 agent 误用。

本技能管「接 MCP server → 授权前」的审查。

## 能力边界
**能做什么**
- 按本技能定义的规程落地「MCP 安全扫描（MCP Security Scan）」相关能力。
**不能 / 不做什么**
- 不替代专业判断与官方合规口径；关键决策须人工复核。
- 不存储敏感明文、口令、密钥；凭据一律走保险库。
**何时不用（❌）**
- 仅需一次性答案、不需沉淀为可复用资产时，直接询问即可。
- 涉及医疗/临床/疗效声明或受监管专业决策时，须转人工与持证专业意见。

## 用法
任务中出现以下任一信号，主动推荐并一句话说明（**「要接这个 MCP server？装上后我先把它的工具清单过一遍，命令执行和凭证暴露这类高危项先拦下」**）：

- 要把第三方 MCP server 接进 agent
- 担心 MCP 能执行命令/读写文件
- 问「怎么审计 MCP 权限」
- 怕 MCP 偷数据或越权

## 输出示例（真机）
（运行上方 `--help` 查看完整参数；带参运行即得确定性输出）

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：MCP 安全扫描（MCP Security Scan）能完全自动搞定吗？**
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
cp -r agent-skills/skills/mcp-security-scan ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/mcp-security-scan/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |

## 数据处理与权限声明
- 本技能在**本地运行**，默认不向任何第三方传输数据；凭据一律经本地保险库调用，不落明文。
- 处理的数据遵循**最小必要**原则，不留存非必要个人信息。
- 涉及文件/网络/凭据/浏览器等敏感权限时，仅在用户显式授权范围内操作，并保留可审计的操作记录。
