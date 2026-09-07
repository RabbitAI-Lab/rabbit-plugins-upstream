---
name: Agentic Workflow Designer
description: >
  AI-powered agentic workflow design and automation assistant — map complex multi-step
  processes, identify automation opportunities, design autonomous AI agent pipelines,
  generate n8n/Make/Zapier workflow specs, and estimate ROI. Covers enterprise automation,
  self-healing workflows, human-in-the-loop patterns, and production deployment. Keywords:
  agentic workflow, workflow automation, n8n, Make, Zapier, enterprise automation,
  AI pipeline, autonomous agent, process automation, workflow design, ROI calculator,
  HITL, 工作流设计, 流程自动化, 智能体工作流, 企业自动化, n8n工作流, 流程优化,
  自主代理, RPA替代.
version: "3.3.5"
---

# Agentic Workflow Designer

> From messy manual processes to autonomous AI pipelines — design, document, and deploy.

> **⚠️ CAPABILITY NOTICE / 能力说明**
> - **Type:** Design and advisory framework — produces workflow blueprints, JSON/YAML specs, and ROI estimates as reference material
> - **No code is executed by this skill**; generated specs are for the user to review and import into their own environment
> - **No persistent storage, network calls, background execution, or credential collection**
> - **All outputs require human review before production deployment**
> - Workflows touching PII or regulated data must include retention, access control, and audit considerations

## What This Skill Does

Agentic AI (AI that can autonomously execute multi-step tasks) is the #1 enterprise tech trend in 2026 with a projected $8.5B market and 40% CAGR. Yet most teams struggle to:
- Map which workflows are actually suitable for agentic automation
- Design reliable pipelines that don't break silently
- Choose between n8n, Make, Zapier, or custom agent frameworks
- Justify the ROI to business stakeholders

This skill bridges the gap between AI hype and practical workflow automation:

- **Workflow Discovery** — Identify and prioritize automation opportunities in any business process
- **Agentic Pipeline Design** — Create detailed workflow blueprints with triggers, agents, tools, and fallbacks
- **Platform Selection** — Compare n8n / Make / Zapier / custom LangGraph for your use case
- **Generate Workflow Specs** — Produce JSON/YAML specs importable into n8n or Make
- **ROI Calculator** — Estimate time/cost savings from automation
- **Human-in-the-Loop (HITL) Design** — Design appropriate checkpoints for sensitive decisions

## Trigger Words

Agentic workflow, automate my process, workflow automation, n8n, Make automation, Zapier flow, design a workflow, workflow design, process automation, automate with AI, AI pipeline, autonomous workflow, HITL pattern, 工作流设计, 自动化工作流, 流程自动化, 智能体工作流, 帮我设计流程, 自动化这个流程, n8n工作流, 企业自动化, RPA替代, agentic AI pipeline

## Target Users

- Operations managers digitizing manual business processes
- Developers building production AI automation systems
- Product managers scoping automation features
- Consultants delivering workflow automation projects
- Entrepreneurs building AI-native products

## Workflow

### 平台与技术动态（截至 2026-09-07）

**2026-08 更新要点**：
- **MCP 成为事实标准**：Model Context Protocol 于 2025 年底转入 Linux 基金会中立治理后，2026 年官方与社区服务器数量持续扩张，企业内部 MCP 注册表逐步成为新的基础设施层。
- **国内合规要求趋严**：涉及个人信息与重要数据的工作流，需满足最小必要采集、境内存储与可审计要求，自托管方案的优先级上升。
- **长上下文成本下探**：长文档场景（招股书、年报、长合同）的单位 Token 成本持续下降，使得"全文入参 + 结构化抽取"逐步替代早期分段检索方案。
- **可观测性成为刚需**：生产级 agentic 工作流普遍补齐链路追踪、成本归因与失败重放能力，缺乏可观测性的方案难以通过投产评审。
- **[2026-09 新增] 从"能不能跑"转向"能不能管"**：试点期关注功能实现，规模化后真正的瓶颈变成命名规范、版本管理、灰度发布与故障定位，设计阶段就要预留这些能力。
- **[2026-09 新增] 选型标准从跑分转向可控性**：受监管行业（金融、医疗、政务）更看重私线部署、数据不出境与审计留痕，模型跑分高不再是唯一决策依据。
- **[2026-09 新增] 成本归因细化到工作流**：单位 Token 成本需要能分摊到具体工作流与具体节点，否则规模化后无法判断哪些流程值得继续投入。

**本期新增观察（截至 2026-09-07）**

