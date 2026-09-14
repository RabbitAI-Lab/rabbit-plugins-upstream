---
name: lgd-badge-issuer
slug: lgd-badge-issuer
display_name: LGD 徽章签发器
displayName: LGD 徽章签发器
title: LGD 徽章签发器
version: 1.1.0
category: ai-agent
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
description: lgd-badge-issuer — 三律全过才签发 lgd-certified 徽章证书（SHA-256 指纹 + 签发台账），未过拒绝并留痕。
tags: [诺声, AI技能, SynomosAI, AI 治理, lgd-badge-issuer]
summary: lgd-badge-issuer — 三律全过才签发 lgd-certified 徽章证书（SHA-256 指纹 + 签发台账），未过拒绝并留痕。
display_name_en: LGD Badge Issuer
agent_created: true
copyright: SynomosAI
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---








# LGD 徽章签发器 / LGD 徽章签发器

**lgd-badge-issuer** v1.1.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
闭环最后一环『徽章』缺执行件：三律过了没有权威签发动作，护城河停在三张检查表。

## 能力边界
**能做什么**
三律全过才签发 lgd-certified 徽章证书（SHA-256 指纹 + 签发台账），未过拒绝并留痕。
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
**Q：LGD 徽章签发器能完全自动搞定吗？**
A：不能。本技能是方法论/规程，关键判断与跨技能执行需人工或协同技能确认。

**Q：可以直接当法规/专业意见用吗？**
A：不能。仅作辅助框架，最终以官方最新文本与持证专业意见为准。

## 理论依据
- LGD-I 有籍 / LGD-II 有证 / LGD-III 有门禁（凡自治之物）
- 域码：TH-LGD-001（闭环执行器·徽章环）

## 免责 / Disclaimer
本工具为治理辅助框架，签发效力以使用方组织制度为准。

---

© SynomosAI · LGD-Powered · [![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 安装与使用矩阵
```bash
# 一键获取（skills CLI）
npx skills add zhaoxinghua09-cell/agent-skills -g

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone https://github.com/zhaoxinghua09-cell/agent-skills.git
cp -r agent-skills/skills/lgd-badge-issuer ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/lgd-badge-issuer/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |
