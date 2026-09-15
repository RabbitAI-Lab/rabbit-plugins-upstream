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
npx skills add zhaoxinghua09-cell/agent-skills -g

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone https://github.com/zhaoxinghua09-cell/agent-skills.git
cp -r agent-skills/skills/agent-output-registry ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/agent-output-registry/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |
