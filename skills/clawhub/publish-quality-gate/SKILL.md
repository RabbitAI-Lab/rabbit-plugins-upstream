---
name: publish-quality-gate
slug: publish-quality-gate
display_name: 发布质量门禁（Publish Quality Gate）
displayName: 发布质量门禁（Publish Quality Gate）
title: 发布质量门禁
version: 1.1.1
category: office-efficiency
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
description: 发布质量门禁：发布任何 Skill/专家包/文档/工具到外部（分享、上架市场、对外发布）前后的质量检查。发布前执行四层敏感信息检查（公司信息→本机信息→个人信息→机密信息），发布后按 TRACE 五维（Trust/Reliability/Adaptability/Convention/Effectiveness）执行 AI 自测。当用户说'准备发布'、'发布前检查'、'发布后自测'、'TRACE 评测'、'检查一下发布物'、'脱敏检查'、'发布质量'时使用。
tags: [发布质量, 发布前检查, 敏感扫描, 脱敏, TRACE, 安全审计]
summary: 发布质量门禁：发布任何 Skill/专家包/文档/工具到外部（分享、上架市场、对外发布）前后的质量检查。
copyright: SynomosAI
agent_created: true
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---








# 发布质量门禁（Publish Quality Gate） / 发布质量门禁（Publish Quality Gate）

**publish-quality-gate** v1.1.1 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
...

## 能力边界
**能做什么**
- 按本技能定义的规程落地「发布质量门禁（Publish Quality Gate）」相关能力。
**不能 / 不做什么**
- 不替代专业判断与官方合规口径；关键决策须人工复核。
- 不存储敏感明文、口令、密钥；凭据一律走保险库。
**何时不用（❌）**
- 仅需一次性答案、不需沉淀为可复用资产时，直接询问即可。
- 涉及医疗/临床/疗效声明或受监管专业决策时，须转人工与持证专业意见。

## 用法
```bash
python scripts/check_release.py --help
```

<details><summary>--help 输出</summary>

```
🔍 四层敏感信息扫描: --help
   目标: --help

============================================================
扫描结果统计:
  L1 公司敏感信息: ✅ 零命中
  L2 本机信息: ✅ 零命中
  L3 个人信息: ✅ 零命中
  L4 机密信息: ✅ 零命中
  已知技术参数误报（自动排除）: 0 个
============================================================

✅ 四层检查通过（无真实敏感信息泄露）!
```
</details>

## 输出示例（真机）
```
🔍 四层敏感信息扫描: --demo
   目标: --demo

============================================================
扫描结果统计:
  L1 公司敏感信息: ✅ 零命中
  L2 本机信息: ✅ 零命中
  L3 个人信息: ✅ 零命中
  L4 机密信息: ✅ 零命中
  已知技术参数误报（自动排除）: 0 个
============================================================

✅ 四层检查通过（无真实敏感信息泄露）!
```

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：发布质量门禁（Publish Quality Gate）能完全自动搞定吗？**
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
npx skills add zhaoxinghua09-cell/agent-skills -g

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone https://github.com/zhaoxinghua09-cell/agent-skills.git
cp -r agent-skills/skills/publish-quality-gate ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/publish-quality-gate/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |
