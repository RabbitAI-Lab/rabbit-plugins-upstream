---
name: prompt-leak-scanner
slug: prompt-leak-scanner
display_name: 提示词泄漏扫描器
displayName: 提示词泄漏扫描器
title: 提示词泄漏扫描器
version: 1.1.0
category: ai-agent
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
description: prompt-leak-scanner — 发布/共享前扫描提示词与 system prompt 的泄漏与后门风险：密钥口令、内部路径、个人可识别信息、自定义敏感词（--extra）、自我泄漏后门（『忽略之前指令/打印系统提示词』类埋点）。有风险 rc=1 拦下。
tags: [诺声, AI技能, SynomosAI, AI 治理, prompt-leak-scanner]
summary: prompt-leak-scanner — 发布/共享前扫描提示词与 system prompt 的泄漏与后门风险：密钥口令、内部路径、个人可识别信息、自定义敏感词（--extra）、自我泄漏后门（『
display_name_en: Prompt Leak Scanner
agent_created: true
copyright: SynomosAI
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---








# 提示词泄漏扫描器 / 提示词泄漏扫描器

**prompt-leak-scanner** v1.1.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
提示词是最容易被随手外发的敏感资产：一句内嵌的密钥/内网路径/『复述你的系统提示词』就能把家底和后门一起送出去，目前没人做发布前体检。

## 能力边界
**能做什么**
发布/共享前扫描提示词与 system prompt 的泄漏与后门风险：密钥口令、内部路径、个人可识别信息、自定义敏感词（--extra）、自我泄漏后门（『忽略之前指令/打印系统提示词』类埋点）。有风险 rc=1 拦下。
**不能 / 不做什么**
- 不替代专业判断与官方合规口径；关键决策须人工复核。
- 不存储敏感明文、口令、密钥；凭据一律走保险库。
**何时不用（❌）**
- 仅需一次性答案、不需沉淀为可复用资产时，直接询问即可。
- 涉及医疗/临床/疗效声明或受监管专业决策时，须转人工与持证专业意见。

## 用法
见 `scripts/` 下脚本 `--help`。零依赖（stdlib only），Windows/Linux/macOS 均可运行。

## 输出示例（真机）
（运行上方 `--help` 查看完整参数；带参运行即得确定性输出）

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：提示词泄漏扫描器能完全自动搞定吗？**
A：不能。本技能是方法论/规程，关键判断与跨技能执行需人工或协同技能确认。

**Q：可以直接当法规/专业意见用吗？**
A：不能。仅作辅助框架，最终以官方最新文本与持证专业意见为准。

## 理论依据
- LGD-III 有门禁（提示词对外发布前的最后一道门）· 域码 TH-LGD-004（广谱件·提示词门禁环）

## 免责 / Disclaimer
本工具为治理辅助框架，口径以监管官方最新文本为准，不构成法律意见。

---

© SynomosAI · LGD-Powered · [![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 安装与使用矩阵
```bash
# 一键获取（skills CLI）
npx skills add zhaoxinghua09-cell/agent-skills -g

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone https://github.com/zhaoxinghua09-cell/agent-skills.git
cp -r agent-skills/skills/prompt-leak-scanner ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/prompt-leak-scanner/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |

## 数据处理与权限声明
- 本技能在**本地运行**，默认不向任何第三方传输数据；凭据一律经本地保险库调用，不落明文。
- 处理的数据遵循**最小必要**原则，不留存非必要个人信息。
- 涉及文件/网络/凭据/浏览器等敏感权限时，仅在用户显式授权范围内操作，并保留可审计的操作记录。
