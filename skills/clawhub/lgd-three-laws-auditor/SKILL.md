---
name: lgd-three-laws-auditor
slug: lgd-three-laws-auditor
display_name: LGD 三律合规自检器（凡自治之物）
displayName: LGD 三律合规自检器（凡自治之物）
title: LGD 三律合规自检器（凡自治之物）
version: 1.1.0
category: ai-agent
platforms: [windows, macos, linux]
author: 诺声(Logos)@SynomosAI
license: MIT
description: 当用户问『我的 AI 系统合不合规 / 怎么评判 AI 治理水平 / agent 要不要上治理护栏』，或要落地『有籍·有证·有门禁』时用。把 LGD 三律做成一套可自评的标准 rubric（有籍=身份/版本/血缘/责任四项登记；有证=六类证据工件齐备；有门禁=触发/评审/放行/复盘四道门），输入系统描述即出评分卡+改进项。这不仅是工具，更是 LGD 治理思想的『定义器』——谁用三籍词汇自评，谁就采用了我们的治理定义权（护城河）。触发词：LGD 三律、有籍有证有门禁、凡自治之物、AI 合规自评、AI 治理标准、agent 治理护栏、三律审计。
tags: [LGD, 三律, 凡自治之物, AI治理, 合规自检, 有籍, 有证, 有门禁, 标准定义]
display_name_en: LGD Three-Laws Compliance Auditor
summary: 当用户问『我的 AI 系统合不合规 / 怎么评判 AI 治理水平 / agent 要不要上治理护栏』，或要落地『有籍·有证·有门禁』时用。
agent_created: true
copyright: SynomosAI
read_when: 
homepage: https://zhaoxinghua09-cell.github.io/lgd-hub/
---








# LGD 三律合规自检器（凡自治之物） / LGD 三律合规自检器（凡自治之物）

**lgd-three-laws-auditor** v1.1.0 · LGD-Powered 家族 · 零依赖·确定性输出 · 退出码 rc=0/1/2

![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 痛点
- **定义权**：rubric 即标准载体，自评即教育——行业用我们的词汇，护城河就成立。
- **闭环互补**：自检发现问题 → 用 `lgd-certify` 签发三律认证（护照→证据链→门禁→徽章）→ 用 `agent-output-registry` 落地"有籍" → 用 `evidence-chain-builder` 落地"有证"。
- **零依赖离线**：纯 stdlib，无云、无密钥，企业内网可直接跑。

## 能力边界
- 本工具输出为**自评辅助**，不构成法律/监管意见；正式合规以属地法规与专业判断为准。
- 启发式自评仅作提示，最终以人工填答的 `--answers` 为准。
- 不编造：缺证据的项标"缺失/未评估"，绝不假装达标。

## 用法
1. `python lgd_audit.py --rubric` —— 先看完整三律标准（可作对外治理文档）。
2. `python lgd_audit.py --system "你的 AI 系统描述"` —— 启发式自评（关键词推测，标"待确认"，**不编造结论**）。
3. `python lgd_audit.py --answers 答卷.json --json` —— 人工填答卷出正式评分卡。
4. 看「改进项」补齐证据工件/登记项，分数即护城河完整度。

## 输出示例（真机）
```bash
# 看标准
python scripts/lgd_audit.py --rubric

# 自评一段系统描述
python scripts/lgd_audit.py --system "我们用 qwen 模型，版本用 git 管理，输出带日志，上线需审批"

# 正式评分（答卷.json: {"LGD-I 有籍 REGISTERED": {"身份登记":"yes","版本登记":"yes",...}}）
python scripts/lgd_audit.py --answers 答卷.json
```

## 退出码与错误码
- `rc=0` 通过 / `rc=1` 发现问题 / `rc=2` 用法或环境错误

（无预定义错误码常量；失败时以非零 rc + 人类可读错误信息退出，不抛原始栈帧）

## 反模式 FAQ
**Q：LGD 三律合规自检器（凡自治之物）能完全自动搞定吗？**
A：不能。本技能是方法论/规程，关键判断与跨技能执行需人工或协同技能确认。

**Q：可以直接当法规/专业意见用吗？**
A：不能。仅作辅助框架，最终以官方最新文本与持证专业意见为准。

## 免责 / Disclaimer
- 本工具输出为**自评辅助**，不构成法律/监管意见；正式合规以属地法规与专业判断为准。
- 启发式自评仅作提示，最终以人工填答的 `--answers` 为准。
- 不编造：缺证据的项标"缺失/未评估"，绝不假装达标。

---

© SynomosAI · LGD-Powered · [![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## 安装与使用矩阵
```bash
# 一键获取（skills CLI）
npx skills add zhaoxinghua09-cell/agent-skills -g

# 或手动：克隆后拷贝本技能到你的 Agent 技能目录
git clone https://github.com/zhaoxinghua09-cell/agent-skills.git
cp -r agent-skills/skills/lgd-three-laws-auditor ~/.workbuddy/skills/
```

| Agent | 技能目录 | 运行示例 |
|---|---|---|
| Claude Code | `~/.claude/skills/lgd-three-laws-auditor/` | 让 Claude 按本技能 SKILL.md 工作流调用脚本 |
| Codex / Cursor / WorkBuddy | 各自 skills 目录 | 同上，SKILL.md 即操作规程 |
| 直接命令行 | 任意位置 | `python scripts/*.py --help`（代码件） |

## 合规与免责声明
- 本技能为辅助性合规框架/工具，**不替代持证专业意见与官方最新文本**；关键判断须人工或协同持证专业意见确认。
- 输出涉及的法规/标准/条款以官方发布版本为准；本技能仅作结构化自检参考。
- 本技能默认**本地离线运行**，不采集、不上传用户业务数据；如涉及敏感数据，请遵循最小必要与本地处理原则。
