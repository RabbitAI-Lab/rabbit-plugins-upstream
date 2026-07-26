# 01 — Triple-Bottom-Line (TBL) ROI Modeling & Analysis Workflow

## I. Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│            Triple-Bottom-Line ROI Modeling & Analysis Map             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │1. Benefit  │──>│2. Economic │──>│3. Social   │──>│4. Safety   │ │
│  │  Identify &│   │  Modeling   │   │  Benefit    │   │  Benefit    │ │
│  │  Classify  │   │  Quantify   │   │  Quantify   │   │  Quantify   │ │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│       │              │              │              │                │
│       v              v              v              v                │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │5. Cost &   │──>│6. ROI/NPV │──>│7. Sensitivity│>│8. Report &  │ │
│  │  TCO       │   │  /IRR      │   │  Analysis    │  │  Presentation│ │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│                                                                     │
│  TBL Model: Economic + Social + Safety Benefit = Total Benefit      │
└─────────────────────────────────────────────────────────────────────┘
```

## II. Methodology Foundation

### 2.1 Triple-Bottom-Line Benefit Model for Transport Digitalization

```
           ┌───────────────────────────────┐
           │     Transport Digitalization    │
           │          Benefits              │
           ├───────────────┬───────────────┤
           │               │               │
     ┌─────┴─────┐  ┌──────┴──────┐  ┌─────┴─────┐
     │  Economic  │  │   Social    │  │   Safety   │
     │ (Economic) │  │  (Social)   │  │ (Safety)   │
     └─────┬─────┘  └──────┬──────┘  └─────┬─────┘
           │               │               │
    ·Revenue increase·Mobility experience·Accident reduction
    ·Cost savings   ·Environment uplift ·Casualty reduction
    ·Efficiency gain·Equity uplift      ·Property-loss reduction
    ·Asset utilization·Jobs created     ·Emergency-capability uplift
```

## III. Detailed Steps

---

### Step 1: Benefit Identification & Classification

**Objective**: Systematically identify all benefit points and classify them under the TBL model.

**Inputs**: Project design, business requirements, sector benefit benchmarks
**Outputs**: Benefit-identification list, benefit-classification table

**Guidance**:

**1.1 Benefit Landscape for Transport Digitalization**

```
Benefit Identification Landscape:

┌─────────────────────────────────────────────────────────────┐
│  Economic Benefit                                             │
├─────────────────────────────────────────────────────────────┤
│  Direct economic benefits:                                   │
│  □ Labor-cost savings (inspection / reporting / dispatch /   │
│    customer-service headcount reduction & efficiency)        │
│  □ O&M cost reduction (predictive vs. periodic / reactive)   │
│  □ Energy savings (signal optimization reduces idling,        │
│    smart tunnel-lighting control)                            │
│  □ Toll-collection efficiency (electronic tolling speed-up,   │
│    fewer manual lanes)                                       │
│  □ Material / spare-parts savings (AI-assisted maintenance)   │
│                                                              │
│  Indirect economic benefits:                                 │
│  □ Management-efficiency gain (shorter decisions, better      │
│    collaboration)                                            │
│  □ Asset-utilization gain (equipment / fleet / depot)        │
│  □ Data-asset value (data sharing / monetization potential)  │
│  □ Reduced economic loss (value of time saved, accident loss)│
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  Social Benefit                                               │
├─────────────────────────────────────────────────────────────┤
│  □ Travel-time savings (signal optimization, congestion,      │
│    travel-info services)                                     │
│  □ Mobility-experience uplift (info services, payment ease,   │
│    satisfaction)                                             │
│  □ Environmental benefit (carbon reduction, air-quality)      │
│  □ Equity uplift (inter-city / urban-rural service parity)    │
│  □ Jobs created (new digital-role creation)                   │
│  □ Industry spillover (digital-transport ecosystem growth)    │
│  □ City-image uplift (smart-city showcase)                   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  Safety Benefit                                               │
├─────────────────────────────────────────────────────────────┤
│  □ Traffic-accident reduction (AI early-warning, proactive     │
│    prevention, violation monitoring)                         │
│  □ Casualty reduction (faster emergency response)            │
│  □ Property-loss reduction (fewer accidents + fast handling)  │
│  □ Road-infrastructure safety (bridge / tunnel health         │
│    monitoring, preventive maintenance)                       │
│  □ Public-safety response capability (emergency command,      │
│    video patrol)                                             │
│  □ Cybersecurity protection (security classification, data    │
│    security)                                                 │
└─────────────────────────────────────────────────────────────┘
```

---

### Step 2: Economic-Benefit Modeling & Quantification

**Objective**: Convert economic-benefit points into quantifiable monetary value.

**Inputs**: Benefit-identification list, operations data, sector benchmarks
**Outputs**: Economic-benefit quantification model, annual economic-benefit forecast

**Guidance**:

**2.1 Economic-Benefit Quantification Methods**

| Benefit Type | Quantification | Formula |
|--------------|----------------|---------|
| Labor-cost saving | Headcount reduced × avg. annual salary | ΔE_labor = N_saved × Salary_avg |
| O&M cost reduction | Baseline O&M × reduction ratio | ΔE_ops = Cost_baseline × R_reduction |
| Energy reduction | Baseline energy cost × reduction ratio | ΔE_energy = Cost_baseline × R_reduction |
| Congestion reduction | Delay reduced × value of time × vehicles | ΔE_congestion = ΔT × VOT × N_vehicle |
| Asset utilization | Utilization gain × marginal asset-output value | ΔE_asset = ΔUtil × Asset_value × margin |

**2.2 Sector Benefit Benchmark Reference**

| Benefit | Sector Benchmark | Source |
|---------|------------------|--------|
| AI video inspection vs. manual | 60–80% inspection labor saved | Multiple smart-highway project retrospectives |
| Signal optimization — stops reduced | 15–30% | Traffic-engineering literature |
| Predictive maintenance — O&M reduction | 20–40% | Industrial-internet sector data |
| Electronic tolling — throughput gain | 3–5× manual lane | Sector regulator statistics |
| Faster incident handling — congestion | 20–30% annual congestion-duration reduction | Integrated Transport Operations Coordination Center (TOCC) benefit stats |

**2.3 Year-by-Year Economic-Benefit Forecast**

| Benefit | Y1 | Y2 | Y3 | Y4 | Y5 | 5-Yr Total |
|---------|---:|---:|---:|---:|---:|---:|
| Labor-cost saving | | | | | | |
| O&M cost reduction | | | | | | |
| Energy reduction | | | | | | |
| Congestion economic-loss reduction | | | | | | |
| Asset-utilization gain | | | | | | |
| **Annual Total** | | | | | | |

---

### Step 3: Social-Benefit Modeling & Quantification

**Objective**: Convert social-benefit points into quantifiable value (monetized or non-monetized indicators).

**Inputs**: Benefit-identification list, transport statistics
**Outputs**: Social-benefit quantification model, social-benefit assessment table

**Guidance**:

**3.1 Social-Benefit Monetization Methods**

| Social Benefit | Monetization | Reference Unit Price |
|----------------|--------------|----------------------|
| Travel-time savings | Time saved × value of time | Non-business travel: $4–7 / hour |
| Carbon reduction | CO₂ reduced × carbon price | ≈ $8–14 / ton CO₂ |
| Air-pollution reduction | PM2.5 etc. reduced × abatement cost | Reference environmental agency data |
| Accident reduction | Accidents avoided × social cost per accident | Includes casualty & property loss |

**3.2 Travel-Time Savings Model**

```
Travel-Time Savings Calculation:

ΔT = N_trip × Δt × P_share × 365

Where:
  N_trip: average daily trips (persons / vehicles)
  Δt: average time saved per trip (hours)
  P_share: share of trips affected by the system
  365: annualization factor

Monetization:
  V = ΔT × VOT

  Where VOT (Value of Time):
    - Passenger car: $5–8 / hour (incl. vehicle operating cost)
    - Transit / bus: $3–5 / hour
    - Freight: $11–17 / hour
```

**3.3 Multi-Dimensional Social-Benefit Assessment**

| Social Indicator | Unit | Baseline | Target | Uplift | Population Covered |
|------------------|------|:---:|:---:|:---:|--------------------|
| Average commute time | min | | | | |
| Public mobility satisfaction | score | | | | |
| Travel-info coverage | % | | | | |
| Urban-rural mobility gap | index | | | | |

---

### Step 4: Safety-Benefit Modeling & Quantification

**Objective**: Quantify benefits from safety improvements.

**Inputs**: Traffic-accident statistics, safety-management data
**Outputs**: Safety-benefit quantification model, safety-benefit assessment table

**Guidance**:

**4.1 Traffic-Accident Cost Accounting**

```
Economic Cost per Traffic Accident (reference values):

Accident Level   Direct Loss   Indirect Loss   Total Social Cost
──────────────────────────────────────────────────────────────
Minor            $0.7k–2.8k    $1.4k–7k       $0.7k–15k
General          $2.8k–14k     $7k–28k        $14k–70k
Serious          $14k–70k      $28k–140k      $70k–$0.7M
Major (fatal)    $70k–140k+    $140k–$0.4M+   $0.7M–$1.4M+
                 (+compensation)(+social impact)

Note: Source — sector regulator annual road-safety accident statistics.
```

**4.2 Safety-Benefit Calculation Model**

```
Safety Benefit:

ΔB_safety = Σ(ΔN_grade_i × Cost_per_i)

Where:
  ΔN_grade_i: annual reduction in grade-i accidents
  Cost_per_i: total social cost of a grade-i accident

Accident-reduction forecasting methods:
  Method 1: Historical-trend extrapolation + system-impact correction factor
  Method 2: Controlled experiment (before/after comparison of similar projects)
  Method 3: Expert assessment (safety experts, item-by-item)
```

---

### Step 5: Cost Calculation & TCO

**Objective**: Comprehensively calculate the Total Cost of Ownership (TCO).

**Inputs**: Investment estimate, O&M plan
**Outputs**: TCO analysis table, cost-composition chart

**Guidance**:

**5.1 TCO Composition Model**

```
TCO = CapEx + OpEx

CapEx (Capital Expenditure):
  Construction investment
  └─ Software / Hardware / Integration / Consulting / Training

  Capitalized O&M (if any)
  └─ Ongoing upgrade & transformation investment

OpEx (Operating Expenditure):
  Routine O&M
  ├─ Labor cost (O&M team)
  ├─ Cloud / data-center leasing
  ├─ Software-license renewal
  ├─ Hardware maintenance
  └─ Communications cost

  Continuous optimization
  ├─ Algorithm iteration
  ├─ New-feature development
  └─ Data governance
```

**5.2 5-Year TCO Forecast**

| Cost Item | Y0 (Build) | Y1 | Y2 | Y3 | Y4 | Y5 | 5-Yr Total |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| CapEx | | – | – | – | – | – | |
| OpEx | – | | | | | | |
| **Annual Total** | | | | | | | |

---

### Step 6: ROI / NPV / IRR Analysis

**Objective**: Use standard financial-analysis methods to assess investment value.

**Inputs**: Benefit forecast, cost forecast
**Outputs**: ROI / NPV / IRR calculation, investment-return charts

**Guidance**:

**6.1 Core Metric Calculation**

```
1. ROI (Return on Investment)
   ROI = (Total Benefit − Total Cost) / Total Cost × 100%

2. NPV (Net Present Value)
   NPV = Σ[(Bt − Ct) / (1 + r)^t]
   Bt: benefit in year t
   Ct: cost in year t
   r: discount rate (large projects typically 4–6%)
   t: year index

3. IRR (Internal Rate of Return)
   Discount rate that makes NPV = 0

4. Payback Period
   Year when cumulative net benefit ≥ initial investment
```

**6.2 Transport-Project Return Characteristics**

| Project Type | Typical Payback | Typical 5-Yr ROI | Notes |
|--------------|:---:|:---:|-------|
| Integrated Transport Operations Coordination Center / mobility-management platform | 3–5 yrs | 100–200% | Broad but diffuse benefits |
| Smart highway | 3–5 yrs | 80–150% | High roadside-equipment investment |
| Video-AI platform | 1–2 yrs | 200–400% | Higher ROI |
| Data middle-platform | 2–4 yrs | 100–200% | Benefit release lags |
| Executive decision cockpit | 1–2 yrs | 150–300% | Relatively low investment |

**6.3 Investment-Return Analysis Table**

| Year | Annual Benefit | Annual Cost | Net Benefit | Cumulative Net | Discount Factor (5%) | Discounted Net |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Y0 | 0 | CapEx | −CapEx | −CapEx | 1.000 | −CapEx |
| Y1 | | | | | 0.952 | |
| ... | | | | | | |
| **Total** | | | | | | |

---

### Step 7: Sensitivity Analysis

**Objective**: Identify key uncertainties and assess their impact on investment return.

**Inputs**: ROI model, key assumptions
**Outputs**: Sensitivity-analysis report, tornado / spider chart

**Guidance**:

**7.1 Sensitivity Key Variables**

| Variable | Optimistic (+20%) | Baseline | Pessimistic (−20%) | NPV Impact |
|----------|:---:|:---:|:---:|-----------|
| Labor-cost saving | | | | |
| O&M cost reduction | | | | |
| Construction over-run | | | | |
| Benefit-release delay | | | | |
| OpEx increase | | | | |

**7.2 Scenario Analysis**

| Scenario | Key Assumption | NPV | IRR | Payback |
|----------|----------------|:---:|:---:|:---:|
| Optimistic | Benefits at 110%, cost at 95% | | | |
| Baseline | Benefits at 100%, cost per plan | | | |
| Pessimistic | Benefits at 70%, cost +15% over-run | | | |

---

### Step 8: Report Authoring & Presentation

**Objective**: Author the complete investment-benefit analysis report to support decision-making.

**Inputs**: TBL model, TCO, financial analysis
**Outputs**: Investment-benefit analysis report, presentation deck

**Guidance**:

**8.1 Report Structure**

```
Investment-Benefit Analysis Report:

Executive Summary (1–2 pp.)
  Key conclusions, core metrics, sensitivity conclusions

Chapter 1 — Analysis Overview
  Purpose, scope, method description

Chapter 2 — Triple-Bottom-Line Analysis
  2.1 Economic benefit
  2.2 Social benefit
  2.3 Safety benefit

Chapter 3 — Cost Analysis
  3.1 Investment overview
  3.2 TCO (5-year)
  3.3 Cost benchmarking

Chapter 4 — Investment-Return Analysis
  4.1 Core financial metrics
  4.2 Payback path
  4.3 Sector benchmarking

Chapter 5 — Sensitivity Analysis
  5.1 Single-variable sensitivity
  5.2 Multi-scenario analysis
  5.3 Risk analysis & recommendations

Chapter 6 — Conclusions & Recommendations
```

---

## V. Roles & Responsibilities (RACI Matrix)

| Activity | Economic Analyst | Domain Expert | Technical Expert | Client Finance | Sponsor |
|----------|:---:|:---:|:---:|:---:|:---:|
| Benefit identification | **R** | **R** | C | C | I |
| Economic quantification | **R/A** | C | I | C | I |
| Social quantification | **R** | C | I | I | I |
| Safety quantification | **R** | C | I | I | I |
| Cost calculation | **R** | I | C | C | I |
| Financial analysis | **R/A** | I | I | C | I |
| Sensitivity analysis | **R** | I | I | I | I |
| Report authoring | **R/A** | C | I | I | C |
| Presentation & approval | C | I | I | C | **A** |

---

## VI. Key Checkpoints

| # | Checkpoint | Pass Criteria |
|---|------------|---------------|
| CP1 | Complete benefit identification | TBL coverage, > 5 benefit points per class |
| CP2 | Sufficient quantification basis | Each quantification backed by data source or benchmark |
| CP3 | Complete TCO | CapEx + 5-year OpEx all included |
| CP4 | Reasonable financial metrics | NPV > 0, IRR > discount rate, payback < 5 yrs |
| CP5 | Sufficient sensitivity | Key-variable coverage > 80%, includes pessimistic scenario |
| CP6 | Confirmation | Sponsor accepts analysis conclusions |

---

## VII. Estimated Duration

| Phase | Duration |
|------|:---:|
| Benefit identification & classification | 0.5–1 day |
| TBL modeling & quantification | 2–3 days |
| TCO calculation | 0.5–1 day |
| Financial analysis | 0.5–1 day |
| Sensitivity analysis | 0.5–1 day |
| Report authoring | 1–2 days |
| **Total** | **5–9 days** |

---

## VIII. Deliverables List

1. **Benefit-Identification List** (.xlsx)
2. **Triple-Bottom-Line Quantification Model** (.xlsx)
3. **TCO Analysis Table** (.xlsx)
4. **ROI / NPV / IRR Calculation** (.xlsx)
5. **Sensitivity-Analysis Model** (.xlsx)
6. **Investment-Benefit Analysis Report** (.docx)
7. **Investment-Benefit Presentation** (.pptx)

---

> **Version**: V1.0 | **Date**: 2025-07 | **Economic Reference**: Cost-Benefit Analysis (CBA), Project Evaluation Methodology
