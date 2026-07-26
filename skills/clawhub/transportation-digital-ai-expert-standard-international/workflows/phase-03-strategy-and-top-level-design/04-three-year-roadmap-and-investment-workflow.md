# 04-Three-Year Roadmap and Investment Plan Workflow

## I. Workflow Overview

```
+-----------------------------------------------------------------------------+
|            Three-Year Roadmap & Investment Plan Workflow                 |
+-----------------------------------------------------------------------------+
|                                                                             |
|  +----------+   +----------+   +----------+   +----------+                  |
|  |1. Project|-->|2. Depende|-->|3. Invest.|-->|4. Resource|               |
|  |  Inventory|  |  ncy     |   |  Estimate|   |  Plan    |               |
|  | Analysis |   |  Analysis|   |  & Author|   |  & Config|     |
|  +----------+   +----------+   +----------+   +----------+                  |
|       |              |              |              |                        |
|       v              v              v              v                        |
|  +----------+   +----------+   +----------+   +----------+                  |
|  |5. Roadmap|-->|6. Benefit|-->|7. Risk   |-->|8. Review |               |
|  |  Author  |   |  Analysis|   |  Plan    |   |  & Release|              |
|  +----------+   +----------+   +----------+   +----------+                  |
|                                                                             |
|  Method: Value-driven ranking | Dependency-network | TCO | Monte-Carlo     |
+-----------------------------------------------------------------------------+
```

## II. Applicable Scenarios

This workflow applies to authoring a 3-year digital-transformation roadmap and the supporting investment plan for transport-sector clients, supporting investment decisions, annual-budget requests, and public-sector approvals.

## III. Prerequisites and Inputs

| Input | Source |
|-------|------|
| Strategic goals & KPI system | Phase 03-01 |
| Business & application architecture | Phase 03-02 |
| Data & technology architecture | Phase 03-03 |
| Improvement-opportunity list (incl. quick wins) | Phase 02-04 |
| Client budget constraints & funding sources | Client |

---

## IV. Detailed Steps

---

### Step 1: Project Inventory

**Goal**: Convert architecture design and opportunities into an executable project list.

**Inputs**: Architecture docs, opportunity list
**Outputs**: Full project list, project cards

**Guidance:**

**1.1 Project decomposition logic**

```
Strategy goal → Program → Project → Sub-Project

Example:
SG-01: Build region-wide, second-level-response sensing system
  └─ Program-01: Network-sensing system build
       ├─ Project-01-01: Field-sensing device fill-in
       │   ├─ New video points ×200
       │   ├─ Upgrade legacy cameras ×300
       │   └─ Deploy mmWave radar ×50
       ├─ Project-01-02: Video-AI analysis platform
       │   ├─ AI model training & deployment
       │   ├─ Video-analysis platform dev
       │   └─ Cloud-edge framework
       ├─ Project-01-03: Multi-source data-fusion platform
       │   ├─ Ingestion standardization
       │   ├─ Fusion-algorithm dev
       │   └─ Situational common-operating-picture
       └─ Project-01-04: Network-ops monitoring platform
           ├─ Ops-monitoring module
           ├─ Alert-publishing module
           └─ Mobile app
```

**1.2 Project-card template**

```
Project card:

ID: P-01-02
Name: Video-AI analysis platform
Program: Program-01 Network sensing
Goal: Build a unified video-AI platform for automated traffic-incident detection
Key deliverables: AI platform + 10 transport-scenario models + API service
Duration: 12 months
Investment: $1.1M
Predecessors: P-01-01 (device fill-in), P-00-01 (cloud-platform expansion)
Business value: Auto-detection 30%→85%; save 5,000 manual-inspection hrs/yr
Tech approach: Cloud training + edge inference, K8s deploy, elastic GPU
Priority: P0 (highest)
Phasing: Phase 1 / M1-6 (base + 4 models), Phase 2 / M7-12 (6 models + optimize)
```

---

### Step 2: Dependency Analysis and Ranking

**Goal**: Analyze inter-project dependencies and rank scientifically.

**Inputs**: Full project list
**Outputs**: Dependency graph, ranking, phasing suggestions

**Guidance:**

**2.1 Dependency types**

| Type | Description | Example |
|---------|------|---------|
| Technical predecessor | A is the technical prerequisite for B | Cloud before app projects |
| Data predecessor | A feeds data to B | Sensing devices feed AI platform |
| Business predecessor | A's process is B's input | Process mapping before system dev |
| Resource dependency | A and B share key resources | Same AI team on multiple projects |

**2.2 Ranking — weighted scoring**

| Dimension | Weight | Score (1–5) |
|---------|:---:|------|
| Strategy alignment | 25% | Contribution to strategy goals |
| Business value | 25% | Quantified direct/indirect benefit |
| Urgency | 15% | Regulatory / KPI / safety deadline |
| Feasibility | 15% | Tech maturity + org readiness |
| ROI ratio | 10% | Annual ROI estimate |
| Risk control | 10% | Tech / org / regulatory risk |

**Rank score = Σ(dimension score × weight)**

**2.3 Dependency-network analysis**

```
Dependency network example:

Cloud base platform ─┬─> Data platform ─┬─> AI platform ─> Smart apps (phase 2)
(P-00)              │    (P-02)       │    (P-04)     (P-06, P-07)
                    │                 │
                    ├─> Unified portal ┼─> Ops-monitoring
                    │    (P-01)       │    (P-03)
                    │                 │
                    └─> IoT platform ┴─> Maintenance-mgmt
                         (P-05)          (P-05)

Critical path: P-00 → P-02 → P-04 → P-06 (longest dependency chain)
```

---

### Step 3: Investment Estimation and Authoring

**Goal**: Scientifically estimate each project's investment and author the plan.

**Inputs**: Project list, project cards
**Outputs**: Investment-estimate table, annual investment plan

**Guidance:**

**3.1 Three-level estimation method**

```
Three-level investment estimation:

Level 1: Analogous (±30%)
  Use: early planning
  Method: reference actual investment of similar-scale projects

Level 2: Parametric (±20%)
  Use: project-definition stage
  Method: function points / data volume / users × unit price

Level 3: Bottom-up (±10%)
  Use: after detailed design
  Method: WBS to work-package level, sum estimates
```

**3.2 Investment composition template**

| Cost category | Sub-class | Y1 | Y2 | Y3 | Total |
|---------|------|-------:|-------:|-------:|-----:|
| Software platform | App dev | | | | |
| | Product procurement | | | | |
| | Data governance | | | | |
| Hardware | Servers / storage | | | | |
| | Network equipment | | | | |
| | Field devices | | | | |
| Consulting | Planning / design | | | | |
| | Project mgmt | | | | |
| | Supervision / assessment | | | | |
| Implementation | System integration | | | | |
| | Data migration | | | | |
| Training | User training | | | | |
| O&M | Ops service | | | | |
| Other | Contingency | | | | |
| **Total** | | | | | |

**3.3 Transport investment reference ranges**

| Project type | Typical range | Note |
|---------|:----------:|------|
| Intelligent-mobility mgmt platform / TOCC | $3M–$12M | Varies by city size & scope |
| Smart motorway (100 km) | $4M–$14M | Includes field devices |
| Public-transit intelligence | $1.5M–$7M | Bus / rail / hub |
| AI video-analysis platform | $0.7M–$3M | Model count, camera count |
| Data platform | $1M–$4M | Includes data governance |
| Executive cockpit | $0.4M–$1.5M | Video wall + data |
| Sovereignty replacement (system-level) | $0.7M–$3M | Count & complexity |

---

### Step 4: Resource Planning and Configuration

**Goal**: Assess and plan the human, technical, and management resources for the roadmap.

**Inputs**: Project ranking, investment plan
**Outputs**: Resource plan, conflict-resolution

**Guidance:**

**4.1 Resource analysis dimensions**

| Type | Content |
|---------|---------|
| Human | Required roles / headcount / skills / availability window |
| Technical | Dev / test environments / toolchain |
| Data | Data availability, quality, permissions |
| Management | Client staff & time to invest |
| Supply chain | Hardware lead time, vendor capability |

**4.2 Resource summary table**

| Role | Y1-Q1 | Y1-Q2 | Y1-Q3 | Y1-Q4 | Y2 |
|---------|:---:|:---:|:---:|:---:|:---:|
| PM | 1 | 2 | 3 | 3 | 3 |
| Architect | 1 | 1 | 1 | 1 | 1 |
| Backend dev | 2 | 5 | 8 | 10 | 8 |
| Frontend dev | 1 | 3 | 4 | 5 | 4 |
| Data engineer | 1 | 2 | 3 | 4 | 3 |
| AI engineer | 1 | 2 | 3 | 3 | 3 |
| Test engineer | 1 | 2 | 4 | 4 | 3 |
| UI/UX | 1 | 1 | 1 | 1 | 1 |

---

### Step 5: Roadmap Authoring

**Goal**: Author a visualized 3-year roadmap showing project timing and milestones.

**Inputs**: Project list, ranking, phasing, resource plan
**Outputs**: 3-year roadmap, milestone plan

**Guidance:**

**5.1 Roadmap visualization**

```
3-year roadmap example (Gantt style):

 Year 1 (2025)              Year 2 (2026)              Year 3 (2027)
 Q1    Q2    Q3    Q4       Q1    Q2    Q3    Q4       Q1    Q2    Q3    Q4
+────+────+────+────+    +────+────+────+────+    +────+────+────+────+
| ██ | ██ | ██ |     |    |    |    |    |    |    |    |    |    |    | Cloud platform
|    | ██ | ██ | ██  |    | ██ | ██ |    |    |    |    |    |    |    Data platform
|    |    | ██ | ██  |    | ██ | ██ | ██ | ██ |    |    |    |    |    AI platform
|    |    |    | ██  |    | ██ | ██ | ██ |    |    |    |    |    |    Ops-monitoring
|    |    |    |     |    |    | ██ | ██ | ██ |    | ██ | ██ |    |    Maint-mgmt
| ██ | ██ |    |     |    |    |    |    |    |    |    |    |    |    Quick wins
+────+────+────+────+    +────+────+────+────+    +────+────+────+────+
         ▲                         ▲                         ▲
    Y1 milestone:            Y2 milestone:            Y3 milestone:
    ·Cloud live              ·Data platform live      ·AI on 50% scenarios
    ·Ops-monitoring ph1      ·AI platform live        ·Full intelligent ops
```

**5.2 Roadmap layering**

| Layer | Content | Frequency | Audience |
|------|------|:---:|-------|
| Strategy roadmap | Goals → programs → milestones | Annual | Exec |
| Project roadmap | Project start/end & milestones | Quarterly | Mid |
| Release plan | Version-release plan per system | Monthly | Execution |
| Iteration plan | Sprint / iteration detail | Biweekly | Dev team |

---

### Step 6: Investment-Benefit Analysis and Validation

**Goal**: Validate the overall program benefit to ensure investment rationality.

**Inputs**: Investment plan, project-value estimates
**Outputs**: Investment-benefit analysis report

**Guidance:**

**6.1 Triple-bottom-line evaluation framework**

See [Phase 05 Step 1 (Triple-Bottom-Line ROI)](../phase-05-financing-and-investment-review/01-triple-bottom-line-roi-workflow.md).

**6.2 Investment-rationality validation**

| Dimension | Method | Pass criterion |
|---------|------|---------|
| Strategy coverage | Each goal has a corresponding project | 100% covered |
| Investment slope | Annual growth vs. org absorption | Annual growth <50% |
| Benefit cadence | Continuous quick-win output | ≥1 visible result per half-year |
| Tech safeguard | Base platforms before app projects | Platform before apps |
| Risk dispersion | Not all resources on one project | No single project >40% of budget |

---

### Step 7: Risk-Plan Authoring

**Goal**: Identify key roadmap-execution risks and prepare plans.

**Inputs**: Roadmap, investment plan
**Outputs**: Risk register, contingency plan

**Guidance:**

**7.1 Key roadmap risks**

| Category | Description | Prob | Impact | Level | Response |
|---------|---------|:---:|:---:|:---:|---------|
| Regulatory | Leadership change shifts strategy | Med | High | High | Formalize docs, multi-tier reporting |
| Funding | Funder tightness delays / cuts budget | High | High | High | Minimum-guaranteed budget, phased invest |
| Tech | New-tech validation shortfalls | Med | Med | Med | PoC pilot |
| Org | Client IT team under-capable | High | Med | Med | Training + knowledge transfer |
| Vendor | Key vendor issues | Low | High | Med | Multi-vendor strategy |
| Data | Access-permission / quality issues | High | Med | Med | Early data-governance campaign |

