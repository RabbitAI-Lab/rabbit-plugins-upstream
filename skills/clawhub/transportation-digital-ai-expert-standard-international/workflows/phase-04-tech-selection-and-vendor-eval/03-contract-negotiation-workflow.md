# 03 — Contract Negotiation & Execution Workflow

## I. Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│               Contract Negotiation & Execution Workflow Map            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │1. Negotiation│>│2. Key Terms│──>│3. Contract  │──>│4. Formal    │ │
│  │  Strategy   │  │  Analysis  │   │  Draft      │   │  Negotiation │ │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│       │              │              │              │                │
│       v              v              v              v                │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │5. Legal Review│>│6. Contract │──>│7. Signing   │──>│8. Contract   │ │
│  │  & Compliance │  │  Finalization│  │  & Archiving│  │  Handover   │ │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│                                                                     │
│  Covered terms: Scope | Price | Delivery | Acceptance | Payment |   │
│  IP | Warranty | Liability | Dispute                                    │
└─────────────────────────────────────────────────────────────────────┘
```

## II. Applicable Scenarios

This workflow applies to the contract-negotiation and signing stage of a smart-mobility project after the vendor is selected, covering the full process from strategy formulation to contract archiving.

## III. Prerequisites & Inputs

| Input | Source |
|-------|------|
| Vendor evaluation recommendation report | [Phase 04 Step 2 — Vendor Evaluation & PoC](../phase-04-tech-selection-and-vendor-eval/02-vendor-evaluation-and-poc-workflow.md) |
| SOW and technical specifications | [Phase 04 Step 1 — Tech Requirements & RFI/RFP](../phase-04-tech-selection-and-vendor-eval/01-tech-requirements-rfi-rfp-workflow.md) |
| RFP commercial terms and quotes | [Phase 04 Step 1 — Tech Requirements & RFI/RFP](../phase-04-tech-selection-and-vendor-eval/01-tech-requirements-rfi-rfp-workflow.md) |
| Company contract template and sector norms | Legal / Finance |
| Applicable laws & regulations | Contract law / public-procurement regulations (e.g., UNCITRAL Model Law on Procurement, FIDIC, EU / North-American procurement directives) |

---

## IV. Detailed Steps

---

### Step 1: Negotiation Strategy Formulation

**Objective**: Based on project characteristics and vendor situation, formulate a systematic negotiation strategy.

**Inputs**: Recommendation report, SOW, RFP response
**Outputs**: Negotiation strategy document, negotiation-points checklist

**Guidance**:

**1.1 Pre-Negotiation Environment Analysis**

```
Five-Forces Analysis Before Negotiation:

  Vendor bargaining power      Vendor negotiation motivation
 ┌──────────────────┐    ┌──────────────────┐
 │· Sole-source?    │    │· Strategic value  │
 │· Difficulty of   │    │· Current backlog  │
 │  alternative     │    │· Competition level│
 │· Vendor urgency  │    │                  │
 └──────┬───────────┘    └──────┬───────────┘
        │                       │
        └─────────┬─────────────┘
                  │
         ┌────────┴────────┐
         │ Negotiation Strategy │
         └────────┬────────┘
                  │
  ┌───────────────┼───────────────┐
  │               │               │
  v               v               v
Our leverage     Target tiers    Exit strategy
 ·Project appeal  ·Floor / Target / ·Alternative vendor
 ·Budget flexibility Ideal        ·In-house build option
 ·Time pressure   ·Technical /    ·Phased cooperation
                  Commercial / Legal
                  ·Short / Long term
```

**1.2 Negotiation Target Setting (Three-Line Model)**

| Clause Category | Floor (Must-Have) | Target (Want) | Ideal (Nice-to-Have) |
|-----------------|-------------------|---------------|----------------------|
| Price | Within budget ceiling | 8–10% discount | 15%+ discount |
| Payment | Milestone-linked, ≥10% retained after acceptance | 15–20% retained after acceptance | 30% retained after acceptance |
| IP | Client owns custom-developed portions | Client owns all development output | Full source-code delivery |
| Schedule | ≤ 3 months buffer | 1 month earlier | 2 months earlier |
| Warranty | ≥ 1 year free O&M | 2 years free | 3 years free |

**1.3 Negotiation Team Configuration**

```
Negotiation Team Roles:

