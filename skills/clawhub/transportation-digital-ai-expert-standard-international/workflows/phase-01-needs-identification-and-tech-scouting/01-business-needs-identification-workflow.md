# 01-Business Needs Identification and Problem Definition Workflow

## I. Workflow Overview

```
+-----------------------------------------------------------------------------+
|              Business Needs Identification & Problem Definition             |
+-----------------------------------------------------------------------------+
|                                                                             |
|  +----------+   +----------+   +----------+   +----------+                  |
|  |1. Business|-->|2. Current |-->|3. Problem  |-->|4. Goal     |          |
|  |  Context &|   |  Research &|   |  Definition|   |  Setting & |          |
|  |  Strategy |   |  Data Gather|   |  Root-Cause|   |  KPI System|          |
|  +----------+   +----------+   +----------+   +----------+                  |
|       |              |              |              |                        |
|       v              v              v              v                        |
|  +----------+   +----------+   +----------+   +----------+                  |
|  |5. Require-|-->|6. Constraint|-->|7. Priority |-->|8. Require- |          |
|  |  ments    |   |  & Risk    |   |  Ranking & |   |  ment      |          |
|  |  Spec &   |   |  Forecasting|  |  Roadmap  |   |  Sign-off  |          |
|  |  Doc      |   |            |   |            |   |  & Baseline|          |
|  +----------+   +----------+   +----------+   +----------+                  |
|                                                                             |
|  Core Deliverables: Business Requirements Specification (BRS) |            |
|  Problem Definition Report | Requirements Priority Matrix                   |
+-----------------------------------------------------------------------------+
```

## II. Applicable Scenarios

This workflow is written from the perspective of a **technology solution provider** and guides how to systematically identify transportation business needs and define the core problems. It applies to:

- Digital-upgrade needs analysis for transport authorities (signal optimization / congestion management / safety management)
- Smart-transformation needs research for transport operators (motorway operations / bus scheduling / port automation)
- Smart-requirements definition for new transport infrastructure (new corridors / new hubs / new port zones)
- Cross-agency transport data-sharing and collaboration needs analysis

## III. Prerequisites

| Input | Source | Description |
|-------|------|------|
| Domain background knowledge | SKILL.md parts I–II | 15 transport modalities + 12 business value chains |
| Organizational strategy docs | Client | Strategic direction and investment priorities |
| Existing system inventory | Client IT dept. | Current system architecture and technology stack |
| Historical project material | Client | Lessons learned from past projects |

---

## IV. Detailed Steps

---

### Step 1: Business Context and Strategy Alignment (Week 1)

**Goal**: Understand the organization's business strategy and ensure digital needs align with strategic direction.

**Inputs**: Organizational strategy documents, industry analysis reports
**Outputs**: Strategy alignment analysis report

**Key activities:**

| Activity | Method | Deliverable |
|------|------|------|
| Strategy interpretation | Read the org's 5-year plan / annual report / board agendas | List of strategic themes |
| Industry benchmarking | Benchmark against peer digital-transformation successes (see SKILL.md case library) | Benchmark gap analysis |
| Modality confirmation | Confirm applicable transport modality (urban road / motorway / rail / port ...) | Modality profile |
| Strategy–digital mapping | Map business-strategy objectives to digital-capability needs | Preliminary digital-needs filter |

**Strategy alignment checklist:**
- [ ] What are the organization's core business objectives? (Safety / Efficiency / Cost / Service / Compliance)
- [ ] What is the role of digitalization in the org's strategy? (Core driver / supporting tool / exploratory direction)
- [ ] What is the digital maturity of industry leaders? (Reference the T-DMM maturity baseline)
- [ ] Strategic urgency of this need? (Regulatory-driven / competition-driven / efficiency-driven / innovation-driven)

---

### Step 2: Current-State Research and Data Collection (Weeks 1–2)

**Goal**: Comprehensively understand the business, system, and data current state.

**Research method matrix:**

| Method | Target | Sample size | Time | Deliverable |
|------|------|:---:|:---:|------|
| Executive interviews | CEO / CTO / Business VP | 3–5 | 1h each | Strategic expectations & constraints |
| Operational-lead interviews | Department managers / domain experts | 5–10 | 1.5h each | Business process & pain points |
| IT interviews | CIO / IT manager / Ops lead | 3–5 | 1h each | System state & technical constraints |
| Field observation | Operators / dispatchers / field staff | 2–3 days | Full day | Actual workflow & hidden needs |
| Data analysis | Business data / system logs / KPI reports | — | 1 week | Quantified state & trends |
| Document review | Process docs / system design docs / ops manuals | — | — | Standardized current state |

**Current-state assessment framework (As-Is Six-Dimension Profile):**

| Dimension | Assessment focus | Score (1–5) |
|------|------|:---:|
| Process maturity | Standardization / automation rate / exception handling | /5 |
| System & technology state | Architecture / stack / technical debt / scalability | /5 |
| Data capability | Collection / quality / governance / utilization | /5 |
| Organization & talent | Digital team size / skill mix / AI capability | /5 |
| Security & compliance | Cybersecurity / data protection / regulatory compliance | /5 |
| Operations capability | Monitoring / alerting / change mgmt / DR | /5 |

---

### Step 3: Problem Definition and Root-Cause Analysis (Weeks 2–3)

**Goal**: Dig from symptoms to root causes and define actionable business problems.

**Problem definition method: 5 Whys + Fishbone + Data Validation**

**Problem definition template:**

```
Problem statement: [One-sentence description of the core problem]
Impact scope: [Affected business domain / users / systems]
Severity: [P0-Critical / P1-Major / P2-Minor]
Frequency: [Continuous / Daily / Weekly / Periodic]
Root-cause analysis:
  Direct cause -> [Surface]
  Mid-level cause -> [Process / System / People]
  Root cause -> [Strategy / Architecture / Data / Organization]
Quantified impact: [Financial loss / efficiency loss / safety impact / user impact]
```

**Common problem patterns in transport:**

| Problem domain | Typical symptom | Common root cause | Digital solution direction |
|------|------|------|------|
| Congestion mgmt | Peak congestion length > X km | Outdated signal timing / slow incident response / data blind spots | AI signal control / incident detection / situational awareness |
| Safety incidents | Accident rate > Y per 100M veh-km | Insufficient sensing / missing early warning / broken coordination | Omni-sensing / risk prediction / V2X safety |
| O&M cost | Maintenance cost growing > Z% annually | Poor planning / weak inspection / misallocated resources | Predictive maintenance / drone inspection / digital twin |
| Data silos | Cross-agency data cannot be shared | Inconsistent standards / unclear ownership / heterogeneous tech | Data platform / standard interfaces / data governance |
| Service experience | High public complaints / NPS < X | Information asymmetry / service gaps / outdated interaction | MaaS / info services / one-stop service |

---

### Step 4: Goal Setting and KPI System (Week 3)

**Goal**: Based on the problem definition, set quantifiable improvement goals and a KPI system.

**Goal-setting principle (SMART-R):**
- Specific, Measurable, Achievable, Relevant, Time-bound, Risk-aware

**Transport digitalization KPI system:**

| KPI category | Core metrics | Target example | Baseline source |
|------|------|------|------|
| Efficiency | Avg. travel time / delay index / green-wave bandwidth utilization | −15–20% | Probe vehicle / ANPR gantry / TomTom–HERE traffic data |
| Safety | Accidents per 100M veh-km / fatalities / incident response time | −10–30% | Authority crash records / emergency dispatch (112/911) |
| Cost saving | Maintenance / energy / labor cost | −10–25% | Financial reports / O&M system |
| Service | Public satisfaction (NPS) / info publish timeliness / complaints | NPS +10 | User surveys / service desk |
| Environment | CO2 emissions / fuel use / clean-energy share | −15–25% | Energy monitoring / carbon accounting |

---

### Step 5: Requirements Specification and Documentation (Weeks 3–4)

**Goal**: Convert research and analysis into a structured Business Requirements Specification (BRS).

**BRS document structure:**
```
1. Document overview (version / scope / terms / references)
2. Business context & strategy alignment
3. Current-state description (As-Is six-dimension profile)
4. Core problems & root-cause analysis
5. Business goals & KPI system
6. Functional requirements (by priority: P0-Must / P1-Should / P2-Could)
  6.1 Core business functions
  6.2 Supporting business functions
  6.3 Data & reporting requirements
  6.4 Integration & interface requirements
7. Non-functional requirements
  7.1 Performance (response time / concurrency / throughput)
  7.2 Availability (SLA / DR / RPO-RTO)
  7.3 Security (security classification / CII protection / data-security level)
  7.4 Scalability (expected growth over next 3–5 years)
8. Constraints & assumptions
9. Acceptance criteria
10. Appendices (interview records / research data / reference docs)
```

---

### Step 6: Constraint Identification and Risk Forecasting (Week 4)

**Goal**: Identify all constraints and forecast potential risks.

**Constraint classification framework:**

| Constraint type | Typical constraint | Impact |
|------|------|------|
| Budget | Annual IT budget cap / funding-source limits | Scope / tech route / phasing strategy |
| Time | Go-live deadline / regulatory window | Delivery strategy / parallelism / MVP scope |
| Technical | Legacy-system compatibility / stack limits / vendor lock-in | Architecture choice / integration / tech route |
| Organizational | IT team size / skill / cross-agency coordination | Build-vs-buy / training / change management |
| Compliance | Security standards / data protection / sector regulation | Security architecture / data governance / audit |
| Operational | 24×7 O&M capability / DR / SLA | Architecture redundancy / O&M tooling / outsourcing |

**Risk forecast matrix (Top 10):**