**7.2 Plan design**

For high-level risks, detailed plans:
- Trigger (when to activate)
- Response (what to do)
- Owner (who)
- Recovery (how to get back on track)

---

### Step 8: Roadmap Review and Release

**Goal**: Complete roadmap review, gain exec approval, formally release.

**Inputs**: Roadmap doc, investment plan, risk plan
**Outputs**: Review minutes, signed roadmap

**Guidance:**

**8.1 Review meeting**

| Agenda | Content | Duration |
|------|------|:---:|
| Roadmap overview | 3-yr panorama, key milestones | 15 min |
| Annual plan | Y1 detail, resources, risks | 20 min |
| Investment needs | Estimate, annual plan, benefit | 15 min |
| Discussion / decision | Q&A, discussion, decision | 30 min |
| Next steps | Clarify follow-ups | 10 min |

**8.2 Release**

- Signed formal roadmap document
- Embedded in client's annual work plan
- Basis for project kickoff & annual budget
- Annual review & rolling-update framework

---

## V. Roles and Responsibilities (RACI Matrix)

| Activity | Planning advisor | Tech expert | PM | Client sponsor | Client IT | Client finance |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| Project inventory | **R/A** | C | I | I | C | I |
| Dependency & ranking | **R/A** | C | I | C | C | I |
| Investment estimate | C | C | **R/A** | I | C | **C** |
| Resource plan | C | C | **R/A** | I | C | I |
| Roadmap author | **R/A** | C | I | C | I | I |
| Benefit validation | **R/A** | I | C | C | I | C |
| Risk plan | C | C | **R/A** | C | I | I |
| Roadmap review | C | C | C | **A** | C | C |

---

## VI. Key Checkpoints

| # | Checkpoint | Pass criterion |
|---|--------|---------|
| CP1 | Project-list completeness | Covers all goals & opportunities |
| CP2 | Dependency analysis sound | Critical path clear |
| CP3 | Investment estimate sound | Analogous/parametric support, within benchmark |
| CP4 | Resource match | Within allocatable range |
| CP5 | Roadmap clear | One diagram shows the whole picture |
| CP6 | Client approval | Exec formally approves |

---

## VII. Estimated Duration

| Stage | Small | Medium | Large |
|------|:---:|:---:|:---:|
| Inventory & ranking | 1–2 days | 2–3 days | 3–5 days |
| Investment estimate | 1–2 days | 2–3 days | 3–5 days |
| Roadmap author | 1–2 days | 2–3 days | 3–5 days |
| Benefit & risk | 1 day | 1–2 days | 2–3 days |
| Review & release | 0.5 day | 0.5–1 day | 1 day |
| **Total** | **5–9 days** | **8–14 days** | **12–19 days** |

---

## VIII. Common Pitfalls and Countermeasures

| # | Pitfall | Countermeasure |
|---|------|------|
| 1 | Too many projects, scattered resources | ≤5–8 parallel projects per year |
| 2 | Too much in year one | Year 1: platform + 1–2 core apps + quick wins |
| 3 | Over-long dependency chain | Compress critical path, add parallelism |
| 4 | Over-optimistic estimate | +10–15% contingency, give ranges |
| 5 | Roadmap "on the wall" | Quarterly tracking, rolling update |
| 6 | Ignore talent-build lead time | Start hiring/training 6 mo early |

---

## IX. Outputs List

1. **Full project list & cards** (.xlsx)
2. **Project dependency graph** (.pptx)
3. **Project ranking** (.xlsx)
4. **Investment estimate (annual)** (.xlsx)
5. **Resource plan** (.xlsx)
6. **3-year roadmap** (.pptx — Gantt + milestones)
7. **Investment-benefit analysis** (.docx)
8. **Risk register & plan** (.xlsx)
9. **Signed roadmap (formal)** (.docx)

---

> **Version**: V1.0 | **Date**: 2025-07 | **Method**: Value-driven ranking + Critical Path + TCO