┌─────────────────────────────────────────────────┐
│ Chief Negotiator (Sales VP / Program Director)   │
│ - Controls pace, makes strategic concessions      │
├─────────────────────────────────────────────────┤
│ Technical Negotiator (Technical Lead)             │
│ - "Interpretation rights" on tech, holds tech boundaries │
├─────────────────────────────────────────────────┤
│ Commercial Negotiator (Procurement / Commercial Mgr) │
│ - Price, payment terms, service terms            │
├─────────────────────────────────────────────────┤
│ Legal Support (Legal / Outside Counsel)          │
│ - Legal clause review, compliance risk control   │
├─────────────────────────────────────────────────┤
│ Recorder (Project Manager)                       │
│ - Full record, meeting minutes, clause tracking  │
└─────────────────────────────────────────────────┘
```

---

### Step 2: Key-Terms Analysis

**Objective**: Comprehensively identify and analyze key contractual terms and potential risk points.

**Inputs**: RFP commercial terms, vendor preliminary response
**Outputs**: Key-terms analysis report, risk-clause list

**Guidance**:

**2.1 Transport-Sector Key Contract-Clause Checklist**

| Clause Type | Key Clause | Focus |
|-------------|-----------|-------|
| Scope | Statement of Work (SOW) | Clear boundaries, avoid ambiguity |
| Delivery | Deliverables list + acceptance criteria | Each deliverable quantifiable, testable |
| Schedule | Milestone plan + delay penalty | Clear milestones, strong penalties |
| Price | Lump-sum / unit price, tax-inclusive / exclusive | Price lock, change-pricing framework |
| Payment | Payment milestones, ratio, conditions | Strictly tied to milestones |
| IP | Source-code / docs / data ownership | Custom-developed IP belongs to client |
| Confidentiality | Scope, term, breach liability | Covers both parties' data and trade secrets |
| Warranty | Warranty period, response SLA, fix SLA | Specific metrics, not principle-only |
| Liability | Breach events, liability cap, termination | Mutual but protective |
| Dispute resolution | Governing law, jurisdiction, arbitration | Local jurisdiction |
| Change | Change process, pricing, approval | Fair and transparent |

**2.2 Technical & Delivery Clause Deep Analysis**

```
Technical / Delivery Clause Analysis Points:

[Deliverable Definition]
□ Does each deliverable have clear format, content, quality standard?
□ Is source-code delivery scope clear (all / partial / compiled product)?
□ Is the document list complete (design / O&M / user / interface / deployment)?

[Acceptance Criteria]
□ Are acceptance conditions objectively testable?
□ Who prepares the acceptance test environment and data?
□ What is the remedy framework if acceptance fails?
□ Acceptance sign-off procedure and timing?

[Performance Metrics]
□ Are response time, throughput, concurrency quantified?
□ Are performance-test method and tool clear?
□ What are the consequences of failing performance?

[Integration Responsibility]
□ Is integration responsibility with existing systems clear?
□ Responsibility for third-party system interfaces?
□ Timing and parties for joint testing?
```

---

### Step 3: Contract Draft Authoring

**Objective**: Based on preliminary mutual understanding, author the contract draft.

**Inputs**: SOW, commercial terms, negotiation strategy
**Outputs**: Contract draft V1.0

**Guidance**:

**3.1 Smart-Mobility Project Contract Structure**

```
Smart-Mobility Project Contract Structure:

