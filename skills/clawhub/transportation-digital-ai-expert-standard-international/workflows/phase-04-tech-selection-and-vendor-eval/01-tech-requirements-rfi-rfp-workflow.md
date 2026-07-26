# 01 — Technology Requirements Definition & RFI/RFP Workflow

## I. Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│              Technology Requirements & RFI/RFP Workflow Map           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │1. Requirements│──>│2. Tech Spec│──>│3. RFI Design│──>│4. RFI Issue │  │
│  │  Review & Confirm│  │  & SOW     │   │  & Questionnaire││ & Vendor Invite│ │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│       │              │              │              │                │
│       v              v              v              v                │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │5. RFI Response│──>│6. RFP Draft│──>│7. Proposal   │──>│8. RFP Issue  │ │
│  │  Analysis &  │   │  & Finalize │  │  Evaluation   │   │ & Response   │ │
│  │  Shortlist   │   │            │  │  Criteria     │   │ Management   │ │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│                                                                     │
│  Core Deliverables: SOW | RFI | RFP | Proposal Evaluation Criteria | │
│  Contract Technical Annex                                                  │
└─────────────────────────────────────────────────────────────────────┘
```

## II. Applicable Scenarios

This workflow applies after a smart-mobility / intelligent transportation program has fixed its technical direction, and uses a structured RFI (Request for Information) and RFP (Request for Proposal) process to select the most suitable vendor or technical solution. It is written from the **client / buyer perspective** and guides how to design and manage the RFI/RFP process.

## III. Prerequisites & Inputs

| Input | Source | Notes |
|-------|------|------|
| Business Requirements Document (BRD) | [Phase 02 Step 2 — Deep Business Research](../phase-02-current-state-diagnosis-and-maturity/02-deep-business-research-workflow.md) | Complete business requirements |
| Technology Architecture Design | [Phase 03 Step 3 — Data & Tech Architecture](../phase-03-strategy-and-top-level-design/03-data-and-tech-architecture-workflow.md) | Technology selection & architecture requirements |
| Investment Estimate | [Phase 03 Step 4 — 3-Year Roadmap & Investment Plan](../phase-03-strategy-and-top-level-design/04-three-year-roadmap-and-investment-workflow.md) | Budget envelope |
| Procurement Regulations / Policy | Provided by client | Public-sector / state-owned enterprise procurement rules |

---

## IV. Detailed Steps

---

### Step 1: Requirements Review & Confirmation

**Objective**: Before entering the procurement process, finally confirm that the technical requirements are complete, accurate, and measurable.

**Inputs**: BRD, architecture design, investment budget
**Outputs**: Requirements baseline document, SOW draft

**Guidance**:

**1.1 Requirements Classification Matrix**

Classify requirements using the matrix below to clarify how each class is handled:

| Requirement Type | Handling | Example |
|------------------|----------|---------|
| Mandatory requirement | Non-compliant bid is rejected | Security classification (e.g., classified protection Level 3) compliance |
| Core requirement | Highest-weighted scoring item | AI incident-detection accuracy > 85% |
| Differentiator requirement | Used to separate vendor tiers | Support for additional algorithm scenarios |
| Reference requirement | Not scored but must be addressed | Phase-2 expansion approach |

**1.2 Avoid "Gold-Plating" Requirements**

- Every requirement must answer: *Why do we need this? Which business scenario requires it?*
- Drop features that "sound impressive but have no real use."
- Distinguish "must-have" from "nice-to-have."

**1.3 SOW (Statement of Work) Draft Structure**

```
Statement of Work (SOW) Draft:

1. Project Background & Objectives
2. Project Scope
3. Technical Solution Requirements
4. Deliverables List
5. Implementation Schedule & Milestones
6. Acceptance Criteria
7. Technology Transfer & Training Requirements
8. Operations & Support Requirements
9. Project Management Requirements
10. Division of Responsibilities
11. Assumptions & Constraints
```

---

### Step 2: Technical Specifications & SOW Authoring

**Objective**: Translate business requirements into precise technical specifications and write the complete SOW.

**Inputs**: Requirements baseline, architecture design
**Outputs**: Technical specification document, complete SOW

**Guidance**:

**2.1 Principles for Writing Technical Specifications**

| Principle | Description |
|-----------|-------------|
| Objective & measurable | Avoid subjective wording such as "user-friendly UI" or "excellent performance" |
| Technology-neutral | Do not name specific products (unless strongly justified) |
| Outcome-oriented | Describe *what it must do*, not *how to implement it* |
| Verifiable | Every spec has a corresponding acceptance test method |
| Industry-standard | Prefer referencing international / sector standards |

**2.2 Sample Transport-Sector Technical Specifications**

```
Sample Technical Specifications:

