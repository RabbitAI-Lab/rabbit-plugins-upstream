---
name: agent-memory-keeper
display_name: 跨会话长期记忆治理（Memory Keeper）
display_name_en: "Agent Memory Keeper"
description: "当用户说『AI又忘了我之前说的』『记忆越来越乱/重复/互相矛盾』『长期记忆怎么管』『记忆库该清理了』，或要设计/治理一个 agent 的跨会话记忆（笔记/知识库/偏好/项目约定）时使用。把记忆当成『有籍贯、可审计、能收敛』的资产：审计重复·孤儿·陈旧·无溯源四维度，给出收敛(单一真源)+门禁(改前备份)两步流程与可运行脚本（记忆审计器）。理论根基：LGD 三律（有籍·有证·有门禁）。触发词：长期记忆、跨会话记忆、memory governance、记忆治理、记忆重复、记忆冲突、记忆溯源、agent记忆、知识库去重、记忆清理。"
version: 1.1.1
agent_created: true
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep
category: AI工程方法
platforms: [windows, macos, linux]
read_when:
  - AI 在关掉对话后丢失了用户之前明确说过的约定/偏好
  - 记忆库里出现多条互相矛盾或高度重复的内容
  - 要搭建或清理一个 agent 的长期记忆（笔记/知识库/项目约定）
  - 用户抱怨「你上次记的不算数」或「记忆怎么乱了」
  - 想给记忆条目加溯源（谁、何时、从哪来）
tags: [长期记忆, memory governance, 记忆治理, 记忆去重, 跨会话, 记忆溯源, agent优化]
slug: agent-memory-keeper
title: 跨会话长期记忆治理（Memory Keeper）
copyright: SynomosAI
description_zh: "当用户说『AI又忘了我之前说的』『记忆越来越乱/重复/互相矛盾』『长期记忆怎么管』『记忆库该清理了』，或要设计/治理一个 agent 的跨会话记忆（笔记/知识库/偏好/项目约定）时使用。把记忆当成『有籍贯、可审计、能收敛』的资产：审计重复·孤儿·陈旧·无溯源四维度，给出收敛(单一真源)+门禁(改前备份)两步流程与可运行脚本（记忆审计器）。理论根基：LGD 三律（有籍·有证·有门禁）。触发词：长期记忆、跨会话记忆、memory governance、记忆治理、记忆重复、记忆冲突、记忆溯源、agent记忆、知识库去重、记忆清理。"
description_en: "Govern an agent's cross-session memory as an auditable, converging asset: provenance, dedup, conflict resolution and cleanup for notes, knowledge bases, preferences and project conventions."
classification:
  skillhub: ["knowledge"]
  iso_25010: ["Maintainability"]
risk_tier: medium
risk_rationale: "门禁批量补丁默认 medium：调用 API/读写文件/本地执行，最小权限，密钥走 Secret；若实际涉对外代执行(push/发布/发送/上架)须人工复评，改 high。"
ai_protocol: true
spec: usk/1.0
interface:
  type: cli
  entry_point: scripts/memory_audit.py
  runtime: python3
  call_pattern: args
input_schema:
  - name: dir
    type: string
    description: 记忆目录（.md/.jsonl）
    required: false
  - name: file
    type: string
    description: 单个 JSONL 文件
    required: false
  - name: stale-days
    type: int
    description: 陈旧阈值天数，默认30
    required: false
  - name: json
    type: bool
    description: JSON 输出
    required: false
output_schema:
  stdout: 四类问题清单（重复/孤儿/陈旧/无籍）
  exit_code:
    type: integer
    description: "0=OK/PASS; 1=findings/warnings; 2=usage or argument error"
capabilities:
  - memory_audit
  - data_quality
  - maintenance
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
1. The user reports memory loss, lost context or confusion.
2. Cross-session memory needs governance: duplicates, contradictions, stale entries.
3. Designing a long-term memory system; memory audit and LGD three-law compliance checks.

### Usage
1. Run `python memory_audit.py` to start the memory auditor.
2. `--converge` merges into a single source of truth; `--backup` runs the pre-change backup gate.
3. Activate via trigger words; no need to touch `__pycache__`.

### Flow
1. Identify the user's memory-management intent (forgetting / conflict / cleanup) and confirm permissions.
2. Run the four-dimension audit: duplicates, orphans, stale, no-provenance entries.
3. Tag memory-asset state per LGD; build a converged single-source index.
4. Backup gate before modifying the knowledge base (keep history).
5. Deduplicate and remove contradictory/outdated info.
6. Output the audit report plus the updated memory snapshot for user review.

### Evidence & safety
- Evidence: TBD. Version: 1.1.1. Security: no independent scan (TBD).

## 中文

### 何时用
1. 当用户反馈 AI 出现记忆遗忘、上下文丢失或逻辑混乱时。
2. 需要治理 Agent 的跨会话记忆，处理重复、矛盾或陈旧的知识资产时。
3. 涉及长期记忆系统设计，需执行记忆审计与 LGD 三律（有籍·有证·有门禁）合规检查时。

### 用法
1. 直接运行 Python 脚本 `python memory_audit.py` 启动内存审计器。
2. 添加参数 `--converge` 开启收敛模式，合并单一真源；添加参数 `--backup` 执行门禁改前备份。
3. 技能文档已内化，用户需通过触发词唤醒技能，无需直接访问 Python 缓存文件。

### 流程
1. 识别用户的记忆管理意图（遗忘/冲突/清洗）并确认调用权限。
2. 执行四维度审计：扫描重复、孤儿、陈旧及无溯源记忆条目。
3. 依据 LGD 三律标记记忆资产状态，建立可收敛的真实源索引。
4. 在修改知识库前自动触门禁备份（Backup Gate），保留历史版本。
5. 对识别出的矛盾或过时信息执行去重与剔除操作。
6. 输出审计报告与更新后的记忆库快照，供用户审核确认。

### 证据与安全声明
- 证据：TBD（暂无评测/徽章链接；产生后在此更新实际链接）
- 版本：1.1.1
- 安全：未做独立安全扫描（TBD），结论待补；补全前不作推荐背书。