Part 1: Contract Body
  1. Definitions & Interpretation
  2. Subject Matter & Scope (references SOW appendix)
  3. Price & Payment
  4. Delivery & Acceptance
  5. Project Organization & Management
  6. Intellectual Property
  7. Confidentiality Obligations
  8. Quality Assurance & After-Sales Service
  9. Liability for Breach
  10. Force Majeure
  11. Contract Change & Termination
  12. Dispute Resolution
  13. Notice & Service
  14. Effectiveness & Term

Part 2: Appendices
  Appendix 1: Statement of Work (SOW)
  Appendix 2: Technical Requirements Specification
  Appendix 3: Deliverables List
  Appendix 4: Project Plan & Milestones
  Appendix 5: Acceptance Criteria & Test Plan
  Appendix 6: Pricing Detail Schedule
  Appendix 7: Project Team Roster
  Appendix 8: O&M Service SLA
  Appendix 9: Non-Disclosure Agreement (NDA)
  Appendix 10: Information-Security Commitment Letter
```

**3.2 Smart Contract Clauses**

For smart-mobility projects, recommend adding these sector-specific clauses:
- **AI Model Performance Guarantee**: guarantees and long-term maintenance of AI model accuracy / recall metrics
- **Data-Security Special Clause**: data-processing obligations per data-security and personal-information-protection regulations
- **Sovereign-Tech Compliance Clause**: compatibility commitment in sovereign-tech / local-content environments
- **Security-Classification Compliance Clause**: obligation to cooperate with security-classification assessment and remediation
- **Transport-Sector Special Clause**: special assurance commitment during major-event / peak periods (holidays, major events)

---

### Step 4: Formal Negotiation & Bargaining

**Objective**: Conduct formal contract negotiation with the vendor to reach optimal terms.

**Inputs**: Contract draft, negotiation strategy
**Outputs**: Negotiation minutes, clause-revision log

**Guidance**:

**4.1 Negotiation Agenda Design**

```
Suggested Negotiation Meeting Plan:

Round 1: Commercial (half day)
  - Price and payment terms
  - Delivery schedule and milestones
  - Warranty and SLA
  - Goal: lock core commercial terms

Round 2: Technical (half day)
  - SOW boundary confirmation
  - Final technical-solution confirmation
  - Deliverables and acceptance criteria
  - Goal: lock technical solution and scope

Round 3: Legal (half day)
  - Intellectual property
  - Liability for breach
  - Confidentiality and compliance
  - Goal: lock legal terms

Round 4: Final (half day)
  - Resolve remaining disagreements
  - Full confirmation
  - Goal: reach agreement on all terms
```

**4.2 Negotiation Technique Toolkit**

| Technique | Scenario | Example Script |
|-----------|----------|----------------|
| Anchoring | Opening quote | "Based on our market research, comparable projects fall in the range of…" |
| Concession exchange | Request price cut | "If you cut 10%, we can move the payment milestone earlier" |
| Silent pressure | Opponent quotes too high | (Stay silent, let opponent explain or adjust) |
| High-point concession | Break deadlock | "If you accept this clause, we can concede on X" |
| Small-point collection | Closing stage | "The big picture is set; you won't object to these minor tweaks?" |
| Time pressure | Stalling tactic | "We need to report the final result to decision-makers by Monday" |

**4.3 Transport-Sector Special Negotiation Points**

| Issue | Our Position | Common Disagreement | Negotiation Strategy |
|-------|--------------|---------------------|----------------------|
| AI model ownership | Models trained on client data belong to client | Vendor wants to retain model | Distinguish base model (vendor) vs. custom model (client) |
| Data ownership | All data generated during delivery belongs to client | Vendor wants reuse | Contractually prohibit secondary data use |
| Sovereign-tech guarantee | Commitment to run in sovereign-tech environment | Vendor deflects as out-of-scope | Define compatibility test scope and standard |
| O&M SLA | 15-min response / 2-hour on-site | Vendor commits 2-hour response | Cite sector benchmarks, tiered SLA |
| Source-code escrow | Third-party source-code escrow | Vendor reluctant to release source | Agree release on specific events (bankruptcy / cessation) |

---

### Step 5: Legal Review & Compliance

**Objective**: Ensure legal compliance of contract terms and prevent legal risk.

**Inputs**: Post-negotiation revised contract draft
**Outputs**: Legal review opinion, revised contract

**Guidance**:

**5.1 Legal Review Checklist**

| Dimension | Check Point | Reviewer |
|-----------|-------------|:---:|
| Subject qualification | Is signing entity valid and licensed? | Legal |
| Contract validity | Any void / voidable circumstances? | Legal |
| Rights & obligations | Mutually balanced (not over-biased)? | Legal |
| IP | IP ownership and license clear? | Legal + Tech |
| Liability | Breach clauses clear, not excessive/light? | Legal |
| Dispute resolution | Jurisdiction / arbitration favorable? | Legal |
| Compliance review | Conforms to procurement law? | Legal |
| Data compliance | Conforms to data-security & personal-info law? | Legal + Security |
| Sovereign-tech compliance | Meets sovereign-tech substitution requirements? | Tech |

**5.2 Common Legal Red Flags**

- Contract amount exceeds vendor's registered capital by a large multiple (doubtful delivery capacity)
- Liability cap set too high or too low (>30% or <5% of contract value)
- Unlimited-liability clauses (software industry typically caps liability at contract value)
- Over-restrictive unilateral termination rights
- "Creative Commons"-style loose IP license (client output leaks away)
- Dispute jurisdiction in vendor's home location

---

### Step 6: Contract Finalization & Internal Approval

**Objective**: Complete the final contract version and pass internal approval.

**Inputs**: Legally reviewed contract
**Outputs**: Final contract, internal approval form

**Guidance**:

**6.1 Internal Approval Flow**

```
Typical Contract Approval Flow:

Project Manager initiates → Technical Lead approves → Commercial Lead approves →
Legal approves → Finance approves → VP / GM approves

Each approver focuses on:
  Technical Lead: SOW scope, technical solution, acceptance criteria
  Commercial Lead: price, payment, commercial-term reasonableness
  Legal: legal risk, compliance
  Finance: budget fit, payment cadence, invoicing requirements
  VP / GM: strategic fit, overall risk judgment
```

**6.2 Contract Version Management**

- Version-tag each revision (V1.0 → V1.1 → V2.0 (signed version))
- Retain all historical versions and revision comments
- Final version uses a "clean copy" (no comment marks) for signing

---

### Step 7: Signing Execution & Archiving

**Objective**: Complete formal contract signing and archiving.

**Inputs**: Final contract
**Outputs**: Signed contract, contract-archiving record

**Guidance**:

**7.1 Signing Execution Checklist**

- [ ] Verify signatory authorization (legal authority to sign)
- [ ] Text-consistency check (both parties' copies identical)
- [ ] Apply company seal / contract seal
- [ ] Apply cross-page seal (multi-page contracts)
- [ ] Fill in signing date
- [ ] Allocate original / copy (typically 2 originals, one per party; copies as needed)
- [ ] Scan electronic copy for archiving
- [ ] Archive original (Finance + records room)

**7.2 Transport-Sector Special Signing Notes**

- Whether payment terms require filing with the funding-authority department
- Whether over-budget projects completed budget-supplement approval
- Contract-information publication requirement (procurement projects announced on official public-procurement portal)
- Consistency check between award notification letter and contract

---

### Step 8: Contract Handover

**Objective**: Hand over signed contract information to the project-management team so execution has a basis.

**Inputs**: Signed contract, related appendices
**Outputs**: Contract summary, contract-kickoff meeting minutes

**Guidance**:

**8.1 Contract Information Summary (for Project Manager)**

```
Contract Information Summary (one-pager):

Project Name: _________
Contract No.: _________
Total Contract Value: _________ $M
Contract Effective Date: _________
Contract Expiry Date: _________

Key Milestones & Payments:
  M1: _________  Payment: _____$M (___%)
  M2: _________  Payment: _____$M (___%)
  M3: _________  Payment: _____$M (___%)
  ...

Key Constraints:
  ·Schedule: total ___ days, key milestones no delay beyond ___ days
  ·Quality: acceptance criteria per Appendix 5
  ·Personnel: key personnel not replaceable, per Appendix 7
  ·SLA: per Appendix 8

Key Risk Clauses:
  ·Liquidated damages: ___%/day delay, cap ___%
  ·Termination conditions: _________
  ·Dispute resolution: _________

Counterpart Key Contacts:
  Project Manager: ___  Tel: ___  Email: ___
  Technical Lead: ___  Tel: ___  Email: ___
```

**8.2 Contract Kickoff Meeting**

- Signing team briefs the delivery team on the contract
- Explains business meaning of each key clause point-by-point
- Emphasizes "minefields" during execution (easy-to-breach clauses)
- Clarifies contract-change process and authority

---

## V. Roles & Responsibilities (RACI Matrix)

| Activity | Project Manager | Commercial Mgr | Technical Lead | Legal | Finance | VP |
|----------|:---:|:---:|:---:|:---:|:---:|:---:|
| Negotiation strategy | C | **R/A** | C | I | I | C |
| Term analysis | C | **R** | C | **R** | I | I |
| Contract draft | C | **R** | C | C | I | I |
| Formal negotiation | C | **R/A** | C | C | I | I |
| Legal review | I | I | I | **R/A** | I | I |
| Contract finalization | **R** | C | C | C | C | **A** |
| Signing execution | **R/A** | C | I | I | I | I |
| Contract handover | **R/A** | C | C | I | I | I |

---

## VI. Key Checkpoints

| # | Checkpoint | Pass Criteria |
|---|------------|---------------|
| CP1 | Negotiation strategy review | Three-line targets reasonable, clear exit conditions |
| CP2 | Term risk analysis | All key terms analyzed with response plan |
| CP3 | Legal review | Legal signs "no material legal risk" opinion |
| CP4 | Internal approval | All approval nodes passed |
| CP5 | Signing compliance | Authorization, seals, text all correct |
| CP6 | Contract kickoff | PM team confirms understanding of all key terms |

---

## VII. Estimated Duration

| Phase | Standard | Urgent |
|------|:---:|:---:|
| Negotiation strategy prep | 1–2 days | 0.5 day |
| Contract negotiation | 1–2 weeks | 1 week |
| Legal review | 2–3 days | 1 day |
| Internal approval | 3–5 days | 2 days |
| Signing execution | 1–2 days | 0.5 day |
| **Total** | **2–4 weeks** | **1–2 weeks** |

---

## VIII. Common Pitfalls & Countermeasures

| # | Pitfall | Countermeasure |
|---|---------|----------------|
| 1 | Appendix content inconsistent with body | Verify word-by-word, especially SOW and tech specs |
| 2 | Rush to sign, ignore risk clauses | Insist on legal review; don't rush the signing moment |
| 3 | Vague IP clauses cause later disputes | Clearly distinguish "background IP" vs. "foreground IP" ownership |
| 4 | Payment nodes not tied to real delivery | Payment nodes must be objectively verifiable delivery milestones |
| 5 | Signed contract shelved | Must do contract kickoff so execution team knows the terms |
| 6 | Verbal promises not written in | All negotiation promises must be documented |

---

## IX. Deliverables List

1. **Negotiation Strategy Document** (.docx)
2. **Key-Terms Analysis Report** (.docx)
3. **Contract Draft** (.docx)
4. **Negotiation Minutes (per round)** (.docx)
5. **Legal Review Opinion** (.docx)
6. **Final Contract** (.docx)
7. **Internal Approval Form** (.docx)
8. **Signed Contract** (.pdf)
9. **Contract Information Summary** (.docx)
10. **Contract Kickoff Meeting Minutes** (.docx)

---

> **Version**: V1.0 | **Date**: 2025-07 | **Legal Basis**: Contract Law / Public-Procurement Regulations
