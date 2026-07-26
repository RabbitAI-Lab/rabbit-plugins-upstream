# 03 — Digital Capability Maturity Re-Assessment & Continuous Evolution

## 1. Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│          Maturity Re-Assessment & Continuous Evolution Map            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │1.Re-Assess│──>│2.Maturity │──>│3.Trend    │──>│4.Gap       │        │
│  │  Prep &   │   │  Re-Assess│   │  Analysis │   │  Update &  │        │
│  │  Baseline │   │  Execute  │   │  & Bench. │   │  Identify  │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│       │              │              │              │                │
│       v              v              v              v                │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │5.New-Gen │──>│6.Evolution│──>│7.Annual   │──>│8.Ecosystem │        │
│  │  Tech     │   │  Roadmap  │   │  Planning │   │  Build &   │        │
│  │  Radar    │   │          │   │  Linkage  │   │  Expand    │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│                                                                     │
│  Idea: Assess → Plan → Build → Operate → Re-Assess (PDCA loop)     │
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Applicable Scenarios

This workflow applies 1–2 years after go-live, to re-assess the client's digital capability, compare against the baseline, identify new gaps and opportunities, and formulate a new evolution roadmap.

## 3. Recommended Cadence

```
Continuous-evolution cadence:

  Annual:     Full maturity re-assessment + 3-yr roadmap roll-forward
  Semi-annual: Value-realization tracking + new-gen tech-radar update
  Quarterly:  KPI review + benchmark comparison
  Monthly:     Ops-data analysis + user-feedback handling
```

---

## 4. Detailed Steps

---

### Step 1: Re-Assessment Prep & Baseline Review

**Objective**: Review baseline conclusions; prepare re-assessment.

**Inputs**: T-DMM baseline report, project records, operations data
**Outputs**: Re-assessment plan, baseline-review report

**Guidance:**

**1.1 Baseline-review points**

| Review item | Content |
|-------|------|
| Baseline score | Last assessment's six-dimension & overall scores |
| Improvement targets | Last-set target values per dimension |
| Completed projects | List of delivered digital projects |
| Expected uplift | Expected maturity gain per project |

**1.2 Re-assessment scope confirmation**

- Expand scope (new business domain / new subsidiary)?
- Adjust criteria (regulatory change / tech progress)?
- Add new dimensions (e.g., data asset / green-low-carbon)?

---

### Step 2: Maturity Re-Assessment Execution

**Objective**: Re-assess per the T-DMM methodology.

**Inputs**: Re-assessment plan, ops data, stakeholder contacts
**Outputs**: Re-assessment scores, re-assessment report

**Guidance:**

**2.1 Re-assessment method**

Reuse the T-DMM six-dimension framework (see [phase-02-01-t-dmm-maturity-assessment-workflow](../phase-02-current-state-diagnosis-and-maturity/01-t-dmm-maturity-assessment-workflow.md)), but:
- Questionnaire can be trimmed to a change-perception version (only changed parts)
- Focus on maturity uplift from implemented projects
- Include ≥1 veteran of the baseline team (consistency)

**2.2 Score comparison**

| Dimension | Baseline (Y0) | Re (Y2) | Δ | Target | Rate |
|------|:---:|:---:|:---:|:---:|:---:|
| Strategy & Governance | 2.8 | 3.5 | +0.7 | 3.5 | 100% |
| Business Digitalization | 2.2 | 3.2 | +1.0 | 3.0 | 107% |
| Data Capability | 1.8 | 2.8 | +1.0 | 2.5 | 112% |
| Technology Base | 2.5 | 3.5 | +1.0 | 3.5 | 100% |
| Organization & Talent | 2.0 | 2.5 | +0.5 | 3.0 | 83% |
| Security & Compliance | 3.2 | 3.8 | +0.6 | 4.0 | 90% |
| **Overall** | **2.4** | **3.2** | **+0.8** | **3.2** | **100%** |

---

### Step 3: Trend Analysis & Benchmarking

