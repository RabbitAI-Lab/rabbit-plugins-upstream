---
name: evidence-chain-builder
slug: evidence-chain-builder
display_name: AI 论断有证证据链（LGD-II 有证）
displayName: AI 论断有证证据链（LGD-II 有证）
title: AI 论断有证证据链（LGD-II 有证）
version: 1.1.0
category: ai-agent
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
description: 当用户要『验证 AI 论断 / 防幻觉 / 给结论找证据 / 判断信源可信度』时用。把论断拆成可验证证据链：每条证据标来源类型(official/paper/data/internal/assertion)、是否可独立验证、可信度，输出『证成度』与未支撑论断清单。对齐 EIFP 不编造原教旨——本工具不判定论断真假，只评估证据质量；缺可验证证据的论断明确标『勿作结论』。这是 LGD-II 有证的落地执行器。触发词：证据链、论断验证、防幻觉、信源可信、有证、claim 证据、论断举证。
tags: [LGD, 有证, 证据链, 防幻觉, 事实核查, 信源, 证成度, 不编造]
display_name_en: AI Claim Evidence-Chain Builder (LGD-II Evidenced)
summary: 当用户要『验证 AI 论断 / 防幻觉 / 给结论找证据 / 判断信源可信度』时用。
agent_created: true
copyright: SynomosAI
read_when: 
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---








# AI 论断有证证据链（LGD-II 有证） / AI 论断有证证据链（LGD-II 有证）

**evidence-chain-builder** v1.1.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
- AI 张口就来、论断不可信 → 强制"先有证据再下结论"。
- 幻觉无法举证 → 证据链把"信"变成"可查"。
- 内部/主张类被当成事实 → 明确降权、标注不可独立验证。

## 能力边界
- 本工具**不判定论断真假**，只评估证据质量——这是"不编造"的硬边界。
- 证成度≠正确度；最终判断仍须人工复核原始来源。
- 不编造：内部/主张类证据明确标"不可独立验证"，绝不冒充官方佐证。

## 用法
```bash
# 直接给论断+证据（|| 分隔；@类型:来源 后缀可选）
python scripts/evidence_chain.py --claim "本产品不良率低于 0.5%" \
  --evidences "2025 年度质检报告@official:公司QA" "客户反馈无相关投诉@internal:客服"

# 从 JSON 构建
python scripts/evidence_chain.py --from claim.json --json
```

证据格式：`文本@类型:来源`，如 `2024年报@official:统计局`。

## 输出示例（真机）
（运行上方 `--help` 查看完整参数；带参运行即得确定性输出）

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：AI 论断有证证据链（LGD-II 有证）能完全自动搞定吗？**
A：不能。本技能是方法论/规程，关键判断与跨技能执行需人工或协同技能确认。

**Q：可以直接当法规/专业意见用吗？**
A：不能。仅作辅助框架，最终以官方最新文本与持证专业意见为准。

## 免责 / Disclaimer
- 本工具**不判定论断真假**，只评估证据质量——这是"不编造"的硬边界。
- 证成度≠正确度；最终判断仍须人工复核原始来源。
- 不编造：内部/主张类证据明确标"不可独立验证"，绝不冒充官方佐证。

---

© SynomosAI · LGD-Powered · [![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 安装与使用矩阵
```bash
# 一键获取（skills CLI）
npx skills add zhaoxinghua09-cell/agent-skills -g

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone https://github.com/zhaoxinghua09-cell/agent-skills.git
cp -r agent-skills/skills/evidence-chain-builder ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/evidence-chain-builder/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |
