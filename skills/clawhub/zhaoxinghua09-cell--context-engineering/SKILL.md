---
name: context-engineering
display_name: 上下文工程（Context Engineering）
display_name_en: "Context Engineering"
description: "当用户说『AI越来越笨/答非所问/忘了前面的设定』『上下文太长』『token烧太快』『RAG召回不准』，或要设计/优化 agent 的提示、记忆、检索、工具编排时使用。把『上下文窗口里到底该放什么』当成一门工程：审计相关性·冗余·预算·衰减 四维度，给出裁剪/检索/记忆/门禁四步流程与可运行脚本。触发词：上下文工程、context engineering、上下文窗口、上下文污染、上下文衰减、context rot、token预算、RAG召回、记忆编排、agent上下文、长上下文优化。"
version: 1.0.1
agent_created: true
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Write, WebFetch, WebSearch
category: AI工程方法
platforms: [windows, macos, linux]
read_when:
  - AI 在长对话/多轮任务里开始答非所问、遗忘早期约束
  - 要搭建或优化一个 agent 的 system prompt / 记忆 / 检索 / 工具返回
  - token 消耗异常高，怀疑上下文里有冗余或重复内容
  - RAG 召回的文档塞进上下文后反而让回答变差
  - 用户抱怨「你上次说的怎么不算数了」
tags: [上下文工程, context engineering, 上下文窗口, token预算, RAG, 记忆编排, agent优化]
slug: context-engineering
title: 上下文工程（Context Engineering）
copyright: SynomosAI
description_zh: "把『上下文窗口里到底该放什么』当成一门工程：审计相关性·冗余·预算·衰减 四维度，给出裁剪/检索/记忆/门禁四步流程与可运行脚本（上下文预算计算器+审计清单生成器）。"
description_en: "Engineer what goes into the context window: relevance audit, memory/retrieval/tool orchestration patterns to fix degraded answers, context overflow and token burn."
classification:
  skillhub: ["security-compliance"]
  iso_25010: ["Security"]
risk_tier: medium
risk_rationale: "门禁批量补丁默认 medium：调用 API/读写文件/本地执行，最小权限，密钥走 Secret；若实际涉对外代执行(push/发布/发送/上架)须人工复评，改 high。"
ai_protocol: true
spec: usk/1.0
interface:
  type: cli
  entry_point: scripts/context_budget.py
  runtime: python3
  call_pattern: args
input_schema:
  - name: window
    type: int
    description: 上下文窗口 token 上限默认128000
    required: false
  - name: block
    type: string
    description: stdin 归属块名
    required: false
output_schema:
  stdout: 各块 token 预算分配建议
  exit_code:
    type: integer
    description: "0=OK/PASS; 1=findings/warnings; 2=usage or argument error"
capabilities:
  - context_budget
  - llm_engineering
  - optimization
permissions:
  network: false
  filesystem: false
  subprocess: false
requirements:
  python_packages: []
  min_python: "3.8"
changelog: "1.0.1: Bilingual rewrite (full EN+ZH, English first); 1.0.0: initial upload (USK v3)"
---

> 凡自治之物 · LGD 治理学 · 创造术家族 ｜ 评测协议：skill-quality-gate（外部公开评测门禁文档）

## English

### When to use
1. The model starts giving off-topic answers or forgetting earlier settings ("context pollution / decay").
2. Designing / optimizing an agent's prompt, memory, RAG retrieval or tool orchestration.
3. Token burn is high; the context window is too long; memory orchestration needs refinement.
4. Trigger words: "context engineering", "long-context optimization", "RAG recall".

### Usage
1. Run `context_budget.py --calculate` to estimate current token budget and remaining window.
2. Set `--budget_limit` (int) and `--model_name` for model-specific advice.
3. `context_budget.py --audit` produces a relevance/redundancy checklist.
4. For doc-style tasks, read the in-file function library for memory-decay and retrieval-recall helpers.

### Flow
1. **Context audit**: scan interaction history; flag low-relevance, stale or duplicate info.
2. **Budget accounting**: compute current token share and remaining-window risk.
3. **Trimming**: apply the four-dimension standard (relevance / redundancy / budget / decay); compress memory.
4. **Retrieval tuning**: adjust RAG recall params and tool order so key data loads first.
5. **Gate check**: gate new incoming info so new tokens don't overwrite old key settings.
6. **Closed loop**: re-inject the optimized context into the model; log adjustments.

### Evidence & safety
- Evidence: TBD. Version: 1.0.1. Security: no independent scan (TBD).

## 中文

### 何时用
1. 当用户反馈模型"答非所问"、"遗忘设定"或遭遇"上下文污染"、"上下文衰减"等质量问题时。
2. 在进行 Agent 设计、优化提示词（Prompt）、记忆管理或 RAG 检索策略的技术调试与评估场景。
3. 监控对话成本，涉及"token 预算烧太快"、"上下文窗口过长"或需要精细化"记忆编排"时的决策节点。
4. 触发关键词包含"context engineering"、"长上下文优化"、"RAG 召回"及具体指标时自动介入。

### 用法
1. 执行核心计算脚本 `context_budget.py`，启用 `--calculate` 模式以输出当前对话的 Token 预算与剩余窗口估算。
2. 配置 `--budget_limit` 参数（整数）以设定最大可接受上下文长度，配合 `--model_name` 指定目标模型优化建议。
3. 调用 `context_budget.py --audit` 生成包含相关性、冗余度评分的详细清单，用于审查历史会话质量。
4. 对于文档型任务，可通过读取 `context_budget.py` 文件内的函数库获取预定义的"内存衰减"与"检索召回"算法接口。

### 流程
1. **上下文审计**：扫描当前交互历史，识别低相关性、过期或重复信息（使用审计清单生成器）。
2. **预算核算**：调用 `context_budget.py` 计算当前输入占用的 Token 比例及剩余窗口风险。
3. **信息裁剪**：依据四维度标准（相关性·冗余·预算·衰减）删除不必要节点，实施记忆压缩。
4. **检索优化**：调整 RAG 召回参数与工具编排顺序，确保关键数据被优先加载。
5. **门禁校验**：对新进入的信息进行"上下文门控"检查，防止新 Token 覆盖旧的关键设定。
6. **闭环反馈**：将优化后的上下文结构重新注入模型，并记录本次调整日志用于下一轮参考。

### 证据与安全声明
- 证据：TBD（暂无评测/徽章链接；产生后在此更新实际链接）
- 版本：1.0.1
- 安全：未做独立安全扫描（TBD），结论待补；补全前不作推荐背书。
