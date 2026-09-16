---
name: Prompt Engineering Lab
description: >
  AI-powered prompt engineering workbench — write, test, iterate, and optimize prompts
  for any LLM application. Covers the full prompt lifecycle: drafting with proven
  frameworks (Chain-of-Thought, ReAct, Few-Shot, Tree-of-Thought), systematic A/B
  testing, failure analysis, prompt versioning strategy, CI/CD integration, and
  production monitoring. Supports GPT-4o, Claude, Gemini, Llama, Mistral, DeepSeek,
  and open-source models. Built for developers, prompt engineers, and AI product teams
  who need reliable, measurable prompt performance.
  Keywords: prompt engineering, prompt optimization, LLM prompt, chain-of-thought,
  few-shot learning, prompt testing, GPT-4o, Claude prompting, AI prompt design,
  prompt A/B test, system prompt, prompt versioning.
version: "3.0.1"
---

# Prompt Engineering Lab / 提示词工程实验室

**Write better prompts. Ship better AI products.**
**写出更好的提示词，交付更可靠的 AI 产品。**

Prompt engineering in 2026 is no longer just "write something and hope" — it's a
disciplined, measurable engineering practice. This skill is your structured lab for
designing, testing, and optimizing prompts that actually work in production.

---

## What This Skill Does

- **Prompt Drafting** — Apply proven frameworks to write effective prompts from scratch
- **Prompt Diagnosis** — Identify why a prompt produces bad outputs and fix it
- **A/B Testing Design** — Set up structured experiments to compare prompt variants
- **Framework Library** — Chain-of-Thought, ReAct, Tree-of-Thought, Self-Consistency, Structured Output, Reflexion
- **Model-Specific Tuning** — Optimize prompts for specific models (GPT-4o, Claude, Gemini, etc.)
- **System Prompt Architecture** — Design robust system prompts for chatbots and agents
- **Prompt Version Control** — Strategy for managing prompt versions across dev/staging/prod
- **Evaluation Rubric** — Score prompts on clarity, specificity, output format, and edge cases
- **Regression Testing** — Build an eval set and prevent regressions when prompts change
- **Regulated-Industry Guardrails** — Grounding rules, citation requirements, and escalation design

---

## Trigger Phrases

**English:**
- "improve my prompt"
- "why is my prompt not working"
- "write a system prompt for X"
- "chain-of-thought prompt"
- "few-shot examples for Y"
- "optimize prompt for GPT-4o"
- "my AI keeps giving wrong answers"
- "prompt A/B testing"
- "production prompt best practices"
- "prompt engineering tutorial"
- "prompt versioning strategy"
- "how many test cases before calling a winner"

**Chinese / 中文:**
- 提示词优化
- 优化我的 Prompt
- 为什么我的提示词效果不好
- 写一个系统提示词
- 思维链提示词
- Few-Shot 示例
- GPT 提示词技巧
- Claude 提示词最佳实践
- 提示词 A/B 测试
- 大模型提示词工程
- 提示词版本管理
- 如何写出好的 Prompt
- 提示词评测集
- 提示词回归测试
- 模型幻觉怎么控制

---

## Ecosystem & Compliance Updates [2026-09-13] / 生态与合规动态

| 类型 | 内容摘要 | 对提示词实践的影响 | 落地动作 | 优先级 |
|-----|---------|-----------------|---------|-------|
| 模型迭代 | 主流模型版本迭代加快，同一提示词跨版本表现差异明显 | 提示词必须绑定目标模型版本 | 在提示词元信息中记录适用模型与版本 | 高 |
| 结构化输出 | 结构化输出与工具调用能力持续增强，格式约束更可靠 | 输出格式可用 schema 约束替代大段自然语言描述 | 优先用 schema，自然语言只描述语义要求 | 高 |
| 评测工具链 | 提示词评测、追踪与版本管理工具趋于成熟 | 提示词可进入 CI，参与回归测试 | 建立评测集并纳入发布流程 | 高 |
| 安全与红队 | 提示词注入与越狱防护成为上线必查项 | 系统提示需包含注入防护与边界规则 | 上线前执行红队用例集 | 高 |
| 生成内容治理 | 生成合成内容需按规定标识，输出需可追溯 | 提示词需配合标识与留痕机制 | 输出附带标识与版本信息 | 高 |
| 金融等行业合规 | 受监管行业要求人工复核、留痕与不越权表述 | 提示词须内置免责、边界与人工转接规则 | 确立"生成—复核—发布"链路 | 高 |
| 成本与上下文 | 长上下文成本差异被放大，上下文预算需精算 | 少样本示例与系统提示都会占用预算 | 按任务设定上下文预算并监控 | 中 |
| 数据合规 | 输入数据需满足最小必要与去标识要求 | 提示词中不应携带敏感个人信息 | 输入前过滤或脱敏 | 高 |

> **数据截止**: 2026-09-13 | 来源：主流模型与工具官方文档、行业公开信息
> **声明**: 以上为生态与合规观察，模型能力与合规要求请以官方最新发布为准

**动态解读示例（两类高频场景）**

- **场景A｜提示词未绑定模型版本**：团队在一版模型上调优的提示词，模型升级后输出格式开始漂移，测试阶段未发现 → 上线后出现解析失败。**改进动作**：提示词元信息记录"适用模型 + 版本 + 最后验证日期"，模型升级后先跑评测集再放量。
- **场景B｜直接投喂含个人信息的原始文本**：把包含客户姓名与手机号的原始满意度文本直接送入模型 → 违反最小必要原则。**改进动作**：输入前做字段替换与掩码（如"客户A""138****5678"），并在提示词中声明"输入已脱敏"。

---

## Core Workflows

### Workflow 1: Prompt Quality Audit

**Input**: Your existing prompt + model + sample outputs (good and bad)

**Steps**:
1. Score the prompt on 7 dimensions (see rubric below)
2. Identify top 3 failure patterns in sample outputs
3. Generate an improved prompt with annotations explaining each change
4. Provide before/after comparison with expected improvements

#### 1.1 Scoring Rubric / 提示词评分表

| 维度 | 权重 | 满分标准 | 典型失分点 |
|-----|-----|---------|-----------|
| Clarity 清晰度 | 20% | 指令无歧义，动词明确 | "处理一下""优化下" |
| Context 上下文 | 15% | 提供必要背景与输入边界 | 缺少输入来源说明 |
| Constraints 约束 | 15% | 明确"不要做什么" | 只写正向要求 |
| Output Format 输出格式 | 15% | 格式可机器解析 | 只说"用表格"未给列名 |
| Examples 示例 | 10% | 1-3 个高质量示例 | 示例与目标格式不一致 |
| Persona 角色 | 10% | 角色与任务匹配 | 角色泛化（"你是专家"） |
| Edge Cases 边界处理 | 15% | 明确不确定时的行为 | 无"信息不足时如何处理"规则 |

**评级**：≥85 分可直接进入测试；70-84 分建议按低分维度改造；<70 分建议重写。

#### 1.2 Failure Pattern Map / 失败模式对照表

| 现象 | 常见根因 | 修法 |
|-----|---------|------|
| 内容编造 | 未要求"仅依据给定材料" | 增加接地约束与"未提及则说明"规则 |
| 格式漂移 | 格式描述模糊或多重要求冲突 | 用 schema 或给字段清单 |
| 忽略部分指令 | 指令过多且未分节 | 按小节编号，明确优先级 |
| 输出过长/过短 | 无长度约束 | 给出字数或条目数上下限 |
| 立场不稳定 | 无判定标准 | 给出判定规则与优先顺序 |
| 越权给建议 | 未设边界规则 | 明确禁止项与转人工条件 |

### Workflow 2: Prompt from Scratch

**Input**: What you want the AI to do (plain language)

**Steps**:
1. Extract: goal, audience, output format, tone, constraints
2. Select best framework for the use case
3. Draft prompt using structured template
4. Add 2-3 few-shot examples if beneficial
5. Generate 3 variant prompts at different complexity levels
6. Recommend testing approach

### Workflow 3: A/B Test Design

**Input**: Current prompt + hypothesis about improvement

**Steps**:
1. Define your success metric (accuracy, format compliance, user rating, cost per call)
2. Generate 2-4 variant prompts targeting different improvements
3. Design test matrix (how many samples, what inputs to test)
4. Provide analysis template to track results
5. Statistical significance guidance (how many tests before calling a winner)

#### 3.1 Test Design Table / 测试设计表

| 要素 | 设计要求 | 示例 |
|-----|---------|------|
| 成功指标 | 单一主指标 + 1-2 个安全指标 | 主指标：格式合规率；安全指标：事实错误率 |
| 样本量 | 覆盖典型、边界、对抗三类输入 | 每类 ≥20 条 |
| 变量控制 | 一次只改一个维度 | 只改格式段，不动角色段 |
| 判定门槛 | 明确"胜出"标准 | 主指标提升 ≥5 个百分点且安全指标不下降 |
| 复现性 | 固定温度与随机种子 | 记录参数设置 |
| 迭代节奏 | 单轮不叠加多处修改 | 便于归因 |

### Workflow 4: Model-Specific Optimization

**Input**: Current prompt + target model

**Steps**:
1. Explain the target model's known strengths and quirks
2. Apply model-specific best practices
3. Rewrite prompt optimized for that model
4. Flag any behaviors to watch for in that model

### Workflow 5: Production Prompt Architecture

**Input**: Application type (chatbot, RAG assistant, coding tool, data extractor, etc.)

**Steps**:
1. Design system prompt structure (role, context, rules, format)
2. Design user message template
3. Design few-shot injection strategy
4. Handle dynamic context insertion (dates, user info, retrieved docs)
5. Prompt versioning strategy + change management process

#### 5.1 Versioning & Change Management / 版本与变更管理

| 环节 | 要求 | 输出 |
|-----|------|------|
| 版本命名 | 语义化版本，提示词与代码同源管理 | prompt-v1.4.0 |
| 元信息 | 适用模型、版本、最后验证日期、责任人 | 提示词头部注释 |
| 变更流程 | 改动 → 跑评测集 → 灰度 → 放量 | 变更记录 |
| 回滚 | 保留上一可用版本，支持快速回滚 | 回滚预案 |
| 留痕 | 记录每次变更的动机与影响 | 变更日志 |

### Workflow 6: Regression & Go-Live Check / 回归与上线检查

| 检查项 | 标准 | 方式 |
|-------|------|------|
| 评测集覆盖 | 典型/边界/对抗三类齐备 | 用例清单 |
| 回归通过 | 关键指标不低于上一版本 | 自动比对 |
| 注入防护 | 越狱与提示注入用例未突破 | 红队用例集 |
| 敏感信息 | 输入输出均无未脱敏个人信息 | 抽样核查 |
| 免责与边界 | 高风险问题给出边界表述或转人工 | 用例验证 |
| 标识与留痕 | 输出含标识与版本信息 | 抽查 |
| 成本与延迟 | 在预算与延迟目标内 | 用量统计 |

---

## Prompt Framework Reference

### Chain-of-Thought (CoT)
Best for: Multi-step reasoning, math, logical problems
```
Think through this step by step:
[problem]
Before giving your answer, show your reasoning.
```

### ReAct (Reason + Act)
Best for: Tool-calling agents, research tasks
```
For each step:
Thought: [what you're thinking]
Action: [what tool/step to take]
Observation: [what you learned]
...Final Answer: [conclusion]
```

### Few-Shot
Best for: Classification, formatting, domain-specific tasks
```
Here are examples:
Input: [example 1] → Output: [expected 1]
Input: [example 2] → Output: [expected 2]
Input: [example 3] → Output: [expected 3]

Now for this input: [actual input]
```

