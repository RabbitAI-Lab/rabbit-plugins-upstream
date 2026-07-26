# 01-Digital Vision and Goals Definition Workflow

## I. Workflow Overview

```
+-----------------------------------------------------------------------------+
|             Digital Vision & Strategic-Goals Definition Workflow            |
+-----------------------------------------------------------------------------+
|                                                                             |
|  +----------+   +----------+   +----------+   +----------+                  |
|  |1. Environ|-->|2. Vision |-->|3. Strategy|-->|4. KPI    |               |
|  |  Scan & |   |  Co-create|   |  Goals   |   |  Decomp. |               |
|  |  Digest |   |  Workshop |   |  Define  |   |  & Target|               |
|  +----------+   +----------+   +----------+   +----------+                  |
|       |              |              |              |                        |
|       v              v              v              v                        |
|  +----------+   +----------+   +----------+   +----------+                  |
|  |5. Benchm.|-->|6. Vision |-->|7. Commun|-->|8. Goal    |                |
|  |  & Compl|   |  Doc     |   |  icate  |   |  Mgmt &  |                |
|  |  Review  |   |  Author  |   |  Align  |   |  Track   |                |
|  +----------+   +----------+   +----------+   +----------+                  |
|                                                                             |
|  Hierarchy: Vision → Mission → Strategy Goals → KPIs → Annual → Project     |
+-----------------------------------------------------------------------------+
```

## II. Applicable Scenarios

This workflow helps transport-sector clients (transport authorities, transport-investment groups, public-transit operators, etc.) define the vision, mission, strategic goals, and KPI system for digital transformation, supporting subsequent architecture design and roadmap authoring.

## III. Prerequisites and Inputs

| Input | Source | Description |
|-------|------|------|
| T-DMM maturity-assessment report | Phase 02 | Client digital-current baseline |
| Gap-analysis report | Phase 02 | As-Is vs To-Be gaps |
| Client's existing strategy | Client | Recent / next 5-yr plan, etc. |
| National / regional transport-digital regulation compendium | Industry research | Regulatory requirements & direction |
| Industry benchmark case library | Industry research | Peer success practices |

---

## IV. Detailed Steps

---

### Step 1: Environment Scan and Input Digestion

**Goal**: Fully digest internal/external inputs to ground the vision definition.

**Inputs**: Prior assessment reports, client strategy docs, regulatory files
**Outputs**: Environment-analysis report, brief SWOT

**Guidance:**

**1.1 Four-dimension environment scan**

| Dimension | Content | Method |
|------|---------|------|
| Regulatory environment | National / regional transport-digital regulations, KPI requirements | Regulatory-file study |
| Industry trends | Transport-tech trends, tech-maturity curves | Industry reports + tech radar |
| Competitive environment | Peer cities / peer-agency digital levels | Benchmarking |
| Internal environment | Client's strategy, resources, constraints | Strategy docs + interviews |

**1.2 Transport regulatory key-framework quick reference (2024–2025)**

```
Key regulatory frameworks:

National level:
 · National transport-development strategy → evaluation indicator system
 · Digital-transport 5-year plan → 7 key tasks
 · Highway digital-transformation acceleration action plan (e.g., PIARC / FHWA guidance)
 · Guidance on data economy × transport (open-data / data-space initiatives)
 · Vehicle-infrastructure-cloud (cooperative-ITS) pilot program
 · Next-cycle national transport-plan directions (e.g., EU TEN-T / national 5-yr plan)

Regional level:
 · Regional / state transport-development pilot mandates
 · Regional digital-government / digital-economy plans
 · Local transport-digital dedicated-budget regulations
```

**1.3 Strategic SWOT brief**

| Internal | Strengths (S) | Weaknesses (W) |
|------|---------|---------|
| | Existing IT base, management support, business-data accumulation | Thin IT talent, legacy systems, data silos |
| External | Opportunities (O) | Threats (T) |
| | Strong regulatory push, mature AI, dedicated budgets | Budget uncertainty, fast tech iteration, vendor lock-in |

---

### Step 2: Vision Co-Creation Workshop

**Goal**: Through a structured workshop, have the client's core management jointly paint the digital-transformation vision.

**Inputs**: Environment report, SWOT, benchmark cases
**Outputs**: Vision statement (draft), strategic-direction consensus

**Guidance:**

**2.1 Vision workshop design** (1 day)

```
Vision co-creation agenda:

09:00-09:30  Open & inspire
  · Workshop goal & rules
  · Inspiration video / cases: Singapore Smart Nation, London TfL, Rotterdam port

09:30-10:30  Module 1: A day in 2035
  · Prompt: "Imagine a day in 2035 — what is our transport system like?"
  · Breakout + visualize
  · Themes: manager view / traveler view / operator view

10:30-10:45  Break

10:45-12:00  Module 2: Gaps & challenges
  · Prompt: "From today to the vision, what is the biggest obstacle?"
  · Brainstorm + vote to converge
  · Rank by urgency & impact

12:00-13:30  Lunch

13:30-15:00  Module 3: Vision consensus
  · Prompt: "Describe our digital vision in one sentence"
  · Each writes 3 keywords → group → all vote
  · Generate 3–5 candidate vision statements

15:00-15:15  Break

15:15-16:30  Module 4: Mission & values
  · Prompt: "What principles must we uphold to realize the vision?"
  · Output: mission statement + 3–5 core values
  · e.g., "Data-driven", "User-first", "Safety-first", "Agile innovation"

16:30-17:00  Module 5: Vote & consensus
  · All vote on vision, mission, values
  · Confirm final version (or direction to revise)
  · Next steps
```

**2.2 Vision definition method**

A good digital vision should:

| Trait | Description | Example |
|------|------|------|
| Aspirational | Desirable future state | "Become a globally leading smart-mobility benchmark" |
| Understandable | Everyone gets it | Avoid overly technical jargon |
| Distinctive | Reflects unique positioning | "Rail + bus + active-mobility integrated smart travel" |
| Quantifiable | Decomposes into measurable goals | Via KPIs |
| Time-bound | Has a rough timeframe | 3 yr / 5 yr / 10 yr |

**2.3 Transport vision examples**

```
 · "Build a world-class, citizen-satisfying smart-mobility service system"
 · "Establish a data-driven, AI-enabled, omni-aware smart-motorway benchmark"
 · "Let every vehicle flow smoothly, every passenger arrive safely"
 · "Become a pacesetter in transport-sector digital transformation"
 · "One screen for the whole region, one network to run the city, one click to dispatch all"
```

---

### Step 3: Strategic-Goals Definition

**Goal**: Decompose the vision into concrete, measurable strategic goals.

**Inputs**: Vision statement, gap-analysis report, regulatory requirements
**Outputs**: Strategic-goal system (about 4–7 goals)

**Guidance:**

**3.1 Strategic-goals decomposition — Balanced Scorecard (BSC) four quadrants**

```
Strategic-goals four-dimension framework:

       +---------------------------------------------+
       |        Strategic-Goal System (Vision)        |
       +---------------------+-----------------------+
       |  Benefit dimension |  Customer / Service dim |
       |  (cost & eff.)     |  (traveler experience) |
       |  · Lower opex      |  · Service satisfaction|
       |  · Resource use    |  · Info timeliness     |
       |  · Lower accident  |  · Lower complaints    |
       |  · ROI             |  · Congestion relief   |
       +---------------------+-----------------------+
       |  Process / Capability | Learning / Growth    |
       |  (mgmt efficiency)|  (org & talent)        |
       |  · Decision efficiency| · Digital-talent share|
       |  · Emergency speed|  · Staff digital skill |
       |  · Cross-agency collab| · Innovation projects|
       |  · Process online |  · Knowledge mgmt      |
       +---------------------+-----------------------+
```

**3.2 Strategic-goal SMART principle**

Each strategic goal must be:
- **S**pecific — clear and concrete
- **M**easurable — quantifiable
- **A**chievable — capability-attainable
- **R**elevant — aligned with vision
- **T**ime-bound — explicit deadline

**3.3 Transport strategic-goal library (reference)**

| ID | Strategic goal | Dimension |
|:---:|------|------|
| SG-01 | Build a region-wide, second-level-response network-sensing system | Process/Capability |
| SG-02 | Core business 100% online, automation rate >70% | Process/Capability |
| SG-03 | One-stop traveler service, satisfaction >90% | Customer/Service |
| SG-04 | Build transport data platform, data-sharing rate >80% | Process/Capability |
| SG-05 | Opex −20% in 3 yrs, accident rate −30% | Benefit |
| SG-06 | AI covers >50% of core business scenarios | Process/Capability |
| SG-07 | Cultivate a 100+ person digital-professional team | Learning/Growth |
| SG-08 | Security-classification compliance 100% | Process/Capability |

---

### Step 4: KPI Decomposition and Target Setting

**Goal**: Set measurable KPIs and annual target values for each strategic goal.

**Inputs**: Strategic-goal system, benchmarking data, client current-state data
**Outputs**: KPI tree, annual targets, KPI dictionary

**Guidance:**

**4.1 KPI decomposition tree**

```
Vision → Strategy Goal → KPIs → Annual Target → Project Target

Example:
Vision: "Build a world-class smart-mobility system"

Strategy SG-02: core business 100% online
  ├─ KPI 2.1: Process-online rate
  │    ├─ 2025 target: 60%
  │    ├─ 2026 target: 80%
  │    └─ 2027 target: 100%
  ├─ KPI 2.2: Process-automation rate
  │    ├─ 2025 target: 30%
  │    ├─ 2026 target: 55%
  │    └─ 2027 target: 70%
  └─ KPI 2.3: Mobile-app coverage
       ├─ 2025 target: 50%
       ├─ 2026 target: 80%
       └─ 2027 target: 100%
```

**4.2 KPI dictionary template**

```
KPI dictionary:

KPI ID: KPI-02-01
Name: Process-online rate
Strategy goal: SG-02 core-business online
Definition: Online core processes ÷ total core processes
Formula: (online processes ÷ total) × 100%
Source: Per-system process stats
Period: Quarterly
Target: 2025-60%, 2026-80%, 2027-100%
Current baseline: ~35% (from assessment)
Benchmark: Advanced level 90%+
Owner: IT dept + business units
```

**4.3 Transport core KPIs reference**

| Category | KPI | Advanced | Baseline target |
|------|-----|:---:|:---:|
| Network monitoring | Auto incident-detection rate | >85% | >70% |
| Network monitoring | Incident occurrence→handling avg time | <15 min | <30 min |
| Maintenance | Pavement-defect AI-ID accuracy | >90% | >80% |
| Maintenance | Data-driven maintenance-plan share | >80% | >60% |
| Public service | Travel-info service satisfaction | >90 | >80 |
| Public service | Info-publish update latency | <1 min | <5 min |
| Data mgmt | Core-data accuracy | >99% | >95% |
| Data mgmt | Data-sharing timeliness | >95% | >85% |

---

### Step 5: Benchmarking and Compliance Review

**Goal**: Ensure digital-strategy goals align with national / regional transport regulations.

**Inputs**: Strategic-goal system, KPIs, regulatory files
**Outputs**: Benchmarking matrix, compliance-review report

**Guidance:**

**5.1 Benchmarking matrix**

| Regulatory requirement | Source | Our strategy goal | Alignment | Gap |
|---------|---------|------------|:---:|------|
| National transport-strategy evaluation indicators | National transport strategy | SG-01 full sensing | High | - |
| Data-sharing rate >80% | Digital-transport plan | SG-04 data platform | Med | accelerate |
| Security classification Level 3 | Cybersecurity law / NIS2 | SG-08 compliance | High | 2 systems pending |

**5.2 Compliance checklist**

- [ ] Does the digital strategy cover all national transport-development evaluation indicators?
- [ ] Does it respond to the explicit deadlines in the latest regulatory files?
- [ ] Does it address emerging directions (data economy / innovation-driven productivity)?
- [ ] Do security KPIs satisfy classification, cryptographic, and critical-infrastructure protection requirements?
- [ ] Does it benchmark the region's / state's dedicated plan and KPIs?

---

### Step 6: Vision Document Authoring

**Goal**: Author the formal digital-vision and strategic-goals document.

**Inputs**: Vision statement, strategic goals, KPI system
**Outputs**: Digital-Transformation Vision & Strategic-Goals White Paper

**Guidance:**

**6.1 Document structure**

```
Digital-Transformation Vision & Strategic-Goals White Paper:

Preface — A message from leadership (client's top decision maker)

Ch.1 Strategic background
  1.1 Macro environment & regulatory drivers
  1.2 Industry development & trends
  1.3 Internal demands & challenges

Ch.2 Vision & mission
  2.1 Digital-transformation vision
  2.2 Digital mission
  2.3 Core values

Ch.3 Strategic-goal system
  3.1 Goal landscape
  3.2 Per-goal detail
  3.3 Logical relationships

Ch.4 KPIs & target values
  4.1 KPI landscape
  4.2 Annual targets
  4.3 KPI dictionary

Ch.5 Strategic initiatives
  5.1 Key programs & projects
  5.2 Resource safeguards
  5.3 Governance framework

Ch.6 Implementation path
  6.1 Phased plan
  6.2 Key milestones
  6.3 Risks & responses

Appendices: Regulatory index, benchmark sources
```

---

### Step 7: Communication and Consensus

**Goal**: Through effective communication, help every org tier understand and buy into the digital vision.

**Inputs**: Vision white paper
**Outputs**: Communication materials, roadshow, feedback

**Guidance:**

**7.1 Tiered communication strategy**

