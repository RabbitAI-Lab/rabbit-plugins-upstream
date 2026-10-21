---
name: model-router
display_name: 模型路由省成本（Model Router）
display_name_en: "Model Router"
description: "当用户说『全用旗舰模型太贵』『小任务也要排队等大模型』『怎么按难度选模型』『怎么给agent配模型梯队』，或想在不降质前提下把推理成本压下来时使用。按任务复杂度把请求路由到『刚好够用』的模型档位(旗舰/中端/小模型/本地)，附成本对比与回退策略。理论根基：LGD 三律（有籍·有证·有门禁）。触发词：模型路由、model routing、省钱、成本优化、模型梯队、小任务大模型、路由策略、LLM成本。"
version: 1.1.1
agent_created: true
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Edit
category: AI工程方法
platforms: [windows, macos, linux]
platform_compatibility: [windows, macos, linux]
read_when:
  - 所有请求都打旗舰模型，账单飙升
  - 简单分类/抽取/改写也占着大模型队列
  - 想建「旗舰/中端/小/本地」四档梯队按难度分发
  - 用户问「怎么在不降质下省推理钱」
tags: [模型路由, model routing, 成本优化, 模型梯队, LLM成本, agent优化, 省钱]
slug: model-router
title: 模型路由省成本（Model Router）
copyright: SynomosAI
description_zh: "当用户说『全用旗舰模型太贵』『小任务也要排队等大模型』『怎么按难度选模型』『怎么给agent配模型梯队』，或想在不降质前提下把推理成本压下来时使用。按任务复杂度把请求路由到『刚好够用』的模型档位(旗舰/中端/小模型/本地)，附成本对比与回退策略。理论根基：LGD 三律（有籍·有证·有门禁）。触发词：模型路由、model routing、省钱、成本优化、模型梯队、小任务大模型、路由策略、LLM成本。"
description_en: "Route requests to just-enough model tiers (flagship, mid, small, local) by task complexity to cut inference cost without quality collapse."
classification:
  skillhub: ["security-compliance"]
  iso_25010: ["Security"]
risk_tier: medium
risk_rationale: "门禁批量补丁默认 medium（内部约定：本 skill 设计为中等风险）：调用 API/读写文件/本地执行，最小权限，密钥走 Secret；若实际涉对外代执行(push/发布/发送/上架)须人工复评，改 high 并走负责人批准。"
ai_protocol: true
spec: usk/1.0
interface:
  type: cli
  entry_point: scripts/model_router.py
  runtime: python3
  call_pattern: args
input_schema:
  task:
    type: string
    description: "task"
    required: true
  json:
    type: bool
    description: "json"
    required: false
output_schema:
  stdout: 结构化 JSON IR（含 result / rc / error_code / warnings）
  exit_code: rc=0 正常 / rc=1 告警或从严推定 / rc=2 输入不足或非法
capabilities:
  - llm
  - routing
  - cost
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
Use this skill when the user explicitly says large-model costs are too high, requests queue behind big models, or the user is pursuing cost optimization. It also applies when the conversation concerns choosing model tiers by task complexity or configuring an agent's model lineup, and the default routing logic has not already kicked in. Trigger on keywords such as "small task on big model", "save money" or specific LLM routing-strategy needs, whenever there is an implicit quality bar for reasoning.

### Usage
Invoke `model_router.py` directly from Python, passing a JSON-formatted `request_payload` containing `task_type`, `complexity_score` and `budget_limit`. Alternatively, activate the internal module via natural-language triggers such as "model routing" or "cost optimization". The system reads the configuration automatically and outputs the recommended tier together with a fallback plan.

### Workflow
1. Identify user intent and parse keywords and context.
2. Estimate task complexity and resource demand, and build a cost-assessment matrix.
3. Match the "flagship / mid / small / local" tier per the LGD Three Laws.
4. Compute the cost-performance of each model tier and produce a comparison report.
5. Choose the primary target model and the backup degradation strategy.
6. Execute the call and monitor output quality; notify the user when the fallback mechanism triggers.

### Evidence & safety statement
- Evidence: TBD (no evaluation / badge link yet; update here once produced)
- Version: 1.1.1
- Safety: no independent security scan has been performed (TBD); the conclusion is pending and no endorsement is given until it is completed.

## 中文

### 何时用
用户明确表达大模型费用过高、排队等待或追求成本优化时。当对话涉及如何按任务复杂度选择模型梯队或配置 Agent 模型组合，且未触发默认路由逻辑时。检测到关键词如「小任务大模型」「省钱」或特定 LLM 路由策略需求，同时存在对质询/推理质量有隐性要求时。

### 用法
支持 Python 脚本直接调用 `model_router.py`，传入 JSON 格式的 `request_payload` 参数包含 `task_type`, `complexity_score`, `budget_limit`。或通过自然语言触发指令「模型路由」「成本优化」来激活内部模块。系统自动读取配置并输出推荐档位与回退方案。

### 流程
1. 用户输入意图识别，解析关键词与上下文语境。
2. 估算任务复杂度与资源需求，建立成本评估矩阵。
3. 依据 LGD 三律匹配「旗舰/中端/小模型/本地」档位。
4. 计算不同模型的推理性价比并生成对比报告。
5. 确定主路由目标模型与备用降级策略。
6. 执行调用并监控输出质量，触发回退机制时通知用户。

### 证据与安全声明

- 证据：TBD（暂无评测/徽章链接；产生后在此更新实际链接）
- 版本：1.1.1
- 安全：未做独立安全扫描（TBD），结论待补；补全前不作推荐背书。
