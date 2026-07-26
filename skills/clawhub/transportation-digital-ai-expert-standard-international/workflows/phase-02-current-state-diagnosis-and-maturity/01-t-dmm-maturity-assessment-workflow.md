# 01-T-DMM Maturity Assessment Execution Workflow

## I. Workflow Overview

```
+-----------------------------------------------------------------------------+
|                 T-DMM (Transport Digital Maturity Model)                    |
+-----------------------------------------------------------------------------+
|                                                                             |
|  +----------+   +----------+   +----------+   +----------+                  |
|  |1. Assess |-->|2. Data    |-->|3. Workshop|-->|4. Scoring|                |
|  |  Planning|   |  Collect |   |  & Interv.|   |  & Calib.|                |
|  |  & Prep  |   |  & Survey|   |  (deep)   |   |          |                |
|  +----------+   +----------+   +----------+   +----------+                  |
|       |              |              |              |                        |
|       v              v              v              v                        |
|  +----------+   +----------+   +----------+   +----------+                  |
|  |5. Report |-->|6. Results |-->|7. Improve-|-->|8. Track  |               |
|  |  Author  |   |  Present |   |  ment &   |   |  & Re-   |               |
|  |          |   |  & Align |   |  Roadmap  |   |  assess  |               |
|  +----------+   +----------+   +----------+   +----------+                  |
|                                                                             |
|  Dimensions: Strategy&Governance | Business Digital | Data | Tech |         |
|  People | Security&Compliance                                                 |
+-----------------------------------------------------------------------------+
```

## II. T-DMM Model Overview

### 2.1 Six Assessment Dimensions

```
T-DMM Transport Digital Maturity Model — Dimension Framework

 +-----------------------------------------------------------------------+
 |                     Transport Digital Maturity                         |
 +----------+----------+----------+----------+----------+---------------+
 | Strategy | Business | Data     | Tech     | People   | Security      |
 | & Govern.| Digital  | Capability| Foundation| & Talent| & Compliance  |
 +----------+----------+----------+----------+----------+---------------+
 |·Vision   |·Online   |·Collection|·Infra    |·Org struct|·Cybersecurity|
 |·Gov. run |·Process  |·Governance|·Cloud    |·Talent mix|·Data security|
 | framework| automation|·Application|·Architect.|·Digital cult|·Compliance |
 |·Invest.  |·Smart app|·Data asset|·Tech plat|·Training  |·Incident resp|
 | framework|·Collab.  |          |          |·Enablement|               |
 +----------+----------+----------+----------+----------+---------------+
```

### 2.2 Five Maturity Levels

| Level | Name | Characteristics |
|:---:|------|---------|
| 1 | **Initial** | Fragmented IT, manual-dependence, no unified planning |
| 2 | **Defined** | Core business systematized, basic IT management, data starts aggregating |
| 3 | **Integrated** | Systems interconnected, data initially governed, platform-based |
| 4 | **Intelligent** | AI-assisted decisions, data-driven operations, advanced architecture |
| 5 | **Leading** | Fully intelligent, industry benchmark, capabilities exported outward |

---

## III. Detailed Steps

---

### Step 1: Assessment Planning and Preparation (Week 1)

**Goal**: Clarify scope, form the assessment team, set the plan, secure client commitment.

**Inputs**: Project contract / SOW, client basic info
**Outputs**: Assessment project plan, interview list, questionnaire design, kickoff materials

**Guidance:**

**1.1 Scope confirmation**

| Item | Description | Decision maker |
|-------|------|-------|
| Org scope | Which departments / subsidiaries / business units | Client sponsor |
| Business scope | Which lines assessed (operations / maintenance / dispatch / service) | Business decision maker |
| System scope | Which core systems involved | IT dept. head |
| Depth | Quick diagnosis (2 wks) / deep assessment (4–6 wks) | Project budget |

**1.2 Assessment team formation**

```
Assessment team structure (joint our-side + client-side):

         +-------------------+
         | Steering Committee| <- Execs from both sides (sponsor level)
         +---------+---------+
                   |
     +-------------+-------------+
     |             |             |
     v             v             v
+----------+ +----------+ +----------+
|Our assess| |Client    | |Domain    |
|team      | |liaison   | |experts   |
|PM+advise | |IT+business| |(as needed|
|+consultant| |          | |security/ |
+----------+ +----------+ |data)     |
                          +----------+
```

**1.3 Assessment plan**

| Week | Main activity | Deliverable | Participants |
|:---:|------|------|-------|
| W1 | Kickoff + survey + doc collection | Kickoff minutes, returned surveys | Assessment + client |
| W2 | Deep interviews + system demo | Interview notes | Assessment + key stakeholders |
| W3 | Assessment workshop + breakout | Workshop output | Assessment + client backbone |
| W4 | Data supplement + initial scoring | Draft scores | Assessment team |
| W5 | Report authoring + calibration | Assessment report V1.0 | Assessment team |
| W6 | Presentation + improvement discussion | Final report + roadmap recommendation | All |

**1.4 Kickoff prep**
- Kickoff deck: value, methodology, plan, cooperation needs
- Exec sponsorship: secure exec attendance and visible support
- Pre-issue survey: distribute the digital-maturity self-assessment on kickoff day

---

### Step 2: Data Collection and Survey Distribution (W1–W2)

**Goal**: Systematically collect full-dimensional data and information for the assessment.

**Inputs**: Assessment plan, questionnaire, data-collection checklist
**Outputs**: Survey return stats, doc-collection checklist, initial data-quality assessment

**Guidance:**

**2.1 Three data-collection channels**

```
Three data sources:

  +-----------------------------------------------------------+
  |                                                           |
  |  +---------+   +---------+   +---------+                  |
  |  |Doc review|   | Survey  |   |Interviews|                |
  |  | 30% wt. |   | 40% wt. |   | 30% wt. |                |
  |  +----+----+   +----+----+   +----+----+                |
  |       |            |            |                         |
  |       v            v            v                         |
  |  Strategy docs  All-staff self IT/business questionnaires|
  |  Tech docs     assessments  Decision-maker interviews    |
  |  Project docs  Third-party  Mid-level focus groups       |
  |  Ops data      evaluations  Backbone deep dives          |
  +-----------------------------------------------------------+
```

**2.2 Document collection checklist (transport-tailored)**

| Category | Core documents | Purpose | Priority |
|------|---------|------|:---:|
| Strategy | Recent / next 5-yr plan, dedicated digital-transformation plan | Strategy dimension | ★★★ |
| Org & governance | Org chart, IT-governance policy, data-governance policy | Governance & org | ★★★ |
| Technical | System architecture, network topology, data-architecture design | Tech dimension | ★★★ |
| Project archive | Last 3 yrs IT project list, acceptance reports | Build outcomes | ★★☆ |
| Ops data | O&M records, data-quality reports, security-incident logs | Ops capability | ★★☆ |
| Financial | Last 3 yrs IT budget & spend, project ROI | Investment level | ★★☆ |
| People | IT team roster, training records, performance reviews | Talent dimension | ★★☆ |

**2.3 Questionnaire design principles**

T-DMM self-assessment questionnaire design:
- 10–15 questions per dimension, total 100 points
- 5-point Likert scale (1 = strongly disagree, 5 = strongly agree)
- Mix of objective-fact and subjective-evaluation items
- Cross-validation items (check response consistency)
- Transport-scenario questions (e.g., "real-time collection coverage of maintenance-inspection data")

**2.4 Data-quality control**
- Survey return-rate target: >80%
- Low-quality survey identification: completion <3 min, all same option
- Document-gap log: key docs not obtained and why

---

### Step 3: Assessment Workshop and Deep Interviews (W2–W3)

**Goal**: Through face-to-face workshops and deep interviews, capture the deeper information surveys and docs cannot reveal.

**Inputs**: Survey analysis, doc-review findings, interview outline
**Outputs**: Workshop minutes, interview minutes, initial findings list

**Guidance:**

**3.1 Structured deep-interview outline**

**Decision-maker interview** (45–60 min each)

```
Decision-maker interview framework:

1. Opening (5 min)
   - Purpose, confidentiality commitment
   - Role & responsibility confirmation

2. Strategy & vision (15 min)
   - Your overall vision for transport digitalization?
   - Priority of digitalization in your strategy?
   - Most / least satisfying digital outcomes?

3. Investment & operations framework (15 min)
   - How is the IT-budget decision framework structured?
   - IT investment focus over the past 3 years?
   - How do you view return on investment?

4. Challenges & expectations (15 min)
   - Biggest resistance to advancing digitalization?
   - What kind of external partner do you expect?
   - What defines success?

5. Close (5–10 min)
   - Additional comments, suggestions, expectations
```

**Operational / technical backbone interview** (45–60 min each)

```
Backbone interview framework:

1. Work status (15 min)
   - Daily-work digitalization level?
   - Most time-consuming repetitive work?
   - Biggest difficulty in data access & use?

2. System experience (15 min)
   - Are core systems usable? Most wanted improvement?
   - Pain of cross-system operations?
   - Error / failure frequency and impact?

3. Capability & needs (15 min)
   - Self-rated digital-skill level?
   - Training & learning needs?
   - Features known but unused?

4. Improvement suggestions (10 min)
   - If you could change only one thing, what?
```

**3.2 Assessment workshop design** (half day)

| Time | Segment | Content | Participants |
|-------|------|------|-------|
| 09:00-09:30 | Open & benchmark | Industry benchmark cases, framework intro | All |
| 09:30-10:30 | Breakout 1 | By 6 dimensions: status consensus, strengths & gaps | Groups |
| 10:30-10:45 | Break | | |
| 10:45-11:45 | Breakout 2 | Groups preliminarily score the 6 dimensions | Groups |
| 11:45-12:00 | Showcase | Groups share core findings & scores | All |

**3.3 System demo observation**

- Have client IT team demo core systems live
- Observe: operations workflow, system response, data display, exception handling
- Record: UI age, operational efficiency, usability issues

---

### Step 4: Scoring and Calibration Analysis (W3–W4)

**Goal**: Comprehensive scoring from multi-source data, ensuring objectivity and consistency.

**Inputs**: Survey results, doc review, interview notes, workshop output
**Outputs**: Six-dimension scorecard, maturity radar chart, calibration record

**Guidance:**

**4.1 Composite scoring model**

```
T-DMM composite scoring logic:

        Survey(40%)     Doc review(30%)   Expert assess(30%)
            |                |                |
            v                v                v
      Survey×0.4     +  Doc×0.3      +  Expert×0.3
            |                |                |
            └────────────────┼────────────────┘
                             |
                             v
                   Per-dimension composite
                             |
                  (weighted avg per dimension)
                             v
                   Overall maturity score
```

**4.2 Six-dimension scoring rules**

| Dimension | Sub-items | Weight | Scoring outline |
|------|------|:---:|-------------|
| Strategy & governance | Vision / investment-ops framework / governance / standards | 15% | No plan → comprehensive → plan-execution aligned |
| Business digital | Online rate / process automation / smart apps | 25% | Manual → systematized → automated → intelligent |
| Data capability | Collection / governance / application / asset mgmt | 20% | Scattered → aggregated → governed → assetized |
| Tech foundation | Infra / cloud / architecture / platform | 15% | Legacy → virtualized → cloud → cloud-native |
| People & talent | Org / talent mix / training / culture | 15% | No dedicated → team → specialized → leading |
| Security & compliance | Cyber / data security / classification / incident response | 10% | Basic → systematic → proactive → resilient |

**4.3 Calibration**

```
Three calibration principles:

1. Cross-validation
   Each conclusion needs 2+ independent sources
   e.g., "poor data quality" → survey + interview + demo observation

2. Evidence-driven
   Every score change needs concrete evidence
   e.g., 2→3 needs proof of data-governance policy + tool + execution log

3. Consistency
   Internal assessment-team scoring consistency >80%
   Disagreements discussed to consensus
```

**4.4 Score-output example**

```
T-DMM maturity score output:

 +-----------------------------------+
 | Dimension        | Score | Level  |
 +-----------------------------------+
 | Strategy&Gov.    | 2.8   | 2→3   |
 | Business digital | 2.2   |  2    |
 | Data capability  | 1.8   | 1→2   |
 | Tech foundation  | 2.5   | 2→3   |
 | People & talent  | 2.0   |  2    |
 | Security&Compl.  | 3.2   |  3    |
 +-----------------------------------+
 | Overall maturity  | 2.4   |  2    |
 +-----------------------------------+

 Radar: [Strategy][Business][Data][Tech][People][Security]
```

---

### Step 5: Assessment Report Authoring (W4–W5)

**Goal**: Author a complete, well-evidenced, actionable assessment report.

**Inputs**: Score data, findings list, draft improvement suggestions
**Outputs**: T-DMM assessment report V1.0

**Guidance:**

**5.1 Standard report structure**

```
T-DMM assessment report contents:

Executive summary (2–3 pages)
- Overall conclusion
- Core findings (3–5)
- Key recommendations (3–5)
- Maturity overview

Ch.1 Assessment overview
  1.1 Background & goals
  1.2 Scope & methodology
  1.3 Process summary

Ch.2 Overall conclusion
  2.1 Composite maturity score
  2.2 Six-dimension scorecard
  2.3 Industry benchmarking
  2.4 Strengths & gaps

Ch.3 Dimension-by-dimension detail
  3.1 Strategy & governance
  3.2 Business digital
  3.3 Data capability
  3.4 Tech foundation
  3.5 People & talent
  3.6 Security & compliance
  (each: status → evidence → scoring basis → improvement direction)

Ch.4 Benchmark analysis
  4.1 Leading practices
  4.2 Quantified gap analysis
  4.3 Catch-up path analysis

Ch.5 Improvement recommendations
  5.1 Priority matrix
  5.2 Short-term quick wins (0–6 mo)
  5.3 Mid-term uplift (6–18 mo)
  5.4 Long-term plan (18–36 mo)

Appendices
- Interview list
- Document checklist
- Scoring rules
- Survey stats
```

---

### Step 6: Results Presentation and Alignment (W5–W6)

**Goal**: Present results to client management, gain recognition, drive action.

**Inputs**: Assessment report, presentation deck
**Outputs**: Presentation minutes, management feedback, follow-up execution consensus

**Guidance:**

**6.1 Presentation strategy**

```
Audience tiers:

Tier            Focus                          Strategy
------------------------------------------------------------
Exec decision  Strategic positioning,         <=5 pages, sharp
(Sponsor)      benchmarking, overall gap,      contrast, clear
               action direction                recommendations

Mid management Specific gaps, root cause,      Detailed data
(IT/biz leads) improvement plan, resources    per-dimension depth

Frontline      Specific problems, methods,     Concrete problems,
(operators)    personal impact, training       actionable steps
```

**6.2 Difficult-conversation scripts**

| Scenario | Response |
|------|---------|
| Client disputes low score | "We understand. This score reflects the gap vs. industry benchmark, not a denial of past achievements..." |
| Inter-department blame | "The maturity model emphasizes systemic thinking — each dimension needs cross-department collaboration..." |
| Feels improvement too hard | "We suggest starting with 3 low-cost, fast-return directions..." |
| Questions the method | "Our methodology references international DMM, CMMI, and comparable maturity frameworks..." |

---

### Step 7: Improvement Recommendations and Roadmap

**Goal**: Based on findings, build a practical improvement plan and roadmap.

**Inputs**: Assessment report, client resource constraints
**Outputs**: Improvement proposal, preliminary roadmap

**Guidance**: See [Phase 03 Step 4 (3-Year Roadmap & Investment Plan)](../phase-03-strategy-and-top-level-design/04-three-year-roadmap-and-investment-workflow.md).

---

### Step 8: Continuous Tracking and Re-Assessment (Ongoing)

**Goal**: Establish a periodic re-assessment cadence and track improvement progress.

**Inputs**: Baseline assessment, improvement roadmap
**Outputs**: Annual re-assessment report, maturity trend chart

**Guidance:**

- Recommended re-assessment: annually (or after major project completion)
- Focus: compare against baseline score change, validate improvement effectiveness
- Trend analysis: multi-period scores, assess improvement velocity

---

## V. Roles and Responsibilities (RACI Matrix)

| Activity | Assess PM | Assess advisor | Client sponsor | Client IT lead | Client backbone |
|------|:---:|:---:|:---:|:---:|:---:|
| Assessment planning | **R/A** | C | C | C | I |
| Doc collection | **R** | I | I | C | C |
| Survey & analysis | **R** | C | I | C | C |
| Deep interviews | C | **R** | I | C | C |
| Workshop facilitation | I | **R** | C | C | **R** |
| Score calibration | C | **R/A** | I | I | I |
| Report authoring | C | **R/A** | I | C | I |
| Results presentation | C | **R** | **A** | C | I |

---

## VI. Key Checkpoints

| # | Checkpoint | Timing | Pass criterion |
|---|--------|------|---------|
| CP1 | Plan review | W1 | Sponsor approves plan |
| CP2 | Data collection complete | End W2 | Docs >80%, surveys >80% |
| CP3 | Interview coverage | Mid W3 | 100% key stakeholders |
| CP4 | Score calibration | Mid W4 | Internal consistency >80% |
| CP5 | Internal report review | End W5 | Internal review passed |
| CP6 | Client acceptance | W6 | Client confirms conclusion |

---

## VII. Estimated Duration

| Mode | Duration | Team | Applies to |
|---------|:---:|---------|---------|
| Quick diagnosis | 2 wks | 2–3 | Preliminary judgement, small clients |
| Standard | 4–6 wks | 3–5 | Standard projects |
| Deep | 8–12 wks | 5–8 | Large groups, multi-business |

---

## VIII. Common Pitfalls and Countermeasures

| # | Pitfall | Countermeasure |
|---|------|------|
| 1 | Client provides polished info | Multi-source cross-validation, on-site system observation |
| 2 | Inter-dept blame causes info gaps | Sponsor mandates cross-dept cooperation |
| 3 | Low survey return | Deadline + key-person follow-up |
| 4 | Over-reliance on survey | Survey only 40%; combine doc + interview |
| 5 | Over-harsh scores cause resistance | Frame as "room to grow" not "gap" |
| 6 | No industry benchmark data | Build an industry baseline database |

---

## IX. Outputs List

1. **Assessment project plan** (.docx)
2. **T-DMM self-assessment questionnaire** (.docx/.xlsx)
3. **Data-collection checklist & tracker** (.xlsx)
4. **Interview minutes** (.docx)
5. **Workshop materials & minutes** (.pptx + .docx)
6. **Assessment report** (.docx + .pptx)
7. **Maturity radar chart** (.pptx/image)
8. **Improvement roadmap proposal** (.pptx)

---

> **Version**: V1.0 | **Date**: 2025-07 | **Reference standards**: DMM / CMMI / COBIT / ISO-IEC 33000