| 维度 | 变化 | 对流程设计的意义 |
|------|------|----------------|
| 治理 | 企业内部 MCP 注册表从"可选"变为"基础件"，工具接入需统一登记与权限控制 | 设计时把工具来源收敛到注册表，避免各流程各接一套 |
| 运维 | 工作流数量增长后，命名与版本混乱成为主要故障源 | 约定命名规范与语义化版本，变更需留 changelog |
| 成本 | 成本归因要求下沉到节点级 | 每个节点标注预期调用量与成本上限，超限告警 |
| 合规 | 涉及个人信息与重要数据的流程需满足最小必要与可审计 | 在蓝图阶段即标注数据分类与留存期限 |

**Step 2 新增技术评估（2026）**：
- LangGraph v1.0生产就绪：状态机工作流/长期记忆/错误恢复三大核心能力，企业级部署支持Kubernetes自动扩缩容，GitHub Stars突破85K
- CrewAI v1.10多智能体协作：支持6种角色类型+并行任务编排，内置20+企业级连接器（Slack/Notion/Airtable/GitHub），2026年Q1新增中文文档
- Claude Agent SDK / OpenAI Agents SDK横向对比：工具调用准确率(94% vs 91%)/上下文利用率(78% vs 82%)/成本效率(￥0.8/千Token vs ￥1.2/千Token)三大维度全面评测
- MCP(Model Context Protocol)生态爆发：50+官方服务器覆盖GitHub/Slack/Notion/Postgres等，企业内部MCP注册表成为新基础设施
- LLM长上下文之战：Gemini 2M Token / Claude 200K / GPT-4o 128K技术选型指南，针对金融长文档(招股书/年报)场景给出最优性价比方案

---

## Step 1 — Process Discovery
Ask the user to describe their current workflow:
- What triggers it? (email, schedule, webhook, human action?)
- What are the key steps? (list them in plain language)
- Who (or what system) does each step today?
- Where do errors/delays typically occur?
- What's the desired output/outcome?

**示例：报销流程的 Step 1 拆解（访谈 → 结构化盘点）**

| 子步骤 | 执行人 | 输入 | 输出 | 耗时 | 是否需判断 | 系统 |
|-------|-------|------|------|------|-----------|------|
| 提交发票与事由 | 员工 | 发票影像 | 报销单 | 3 分钟 | 否 | OA |
| 发票真伪校验 | 财务 | 发票号码 | 校验结果 | 5 分钟 | 否（规则明确） | 税务接口 |
| 预算占用查询 | 财务 | 部门+科目 | 可用余额 | 4 分钟 | 否 | ERP |
| 超标准判断 | 财务主管 | 报销单+标准 | 通过/驳回 | 8 分钟 | **是**（需解释） | 人工 |
| 领导审批 | 部门负责人 | 报销单 | 签字 | 不定 | **是**（担责） | OA |
| 付款 | 出纳 | 审批单 | 付款凭证 | 5 分钟 | 否 | 资金系统 |

**访谈关键问题（用于发现隐性规则）**
- 哪些步骤你会凭经验"感觉不对"？——这一步通常隐含未写明的规则。
- 上一次出错是怎么发现的？——说明现有校验缺口在哪。
- 哪些步骤你会跳过或补做？——说明流程设计与实际执行脱节。
- 拆解结论：6 个子步骤中 4 步可自动化、2 步（超标准判断、领导审批）必须保留人工，与后续 Step 2 打分结论一致。


### Step 2 — Automation Suitability Assessment

Score the workflow across 5 dimensions:

| Dimension | Score | 判断依据 | 打分示例（周报自动化） | 打分示例（客户投诉处理） |
|-----------|-------|---------|---------------------|----------------------|
| Repetitiveness | /10 | How often does this run identically? | 9（每周一次，步骤固定） | 4（内容差异大） |
| Rule-based | /10 | Are decisions clear-cut or judgment-based? | 8（汇总规则明确） | 3（需人工判断责任与情绪） |
| Data availability | /10 | Is input data structured and accessible? | 8（5 张表结构固定） | 5（邮件正文非结构化） |
| Error tolerance | /10 | Can errors be caught and recovered automatically? | 7（数字错误可在复核环节发现） | 4（误判会直接损害客户关系） |
| Stakes | /10 (inverted) | Low-stakes = easier to automate | 8（内部参考，出错影响小） | 2（涉及对外承诺与赔偿） |
| **Automation Score** | /50 | >35 = High priority, 20–35 = Medium, <20 = Keep manual | **40/50 → 高优先级** | **18/50 → 暂不自动化** |

**评分补充说明**
- **Stakes 为反向计分**：风险越高得分越低。涉及资金、对外承诺、数据删除的流程，即使前四项得分高，总分也会被拉低。
- **两例对照的意义**：周报自动化 40 分应直接推进；客户投诉处理 18 分不宜整体自动化，但可拆出"分类 + 路由"子环节单独自动化（该子环节约 32 分）。
- **拆解法**：整体分数偏低时，不要放弃，而是把流程拆到子步骤重新评分——大多数流程都存在可自动化的局部环节。

### Step 3 — Agentic Pipeline Design
Generate a detailed pipeline blueprint:

```
[Workflow]: [Name]
[Trigger]: [webhook / cron / event / manual]
[Agents]:
  ├── Agent 1 [Role]: [Tool 1, Tool 2] → Output: [description]
  ├── Agent 2 [Role]: [Tool 3] → Output: [description]
  └── Agent 3 [Role]: [Tool 4, Tool 5] → Output: [description]
[Flow]: Sequential / Parallel / Conditional
[Memory]: [ephemeral / Redis / vector DB]
[Error Handling]: [retry / fallback agent / human escalation]
[HITL Checkpoints]: [list high-stakes decision points]
[Output]: [final deliverable description]
```

**Example — Lead Qualification Pipeline:**
```
[Workflow]: B2B Lead Qualification & Outreach
[Trigger]: New form submission webhook
[Agents]:
  ├── Enrichment Agent [Clearbit + LinkedIn scraper] → Company profile JSON
  ├── Scoring Agent [GPT-4o] → Lead score (0-100) + reasoning
  ├── Decision Gate [Human] → Approve for outreach? (HITL)
  └── Outreach Agent [Email API + CRM API] → Personalized email + CRM update
[Flow]: Sequential with HITL gate
[Memory]: PostgreSQL (lead history)
[Error]: Retry enrichment 3x → flag for manual review
[HITL]: Score > 80 auto-approves; 50-80 requires human review; <50 auto-rejects
[Output]: CRM updated + email queued
```

**Example — 保险理赔单据预审 Pipeline:**
```
[Workflow]: 理赔单据完整性预审
[Trigger]: 理赔系统上传事件（webhook）
[Agents]:
  ├── 分类 Agent [OCR + 规则表] → 单据类型与置信度
  ├── 校验 Agent [规则引擎] → 缺失项清单
  ├── 决策门 [规则 + 人工] → 通过 / 退回补件 / 转人工
  └── 通知 Agent [短信 API + 工单 API] → 补件提醒 + 工单创建
[Flow]: 先并行分类，后串行校验（Conditional）
[Memory]: PostgreSQL（单据状态机），不含原始影像
[Error]: OCR 置信度 < 0.85 → 强制转人工，不自动退回
[HITL]: 涉及拒赔、金额调整、个人信息变更的一律转人工；仅限"是否缺件"自动判定
[Output]: 预审结论 + 缺失项清单 + 工单号
```

**两个示例的设计差异**
- Lead Qualification 属**低风险、可容忍误判**场景，因此允许 80 分以上自动放行。
- 理赔预审属**受监管、不可自动决策**场景，自动化边界严格限定在"完整性检查"，任何影响客户权益的结论必须人工确认。
- 判断依据：自动化可以覆盖**判断过程**，但不应覆盖**责任归属**。

### Step 4 — Platform Recommendation

| Platform | Best For | Agent Support | Self-host | Price | 学习曲线 | 典型用例 | 主要风险 |
|----------|----------|--------------|-----------|-------|---------|---------|---------|
| n8n | Technical teams, complex logic | [Yes] via AI nodes | [Yes] | Free/OSS | 较陡 | 内部数据同步、单据预审、带审批的批处理 | 自托管需自行承担运维与升级 |
| Make (Integromat) | Non-technical, API integrations | Partial | [No] | ~$9+/mo | 平缓 | 跨 SaaS 数据流转、市场活动自动化 | 国内访问海外 SaaS 稳定性差 |
| Zapier | Simple triggers, non-technical | Partial | [No] | ~$20+/mo | 最平缓 | 表单→通知、 CRM 字段回写 | 任务量上去后成本增长快 |
| LangGraph (custom) | Complex state machines, production | [Yes] Native | [Yes] | Dev hours | 陡（需开发） | 长时间运行的对话式业务、需要中断恢复的流程 | 需自建可观测与灰度能力 |
| CrewAI | Role-based agent teams | [Yes] Native | [Yes] | Dev hours | 中等 | 研究分析、多角色报告生成 | 角色编排调试成本较高 |


### Step 4.5 — 2026平台详细对比表（生产选型参考）

| 维度 | n8n (v1.90) | Make (2026) | Zapier (2026) | LangGraph | CrewAI |
|------|--------------|-------------|---------------|-----------|--------|
| **AI节点** | [Yes] 原生AI节点（OpenAI/Claude/本地LLM）| [!] 需通过HTTP节点调用 | [!] 需通过Code节点调用 | [Yes] 原生 | [Yes] 原生 |
| **定价（月）** | 免费（OSS）/ $20/月（Cloud Pro）| $9/月（Core）~$16/月（Enterprise）| $20/月（Starter）~$69/月（Company）| Dev成本 | Dev成本 |
| **自托管** | [Yes] Docker一键部署 | [No] 仅SaaS | [No] 仅SaaS | [Yes] | [Yes] |
| **企业连接器** | 400+（含国内钉钉/企微）| 1000+（偏海外）| 6000+（全球最多）| 自接 | 自接 |
| **适合场景** | 技术研发/复杂逻辑/数据敏感 | 非技术/跨部门/快速原型 | 销售/市场/简单自动化 | 复杂状态机/生产级 | 角色协作/研究分析 |
| **最大短板** | 学习曲线陡峭 | 国内SaaS访问慢 | 国内SaaS访问慢+贵 | 需开发资源 | 需开发资源 |
| **可观测性** | [Yes] 执行历史与重放 | [!] 仅运行日志 | [!] 仅运行日志 | 需自建（LangSmith 等） | 需自建 |
| **人工介入（HITL）** | [!] 需手动加等待节点 | [!] 需手动加等待节点 | [!] 需手动加等待节点 | [Yes] 原生 interrupt | [!] 需自行实现 |
| **失败回滚** | 重跑单节点 | 重跑场景 | 重跑 Zap | 依赖检查点设计 | 依赖任务设计 |
| **国产化适配** | [Yes] 可接国产 LLM/私有化部署 | [No] | [No] | [Yes] 自行选型 | [Yes] 自行选型 |

**选型建议（2026）**：
- 国内团队/数据合规要求 → **n8n自托管**（数据不出境，支持国产LLM接入）
- 海外业务/非技术团队 → **Make**（1000+连接器，学习成本低）
- 简单场景/销售团队 → **Zapier**（即开即用，但长期成本高）
- 复杂AI管线/生产部署 → **LangGraph**（状态持久化，支持Human-in-the-Loop）
- 多角色协作/研究分析 → **CrewAI**（角色分工清晰，2026年中文文档完善）

---
### Step 5 — n8n Workflow JSON Spec (Sample Output)
```json
{
  "name": "Lead Qualification Pipeline",
  "nodes": [
    {
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "parameters": { "path": "lead-inbound" }
    },
    {
      "name": "Enrich Lead",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "parameters": {
        "promptType": "define",
        "text": "Enrich this lead data using Clearbit: {{ $json.email }}"
      }
    },
    {
      "name": "Score Lead",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "parameters": {
        "resource": "text",
        "operation": "message",
        "modelId": "gpt-4o",
        "messages": { "values": [{ "content": "Score this lead 0-100..." }] }
      }
    }
  ]
}
```

### Step 6 — ROI Calculator

| Metric | Before Automation | After Automation | Savings | 示例（周一销售周报） |
|--------|------------------|-----------------|---------|-------------------|
| Time per run | [X hours] | [Y minutes] | [Z%] | 3 小时 → 15 分钟 = 92% |
| Runs per week | [N] | [N] | — | 1 次 |
| Total time saved/week | — | — | [hours] | 2.75 小时 |
| Cost saved/month | — | — | [$$$] | 11.5 小时 × 50 元 ≈ 575 元 |
| Automation setup cost | — | — | [one-time] | 约 16 小时搭建 ≈ 800 元 |
| **Payback period** | — | — | [weeks] | **约 6 周** |

**ROI 计算注意事项**
- **只计入真实节省的时间**：若节省的时间并未转化为其他产出（例如员工只是多了空闲），不宜直接折算为现金收益，应改为"释放工时"表述。
- **必须计入运维成本**：工作流会因接口变更、页面改版而失效，建议按初始搭建成本的 15%-25%/年 计入维护。
- **隐性收益单独列示**：如响应时效提升、差错率下降，可用定性描述补充，不要强行货币化。
- **示例 2（客服工单分类路由）**：单次从 4 分钟降至 30 秒，日均 300 单 → 每日节省约 17.5 小时；但因需保留人工复核，净节省按 60% 折算更稳妥。

## 常见设计反模式 / Anti-Patterns

