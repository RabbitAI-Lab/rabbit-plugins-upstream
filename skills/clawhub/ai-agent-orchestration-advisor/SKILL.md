---
name: AI Agent Orchestration Advisor
description: >
  AI-powered multi-agent framework comparison and selection assistant — analyze use cases,
  compare LangGraph/CrewAI/OpenAI Agents SDK/Claude Agent SDK, generate architecture
  recommendations and starter code. Keywords: multi-agent, agent orchestration, LangGraph,
  CrewAI, OpenAI Agents SDK, Claude Agent SDK, Strands Agents, AutoGen, agent framework
  comparison, AI agent architecture, multi-agent system design, agent SDK, 多智能体,
  智能体编排, 框架对比, 智能体架构.
version: "3.0.1"
---

# AI Agent Orchestration Advisor / 多智能体编排选型顾问

> Your expert co-pilot for designing, selecting, and implementing multi-agent AI systems.
> 面向多智能体系统的选型、架构设计与落地实施：从需求澄清到框架对比、架构拓扑、起步代码、评测护栏与成本测算。

## What This Skill Does

In 2026, the agentic AI ecosystem exploded — LangGraph, CrewAI, AutoGen/AG2, OpenAI Agents SDK, Claude Agent SDK, and Strands Agents all compete for developer mindshare. Picking the wrong framework wastes weeks. This skill helps you:

- **Choose the right framework** for your specific use case (workflow complexity, state management, team size, hosting requirements)
- **Generate architecture diagrams** and data flow specs for multi-agent systems
- **Produce starter code** scaffolds (Python) for the chosen framework
- **Analyze trade-offs** across orchestration patterns (hierarchical, sequential, parallel, event-driven)
- **Design evaluation and guardrails** before go-live, including human-review checkpoints
- **Estimate cost and capacity** per run and per month
- **Debug and optimize** existing multi-agent implementations

## Trigger Words / 触发词

Multi-agent, agent orchestration, LangGraph, CrewAI, AutoGen, AG2, OpenAI Agents SDK, Claude Agent SDK, Strands Agents, 多智能体, 智能体编排, 框架对比, 框架选型, 多代理, 智能体架构, agent framework, which agent framework, compare agent frameworks, build multi-agent system, agentic workflow, 智能体评测, 智能体护栏

## Target Users / 适用人群

- AI engineers building production agent systems
- Data scientists exploring agentic automation
- Product managers scoping agent-based features
- Developers migrating from single LLM to multi-agent pipelines
- **金融行业科技与数据团队**：需同时满足业务交付与合规留痕要求

---

## Ecosystem & Compliance Updates [2026-09-13] / 生态与合规动态

| 类型 | 内容摘要 | 对选型的影响 | 落地动作 | 优先级 |
|-----|---------|-----------|---------|-------|
| 框架成熟度 | LangGraph 状态机路线趋于稳定：状态持久化/长期记忆/错误恢复成为基线能力，企业级部署支持容器编排扩缩容 | 复杂有状态工作流首选评估对象 | 以"状态恢复是否可验证"作为 POC 验收项 | 高 |
| 多智能体协作 | CrewAI 路线强化角色化协作与并行任务编排，连接器生态扩张 | 角色清晰、流程线性的场景上手成本低 | 先用 2-3 个角色做最小闭环 | 高 |
| SDK 竞争 | Claude Agent SDK / OpenAI Agents SDK 在工具调用与上下文利用上各有侧重 | 与既有模型生态绑定程度决定迁移成本 | 以"模型可替换性"评估锁定风险 | 高 |
| 协议生态 | MCP 生态持续扩张，企业内部 MCP 注册表逐步成为基础设施 | 工具接入标准化，减少定制胶水代码 | 建立内部工具注册与权限清单 | 中 |
| 互操作协议 | Agent 间互操作协议（如 A2A 方向）推进，跨系统协作成为议题 | 跨部门/跨厂商协作场景需预留适配层 | 关键接口做抽象层，避免直连 | 中 |
| 长上下文 | 主流模型上下文窗口差异显著，长文档场景成本差异被放大 | 金融长文档场景需按"分片 + 检索"而非全量投喂 | 以 10 万字符文档做成本对照测试 | 中 |
| AI 治理 | 金融机构 AI 应用需满足安全开发与合规使用要求，涉及场景清单、数据来源与人工复核 | Agent 系统需自带留痕与复核环节 | 上线清单中加入治理条目 | 高 |
| 可观测性 | 评测与追踪工具成为生产必备 | 无追踪能力的框架运维成本高 | 选型时把追踪能力纳入打分 | 中 |

> **数据截止**: 2026-09-13 | 来源：各框架官方文档与公开版本说明、协议公开资料、行业公开信息
> **声明**: 以上为生态观察与技术选型参考，框架版本与能力请以官方最新发布为准

**动态解读示例（两类高频场景）**

- **场景A｜框架锁定风险被低估**：团队为快速交付直接把业务逻辑写入某 SDK 的专有抽象层，半年后需要更换模型供应商 → 迁移成本约等于重写。**改进动作**：把"模型调用、工具定义、记忆存储"三类接口做薄抽象层；POC 阶段就验证一次模型替换（换供应商跑同一套评测集）。
- **场景B｜缺失追踪导致问题无法定位**：多智能体跑出错误结论，但未记录中间步骤与工具调用参数 → 无法复盘是检索错、工具错还是生成错。**改进动作**：选型时将"每步输入输出可导出、可回放"列为硬性要求，并在 POC 中导出一次完整调用链。

---

## Step 1 — Understand the Use Case

Ask the user to describe:

- The task or workflow to automate (e.g., "research + summarize + post")
- Number of distinct roles/agents needed
- State persistence requirements (ephemeral vs. persistent)
- Hosting preference (cloud / local / serverless)
- Team's programming experience

### 1.1 Requirement Intake Table / 需求采集表

| 维度 | 关键问题 | 为什么重要 | 常见误判 |
|-----|---------|-----------|---------|
| 任务形态 | 线性流程、分支决策还是开放探索？ | 决定编排模式（顺序/图/事件驱动） | 把线性流程做成多智能体 |
| 角色数量 | 真正需要几个不同职责？ | 角色越多，通信成本与失败点越多 | 为"看起来强大"堆角色 |
| 状态需求 | 是否需要跨会话记忆与断点恢复？ | 决定是否必须有持久化检查点 | 用外部数据库硬凑 |
| 延迟预算 | 单次任务可接受多少秒？ | 多跳调用会线性放大延迟 | 忽略并行化的可行性 |
| 成本上限 | 单次任务可接受成本？ | 角色数与上下文窗口直接放大成本 | 按"每个 Token 单价"估算而非按任务 |
| 部署环境 | 公有云、私有化还是一体机？ | 部分框架/服务在私有化下受限 | 忽略内部网络与数据出域限制 |
| 团队技能 | 团队熟悉 Python 异步与状态管理吗？ | 决定学习曲线是否可承受 | 低估调试成本 |
| 合规要求 | 是否需要留痕、复核、可解释？ | 金融场景为硬性要求 | 上线前才补 |

---

## Step 2 — Framework Shortlist & Comparison

### 2.1 Comparison Table / 框架对比

| Framework | Best For | State Mgmt | Learning Curve | Hosting | Observability | 成本模型 |
|-----------|----------|------------|----------------|---------|--------------|--------|
| LangGraph | Complex stateful workflows | ✅ Built-in | Medium | Any | 强（图级追踪） | 按节点调用计费 |
| CrewAI | Role-based team simulations | Partial | Low | Any | 中 | 按角色任务计费 |
| AutoGen/AG2 | Conversational agent loops | External | Medium | Any | 中 | 按轮次计费 |
| OpenAI Agents SDK | OpenAI ecosystem, handoffs | Built-in | Low | Cloud-first | 中 | 按调用计费 |
| Claude Agent SDK | Anthropic native, tool use | Built-in | Low | Cloud-first | 中 | 按调用计费 |
| Strands Agents | AWS/Bedrock integration | External | Medium | AWS | 依赖云侧 | 按云服务计费 |
| LlamaIndex Workflows | 检索增强类流程 | Built-in | Low | Any | 中 | 按调用计费 |
| Semantic Kernel | .NET/多语言企业栈 | External | Medium | Any | 中 | 按调用计费 |
| 低代码平台（Dify/Coze 类） | 内部工具、快速验证 | Built-in | Very Low | SaaS/私有 | 弱至中 | 按订阅计费 |

### 2.2 Selection Decision Table / 选型决策表

| 情形 | 首选 | 次选 | 理由 |
|-----|------|------|------|
| 有状态、需断点恢复的长流程 | LangGraph | LlamaIndex Workflows | 图结构与检查点是核心诉求 |
| 角色清晰、线性协作 | CrewAI | AutoGen/AG2 | 上手快，角色定义直观 |
| 需要与既有模型生态深度绑定 | 对应厂商 SDK | LangGraph | 官方 SDK 的工具与回退机制更完整 |
| 强检索依赖（知识库问答） | LlamaIndex Workflows | LangGraph | 检索组件成熟 |
| 企业 .NET 技术栈 | Semantic Kernel | LangGraph | 与既有服务栈一致 |
| 快速验证业务想法 | 低代码平台 | CrewAI | 一周内可出可用原型 |
| 私有化 + 强合规留痕 | LangGraph | 自研轻量状态机 | 追踪与持久化可完全自控 |

> **规则**：先用"流程是否有状态 + 是否需要检索 + 部署限制"三个问题筛掉大部分选项，再在剩余的 2-3 个里做 POC 对比。

---

## Step 3 — Architecture Recommendation

Output a recommended architecture including:

- Agent topology (who calls whom)
- Tool assignments per agent
- Memory / state strategy
- Human-in-the-loop checkpoints
- Error handling & fallback patterns

### 3.1 Orchestration Patterns / 编排模式

| 模式 | 适用场景 | 优点 | 风险 | 典型实现 |
|-----|---------|------|------|---------|
| 顺序（Sequential） | 步骤确定的流水线 | 易调试、成本可预测 | 缺乏动态调整能力 | CrewAI Process.sequential |
| 层级（Hierarchical） | 需要主管分配与汇总 | 复杂任务可分工 | 主管节点易成瓶颈 | 主管 Agent + 子 Agent |
| 并行（Parallel） | 多源独立取数/多方案比较 | 降低总延迟 | 结果合并需一致性处理 | 并发任务 + 汇总节点 |
| 事件驱动（Event-driven） | 长时任务、需外部触发 | 解耦、可扩展 | 状态追踪复杂 | 队列 + 状态机 |
| 评审循环（Critic loop） | 质量要求高的产出 | 自我纠错 | 循环失控导致成本飙升 | 生成 + 评审双角色 |

**拓扑示例（层级 + 评审循环）**

```
Coordinator
 ├── Retriever Agent   → 工具：知识库检索
 ├── Analyst Agent     → 工具：结构化计算
 └── Writer Agent      → 工具：文档生成
        ↑
   Critic Agent ── 不通过则回退到对应节点（限 2 轮）
```

### 3.2 Human-in-the-Loop Checkpoints / 人工复核卡点

| 卡点 | 触发条件 | 人工动作 | 留痕要求 |
|-----|---------|---------|---------|
| 外发前 | 产出将对外使用 | 复核事实与表述 | 复核人、时间、版本 |
| 高金额/高风险决策 | 涉及资金或风险判断 | 双人复核 | 双人签字或系统记录 |
| 低置信输出 | 置信度低于阈值 | 转人工处理 | 标注不确定点 |
| 循环失控 | 评审循环超过预设轮数 | 中止并转人工 | 保留循环记录 |

---

## Step 4 — Starter Code Generation

Generate a complete, runnable Python scaffold:

```python
# Example: CrewAI research + report pipeline
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

researcher = Agent(
    role="Senior Research Analyst",
    goal="Uncover cutting-edge developments in {topic}",
    backstory="You are an expert researcher...",
    tools=[search_tool],
    verbose=True
)

writer = Agent(
    role="Technical Writer",
    goal="Craft insightful, accurate reports from research",
    backstory="You transform raw research into executive summaries...",
    verbose=True
)

research_task = Task(
    description="Research {topic} thoroughly...",
    agent=researcher,
    expected_output="Bullet-point research findings"
)

write_task = Task(
    description="Write a 500-word report on the research findings",
    agent=writer,
    expected_output="Polished report with sections"
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff(inputs={"topic": "agentic AI in 2026"})
```

### 4.1 Stateful Skeleton (LangGraph style) / 有状态骨架

```python
from typing import TypedDict

class State(TypedDict):
    query: str
    findings: list
    draft: str
    review_passed: bool
    rounds: int

def route_after_review(state: State) -> str:
    """评审后的路由：通过则结束，未通过且轮次未超限则回退"""
    if state["review_passed"]:
        return "end"
    if state["rounds"] >= 2:
        return "human_review"      # 循环超限 → 转人工，避免无限循环
    return "revise"

# 关键点：
# 1) 检查点持久化，支持中断恢复
# 2) 循环轮次上限，防止成本失控
# 3) 低置信输出走人工复核分支
```

### 4.2 交付物清单 / Deliverables Checklist

- [ ] 架构拓扑图（节点、边、条件路由）
- [ ] 每个 Agent 的职责边界与工具清单
- [ ] 状态结构定义与持久化方案
- [ ] 评审与回退规则（含轮次上限）
- [ ] 人工复核卡点清单
- [ ] 评测集与验收标准

---

## Step 5 — Evaluation & Guardrails / 评测与护栏

### 5.1 Evaluation Dimensions / 评测维度

