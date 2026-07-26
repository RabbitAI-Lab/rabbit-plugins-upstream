# 01 — Technical Solution Design Workflow

## 1. Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                 Technical Solution Design Workflow Map                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │1.Requirements│──>│2.Business │──>│3.Architecture│──>│4.Tech      │        │
│  │  Analysis   │   │  Modeling  │   │  Design      │   │  Selection  │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│       │              │              │              │                │
│       v              v              v              v                │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │5.Implement│──>│6.Solution │──>│7.Internal  │──>│8.Finalize  │        │
│  │  Plan &   │   │  Authoring│   │  Review     │   │  & Deliver  │        │
│  │  Res. Est.│   │  & Visual.│   │  & Revise   │   │            │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│                                                                     │
│  Core Deliverables: Requirements Analysis | Architecture Spec      │
│    Tech Selection Report | Implementation Plan | Complete Solution │
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Applicable Scenarios

This workflow governs the design and authoring of transportation technology solutions, covering the full cycle from requirement intake to solution sign-off. It applies to:

- Intelligent transport management platform (ITMP) / integrated transport operation coordination center (TOCC) build-out proposals
- Smart highway / V2X cooperative-intelligent-transport / smart rail / smart port solution proposals
- AI / big-data / digital-twin platform dedicated technical solutions
- System upgrade / replacement / migration technical solutions

## 3. Preconditions and Inputs

| Input | Source | Description |
|-------|--------|-------------|
| Project requirements document (BRD/MRD) | phase-02-current-state-diagnosis-and-maturity | Business needs and objectives |
| Digital maturity assessment report | phase-02-current-state-diagnosis-and-maturity | T-DMM assessment results |
| Technical current-state survey | phase-02-current-state-diagnosis-and-maturity | Existing systems / data / interfaces / constraints |
| Industry standards & regulations | SKILL.md, Part 24 (Standards & Regulations Index) | Applicable standards & regulatory checklist |
| Budget envelope | Client / internal planning | Investment ceiling |

---

## 4. Detailed Step-by-Step

---

### Step 1: Requirements Understanding & Analysis (Week 1)

**Objective**: Develop a deep understanding of business needs; identify explicit and latent requirements.

**Inputs**: BRD, client interview notes, current-state research report
**Outputs**: Requirements analysis document, requirements priority matrix

**Key activities:**

1. **Structured business requirements decomposition**
   - Use the "five-layer business analysis framework" (User → Scenario → Process → Data → System) to decompose layer by layer
   - Identify explicit and latent (implicit) requirements — latent needs are often more critical than explicit ones
   - Annotate the business value behind each requirement

2. **Requirements prioritization**
   | Priority | Definition | Decision criteria |
   |:---:|------|------|
   | P0 | Must implement | Project has no value without it |
   | P1 | Should implement | Core value contributor |
   | P2 | Could implement | Nice-to-have; may be deferred |
   | P3 | Not this phase | Out of scope for this phase; added to roadmap |

3. **Requirement conflict identification**
   - Identify mutually conflicting requirements (e.g., "absolute safety" vs. "peak performance")
   - Propose a balancing approach or advise the client on trade-offs

**Checklist:**
- [ ] Each requirement has a clear business-value statement
- [ ] Latent requirements identified (performance / security / compliance / O&M / extensibility)
- [ ] Requirement priorities confirmed by client / project sponsor
- [ ] Requirement conflicts identified with a resolution approach

---

### Step 2: Business Modeling & Scenario Mapping (Weeks 1–2)

**Objective**: Translate business requirements into designable business scenarios and technical use cases.

**Inputs**: Requirements analysis document
**Outputs**: Scenario card set, business process diagrams, data-flow diagrams

**Key activities:**

1. **Core scenario cards**
   | Scenario ID | Scenario Name | Trigger | Business Process | Frequency | Data Input | System Response | Key Constraint |
   |------|------|------|------|:---:|------|------|------|
   | SC-01 | AM-peak congestion auto-detection | Segment speed < threshold for >5 min | Detect → Confirm → Warn → Diversion → Report | Daily | Radar / video / floating-car | Auto-alert <30 s | False-positive rate <5% |

2. **End-to-end business process modeling**
   - Draw swim-lane process diagrams for key scenarios
   - Annotate data inputs/outputs at each node
   - Identify automation opportunities and human decision points

3. **Data-flow analysis**
   - Map the source → transport → processing → storage → consumption chain for each scenario
   - Annotate data volume / frequency / latency requirement / quality requirement

---

### Step 3: Architecture Design (Weeks 2–4)

**Objective**: Complete the four-layer architecture design (logical / physical / data / security).

**Inputs**: Scenario card set, data-flow diagrams
**Outputs**: Architecture design specification (with diagrams)

**Key activities:**

1. **Logical architecture design**
   - Decompose functional modules by business capability domain
   - Define inter-module interfaces and dependencies
   - Match patterns against the architecture patterns in SKILL.md, Part 10 (Architecture Patterns)

2. **Physical architecture design**
   - Determine deployment nodes (roadside / edge / regional / central / DR)
   - Compute compute / storage / network requirements per node
   - Design high-availability and disaster-recovery (DR) approach

3. **Data architecture design**
   - Data classification (real-time / near-line / offline / archive)
   - Storage engine selection (OLTP / OLAP / time-series / search / cache)
   - Data lifecycle management strategy

4. **Security architecture design**
   - Network security layering (OT / IT / DMZ)
   - Identity & access management
   - Data security and encryption strategy

**Reference architecture patterns (from SKILL.md, Part 10):**
- Event-driven architecture → real-time data-stream processing scenarios
- CQRS (read/write segregation) → high-frequency write + complex query scenarios
- Edge–cloud collaboration → V2X / low-latency control scenarios
- Three-layer digital twin → traffic simulation and decision-making scenarios
- Zero-trust security → OT/IT convergence security scenarios

---

### Step 4: Technology Selection & Comparative Justification (Weeks 3–5)

**Objective**: Select the optimal option for each key technology domain and provide thorough comparative justification.

**Inputs**: Architecture design specification
**Outputs**: Technology selection report

**Key activities:**

1. **Technology domain list**
   | Domain | Candidates | Recommended | Rationale |
   |------|------|------|------|
   | Message queue | Kafka / Pulsar / Redis Streams | Kafka | Mature ecosystem / team experience / best Flink integration |
   | Stream computing | Flink / Spark Streaming / RisingWave | Flink | Strongest CEP / windowing / state management for transport |
   | OLAP engine | StarRocks / ClickHouse / Doris | StarRocks | Blazing-fast queries / federated query / MySQL-compatible |

2. **Comparative justification requirements**
   - Every key selection must have ≥2 candidate options
   - Comparison dimensions: functionality / performance / ecosystem / O&M / cost / team fit / lock-in risk
   - Recommendation rationale must be quantified (not merely "technically advanced")

3. **Make vs. Buy assessment**
   - Core (differentiating) capabilities → build in-house
   - Generic (non-differentiating) capabilities → procure
   - Evaluation criteria: strategic value / build capability / time window / cost

---

### Step 5: Implementation Plan & Resource Estimation (Weeks 4–5)

**Objective**: Produce an executable implementation plan and resource requirements.

**Inputs**: Architecture design specification, technology selection report
**Outputs**: Implementation plan, resource requirements table

**Key activities:**

1. **WBS decomposition**
   | WBS | Work Package | Predecessor | Effort (person-days) | Owner | Deliverable |
   |:---:|------|------|:---:|------|------|
   | 1.1 | Infrastructure deployment | — | 10 | | Environment-ready report |
   | 1.2 | Data ingestion development | 1.1 | 20 | | Data ingestion module |

2. **Phased delivery strategy**
   - Follow the "validate → expand → scale" progressive strategy (see SKILL.md, Part 17)
   - Phase 1 (PoC/MVP) validates core hypotheses
   - Phase 2 expands coverage
   - Phase 3 scales and optimizes

3. **Resource requirements list**
   - Human: role / headcount / skill requirement / engagement period
   - Hardware: servers / storage / network / edge devices
   - Software: licenses / subscriptions / cloud services
   - Data: data procurement / annotation / migration

---

### Step 6: Solution Authoring & Visualization (Weeks 5–6)

**Objective**: Convert design outputs into a professional technical solution document.

**Inputs**: All outputs from the previous five steps
**Outputs**: Complete technical solution document

**Solution structure (see playbooks/04-tech-architecture-design-playbook):**
1. Executive summary (1 page, decision-maker view)
2. Business understanding & requirements analysis
3. Overall architecture design (logical / physical / data / security)
4. Key technology description (with selection rationale)
5. System integration approach
6. Implementation plan & resource requirements
7. Operations approach & SLA
8. Risk assessment & mitigation
9. Reference cases

---

### Step 7: Internal Review & Revision (Weeks 6–7)

**Objective**: Pass internal technical review to ensure solution quality.

**Inputs**: Complete technical solution document
**Outputs**: Review comments, revised solution

**Review roles and focus areas:**
| Review role | Focus | Veto scope |
|------|------|------|
| Solution architect (peer) | Architecture soundness / extensibility | Architecture design |
| Transport domain expert | Business-understanding accuracy / scenario coverage | Business-requirements fit |
| Security architect | Security-design compliance | Security architecture |
| Delivery lead | Implementation feasibility / resource realism | Implementation plan |
| Commercial lead | Cost realism / vendor strategy | Cost estimate |

**Review process:**
1. Pre-review (solution circulated 3 days ahead; reviewers read independently)
2. Review meeting (2–3 hours, chapter-by-chapter discussion; record all comments)
3. Comment triage (must-fix / should-fix / noted-for-reference)
4. Revision & re-review (architect confirms key changes after revision)

---

### Step 8: Solution Finalization & Delivery (Weeks 7–8)

**Objective**: Finalize the solution and deliver to the client or hand off to the next phase.

**Inputs**: Revised solution
**Outputs**: Final solution, solution briefing deck, client Q&A prep

**Delivery checklist:**
- [ ] Technical solution document (final version)
- [ ] Architecture design specification
- [ ] Technology selection report
- [ ] Implementation plan (with resource requirements)
- [ ] Risk assessment report
- [ ] Solution briefing deck (20–30 slides, client view)
- [ ] Client FAQ / Q&A preparation

---

## 5. Deliverables Catalog

| Deliverable | Owner | Completion | Recipient |
|------|------|:---:|------|
| Requirements analysis document | Business analyst | Week 1 | Architect |
| Scenario card set | Business analyst | Week 2 | Architect |
| Architecture design specification | Solution architect | Week 4 | Tech review board |
| Technology selection report | Solution architect | Week 5 | Tech review board |
| Implementation plan | Project manager | Week 5 | PMO |
| Complete technical solution | Solution architect | Week 6 | Internal review board |
| Solution briefing deck | Solution architect | Week 8 | Client / decision-makers |

---

> **Version**: V1.0 | **Date**: 2026-07 | **Applies to**: Transportation technology solution design