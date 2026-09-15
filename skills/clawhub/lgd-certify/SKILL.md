---
name: lgd-certify
slug: lgd-certify
display_name: LGD 三律闭环认证（有籍→有证→有门禁）
displayName: LGD 三律闭环认证（有籍→有证→有门禁）
title: LGD 三律闭环认证（有籍→有证→有门禁）
version: 1.1.0
category: ai-agent
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
description: 当用户要『给 AI 产物发可信护照 / 做三律合规认证 / 生成可挂载徽章』时用。这是市场唯一把『有籍护照签发 → 有证证据链 → 有门禁签发 → 可挂载徽章』做成闭环的 CLI：register 签发算法护照(三锚一票同源+SHA-256指纹)、evidence 扫六类证据工件链式哈希、gate 三律评审 PASS/FAIL 并签发认证 + medxpert.cn 徽章嵌入码。LGD 三律旗舰执行器，对标调研证实治理生态全是单点工具、无此闭环。触发词：LGD 认证、三律闭环、算法护照、可信徽章、有籍有证有门禁认证、护照签发。
tags: [LGD, 三律闭环, 算法护照, 认证, 徽章, 有籍, 有证, 有门禁, 闭环]
display_name_en: LGD Three-Laws Closed-Loop Certifier
summary: 当用户要『给 AI 产物发可信护照 / 做三律合规认证 / 生成可挂载徽章』时用。
agent_created: true
copyright: SynomosAI
read_when: 
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---








# LGD 三律闭环认证（有籍→有证→有门禁） / LGD 三律闭环认证（有籍→有证→有门禁）

**lgd-certify** v1.1.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
当用户要『给 AI 产物发可信护照 / 做三律合规认证 / 生成可挂载徽章』时用。这是市场唯一把『有籍护照签发 → 有证证据链 → 有门禁签发 → 可挂载徽章』做成闭环的 CLI：register 签发算法护照(三锚一票同源+SHA-256指纹)、evidence 扫六类证据工件链式哈希、gate 三律评审 PASS/FAIL 并签发认证 + medxpert.cn 徽章嵌入码。LGD 三律旗舰执行器，对标调研证实治理生态全是单点工具、无此闭环。触发词：LGD 认证、三律闭环、算法护照、可信徽章、有籍有证有门禁认证、护照签发。

## 能力边界
- 认证结论基于你放入的证据工件，**不替代**监管/法律合规审查。
- 门禁未过（证据未齐）属正常，放齐六类后重跑 `evidence → gate` 即可。
- 不编造：缺工件即标缺失，绝不伪造通过。

## 用法
| 命令 | 律 | 作用 |
|---|---|---|
| `register` | 有籍 REGISTERED | 凡造必登：生成算法护照（schema v1.0 三锚一票同源）+ SHA-256 指纹 |
| `evidence` | 有证 EVIDENCED | 凡所行必有证据：扫描六类证据工件 → 链式哈希证据链（防篡改） |
| `gate` | 有门禁 GATED | 凡演化必经门禁：三律评审 → PASS/FAIL → 签发认证 + 官方徽章嵌入码 |

## 输出示例（真机）
（运行上方 `--help` 查看完整参数；带参运行即得确定性输出）

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：LGD 三律闭环认证（有籍→有证→有门禁）能完全自动搞定吗？**
A：不能。本技能是方法论/规程，关键判断与跨技能执行需人工或协同技能确认。

**Q：可以直接当法规/专业意见用吗？**
A：不能。仅作辅助框架，最终以官方最新文本与持证专业意见为准。

## 理论依据
| 命令 | 律 | 作用 |
|---|---|---|
| `register` | 有籍 REGISTERED | 凡造必登：生成算法护照（schema v1.0 三锚一票同源）+ SHA-256 指纹 |
| `evidence` | 有证 EVIDENCED | 凡所行必有证据：扫描六类证据工件 → 链式哈希证据链（防篡改） |
| `gate` | 有门禁 GATED | 凡演化必经门禁：三律评审 → PASS/FAIL → 签发认证 + 官方徽章嵌入码 |

## 免责 / Disclaimer
- 认证结论基于你放入的证据工件，**不替代**监管/法律合规审查。
- 门禁未过（证据未齐）属正常，放齐六类后重跑 `evidence → gate` 即可。
- 不编造：缺工件即标缺失，绝不伪造通过。

---

© SynomosAI · LGD-Powered · [![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 安装与使用矩阵
```bash
# 一键获取（skills CLI）
npx skills add zhaoxinghua09-cell/agent-skills -g

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone https://github.com/zhaoxinghua09-cell/agent-skills.git
cp -r agent-skills/skills/lgd-certify ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/lgd-certify/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |
