# 02 — Data-Driven Operations Optimization Workflow

## 1. Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│               Data-Driven Ops Optimization Map                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │1.KPI      │──>│2.Data     │──>│3.Data     │──>│4.Insight  │        │
│  │  System   │   │  Collection│   │  Analysis  │   │  & Opportunity│    │
│  │  Build    │   │  & Integ. │   │  & Diag.  │   │  Identify  │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│       │              │              │              │                │
│       v              v              v              v                │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │5.A/B Test│──>│6.Optimiz. │──>│7.Effect   │──>│8.Iterate  │        │
│  │  & Exp.  │   │  Execute  │   │  Assess   │   │  Loop     │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│                                                                     │
│  Core idea: Collect → Analyze → Insight → Act → Assess → Iterate (PDCA)
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Detailed Steps

---

### Step 1: KPI System Build

**Objective**: Build a data-driven KPI system covering all operations domains.

**Guidance:**

**1.1 Four-layer transport-operations KPI pyramid**

```
        ┌─────────────┐
        │ Strategic KPI│  3–5: road-network health index, safety-score
        │ (exec)      │
        ├─────────────┤
        │ Management KPI│  8–12: event-detection rate, handling time,
        │ (mgmt)      │  maintenance compliance
        ├─────────────┤
        │ Operations KPI│  20–30: device online rate, data accuracy,
        │ (ops)       │  ticket throughput
        └─────────────┘
```

**1.2 Core transport-operations KPI examples**

| Category | KPI | Calculation | Baseline |
|---------|-----|---------|:---:|
| Network efficiency | Network congestion index | Actual travel time / free-flow travel time | <1.5 |
| Incident mgmt | Mean detection-to-clearance time | Clear time − detect time | <30min |
| Maintenance quality | Pavement-defect repair timeliness | On-time repairs / total defects | >95% |
| Device O&M | Field-device online rate | Online devices / total devices | >98% |
| Data quality | Core-data accuracy | Correct records / sample total | >99% |
| Public service | Hotline answer rate | Answered / incoming calls | >95% |
| Resource use | Device utilization | Actual use / rated capacity | >75% |

---

### Step 2: Data Collection & Integration

**Objective**: Build an automated operations-data collection and integration framework.

**Guidance:**

**2.1 Operations-data collection landscape**

| Domain | Source | Method | Freq |
|-------|-------|-----------|:---:|
| Business ops | Business systems | API / ETL | Real-time / daily |
| O&M | ITSM / monitoring | API | Real-time |
| IoT | Field devices | MQTT / Kafka | Real-time |
| User behavior | Tracking / logs | SDK / log collect | Real-time |
| External | Weather / maps / sentiment | API / crawler | Hourly |

**2.2 Continuous data-quality monitoring**

Run data-quality checks on core operations data monthly:
- Completeness: missing-rate of key fields
- Timeliness: data-latency distribution
- Accuracy: vs. sampling / third-party comparison
- Consistency: cross-system data consistency

---

### Steps 3–4: Data Analysis & Insight Discovery

**Objective**: Discover operations-optimization opportunities through analysis and mining.

**Guidance:**

**3.1 Four analytics methods**

| Method | Question | Transport example |
|------|-----------|------------|
| Descriptive | What happened? | How many crashes last month? Where? |
| Diagnostic | Why did it happen? | Why high crash rate on a segment? Weather / flow / design? |
| Predictive | What will happen? | Predict next week's most congested time window |
| Prescriptive | What should we do? | Where to deploy patrols, when to divert |

**3.2 Typical transport-operations analysis scenarios**

```
Typical analysis scenarios:

1. Congestion-cause analysis
   Input: flow + incident + work-zone + weather data
   Output: Top 5 congestion causes & contribution

2. Maintenance-decision optimization
   Input: pavement-defect + flow + repair-cost data
   Output: optimal maintenance timing & method suggestion

3. Device-failure prediction
   Input: device logs + environment + maintenance records
   Output: 72h device-failure risk list

4. Citizen-service hot-topic analysis
   Input: hotline ticket text + NLP
   Output: Top 10 citizen-concern topics & sentiment
```

---

### Step 5: A/B Testing & Experimentation

**Objective**: Validate optimization effect through controlled experiments.

**Guidance:**

**5.1 Transport A/B test design**

| Scenario | A (control) | B (treatment) | Metric |
|------|---------|---------|---------|
| Signal timing | Existing plan | New plan | Mean delay |
| VMS message strategy | Fixed format | Personalized | Driver compliance |
| Maintenance scheduling | Fixed cycle | Data-driven | Cost / defect progression |

**5.2 A/B test SOP**

```
A/B test SOP:

1. Define hypothesis
   "If AI dynamic signal timing is adopted, peak delay drops ~15%"

2. Select test area / time
   - Pick 2–3 similar intersections
   - Control variables (flow / geometry as similar as possible)

3. Determine sample size & period
   - At least 2 weeks of comparison data
   - Avoid holidays / anomalous dates

4. Execute test
   - Strictly prevent A/B cross-contamination

5. Statistical analysis
   - T-test for significance

6. Conclude
   - Adopt / reject / adjust hypothesis
```

---

### Steps 6–8: Optimize → Assess → Iterate Loop

**6. Optimize execution:** Based on insights and A/B results, plan and execute optimization.

**7. Effect assessment:**
- Compare pre/post optimization KPI changes
- Compute actual ROI
- Identify unexpected side effects

**8. Iterate loop:**
- Monthly operations-data review meeting
- Quarterly optimization retrospective
- Continuous optimize → continuous measure → continuous iterate

---

## 3. Roles & Responsibilities (RACI Matrix)

| Activity | Data Analyst | Ops Manager | Business Owner | IT O&M |
|------|:---:|:---:|:---:|:---:|
| KPI system | **R** | **A** | C | I |
| Data collection | C | I | I | **R/A** |
| Data analysis | **R/A** | C | C | I |
| Insight discovery | **R** | C | **A** | I |
| A/B test | **R** | C | **A** | C |
| Effect assessment | **R/A** | C | C | I |

---

## 4. Key Checkpoints

| # | Checkpoint | Pass standard |
|---|--------|---------|
| CP1 | KPI system live | Core KPIs viewable real-time on dashboard |
| CP2 | Data-quality baseline | Core-data accuracy >95% |
| CP3 | First analysis done | ≥3 operations-optimization insights |
| CP4 | A/B test done | ≥1 optimization measure validated |
| CP5 | Monthly retro running | Monthly meeting established & running |

---

## 5. Estimated Duration

| Stage | Duration |
|------|:---:|
| KPI system build | 1–2 wks |
| Data-collection config | 2–4 wks |
| First analysis | 1–2 wks |
| Continuous optimization | Ongoing (monthly loop) |

---

## 6. Output Catalog

1. **KPI system document** (.docx)
2. **Operations-data dashboard** (BI board)
3. **Monthly operations-analysis report** (.pptx)
4. **A/B test experiment report** (.docx)
5. **Optimization effect-assessment report** (.docx)
6. **Quarterly optimization retrospective** (.pptx)

---

> **Version**: V1.0 | **Date**: 2025-07
