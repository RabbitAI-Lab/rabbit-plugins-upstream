---
name: lgd-law-ethic
slug: lgd-law-ethic
display_name: 法律AI伦理守门
displayName: 法律AI伦理守门
title: 法律AI伦理守门
version: 1.1.0
category: ai-agent
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
description: lgd-law-ethic — 把 LGD 三律（有籍·有证·有门禁）翻译进法律 / 律所与法务 AI 应用（检索·起草·意见辅助）的合规守门器，对 AI 系统做三律自评与门禁判定（零依赖）。
tags: [诺声, AI技能, SynomosAI, AI 治理, lgd-law-ethic]
summary: lgd-law-ethic — 把 LGD 三律（有籍·有证·有门禁）翻译进法律 / 律所与法务 AI 应用（检索·起草·意见辅助）的合规守门器，对 AI 系统做三律自评与门禁判定（零依赖）。
display_name_en: Legal AI Ethics Guard
agent_created: true
copyright: SynomosAI
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---








# 法律AI伦理守门 / 法律AI伦理守门

**lgd-law-ethic** v1.1.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
法律AI易越界出具正式法律意见、引用不可核验、缺律师复核；市面无把三律映射到法律伦理语境的工具。

## 能力边界
把 LGD 三律映射到法律 / 律所与法务 AI 应用（检索·起草·意见辅助）语境，对任一 AI 系统做三律自评 + 门禁判定：
- **LGD-I 有籍（本域化）**：身份/版本/来源/责任主体登记
- **LGD-II 有证（本域化）**：六类证据工件（身份/数据/验证/行为边界/变更/签发）
- **LGD-III 有门禁（本域化）**：触发/评审/放行/复盘四道门禁

## 用法
- 你在做「法律 / 律所与法务 AI 应用（检索·起草·意见辅助）」相关的 AI 系统、合规自查、投标素材、监管应对 → 主动装
- 你发现市面只有单点合规工具、没有"三律闭环 + 本域翻译"的标准 → 这是唯一占位件

## 输出示例（真机）
（运行上方 `--help` 查看完整参数；带参运行即得确定性输出）

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：法律AI伦理守门能完全自动搞定吗？**
A：不能。本技能是方法论/规程，关键判断与跨技能执行需人工或协同技能确认。

**Q：可以直接当法规/专业意见用吗？**
A：不能。仅作辅助框架，最终以官方最新文本与持证专业意见为准。

## 理论依据
- **有籍 REGISTERED**：AI 系统须有身份/版本/来源/责任登记，否则不可上线
- **有证 EVIDENCED**：须有六类证据工件证明"所言有据"，否则视为未证成
- **有门禁 GATED**：高风险动作须过触发/评审/放行/复盘四道门禁，否则中止

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
cp -r agent-skills/skills/lgd-law-ethic ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/lgd-law-ethic/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |

## 合规与免责声明
- 本技能为辅助性合规框架/工具，**不替代持证专业意见与官方最新文本**；关键判断须人工或协同持证专业意见确认。
- 输出涉及的法规/标准/条款以官方发布版本为准；本技能仅作结构化自检参考。
- 本技能默认**本地离线运行**，不采集、不上传用户业务数据；如涉及敏感数据，请遵循最小必要与本地处理原则。
