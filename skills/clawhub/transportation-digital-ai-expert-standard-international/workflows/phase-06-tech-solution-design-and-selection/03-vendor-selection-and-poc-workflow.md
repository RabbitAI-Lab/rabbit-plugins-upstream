# 03 — Vendor Selection & PoC Execution Workflow

## 1. Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│               Vendor Selection & PoC Execution Map                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │1.Reqs &  │──>│2.Market   │──>│3.Shortlist│──>│4.RFI/RFP │        │
│  │  RFI Design│  │  Research │   │  Screening │   │  Issue &   │        │
│  │           │   │  Longlist │   │            │   │  Responses │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│       │              │              │              │                │
│       v              v              v              v                │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │5.PoC     │──>│6.PoC Exec│──>│7.Eval &  │──>│8.Recommend│        │
│  │  Design  │   │  & Verify│   │  Score    │   │  & Decide │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│                                                                     │
│  Core Deliverables: Vendor longlist/shortlist | RFI/RFP docs       │
│    PoC test report | Vendor evaluation report | Recommendation    │
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Applicable Scenarios

This workflow takes the perspective of the **technology-solution buyer** and guides how to systematically evaluate and select technology vendors. It applies to:

- Large-platform selection: ITMP / TOCC / digital-twin platform
- Product selection: signal-control systems / tolling (e.g., ETC/RFID) systems / V2X devices
- System integrator / O&M service provider selection
- Technical-solution competition evaluation

## 3. Preconditions

| Input | Source | Description |
|-------|--------|-------------|
| Technical requirements specification | [phase-06-01-tech-solution-design-workflow](../phase-06-tech-solution-design-and-selection/01-tech-solution-design-workflow.md) | Functional / non-functional requirement definitions |
| Investment budget envelope | phase-05-financing-and-investment-review | Budget ceiling |
| Technical architecture design | [phase-06-01-tech-solution-design-workflow](../phase-06-tech-solution-design-and-selection/01-tech-solution-design-workflow.md) | Logical / physical / data / security architecture |
| Vendor landscape | SKILL.md, Part 5 (Transport Tech Vendor Landscape) | 12 categories × 140+ vendors |
| Solution evaluation framework | SKILL.md, Part 17 (Five-Dimension Evaluation Model) | Five-dimension evaluation model |

---

## 4. Detailed Step-by-Step

---

### Step 1: Requirement Definition & RFI Design (Weeks 1–2)

**Objective**: Clarify the procured technical requirements; design the RFI (Request for Information) questionnaire.

**Inputs**: Technical requirements specification
**Outputs**: RFI document, vendor longlist (≥10 vendors)

**RFI design focus:**
| Info category | Key questions | Purpose |
|------|------|------|
| Company profile | Founded / size / transport-revenue share / R&D ratio | Assess stability & industry focus |
| Product / solution | Core product architecture / tech stack / deployment model / scalability | Assess solution fit |
| Client cases | Number / scale of comparable projects / referenceable clients | Verify delivery capability |
| Service system | Implementation team size / O&M SLA / local support | Assess service assurance |
| Commercial info | Pricing model / typical project price band | Preliminary commercial feasibility |

---

### Step 2: Market Research & Longlist (Weeks 2–3)

**Objective**: Comprehensively scan the market to form the longlist.

**Information sources:**
- SKILL.md, Part 5 (Transport Tech Vendor Landscape)
- Industry reports (IDC / Gartner / ERTICO–ITS Europe / ITS America)
- Client word-of-mouth / industry conferences / tech communities
- Vendor websites / case showcases / technical white papers

**Longlist inclusion criteria:**
| Criterion | Threshold |
|------|------|
| Product / solution relevance | Product directly covers ≥70% of the procured functional domains |
| Transport industry experience | At least 1 delivered comparable transport project |
| Corporate stability | Founded ≥3 yrs, no major operational risk |
| Technology direction | Tech roadmap aligned with the procured direction |

---

### Step 3: Vendor Shortlist Screening (Weeks 3–4)

**Objective**: Screen 3–5 vendors from the longlist into the shortlist (PoC candidates).

**Screening dimensions & weights:**

| Dimension | Weight | Data source | Method |
|------|:---:|------|------|
| Functional fit | 30% | RFI response / product demo | Requirement-coverage matrix scoring |
| Technical architecture | 25% | RFI response / tech exchange | Architecture review |
| Transport experience | 20% | Case list / client callback | Similar-project count + scale |
| Implementation & O&M | 15% | RFI response / client callback | Team size / localization depth |
| Commercial feasibility | 10% | Preliminary quote / public financials | Price band / financial health |

**Shortlist decision meeting:**
- Participants: evaluation team (architect + domain expert + procurement + PM)
- Output: 3–5 shortlisted vendors, each with explicit inclusion rationale and points to validate

---

### Step 4: RFI/RFP Issuance & Response (Weeks 4–6)

**Objective**: Issue formal RFI/RFP to shortlisted vendors; collect detailed responses.

**RFP document structure:**
```
1. Project overview & background
2. Technical requirements specification (functional + non-functional)
3. Response requirements & scoring criteria
4. Technical-solution requirements (architecture / implementation / O&M / training)
5. Commercial requirements (pricing / payment / warranty / IP)
6. Response timeline & submission process
```

**Response management:**
- Establish a single Q&A channel (written, to ensure fairness)
- Organize vendor tech-exchange sessions (uniform briefing, avoid information asymmetry)
- Open unified evaluation after the response deadline

---

### Step 5: PoC Design & Scenario Definition (Weeks 5–6)

**Objective**: Design the PoC plan; define validation scenarios and success criteria.

**PoC scenario selection principles:**
1. **Highest risk first**: Prioritize the highest technical-risk scenarios
2. **Core value first**: Prioritize scenarios contributing most business value
3. **Comparable first**: Scenarios must yield quantifiable comparative data
4. **Time-boxed**: PoC duration ≤ 6 weeks

**PoC scenario template:**

| Scenario ID | Description | Validation focus | Input data | Success criteria | Weight |
|:---:|------|------|------|------|:---:|
| PoC-1 | [desc] | [tech/func/perf] | [type/volume] | [quantified] | 30% |
| PoC-2 | [desc] | [tech/func/perf] | [type/volume] | [quantified] | 25% |
| PoC-3 | [desc] | [tech/func/perf] | [type/volume] | [quantified] | 25% |
| PoC-4 | [desc] | [tech/func/perf] | [type/volume] | [quantified] | 20% |

---

### Step 6: PoC Execution & Verification (Weeks 6–10)

**Objective**: Run PoCs in parallel in a unified environment; produce comparable evaluation data.

**PoC execution principles:**
- **Unified environment**: All vendors use identical hardware and test data
- **Unified criteria**: All vendors evaluated against the same success criteria
- **Parallel execution**: Vendors run simultaneously to minimize timing bias
- **Full recording**: Record each test scenario; retain raw data

**PoC execution stages:**

| Stage | Content | Duration | Output |
|------|------|:---:|------|
| Environment prep | Vendor deploys env / imports test data | Week 1 | Env-ready confirmation |
| Functional validation | Validate core functions per PoC scenario | Weeks 2–3 | Functional validation log |
| Performance testing | Load / stability / boundary testing | Week 4 | Performance test report |
| Holistic evaluation | UX / O&M experience / doc quality | Week 5 | Holistic evaluation log |
| Evaluation summary | Consolidate data / write PoC report | Week 6 | PoC evaluation report |

---

### Step 7: Comprehensive Evaluation & Scoring (Weeks 10–11)

**Objective**: Combine RFI response + PoC results + commercial terms into a final evaluation.

**Evaluation dimensions & data sources:**

| Dimension | Weight | RFI data | PoC data | Commercial data |
|------|:---:|:---:|:---:|:---:|
| Technical architecture | 30% | Architecture doc review | Actual deployment / perf measured | — |
| Functional fit | 25% | Feature checklist | Actual function verified | — |
| Implementation & O&M | 15% | Methodology / SLA commitment | Deployment UX / doc quality | Service quote |
| Commercial terms | 20% | Preliminary quote | — | TCO / payment / warranty / IP |
| Vendor strength | 10% | Company profile / financials / callbacks | Team professionalism / responsiveness | Financial health |

**Score consolidation:**

| Vendor | Arch (30%) | Func (25%) | Impl (15%) | Comm (20%) | Strength (10%) | **Total** |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| A | /10 | /10 | /10 | /10 | /10 | **/10** |
| B | /10 | /10 | /10 | /10 | /10 | **/10** |
| C | /10 | /10 | /10 | /10 | /10 | **/10** |

---

### Step 8: Recommendation & Decision (Weeks 11–12)

**Objective**: Produce the recommendation report; submit to decision-makers for approval.

**Recommendation report structure:**
1. Executive summary (1 page, decision-maker view)
2. Evaluation process recap (methodology / process / timeline)
3. Vendor comparison analysis (radar chart + key differentiators)
4. Recommendation (primary + backup + rationale)
5. Commercial-negotiation advice (key points / bottom-line clauses / concessions)
6. Implementation advice (phased plan / transition approach)
7. Risk assessment & mitigation

**Decision-meeting prep:**
- Prepare likely decision-maker questions and answers
- Special analysis of major deviations (a vendor significantly above/below average on a dimension)
- One-line summary of the recommendation rationale

---

## 5. Key Considerations

### 5.1 Fairness Principles
- All vendors receive identical information and the same response window
- RFI/RFP Q&A published uniformly
- PoC environment / data / scenarios / success criteria fully unified
- Evaluation criteria fixed before RFI/RFP issuance; not changed mid-process

### 5.2 Common Pitfalls

| Pitfall | Symptom | Prevention |
|------|------|------|
| **Over-focus on price** | Pick unfit vendor for low price | Weight structure tech 70% + commercial 30% |
| **PoC showrooming** | Vendor optimizes only for PoC scenarios | Randomly test undisclosed scenarios |
| **Ignore long-term TCO** | Look only at first-term license fee | Mandatory 5-year TCO comparison |
| **Reference-client bias** | Vendor shows only successes | Independently callback clients; ask about problems |
| **Shallow architecture review** | Read diagrams but not interfaces | Require vendors to open API docs & test env |

### 5.3 Vendor Relationship Management
- The PoC is also relationship-building
- Give respectful feedback to non-selected vendors (help them understand the gap)
- Maintain good ties with non-selected vendors (backup / future collaboration)

---

## 6. Deliverables Catalog

| Deliverable | Owner | Completion | Recipient |
|------|------|:---:|------|
| RFI/RFP document | Solution architect + procurement | Week 2 | Vendors |
| Vendor longlist | Market analyst | Week 2 | Evaluation team |
| Vendor shortlist (3–5) | Evaluation team | Week 4 | Decision-makers |
| PoC plan design | Solution architect | Week 6 | Vendors + evaluation team |
| PoC evaluation report | Solution architect | Week 10 | Evaluation team |
| Vendor comprehensive evaluation report | Evaluation team | Week 11 | Decision-makers |
| Recommendation & commercial-negotiation strategy | Evaluation team + procurement | Week 12 | Decision-makers |

---

> **Version**: V1.0 | **Date**: 2026-07 | **Applies to**: Transportation solution vendor selection
