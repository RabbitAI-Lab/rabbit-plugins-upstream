---
name: prompt-version-control
display_name: 提示版本管理（Prompt Version Control）
display_name_en: "Prompt Version Control"
description: "当用户说『提示改乱了回不去』『不知道哪版提示效果更好』『提示也要版本管理』『怎么AB测试不同提示』，或团队多人改同一套提示容易互相覆盖时使用。把提示当『可版本化资产』：每次改动留版本+差异+绑定效果评分，可 diff/回滚/选优。理论根基：LGD 三律（有籍·有证·有门禁）。触发词：提示版本、prompt版本管理、提示回滚、prompt diff、AB测试提示、提示治理、prompt registry。"
version: 1.1.1
agent_created: true
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Write
category: AI工程方法
platforms: [windows, macos, linux]
platform_compatibility: [windows, macos, linux]
read_when:
  - 提示被多人改、互相覆盖、回不去
  - 想对比不同提示版本的效果
  - 要保留「哪版提示对应哪次结果」的关联
  - 用户问「提示能不能像代码一样版本管理」
tags: [提示版本, prompt version, 提示回滚, prompt diff, AB测试, 提示治理, agent优化, 可复现]
slug: prompt-version-control
title: 提示版本管理（Prompt Version Control）
copyright: SynomosAI
description_zh: "当用户说『提示改乱了回不去』『不知道哪版提示效果更好』『提示也要版本管理』『怎么AB测试不同提示』，或团队多人改同一套提示容易互相覆盖时使用。把提示当『可版本化资产』：每次改动留版本+差异+绑定效果评分，可 diff/回滚/选优。理论根基：LGD 三律（有籍·有证·有门禁）。触发词：提示版本、prompt版本管理、提示回滚、prompt diff、AB测试提示、提示治理、prompt registry。"
description_en: "Treat prompts as versioned assets: every change tracked with diff and bound effect scores, diffable and revertible for team collaboration and A/B testing."
classification:
  skillhub: ["security-compliance"]
  iso_25010: ["Security"]
risk_tier: medium
risk_rationale: "门禁批量补丁默认 medium（内部约定：本 skill 设计为中等风险）：调用 API/读写文件/本地执行，最小权限，密钥走 Secret；若实际涉对外代执行(push/发布/发送/上架)须人工复评，改 high 并走负责人批准。"
ai_protocol: true
spec: usk/1.0
interface:
  type: cli
  entry_point: scripts/prompt_vc.py
  runtime: python3
  call_pattern: args
input_schema:
  old:
    type: string
    description: "old"
    required: true
  new:
    type: string
    description: "new"
    required: true
  score:
    type: number
    description: "score"
    required: false
  registry:
    type: string
    description: "registry"
    required: false
  json:
    type: bool
    description: "json"
    required: false
output_schema:
  stdout: 结构化 JSON IR（含 result / rc / error_code / warnings）
  exit_code: rc=0 正常 / rc=1 告警或从严推定 / rc=2 输入不足或非法
capabilities:
  - prompt
  - versioning
  - vcs
permissions:
  network: false
  filesystem: false
  subprocess: false
requirements:
  python_packages: []
  min_python: "3.8"
changelog: "1.1.1: Bilingual rewrite (full EN+ZH, English first); 1.0.0: initial upload (USK v3)"
---

> 凡自治之物 · LGD 治理学 · 创造术家族 ｜ 评测协议：skill-quality-gate

## English

### When to use
- When users report abnormal prompt performance or mis-operation that makes the old version unrecoverable.
- When a team co-authors the same prompt set and must prevent editors' configurations from overwriting each other.
- When comparing prompt versions (A/B test) and evaluating which is better.
- When change history and version diffs must be recorded for audit traceability.

### Usage
- Basic create: `python prompt_vc.py create <prompt_id> --tag <v_name> --effect_score`; modifier credentials must be bound.
- Diff compare: `compare <v1> <v2> --metric accuracy` produces a diff report for winner selection.
- Rollback: `rollback <version_id>` restores the system config to a chosen historical version, protected by gate permissions.
- Parameters: every command supports `--effect_score` (0-1) and `--owner_id`, both required to satisfy the registered/evidenced principles.

### Workflow
1. Branch and commit: the create script issues a unique version ID for the current prompt and records the initial diff.
2. Bind credentials and scores: at commit time, link the modifier identity, change reason and expected/measured effect score.
3. Gate check: the system auto-verifies access permissions so the change complies with the LGD "gated" requirement.
4. Merge and release: after scoring-based selection or manual approval, merge the new version into the main branch and archive it.
5. Diff trace: use diff to inspect old vs new versions; supports A/B-test evidence-chain records.
6. Rollback or switch: when performance fails, trigger rollback, lock the current config and load the chosen old version ID.

### Evidence & safety statement
- Evidence: TBD (no evaluation / badge link yet; update here once produced)
- Version: 1.1.1
- Safety: no independent security scan has been performed (TBD); the conclusion is pending and no endorsement is given until it is completed.

## 中文

### 何时用
- 当用户反馈提示词效果异常或误操作导致无法恢复旧版时。
- 当团队多人协作编写同一套提示，需防止修改者之间的配置相互覆盖时。
- 当需要进行不同版本的提示词对比测试（AB Test）并评估优劣时。
- 当需要记录变更历史及版本差异以便进行审计追溯时。

### 用法
- 基础创建命令：`python prompt_vc.py create <prompt_id> --tag <v_name> --effect_score`，需绑定修改者凭证。
- 差异对比命令：使用 `compare <v1> <v2> --metric accuracy` 生成 Diff 报告，用于选优分析。
- 版本回滚命令：执行 `rollback <version_id>` 将系统配置恢复到指定历史版本，受门禁权限保护。
- 参数说明：所有命令支持 `--effect_score`（0-1 分数值）和 `--owner_id` 字段，必须填写以符合有籍·有证原则。

### 流程
1. 创建分支与提交：调用 create 脚本为当前提示词生成唯一版本 ID，记录初始差异内容。
2. 绑定凭证与评分：在提交时关联修改者身份、变更理由及预期或实测效果评分数据。
3. 门禁校验：系统自动检查访问权限，确保变更符合 LGD 三律中的“有门禁”要求。
4. 版本合并与发布：根据评分选优或人工审批后，将新版本合并至主分支并归档。
5. 差异追溯与对比：通过 diff 功能查看新旧版本差异，支持生成 AB 测试证据链记录。
6. 回滚或切换：在效果不达标时触发 rollback 指令，锁定当前配置并加载指定旧版本 ID。

### 证据与安全声明

- 证据：TBD（暂无评测/徽章链接；产生后在此更新实际链接）
- 版本：1.1.1
- 安全：未做独立安全扫描（TBD），结论待补；补全前不作推荐背书。
