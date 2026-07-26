# Technology Selection & Vendor Evaluation Report

> **Project Name:** [XX System / Platform] — Technology Selection & Vendor Evaluation
> **Sponsor:** [Organization Name]
> **Date:** [YYYY-MM-DD]
> **Version:** V[X.X]

---

## Table of Contents

1. [Business Requirements Summary](#1-business-requirements-summary)
2. [Technical Requirements Specification](#2-technical-requirements-specification)
3. [Market Research](#3-market-research)
4. [Shortlisted Candidate Vendors](#4-shortlisted-candidate-vendors)
5. [Evaluation Methodology](#5-evaluation-methodology)
6. [Vendor Profiles & Scoring](#6-vendor-profiles--scoring)
7. [Proof-of-Concept (PoC) Results](#7-proof-of-concept-poc-results)
8. [TCO Comparison (5-Year)](#8-tco-comparison-5-year)
9. [Reference Customer Research](#9-reference-customer-research)
10. [Recommended Solution & Rationale](#10-recommended-solution--rationale)
11. [Commercial Negotiation Position](#11-commercial-negotiation-position)
12. [Implementation Partner Selection](#12-implementation-partner-selection)
13. [Appendices](#13-appendices)

---

## 1. Business Requirements Summary

### 1.1 Project Background

[Briefly explain why this project is needed: business pain points, strategic drivers, regulatory requirements, etc. 2–3 paragraphs.]

> **Example:** "As average daily traffic on [XX Motorway] exceeds [XX] thousand vehicles, the existing toll system (built in 2015) can no longer support growing throughput. Peak response latency exceeds [X] seconds, causing recurring toll-plaza congestion and a [XX%] YoY increase in public complaints. Meanwhile, regulator [XX] requires full implementation of XXX by 202X; this project is the core measure to meet that requirement."

### 1.2 Business Objectives

| No. | Business Objective | Quantified Metric | Priority |
|-----|--------------------|-------------------|---------|
| B1 | [Objective, e.g., improve throughput] | [Metric, e.g., per-vehicle pass time ≤ 3 sec] | P0 — Mandatory |
| B2 | [Objective] | [Quantified metric] | P1 — Important |
| B3 | [Objective] | [Quantified metric] | P1 — Important |
| B4 | [Objective] | [Quantified metric] | P2 — Desirable |
| B5 | [Objective] | [Quantified metric] | P2 — Desirable |

### 1.3 Business Scope

| Dimension | Scope Description |
|-----------|------------------|
| Business modules | [Which modules are covered] |
| Organizational scope | [Which departments / subsidiaries] |
| Geographic scope | [Which stations / corridors / zones] |
| User scope | [Internal users / external users] |
| Data scope | [Which data types / volumes] |

### 1.4 Key Constraints

| Constraint Type | Description | Impact |
|-----------------|-------------|-------|
| Time | [Must go live by YYYY-MM-DD] | [Notes] |
| Budget | [Total budget ≤ €XX M] | [Notes] |
| Technical | [Must be compatible with existing XX system / run on XX network] | [Notes] |
| Compliance | [Must pass ISO 27001 / meet XX regulation] | [Notes] |
| Technology sovereignty | [Local-content / open-standards requirement: open-source-friendly stack; no single-vendor lock-in; standards-based interfaces] | [Notes] |

---

## 2. Technical Requirements Specification

### 2.1 Functional Requirements

| ID | Module | Requirement Description | Priority | Acceptance Criteria |
|----|--------|-------------------------|----------|---------------------|
| F-01 | [Module] | [Detailed function] | P0 | [Testable standard] |
| F-02 | [Module] | [Detailed function] | P0 | [Testable standard] |
| F-03 | [Module] | [Detailed function] | P1 | [Testable standard] |
| ... | ... | ... | ... | ... |
| F-NN | [Module] | [Detailed function] | P2 | [Testable standard] |

### 2.2 Non-Functional Requirements

| ID | Category | Requirement | Quantified Metric | Priority |
|----|----------|-------------|-------------------|----------|
| NF-01 | Performance | Response time | Routine op ≤ [X] sec; complex query ≤ [X] sec | P0 |
| NF-02 | Performance | Concurrency | Support ≥ [XXXX] concurrent users / endpoints | P0 |
| NF-03 | Availability | System SLA | ≥ 99.9% (annual downtime < 8.76 h) | P0 |
| NF-04 | Scalability | Horizontal scale | Support [X×] data / user growth with no architecture change | P1 |
| NF-05 | Security | Security level | ISO 27001 / IEC 62443; encryption in transit + at rest | P0 |
| NF-06 | Maintainability | O&M complexity | Automated deployment, monitoring/alerting, canary release | P1 |
| NF-07 | Compatibility | Open-standards compatibility | Linux (RHEL / Ubuntu) + PostgreSQL / open-source RDBMS | P0/P1 |
| NF-08 | Data timeliness | Data latency | Real-time ≤ [X] sec; batch ≤ [X] min | P0 |
| NF-09 | Integration | API / integration | Standard RESTful API + message queue | P1 |
| NF-10 | Internationalization | Multi-language | EN / [local language] UI switch | P2 |

### 2.3 Potential Expansion Requirements (Future Scope)

[List functions not in scope now but possibly needed later, to test platform extensibility / foresight.]

| ID | Expansion Need | Expected Timing | Impact on Selection |
|----|----------------|-----------------|---------------------|
| E-01 | [e.g., AI vision analytics extension] | [Y2–Y3] | [Must reserve AI inference framework integration] |
| E-02 | [e.g., digital twin] | [Y3] | [Must support 3D engine / WebGL] |

---

## 3. Market Research

### 3.1 Market Overview

[Briefly describe the market size, trend, key players, and technology evolution of this domain. 1–2 paragraphs.]

> **Example:** "The global transport data-platform market is approximately [€XX B] in 2024, with a CAGR of about [XX]%. Main vendors fall into three groups: ① hyperscale cloud providers (AWS, Microsoft Azure, Google Cloud); ② global IT & engineering firms (IBM, Cisco, SAP, Siemens Mobility); ③ transport-vertical specialists (Thales, Kapsch, Yunex, Cubic, Swarco, Q-Free, Indra). Architecturally, Data Fabric, Data Mesh, and Lakehouse concepts are progressively penetrating the sector……"

### 3.2 Long List Screening

[List all initially researched potential vendors (10–15) and the basis for preliminary screening.]

| No. | Vendor / Product | Type | Preliminary Conclusion | Reason |
|-----|------------------|------|------------------------|-------|
| 1 | [Vendor A — Product X] | [Cloud / IT / vertical] | ✅ Shortlist | [Reason] |
| 2 | [Vendor B — Product Y] | [Type] | ✅ Shortlist | [Reason] |
| 3 | [Vendor C — Product Z] | [Type] | ✅ Shortlist | [Reason] |
| 4 | [Vendor D] | [Type] | ❌ Drop | [Too small / no transport case / supply risk] |
| 5 | [Vendor E] | [Type] | ❌ Drop | [Product EOL / supply risk] |
| ... | ... | ... | ... | ... |

### 3.3 Shortlist Confirmation

After preliminary screening, the following [3–5] vendors enter detailed evaluation:

| No. | Vendor | Product / Solution | Rationale for Shortlist |
|-----|--------|-------------------|--------------------------|
| 1 | [Vendor A] | [Product name + version] | [Reason: #1 market share, rich transport cases] |
| 2 | [Vendor B] | [Product name + version] | [Reason: most advanced architecture, best open-standards support] |
| 3 | [Vendor C] | [Product name + version] | [Reason: existing relationship, lowest TCO] |
| 4 | [Vendor D] | [Product name + version] | [Reason: open-source route, avoids lock-in] |
| 5 | [Vendor E] | [Product name + version] | [Reason: transport-focused, best functional fit] |

---

## 4. Shortlisted Candidate Vendors

### 4.1 Vendor A: [Full Name]

| Item | Detail |
|------|-------|
| **Company profile** | Founded [XXXX], HQ [XX], [XXXX]+ employees, [public / private] |
| **Revenue scale** | [€XX B] (202X), relevant product-line revenue [€XX B] |
| **Market share** | Rank [X] globally, rank [X] in transport (Source: IDC / Gartner) |
| **Core product** | [Product name + version + release date] |
| **Tech architecture** | [Microservices / monolith], [Java / Go / Python], [K8s / Docker], [PostgreSQL / self-developed DB] |
| **Transport cases** | [XX] transport clients, including: [3–5 benchmark clients] |
| **Open-standards support** | Adaptation to [Linux / PostgreSQL / Kafka / etc.] |
| **Certifications** | [CMMI L5 / ISO 27001 / ISO 20000 / IEC 62443 / …] |
| **R&D investment** | [XXXX]+ R&D staff, annual R&D [€XX B] ([XX%] of revenue) |
| **Strengths** | [3–5 core strengths] |
| **Potential risks** | [3–5 potential risks / concerns] |

### 4.2 Vendor B: [Full Name]

[Follow 4.1 format]

### 4.3 Vendor C: [Full Name]

[Follow 4.1 format]

### 4.4 Vendor D: [Full Name]

[Follow 4.1 format]

### 4.5 Vendor E: [Full Name]

[Follow 4.1 format]

---

## 5. Evaluation Methodology

### 5.1 Seven-Dimension Framework

This evaluation uses the **"7D-TEVF" (7-Dimension Technology Evaluation & Vendor Selection Framework)** to comprehensively assess candidate vendors across seven dimensions.

| Dimension | Weight | Assessment Content | Data Source |
|-----------|--------|--------------------|-------------|
| **D1: Functional Fit** | 25% | Satisfaction of P0/P1/P2 functional needs | Requirement matrix, demo, PoC |
| **D2: Tech Architecture** | 20% | Architecture modernity, scalability, performance, security, openness & standardization | Whitepaper review, PoC test, architecture review |
| **D3: Vendor Strength** | 15% | Company scale, financials, R&D, market position, continuity | Annual reports, 3rd-party (IDC / Gartner), site visit |
| **D4: Industry Experience** | 15% | Transport case count & quality, solution maturity, domain insight | Reference interviews, case review |
| **D5: TCO** | 10% | 5-year TCO (license / hardware / implementation / O&M / upgrade) | Quote analysis, TCO model |
| **D6: Service & Support** | 10% | Implementation, after-sales, training, local support | SLA commitment, reference feedback |
| **D7: Ecosystem & Compatibility** | 5% | API / standard support, ISV ecosystem, compatibility with existing stack, open-standards adaptation | Integration test, ecosystem list review |

### 5.2 Scoring Scale

| Score | Level | Meaning |
|-------|-------|---------|
| 5.0 | Excellent | Fully meets and exceeds expectations; distinctive advantage |
| 4.0 | Good | Meets needs; no significant gaps |
| 3.0 | Adequate | Basically meets; minor gaps not affecting core function |
| 2.0 | Insufficient | Significant gaps; heavy customization or compromise needed |
| 1.0 | Unacceptable | Does not meet need; veto item |

### 5.3 Hard Gates (Veto Items)

Failure of any of the following disqualifies the vendor immediately:

1. [Must hold ISO 27001 / IEC 62443 certification]
2. [Must support open-standards OS (Linux) and open-source RDBMS (PostgreSQL)]
3. [Must have ≥ 3 transport cases of comparable scale]
4. [System must support ≥ XX concurrency]
5. [5-year TCO must not exceed 120% of budget]

### 5.4 Evaluation Process

```
RFI issued → Vendor response → Long-list screening → RFP issued → Vendor tech proposal
    → Technical / commercial review → Shortlist confirmed → PoC test → Reference research
    → Composite scoring → Negotiation → Recommendation → Final decision
```

| Stage | Date | Participants | Deliverable |
|-------|------|--------------|-------------|
| RFI / RFP | [YYYY-MM-DD] | Procurement / IT / Business | RFI / RFP docs |
| Tech proposal & bid | [YYYY-MM-DD] | Vendor | Tech proposal doc |
| Review & scoring | [YYYY-MM-DD] | Review committee | Scorecard |
| PoC test | [YYYY-MM-DD] | Tech team | PoC report |
| Reference research | [YYYY-MM-DD] | Business / IT | Research notes |
| Composite review | [YYYY-MM-DD] | Review committee | Recommendation report (this doc) |
| Commercial negotiation | [YYYY-MM-DD] | Procurement / Legal | Contract draft |
| Final decision | [YYYY-MM-DD] | Decision committee | Procurement resolution |

---

## 6. Vendor Profiles & Scoring

### 6.1 Composite Score Matrix

| Dimension | Weight | Vendor A | Vendor B | Vendor C | Vendor D | Vendor E |
|-----------|--------|----------|----------|----------|----------|----------|
| D1: Functional Fit | 25% | [X.X] | [X.X] | [X.X] | [X.X] | [X.X] |
| D2: Tech Architecture | 20% | [X.X] | [X.X] | [X.X] | [X.X] | [X.X] |
| D3: Vendor Strength | 15% | [X.X] | [X.X] | [X.X] | [X.X] | [X.X] |
| D4: Industry Experience | 15% | [X.X] | [X.X] | [X.X] | [X.X] | [X.X] |
| D5: TCO | 10% | [X.X] | [X.X] | [X.X] | [X.X] | [X.X] |
| D6: Service & Support | 10% | [X.X] | [X.X] | [X.X] | [X.X] | [X.X] |
| D7: Ecosystem & Compatibility | 5% | [X.X] | [X.X] | [X.X] | [X.X] | [X.X] |
| **Weighted total** | **100%** | **[X.X]** | **[X.X]** | **[X.X]** | **[X.X]** | **[X.X]** |
| **Rank** | — | **[X]** | **[X]** | **[X]** | **[X]** | **[X]** |

### 6.2 Detailed Scoring & Basis per Dimension

#### D1: Functional Fit (Weight 25%)

| P0 Function | Vendor A | Vendor B | Vendor C | Vendor D | Vendor E |
|-------------|----------|----------|----------|----------|----------|
| F-01: [Name] | ✅ Native | ✅ Native | ⚠️ Custom | ✅ Native | ❌ None |
| F-02: [Name] | ✅ Native | ⚠️ 3rd-party | ✅ Native | ✅ Native | ✅ Native |
| ... | ... | ... | ... | ... | ... |

**P0 satisfaction rate:** A:[XX%] B:[XX%] C:[XX%] D:[XX%] E:[XX%]
**P0+P1 satisfaction rate:** A:[XX%] B:[XX%] C:[XX%] D:[XX%] E:[XX%]

**D1 scoring basis:**

- **Vendor A ([X.X]):** [Rationale]
- **Vendor B ([X.X]):** [Rationale]
- ...

#### D2: Tech Architecture (Weight 20%)

| Item | Vendor A | Vendor B | Vendor C | Vendor D | Vendor E |
|------|----------|----------|----------|----------|----------|
| Architecture style | [Microservices] | [Modular monolith] | [Microservices] | [Microservices] | [SOA] |
| Containerization & orchestration | [K8s-native] | [Docker Swarm] | [K8s] | [K8s] | [K8s] |
| Stack modernity | [High] | [Med] | [High] | [High] | [Low-Med] |
| API standardization | [REST+GraphQL] | [REST] | [REST+gRPC] | [REST] | [REST+SOAP] |
| HA architecture | [Active-active] | [Active-standby] | [Active-active] | [Active-standby] | [Active-standby] |
| Performance benchmark (PoC) | [See 7.3] | [See 7.3] | [See 7.3] | [See 7.3] | [See 7.3] |
| Security framework completeness | [High] | [High] | [Med] | [High] | [Med] |
| Scalability | [Horizontal] | [Limited] | [Horizontal] | [Horizontal] | [Limited] |
| Open-source dependency / license risk | [Low] | [Low] | [Med] | [Low] | [High] |

**D2 scoring basis:**

- **Vendor A ([X.X]):** [Rationale]
- ...

#### D3: Vendor Strength (Weight 15%)

| Item | Vendor A | Vendor B | Vendor C | Vendor D | Vendor E |
|------|----------|----------|----------|----------|----------|
| Annual revenue (€B) | [XX] | [XX] | [XX] | [XX] | [XX] |
| Relevant product-line revenue | [XX] | [XX] | [XX] | [XX] | [XX] |
| Total employees | [XXXX] | [XXXX] | [XXXX] | [XXXX] | [XXXX] |
| R&D staff ratio | [XX%] | [XX%] | [XX%] | [XX%] | [XX%] |
| Financial rating | [AAA/AA/A] | [...] | [...] | [...] | [...] |
| IPO / public status | [Public / private] | [...] | [...] | [...] | [...] |
| Negative risk | [None / Yes: XX] | [...] | [...] | [...] | [...] |

**D3 scoring basis:** [Detailed explanation]

#### D4: Industry Experience (Weight 15%)

| Item | Vendor A | Vendor B | Vendor C | Vendor D | Vendor E |
|------|----------|----------|----------|----------|----------|
| Transport clients | [XX] | [XX] | [XX] | [XX] | [XX] |
| Comparable-scale cases | [X] | [X] | [X] | [X] | [X] |
| Transport solution maturity | [High/Med/Low] | [...] | [...] | [...] | [...] |
| Benchmark clients | [List] | [List] | [List] | [List] | [List] |
| Customer satisfaction (ref.) | [X.X/5] | [X.X/5] | [X.X/5] | [X.X/5] | [X.X/5] |

**D4 scoring basis:** [Detailed explanation]

#### D5: TCO (Weight 10%)

[See Chapter 8 TCO comparison; summary scores here.]

| Vendor | 5-yr TCO (€M) | Relative Index | D5 Score |
|--------|---------------|----------------|----------|
| Vendor A | [XXXX] | 1.00 (baseline) | [X.X] |
| Vendor B | [XXXX] | 0.85 | [X.X] |
| ... | ... | ... | ... |

#### D6: Service & Support (Weight 10%)

| Item | Vendor A | Vendor B | Vendor C | Vendor D | Vendor E |
|------|----------|----------|----------|----------|----------|
| Implementation team (local) | [XX] | [XX] | [XX] | [XX] | [XX] |
| Local service offices | [XX] offices | [...] | [...] | [...] | [...] |
| After-sales SLA | [7×24 / 5×8] | [...] | [...] | [...] | [...] |
| On-site support | [X-hr on-site in region] | [...] | [...] | [...] | [...] |
| Training service | [Structured / none] | [...] | [...] | [...] | [...] |
| Service reputation (ref.) | [X.X/5] | [X.X/5] | [X.X/5] | [X.X/5] | [X.X/5] |

**D6 scoring basis:** [Detailed explanation]

#### D7: Ecosystem & Compatibility (Weight 5%)

| Item | Vendor A | Vendor B | Vendor C | Vendor D | Vendor E |
|------|----------|----------|----------|----------|----------|
| Open API / standardization | [High/Med/Low] | [...] | [...] | [...] | [...] |
| ISV / partner ecosystem | [XX] | [XX] | [XX] | [XX] | [XX] |
| Compatibility with existing systems | [High/Med/Low] | [...] | [...] | [...] | [...] |
| Open-standards adaptation completeness | [Full CPU/OS/DB coverage] | [...] | [...] | [...] | [...] |

**D7 scoring basis:** [Detailed explanation]

---

## 7. Proof-of-Concept (PoC) Results

### 7.1 PoC Scope & Scenarios

| ID | Scenario | Objective | Linked Requirement | Pass Criteria |
|----|----------|-----------|--------------------|---------------|
| TC-01 | [Scenario] | [What to verify] | [F-01/NF-03] | [Quantified] |
| TC-02 | [Scenario] | [What to verify] | [F-03/F-05] | [Quantified] |
| TC-03 | [Scenario] | [What to verify] | [NF-01] | [Quantified] |
| TC-04 | [Stress / performance] | [Verify concurrency] | [NF-02] | [Quantified] |
| TC-05 | [Integration] | [Verify linkage with XX system] | [NF-09] | [Quantified] |
| TC-06 | [Security test] | [Verify security framework] | [NF-05] | [Quantified] |

### 7.2 PoC Environment

| Item | Description |
|------|-------------|
| Test environment | [Hardware spec / VM spec / cloud instance type] |
| Data scale | [Simulated volume / masked real volume] |
| Test tools | [JMeter / LoadRunner / custom scripts] |
| Test period | [YYYY-MM-DD to YYYY-MM-DD] |

### 7.3 PoC Results

| Scenario | Vendor A | Vendor B | Vendor C | Vendor D | Vendor E |
|----------|----------|----------|----------|----------|----------|
| TC-01: [Name] | ✅ Pass | ✅ Pass | ⚠️ Partial | ✅ Pass | ❌ Fail |
| TC-02: [Name] | ✅ Pass | ✅ Pass | ✅ Pass | ✅ Pass | ✅ Pass |
| TC-03: [Name] | ✅ Pass | ⚠️ Partial | ✅ Pass | ✅ Pass | ⚠️ Partial |
| TC-04: [Stress] | [TPS:XXX] | [TPS:XXX] | [TPS:XXX] | [TPS:XXX] | [TPS:XXX] |
| TC-05: [Integration] | ✅ Pass | ⚠️ Partial | ✅ Pass | ❌ Fail | ✅ Pass |
| TC-06: [Security] | ✅ Pass | ✅ Pass | ✅ Pass | ✅ Pass | ⚠️ Partial |
| **Pass rate** | **[XX%]** | **[XX%]** | **[XX%]** | **[XX%]** | **[XX%]** |

### 7.4 Key PoC Findings

**Vendor A:**
- Strengths: [Aspects that stood out]
- Weaknesses: [Issues surfaced]

**Vendor B:**
- Strengths: [...]
- Weaknesses: [...]

[Evaluate all PoC participants in turn]

---

## 8. TCO Comparison (5-Year)

### 8.1 TCO Model

**Scope: 5-year TCO = one-time investment + annual O&M cost × 5**

| Category | Cost Item | Notes |
|----------|-----------|-------|
| **CAPEX (one-time)** | Software license | [Feature / user / CPU license] |
| | Hardware / infrastructure | [Servers / storage / network] |
| | Implementation & custom dev | [Deployment, customization, data migration] |
| | 3rd-party software / middleware | [OS / DB / middleware] |
| **OPEX (annual)** | Maintenance / subscription | [Annual maintenance (typically 15–22% of license)] |
| | Cloud / IDC | [Cloud instances / racks / bandwidth] |
| | O&M personnel | [Need [X] O&M staff, avg cost €XXk/yr] |
| | Upgrade / expansion | [Expansion every 2–3 yrs] |
| | Training | [Annual training budget] |

### 8.2 TCO Detail per Vendor

#### Vendor A — 5-Year TCO

| Cost Item | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | Subtotal |
|-----------|--------|--------|--------|--------|--------|----------|
| Software license | [XXX] | — | — | — | — | [XXX] |
| Hardware | [XXX] | — | [XXX] | — | — | [XXX] |
| Implementation / custom | [XXX] | [XX] | — | — | — | [XXX] |
| Maintenance | [XX] | [XX] | [XX] | [XX] | [XX] | [XXX] |
| Cloud / IDC | [XX] | [XX] | [XX] | [XX] | [XX] | [XXX] |
| O&M personnel | [XX] | [XX] | [XX] | [XX] | [XX] | [XXX] |
| Training | [XX] | [X] | [X] | [X] | [X] | [XX] |
| **Annual total** | **[XXX]** | **[XXX]** | **[XXX]** | **[XXX]** | **[XXX]** | **[XXXX]** |

#### Vendor B — 5-Year TCO

[Same format as above]

#### Vendor C — 5-Year TCO

[Same format as above]

#### Vendor D — 5-Year TCO

[Same format as above]

#### Vendor E — 5-Year TCO

[Same format as above]

### 8.3 TCO Comparison

| Vendor | CAPEX Total | OPEX Total (5 yr) | 5-yr TCO | Relative Index | Rank |
|--------|-------------|-------------------|----------|----------------|------|
| Vendor A | [XXX] | [XXX] | [XXXX] | 1.00 | [X] |
| Vendor B | [XXX] | [XXX] | [XXXX] | 0.85 | [X] |
| Vendor C | [XXX] | [XXX] | [XXXX] | 0.92 | [X] |
| Vendor D | [XXX] | [XXX] | [XXXX] | 1.15 | [X] |
| Vendor E | [XXX] | [XXX] | [XXXX] | 0.78 | [X] |

### 8.4 Hidden-Cost Watch-outs

[Costs not in the quote but likely to occur: interface dev, data migration, change management, extra training, emergency expansion.]

| Hidden Cost | Est. Amount | Applies to all vendors? |
|-------------|-------------|-------------------------|
| [Data migration] | [€XX M] | Yes / No (Vendor XX already includes it) |
| [System integration dev] | [€XX M / system] | Yes |
| [Organizational change mgmt] | [€XX M] | Yes |
| ... | ... | ... |

---

## 9. Reference Customer Research

### 9.1 Research Method

| Item | Description |
|------|-------------|
| Method | [Phone interview / site visit / survey] |
| Targets | [2–3 references per vendor; prefer similar scale / industry] |
| Questions | [Standardized interview guide, see Appendix B] |
| Period | [YYYY-MM-DD to YYYY-MM-DD] |

### 9.2 Vendor A — Reference Feedback

| Reference | Project Scale | Go-live | Overall Rating | Strengths | Weaknesses / Issues |
|-----------|---------------|---------|----------------|-----------|---------------------|
| [XX Motorway Group] | [€XX M] | [202X] | [4.2/5] | [Strength 1, 2] | [Issue 1, 2] |
| [XX City Transport Dept] | [€XX M] | [202X] | [3.8/5] | [Strength 1] | [Issue 1] |
| [XX Port Authority] | [€XX M] | [202X] | [4.5/5] | [Strength 1, 2, 3] | [None significant] |

**Key quote:**

> "[Verbatim quote from reference, positive or negative]" — CIO, [XX Group]

**Composite customer satisfaction:** [X.X] / 5.0

### 9.3 Vendor B — Reference Feedback

[Same format as above]

### 9.4 Vendor C/D/E — Reference Feedback

[Expand in turn]

### 9.5 Reference Research Summary

| Vendor | Customers Surveyed | Avg Satisfaction | Recommend Rate | Key Strengths | Key Pain Points |
|--------|--------------------|------------------|----------------|---------------|-----------------|
| Vendor A | [X] | [X.X] | [X/X] | [Strengths] | [Pain] |
| Vendor B | [X] | [X.X] | [X/X] | [Strengths] | [Pain] |
| ... | ... | ... | ... | ... | ... |

---

## 10. Recommended Solution & Rationale

### 10.1 Recommendation

**Recommendation:** Select **[Vendor X]**'s **[Product Name]** as the technology platform for this project.

**Composite ranking:**

| Rank | Vendor | Weighted Total | Conclusion |
|------|--------|----------------|------------|
| 🥇 1st | [Vendor X] | [X.X] | **Recommended (primary)** |
| 🥈 2nd | [Vendor Y] | [X.X] | Backup |
| 🥉 3rd | [Vendor Z] | [X.X] | Not recommended |
| 4 | [...] | [...] | Not recommended |
| 5 | [...] | [...] | Not recommended |

### 10.2 Rationale (Why)

**Primary reasons:**

1. **Best functional fit:** [P0 satisfaction XX%; only vendor natively supporting XX]
2. **Richest industry experience:** [XX transport cases of comparable scale, incl. XX client highly similar to us]
3. **Best architecture:** [Cloud-native, containerized, horizontal scale; best PoC performance]
4. **Best ecosystem compatibility:** [Already adapted to our existing XX system; mature data-migration plan]
5. **Reasonable TCO:** [Not the lowest 5-yr TCO, but best value-for-money; highest capability/price ratio]

### 10.3 Backup Evaluation

**Backup: Vendor Y**

- **Strengths:** [vs. primary, e.g., lower price, more timely local service]
- **Weaknesses:** [vs. primary, e.g., lower functional fit, fewer industry cases]
- **When to switch:** [If the primary plan hits XX problem, switch to backup]

### 10.4 Dropped Vendors

| Dropped Vendor | Reason |
|----------------|--------|
| [Vendor Z] | [e.g., 3 P0 functions unsupported, veto] |
| [Vendor W] | [e.g., PoC stress test failed] |
| [Vendor V] | [e.g., 5-yr TCO exceeded 120% budget cap] |

---

## 11. Commercial Negotiation Position

### 11.1 Negotiation Points

| Item | Our Target | Vendor Initial Quote / Position | Strategy | Floor |
|------|------------|----------------------------------|----------|-------|
| **Price** | [License −XX%] | [Quote €XX M] | [Bring in backup competition; emphasize phase-2/3 upside] | [€XX M] |
| **Maintenance rate** | [≤15%] | [22%] | [Benchmark against market price] | [18%] |
| **Payment terms** | [30-30-30-10] | [50-30-20] | [Tie to milestones] | [40-30-30] |
| **IPR** | [Joint dev IP belongs to / shared with us] | [Vendor retains] | [Leverage phase-2 as bargaining chip] | [Shared + source escrow] |
| **Source escrow** | [Required] | [Not provided] | [Industry norm + risk control] | [At least escrow] |
| **Implementation service** | [XX person-months free] | [Fully charged] | [Bundle negotiation] | [XX person-months] |
| **SLA** | [99.9% + penalty] | [99.5%] | [Business continuity need] | [99.9% + penalty cap 50% of contract] |
| **Lock-in clause** | [No restriction on 3rd-party re-dev] | [OEM only] | [Long-term tech autonomy] | [OEM-certified 3rd party allowed] |

### 11.2 Negotiation Cadence

| Round | Content | Our Posture |
|-------|---------|-------------|
| 1 | State core asks; show backup options | Keep pressure |
| 2 | Deep negotiation on price, SLA, IPR | Hold principles |
| 3 | Concede on minor terms for core breakthroughs | Flexible trade |
| Final | Lock into contract | Careful review |

---

## 12. Implementation Partner Selection

### 12.1 Delivery Model Decision

| Model | Description | Strength | Weakness | Recommendation |
|-------|-------------|----------|----------|----------------|
| **OEM delivery** | Product vendor delivers directly | High quality, clear accountability | Costly, slow when resources tight | ✅ Recommended |
| **Partner delivery** | OEM-certified local partner delivers | Lower cost, fast local response | Variable quality | Backup |
| **Hybrid** | OEM for core + partner for general | Balances cost & quality | Complex coordination | Case-by-case |

### 12.2 Implementation Partner Evaluation (if partner model)

| Item | Partner A | Partner B | Partner C |
|------|-----------|-----------|-----------|
| Profile | [Desc] | [Desc] | [Desc] |
| OEM certification level | [Gold / Silver / Certified] | [...] | [...] |
| Similar project experience | [Count + scale] | [...] | [...] |
| Implementation team size | [XX] | [XX] | [XX] |
| Customer rating | [X.X/5] | [X.X/5] | [X.X/5] |
| Quote (implementation) | [€XX M] | [€XX M] | [€XX M] |
| Rank | [1st] | [2nd] | [3rd] |

### 12.3 Recommended Delivery Plan

**Recommendation:** [OEM delivery / XX partner / OEM+partner hybrid]

**Rationale:** [Detailed explanation]

---

## 13. Appendices

### Appendix A: Functional Requirement Matrix (Full)

[Table listing every functional requirement and each vendor's support: native / config / custom dev / 3rd-party / none.]

| Req ID | Description | Vendor A | Vendor B | Vendor C | Vendor D | Vendor E |
|--------|-------------|----------|----------|----------|----------|----------|
| F-01 | [Desc] | ✅ Native | ✅ Native | ⚠️ Custom | ✅ Native | ❌ None |
| F-02 | [Desc] | ✅ Native | ✅ Native | ✅ Native | ⚠️ Config | ✅ Native |
| ... | ... | ... | ... | ... | ... | ... |

### Appendix B: Reference Interview Guide

1. **Overall:** Out of 5, how satisfied are you overall with this vendor? Why?
2. **Product capability:** Did the product meet expectations? Highlights and gaps?
3. **Implementation:** Was the schedule on plan? What unexpected issues arose?
4. **After-sales:** Was issue response timely? How good was technical support?
5. **Value:** Satisfied with ROI? Any hidden costs?
6. **Re-do:** If you chose again, would you pick this vendor? Why?
7. **Risk tips:** Any "gotchas" I should watch for?

### Appendix C: Vendor Site-Visit Records

| Vendor | Date | Location | Content | Visitors | Impression |
|--------|------|----------|---------|----------|------------|
| [Vendor A] | [Date] | [R&D center / HQ] | [R&D / delivery / O&M center] | [Name] | [Impression] |
| ... | ... | ... | ... | ... | ... |

### Appendix D: Evaluation Team & Decision Committee

| Role | Name | Title | Responsibility |
|------|------|-------|----------------|
| Evaluation lead | [Name] | [CIO / CTO] | Overall, final recommendation |
| Tech review | [Name] | [Architect] | Tech dimension, PoC |
| Business review | [Name] | [Business head] | Requirement fit |
| Procurement / commercial | [Name] | [Procurement mgr] | Commercial terms, negotiation |
| Legal | [Name] | [Legal mgr] | Contract review |
| Decision approval | [Name] | [VP / GM] | Final decision |

### Appendix E: Evaluation Document Inventory

| No. | Document | Version | Date |
|-----|----------|---------|------|
| 1 | RFI (Request for Information) | V1.0 | [YYYY-MM-DD] |
| 2 | RFP (Request for Proposal) | V1.0 | [YYYY-MM-DD] |
| 3 | Vendor A technical proposal | — | [YYYY-MM-DD] |
| 4 | Vendor B technical proposal | — | [YYYY-MM-DD] |
| ... | ... | ... | ... |
| N | PoC test report | V1.0 | [YYYY-MM-DD] |
| N+1 | Reference interview compilation | V1.0 | [YYYY-MM-DD] |
| N+2 | Vendor site-visit report | V1.0 | [YYYY-MM-DD] |

---

> **Prepared by:** [Evaluation working group]
> **Reviewed by:** [Tech lead / commercial lead]
> **Approved by:** [Decision approver]
> **Date:** [YYYY-MM-DD]
>
> **Disclaimer:** The scores and conclusions in this report are based on information obtained during the evaluation period; actual vendor performance may differ. It is recommended to include adequate performance-guarantee clauses in the contract.
