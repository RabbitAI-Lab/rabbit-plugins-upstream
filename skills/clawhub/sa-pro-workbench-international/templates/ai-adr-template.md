# AI Selection Architecture Decision Record / AI Selection ADR

> **ADR ID**: AI-ADR-{NNN}
> **Date**: {YYYY-MM-DD}
> **Status**: {Proposed / Accepted / Deprecated / Superseded}
> **Related**: `adr-template.md` (general Architecture Decision Record)

---

## Title

{One sentence describing the AI decision, e.g. "Adopt Multi-Agent Orchestrator-Worker for intelligent assistant" / "RAG engine = PGVector + hybrid retrieval" / "Unify model calls behind an AI Gateway"}

---

## Context

{Background and constraints for this AI decision}

- **Business context**: {Why is AI capability needed? What pain point or presales value?}
- **Technical constraints**: {latency / compliance / privatization / compute / data residency}
- **Cost constraints**: {token/inference budget, self-hosted compute?}
- **Stakeholders**: {client architect / security & compliance / business / end users}

---

## Decision

{State clearly what we decided to do}

**We decided**: {decision content}

**Key selections** (fill/check as applicable):
- Adopt Agent / multi-agent orchestration: {Yes / No; pattern Orchestrator-Worker / Supervisor}
- Model tiered routing: {trigger conditions & fallback for small/mid/large/reasoning models}
- Retrieval strategy (RAG 2.0): {hybrid retrieval / GraphRAG / re-ranking / context compression}
- Vector DB: {Milvus / PGVector / Qdrant / Chroma / other}
- Tool access: {MCP Server/Client / Function Calling / custom plugin}
- Guardrails & evaluation: {Prompt injection defense / jailbreak defense / red teaming / RAGAS threshold}
- Cost red lines: {cost ceiling per answer / per task; budget alert threshold}

---

## Consequences

{Positive and negative effects}

**Positive**:
- {e.g. quality uplift, lower unit cost, compliance achievable}

**Negative / Risks**:
- {e.g. orchestration complexity, need eval regression, inference latency variance}

**Trade-offs & Alternatives**:
- Alternative A: {brief}
- Alternative B: {brief}
- Why current: {rationale}

---

## Evaluation & Review

- **Pre-launch red team result**: {pass / open items}
- **Objective metric thresholds**: {faithfulness ≥ X; answer relevancy ≥ Y}
- **Cost measurement**: {tokens / cost per task}
- **Review point**: {revisit N weeks after launch}