**Objective**: Analyze maturity trend; benchmark against industry leaders.

**Guidance:**

**3.1 Maturity trend chart**

```
Maturity trend:

  Level 5 ┤
          │
  Level 4 ┤                              ▲ ?(target)
          │                     ▲ Y2(3.2)
  Level 3 ┤              ▲ Y1(2.8)
          │         ▲ Y0(2.4)
  Level 2 ┤    ▲
          │
  Level 1 ┤
          └─────┬─────┬─────┬─────┬─────
               Y0    Y1    Y2    Y3    Y4
              (base) (mid) (re) (tgt)(vision)
```

**3.2 Benchmark update**

| Dimension | Last bench | This bench | Leader moved? |
|---------|:---:|:---:|:---:|
| Peer average | 2.6 | 2.9 | Industry progressing |
| Leader level | 3.8 | 4.0 | Leader advancing too |
| Gap to leader | -1.4 | -0.8 | Gap narrowing |

Key conclusion: We advanced 0.8, industry advanced 0.3, gap narrowed.

---

### Step 4: Gap Update & Identification

**Objective**: Identify new gaps and unmet improvement targets.

**Guidance:**

**4.1 New-gap analysis**

| New gap | Source | Cause |
|-------|------|---------|
| Org & talent short (2.5 vs 3.0) | Re-assessment | Slow hiring, low training coverage |
| Shallow AI depth | Tech benchmark | AI in only 2–3 scenarios |
| Data-asset ops not started | New dimension | Not capitalized, not productized |

**4.2 Org & talent root-cause (5-Why)**

1. Why low talent rate? — Key roles not filled
2. Why not filled? — Pay not competitive
3. Why not competitive? — Digital-talent pay band unchanged
...

---

### Step 5: New-Generation Tech Radar

**Objective**: Scan new-gen tech trends; assess their transport-digital impact.

**Guidance:**

**5.1 Tech-radar quadrants**

```
New-gen transport-digital tech radar:

  ┌────────────────────┬────────────────────┐
  │  Adopt             │  Trial             │
  │  ·LLM             │  ·Transport GPT /  │
  │  ·Multimodal AI   │   domain LLM       │
  │  ·Cloud-native     │  ·VIC V2X         │
  │   Serverless       │  ·Digital-twin sim │
  ├────────────────────┼────────────────────┤
  │  Assess           │  Hold             │
  │  ·Quantum (opt.)  │  ·Metaverse traffic│
  │  ·6G comms        │  ·Full AV (L5)     │
  │  ·BCI             │  ·Flying-car mgmt  │
  └────────────────────┴────────────────────┘
```

**5.2 Tech-impact assessment**

| Tech | Maturity | Transport impact | Action | Window |
|------|:---:|------|---------|:---:|
| LLM | High | Smart helpdesk, auto-reports, KM | Adopt now | Now |
| Transport LLM | Med | Event analysis, maintenance KB | Start PoC | 3–6 mo |
| VIC | Med | AV coordination, full awareness | Track standard | 12–18 mo |
| Data assetization | High | Capitalization, financing | Pilot | 3–6 mo |

---

### Step 6: Continuous-Evolution Roadmap

**Objective**: Based on re-assessment & trends, build a new evolution roadmap.

**Guidance:**

**6.1 New 3-year evolution roadmap**

```
Evolution roadmap (Y3–Y5):

  Year 3 (Consolidate)   Year 4 (Intelligent)   Year 5 (Lead)
 ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
 │ ·Close talent gap│  │ ·AI covers 80%  │  │ ·Transport LLM   │
 │ ·Data-asset pilot│  │ ·Digital twin   │  │ ·Data-asset scale│
 │ ·Deepen org change│ │ ·VIC pilot      │  │ ·External capability│
 │ ·Harden security │  │ ·Data-asset ops │  │ ·Industry standards│
 └─────────────────┘  └─────────────────┘  └─────────────────┘

  Target maturity: 3.8      Target: 4.3          Target: 4.8
```

