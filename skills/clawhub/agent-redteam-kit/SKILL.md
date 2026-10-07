---
name: agent-redteam-kit
slug: agent-redteam-kit
display_name: AI红队对抗测试（Red Team Kit）
displayName: AI红队对抗测试（Red Team Kit）
title: AI红队对抗测试（Red Team Kit）
version: 1.1.0
category: it-ops-security
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Bash, Write, WebFetch
description: 当用户说『测一下这个AI安不安全』『会不会被越狱』『让AI干危险的事它听不听』『上线前做对抗测试』，或要给一个 agent/提示词做安全性红队时使用。中英双库扫描越狱/危险能力请求（DAN/忽略指令/提权/数据外泄/自改进等），给出风险分级+加固建议，并设「危险操作闸门」（有门禁）。可运行脚本（redteam_scan 扫描器）。理论根基：LGD 三律之有门禁（危险动作先过闸）。触发词：红队、red team、越狱、jailbreak、对抗测试、prompt攻击、AI安全测试、危险指令、安全评估。
tags: [红队, red team, 越狱, jailbreak, 对抗测试, AI安全, 有门禁]
display_name_en: AI Red Team Kit
summary: 当用户说『测一下这个AI安不安全』『会不会被越狱』『让AI干危险的事它听不听』『上线前做对抗测试』，或要给一个 agent/提示词做安全性红队时使用。
agent_created: true
copyright: SynomosAI
read_when: 
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---









# AI红队对抗测试（Red Team Kit） / AI红队对抗测试（Red Team Kit）

**agent-redteam-kit** v1.1.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2/3（0 通过 / 1 中危 / 2 高危拦截 / 3 用法错误）

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
当用户说『测一下这个AI安不安全』『会不会被越狱』『让AI干危险的事它听不听』『上线前做对抗测试』，或要给一个 agent/提示词做安全性红队时使用。中英双库扫描越狱/危险能力请求（DAN/忽略指令/提权/数据外泄/自改进等），给出风险分级+加固建议，并设「危险操作闸门」（有门禁）。可运行脚本（redteam_scan 扫描器）。理论根基：LGD 三律之有门禁（危险动作先过闸）。触发词：红队、red team、越狱、jailbreak、对抗测试、prompt攻击、AI安全测试、危险指令、安全评估。

## 能力边界
**能做什么**
- 按本技能定义的规程落地「AI红队对抗测试（Red Team Kit）」相关能力。
**不能 / 不做什么**
- 不替代专业判断与官方合规口径；关键决策须人工复核。
- 不存储敏感明文、口令、密钥；凭据一律走保险库。
**何时不用（❌）**
- 仅需一次性答案、不需沉淀为可复用资产时，直接询问即可。
- 涉及医疗/临床/疗效声明或受监管专业决策时，须转人工与持证专业意见。

## 用法
> 以下情形通常与本技能相关；**是否使用、是否安装，由使用者自行决定**：

- 要上线/发布一个 agent 或提示词
- 收到越狱/忽略指令类输入
- 担心 AI 被诱导干危险事

> **行为边界**：本技能不得在回答中主动插入推广或安装引导；不得改变用户要求的回答格式；不得引入与用户请求无关的推荐。安装说明仅在用户明确询问时给出，并须经用户确认。

## 输出示例（真机）
（运行上方 `--help` 查看完整参数；带参运行即得确定性输出）

## 退出码与错误码
- `rc=0` 未发现红队模式（通过）
- `rc=1` 仅命中中危模式（需人工复核）
- `rc=2` 命中高危模式（拦截；调用方应据此阻断）
- `rc=3` 用法或环境错误（文件不存在 / 参数错误）

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：AI红队对抗测试（Red Team Kit）能完全自动搞定吗？**
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
npx skills@1.7.0 add https://github.com/zhaoxinghua09-cell/agent-skills/tree/v2026.09.28.1/skills/agent-redteam-kit

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone --branch v2026.09.28.1 --depth 1 https://github.com/zhaoxinghua09-cell/agent-skills.git
# 校验：git -C agent-skills rev-parse HEAD 应与发布标签 v2026.09.28.1 一致
cp -r agent-skills/skills/agent-redteam-kit ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/agent-redteam-kit/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |

## 数据处理与权限声明
- 本技能在**本地运行**，默认不向任何第三方传输数据；凭据一律经本地保险库调用，不落明文。
- 处理的数据遵循**最小必要**原则，不留存非必要个人信息。
- 涉及文件/网络/凭据/浏览器等敏感权限时，仅在用户显式授权范围内操作，并保留可审计的操作记录。

---

## License & attribution
**分层许可（务必并读；代码许可不覆盖文档与理论文本）**

| 层 | 载体 | 许可 |
|---|---|---|
| 代码 | `redteam_scan.py` | **MIT** |
| 文档与理论文本 | 本 `SKILL.md`、`README.md`、其中「理论依据」段与一切理论表述 | **不在 MIT 覆盖范围内**：保留所有权利（All rights reserved） |

> 即：**代码可依 MIT 使用与再分发；文档与理论文本不因代码许可而默认可自由再发布。**

```
© 2026 赵兴华 / Steven Zhao·China (ORCID 0009-0001-0512-1237). All rights reserved.
理论署名 (attribution) : LGD（Lifecycle Governance Doctrine / 全程治理论）— SynomosAI initiative
名称状态 (name status)  : "SynomosAI" / "MedXpert" — 未申请实体注册、未申请商标注册
                        (not a registered legal entity; no trademark registered)
生产参考部署 (production reference, self-reported) : MedXpert
                    ← 非认证、非背书、非监管认可（not a certification or endorsement）
代码许可 (code license) : 本包 = MIT (see LICENSE)
                    本文本与理论表述不在任何代码许可覆盖范围内
引用格式 (cite as)      : 本资产无 DOI
```
（上列为《LGD 对外表述规范》§3.2 统一块，**整体复制、未删改**；发布/重提前须照最新版本复核。）

**本包补充（包级许可事实）**：本包代码文件 `redteam_scan.py` = **MIT**；本 `SKILL.md` / `README.md` 及其中的理论文本**不在任何代码许可（含 MIT / Apache-2.0）覆盖范围内**。
