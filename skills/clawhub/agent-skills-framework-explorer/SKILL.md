---
name: "Agent Skills Framework Explorer"
description: "AI-powered assistant for exploring, understanding, and building with AI agent skills frameworks — covers Anthropic agent-skills, OpenAI agent SDKs, LangChain tools, CrewAI protocols, and open-source agent skill marketplaces. Built for AI developers and agent builders. Keywords: agent-skills, AI agent framework, LangChain tools, CrewAI, OpenAI Agents SDK, Claude Agent SDK, agent tool ecosystem, skills marketplace, MCP tools, n8n agent nodes, agent protocol."
version: "1.0.1"
---

# Agent Skills Framework Explorer

## Overview

A comprehensive guide and assistant for navigating the rapidly evolving AI agent skills framework ecosystem. Whether you're exploring addyosmani/agent-skills (40K+ stars), building with Anthropic's Claude Agent SDK, designing multi-agent pipelines with CrewAI/LangGraph, or connecting tools via MCP protocol — this skill helps you understand, compare, and implement the right framework for your use case.

## Triggers

- "compare agent frameworks"
- "how to use agent-skills"
- "build a multi-agent pipeline with [framework]"
- "what is MCP protocol"
- "CrewAI vs LangGraph vs OpenAI Agents SDK"
- "find tools for my agent"
- "agent framework comparison"
- "MCP server setup"
- "AI Agent工具框架对比"
- "多智能体框架选型"

## Workflow

### Step 1: Identify the User's Goal

Determine the primary use case:
- **Framework selection**: Comparing options for a new project
- **Tool integration**: Adding capabilities to an existing agent
- **Multi-agent design**: Orchestrating multiple specialized agents
- **Skills marketplace**: Finding pre-built agent capabilities
- **Protocol understanding**: Learning MCP, Agent Protocol, or other standards
- **Migration**: Moving from one framework to another

### Step 2: Framework Deep Dive

Provide structured comparison and guidance for the relevant framework:

#### Anthropic agent-skills (addyosmani/agent-skills)
- **What it is**: Shell-based skill framework for CLI agents, Claude Code, and GitHub Actions
- **Key concepts**: `skill.yaml` metadata, bash/python/shell execution, skill chaining
- **Use when**: Building CLI tools, automation scripts, developer-facing agents
- **Ecosystem**: 40K+ stars, active community, skill registry at agent-skills.dev
- **Example skill structure**:
  ```
  skill.yaml  (name, triggers, description, tools)
  run.sh     (main execution script)
  references/ (docs, examples)
  ```

#### OpenAI Agents SDK
- **What it is**: Official Python SDK for building multi-agent systems
- **Key concepts**: Handoffs, tracing, guardrails, function calling
- **Use when**: Building customer-facing agents on OpenAI models
- **Best for**: Product teams needing production-ready agents with built-in observability

#### Claude Agent SDK (Anthropic)
- **What it is**: SDK for building Claude-powered agents with tool use
- **Key concepts**: Tools, sessions, context management, computer use
- **Use when**: Deep Claude integration, computer-use agents, complex tool chains

#### LangGraph (LangChain)
- **What it is**: Graph-based framework for cyclical agent workflows
- **Key concepts**: Nodes, edges, state machines, human-in-the-loop
- **Use when**: Complex workflows with branching, loops, and multi-agent coordination

#### CrewAI
- **What it is**: Role-based multi-agent framework
- **Key concepts**: Agents with roles/goals/backstory, task delegation, crew orchestration
- **Use when**: Team-based AI workflows (e.g., research crew, writing crew)
- **Best for**: Business users who want multi-agent without deep coding

#### MCP (Model Context Protocol)
- **What it is**: Open protocol for connecting AI models to external tools
- **Key concepts**: Servers, clients, resources, prompts, tools
- **Ecosystem**: 50+ official and community servers (GitHub, Slack, Postgres, etc.)
- **Use when**: Connecting agents to real-world data and services
- **Reference**: https://modelcontextprotocol.io

#### Per-framework worked examples (2 each)

**agent-skills**
1. *Release-notes bot*: a `run.sh` that diffs two git tags, pipes the diff to the CLI agent, and posts the summary to Slack. No long-running process, no state — ideal for CI.
2. *Repo hygiene sweeper*: scheduled weekly, checks for stale branches and large binaries, opens issues. Fails safe because each run is independent.

**OpenAI Agents SDK**
1. *Support triage with handoffs*: triage agent classifies intent, then hands off to billing / technical / retention specialists; guardrails block prompt-injection from pasted logs.
2. *Traced batch pipeline*: same agent run over 5,000 rows with built-in tracing so every output is auditable — useful when compliance asks "why did it answer that".

**Claude Agent SDK**
1. *Long-context contract review*: sessions + context management let you keep a 200-page policy in context while comparing clauses across versions.
2. *Computer-use back-office*: driving a legacy desktop underwriting terminal that has no API, with an approval gate before any submit action.

**LangGraph**
1. *Underwriting decision graph*: nodes for intake → rules → model score → human approval, with a conditional edge that loops back when documents are missing.
2. *Retry-and-escalate workflow*: explicit state machine for API flakiness, with a bounded retry counter so it can never loop forever.

**CrewAI**
1. *Weekly market-research crew*: Researcher + Analyst + Writer agents with distinct backstories; the writer agent never calls external tools, which keeps the final text grounded.
2. *RFP response crew*: one agent extracts requirements, one maps them to product capabilities, one drafts; a human reviews before send.

**MCP**
1. *One connector, many agents*: expose your internal policy database once as an MCP server; every framework above can then consume it without bespoke integrations.
2. *Least-privilege data access*: give the agent a read-only MCP server with row-level filtering rather than raw database credentials.

### Step 3: Hands-On Implementation

For each framework, provide starter code and best practices:

#### Setting up agent-skills
```bash
# Clone the framework
git clone https://github.com/addyosmani/agent-skills

# Register a new skill
cd agent-skills/skills
npx create-skill my-skill

# skill.yaml example
name: my-skill
triggers:
  - "run my task"
  - "execute my workflow"
description: "A custom agent skill"
tools:
  - bash
  - filesystem
execute: ./run.sh
```

#### Building with CrewAI
```python
from crewai import Agent, Task, Crew

researcher = Agent(
    role="Financial Analyst",
    goal="Research insurance market trends",
    backstory="Expert in insurance data analysis",
    tools=[...],
)

research_task = Task(
    description="Analyze Q1 2026 insurance market trends",
    agent=researcher,
)

crew = Crew(agents=[researcher], tasks=[research_task])
result = crew.kickoff()
```

#### Connecting via MCP
```python
from mcp.client import MCPClient

client = MCPClient()
# Connect to GitHub MCP server
await client.connect("github", token=os.getenv("GITHUB_TOKEN"))
# Use tools from the server
result = await client.call_tool("github", "create_issue", {
    "repo": "owner/repo",
    "title": "Agent-generated task",
})
```

### Step 4: Framework Comparison Matrix

| Criteria | agent-skills | OpenAI Agents SDK | Claude Agent SDK | LangGraph | CrewAI | MCP |
|----------|-------------|-------------------|-----------------|-----------|--------|-----|
| Multi-agent | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Ease of use | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Production-ready | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Customization | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Tool ecosystem | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Observability / tracing | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Human-in-the-loop | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Cost & token control | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| On-prem / data residency | ⭐⭐⭐⭐⭐ | ⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Time to first demo | < 1 h | 2–4 h | 2–4 h | 1–2 d | 1–2 h | 2–4 h |
| Typical failure mode | Shell escaping bugs | Runaway handoffs | Context overflow | Graph debugging pain | Role prompt drift | Server trust/permissions |
| Best for | Dev tools, CLI | Product agents | Claude-native | Complex workflows | Business teams | Tool integration |

**How to read the added rows**

- *Cost & token control*: agent-skills runs deterministic shell steps, so cost is predictable; multi-agent frameworks can multiply token spend by agent count × turns. Always cap `max_turns`.
- *On-prem / data residency*: matters for regulated industries (insurance, banking). Shell-based skills and self-hosted MCP servers keep data local; hosted SDKs usually require an egress review.
- *Typical failure mode*: pick your framework by which failure you are willing to debug — this is more predictive than star counts.

### Step 4b: Scenario → Stack Decision Table

