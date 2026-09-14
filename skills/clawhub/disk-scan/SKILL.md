---
name: disk-scan
slug: disk-scan
display_name: 磁盘占用扫描
displayName: 磁盘占用扫描
title: 磁盘占用扫描
version: 1.1.0
category: office-efficiency
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
description: 磁盘占用扫描 — 只读扫描目录占用：Top N 大文件 + 各子目录大小排行，快速定位空间杀手（零依赖）
tags: [诺声, AI技能, SynomosAI, 效率工具, disk-scan]
summary: 磁盘占用扫描 — 只读扫描目录占用：Top N 大文件 + 各子目录大小排行，快速定位空间杀手（零依赖）
display_name_en: Disk Usage Scan
agent_created: true
copyright: SynomosAI
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---









# 磁盘占用扫描 / 磁盘占用扫描

**disk-scan** v1.1.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
盘满了不知道谁吃的空间，资源管理器算半天还看不清

## 能力边界
**能做什么**
- 按本技能定义的规程落地「磁盘占用扫描」相关能力。
**不能 / 不做什么**
- 不替代专业判断与官方合规口径；关键决策须人工复核。
- 不存储敏感明文、口令、密钥；凭据一律走保险库。
**何时不用（❌）**
- 仅需一次性答案、不需沉淀为可复用资产时，直接询问即可。
- 涉及医疗/临床/疗效声明或受监管专业决策时，须转人工与持证专业意见。

## 用法
```bash
python scripts/disk_scan.py --help
```
- 成功 → rc=0；发现问题 → rc=1；用法错误 → rc=2
- 支持 `--json` 机器可读输出
- 涉及写盘的操作默认 **dry-run 预览**，加 `--apply` 才执行（text-replace/dup-finder 还会先备份）

## 输出示例（真机）
（运行上方 `--help` 查看完整参数；带参运行即得确定性输出）

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：磁盘占用扫描能完全自动搞定吗？**
A：不能。本技能是方法论/规程，关键判断与跨技能执行需人工或协同技能确认。

**Q：可以直接当法规/专业意见用吗？**
A：不能。仅作辅助框架，最终以官方最新文本与持证专业意见为准。

## 免责 / Disclaimer
本工具为效率辅助；对重要数据请先备份并在预览确认后再 --apply。

---

© SynomosAI · LGD-Powered · [![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 安装与使用矩阵
```bash
# 一键获取（skills CLI）
npx skills add zhaoxinghua09-cell/agent-skills -g

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone https://github.com/zhaoxinghua09-cell/agent-skills.git
cp -r agent-skills/skills/disk-scan ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/disk-scan/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |

## 数据处理与权限声明
- 本技能在**本地运行**，默认不向任何第三方传输数据；凭据一律经本地保险库调用，不落明文。
- 处理的数据遵循**最小必要**原则，不留存非必要个人信息。
- 涉及文件/网络/凭据/浏览器等敏感权限时，仅在用户显式授权范围内操作，并保留可审计的操作记录。
