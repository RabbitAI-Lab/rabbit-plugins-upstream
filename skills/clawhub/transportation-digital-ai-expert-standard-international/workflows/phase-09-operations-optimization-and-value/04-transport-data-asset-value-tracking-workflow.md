# 04 — Transport Data-Asset Value Tracking Workflow

## 1. Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                Transport Data-Asset Value Tracking Map                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │1.Data     │──>│2.Value    │──>│3.Value    │──>│4.Data      │        │
│  │  Asset     │   │  Model    │   │  Tracking │   │  Service   │        │
│  │  Inventory │   │  Build    │   │  Monitor  │   │  Productize│       │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│       │              │              │              │                │
│       v              v              v              v                │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │5.Data     │──>│6.Data     │──>│7.Value    │──>│8.Data      │        │
│  │  Security  │   │  Compliance│   │  Report   │   │  Strategy  │        │
│  │  & Access │   │  & Privacy│   │  Author   │   │  Evolution │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Detailed Steps

---

### Step 1: Data-Asset Inventory

**Objective**: Comprehensively inventory transport data assets; build a data-asset catalog.

**Guidance:**

**1.1 Transport data-asset classification**

| Category | Sub-class | Core data |
|---------|---------|---------|
| Infrastructure | Road network / bridges-tunnels / stations / devices | Segment attrs, bridge-tunnel BIM, device ledger |
| Dynamic operations | Flow / incident / tolling / weather | Flow series, incident records, tolling (ETC/RFID) transactions |
| Business mgmt | Maintenance / emergency / enforcement / service | Maintenance records, emergency plans, hotline tickets |
| Mobility service | OD / travel behavior / preference | Trip paths, mode choice, payment habits |
| Enterprise mgmt | HR / finance / assets / engineering | Org, budget, contracts, asset ledger |
| External | Weather / POI / sentiment / maps | Weather, navigation data, social media |

**1.2 Data-asset catalog template**

| Asset name | Domain | Volume | Update freq | Criticality | Users | Data Owner |
|------------|----------|:---:|:---:|:---:|---------|----------|
| 5-min traffic flow | Ops monitoring | 50TB | 5 min | ★★★ | Ops / Maint. | Info Center |

---

### Step 2: Value-Assessment Model Build

**Objective**: Build a model to assess data-asset value.

**Guidance:**

**2.1 Five-dimension data-value model**

| Dimension | Description | Score (1–5) |
|---------|------|:---:|
| Business-support value | Indispensability to core business | |
| Decision-support value | Support to management decisions | |
| Share-reuse value | Degree shared/reused by depts / systems | |
| Innovation-dev value | Value to AI / data-product development | |
| External-exchange value | Value to external (authority / public / market) | |

**2.2 Value-index calculation**

```
Value index = Σ(dimension score × weight)

Recommended weights:
  Business 30% + Decision 25% + Share-reuse 20% + Innovation 15% + External 10%

Value tiers:
  · A (index >4.0): Core data asset — protect & monetize
  · B (index 3.0–4.0): Important data asset — keep optimizing
  · C (index <3.0): General data asset — manage normally
```

---

### Step 3: Value-Tracking Metrics Monitoring

**Objective**: Establish a continuous data-value tracking framework.

**Guidance:**

**3.1 Data-value tracking metrics**

| Category | Metric | Description |
|---------|------|------|
| Usage volume | API calls / month | Frequency data is accessed & used |
| Users | Distinct depts / systems using data | Coverage |
| Data-driven decisions | Decisions based on data | Actual influence |
| Data quality | Data-quality incidents | Trustworthiness |
| Application scenarios | Apps / models built on data | Innovative use |
| Sharing records | External sharing count & scope | Circulation value |

**3.2 Data-value dashboard**

```
Data-value dashboard (monthly):

  ┌──────────────┬──────────────┬──────────────┐
  │ API calls:   │ Active users:│ Data products:│
  │ 1.25M / mo   │ 8 depts      │ 15           │
  │  ↑ 12%      │  ↑ 1 new     │  ↑ 3 new     │
  ├──────────────┼──────────────┼──────────────┤
  │ Data quality:│ Data sharing:│ Decision impact:│
  │ 99.2% acc.  │ 5 shares/mo  │ 12 decisions/mo│
  │  → stable    │  ↑ 2        │  ↑ 25%       │
  └──────────────┴──────────────┴──────────────┘
```

---

### Step 4: Data-Service Productization

**Objective**: Turn data assets into reusable data-service products.

**Guidance:**

**4.1 Data-service product types**

| Type | Description | Example |
|---------|------|------|
| Data API | Standardized query interface | Real-time traffic API, flow-stats API |
| Data report | Periodic analysis report | Monthly traffic-ops report |
| Data dashboard | Visualized display | Exec cockpit, ops wallboard |
| Data model | AI / analytics model output | Congestion-prediction, crash-risk model |
| Data subscription | Data push service | Real-time anomaly-event push |

**4.2 Data-product pricing reference**

| Model | Description | Scenario |
|---------|------|---------|
| Per-call | Billed by API call count | High-frequency APIs |
| Subscription | Monthly / quarterly / annual | Reports / dashboards |
| Per-project | One-time project delivery | Deep analysis / custom model |
| Value-share | Revenue share from data value | Joint data operation |

---

### Steps 5–8: Security, Compliance & Strategy Evolution

**5. Data security & access:**
- Data classification & grading (per data-security regulation)
- Least-privilege data access
- Auditable review log of data operations

**6. Data compliance & privacy:**
- Personal-data protection (GDPR / local equivalent)
- Masking / anonymization of mobility data
- Cross-border data-transfer assessment (where applicable)

**7. Value report authoring:**
- Quarterly data-asset value report
- Data-usage benefit analysis

**8. Data-strategy evolution:**
- From "data resource" → "data asset" → "data capital"
- Explore data exchange / data-element market participation
- Data-asset capitalization (see [phase-10-02-data-asset-capitalization-workflow](../phase-10-post-evaluation-and-iteration/02-data-asset-capitalization-workflow.md))

---

## 3. Output Catalog

1. **Data-asset catalog** (.xlsx)
2. **Data-asset value-assessment report** (.docx)
3. **Data-value tracking dashboard** (BI board)
4. **Data-service product list** (.xlsx)
5. **Data classification & grading list** (.xlsx)
6. **Quarterly data-asset value report** (.pptx)

---

> **Version**: V1.0 | **Date**: 2025-07