| Risk | Likelihood | Impact | Level | Mitigation |
|------|:---:|:---:|:---:|------|
| Frequent requirement change | High | Med | 🟡 | Agile iteration + MVP first |
| Data quality below bar | High | High | 🔴 | Front-load data-quality assessment |
| Legacy integration difficulty | Med | High | 🔴 | Early API assessment + middleware |
| Vendor delivery delay | Med | Med | 🟡 | Milestones + penalty clauses |
| Wrong tech selection | Low | High | 🟡 | Tech scouting + PoC validation |
| Insufficient team capability | Med | Med | 🟡 | Training + external advisors + knowledge transfer |
| Security incident | Low | Extreme | 🟡 | Shift-left security + penetration testing |
| O&M complexity exceeds plan | Med | Med | 🟡 | Observability design + automation |

---

### Step 7: Prioritization and Roadmap (Weeks 4–5)

**Goal**: Rank requirements by value / feasibility / urgency and build a phased roadmap.

**Priority evaluation matrix:**

| Req ID | Description | Business value (1–5) | Difficulty (1–5) | Urgency (1–5) | Priority score | Suggested phase |
|:---:|------|:---:|:---:|:---:|:---:|:---:|
| REQ-01 | [Description] | 5 | 3 | 5 | 8.3 | Phase 1 |
| REQ-02 | [Description] | 4 | 4 | 4 | 6.0 | Phase 1 |
| ... | ... | ... | ... | ... | ... | ... |

> **Priority score** = (Value × 2 + Urgency × 1.5 − Difficulty × 1) / 3

**Roadmap phasing:**

| Phase | Horizon | Goal | Key requirements | Expected outcome |
|------|:---:|------|------|------|
| Phase 1: Quick wins | 0–6 mo | Fast results, build confidence | High value + low difficulty | Early KPI improvement |
| Phase 2: Core capability | 6–18 mo | Build core platform capability | High value + medium difficulty | Platform live + core scenarios |
| Phase 3: Deepen & expand | 18–36 mo | Full-scenario coverage + AI deepening | Medium value + med–high difficulty | End-to-end digitalization |
| Phase 4: Innovate & lead | 36 mo+ | Frontier-tech pilots | Forward-looking scenarios | Industry benchmark / innovation |

---

### Step 8: Requirements Confirmation and Baseline Lock (Week 5)

**Goal**: Confirm requirements with all stakeholders and formally lock the baseline.

**Requirements confirmation checklist:**
- [ ] All business stakeholders have reviewed and signed off
- [ ] IT / data / security departments have confirmed technical feasibility
- [ ] Finance / investment department has confirmed budget feasibility
- [ ] Requirements priority has reached consensus
- [ ] Non-functional requirements (SLA / performance / security) have explicit quantified thresholds
- [ ] Acceptance criteria are defined and testable
- [ ] A requirements change-control process is in place

---

## V. Key Considerations

### 5.1 Transport-Specific Points

- **Modality differences are decisive**: Urban road, motorway, rail, and port requirements follow completely different logic — never reuse a template blindly.
- **Safety is always the top priority**: Requirements touching vehicle / flight / train safety must carry the highest reliability bar.
- **Multi-stakeholder coordination**: Transport projects typically involve business, IT, finance, and sector regulators (often public safety / emergency mgmt), making alignment costly.
- **Data is the biggest bottleneck**: For most transport projects the hardest challenge is not technology but data quality, data standards, and data sharing.

### 5.2 Common Anti-Patterns

| Anti-pattern | Symptom | Avoidance |
|------|------|------|
| **Gold-plating** | Chasing maximal feature breadth far beyond actual need | Strictly rank by value / urgency; do "must-haves" first |
| **Technology-pushed** | Pick tech first, then hunt for problems | Stay problem-driven: business problem → technical solution |
| **Dashboard-first** | Chasing a flashy video wall over real business value | Design around the operator's daily work scenarios |
| **Big-bang** | Trying to solve everything in phase one | Phase delivery so each phase has standalone value |

---

## VI. Deliverables List

| Deliverable | Owner | Due | Recipient |
|------|------|:---:|------|
| Strategy alignment analysis report | Business analyst | Wk 1 | Project sponsor |
| As-Is six-dimension current-state assessment | BA + solution architect | Wk 2 | Project team |
| Problem definition & root-cause report | Business analyst | Wk 3 | All stakeholders |
| Business Requirements Specification (BRS) | Business analyst | Wk 4 | Tech team + stakeholders |
| Constraints & risk register | Project manager | Wk 4 | PMO |
| Requirements priority matrix & roadmap | BA + PM | Wk 5 | Decision makers |
| Requirements baseline sign-off | Project manager | Wk 5 | All stakeholders (signed) |

---

> **Version**: V1.0 | **Date**: 2026-07 | **Applies to**: Transport digital solution — needs-identification phase