### Tree-of-Thought (ToT)
Best for: Creative problems, strategy, complex decisions
```
Consider 3 different approaches to this problem:
Approach A: [think through it]
Approach B: [think through it]
Approach C: [think through it]
Now evaluate which approach is best and why.
```

### Self-Consistency
Best for: High-stakes answers where you want to verify
```
Answer this question 3 different ways, using different reasoning paths.
Then identify which answer appears most consistently and explain your confidence.
```

### Persona + Constraint
Best for: Role-playing, expert systems, constrained outputs
```
You are [expert role] with [specific expertise].
Your audience is [who they are].
Your task is [specific task].
Rules: [constraints]
Format your response as: [exact format]
```

### Structured Output / 结构化输出
Best for: 需要机器解析的产出（抽字段、分类、打标）
```
Return JSON matching this schema:
{"field_a": string, "field_b": number, "confidence": number}
Rules:
- If a field is not present in the source, set it to null and list it under "missing".
- Do not invent values.
```

### Reflexion / 自省循环
Best for: 质量要求高、可自动校验的任务
```
Step 1: Produce a draft.
Step 2: List up to 3 specific weaknesses in the draft, citing the requirement each one violates.
Step 3: Revise the draft to fix those weaknesses.
Step 4: If no weakness remains, output the final version; otherwise repeat Step 2 once.
```

---

## Model Quick Reference

| Model | Context | Strengths | Prompting Style | Watch Out For |
|-------|---------|-----------|----------------|--------------|
| GPT-4o | 128K | 代码、结构化输出 | Schema 与分节编号 | 长系统提示下遵循度下降 |
| Claude 3.5/4 | 200K | 长文本分析 | XML 标签分区、格式显式声明 | 过度冗长时需明确长度上限 |
| Gemini 1.5/2 | 至 2M | 多模态、长上下文 | 详细指令 + 分步 | 超长上下文下成本与延迟上升 |
| Llama 3 | 8K-128K | 开源可定制 | 结构需更显式 | 复杂指令易漏项 |
| DeepSeek V4 | 128K | 性价比、代码 | 类 GPT 风格 | 需明确禁止项的表述 |
| Mistral | 32K-128K | 快速、轻量 | 保持简洁 | 长提示易被截断 |

> **提示**：上表为通用经验，实际表现随版本变化；上线前须在目标模型与版本上实测。

---

## Regulated-Industry Prompt Guardrails / 受监管行业的提示词护栏

| 护栏 | 提示词写法 | 验证方式 |
|-----|-----------|---------|
| 接地约束 | "仅依据下方材料作答，材料未提及的须明确说明未提及" | 无材料问答用例 |
| 引用要求 | "每条结论后标注来源编号" | 抽查引用可对齐 |
| 不确定性表达 | "信息不足时输出'无法判断'，不要推测" | 缺信息用例 |
| 禁止越权 | "不提供投资建议、不承诺收益、不判断赔付结果" | 越界问句用例 |
| 转人工条件 | "涉及资金安全、投诉、权限判断时提示转人工" | 触发场景用例 |
| 免责与标识 | 输出附带"仅供参考"与生成方式说明 | 输出格式检查 |
| 数据最小化 | 输入前脱敏，提示词中不携带敏感信息 | 输入抽样 |

---

## Common Prompt Mistakes

1. **Vague instructions** → "Do better" vs. "Rewrite with 20% fewer words, keeping all key facts"
2. **No output format spec** → Always specify: list, JSON, paragraph, table, etc.
3. **No examples** → Add 1-3 examples whenever possible for complex tasks
4. **Too many instructions at once** → Break complex prompts into steps
5. **No persona** → "You are an expert [role]" dramatically improves output quality
6. **Missing constraints** → "Do not include..." is as important as "Include..."
7. **Ignoring context length** → System prompts + few-shot can eat your context budget
8. **No grounding rule** → Without "only use the provided text", models will fill gaps
9. **No version binding** → A prompt tuned on one model version may drift after upgrades
10. **No regression set** → Prompt edits ship without evidence, and failures are discovered in production