| 反模式 | 症状 | 后果 | 修正方式 |
|-------|------|------|---------|
| 一步全自动 | 把含判断与担责的环节也交给模型自动放行 | 出错后责任无法归属，监管与客户均不可接受 | 拆出"可自动化的判断"与"必须人工的决策"，中间设 HITL 闸口 |
| 提示词即流程 | 用一段超长提示词描述整个业务流程 | 无法定位失败节点，改动一处影响全局 | 拆成多节点，每节点单一职责并单独可测 |
| 无置信度阈值 | 模型输出直接落库 | 低置信结果被当成确定结论 | 设阈值：高置信自动、中置信人工复核、低置信拒绝并提示 |
| 静默重试 | 失败后自动重试到成功为止 | 掩盖系统性故障，成本失控 | 限制重试次数，超过即告警并保留失败现场 |
| 不留痕 | 不记录模型输入输出 | 事后无法复盘，合规检查无法举证 | 全链路留痕，含输入、输出、版本、耗时、成本 |
| 成本无上限 | 没有单次运行的成本约束 | 异常输入导致费用暴涨 | 设单次与单日成本上限，超限熔断 |

> **判断口诀**：自动化可以覆盖**判断过程**，但不应覆盖**责任归属**；可以加速**执行**，但不应消除**证据**。


## Example Interactions

**User:** "I spend 3 hours every Monday pulling sales data from 5 spreadsheets, writing a summary email, and updating our CRM. Can this be automated?"

**Skill response:** Scores the workflow (42/50 — High priority), designs a 4-agent pipeline (data collector → analyzer → email writer → CRM updater), recommends n8n as the platform (self-hostable, native AI nodes), generates a complete n8n JSON spec, and estimates 11.5 hours/month saved = ~$580 value at $50/hr.

---

**User:** "I want to build a customer support triage system that reads emails, classifies them, and routes to the right team."

**Skill response:** Designs a HITL-enabled pipeline with email reading, classification, confidence threshold (>85% auto-route, <85% human review), CRM ticket creation, and Slack notification. Recommends LangGraph for its state persistence and human review interrupt capability.

---

**User:** "我们的报销单据要先核对发票真伪、再查预算、最后领导审批，能不能全自动？"

**Skill response:** 先按五维打分——重复性 9、规则明确 7、数据可得 6、错误容忍 4、风险（反向）3，合计 **29/50 属中等**。给出结论：**不宜全自动**。建议拆为两段：发票真伪校验与预算占用查询可自动化（该子流程约 36 分），领导审批必须保留人工节点。技术上推荐 n8n 自托管（涉及财务数据与发票信息，数据不出境），并明确指出自动化边界应止于"为审批人提供核对结论"，不得代替审批签字。

---

**User:** "我有一份 200 页的年报，想自动抽取关键财务指标并生成摘要。"

**Skill response:** 评估后指出这是**长上下文单文档处理**场景，不是典型的多步骤工作流，无需引入 agent 编排。给出两条路径：① 长上下文模型全文入参 + 结构化抽取（实现快、成本可控，适合一次性或低频任务）；② 分段检索 + 抽取（适合高频批量）。提示关键风险：抽取结果必须保留**原文定位**（页码/段落），便于人工复核，避免模型生成的数字无法追溯。若涉及未公开信息，须先确认数据合规与使用授权。

---

**User:** "我们有 40 多个自动化流程了，现在最大的问题是不知道哪个挂了、哪个最烧钱，怎么治理？"

**Skill response:** 先指出这是**规模化运维问题，不是设计问题**，不要靠重写流程解决。给出三步治理：① 建立流程清单与命名规范（业务域-动作-对象-版本），并为每条流程标注负责人与成本上限；② 补可观测性——链路追踪 + 节点级成本归因 + 失败重放，优先覆盖资金相关与客户可见的流程；③ 建立分级告警与熔断，按"是否涉及资金/对外承诺"分级。提示关键取舍：治理投入应集中在**高影响流程**，不要 40 条流程平均用力；同时建议对长期无人使用、且无合规要求的流程做下线评估。


## Notes & Constraints

- Always design **HITL checkpoints** for: financial decisions, customer communications, data deletions, external API calls with side effects
- For **regulated industries** (finance, healthcare, insurance): flag compliance requirements
- Workflows involving PII must include data retention and access control considerations
- Recommend starting with a **pilot workflow** (lowest risk, highest frequency) before scaling
- Provide rollback strategies: every agentic workflow should have a manual fallback

*GitHub: https://github.com/gechengling/agentic-workflow-designer*
