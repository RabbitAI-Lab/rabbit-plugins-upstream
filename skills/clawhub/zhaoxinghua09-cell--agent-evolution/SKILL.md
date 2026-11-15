---
name: agent-evolution
display_name: 数字员工进化飞轮
display_name_en: Agent Evolution Flywheel
description: 'AI 团队「复盘→固化」进化飞轮。当某席数字员工完成一单任务、或用户要求「复盘/进化/沉淀经验/固化经验」时调用。提取本次可复用经验，判定沉淀为技能(SkillManage,动作型)还是记忆(memory,信息型)，并回写该席能力卡的进化记录，使团队下次更强。触发词：复盘、进化、沉淀经验、固化经验、agent-evolution、能力提升。'
description_zh: 'AI 团队「复盘→固化」进化飞轮。当某席数字员工完成一单任务、或用户要求「复盘/进化/沉淀经验/固化经验」时调用。提取本次可复用经验，判定沉淀为技能(SkillManage,动作型)还是记忆(memory,信息型)，并回写该席能力卡的进化记录，使团队下次更强。触发词：复盘、进化、沉淀经验、固化经验、agent-evolution、能力提升。'
description_en: 'AI team''s "review → solidify" evolution flywheel. Invoked when a digital employee completes a task, or the user requests "review / evolve / distill experience / solidify experience". Extracts reusable experience from the run and decides whether to crystallize it as a Skill (action-type, via SkillManage) or as memory (info-type), then writes back the evolution record to that employee''s capability card so the team gets stronger next time. Trigger words: review, evolve, distill experience, solidify experience, agent-evolution, capability improvement.'
version: '1.1.1'
agent_created: true
author: 潘布达 (Buda Pan) @SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Write, Edit, WebFetch, WebSearch
category: AI工程
slug: agent-evolution
displayName: Agent 复盘进化飞轮（复盘→固化）
title: Agent 复盘进化飞轮（复盘→固化）
platforms: [Claude Code, Windows, macOS, Linux, cli]
classification:
  skillhub: ["security-compliance"]
  iso_25010: ["Security"]
risk_tier: medium
risk_rationale: "门禁批量补丁默认 medium：调用 API/读写文件/本地执行，最小权限，密钥走 Secret；若实际涉对外代执行(push/发布/发送/上架)须人工复评，改 high。"
tags: [agent-evolution, AI工程]
read_when:
  - 某席数字员工完成一单高价值任务后自动复盘
  - 用户说「复盘/进化/沉淀经验/固化经验」
  - 定期把临时操作经验批量转成团队共享技能库
ai_protocol: true
spec: usk/1.0
interface:
  type: cli
  entry_point: SKILL.md
  runtime: text
  call_pattern: args
input_schema:
  - name: situation
    type: string
    description: 待评估的智能体自我演进/修改提议
    required: true
output_schema:
  stdout: 演进风险评审要点与边界清单文本
  exit_code: "0=正常"
capabilities:
  - ai_governance
  - agent_evolution
  - self_modification
permissions:
  network: false
  filesystem: false
  subprocess: false
requirements:
  python_packages: []
  min_python: "3.8"
changelog: "1.1.1: Bilingual rewrite (full EN+ZH, English first); 1.0.0: initial upload (USK v3)"
---

> 凡自治之物 · LGD 治理学 · 创造术家族 ｜ 评测协议：skill-quality-gate（外部公开评测门禁文档）

## English

### When to use
- **Task closed-loop**: when a digital employee completes a high-value task and "review" / "distill experience" intent is detected.
- **Explicit request**: the user or admin says "evolve" / "solidify capability" and asks to extract standardized behavior from the current session.
- **Team capability update**: during maintenance windows, batch-convert ad-hoc operational experience into the team shared skill library.

### Usage
- Trigger: no external script; auto-activated via a pre-hook or listening to trigger words such as "agent-evolution".
- Params: input = task context data; output = JSON evolution record (`type`: "Skill"|"Memory", `content`, `timestamp`).
- Mode: pass the current session/task result as the experience source; configure this skill as doc-type auto-write-back.

### Flow
1. Receive task logs or a natural-language request ("review this service").
2. Parse text/dialogue; identify reusable behavior patterns, rule snippets and data regularities.
3. Decide knowledge type: action-type skill (SkillManage) vs static info memory (Memory).
4. Compliance check: does the solidified data meet security policy and team standards?
5. Write back to the capability card: mark as "solidified".
6. Return confirmation to the caller, stating the new capability scope.

### Evidence & safety
- Evidence: TBD.
- Version: 1.1.1
- Security: no independent scan (TBD).

## 中文

### 何时用
- **任务闭环场景**：当某席数字员工完成一单高价值业务任务时，系统检测到"复盘"、"沉淀经验"等隐含意图需自动触发。
- **显式指令请求**：外部用户或管理员直接发送"进化"、"固化能力"等关键词，要求对当前会话行为进行标准化提取。
- **团队能力更新**：在定期运维窗口期，当需要批量将临时操作经验转化为团队共享技能库时调用。

### 用法
- **触发方式**：无需执行外部脚本，通过配置节点的前置钩子或监听指定触发词（如「agent-evolution」）自动激活。
- **参数说明**：输入为任务上下文数据，输出为 JSON 格式的进化记录摘要（含 `type`: "Skill"|"Memory", `content`, `timestamp`）。
- **使用方式**：将当前会话或任务结果作为经验源传入系统，配置该技能为文档型自动回写模式。

### 流程
1. 接收任务执行日志或用户自然语言指令（如"复盘本次服务"）。
2. 解析文本与对话记录，识别可复用的行为模式、规则片段及数据规律。
3. 判定知识类型：操作型技能（SkillManage）vs 静态信息记忆（Memory）。
4. 校验内容合规性。
5. 回写能力卡进化记录：标记为"已固化"。
6. 返回确认反馈：通知调用方本次经验提取完成，并告知新的能力应用范围。

### 证据与安全声明
- 证据：TBD（暂无评测/徽章链接；产生后在此更新实际链接）
- 版本：1.1.1
- 安全：未做独立安全扫描（TBD），结论待补；补全前不作推荐背书。