---

## Example Interactions

**User**: "My prompt asks GPT-4o to summarize customer feedback but it always makes things up."

**Prompt Engineering Lab**:
> Classic hallucination problem. Here's what's likely happening and how to fix it:
>
> **Root cause**: No constraint to "stay grounded in the provided text"
>
> **Fixes**:
> 1. Add: "Only use information explicitly stated in the feedback below. Do not infer or add information not present in the text."
> 2. Add: "If you're unsure about something, say 'The feedback does not mention this' rather than guessing."
> 3. Add output format: "List up to 5 specific complaints and 3 specific compliments, verbatim where possible."
>
> Want me to rewrite your full prompt with these fixes?

---

**User**: "I'm building a customer support chatbot for an insurance company. How should I design the system prompt?"

**Prompt Engineering Lab**:
> Here's a production-grade system prompt architecture for your use case:
>
> **Structure** (5-section approach):
> 1. **Role & Identity** — Who the bot is, company name, tone
> 2. **Capabilities** — What it can and cannot do
> 3. **Knowledge Scope** — Products it knows about, claim process, FAQs
> 4. **Safety Rules** — Never provide medical/legal advice, always escalate edge cases
> 5. **Output Format** — Response length, language style, escalation triggers
>
> [generates full example system prompt]

---

**User**: "我们想用大模型做监管文件的条款抽取，但抽出来的字段有时是编的，怎么办？"

**Prompt Engineering Lab**:
> 建议按"结构化输出 + 接地约束 + 缺失显式化"三层处理：
> 1. **结构化输出**：给出 JSON schema（条款编号、适用对象、生效日期、confidence）。
> 2. **接地约束**：明确"仅依据原文，不得推断；原文未出现的字段填 null"。
> 3. **缺失显式化**：要求把 null 字段列入 `missing` 数组，便于人工复核。
> 4. **回归验证**：准备 ≥30 条用例（含无该字段的原文），验证是否会出现编造。
>
> 抽取结果须经人工复核后使用，不能直接作为报送依据。

---

**User**: "提示词改了之后效果忽好忽坏，怎么判断到底有没有变好？"

**Prompt Engineering Lab**:
> 这是典型的缺少评测集与判定门槛问题。建议：
> 1. 建立覆盖"典型/边界/对抗"三类、每类 ≥20 条的评测集；
> 2. 只改一个维度、固定参数，避免多处同时改动；
> 3. 主指标提升 ≥5 个百分点且安全指标不下降，才判定为改进；
> 4. 把评测集纳入发布流程，改动即回归，防止新版本引入旧问题。

---

## Target Users

- **AI engineers** building LLM-powered applications
- **Product managers** writing prompts for internal tools
- **Founders** using AI APIs for the first time
- **Data scientists** integrating LLMs into workflows
- **Technical writers** creating AI-assisted content pipelines

---

## Tools Referenced

- **PromptFoo** — open-source prompt testing CLI, red teaming, and CI/CD integration
- **Braintrust** — prompt versioning + evaluation
- **Vellum** — production prompt management
- **LangSmith** — prompt tracing and dataset evaluation
- **PromptHub** — collaborative prompt repository

---

## Notes & Limitations

- Prompt performance varies significantly across model versions — always test on your target model
- This skill provides prompt design guidance, not direct API execution
- For regulated industries (medical, legal, financial), always have prompts reviewed by domain experts
- Prompt optimization is iterative — plan for multiple testing cycles
- Prompts should be treated as versioned artifacts, not ad-hoc strings
- Evaluation sets should be maintained alongside prompts; stale eval sets give false confidence

---

*Better prompts → better AI → better products.*
*Author: @gechengling | version: "3.0.1"*
