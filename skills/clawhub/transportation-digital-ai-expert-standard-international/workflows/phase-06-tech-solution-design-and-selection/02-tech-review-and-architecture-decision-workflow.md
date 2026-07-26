# 02 — Technical Review & Architecture Decision Workflow

## 1. Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│             Technical Review & Architecture Decision Map              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │1.Review  │──>│2.Arch.   │──>│3.Special-│──>│4.Decision│        │
│  │  Prep    │   │  Review   │   │  Topic    │   │  Meeting  │        │
│  │  Materials│   │  Compl./ │   │  Sec/Perf/│   │  Decide & │        │
│  │  /Panel  │   │  Bench.   │   │  Integ/Op│   │  Log ADR  │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│       │              │              │              │                │
│       v              v              v              v                │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │5.ADR      │──>│6.Issue    │──>│7.Re-review│──>│8.Close-out│        │
│  │  Archive  │   │  Tracking │   │  Pass/Cond│   │  Archive & │        │
│  │  Decision │   │  Remediate│   │  /Fail    │   │  Handover  │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│                                                                     │
│  Core Deliverables: Architecture Review Report | ADR | Issue Log   │
│    Review Resolution                                                │
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Applicable Scenarios

This workflow provides the quality gate for transportation technical solutions before formal delivery. It covers:

- Internal technical review of solutions (quality gate between design and development)
- Technical evaluation of external vendor solutions
- Decision review for major architecture changes
- Final confirmation of technology selection

## 3. Review Organization

### 3.1 Review Panel Composition

| Role | Headcount | Responsibility | Required skills |
|------|:---:|------|------|
| **Lead reviewer (architect)** | 1 | Chair review / consolidate comments / produce report | Transport + technical architecture ≥8 yrs |
| **Transport domain expert** | 1 | Review business understanding / scenario coverage / functional fit | Transport industry ≥5 yrs |
| **Security architect** | 1 | Review security design / compliance | Security + transport ≥3 yrs |
| **Data architect** | 1 | Review data architecture / data flow / data governance | Big data ≥5 yrs |
| **Infrastructure expert** | 1 | Review deployment / O&M / DR | Cloud / DC / edge ≥5 yrs |
| **Delivery lead** | 1 | Review implementation feasibility / resource realism | Project management ≥5 yrs |
| **Recorder** | 1 | Record review process / consolidate comments | — |

### 3.2 Review Entry Criteria

A solution may enter technical review only if it meets the following:

- [ ] Solution document complete (logical / physical / data / security architectures)
- [ ] Key technology selections have comparative justification with ≥2 candidates
- [ ] Non-functional requirements (performance / security / availability / scalability) have quantified definitions
- [ ] Implementation plan has WBS and resource estimates
- [ ] Solution passed the architect's self-check (using [tools/10-tech-solution-maturity-assessment-tool](../../tools/10-tech-solution-maturity-assessment-tool.md), score ≥ 65)

---

## 4. Architecture Review

### 4.1 Review Dimensions & Criteria

| Dimension | Weight | Checkpoints | Pass standard |
|------|:---:|------|------|
| **Architecture soundness** | 30% | Clear layering / clear responsibilities / low coupling / pattern-compliant | No major architectural defects |
| **Business fit** | 25% | Accurate pain-point understanding / complete scenario coverage / traceable requirements | Core scenario coverage ≥90% |
| **Technical feasibility** | 20% | Sound selection / team capability fit / no "impossible" designs | Key tech risks identified with mitigation |
| **Performance & availability** | 15% | Quantified metrics / capacity plan / HA design | Core scenarios meet performance SLA |
| **Security & compliance** | 10% | Four-layer security / IAM / data security / compliance | Meets ISO/IEC 27001 / NIS2 / critical-infrastructure-protection requirements |

### 4.2 Common Architecture Issues & Responses

| Issue type | Typical symptom | Severity | Handling |
|------|------|:---:|------|
| **Layering violation** | Application-layer logic pushed down to infrastructure layer | High | Redesign / review fails |
| **Single point of failure** | Core service / DB lacks active-active / DR | High | Add redundancy, then re-review |
| **Not scalable** | Performance ceiling near current volume | High | Add horizontal-scale design |
| **Over-coupling** | Changing one module forces changes in five | Medium | Decouple / add interface abstraction |
| **Data-flow defect** | Real-time data into OLAP / historical data into Redis | Medium | Correct storage-engine selection |
| **Over-engineering** | Small project uses large-scale architecture (data mesh + event sourcing, etc.) | Medium | Simplify / trim to need |

### 4.3 Architecture Decision Record (ADR)

