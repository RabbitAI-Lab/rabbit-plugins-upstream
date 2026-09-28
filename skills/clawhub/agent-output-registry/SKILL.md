---
name: agent-output-registry
slug: agent-output-registry
display_name: AI 产出有籍登记器（LGD-I 有籍）
displayName: AI 产出有籍登记器（LGD-I 有籍）
title: AI 产出有籍登记器（LGD-I 有籍）
version: 1.1.0
category: ai-agent
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Bash, Write, WebFetch
description: 当用户要『给 AI 产出溯源 / IP 归属 / 防篡改 / 审计留痕』，或担心『AI 生成内容说不清来源、被改了认不出、权属扯不清』时用。给每条 AI 产出发一张『籍』(户口)：SHA-256 指纹 + 模型/版本/提示哈希 + 时间戳 + 权属，写入本地台账；支持 verify 证完整性、lookup 查归属、report 列全部。这是 LGD-I 有籍的落地执行器——把抽象的『有籍』变成每条产出可查的户口。触发词：AI 产出溯源、AI 内容登记、IP 归属、产出指纹、防篡改、审计留痕、有籍、产出户口。
tags: [LGD, 有籍, 溯源, IP归属, 防篡改, 审计留痕, AI产出, 户口, 指纹]
display_name_en: Agent Output Registry (LGD-I Registered)
summary: 当用户要『给 AI 产出溯源 / IP 归属 / 防篡改 / 审计留痕』，或担心『AI 生成内容说不清来源、被改了认不出、权属扯不清』时用。
agent_created: true
copyright: SynomosAI
read_when: 
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---









# AI 产出有籍登记器（LGD-I 有籍） / AI 产出有籍登记器（LGD-I 有籍）

**agent-output-registry** v1.1.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
- AI 产出满天飞，却**说不清来源、找不到版本、改了认不出** → 登记后一切可查。
- IP 归属扯皮、审计无据 → 指纹 + 权属人 = 可举证的户口。
- 合规要求"凡造必登"但无工具 → 本技能即最小可行执行器。

## 能力边界
- 指纹只证"字节一致"，不证"内容正确"——正确性由 `evidence-chain-builder`（有证）补。
- 台账存本地，敏感产出勿登记含密钥/内部代号的原文。
- 不编造：缺字段明确标"未知/未声明"，不替你补。

## 用法
```bash
# 登记一条产出（--out 可传文件路径或文本）
python scripts/output_registry.py add --out 报告.txt --model qwen3.5 --version 9b --prompt "写一份合规总结" --issuer "MedXpert" --license MIT
# → 返回籍号 LGD-REG-xxxxxxxx

# 证完整性：重算哈希比对台账
python scripts/output_registry.py verify --id LGD-REG-xxxxxxxx --out 报告.txt

# 查归属 / 列全部
python scripts/output_registry.py lookup --id LGD-REG-xxxxxxxx
python scripts/output_registry.py report
```

## 输出示例（真机）
（运行上方 `--help` 查看完整参数；带参运行即得确定性输出）

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：AI 产出有籍登记器（LGD-I 有籍）能完全自动搞定吗？**
A：不能。本技能是方法论/规程，关键判断与跨技能执行需人工或协同技能确认。

**Q：可以直接当法规/专业意见用吗？**
A：不能。仅作辅助框架，最终以官方最新文本与持证专业意见为准。

## 免责 / Disclaimer
- 指纹只证"字节一致"，不证"内容正确"——正确性由 `evidence-chain-builder`（有证）补。
- 台账存本地，敏感产出勿登记含密钥/内部代号的原文。
- 不编造：缺字段明确标"未知/未声明"，不替你补。

---

© SynomosAI · LGD-Powered · [![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 安装与使用矩阵
```bash
# 一键获取（skills CLI）
npx skills@1.7.0 add https://github.com/zhaoxinghua09-cell/agent-skills/tree/v2026.09.28.1/skills/agent-output-registry

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone --branch v2026.09.28.1 --depth 1 https://github.com/zhaoxinghua09-cell/agent-skills.git
# 校验：git -C agent-skills rev-parse HEAD 应与发布标签 v2026.09.28.1 一致
cp -r agent-skills/skills/agent-output-registry ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/agent-output-registry/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |

---

## License & attribution
**分层许可（务必并读；代码许可不覆盖文档与理论文本）**

| 层 | 载体 | 许可 |
|---|---|---|
| 代码 | `output_registry.py` | **MIT** |
| 文档与理论文本 | 本 `SKILL.md`、`README.md`、其中「理论依据」段与一切理论表述 | **不在 MIT 覆盖范围内**：保留所有权利（All rights reserved） |

> 即：**代码可依 MIT 使用与再分发；文档与理论文本不因代码许可而默认可自由再发布。**

```
© 2026 赵兴华 / Steven Zhao·China (ORCID 0009-0001-0512-1237). All rights reserved.
理论署名 (attribution) : LGD（Lifecycle Governance Doctrine / 全程治理论）— SynomosAI initiative
名称状态 (name status)  : "SynomosAI" / "MedXpert" — 未申请实体注册、未申请商标注册
                        (not a registered legal entity; no trademark registered)
生产参考部署 (production reference, self-reported) : MedXpert
                    ← 非认证、非背书、非监管认可（not a certification or endorsement）
代码许可 (code license) : uibc-core = Apache-2.0 (see repo LICENSE)
                    本文本与理论表述不在 Apache-2.0 覆盖范围内
引用格式 (cite as)      : uibc-core/CITATION.cff · concept DOI 10.5281/zenodo.22821834
首次公开锚 (first public): 2026-09-17 13:31:45 UTC (commit cb6f11b)
                    外锚 (external anchor): Sigstore Rekor logIndex 2883389783
```
（上列为《LGD 对外表述规范》§3.2 统一块，**整体复制、未删改**；发布/重提前须照最新版本复核。）

**本包补充（包级许可事实）**：本包代码文件 `output_registry.py` = **MIT**；本 `SKILL.md` / `README.md` 及其中的理论文本**不在任何代码许可（含 MIT / Apache-2.0）覆盖范围内**。
