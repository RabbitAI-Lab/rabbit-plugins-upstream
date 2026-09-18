---
name: "Agent Governance Assistant"
slug: agent-gov
description: "UPDATED 2026: Covers China AI Agent governance regulations (generative AI regulations), MCP protocol governance implications, and enterprise AI audit frameworks. AI-powered enterprise AI agent governance framework — audit agent behavior, enforce security policies, ensure CBIRC/CFCA compliance, detect shadow AI, and generate governance reports. Built for IT risk managers, compliance officers, and enterprise AI leaders in financial institutions. Keywords: AI agent governance, enterprise AI, agent compliance, AI security policy, CBIRC, CFCA, shadow AI detection, agent audit, Microsoft Agent 365, Copilot Studio, China AI regulation, Agent治理, 企业AI, AI合规, 影子AI检测, AI审计, NFRA AI合规, AI治理."
version: "5.0.1"
---

# Agent Governance Assistant


### AI Agent治理最新动态 [2026-09-18更新]

| 动态类型 | 内容摘要 | 发布时间 | 影响范围 | 治理应对 |
|---------|---------|---------|---------|---------|
| 协议发布 | MCP 2.0正式发布：无状态协议革命，6个SEP驱动无状态化 | 2026-06 | Agent架构/部署模式重大变革 | 无状态化后更依赖外部审计日志，需补齐留痕 |
| 协议发布 | MCP Apps：Server端渲染交互界面（SEP-1865），沙盒iframe安全运行 | 2026-06 | Agent UI/用户体验 | UI侧输出也需纳入内容合规审查 |
| 协议发布 | Tasks扩展：长时运行任务支持，非阻塞式taskHandle | 2026-06 | Agent编排/工作流 | 长时任务的中间状态需可追溯、可中断 |
| 安全更新 | OpenAI Secure MCP Tunnel：零入站端口企业级安全部署 | 2026-06 | 企业Agent安全 | 仍需配合出网管控与身份鉴别 |
| 互操作 | Google A2A与MCP互操作性测试通过（6月12日联合宣布） | 2026-06 | 多Agent协作 | 跨Agent调用链的责任划分需事先约定 |
| 安全更新 | MCP 2.0安全沙箱：权限声明/执行沙箱/审计日志/用户确认 | 2026-06 | Agent安全治理 | 对应零信任架构的四项控制点 |
| **监管路径分化** | G20期间美方主张轻触式AI监管，与欧盟AI法案、中国分类分级治理形成三条不同路径（以官方最新发布为准） | 2026-09-02 | 跨境AI合规 | 跨国机构需按区域分别设定Agent上线门槛 |
| **AI基建国家化** | AI基础设施被定位为国家级基础设施，主权算力与本土应用能力成为政策议题（以官方最新发布为准） | 2026-09-02 | 金融行业AI基建 | 金融机构的自建算力须同步满足数据不出境要求 |

> **数据截止**: 2026-09-18 | 来源：MCP官方规范、Anthropic官方博客、OpenAI公告、G20公开报道
> **声明**: 以上动态供参考，具体以官方最新发布为准

## Overview

A comprehensive AI-powered framework for governing enterprise AI agents — from audit trails and policy enforcement to regulatory compliance and risk reporting. As enterprise AI agents (Microsoft Agent 365, Copilot Studio, custom agents) proliferate, governance has become the #1 blocker to adoption. This skill bridges the gap between AI capability and enterprise control.

## Title

**Enterprise AI Agent Governance Framework** — Audit · Secure · Comply

## Triggers

- "agent governance" / "AI agent管理" / "代理治理"
- "enterprise AI compliance" / "企业AI合规"
- "shadow AI detection" / "影子AI排查"
- "AI policy enforcement" / "AI策略执行"
- "agent audit trail" / "代理审计日志"
- "Microsoft Agent 365 governance" / "Agent 365治理"
- "AI risk report" / "AI风险报告"
- "Copilot Studio compliance" / "Copilot合规"
- "China AI regulation" / "中国AI监管"
- "CBIRC AI guidance" / "银保监会AI指引"

---

### 0. 2026 企业AI Agent治理最新趋势

| 时间 | 动态 | 治理含义 | 落地动作 |
|------|------|---------|---------|
| **2025年7月** | 中国《生成式人工智能服务管理暂行办法》正式施行 | AI Agent服务纳入互联网信息服务管理，算法备案要求扩展至Agent | 建立Agent算法备案台账 |
| **2025年11月** | MCP协议移交Linux Foundation | AI Agent工具集成标准化带来新的审计盲点，需纳入治理范围 | 把MCP工具调用纳入审计范围 |
| **2026年1月** | NFRA召开2026年监管工作会议，AI治理列为重点 | 金融行业AI Agent应用监管框架加速制定 | 预留季度治理报告报送口径 |
| **2026年** | Microsoft Agent 365/Copilot Studio企业大规模部署 | Agent行为审计、数据隔离、权限管控成为合规核心 | 按部门拆分权限矩阵 |
| **2026年** | 影子AI检测升级：从API监控到行为分析 | 传统DLP监控不足，需引入UEBA（用户实体行为分析）技术 | 网络层API监控 + 行为基线双轨 |
| **2026-09** | AI监管路径区域分化（美国轻触式 / 欧盟AI法案 / 中国分类分级） | 同一Agent在不同区域的可用性不同 | 按区域设定差异化上线门槛 |

> **2026年核心治理挑战：** 企业AI Agent数量激增（从10个→100+），传统Agent Inventory已无法满足监管要求。建议采用"零信任Agent架构"——每个Agent独立身份认证、最小权限、数据隔离、完整审计日志。

---


### AI治理最新动态 [2026-09-18更新]

| 动态类型 | 内容摘要 | 发布时间 | 影响范围 | 治理应对 |
|---------|---------|---------|---------|---------|
| 监管发布 | 金融监管总局《关于银行业保险业人工智能安全开发应用的指导意见》从七大方面提出32项意见，AI治理从指导意见走向刚性规章 | 2026-06-18 | 金融机构AI治理框架 | 对照32项意见逐条建立台账 |
| 标准治理 | MCP 2026路线图将治理成熟度列为四大优先方向，Agent协议治理标准化加速 | 2026-06 | Agent治理与工具标准 | 采用L1–L5成熟度自评对齐 |
| 合规重点 | 高风险AI应用场景明确：资金交易、资产评估、信贷审批、承保理赔、风险管理 | 2026-06-18 | AI应用合规审查 | 上述场景一律要求人工复核 |
| **国际治理分化** | G20期间美方主张轻触式监管以保持创新速度，与欧盟AI法案、中国分类分级治理形成三条路径（以官方最新发布为准） | 2026-09-02 | 跨境合规与集团统一策略 | 跨国机构按区域设差异化门槛，底线取最严 |
| **基础设施属性** | AI基础设施被作为国家级基础设施讨论，主权算力与本土应用能力成为政策议题（以官方最新发布为准） | 2026-09-02 | 金融机构AI基建 | 自建算力需同步满足数据不出境与安全要求 |

> **数据截止**: 2026-09-18 | 来源：国家金融监督管理总局、G20公开报道、行业公开信息
> **声明**: 以上动态供参考，具体以官方最新发布为准；
> 涉及具体合规判定时，请以监管机构最新正式文件与机构法务意见为准。

## Workflow

### Phase 1 — Agent Inventory Discovery

**Step 1.1: Scan for Active AI Agents**

Generate a structured inventory of all AI agents in the enterprise environment.

**Input required:**
- List of known AI platforms in use (e.g., Microsoft 365 Copilot, Salesforce Einstein, custom LangChain agents, RPA bots)
- Department ownership mapping
- API endpoints or integration points

**Output: Agent Inventory Table**

| Agent ID | Platform | Owner | Department | Capabilities | Data Access Level | Autonomy | Registered | Last Active |
|----------|----------|-------|------------|--------------|-------------------|----------|-----------|------------|
| AG-001 | Microsoft Agent 365 | IT Admin | Finance | Email drafting, meeting prep | Full mailbox | Advisory | Yes | 2026-05-07 |
| AG-002 | Custom LangChain | Claims Lead | Claims | Document review, fraud flag | Claims data | Semi-auto | No | 2026-09-02 |
| AG-003 | Copilot Studio | Sales Ops | Sales | Lead scoring | CRM data | Advisory | Yes | 2026-09-10 |

> **Autonomy 取值建议**：Advisory（仅建议，人执行）/ Semi-auto（自动执行但可回退）/ Full-auto（自动执行且不可逆）。
> **Registered 为 No 的 Agent 应优先处置**——未注册却在生产运行，是本阶段最常见的高风险项。
> 上表 AG-002 即属于此类：未注册、半自动、且接触理赔数据，应列为 Critical 候选。

**Step 1.2: Classify Agent Risk Level**

Assign risk tier (Low / Medium / High / Critical) based on:
- Data sensitivity (PII, financial, health, IP)
- External interaction (internet, customers, third parties)
- Autonomy level (advisory only → full automation)
- Regulatory exposure (CBIRC, CFCA, personal information protection)

**Risk Classification Matrix:**

| Tier | Criteria | Example | Audit Frequency | 典型失控场景 | 必备控制 |
|------|----------|---------|----------------|-------------|---------|
| Critical | Customer-facing + financial data + high autonomy | AI underwriting agent | Weekly | 自动拒保且无人工复核入口 | 强制人工复核 + 全量留痕 + 可解释文档 |
| High | Internal + sensitive data + medium autonomy | AI claims processor | Monthly | 理赔金额判定错误被直接执行 | 金额阈值触发人工复核 + 抽样质检 |
| Medium | Internal + general data + advisory only | AI meeting summarizer | Quarterly | 会议纪要把敏感信息扩散给无关人员 | 输出范围限制 + 敏感词过滤 |
| Low | Internal + no sensitive data | AI email categorizer | Bi-annual | 误分类导致重要邮件被漏看 | 定期准确率抽查 |

**分级判定举例（本轮新增）**：

| 场景 | 数据 | 面向 | 自主度 | 判定 | 理由 |
|-----|-----|-----|-----|-----|-----|
| 智能核保助手，自动给出核保结论 | 客户健康与财务数据 | 内部+间接面向客户 | Semi-auto | Critical | 涉及承保决策且含敏感个人信息 |
| 理赔材料完整性预检 | 理赔影像件 | 内部 | Semi-auto | High | 敏感数据但可由人工回退 |
| 会议纪要生成 | 内部会议内容 | 内部 | Advisory | Medium | 仅建议、无敏感数据外发 |
| 邮件自动分类 | 邮件元数据 | 内部 | Full-auto | Low | 无敏感数据、后果可恢复 |

---

### Phase 1.5 — 零信任 Agent 架构落地清单（本轮新增）

对应"2026年核心治理挑战"提出的零信任Agent架构，下表把四项原则拆成可验收的控制点。
治理不能停在原则层，**每一项都要能拿出证据**。

| 原则 | 控制点 | 具体措施 | 验收证据 |
|-----|-----|-----|-----|
| 独立身份认证 | Agent 有唯一身份 | 每个Agent分配独立服务主体，禁止共享账号 | Agent注册表 + 身份清单 |
| 最小权限 | 按职能授予 | 数据范围、工具清单、操作类型分别授权 | 权限矩阵与审批记录 |
| 数据隔离 | 跨部门不可见 | 按部门/业务域隔离数据访问，禁止越域读取 | 隔离策略配置截图 + 越权测试记录 |
| 完整审计日志 | 全链路留痕 | 记录提示词、工具调用、输出与人工处置 | 日志样本 + 留存周期说明 |
| 可中断（新增） | 长时任务可中止 | 长时运行任务支持随时中断与回滚 | 中断演练记录 |
| 可解释（新增） | 决策可回溯 | 关键决策输出依据与模型版本 | 可解释性文档 |

**Step 2.1: Define Governance Policies**

Generate tailored governance policies based on enterprise type and regulatory context.

**For China Financial Institutions (CBIRC/CFCA):**
```
POLICY: CFCA-AI-001 — Agent Data Minimization
All AI agents must process only minimum necessary personal data.
Agents cannot retain PII beyond the transaction completion window.
Annual data audit required.

POLICY: CBIRC-AI-007 — Model Transparency
All AI-assisted decisions in underwriting/claims must provide
human-override capability and explainability documentation.

POLICY: AI-ENTERPRISE-003 — Agent Registration
All production AI agents must be registered in the Enterprise
Agent Registry with documented purpose, data scope, and owner.
Unregistered agents are prohibited from accessing customer data.
```

**Step 2.2: Policy Compliance Checker**

For each registered agent, evaluate against all applicable policies.

**Input:** Agent inventory + policy list
**Output:** Compliance gap matrix with severity scores

---

### Phase 3 — Shadow AI Detection

**Step 3.1: Identify Unauthorized Agent Usage**

Scan for signs of shadow AI — employees using personal AI tools on corporate data.

**Detection indicators:**
- Third-party AI API calls from corporate networks (non-approved domains)
- AI tool usage logs in DLP (Data Loss Prevention) systems
- Browser extensions accessing corporate APIs
- Unsanctioned Zapier/Make/n8n workflows connecting to company data

**Output:** Shadow AI Exposure Report

| Finding | Risk Level | Data at Risk | Detection Source | Recommended Action | 复检时限 |
|---------|-----------|-------------|-----------------|-------------------|---------|
| Employee using free ChatGPT API for customer email drafting | CRITICAL | Customer PII + contract terms | 出网API监控（非白名单域名） | Immediate block + compliance training | 24小时内 |
| Unsanctioned n8n workflow syncing CRM to personal AI tool | HIGH | Contact data + deal values | DLP + 集成平台审计 | Replace with approved integration | 7日内 |
| 浏览器插件读取企业OA页面内容 | HIGH | 内部公文与审批信息 | 浏览器扩展清单核查 | 移除插件并加入禁用清单 | 7日内 |
| 部门自建Agent未纳入注册表 | MEDIUM | 视其数据范围而定 | 定期资产盘点比对 | 补登记并补做风险评估 | 30日内 |

**检测指标与对应手段（本轮新增维度）**：

| 检测指标 | 适用手段 | 局限 |
|---------|---------|-----|
| 第三方AI API调用 | 出网流量监控 + 域名白名单 | 加密流量需配合证书策略 |
| AI工具使用日志 | DLP系统 | 覆盖不到未安装客户端的设备 |
| 浏览器扩展访问企业API | 终端管理 + 扩展清单核查 | 需终端管控能力 |
| 未授权自动化工作流 | 集成平台审计日志 | 影子SaaS需单独发现 |
| 行为异常（下载量突增等） | UEBA 行为基线 | 需历史数据积累，误报需调优 |

---

### Phase 3.5 — 治理成熟度自评（本轮新增）

在出具审计报告前，先用五级模型给企业的Agent治理定级，避免"报告很厚、水平很初"的情况。

| 级别 | 名称 | 特征 | 下一步 |
|-----|-----|-----|-----|
| L1 初始 | 无台账 | Agent数量不清、无人负责 | 立即做资产盘点 |
| L2 可重复 | 有台账 | 已登记但无分级、无策略 | 建立风险分级与基础策略 |
| L3 已定义 | 有策略 | 策略成文并覆盖主要Agent | 落地技术控制与审计日志 |
| L4 已管理 | 可度量 | 有合规评分、定期复检 | 引入UEBA与自动化监控 |
| L5 优化 | 持续改进 | 治理指标纳入考核、定期演练 | 红队演练与跨机构对标 |

**举例（如何定级）**：某企业已完成12个Agent登记、有策略文档但无合规评分、无定期复检 → 判为 L3。
其下一步应优先建设"可度量"能力（合规评分卡 + 季度复检），而不是直接上UEBA——
**跳过L4直接上高级工具，往往因缺少基线数据而失效**。

---

### Phase 4 — Audit Trail & Reporting

**Step 4.1: Generate Governance Audit Report**

Produce a structured audit report for internal risk committees and external regulators.

**Report Sections:**
1. Executive Summary (1 page)
2. Agent Inventory & Risk Classification
3. Governance Maturity Level (L1–L5) — 本版新增
4. Policy Compliance Scorecard
5. Shadow AI Findings
6. Open Risks & Remediation Roadmap
7. Appendix: Agent Decision Logs (sample)

**合规评分卡建议权重（本轮新增维度）**：

| 评分项 | 权重 | 评分依据 |
|-----|-----|-----|
| Agent 注册覆盖率 | 20% | 已注册数 / 生产运行总数 |
| 数据最小化落实 | 20% | 抽查Agent实际读取字段是否必要 |
| 人工复核覆盖率 | 20% | 高风险决策中具备人工复核的比例 |
| 审计日志完整性 | 15% | 提示词/工具调用/输出三类留痕是否齐全 |
| 影子AI处置率 | 15% | 已处置发现项 / 总发现项 |
| 复检及时性 | 10% | 按期完成复检的比例 |

**举例**：某企业12个Agent中8个已注册（20分得13.3）、数据最小化抽查达标（20）、
人工复核覆盖高风险决策的一半（20分得10）、日志仅记录输出（15分得5）、
影子AI 3项中已处置1项（15分得5）、复检按期率约70%（10分得7），总分约 **60.3/100**，
对应 L3 偏上、尚未达到 L4。

**Step 4.2: Generate Regulatory Filing**

Format findings as a CBIRC/CFCA-compliant governance disclosure.

---

## Input / Output Examples

### Example 1: Enterprise Agent Audit

**Input:**
```
We have 12 AI agents across Finance, Claims, and Sales departments.
Recent CBIRC guidance requires quarterly AI governance reporting.
We discovered 3 employees using personal AI tools for work tasks.
```

**Output:**
```
## Phase 1: Agent Inventory
[Structured table of 12 agents with risk tiers]

## Phase 2: Policy Gap Analysis
- 4 agents non-compliant with CFCA-AI-001 (data minimization)
- 2 agents lack human-override capability (CBIRC-AI-007)
- 6 agents unregistered (AI-ENTERPRISE-003 violation)

## Phase 3: Shadow AI Findings
[Shadow AI report with 3 findings]

## Phase 4: Compliance Score — 58/100
Recommended actions prioritized by risk.

## Report ready for CBIRC Q2 submission.
```

### Example 2: Microsoft Agent 365 Governance Setup

**Input:**
```
We are deploying Microsoft Agent 365 across 200 users.
IT needs to configure governance controls before go-live.
Finance and Claims departments need different permission levels.
```

**Output:**
```
## Agent 365 Governance Configuration

### Recommended Permission Matrix
| Department | Agent Capabilities | Data Scope | Human-in-Loop | Audit Level |
|------------|-------------------|------------|---------------|-------------|
| Finance | Report generation, variance analysis | Financial data only | Required for >¥100K | Full |
| Claims | Document review, fraud flag | Claims data | Required for >¥10K | Full |
| Sales | Lead scoring, email drafting | CRM data | Advisory only | Standard |

### Governance Policies to Enable
1. Data Loss Prevention (DLP) rules for PII in agent prompts
2. Agent activity logging to Sentinel/Log Analytics
3. Approval workflows for high-stakes agent actions
4. Monthly governance review dashboard

### Shadow AI Pre-emption
Block list: [personal-ai-tool-1.com, ai-tool-free.xyz]
Allow list: [Copilot, Agent 365, approved-vendor-ai.com]
```

### Example 3: 影子AI专项排查（本版新增）

**Input:**
```
监管检查提出影子AI问题。我们只有网络层的出网日志，
没有终端管控，也没有UEBA。怎么在两周内拿出一个可交付的排查结论？
```

**Output:**
```
## 排查策略（按可执行性排序）
第1周：
1. 出网日志按域名聚合，筛出已知AI服务域名与可疑新域名
2. 拉取集成平台（Zapier/Make/n8n）审计日志，找连接企业数据的自动化流程
3. 向各部门发放自查问卷 + 抽查20台终端的浏览器扩展清单

第2周：
4. 对发现项按"数据敏感度 × 使用频率"分级
5. 出报告，明确每项的建议动作与复检时限
6. 同时提出能力缺口：终端管控与UEBA建议列入下一年度预算

## 交付物
- 影子AI Exposure Report（含 Detection Source 与 复检时限 两列）
- 能力缺口说明（说明本次排查的覆盖边界，避免过度承诺）
```

**要点**：只有网络层日志时，**必须显式说明覆盖边界**——未装终端管控的设备和
加密流量中的调用可能未被发现。治理报告宁可写明局限，也不要给出"已全面排查"的结论。

### Example 4: 高风险Agent上线前评审（本版新增）

**Input:**
```
理赔部门要上线一个自动核赔Agent，金额在1万元以下可自动赔付。
需要走什么治理流程？
```

**Output:**
```
## 风险定级：Critical
理由：客户面向 + 理赔敏感数据 + 半自动执行

## 上线前必过六关（对应零信任清单）
1. 独立身份：分配独立服务主体，不与人工账号混用
2. 最小权限：仅可读取理赔必要字段，禁止访问其他业务域
3. 数据隔离：与其他部门数据域隔离
4. 完整留痕：提示词、工具调用、判定依据、赔付结果全部记录
5. 可中断：保留随时暂停自动赔付的开关
6. 可解释：每笔自动赔付需输出判定依据与模型版本

## 人工复核设计
- 1万元以下自动赔付，但按不低于5%比例抽样人工复核
- 出现同一被保险人短期内多次赔付等异常模式时，自动转为人工
- 保留客户申诉与人工重开通道

## 上线后
- 前3个月按 Weekly 审计频率，稳定后可降为 Monthly
```

---

## Notes & Best Practices

1. **Start with inventory before policy.** You cannot govern what you cannot see.
2. **China-specific:** For CBIRC/CFCA regulated entities, always include PIPL (个人信息保护法) compliance in the policy framework. Agents processing insurance claims data are subject to strict data minimization requirements.
3. **Human-in-the-loop is non-negotiable** for any agent making or materially influencing financial decisions.
4. **Shadow AI is the #1 undetected risk** — prioritize network-level API monitoring.
5. **Update agent registry quarterly** — AI agent proliferation is fast; stale inventories create blind spots.
6. **Leverage Microsoft Purview** for data classification feeding into agent governance policies.
7. **Regulatory alignment:** Check current CBIRC AI guidance, CFCA fintech guidelines, and the generative AI regulation framework when generating policies.
8. **先定级再选工具（本版新增）**：成熟度处于 L1–L2 的企业先做台账与分级，不要直接采购UEBA等高级工具；缺少基线数据会让高级工具失效。
9. **写清覆盖边界（本版新增）**：任何排查与评估报告都要明确说明"哪些没查到"，治理报告的可信度来自坦诚的边界说明，而不是全覆盖的承诺。
10. **人工复核要设计阈值而非口号（本版新增）**：把"必须人工复核"落成具体条件（金额、异常模式、客户申诉），否则执行时会被绕过。
11. **长时任务必须可中断（本版新增）**：支持长时运行的Agent要保留随时暂停与回滚的开关，并定期做中断演练。

---

*Author: @gechengling | Skill: agent-governance-assistant | clawhub.ai/gechengling/agent-governance-assistant*