[Performance]
- Video AI analysis latency: < 2 s from stream ingest to analysis result (per stream)
- API concurrency: > 500 QPS (query-type) / > 100 QPS (transaction-type)
- Map rendering: load road-network data for 1,000+ segments < 3 s
- Data fusion: real-time fusion of 5+ data sources, latency < 5 s
- System availability: core business systems > 99.9% (annual downtime < 8.76 h)

[Functional]
- Ingest and play back ONVIF / RTSP compliant video streams
- Ingest onboard-unit (OBU) data via standard protocols (e.g., NTCIP, ISO 15075)
- AI incident detection covering no fewer than 10 event types (specified list)
- Support OGC / CityGML geospatial data formats

[Security]
- Pass security classification assessment (e.g., classified protection Level 3)
- Support FIPS 140-2/3-approved algorithms (e.g., AES-256, SHA-256, ECDSA)
- Support federated identity (OAuth 2.0 / OIDC)
- Data-in-transit encryption (TLS 1.3), data-at-rest encryption (AES-256)
- Complete audit logging of assessment and review activities

[Scalability]
- Horizontal scale-out to no fewer than 10 nodes
- Data storage scale-out to petabyte level
- Support hybrid X86 and ARM deployment architectures
```

**2.3 SOW Quality Checklist**

- [ ] Scope boundaries clear (what is in and what is out)
- [ ] All deliverables quantified (quantity + quality standard)
- [ ] Milestones clear (time + deliverable + acceptance method)
- [ ] Acceptance criteria measurable
- [ ] Division of responsibilities clear and unambiguous
- [ ] Knowledge-transfer and operations requirements included

---

### Step 3: RFI Design & Questionnaire Authoring

**Objective**: Design the RFI (Request for Information) for market research and initial vendor screening.

**Inputs**: Technical requirements, architecture requirements
**Outputs**: RFI package, RFI questionnaire

**Guidance**:

**3.1 Purpose of the RFI**

RFI vs. RFP:

| | RFI (Request for Information) | RFP (Request for Proposal) |
|---|---|---|
| Purpose | Understand the market, gather information | Obtain formal quotes and proposals |
| Timing | Requirements not yet clear, market needs research | Requirements clear, ready to procure |
| Response | Informational, no formal quote | Formal proposal + quote |
| Obligation | Creates no contract obligation | Creates contract obligation |
| Duration | 2–4 weeks | 4–8 weeks |

**3.2 RFI Questionnaire Structure**

```
RFI Questionnaire Structure:

Part 1: Company Profile
  - Overview (founded, scale, certifications)
  - Core business and major clients
  - Financials for last 3 years (optional)
  - Relevant certifications

Part 2: Technology & Product Capability
  - Product feature introduction (respond point-by-point to requirements)
  - Technology architecture description
  - Compatibility with existing systems
  - Independent IP / proprietary technology
  - R&D investment and technology roadmap

Part 3: Industry Experience
  - Transport-sector project case studies (last 3 years)
  - Experience with projects of similar scale and complexity
  - Client references / contact information

Part 4: Service Capability
  - Project management methodology
  - Implementation team capability
  - Local / in-region service capability
  - Training and knowledge transfer
  - Operations SLA capability

Part 5: Commercial Information (optional)
  - Approximate price range
  - Licensing model
  - Preferred partnership model
```

---

### Step 4: RFI Issuance & Vendor Invitation

**Objective**: Send the RFI to promising vendors and gather market intelligence.

**Inputs**: RFI package, long-list of vendors
**Outputs**: RFI response tracking sheet

**Guidance**:

**4.1 Building the Vendor Long-List**

Vendor sources:
- Vendors met at industry expos / forums
- Industry analyst reports (Gartner / IDC / Forrester, etc.)
- Vendors selected on peer organizations' projects
- Existing partner ecosystem
- Vendors that approached proactively

**4.2 Long-List Inclusion Criteria**

- Has transport-sector relevant case(s) (mandatory)
- Has delivery experience with projects of similar scale
- Financially stable (operating 3+ years)
- No major legal / credit issues

**4.3 RFI Distribution & Management**

| Activity | Timing | Owner |
|----------|:---:|------|
| RFI issued | D-Day | Procurement / project team |
| Vendor Q&A session | D+7 | Project team |
| Q&A minutes issued | D+10 | Project team |
| RFI response deadline | D+21 | Vendor |
| Expected response count | 10–20 vendors | — |

---

### Step 5: RFI Response Analysis & Screening

**Objective**: Based on RFI responses, screen vendors into a shortlist.

**Inputs**: RFI responses, long-list
**Outputs**: RFI analysis report, vendor shortlist

**Guidance**:

**5.1 RFI Response Evaluation Matrix**

| Dimension | Weight | Scoring (1–5) |
|-----------|:---:|------|
| Product-function fit | 30% | Fit to requirements |
| Technology-architecture maturity | 20% | Advanced, open architecture |
| Industry experience | 20% | Number & quality of transport cases |
| Service capability | 15% | Local service, training, operations |
| Company strength | 10% | Scale, certifications, stability |
| Engagement willingness | 5% | Response thoroughness, cooperation |

**5.2 Shortlist Selection Criteria**

- Top 5–7 by composite score
- Ensure coverage of: large systems integrator + domain specialist + innovative technology firm
- Maintain competitiveness (never only one viable option)
- Target: ultimately invite 3–5 vendors into the RFP

---

### Step 6: RFP Drafting & Finalization

**Objective**: Based on RFI market intelligence, author the complete RFP.

**Inputs**: SOW, technical specifications, RFI analysis results
**Outputs**: Full RFP document set

**Guidance**:

**6.1 RFP Document Structure**

```
RFP Document Structure:

Volume 1: Instructions to Proposers
  1. Procurement notice & project overview
  2. Definitions & terminology
  3. Proposer qualification requirements
  4. Proposal cost (borne by proposer)
  5. Site visit & Q&A arrangements
  6. Proposal preparation requirements
  7. Proposal submission
  8. Bid opening & evaluation procedure
  9. Contract award
  10. Disqualification clauses

Volume 2: Statement of Requirements
  1. Project background & objectives
  2. Project scope
  3. Overall technical architecture requirements
  4. Functional requirements detail
  5. Non-functional requirements
  6. Data requirements
  7. Integration requirements
  8. Security requirements
  9. Implementation requirements
  10. Acceptance criteria
  11. Operations & support requirements
  12. Training requirements

Volume 3: Commercial Terms
  1. Pricing requirements & format
  2. Payment terms
  3. Warranty period requirements
  4. Intellectual property
  5. Confidentiality requirements
  6. Liability for breach
  7. Contract template

Volume 4: Appendices
  1. Proposal letter format
  2. Pricing schedule format
  3. Case-study list format
  4. Personnel résumé format
  5. Deviation table format
```

**6.2 Transport-Sector RFP Specific Requirements**

- Sovereign-tech / local-content compatibility evidence
- Security-classification compliance capability evidence (security product portion)
- Conformance with transport-sector standards (ISO / NTCIP / DATEX II / SAE / IEEE series)
- Transport-sector performance stress-testing requirements (peak holiday, extreme-weather scenarios)
- 24×7 operations & maintenance assurance capability

---

### Step 7: Proposal Evaluation Criteria Design

**Objective**: Design a scientific, fair, and quantifiable proposal evaluation methodology.

**Inputs**: Requirement priorities, project characteristics
**Outputs**: Evaluation methodology, detailed scoring rules

**Guidance**:

**7.1 Evaluation Method Selection**

| Method | Applicable Scenario | Description |
|--------|---------------------|-------------|
| Weighted composite scoring | Large technical differences between proposals | Combined technical + commercial scoring |
| Lowest evaluated-price | Highly standardized | Compare price after technical compliance |
| Best value for money | Need to balance tech & price | Score / price ratio |

**Transport-sector recommendation**: Weighted composite scoring (Technical 60–70% + Commercial/Price 30–40%)

**7.2 Sample Scoring Rules**

```
Smart-Mobility Project Scoring Rules (Total 100 points):

I. Technical (65 points)
  1. Project understanding & requirements analysis (5)
  2. Overall technical solution (15)
     - Architecture (5)
     - Functional design (5)
     - Data solution (3)
     - Integration approach (2)
  3. Key technical capability (10)
     - AI / big-data capability (5)
     - GIS / visualization capability (3)
     - Real-time computing capability (2)
  4. Implementation approach (10)
     - Implementation plan (3)
     - Project management (2)
     - Risk control (2)
     - Quality management (3)
  5. Project team (8)
     - Project manager qualification (3)
     - Technical lead (3)
     - Overall team composition (2)
  6. Comparable project cases (7)
     - Number of transport-sector cases (3)
     - Case scale & complexity (2)
     - Client evaluation (2)
  7. Operations service plan (5)
  8. Training & knowledge transfer (5)

II. Commercial (35 points)
  1. Price (25)
     - Price score = (lowest quote / this quote) × 25
  2. Company strength (5)
     - Certifications (3)
     - Financial health (2)
  3. Local / in-region service (3)
  4. Intellectual property (2)
```

**7.3 Transport-Sector Focus Areas**

- Require copies of transport-sector contracts (with amounts and signatures)
- Experience and qualifications of key personnel (project manager, architect)
- Reasonableness of transport-sector performance stress-test plan
- Data-security and personal-information protection approach

---

### Step 8: RFP Issuance & Response Management

**Objective**: Formally issue the RFP and manage vendor Q&A and proposal submission.

**Inputs**: RFP documents, evaluation criteria, shortlist
**Outputs**: Proposal documents, evaluation report

**Guidance**:

**8.1 RFP Timeline**

| Milestone | Timing | Activity |
|-----------|:---:|------|
| RFP issued | D-Day | Send RFP to shortlisted vendors |
| Site visit | D+5 | Organize vendors to understand actual site conditions |
| Q&A submission deadline | D+10 | Vendors submit written questions |
| Q&A response | D+14 | Send Q&A minutes to all vendors |
| Proposal submission | D+28 | Vendors submit sealed proposals |
| Bid opening | D+28 | Open or internal bid opening |
| Proposal evaluation | D+29~D+35 | Evaluation committee review |
| Award announcement | D+38 | Publish shortlisted award candidate |

**8.2 Response Management Essentials**
- Equal treatment for all vendors: same RFP, same Q&A minutes
- Q&A responses must not disclose any vendor's commercial information
- Late proposals strictly rejected
- Sealed-submission and sign-off procedures standardized

---

## V. Roles & Responsibilities (RACI Matrix)

| Activity | Project Manager | Technical Lead | Procurement | Client Sponsor | Legal |
|----------|:---:|:---:|:---:|:---:|:---:|
| Requirements confirmation | C | **R/A** | I | C | I |
| Tech spec authoring | I | **R/A** | I | I | I |
| RFI design | C | **R** | **A** | I | I |
| RFI analysis & screening | C | **R** | **A** | I | I |
| RFP authoring | C | **R** | **A** | I | C |
| Evaluation criteria design | C | **R** | **A** | C | I |
| Evaluation execution | I | **R** | **R** | **A** | C |
| Award | I | I | C | **A** | C |

---

## VI. Key Checkpoints

| # | Checkpoint | Pass Criteria |
|---|------------|---------------|
| CP1 | SOW quality review | Clear scope boundaries, quantified deliverables, measurable acceptance |
| CP2 | Sufficient RFI responses | ≥ 5 qualified RFI responses received |
| CP3 | Shortlist quality | 3–5 vendors, covering different vendor types |
| CP4 | RFP compliance review | Legal confirms RFP terms compliant |
| CP5 | Evaluation criteria approval | Sponsor approves evaluation methodology |
| CP6 | Proposal compliance | All proposals submitted per standard |

---

## VII. Estimated Duration

| Phase | Duration |
|------|:---:|
| Requirements confirmation + SOW authoring | 1–2 weeks |
| RFI design → issue → collect → analyze | 3–4 weeks |
| RFP authoring + approval | 1–2 weeks |
| RFP issue → proposals → evaluation → award | 4–6 weeks |
| **Total (SOW to award)** | **9–14 weeks** |

---

## VIII. Common Pitfalls & Countermeasures

| # | Pitfall | Countermeasure |
|---|---------|----------------|
| 1 | Ambiguous SOW scope causes later disputes | Confirm boundaries repeatedly with stakeholders during SOW authoring |
| 2 | Tech specs point too narrowly at a specific vendor | Describe specs by outcome, not implementation |
| 3 | Too-short procurement window leaves vendors unprepared | Complex transport projects need ≥ 4 weeks for proposal preparation |
| 4 | Overly vague evaluation criteria | Break scoring items into quantifiable metrics, reduce evaluator discretion |
| 5 | Lowest-price award yields poor quality | Set a technical pass-mark (e.g., > 40 / 65) to avoid "cheap but inferior" awards |
| 6 | Ignoring sovereign-tech / local-content requirements | State sovereign-tech compliance requirements explicitly in the RFP |

---

## IX. Deliverables List

1. **Requirements Baseline Confirmation** (.docx)
2. **Statement of Work (SOW)** (.docx)
3. **Technical Specification Document** (.docx)
4. **RFI Package** (.docx + questionnaire .xlsx)
5. **RFI Analysis Report** (.docx)
6. **Vendor Shortlist** (.xlsx)
7. **Full RFP Document Set** (.docx)
8. **Evaluation Methodology & Scoring Rules** (.docx)
9. **Q&A Minutes** (.docx)
10. **Proposal Evaluation Report** (.docx)

---

> **Version**: V1.0 | **Date**: 2025-07 | **Applicable to**: Transport-sector IT procurement projects