| Scenario | Recommended stack | Why this, not that | Team size | Ops burden | First milestone |
|---|---|---|---|---|---|
| CLI / CI automation, no LLM state | agent-skills alone | No orchestration needed; shell is enough | 1 | Very low | One working `run.sh` in CI |
| Customer-facing chat agent | OpenAI Agents SDK | Built-in tracing + guardrails | 2–4 | Medium | Handoff between 2 agents with traces |
| Deep document / long-context analysis | Claude Agent SDK | Session + context management | 2–3 | Medium | Compare 2 versions of one document |
| Regulated multi-step decisioning | LangGraph + MCP | Explicit state, auditable branches, local data | 3–6 | High | Graph with one human-approval node |
| Business-team prototype, low code | CrewAI | Role prompts instead of graph code | 1–2 | Low | 3-agent crew producing one artifact |
| Connect N internal systems | MCP layer first | Solve integration once, reuse across agents | 1–2 | Medium | One read-only server in production |
| Migration off a bespoke framework | MCP for tools, then swap orchestrator | Tools outlive orchestrators | 2–4 | Medium | Tools extracted and re-used |

### Step 5: Skill Discovery

Help users find pre-built skills for their needs:
1. Search agent-skills.dev registry by category
2. Find MCP servers for specific tools (database, API, etc.)
3. Discover CrewAI templates and Crew templates
4. Identify gaps where a custom skill should be built

## Input/Output Examples

### Example 1: Framework Selection

**Input:**
```
I want to build an AI agent that researches stock trends and writes a weekly report.
Which framework should I use?
```

**Output:**
```
Recommendation: CrewAI + MCP combination

Rationale:
- Research + writing = multi-role workflow → CrewAI's agent delegation shines
- Stock data requires external API tools → MCP for data connections
- Weekly automation → agent-skills for scheduling

Suggested stack:
1. CrewAI crew: Researcher agent (MCP-connected) + Writer agent
2. MCP servers: Financial data API, web search
3. agent-skills: Weekly trigger, report delivery

Implementation path:
Week 1: Set up CrewAI with 2 agents
Week 2: Add MCP financial data tools
Week 3: Deploy via agent-skills scheduler
```

### Example 2: MCP Server Selection

**Input:**
```
I need to connect my agent to PostgreSQL and Slack. Which MCP servers should I use?
```

**Output:**
```
Recommended MCP Servers:

1. PostgreSQL MCP Server
   - npm install @modelcontextprotocol/server-postgres
   - Capabilities: query, schema inspection, backup
   - Config: DATABASE_URL env var

2. Slack MCP Server
   - npm install @modelcontextprotocol/server-slack
   - Capabilities: send messages, read channels, manage threads
   - Config: SLACK_BOT_TOKEN, SLACK_TEAM_ID

Quick setup:
```bash
npx mcp install @modelcontextprotocol/server-postgres
npx mcp install @modelcontextprotocol/server-slack
```

Security note: Store tokens in environment variables, never hardcode.
```

### Example 3: Cost blow-up in a multi-agent crew

**Input:**
```
Our 4-agent crew costs $40 per run. How do we cut it?
```

**Output:**
```
Diagnosis order (cheapest fix first):

1. Turn count, not agent count, is usually the multiplier.
   - Cap max_turns per agent (e.g. 8) and add an explicit "done" condition.
2. Context is re-sent every turn.
   - Drop the full backstory from later turns; move static context into a short system note.
3. Tool results are the hidden cost.
   - Truncate tool output to the fields the agent actually uses; never paste whole web pages.
4. Model tiering.
   - Use a small model for routing/classification agents, a large one only for the writer.
5. Cache identical subtasks.
   - Weekly reports repeat the same lookups; cache by (tool, args, date).

Expected outcome: 3–5x reduction without changing agent roles.
Measure before/after with the framework's own tracing, not with estimates.
```

### Example 4: On-prem deployment for a regulated insurer

**Input:**
```
We cannot send policyholder data to a hosted API. What can we still build?
```

**Output:**
```
Constraints accepted: no external LLM egress, all data stays in the VPC.

Viable stack:
1. Self-hosted / VPC-endpoint model for generation (check your provider's
   data-processing terms before assuming — verify with the vendor).
2. agent-skills for deterministic pre/post processing: redaction, schema
   validation, audit logging. Shell steps never leave the network.
3. MCP servers deployed inside the VPC for policy DB and document store,
   read-only service accounts, row-level filters.
4. LangGraph (or any framework you can self-host) for the decision graph,
   with a mandatory human-approval node before any customer-affecting action.

What to avoid:
- Browser/computer-use agents against internal portals unless explicitly approved
- Writing raw PII into agent memory or trace storage

Audit requirements to design in from day one:
- Immutable trace store (who/which model/which tool/which input hash)
- Per-decision reproducibility: same input → same path, replayable
- Human-override logging

Note: this is architectural guidance, not legal advice. Confirm specifics
against your regulator's latest guidance and your internal data policy.
```