**6.2 Roll-forward mechanism**

Same as the 3-year roadmap in [phase-03-04-three-year-roadmap-and-investment-workflow](../phase-03-strategy-and-top-level-design/04-three-year-roadmap-and-investment-workflow.md), rolled forward annually:
- Review last year's achievement
- Adjust future plan per latest regs / tech / business
- Keep "plan 3 yrs, detail 1 yr, update quarterly"

---

### Step 7: Annual-Planning Linkage

**Objective**: Link the evolution roadmap with the client's annual IT plan & budget.

**Guidance:**

**7.1 Annual-linkage timeline**

```
Annual-linkage cadence:

  Sep–Oct: Maturity re-assessment → evolution roadmap draft
  Oct–Nov: Discuss & confirm next-year digital priorities
  Nov–Dec: Assist client's annual IT plan & budget
  Dec–Jan: Assist budget filing & approval
  Jan–Mar: Next-year project launch prep
```

---

### Step 8: Ecosystem Build & Expand

**Objective**: Upgrade from single-project cooperation to digital-ecosystem partnership.

**Guidance:**

**8.1 Partnership ladder**

```
Partnership ladder:

  Level 4: Ecosystem partner ← co-create standards, joint innovation
  Level 3: Strategic partner  ← long-term framework, annual planning, lab
  Level 2: Preferred vendor   ← Phase 2/3 renewal, continuous service
  Level 1: Project vendor     ← complete Phase 1

  Goal: lift every client from L1/L2 to L3/L4
```

**8.2 Ecosystem actions**

- Joint innovation lab: co-develop transport-AI apps
- Industry-standard participation: help client join industry / regional standard-setting
- Ecosystem alliance: bring complementary vendors into a solution ecosystem
- Talent cultivation: partner with universities for targeted transport-digital talent
- Brand co-build: jointly publish whitepapers, cases, industry reports

---

## 5. Roles & Responsibilities (RACI Matrix)

| Activity | CSM | Strategy Advisor | Tech Expert | Client Sponsor | Client IT |
|------|:---:|:---:|:---:|:---:|:---:|
| Re-assessment | C | **R/A** | C | I | C |
| Trend analysis | I | C | **R/A** | I | I |
| Gap ID | C | **R/A** | C | C | I |
| Tech radar | I | C | **R/A** | I | C |
| Evolution roadmap | C | **R/A** | C | C | I |
| Annual linkage | **R** | C | I | **A** | C |
| Ecosystem build | C | C | I | **A** | I |

---

## 6. Key Checkpoints

| # | Checkpoint | Pass standard |
|---|--------|---------|
| CP1 | Re-assessment done | Six-dimension scores vs. baseline |
| CP2 | Trend analysis | Maturity trend + benchmark update |
| CP3 | Evolution roadmap | New roadmap endorsed by client |
| CP4 | Annual linkage | Evolution content in client's annual IT plan |
| CP5 | Partnership upgrade | Cooperation upgraded to strategic / ecosystem level |

---

## 7. Estimated Duration

| Stage | Duration |
|------|:---:|
| Re-assess prep & exec | 2–3 wks |
| Trend & gap analysis | 1 wk |
| Tech-radar update | 1 wk |
| Evolution roadmap | 1–2 wks |
| Annual linkage | Synced with client planning (1–2 mo) |

---

## 8. Output Catalog

1. **Maturity re-assessment report** (.docx + .pptx)
2. **Maturity trend chart** (.pptx)
3. **Benchmark-update report** (.docx)
4. **New-gen tech radar** (.pptx)
5. **Tech-impact assessment** (.docx)
6. **Continuous-evolution roadmap** (.pptx + .docx)
7. **Annual digital-planning linkage advice** (.docx)
8. **Ecosystem-partner build plan** (.docx)

---

> **Version**: V1.0 | **Date**: 2025-07 | **Idea**: PDCA continuous evolution