| Tier | Focus | Format | Duration |
|------|---------|------|:---:|
| Exec | Strategic value, ROI, industry standing | Briefing | 1 hr |
| Mid | Business value, plan, dept role | Work session | 2 hr |
| Frontline | Impact on work, skills, how to join | All-hands + materials | 1 hr |
| External | Social value, service uplift, public participation | Media / video | - |

**7.2 Communication package**
- Vision deck (exec / staff versions)
- One-page vision summary (poster / desk card)
- Vision video (3–5 min)
- Digital-employee handbook (transformation FAQ)

---

### Step 8: Goal Management and Tracking

**Goal**: Establish a normalised strategic-goal management and tracking framework.

**Inputs**: KPI system, annual targets
**Outputs**: Goal-management framework, quarterly tracking report

**Guidance:**

**8.1 Combine OKR and KPI**

Recommend a "KPI + OKR" dual track:
- KPI measures long-term strategic-goal attainment (annual)
- OKR drives quarterly key results and breakthrough goals

**8.2 Strategy tracking board**

```
Strategy tracking board (quarterly):

 Strategy  │  KPI     │ Annual │ Actual │ Status │ Trend
───────────┼──────────┼────────┼────────┼────────┼─────
 SG-01     │ Detect  │ 70%   │ 52%   │ 🟡    │ ↗
 SG-02     │ Online  │ 60%   │ 45%   │ 🟢    │ ↗↗
 SG-03     │ Satis.  │ 80    │ 72    │ 🟡    │ →
 ...

 🟢 Normal  🟡 At risk  🔴 Severely behind
 ↗ Improving  → Flat  ↘ Worsening  ↗↗ Rapidly improving
```

---

## V. Roles and Responsibilities (RACI Matrix)

| Activity | Strategy advisor | Tech expert | PM | Client exec | Client mid | Client frontline |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| Environment scan | **R/A** | C | I | I | I | I |
| Vision workshop facil. | **R/A** | C | C | C | C | I |
| Strategy-goal define | **R** | C | C | **A** | C | I |
| KPI decompose | **R** | C | C | C | C | I |
| Benchmarking | **R** | C | I | I | I | I |
| Doc authoring | **R/A** | C | I | I | I | I |
| Communication | C | I | **R** | I | C | I |
| Goal tracking | I | I | **R** | I | C | I |

---

## VI. Key Checkpoints

| # | Checkpoint | Pass criterion |
|---|--------|---------|
| CP1 | Environment scan done | All four dims produced, regulatory list complete |
| CP2 | Vision workshop success | Vision statement passed by all-vote |
| CP3 | Strategy goals confirmed | 4–7 SMART goals signed by sponsor |
| CP4 | KPI system complete | 2–4 KPIs per goal, with baseline & target |
| CP5 | Benchmarking | Core regulations 100% aligned, no major gap |
| CP6 | White paper released | Formally released after exec approval |

---

## VII. Estimated Duration

| Stage | Duration | Note |
|------|:---:|------|
| Environment scan | 2–3 days | Depends on prior reports |
| Vision workshop | 1 day (+1 prep) | Core half-day compressible |
| Strategy-goal define | 1–2 days | Multiple iterations |
| KPI decompose | 1–2 days | Data collection time |
| Benchmarking | 1 day | Regulatory study + matrix |
| Doc authoring | 2–3 days | Write + polish |
| Communication | 1–2 wks | Distributed |
| **Core total** | **8–12 days** | |

---

## VIII. Common Pitfalls and Countermeasures

| # | Pitfall | Countermeasure |
|---|------|------|
| 1 | Vision becomes empty slogan | Immediately pair with KPIs & annual targets |
| 2 | Goals detached from reality | Staged attainable targets from baseline data |
| 3 | Workshop becomes exec monologue | Pre-interview all views, anonymous voting |
| 4 | Regulations change faster than plan | Annual strategy-review framework, adjust timely |
| 5 | Vision "hangs on the wall" | Pair with appraisal & incentive, embed in dept annual KPIs |

---

## IX. Outputs List

1. **Environment-analysis report** (.docx)
2. **Vision workshop materials & minutes** (.pptx + .docx)
3. **Strategic-goal system diagram** (.pptx)
4. **KPI tree & target-value table** (.xlsx)
5. **KPI dictionary** (.docx)
6. **Benchmarking matrix** (.xlsx)
7. **Digital-Transformation Vision & Strategic-Goals White Paper** (.docx)
8. **Vision communication package** (.pptx + video + poster)
9. **Strategy tracking board** (.pptx/.xlsx)

---

> **Version**: V1.0 | **Date**: 2025-07 | **Method**: BSC + SMART + OKR-KPI
