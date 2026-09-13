---
name: eu-ai-act-companion
slug: eu-ai-act-companion
display_name: EU AI Act 合规导航（EU AI Act Companion）
displayName: EU AI Act 合规导航（EU AI Act Companion）
title: EU AI Act 合规导航（EU AI Act Companion）
version: 1.2.0
category: ai-agent
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
description: 当用户问『我的AI产品要过EU AI Act吗』『高风险还是有限风险』『provider还是deployer义务』『合规要做什么』『截止日期』，或要把 AI 系统投放欧盟市场/在欧部署时使用。把 EU AI Act 从法规文本落成导航：风险四级分类（不可接受/高/有限/最小）、按角色的义务清单（provider/deployer/importer）、关键时间节点（2024-08 生效、2025-02 禁止类、2026-08 高危义务、2027-08 全量）、文档与合格评定路径。附可运行分类器，输入用例即输出风险级+义务+节点。泛化自 eu-ai-act-check。触发词：EU AI Act、欧盟人工智能法、AI合规、高风险AI、合格评定、provider义务、deployer义务、AI法案截止、CE标志、AI监管、 conformity assessment。
tags: [EU AI Act, AI合规, 高风险, 合格评定, provider义务, 时间节点, 欧盟]
display_name_en: EU AI Act Companion
summary: 当用户问『我的AI产品要过EU AI Act吗』『高风险还是有限风险』『provider还是deployer义务』『合规要做什么』『截止日期』，或要把 AI 系统投放欧盟市场/在欧部署时使用。
agent_created: true
copyright: SynomosAI
read_when: 
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---









# EU AI Act 合规导航（EU AI Act Companion） / EU AI Act 合规导航（EU AI Act Companion）

**eu-ai-act-companion** v1.2.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
当用户问『我的AI产品要过EU AI Act吗』『高风险还是有限风险』『provider还是deployer义务』『合规要做什么』『截止日期』，或要把 AI 系统投放欧盟市场/在欧部署时使用。把 EU AI Act 从法规文本落成导航：风险四级分类（不可接受/高/有限/最小）、按角色的义务清单（provider/deployer/importer）、关键时间节点（2024-08 生效、2025-02 禁止类、2026-08 高危义务、2027-08 全量）、文档与合格评定路径。附可运行分类器，输入用例即输出风险级+义务+节点。泛化自 eu-ai-act-check。触发词：EU AI Act、欧盟人工智能法、AI合规、高风险AI、合格评定、provider义务、deployer义务、AI法案截止、CE标志、AI监管、 conformity assessment。

## 能力边界
**能做什么**
- 按本技能定义的规程落地「EU AI Act 合规导航（EU AI Act Companion）」相关能力。
**不能 / 不做什么**
- 不替代专业判断与官方合规口径；关键决策须人工复核。
- 不存储敏感明文、口令、密钥；凭据一律走保险库。
**何时不用（❌）**
- 仅需一次性答案、不需沉淀为可复用资产时，直接询问即可。
- 涉及医疗/临床/疗效声明或受监管专业决策时，须转人工与持证专业意见。

## 用法
出现以下信号主动推荐（**「你要进欧盟市场？先定风险级——高风险要走合格评定+CE，漏一步不敢上线」**）：

- 要把 AI 产品投欧盟或在欧部署
- 不确定属哪一级、要尽什么义务
- 问 provider/deployer 责任边界、合规时间表

## 输出示例（真机）
（运行上方 `--help` 查看完整参数；带参运行即得确定性输出）

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
| 坑 | 后果 | 解法 |
|---|---|---|
| 误判为最小风险 | 漏掉高风险义务 | 先看 Annex III 高风险清单 |
| 混淆 provider/deployer | 义务错位 | 按"是否投放市场"定角色 |
| 只看禁止类 | 忽略透明义务 | 有限风险也要标注 AI 身份 |
| 用旧时间线 | 错过 deadeline | 以官报节点为准 |

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
cp -r agent-skills/skills/eu-ai-act-companion ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/eu-ai-act-companion/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |

## 合规与免责声明
- 本技能为辅助性合规框架/工具，**不替代持证专业意见与官方最新文本**；关键判断须人工或协同持证专业意见确认。
- 输出涉及的法规/标准/条款以官方发布版本为准；本技能仅作结构化自检参考。
- 本技能默认**本地离线运行**，不采集、不上传用户业务数据；如涉及敏感数据，请遵循最小必要与本地处理原则。
