---
name: github-api-push-workaround
slug: github-api-push-workaround
display_name: github-api-push-workaround
displayName: github-api-push-workaround
title: github-api-push-workaround
version: 1.3.0
category: dev-programming
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Bash, Write, WebFetch
description: git 推 GitHub/Gitee/AtomGit 的根因化排查与推送模板：401=凭据问题（helper 链残留死旧 PAT）、超时/挂死=通道问题（代理掐 git 传输，须 no_proxy 直连）、大面积 401=取值前缀坑（--raw 取裸值）。含直连推送模板（令牌走环境变量）、Git Data API 兜底（blob→tree→commit→ref）、Gitee 私有转公开、AtomGit 后端 gitcode 等实测坑。当用户说'推 GitHub'、'git push 失败/401/超时'、'发布仓库到远端'、'令牌失效了'时使用。
tags: [github, git-push, 代理, 凭据, 排查, 发布, gitee, atomgit]
summary: git 推 GitHub/Gitee/AtomGit 的根因化排查与推送模板：401=凭据问题（helper 链残留死旧 PAT）、超时/挂死=通道问题（代理掐 git 传输，须 no_proxy 直
copyright: SynomosAI
agent_created: true
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---








# github-api-push-workaround / github-api-push-workaround

**github-api-push-workaround** v1.3.0 · LGD-Powered 家族 · 方法论·可落地 · AI 友好·边界清晰

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
git 推 GitHub/Gitee/AtomGit 的根因化排查与推送模板：401=凭据问题（helper 链残留死旧 PAT）、超时/挂死=通道问题（代理掐 git 传输，须 no_proxy 直连）、大面积 401=取值前缀坑（--raw 取裸值）。含直连推送模板（令牌走环境变量）、Git Data API 兜底（blob→tree→commit→ref）、Gitee 私有转公开、AtomGit 后端 gitcode 等实测坑。当用户说'推 GitHub'、'git push 失败/401/超时'、'发布仓库到远端'、'令牌失效了'时使用。

## 能力边界
**能做什么**
- 按本技能定义的规程落地「github-api-push-workaround」相关能力。
**不能 / 不做什么**
- 不替代专业判断与官方合规口径；关键决策须人工复核。
- 不存储敏感明文、口令、密钥；凭据一律走保险库。
**何时不用（❌）**
- 仅需一次性答案、不需沉淀为可复用资产时，直接询问即可。
- 涉及医疗/临床/疗效声明或受监管专业决策时，须转人工与持证专业意见。

## 用法
读取本 SKILL.md，按「能力边界 → 用法 → 示例」顺序落地；跨技能协同见对应章节。

## 输出示例（真机）
（方法论技能，无机器输出；落地示例见「反模式 FAQ」与正文示意）

## 反模式 FAQ
**Q：github-api-push-workaround能完全自动搞定吗？**
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
npx skills@1.7.0 add https://github.com/zhaoxinghua09-cell/agent-skills/tree/v2026.09.28.1/skills/github-api-push-workaround

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone --branch v2026.09.28.1 --depth 1 https://github.com/zhaoxinghua09-cell/agent-skills.git
# 校验：git -C agent-skills rev-parse HEAD 应与发布标签 v2026.09.28.1 一致
cp -r agent-skills/skills/github-api-push-workaround ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/github-api-push-workaround/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
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
| 代码 | 本包无独立代码文件（纯文档/理论件） | — |
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

**本包补充（包级许可事实）**：本包无独立代码文件（纯文档与理论文本件），整体**保留所有权利（All Rights Reserved）**；不适用任何代码许可（含 MIT / Apache-2.0）。