| 维度 | 指标示例 | 采集方式 | 参考门槛 |
|-----|---------|---------|---------|
| 任务完成率 | 端到端成功比例 | 评测集回放 | ≥85% |
| 事实准确性 | 与可信来源一致的比例 | 抽样核对 | 关键字段 100% |
| 工具调用正确率 | 参数与调用对象正确比例 | 调用日志 | ≥95% |
| 稳定性 | 重复运行结果一致性 | 同输入跑 10 次 | 结论一致 |
| 延迟 | 端到端耗时 | 埋点 | 符合延迟预算 |
| 成本 | 单任务成本 | 用量统计 | 符合成本上限 |
| 可回放性 | 调用链可导出比例 | 追踪系统 | 100% |

### 5.2 Guardrails / 护栏清单

| 护栏 | 实现方式 | 检查点 |
|-----|---------|-------|
| 工具白名单 | 仅注册允许的工具 | 上线前审核 |
| 输入输出过滤 | 敏感信息与不当内容拦截 | 每次调用 |
| 循环上限 | 迭代轮次与总调用数上限 | 运行时 |
| 超时与熔断 | 单步与整体超时 | 运行时 |
| 权限最小化 | 工具按最小权限授权 | 上线前 |
| 数据出域控制 | 敏感数据不出内网 | 架构评审 |
| 全链路留痕 | 输入、输出、参数、人工动作 | 100% |

---

## Step 6 — Cost & Capacity Estimation / 成本与容量测算

| 项目 | 测算口径 | 示例（单任务） |
|-----|---------|-------------|
| 模型调用 | 各角色 Token 用量 × 单价 | 3 角色 × 8K Token |
| 检索调用 | 检索次数 × 单次成本 | 5 次 |
| 外部工具 | 第三方 API 调用次数 | 2 次 |
| 延迟 | 串行跳数 × 单跳耗时 | 4 跳 × 3 秒 |
| 重试开销 | 预计重试率 | +15% |

**示例测算**：一个"检索 + 分析 + 撰写 + 评审"四角色流程，单任务约 4 跳、合计约 3 万 Token；若以固定单价估算，可通过"降低角色数 + 并行取数 + 结果复用"把单任务成本压缩 30%-50%。**测算应基于实测用量，而非按单价线性外推。**

---

## Step 7 — Production Checklist / 生产检查清单

- [ ] Rate limiting & retry logic
- [ ] Observability (LangSmith / Weights & Biases / custom logging)
- [ ] Secrets management (never hardcode API keys)
- [ ] Cost estimation per run
- [ ] Human review gates for high-stakes outputs
- [ ] 状态持久化与中断恢复验证
- [ ] 循环轮次与总调用数上限
- [ ] 工具权限最小化与白名单
- [ ] 数据出域与脱敏策略
- [ ] 评测集与回归测试流程
- [ ] 版本管理与提示词变更记录
- [ ] 故障演练（工具失败、模型超时、返回格式异常）

## Example Interactions

**User:** "I need to build a system where one agent searches the web, another analyzes sentiment, and a third writes a report. Which framework should I use?"

**Skill response:** Recommends CrewAI for its role-based simplicity, provides a 3-agent architecture diagram, generates a complete scaffold with SerperDevTool + OpenAI, and provides a deployment checklist.

**User:** "I'm using LangGraph but my agents keep losing context between nodes. How do I fix state persistence?"

**Skill response:** Explains LangGraph's StateGraph checkpointing, shows how to add a PostgreSQL checkpointer, provides a code fix.

**User:** "我们的投研团队想做一个自动生成行业简报的多智能体系统，但必须可回溯、可人工复核。"

**Skill response:** 推荐"检索 → 分析 → 撰写 + 评审循环"的层级拓扑，给出状态结构与人工复核卡点表，明确要求每步调用链可导出、循环不超过 2 轮，并给出评测维度与门槛建议。

**User:** "多智能体系统上线后成本比预期高 3 倍，怎么排查？"

**Skill response:** 按"角色数 × 跳数 × 上下文长度 × 重试率"拆解，指出常见原因是评审循环无上限、检索结果全量投喂、以及角色冗余；给出三项压缩动作与验证方式。

## Notes & Constraints

- Always surface the **trade-offs**, not just the "winner" — different teams need different frameworks
- Code examples default to Python; mention JS/TS equivalents where available
- For enterprise requirements, flag SOC2 / data residency considerations
- Keep up with the rapidly evolving MCP (Model Context Protocol) and A2A protocol integrations
- Recommend starting simple: single agent → multi-agent only when genuinely needed
- 金融行业落地需额外关注：数据不出域、全链路留痕、人工复核卡点、循环与调用上限
- 框架版本与生态变化快，选型结论应标注评估日期并定期复核
