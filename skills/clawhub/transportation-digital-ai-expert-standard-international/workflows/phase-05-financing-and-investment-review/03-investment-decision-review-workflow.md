# 03 — Investment Decision Review & Governance Workflow

## I. Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│          Investment Decision Review & Governance Workflow Map          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │1. Decision │──>│2. Technical│──>│3. Investment│──>│4. Risk Review│ │
│  │  Materials │   │  Due Dil. │   │  Committee │   │  & Legal     │ │
│  │  Prep      │   │  & Peer   │   │  Presentation│ │  Compliance  │ │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│       │              │              │              │                │
│       v              v              v              v                │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │5. Commercial│>│6. Final    │──>│7. Condition │──>│8. Investment│ │
│  │  Terms     │  │  Decision  │   │  Satisfaction│  │  Kickoff &  │ │
│  │  Negotiate │  │  & Authorize│ │  & Close    │  │  Fund Disburse│ │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│                                                                     │
│  Decision Bodies: Tech Review Board → Investment Committee → Board  │
└─────────────────────────────────────────────────────────────────────┘
```

## II. Applicable Scenarios

This workflow is written from the **technology-investment decision** perspective and guides how to organize the investment-decision review and governance process. It applies to:
- Investment-committee decisions for large transport-digitalization projects (> $0.7M investment)
- Final investment decision after multi-option comparison
- Build-vs-Buy-vs-Outsource investment-route decisions
- Gated review of phased investment (Go/No-Go decision points)

## III. Prerequisites & Inputs

| Input | Source |
|-------|------|
| Technical solution (incl. architecture design) | [Phase 06 Step 1 — Tech Solution Design](../phase-06-tech-solution-design-and-selection/01-tech-solution-design-workflow.md) |
| TCO model & ROI analysis | [Phase 05 Step 1 — TBL ROI Modeling](../phase-05-financing-and-investment-review/01-triple-bottom-line-roi-workflow.md) |
| Phased investment strategy | [Phase 05 Step 2 — Investment Strategy & Phased Budget](../phase-05-financing-and-investment-review/02-financing-scheme-design-workflow.md) |
| Vendor evaluation report (if procurement involved) | [Phase 06 Step 3 — Vendor Selection & PoC](../phase-06-tech-solution-design-and-selection/03-vendor-selection-and-poc-workflow.md) |
| Technical-risk assessment | [Phase 01 Step 2 — Tech Scouting & Feasibility](../phase-01-needs-identification-and-tech-scouting/02-tech-scouting-and-feasibility-workflow.md) |

---

## IV. Detailed Steps

---

### Step 1: Decision-Material Preparation

**Objective**: Prepare a comprehensive, professional investment-decision material package.

**Decision-Material Package Checklist:**

```
□ Investment-decision summary (Executive Summary, 1–2 pp.)
□ Technical-solution summary (non-technical readable version)
□ TCO model (5-year, incl. sensitivity analysis)
□ Multi-dimensional ROI (economic + social + safety benefit)
□ Phased investment plan & milestones
□ Technical-risk register & mitigation strategy
□ Vendor comparison (if multi-vendor selection)
□ Peer benchmark: peer organizations' / projects' investment level & effect
□ Implementation roadmap (key dependencies & assumptions)
□ Exit strategy & stop-loss conditions
```

**Decision-Summary Design Principles:**

| Principle | Description |
|-----------|-------------|
| Conclusion on page one | Page one states: invest or not / how much / expected return / key risks |
| One view per page | Avoid information overload |
| Visualization first | TCO waterfall, ROI sensitivity spider chart, risk heatmap |
| Contrast emphasis | Invest-vs-not, Option A vs B vs C |
| Clear path | Phased investment, milestones, Go/No-Go criteria |
| Honest risk | Show risks but emphasize controllability |

---

### Step 2: Technical Due Diligence & Peer Review

**Objective**: Before the investment decision, independently review the technical solution.

**Technical Due-Diligence Dimensions:**

| Domain | Review Focus | Method |
|--------|--------------|--------|
| Architecture soundness | Pattern choice / scalability / evolvability | Architecture review session |
| Technical feasibility | Maturity / key-tech risk | Expert review |
| Integration feasibility | Integration with existing systems | Interface review + integration test |
| Performance attainability | Attainability of performance metrics | Performance-model review |
| Security & compliance | Security architecture / data protection / compliance | Security audit |
| O&M supportability | O&M plan / SLA / monitoring | O&M-team review |

**Peer-Review Process:**
1. Form independent review group (internal experts + external advisors, 3–5 people)
2. Technical team submits review materials
3. Hold technical review session (2–3 hours)
4. Issue review opinion (Pass / Pass-with-conditions / Fail)

---

### Step 3: Investment-Committee Presentation & Defense

**Objective**: Deliver a professional presentation and defend the case at the formal decision meeting.

**Audience & Focus:**

| Decision-Maker Role | Core Concern | Presentation Emphasis |
|---------------------|--------------|-----------------------|
| CEO / GM | Strategic value / competitive edge / risk exposure | Strategic alignment + competitive impact + payback |
| CFO / Finance Lead | TCO / ROI / cash-flow / tax impact | Financial model + sensitivity + funding plan |
| CTO / Technical Lead | Tech route / architecture / tech debt / talent | Technical approach + evolution path + team capability |
| COO / Operations Lead | O&M SLA / org impact / service continuity | Operating model + transition plan + training |
| Security / Compliance Lead | Data protection / compliance / audit | Security architecture + compliance checklist |

**Presentation Structure (20-min standard):**

```
0–2 min    Investment recommendation summary (one-line conclusion + key numbers)
2–5 min    Why invest now? (market / tech window + risk of not investing)
5–10 min   What to invest in? (technical solution + implementation roadmap)
10–15 min  Return & risk (TCO + ROI + risk–mitigation matrix)
15–18 min  Next steps (resource needs + timeline + decision request)
18–20 min  Q&A
```

**Q&A Preparation (high-frequency questions):**

| High-Frequency Question | Prepared Answer |
|-------------------------|----------------|
| "ROI period too long, can it be shortened?" | Show phased return + quick-win scenarios + sensitivity |
| "Will we get locked in technically?" | Show open architecture + open-source alternative + switch-cost analysis |
| "Can the team handle it?" | Show team-capability matrix + external advisors + training plan |
| "What do competitors do?" | Show sector benchmark + differentiation strategy |
| "What's the worst case?" | Show pessimistic scenario + stop-loss + exit path |
| "Can we pilot small first?" | Show MVP plan + pilot cost + evaluation criteria |

---

### Step 4: Risk Review & Legal Compliance

**Objective**: Independently assess investment risk and conduct legal/compliance review.

**Risk-Review Framework:**

| Risk Domain | Review Content | Owner |
|-------------|---------------|-------|
| Technology risk | Feasibility / obsolescence / vendor risk | CTO / Architecture Review |
| Market risk | Demand change / competition / tech substitution | Business Lead |
| Execution risk | Team capability / vendor delivery / integration complexity | PMO |
| Financial risk | Cost over-run / return shortfall / FX risk | Finance |
| Compliance risk | Software license / IP / data compliance / security compliance | Legal / Security |
| Operational risk | System stability / O&M capability / SLA breach | O&M Lead |

**Compliance Review Checklist:**
- [ ] Software-license compliance (open-source license compatibility / commercial license scope)
- [ ] Intellectual property (own IP / third-party IP / patent risk)
- [ ] Data-protection compliance (personal-info protection / cross-border data / sector data-management requirements)
- [ ] Security compliance (security classification / critical-infrastructure protection / ISO/SAE 21434 / cybersecurity regulation, e.g., NIS2 and regional equivalents)
- [ ] Vendor-contract compliance (SLA / liability / IP ownership / dispute resolution)
- [ ] Export-control compliance (if cross-border tech / equipment involved)

---

### Step 5: Commercial-Terms Negotiation & Lock

**Objective**: Before the investment decision, complete negotiation and lock of key commercial terms.

**Key Commercial-Terms Negotiation Checklist:**

| Term | Negotiation Focus | Floor |
|------|-------------------|-------|
| Price & payment | Lump-sum / installment / milestone / price protection | Within budget ±15% |
| Delivery scope | Feature list / customization scope / data migration | Core features must be covered |
| Implementation period | Total duration / milestones / delay penalty | Not exceed committed +20% |
| SLA & O&M | Availability / response time / recovery / penalty | No lower than sector benchmark |
| IP | Source-code ownership / custom-portion IP / usage scope | Custom IP to client |
| Warranty & maintenance | Warranty period / renewal price / renewal cap | Renewal increase ≤ CPI + 3% |
| Exit clause | Early-termination condition / data export / transition service | Data complete & portable |

**Negotiation Strategy Suggestions:**
- Keep at least 2 comparable vendor options (avoid single-source negotiation)
- Negotiate scope and service first, then price
- TCO over upfront price: compare using 5-year TCO model, not initial quote

---

### Step 6: Final Decision & Authorization

**Objective**: Complete the final investment decision and obtain formal authorization.

**Decision-Authorization Matrix:**

| Investment Amount | Decision Level | Approval Flow |
|:---:|----------------|---------------|
| < $0.15M | Department Head | Tech review → department approval |
| $0.15M–$0.7M | Tech VP / CTO + CFO | Tech review → Investment Committee → joint approval |
| $0.7M–$2.8M | CEO / GM | Tech due diligence → Investment Committee → CEO approval → Board file |
| > $2.8M | Board of Directors | Tech due diligence → Investment Committee → Board approval |

**Decision-Document Sign-off Checklist:**
- [ ] Investment-decision memo (records decision process & basis)
- [ ] Board resolution / CEO approval (per authority)
- [ ] Fund-disbursement approval
- [ ] Vendor contract (if external procurement)
- [ ] Project charter update (if material change)

**Decision Options:**
- ✅ **Approved**: fully approved, initiate implementation
- 🟡 **Approved with conditions**: conditional (e.g., complete PoC first / sign phase-1 contract first / supply missing materials)
- 🔄 **Deferred**: defer to next review cycle (need more info or conditions mature)
- ❌ **Rejected**: not approved (state reasons and follow-up suggestions)

---

### Step 7: Condition Satisfaction & Close-Out

**Objective**: For conditionally-approved decisions, satisfy each condition and formally close the decision loop.

**Condition-Tracking Table:**

| Condition ID | Description | Owner | Due Date | Status | Close Evidence |
|:---:|-------------|--------|:---:|:---:|-------------|
| C-01 | [Complete PoC validation] | [Technical Lead] | [date] | ✅ | PoC report |
| C-02 | [Obtain security-compliance confirmation] | [Security Lead] | [date] | 🔄 | Compliance confirmation letter |
| C-03 | [Vendor contract signed] | [Procurement Lead] | [date] | ⬜ | Signed contract |

---

### Step 8: Investment Kickoff & Fund Disbursement

**Objective**: After all decision pre-conditions are met, formally launch execution and first-tranche disbursement.

**Investment-Kickoff Checklist:**
- [ ] All decision conditions satisfied
- [ ] Contract signed (if external procurement)
- [ ] Project charter updated and signed
- [ ] First-tranche funds disbursed
- [ ] Project manager and technical lead appointed
- [ ] Financial coding / cost center established
- [ ] Vendor received kickoff notice

**Fund-Disbursement Cadence:**

| Milestone | Disbursement Ratio | Trigger |
|-----------|:---:|---------|
| Project kickoff | 20% | Contract signed + charter signed |
| Design complete | 25% | Detailed-design review passed |
| Half-developed | 20% | Mid-term review passed |
| UAT passed | 20% | User acceptance test passed |
| Production go-live | 12.5% | Go-live + stable 30 days |
| Warranty expiry | 2.5% | Warranty ended + no open issues |

---

## V. Key Notes

### 5.1 Common Investment-Decision Pitfalls

| Pitfall | Manifestation | Prevention |
|---------|---------------|-----------|
| **Optimism bias** | Underestimate cost, overestimate benefit, ignore risk | Mandatory three-scenario analysis + independent review |
| **Sunk-cost fallacy** | "Already invested so much, can't stop" | Judge each decision gate independently, ignore history |
| **Anchoring** | Anchored to first quote / proposal | Always compare ≥ 3 independent options / quotes |
| **Groupthink** | Review group too unanimous | Introduce external independent review + "devil's advocate" role |
| **Confirmation bias** | Only collect evidence supporting conclusion | Require a "reasons not to invest" list |
| **Tech dazzle** | Swayed by vendor demo | Distinguish PoC environment from production; require real-client references |

### 5.2 Exit-Strategy Design

Every investment plan must preset exit conditions and stop-loss lines:

| Exit Trigger | Exit Action |
|--------------|-------------|
| Actual cost over budget > 30% with no remedy | Pause project, re-assess |
| PoC / Pilot key metrics not met | Do not enter next investment phase |
| Core tech / vendor major change | Re-select technology |
| Business need fundamentally changed | Terminate project, liquidate assets |
| Construction period exceeds plan > 50% | Trigger independent audit & decision review |

---

## VI. Deliverables List

| Deliverable | Owner | Submission | Recipient |
|-------------|-------|:---:|-----------|
| Investment-decision material package | PM + Technical Lead | 1 week before meeting | Investment Committee |
| Technical due-diligence report | Independent review group | 1 week before meeting | Investment Committee |
| Investment-committee minutes + resolution | Committee secretary | 3 days after meeting | Stakeholders + archive |
| Risk-review report | Risk / Legal / Security Lead | 3 days before meeting | Investment Committee |
| Commercial-terms negotiation memo | Procurement Lead | Before meeting | Investment Committee |
| Final decision document | CEO / Board | 1 week after meeting | Project team + Finance |
| Condition-satisfaction confirmation | Project Manager | Condition due date | Investment Committee |
| Fund-disbursement notice | Finance Lead | Within 1 week of kickoff | Project team + Vendor |

---

> **Version**: V1.0 | **Date**: 2026-07 | **Applicable to**: Transport digitalization technology-investment decision review & governance