Major architecture decisions must be logged in ADR format:

```markdown
# ADR-XXX: [Decision Title]

**Status**: [Proposed / Accepted / Deprecated / Superseded]
**Date**: YYYY-MM-DD
**Decision-makers**: [Name / Role]

## Context
[Why is this decision needed? What is the background?]

## Decision
[What have we decided to do?]

## Options Considered
1. [Option A] — [Summary + pros/cons]
2. [Option B] — [Summary + pros/cons]

## Impact
[What does this decision affect? What must change as a result?]

## Consequences
- Positive: [Benefits gained]
- Negative: [Costs / limits / risks introduced]
- Mitigation: [How to reduce negative consequences]
```

---

## 5. Topic-Specific Reviews

### 5.1 Security Topic Review

| Check item | Review focus | Pass standard |
|------|------|------|
| Network security layering | Are OT / IT / DMZ three layers isolated? | Clear topology and firewall policy |
| Identity & access | MFA? RBAC granularity? | Core systems support MFA + fine-grained RBAC |
| Data security | Data classification? Masking? Encryption? | Documented data classification & grading plan |
| V2X security (if applicable) | SCMS / PKI certificate system? Message signing? | Conforms to V2X SCMS standard (SAE) |
| Security operations | SOC / SIEM / threat intel / incident response? | Documented SecOps plan |

### 5.2 Performance Topic Review

| Check item | Review focus | Reference baseline |
|------|------|:---:|
| Concurrency | Designed throughput vs. peak business (×3 margin) | Signal system >1000 concurrent streams |
| End-to-end latency | Is latency budget allocated per scenario? | Sense → alert <500 ms |
| Storage I/O | Estimated IOPS for mixed R/W scenarios? | — |
| Capacity planning | Is 3-year data growth within expansion headroom? | Storage capacity estimate ×3 yrs |

### 5.3 Integration Topic Review

| Check item | Review focus |
|------|------|
| External system integration list | Are all external systems to integrate listed? |
| Interface standards | Is protocol / format / frequency / auth defined per external interface? |
| Data migration | Is there a legacy-system data-migration plan? |
| Rollback strategy | If integration fails, is there a fallback plan? |

---

## 6. Review Decision

### 6.1 Review Conclusion Types

| Conclusion | Definition | Next action |
|:---:|------|------|
| **Pass** | Meets quality standard; may proceed to next phase | Archive report / proceed to dev or implementation |
| **Conditional pass** | Non-critical issues remain; fix without re-review | Fix by deadline / architect confirms / archive |
| **Re-review** | Critical issues; must fix and re-submit | Fix → re-review (in 1–2 weeks) |
| **Fail** | Fundamental defects; redesign required | Return to solution-design phase |

### 6.2 Issue Severity & Remediation Deadline

| Level | Definition | Example | Deadline |
|:---:|------|------|:---:|
| **Blocking** | System cannot run correctly if unfixed | No DR / core component single point | Not passable until fixed |
| **Critical** | Affects core quality attribute | No quantified performance / missing security design | Resolve before re-review |
| **Minor** | Affects non-core function or future maintainability | Incomplete docs / missing interface defs | Resolve on schedule after conditional pass |
| **Suggestion** | Optional but recommended | More elegant implementation / better tooling | Noted for reference |

---

## 7. ADR Template Library (Common Transport Architecture Decisions)

| ADR No. | Topic | Common options | Recommended direction |
|:---:|------|------|------|
| ADR-001 | Message-queue selection | Kafka vs. Pulsar vs. Redis Streams | Large scale → Kafka; multi-tenant → Pulsar |
| ADR-002 | API gateway selection | Kong vs. APISIX vs. Spring Cloud Gateway | Cloud-native → APISIX; ecosystem → Kong |
| ADR-003 | OLAP engine selection | StarRocks vs. ClickHouse vs. Doris | Federated query → StarRocks; extreme perf → ClickHouse |
| ADR-004 | Real-time vs. batch architecture | Lambda vs. Kappa | Complex offline analytics → Lambda; full real-time → Kappa |
| ADR-005 | OT/IT security isolation | Physical vs. logical (VLAN) vs. micro-segmentation | Safety-critical → physical; general → micro-segmentation |
| ADR-006 | Roadside compute architecture | Centralized MEC vs. distributed IPC vs. hybrid | High perf → MEC; low cost → IPC |
| ADR-007 | DB primary/standby strategy | Master-slave vs. active-active vs. distributed | Mid scale → master-slave; large → distributed |

---

> **Version**: V1.0 | **Date**: 2026-07 | **Applies to**: Technical review of all transportation solutions