### Example 5: Migration from a bespoke agent framework

**Input:**
```
We built everything on our own framework 2 years ago. Should we migrate?
```

**Output:**
```
Don't migrate the whole thing. Migrate in this order:

Phase 1 — Extract tools to MCP (2–3 weeks)
  Your bespoke tool adapters are the durable asset. Expose them as an MCP
  server. Now any framework can call them. Zero behaviour change.

Phase 2 — Move one low-risk workflow (2 weeks)
  Pick a non-critical, well-understood flow. Rebuild it on the target
  framework. Compare outputs side by side on 100 historical cases.

Phase 3 — Keep both running (ongoing)
  Route traffic by percentage. Don't do a flag day.

Phase 4 — Retire the old path only when the new one has 4 weeks of parity data

Migration kill-criteria (stop and reassess if any hit):
- Output parity below an agreed threshold on the historical set
- Cost per run increases without a capability gain
- The team cannot debug failures without the original authors

Honest answer: if your bespoke framework works and is maintained, the
strongest move is often MCP-only (Phase 1) and nothing else.
```

## Key Frameworks Reference

| Framework | Repository | Stars | Primary Language | License |
|-----------|-----------|-------|-----------------|---------|
| agent-skills | addyosmani/agent-skills | 40K+ | Shell | MIT |
| OpenAI Agents SDK | openai/openai-agents-python | Growing | Python | Apache 2.0 |
| Claude Agent SDK | anthropics/claude-agent-sdk-python | Growing | Python | Apache 2.0 |
| LangGraph | langchain-ai/langgraph | - | Python | MIT |
| CrewAI | crewAIInc/crewAI | - | Python | MIT |
| MCP | modelcontextprotocol/spec | - | Multi | Apache 2.0 |

## Ecosystem Status (as of 2026-09-10)

The agent framework landscape moves fast. Treat every item below as a starting
point to verify, not as settled fact — check each project's official releases
and changelogs before making a decision.

| Area | What to verify before choosing | Why it matters for selection |
|---|---|---|
| MCP governance & spec | Current spec version and governance home | Determines how stable your tool layer is |
| SDK release cadence | Latest release notes of your chosen SDK | Fast-moving SDKs break pinned code |
| Skill registry / marketplace | Whether the registry you rely on is still active | Dead registries strand your skills |
| Model-provider pricing & terms | Current pricing, rate limits, data-processing terms | Drives unit economics and compliance |
| Security scanning of third-party skills | Whether the marketplace scans published skills | Supply-chain risk for agent tooling |

**Recent dynamics (as of 2026-09-10, verify against official sources)**
1. MCP has continued to mature as the de-facto tool-integration layer, with
   governance moving toward a neutral foundation structure — confirm current
   status from the official MCP specification repository before citing it.
2. The centre of gravity has shifted from "which orchestrator" to "which tool
   layer": teams increasingly standardise on MCP first and treat the
   orchestration framework as swappable.
3. Marketplaces for pre-built agent skills have grown, and with them the
   practice of security-scanning published skills before installation —
   treat any third-party skill as untrusted code until reviewed.
4. All version numbers, star counts and repository paths in this document are
   point-in-time; verify against upstream before use.

## Best Practices

1. **Start with the right abstraction level** — agent-skills for CLI tools, CrewAI for business workflows, LangGraph for complex state machines
2. **Use MCP for all external integrations** — it provides a standardized, swappable interface
3. **Combine frameworks** — use CrewAI for orchestration + MCP for tools + agent-skills for deployment
4. **Monitor agent behavior** — all major frameworks support tracing (OpenAI, LangSmith, etc.)
5. **Design for failure** — agents can hallucinate; add guardrails and human-in-the-loop for critical actions

## Changelog

- **1.0.1** (2026-09-10): Extended comparison matrix with 6 new dimensions
  (observability, human-in-the-loop, cost control, data residency, time-to-first-demo,
  typical failure mode). Added per-framework worked examples (2 each). Added
  Scenario → Stack decision table (7 scenarios, 6 columns). Added Examples 3–5
  (cost control, on-prem for regulated industry, migration strategy). Added
  "Ecosystem Status (as of 2026-09-10)" with verification checklist. Corrected
  CrewAI and Claude Agent SDK repository paths.
- **1.0.0** (2026-05-19): Initial version.

**Last Updated**: 2026-09-10
