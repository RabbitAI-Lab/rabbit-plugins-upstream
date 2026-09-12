---
name: gov-disclosure-check
slug: gov-disclosure-check
display_name: 政务公开披露校验
displayName: 政务公开披露校验
title: 政务公开披露校验
version: 1.1.0
category: ai-agent
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
description: gov-disclosure-check — LGD 三律在政务 / 信息公开披露域的纵深合规工具（零依赖）：强制披露字段校验（决策依据/责任部门/时限/救济渠道/数据来源），对 AI 系统/数据做可执行合规校验。
tags: [诺声, AI技能, SynomosAI, AI 治理, gov-disclosure-check]
summary: gov-disclosure-check — LGD 三律在政务 / 信息公开披露域的纵深合规工具（零依赖）：强制披露字段校验（决策依据/责任部门/时限/救济渠道/数据来源），对 AI 系统/数据做可
display_name_en: Gov Disclosure Check
agent_created: true
copyright: SynomosAI
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---








# 政务公开披露校验 / 政务公开披露校验

**gov-disclosure-check** v1.1.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
公开信息缺强制披露字段难以自动核验，存在信息披露不完整风险。

## 能力边界
把 LGD 三律的"有证 / 有门禁"落地为可执行的政务 / 信息公开披露合规动作——强制披露字段校验（决策依据/责任部门/时限/救济渠道/数据来源）：
- 零依赖 CLI，输入即校验，输出结构化结果 + 合规判定（退出码 0/1）
- 把抽象合规要求转成机器可跑的规则，降低人工错漏

## 用法
- 你在做「政务 / 信息公开披露」相关的 AI 系统、合规自查、投标素材、监管应对 → 主动装
- 你需要把三律占位件升级为"能跑"的纵深能力 → 这是标准定义权的落地件

## 输出示例（真机）
（运行上方 `--help` 查看完整参数；带参运行即得确定性输出）

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：政务公开披露校验能完全自动搞定吗？**
A：不能。本技能是方法论/规程，关键判断与跨技能执行需人工或协同技能确认。

**Q：可以直接当法规/专业意见用吗？**
A：不能。仅作辅助框架，最终以官方最新文本与持证专业意见为准。

## 理论依据
- **有籍 REGISTERED**：AI 系统须有身份/版本/来源/责任登记，否则不可上线
- **有证 EVIDENCED**：须有证据工件证明"所言有据"，否则视为未证成
- **有门禁 GATED**：高风险动作须过门禁，否则中止

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
cp -r agent-skills/skills/gov-disclosure-check ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/gov-disclosure-check/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |

## 合规与免责声明
- 本技能为辅助性合规框架/工具，**不替代持证专业意见与官方最新文本**；关键判断须人工或协同持证专业意见确认。
- 输出涉及的法规/标准/条款以官方发布版本为准；本技能仅作结构化自检参考。
- 本技能默认**本地离线运行**，不采集、不上传用户业务数据；如涉及敏感数据，请遵循最小必要与本地处理原则。
