# 02 — Vendor Evaluation & PoC Execution Workflow

## I. Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│              Vendor Evaluation & PoC Execution Workflow Map            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │1. Shortlist│──>│2. PoC Design│──>│3. PoC Prep │──>│4. PoC Execute│ │
│  │  Confirm   │   │  & Plan    │   │  & Environment│ │  & Evaluate │ │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│       │              │              │              │                │
│       v              v              v              v                │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │5. Composite│──>│6. Due Diligence│>│7. Recommendation│>│8. Final Vendor│ │
│  │  Scoring   │   │  & Site Visit  │  │  Report        │  │  Selection   │ │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│                                                                     │
│  Core Methods: PoC (Proof of Concept) | Vendor site visit |         │
│  Multi-dimensional composite evaluation                                  │
└─────────────────────────────────────────────────────────────────────┘
```

## II. Applicable Scenarios

This workflow applies after the RFI shortlist has been established, to conduct in-depth evaluation of candidate vendors — including PoC (Proof of Concept), composite scoring, due diligence, and on-site visits — ultimately producing the recommended vendor.

## III. Prerequisites & Inputs

| Input | Source | Notes |
|-------|------|------|
| Vendor shortlist (3–5 vendors) | [Phase 04 Step 1 — Tech Requirements & RFI/RFP](../phase-04-tech-selection-and-vendor-eval/01-tech-requirements-rfi-rfp-workflow.md) | RFI screening result |
| Technical requirements & SOW | [Phase 04 Step 1 — Tech Requirements & RFI/RFP](../phase-04-tech-selection-and-vendor-eval/01-tech-requirements-rfi-rfp-workflow.md) | Project technical requirements |
| Preliminary evaluation criteria | [Phase 04 Step 1 — Tech Requirements & RFI/RFP](../phase-04-tech-selection-and-vendor-eval/01-tech-requirements-rfi-rfp-workflow.md) | Scoring dimensions reference |

---

## IV. Detailed Steps

---

### Step 1: Shortlist Confirmation & Evaluation Strategy

**Objective**: Finalize the vendors entering in-depth evaluation and define the evaluation strategy.

**Inputs**: RFI analysis report, vendor long-list
**Outputs**: Shortlist confirmation, evaluation strategy document

**Guidance**:

**1.1 Ideal Shortlist Composition (3–5 vendors)**

```
Ideal Shortlist Composition (3–5 vendors):

┌──────────────────────────────────────────┐
│ At least 1 large systems integrator (SI)  │
│  - Strong overall capability, good reputation │
│  - Risk: slow response, limited innovation   │
├──────────────────────────────────────────┤
│ At least 1 transport-domain specialist      │
│  - Deep sector understanding, mature product │
│  - Risk: smaller market share, financial risk│
├──────────────────────────────────────────┤
│ At least 1 innovative specialist vendor     │
│  - Technology-leading, agile responsiveness │
│  - Risk: delivery at scale not yet proven    │
└──────────────────────────────────────────┘
```

**1.2 Evaluation Strategy by Project Type**

| Project Type | PoC Necessity | Site Visit | Evaluation Focus |
|--------------|:---:|:---:|------------------|
| AI / big-data platform | Required | Recommended | Algorithm effect, performance |
| Business application platform | Recommended | Recommended | Function fit, usability |
| Infrastructure platform (IaaS/PaaS) | Required | Recommended | Performance, stability |
| Implementation-services-led | Optional | Required | Team capability, methodology |
| Sovereign-tech substitution | Required | Recommended | Sovereign-tech adaptation, compatibility |

---

### Step 2: PoC Design & Plan

**Objective**: Design a fair, targeted, and operable PoC plan.

**Inputs**: Technical requirements, shortlist
**Outputs**: PoC plan document, PoC scorecard

**Guidance**:

**2.1 PoC Design Principles**

| Principle | Description |
|-----------|-------------|
| Fairness | Identical scenario, data, environment, and time for all vendors |
| Representativeness | Scenarios cover core requirements and surface vendor capability differences |
| Quantifiable | Results scored objectively, not subjectively |
| Time-controlled | 1–3 days PoC execution per vendor |
| Cost-controlled | Reasonable vendor investment (avoid excessive barriers) |

**2.2 Sample Transport-Sector PoC Scenario Design**

```
Smart-Highway AI Video Analysis PoC Scenario Design:

Scenario 1: Traffic Incident Detection (core, weight 40%)
  Test data: 2 hours of real highway surveillance video (labeled)
  Metrics:
    - Stopped-vehicle detection rate > 90%
    - Wrong-way detection rate > 95%
    - Pedestrian intrusion detection rate > 85%
    - Average detection latency < 5 s
    - False-positive rate < 10 per stream per day

Scenario 2: Traffic Parameter Collection (weight 25%)
  Test data: multi-segment, multi-time-period video
  Metrics:
    - Flow-counting accuracy > 95%
    - Speed-estimation error < 10%
    - Vehicle-classification accuracy > 90%

Scenario 3: Interference Robustness (weight 20%)
  Test data: rain/snow, night, occlusion conditions
  Metrics:
    - Detection rate under adverse conditions ≥ 60% of normal

Scenario 4: Platform Capability (weight 15%)
  Test content: API calls, batch processing, result visualization
  Metrics:
    - API response time < 500 ms
    - Concurrent stream support > 50 streams / GPU
```

**2.3 PoC Scorecard Design**

| Scoring Item | Max | Vendor A | Vendor B | Vendor C |
|--------------|:---:|:---:|:---:|:---:|
| Scenario 1 — detection rate | 20 | | | |
| Scenario 1 — false-positive rate | 10 | | | |
| Scenario 2 — accuracy | 15 | | | |
| Scenario 2 — coverage | 10 | | | |
| Scenario 3 — robustness | 10 | | | |
| Scenario 4 — platform capability | 10 | | | |
| On-site performance (professionalism, cooperation) | 10 | | | |
| Implementation proposal (soundness, innovation) | 15 | | | |
| **Total** | **100** | | | |

---

### Step 3: PoC Preparation & Environment Setup

**Objective**: Complete all preparation for PoC execution.

**Inputs**: PoC plan
**Outputs**: PoC environment ready, test data ready, vendor notice issued

**Guidance**:

**3.1 PoC Preparation Checklist**

| Preparation Item | Owner | Completion Standard |
|------------------|-------|---------------------|
| Test environment (servers / GPU) | Client side | Environment configured, vendor can remote-access |
| Test dataset | Client side | Video/image/document datasets prepared & de-identified |
| Test scripts / tools | Client side | Standard scripts for result evaluation |
| PoC plan final confirmation | Both sides | Vendor signs off understanding PoC requirements |
| Schedule | Client side | Time-slot allocation per vendor |
| NDA signed | Both sides | Confidentiality agreement executed |
| Compliance approval | Client side | If client resources are needed |

**3.2 Data Preparation Essentials**

- Test data MUST be **de-identified** (license plates, faces, personal information)
- Test data MUST be **unseen by vendors** (fresh data)
- Test-data labeling MUST pass **dual verification** (two independent labelers agree)
- Prepare sufficient volume (avoid statistical bias)

---

### Step 4: PoC Execution & Evaluation

**Objective**: Execute the PoC fairly and rigorously, and evaluate quantitatively.

**Inputs**: PoC plan, environment, data
**Outputs**: PoC execution log, scoring results

**Guidance**:

**4.1 Single-Vendor PoC Execution Flow**

```
Single-Vendor PoC Execution Flow:

Day 0: Environment Prep
  - Vendor remote-accesses test environment
  - Deploys vendor system
  - Pre-test (confirm environment healthy)

Day 1: PoC Execution
  09:00-09:30  Opening briefing (re-state rules)
  09:30-12:00  Scenario 1 testing
  12:00-13:00  Lunch
  13:00-15:00  Scenario 2 testing
  15:00-17:00  Scenario 3 testing
  17:00-18:00  Platform capability demo

Day 2 (if needed):
  09:00-11:00  Scenario 4 + supplemental testing
  11:00-12:00  Vendor solution walkthrough (implementation proposal)

Day 2/3: Result Compilation
  - Client independently compiles test results
  - Vendor confirms results
```

**4.2 PoC Execution Discipline**

| Discipline | Description |
|-----------|-------------|
| Uniform environment | All vendors use identical hardware configuration |
| Uniform data | All vendors use the same test dataset |
| Uniform time | Each scenario given the same time budget |
| No overfitting | Vendor-specific parameter tuning on test data prohibited |
| Result confidentiality | Do not reveal other vendors' results to any vendor |
| Full recording | PoC process fully recorded (screen capture / shell logs) |

**4.3 PoC Result Handling**

- Objective metrics computed automatically (scripted evaluation)
- Subjective metrics scored independently by ≥ 2 people, then averaged
- Detailed record of vendor feedback points (strengths / weaknesses)
- Per-vendor PoC assessment sub-report produced

---

### Step 5: Composite Evaluation & Scoring

**Objective**: Integrate PoC results with other dimensions for composite scoring.

**Inputs**: PoC scores, technical proposal scores, commercial assessment
**Outputs**: Composite evaluation matrix, ranking result

**Guidance**:

**5.1 Composite Evaluation Dimensions**

| Dimension | Weight | Data Source | Scoring Method |
|-----------|:---:|-------------|----------------|
| PoC technical validation | 30% | PoC execution results | Objective metrics + subjective review |
| Technical proposal | 25% | RFP technical response | Expert review |
| Industry experience | 15% | Case review | Case scoring |
| Team capability | 10% | Interview / résumé review | Interview scoring |
| Commercial terms | 15% | RFP commercial response | Quote + commercial terms |
| Company strength | 5% | Certification / financial review | Objective facts |

**5.2 Composite Score Calculation**

```
Composite Score = PoC×30% + Technical×25% + Experience×15%
                + Team×10% + Commercial×15% + Company×5%
```

**5.3 Weighted Multi-Evaluator Scoring**

| Evaluator | Weight | Role |
|-----------|:---:|------|
| Technical Lead | 30% | Leads technical assessment |
| Business Lead | 25% | Business-fit assessment |
| Project Manager | 20% | Implementation-feasibility assessment |
| Procurement Lead | 15% | Commercial-terms assessment |
| Executive representative | 10% | Strategic-fit assessment |

---

### Step 6: Due Diligence & Site Visit

**Objective**: Conduct due diligence and on-site visits for the top 2–3 vendors.

**Inputs**: Composite evaluation results
**Outputs**: Due-diligence report, site-visit report

**Guidance**:

**6.1 Due-Diligence Checklist**

| Dimension | Content | Method |
|-----------|---------|--------|
| Legal & compliance | Business license, certifications, clean-record certificate | Company registry / credit-check services (e.g., Dun & Bradstreet, national business registries) + original-document check |
| Financial health | Audit reports (last 3 yrs), tax records | Financial data review |
| Intellectual property | Core product software copyrights / patents, open-source compliance | IP inventory + spot check |
| Litigation | Pending cases, administrative penalties | National court records / litigation databases |
| Related-party ties | Any ties to client / evaluation experts | Self-check + background investigation |
| Delivery capacity | Active contract load, delivery-team size | Vendor-provided + client verification |

**6.2 Client Case Verification**

Verify the vendor's claimed key cases:

| Step | Content |
|------|---------|
| 1. Document verification | Request key contract pages (de-identified amounts), acceptance reports |
| 2. Phone verification | Call the case client's IT / business lead (with vendor consent) |
| 3. On-site visit | Visit 1–2 representative case sites to observe system operation |

**6.3 Site-Visit Essentials**

- See the real production system, not a demo system
- Talk to front-line users, not only management
- Observe system health (bug count, response speed)
- Understand after-sales responsiveness and quality

---

### Step 7: Recommendation Report Authoring

**Objective**: Author the vendor-evaluation recommendation report for decision-makers.

**Inputs**: Composite evaluation results, due-diligence report
**Outputs**: Vendor evaluation recommendation report

**Guidance**:

**7.1 Recommendation Report Structure**

```
Vendor Evaluation Recommendation Report:

1. Evaluation Overview
   - Background, scope, process
   - Participating vendor list

2. Evaluation Methodology
   - Dimensions & weights
   - Scoring-rule explanation

3. Per-Vendor Assessment
   For each vendor:
   - Composite score
   - Competitive-strength analysis
   - Risks & gaps
   - PoC results
   - Case-verification results
   - SWOT analysis

4. Comparative Analysis
   - Score-matrix comparison table
   - Core-capability comparison (radar chart)
   - Key-metric comparison (table)

5. Recommendation
   - Ranking & recommended vendor
   - Rationale (core strengths + controllable risk)
   - Fallback option
   - Cooperation suggestion (consortium / subcontracting)

6. Risk Disclosure
   - Key risks of recommended vendor
   - Risk-mitigation suggestions

Appendix
   - Detailed scoring detail
   - Raw PoC test data
   - Due-diligence records
```

---

### Step 8: Final Vendor Selection

**Objective**: Complete the final vendor selection and move into contract negotiation.

**Inputs**: Recommendation report
**Outputs**: Vendor selection notice, next-step plan

**Guidance**:

**8.1 Decision Meeting**

| Agenda | Content | Participants |
|--------|---------|-------------|
| Process briefing | Evaluation method & process | Project Manager |
| Result presentation | Scores & comparison per vendor | Technical Lead |
| Recommendation | Recommended vendor & rationale | Project Manager |
| Discussion & decision | Q&A, discussion, vote | All |
| Next steps | Contract-negotiation plan | All |

**8.2 Selection Notice**

- Issue a letter of intent to the selected vendor
- Issue a courteous notice to non-selected vendors (preserve relationships for future cooperation)
- Provide brief feedback (helps vendors improve, maintains industry relationships)

---

## V. Roles & Responsibilities (RACI Matrix)

| Activity | Technical Lead | Project Manager | Business Lead | Sponsor | Procurement |
|----------|:---:|:---:|:---:|:---:|:---:|
| Shortlist confirmation | C | **R** | C | **A** | C |
| PoC design | **R/A** | C | C | I | I |
| PoC execution | **R** | C | C | I | I |
| PoC scoring | **R/A** | C | C | I | I |
| Composite evaluation | **R** | C | C | I | C |
| Due diligence | C | **R** | I | I | C |
| Client visit | C | **R** | C | I | I |
| Recommendation report | C | **R/A** | C | I | I |
| Final selection | I | C | C | **A** | C |

---

## VI. Key Checkpoints

| # | Checkpoint | Pass Criteria |
|---|------------|---------------|
| CP1 | PoC plan confirmed | All vendors treated fairly, scenarios cover core needs |
| CP2 | PoC data prepared | Dataset de-identified, dual-labeled, unseen by vendors |
| CP3 | PoC discipline | Uniform environment, data, time |
| CP4 | Evaluation consistency | Multi-evaluator score deviation < 15% |
| CP5 | Due diligence complete | Core dimensions 100% covered |
| CP6 | Decision approval | Sponsor formally approves vendor selection |

---

## VII. Estimated Duration

| Phase | Duration |
|------|:---:|
| PoC design & prep | 1–2 weeks |
| PoC execution (3–5 vendors) | 1–2 weeks |
| Composite scoring | 0.5–1 week |
| Due diligence & site visit | 1–2 weeks |
| Report authoring & decision | 0.5–1 week |
| **Total** | **4–8 weeks** |

---

## VIII. Common Pitfalls & Countermeasures

| # | Pitfall | Countermeasure |
|---|---------|----------------|
| 1 | PoC becomes a "beauty contest" ignoring real effect | Design strict objective metrics and automated evaluation tooling |
| 2 | Vendor fakes PoC results | Require deployment in client environment, full monitoring |
| 3 | Evaluation over-weights tech, ignores delivery | Add team-interview and delivery-methodology weight |
| 4 | Ignore vendor long-term stability | Due diligence must review financials and active contract load |
| 5 | Site visit only sees "showcase" projects | Randomly sample verified cases, contact front-line users |

---

## IX. Deliverables List

1. **PoC Plan Document** (.docx)
2. **PoC Test Dataset** (.zip)
3. **PoC Execution Log & Scorecard** (.xlsx)
4. **PoC Result Analysis Report** (.docx)
5. **Composite Evaluation Matrix** (.xlsx)
6. **Due-Diligence Report** (.docx)
7. **Client Case Verification Record** (.docx)
8. **On-Site Visit Report** (.docx)
9. **Vendor Evaluation Recommendation Report** (.docx + .pptx)
10. **Selection Decision Meeting Minutes** (.docx)

---

> **Version**: V1.0 | **Date**: 2025-07
