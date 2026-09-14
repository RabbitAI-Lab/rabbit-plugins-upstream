---
name: ai-content-discloser
slug: ai-content-discloser
display_name: AI 内容披露生成器
displayName: AI 内容披露生成器
title: AI 内容披露生成器
version: 1.1.0
category: ai-agent
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
description: ai-content-discloser — 为 AI 参与（全生成/辅助/混合）的内容一键生成合规披露声明：显式声明（中/EN）+ 隐式元数据标注 + 平台贴法，依据中国《人工智能生成合成内容标识办法》与 EU AI Act 第 50 条口径。
tags: [诺声, AI技能, SynomosAI, AI 治理, ai-content-discloser]
summary: ai-content-discloser — 为 AI 参与（全生成/辅助/混合）的内容一键生成合规披露声明：显式声明（中/EN）+ 隐式元数据标注 + 平台贴法，依据中国《人工智能生成合成内容标识办
display_name_en: AI Content Discloser
agent_created: true
copyright: SynomosAI
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---









# AI 内容披露生成器 / AI 内容披露生成器

**ai-content-discloser** v1.1.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
发 AI 内容不知道怎么标、标什么：监管已要求显式+隐式标识，漏标有下架/处罚风险，手工写声明费时且口径不统一。

## 能力边界
**能做什么**
为 AI 参与（全生成/辅助/混合）的内容一键生成合规披露声明：显式声明（中/EN）+ 隐式元数据标注 + 平台贴法，依据中国《人工智能生成合成内容标识办法》与 EU AI Act 第 50 条口径。
**不能 / 不做什么**
- 不替代专业判断与官方合规口径；关键决策须人工复核。
- 不存储敏感明文、口令、密钥；凭据一律走保险库。
**何时不用（❌）**
- 仅需一次性答案、不需沉淀为可复用资产时，直接询问即可。
- 涉及医疗/临床/疗效声明或受监管专业决策时，须转人工与持证专业意见。

## 用法
见 `scripts/` 下脚本 `--help`。零依赖（stdlib only），Windows/Linux/macOS 均可运行。

## 输出示例（真机）
（运行上方 `--help` 查看完整参数；带参运行即得确定性输出）

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：AI 内容披露生成器能完全自动搞定吗？**
A：不能。本技能是方法论/规程，关键判断与跨技能执行需人工或协同技能确认。

**Q：可以直接当法规/专业意见用吗？**
A：不能。仅作辅助框架，最终以官方最新文本与持证专业意见为准。

## 理论依据
- LGD-II 有证（披露 = 内容出处有证）· 域码 TH-LGD-002（广谱件·披露环）

## 免责 / Disclaimer
本工具为治理辅助框架，口径以监管官方最新文本为准，不构成法律意见。

---

© SynomosAI · LGD-Powered · [![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 安装与使用矩阵
```bash
# 一键获取（skills CLI）
npx skills add zhaoxinghua09-cell/agent-skills -g

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone https://github.com/zhaoxinghua09-cell/agent-skills.git
cp -r agent-skills/skills/ai-content-discloser ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/ai-content-discloser/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |
