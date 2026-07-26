# 02-Deep Business Research Workflow

## I. Workflow Overview

```
+-----------------------------------------------------------------------------+
|                     Deep Business Research Workflow                         |
+-----------------------------------------------------------------------------+
|                                                                             |
|  +----------+   +----------+   +----------+   +----------+                  |
|  |1. Research|-->|2. Stake- |-->|3. On-site|-->|4. Req.   |               |
|  |  Planning|   |  holder   |   |  Observe |   |  Workshop|               |
|  |  & Design|   |  Interviews|  |  (scenes)|   |  Facilit.|               |
|  +----------+   +----------+   +----------+   +----------+                  |
|       |              |              |              |                        |
|       v              v              v              v                        |
|  +----------+   +----------+   +----------+   +----------+                  |
|  |5. Req.   |-->|6. Req.   |-->|7. Req.   |-->|8. Req.   |                |
|  |  Doc     |   |  Review  |   |  Priority|   |  Baseline|                |
|  |  Author  |   |  & Verify|   |  Ranking |   |  & Mgmt  |                |
|  +----------+   +----------+   +----------+   +----------+                  |
|                                                                             |
|  Method: BABOK | User Stories | Scenario-based Research | Prototype Verify  |
+-----------------------------------------------------------------------------+
```

## II. Applicable Scenarios

This workflow applies to systematic business-needs research for transport-sector clients (transport authorities, transport investment & operating enterprises, etc.), covering the full process from research planning to requirements-baseline confirmation.

## III. Prerequisites and Inputs

| Input | Source | Description |
|-------|------|------|
| Contract / SOW | Project initiation docs | Scope, goals, constraints |
| T-DMM assessment report (if any) | Maturity-assessment phase | Client digital-current baseline |
| Client org chart | Client | Departments, responsibilities |
| Research toolkit | Company knowledge base | Standard interview outline, survey templates, user-story templates |

---

## IV. Detailed Steps

---

### Step 1: Research Planning and Design (1–2 days)

**Goal**: Build a systematic research plan, clarifying scope, targets, methods, and outputs.

**Inputs**: Contract, current-state conclusions, client org structure
**Outputs**: Research plan, stakeholder list, interview outline, questionnaire

**Guidance:**

**1.1 Four-dimension scope definition**

| Dimension | Definition | Example |
|------|---------|------|
| Org scope | Which departments / units | Operations mgmt, maintenance mgmt, info center, dispatch center |
| Business scope | Which business domains | Network monitoring, emergency command, maintenance, tolling, public service |
| Tier scope | Which management levels | Group HQ, branch / district office, frontline station |
| Depth scope | How detailed the research goes | Process level / function level / data-field level |

**1.2 Stakeholder identification and classification**

```
Typical transport-sector stakeholder classes:

+-----------------------------------------------------------------+
| Decision layer | Execs / board chair / GM / CIO-equivalent    |
|                | Care: strategic value, outcomes, ROI, risk   |
+-----------------------------------------------------------------+
| Management    | Info-center director, business-unit heads     |
|                | Care: goal attainment, unit interest, resourcing|
+-----------------------------------------------------------------+
| Operations    | Domain experts, sysadmins, frontline operators |
|                | Care: ease of use, efficiency, learning cost   |
+-----------------------------------------------------------------+
| External      | Regulator, public / travelers, partners        |
|                | Care: compliance, service experience, synergy  |
+-----------------------------------------------------------------+
```

**1.3 Research method toolbox**

| Method | Scenario | Duration | Output |
|------|---------|:---:|------|
| 1:1 deep interview | Deep views from execs / key people | 45–60 min | Interview notes |
| Focus group | Multi-party views on a business domain | 90–120 min | Session notes |
| Job-shadowing | Understand frontline actual process | Half day–1 day | Observation log |
| System walkthrough (demo) | Understand existing functions & pain | 60–90 min | System eval record |
| Document analysis | Understand existing process & policy | 1–2 days | Doc analysis report |
| Survey | Large-sample quantitative data | 3–5 days | Stats report |
| Requirements workshop | Facilitated requirements consensus | Half day–1 day | Workshop output |
| Prototype review | Validate understanding via prototype | 2–4 hrs | Prototype feedback |

---

### Step 2: Stakeholder Interview Execution (3–5 days)

**Goal**: Cover all key stakeholders and capture comprehensive needs information.

**Inputs**: Stakeholder list, interview outline, research plan
**Outputs**: Full interview notes, raw requirement records, interview log

**Guidance:**

**2.1 Single-interview SOP**

```
Single-interview SOP:

Before (1–2 days ahead):
□ Send invitation (agenda + pre-read)
□ Review stakeholder background
□ Customize outline for this stakeholder
□ Prepare recording / note template

During (strictly by agenda):
□ Open (5 min): purpose, confidentiality, agenda
□ Understand status (15 min): current work & pain points
□ Explore needs (25 min): dig into expectations & needs
□ Confirm consensus (10 min): summarize key points, confirm understanding
□ Close (5 min): next steps, thanks

After (within 24 hrs):
□ Complete interview notes (while memory fresh)
□ Extract key requirement points
□ Log open follow-ups
□ Rate information credibility (high / med / low)
```

**2.2 Research focus by transport role**

| Role | Focus | Key question |
|------|-----------|---------|
| Network-monitoring staff | Incident detection speed, info accuracy, ease | "From incident occurrence to confirmation, how long on average today?" |
| Maintenance managers | Defect ID, maintenance planning, resource dispatch | "What data does maintenance decisions rely on? Is it enough?" |
| Emergency commanders | Plan mgmt, resource dispatch, info coordination | "Which link in emergency response is most error-prone?" |
| Toll operators | Tolling efficiency, audit capability, analytics | "What is the detection rate of abnormal tolling?" |
| Service / hotline staff | Inquiry handling, complaint routing, satisfaction | "Gap between hotline answer-rate / resolution-rate target and actual?" |
| Data analysts | Data access, analysis tools, reporting | "How long to produce one analytics report typically?" |

**2.3 Requirement logging standard**

Each requirement point must record:
- ID (e.g., REQ-YY-001)
- Source (stakeholder name + role + date)
- Description (one-sentence summary)
- Type (functional / non-functional / data / integration / UI)
- Initial priority (MoSCoW: Must / Should / Could / Won't)
- Related business scenario
- Verification criterion (how to judge the need is met)

---

### Step 3: On-Site Business-Scene Observation (1–2 days)

**Goal**: Go to the front line and understand the real process and pain points via job-shadowing.

**Inputs**: Business-scene list, observation plan
**Outputs**: Shadowing log, process snapshot, pain-point list

**Guidance:**

**3.1 Typical transport observation scenes**

| Scene | Observe | Duration |
|------|---------|:---:|
| Control-room daily watch | Duty process, incident handling, info flow | 2–4 hrs |
| Field maintenance work | Inspection process, data collection, reporting | Half day |
| Toll-lane operation | Tolling process, exception handling, equipment use | 1–2 hrs |
| Service center | Phone / online service handling process | 2 hrs |
| Emergency drill / live | Full emergency-response process | As actual |
| Report authoring | Weekly / monthly data collection & writing | 2 hrs |

**3.2 Shadowing record points**

```
Shadowing record sheet:

Observer: _________  Role: _________  Date: _________
Scene: _________  Duration: _________

1. Process record ("how it's done")
   - Steps (chronological)
   - Tool / system used per step
   - Time per step
   - Collaboration touchpoints with others

2. Pain record ("what's annoying")
   - Steps with duplicate data entry
   - Steps with slow system response
   - Steps requiring switching multiple systems
   - Steps needing manual judgement / calculation
   - Steps with unavailable or delayed info

3. Workbench / tool screenshots (with permission)
   - Main system interfaces
   - Paper forms / ledgers
   - Ad-hoc offline Excel etc.

4. Improvement ideas ("user expectation")
   - Operator's own suggestions
   - Where they feel "others do better"
```

---

### Step 4: Requirements Workshop Facilitation and Consensus (1 day)

**Goal**: Through a structured workshop, let needs from different roles surface and clash, and reach consensus.

**Inputs**: Interview notes, observation records, preliminary requirement list
**Outputs**: Workshop output (requirement map, priority consensus, process sketch)

**Guidance:**

**4.1 Workshop design** (full-day version)

```
Requirements workshop agenda:

Morning: diverge

09:00-09:30  Open & warm-up
   - Workshop goal
   - Ice-breaker: "If the system could do one thing for me..."
   - Group rules

09:30-10:30  Breakout: business-scene inventory
   - Each group maps its full business scenes
   - Mark each scene's "pain index" (1–5)
   - Tool: sticky notes + flip chart

10:30-10:45  Break

10:45-12:00  Breakout: requirement-story writing
   - Use user-story format:
     "As a [role], I want [function] so that [value]"
   - Tag each story with business value (high/med/low) and complexity (high/med/low)
   - Tool: user-story cards

12:00-13:30  Lunch

Afternoon: converge

13:30-14:30  Cross-group share & supplement
   - Each group presents stories
   - Others add omissions
   - Merge duplicates

14:30-15:30  MoSCoW prioritization
   - All vote-rank the stories
   - 10 votes each (Must 5, Should 3, Could 2)
   - Tally → priority matrix

15:30-15:45  Break

15:45-16:30  Value-complexity quadrant analysis
   - Map requirements to four quadrants:
     High value + low complexity → Quick Win
     High value + high complexity → Strategic
     Low value + low complexity → Fill-in
     Low value + high complexity → Consider Drop

16:30-17:00  Summarize & next steps
   - Confirm workshop output
   - Action items & owners
   - Follow-up
```

**4.2 Workshop materials list**

- Flip charts (3–5 per group)
- Sticky notes (3 colors × 10 pads per group)
- Markers (5 per group)
- User-story template cards (printed)
- Voting dots (round stickers)
- Business-scene checklist (preset, as facilitation aid)
- Projector / screen (display consensus output)

---

### Step 5: Requirements Documentation (2–3 days)

**Goal**: Convert research output into a formal requirements document.

**Inputs**: All research records, workshop output
**Outputs**: Business Requirements Document (BRD), User Requirements Specification (URS)

**Guidance:**

**5.1 BRD structure**

```
BRD structure:

Ch.1 Document overview
  1.1 Purpose & scope
  1.2 Terms & abbreviations
  1.3 Reference docs

Ch.2 Background & goals
  2.1 Business background
  2.2 Goals & success criteria
  2.3 Scope & boundaries

Ch.3 Stakeholder analysis
  3.1 Stakeholder map
  3.2 Roles & responsibilities
  3.3 Communication needs

Ch.4 Business scenes & process
  4.1 Business-scene landscape
  4.2 AS-IS process (current)
  4.3 TO-BE process (target)
  4.4 Business rules

Ch.5 Functional requirements
  5.1 Functional requirement list
  5.2 User stories (Epic → Feature → Story)
  5.3 Functional detail (by module)
  5.4 UI prototype & interaction notes

Ch.6 Non-functional requirements
  6.1 Performance
  6.2 Security
  6.3 Usability
  6.4 Reliability
  6.5 Maintainability
  6.6 Compatibility

Ch.7 Data requirements
  7.1 Data-source analysis
  7.2 Data entity relationships
  7.3 Data-quality requirements
  7.4 Data-interface requirements

Ch.8 Integration requirements
  8.1 Internal system integration
  8.2 External system interfaces
  8.3 Interface-spec requirements

Ch.9 Constraints & assumptions
  9.1 Technical constraints
  9.2 Business constraints
  9.3 Sector-regulatory constraints
  9.4 Key assumptions

Appendices
  A. Interview summary
  B. Survey stats
  C. Workshop output photos / scans
```

---

### Step 6: Requirements Review and Verification (1–2 days)

**Goal**: Ensure the requirements document is accurate, complete, and feasible via review.

**Inputs**: BRD / URS draft
**Outputs**: Review comments, revised document, sign-off

**Guidance:**

**6.1 Multi-round review framework**

```
Requirements review process:

Round 1: Internal review (our team)
  ├─ Completeness: covers all research findings
  ├─ Consistency: no contradictions
  ├─ Feasibility: technically & resourcing achievable
  └─ Output: internal review comments

Round 2: Client technical review (client IT)
  ├─ Technical soundness: compatibility with existing systems
  ├─ Implementation feasibility: deployment & maintenance
  └─ Output: technical review comments

Round 3: Client business review (client business)
  ├─ Business accuracy: correctly reflects needs
  ├─ Priority reasonableness: ranking acceptable
  └─ Output: business review comments

Round 4: Final confirmation (both sponsors)
  ├─ Scope confirmation: within contract
  ├─ Sign-off: formally freeze baseline
  └─ Output: signed requirements doc
```

**6.2 Requirement acceptance criteria**

Every requirement must meet SMART:
- **S**pecific: clear function / behavior description
- **M**easurable: explicit acceptance criterion
- **A**chievable: within tech / time / budget constraints
- **R**elevant: related to project goals
- **T**estable: test cases can be designed

---

### Step 7: Requirements Prioritization (1 day)

**Goal**: Rank by business value, implementation complexity, dependencies, etc.

**Inputs**: Requirement list, workshop ranking
**Outputs**: Priority matrix, phased-implementation suggestions

**Guidance:**

**7.1 Priority evaluation model**

| Dimension | Weight | Scoring |
|------|:---:|---------|
| Business value | 30% | Contribution to core KPIs (1–5) |
| Urgency | 25% | Regulatory / KPI / safety deadline pressure (1–5) |
| Usage frequency | 15% | Target-user usage frequency (1–5) |
| Implementation difficulty | 20% | Time & effort (5→1, higher = harder) |
| Dependencies | 10% | Whether depended on by others (prereq = 5) |

**Composite priority = Value×0.3 + Urgency×0.25 + Frequency×0.15 + (6−Difficulty)×0.2 + Dependency×0.1**

**7.2 Four-quadrant analysis**

```
        High value
            ↑
            │
  Quick Win  │   Strategic
            │
  ───────────┼──────────→ Low complexity
  Low compl. │   High complexity
            │
  Fill-in    │   Consider Drop
            │
            ↓ Low value
```

---

### Step 8: Requirements Baseline and Change Management

**Goal**: Formally freeze the requirements baseline and establish change control.

**Inputs**: Reviewed & confirmed requirements document
**Outputs**: Baseline version, change-control process

**Guidance:**

**8.1 Baseline**
- Condition: all key stakeholders reviewed & signed
- Output: BRD / URS V1.0 (baseline version)
- Storage: requirements-management tool (e.g., Jira / Azure DevOps)

**8.2 Change-control process**

```
Change request → Impact analysis (scope / schedule / cost / quality) → CCB review
   → Approve / Reject → Update baseline
   ↑                                              │
   └──────────────────────────────────────────────┘
                  Archive change record
```

---

## V. Roles and Responsibilities (RACI Matrix)

| Activity | Req analyst | PM | Client sponsor | Client IT | Client business |
|------|:---:|:---:|:---:|:---:|:---:|
| Research planning | **R/A** | C | I | C | I |
| Stakeholder interviews | **R** | C | I | C | C |
| On-site observation | **R** | I | I | C | **C** |
| Workshop facilitation | **R/A** | C | I | C | C |
| Requirements authoring | **R/A** | C | I | I | I |
| Requirements review | C | C | **A** | **R** | **R** |
| Prioritization | **R** | C | **A** | C | C |
| Baseline & change mgmt | C | **R/A** | C | C | I |

---

## VI. Key Checkpoints

| # | Checkpoint | Pass criterion |
|---|--------|---------|
| CP1 | Research plan review | Covers all stakeholders & business scope |
| CP2 | Interview coverage | Key >95%, general >80% |
| CP3 | Workshop output quality | >30 user stories, priority consensus |
| CP4 | Requirements doc completeness | Covers functional / non-functional / data / integration |
| CP5 | Review passed | All four rounds passed |
| CP6 | Baseline established | Both sides signed, under config mgmt |

---

## VII. Estimated Duration

| Stage | Small (1–2 mo) | Medium (3–6 mo) | Large (6–12 mo+) |
|------|:---:|:---:|:---:|
| Research planning | 0.5 day | 1 day | 2 days |
| Stakeholder interviews | 1–2 days | 3–5 days | 5–10 days |
| On-site observation | 0.5 day | 1–2 days | 2–3 days |
| Workshop | 0.5 day | 1 day | 1–2 days |
| Requirements doc | 1–2 days | 2–3 days | 3–5 days |
| Review & verify | 0.5–1 day | 1–2 days | 2–3 days |
| **Total** | **4–7 days** | **9–14 days** | **15–25 days** |

---

## VIII. Common Pitfalls and Countermeasures

| # | Pitfall | Countermeasure |
|---|------|------|
| 1 | Only listen to execs, not frontline | Balance all three tiers; frontline voice matters |
| 2 | Client can't articulate needs | Scenario questions + prototype to help them "see" needs |
| 3 | Unbounded need creep | Establish baseline, strict change control |
| 4 | Business vs. tech need conflict | Workshop lets both sides talk directly, compromise |
| 5 | Ignore non-functional needs | Mandate a non-functional section in the BRD |
| 6 | Doc becomes decoration | Ensure traceability to design docs & test cases |

---

## IX. Outputs List

1. **Research plan** (.docx)
2. **Stakeholder interview notes & requirement records** (.docx)
3. **Shadowing observation log** (.docx)
4. **Requirements workshop materials & minutes** (.pptx + .docx)
5. **Business Requirements Document (BRD)** (.docx)
6. **User Requirements Specification (URS)** (.docx)
7. **Requirements priority matrix** (.xlsx)
8. **Requirements sign-off** (.docx)

---

> **Version**: V1.0 | **Date**: 2025-07 | **Method**: BABOK + User Stories
