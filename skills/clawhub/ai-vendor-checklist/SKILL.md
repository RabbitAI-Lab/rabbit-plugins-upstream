---
name: ai-vendor-checklist
slug: ai-vendor-checklist
display_name: AI供应商尽调清单
displayName: AI供应商尽调清单
title: AI供应商尽调清单
version: 1.1.0
category: ai-agent
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
description: ai-vendor-checklist — 10 项 AI 采购尽调清单（数据权属/训练退出/留存/资质/事故通报/子处理者/出境/模型卡/审计/迁移退出）；--template 出清单，--score 打分低于线 rc=1。
tags: [诺声, AI技能, SynomosAI, AI 治理, ai-vendor-checklist]
summary: ai-vendor-checklist — 10 项 AI 采购尽调清单（数据权属/训练退出/留存/资质/事故通报/子处理者/出境/模型卡/审计/迁移退出）；
display_name_en: AI Vendor Checklist
agent_created: true
copyright: SynomosAI
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---









# AI供应商尽调清单 / AI供应商尽调清单

**ai-vendor-checklist** v1.1.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
采购 AI 服务时凭 PPT 拍板：数据拿去训练了吗？出了事谁通报？想退出数据能带走吗——签约后才问就晚了。

## 能力边界
**能做什么**
10 项 AI 采购尽调清单（数据权属/训练退出/留存/资质/事故通报/子处理者/出境/模型卡/审计/迁移退出）；--template 出清单，--score 打分低于线 rc=1。
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
**Q：AI供应商尽调清单能完全自动搞定吗？**
A：不能。本技能是方法论/规程，关键判断与跨技能执行需人工或协同技能确认。

**Q：可以直接当法规/专业意见用吗？**
A：不能。仅作辅助框架，最终以官方最新文本与持证专业意见为准。

## 理论依据
- LGD-I 有籍（供应商资质有据） · 域码 TH-LGD-012

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
cp -r agent-skills/skills/ai-vendor-checklist ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/ai-vendor-checklist/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |
