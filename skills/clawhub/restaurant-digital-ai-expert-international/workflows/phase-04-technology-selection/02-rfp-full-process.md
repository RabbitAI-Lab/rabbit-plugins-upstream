# 02-RFP Full Process

## Triggers
- After the short list is determined, need to formally issue an RFP (Request for Proposal) to vendors

## When Is an RFP Needed?

| Situation | Formal RFP Needed? | Alternative Approach |
|-----------|:---:|---------------------|
| 1-3 locations buying a POS | No | Directly compare 2-3 demos |
| 10-50 locations buying a core system | Simplified RFP | 1-page requirements list + Demo + price comparison |
| 50-200 locations / contract >$100K | Yes | Formal RFP process |
| 200+ locations / contract >$500K | Yes (legal involvement) | Complete RFP process + PoC |

---

## RFP Document Structure (Standard 8 Sections)

```
1. Project Background & Objectives
2. Project Scope & Technical Requirements
3. Implementation & Delivery Requirements
4. Service & SLA Requirements
5. Vendor Qualification Requirements
6. Commercial Terms
7. Scoring Criteria
8. Response Format Requirements
```

---

## Section 1: Project Background & Objectives

**Writing Guidelines**:
- Briefly describe the company/brand basics (locations / format / current systems / pain points)
- Clearly state project objectives (quantified, e.g., "reduce location reconciliation time from 30 minutes to 5 minutes")
- Explain why this project is being initiated now

**Template**:
```
[Brand Name] currently operates [XX] [format] locations across [regions], with annual revenue of approximately [$XX]M.
Currently using [XX systems], experiencing [XX pain points].
This project aims to [XX objectives], with expected realization of [XX quantified benefits].
```

---

## Section 2: Project Scope & Technical Requirements

**Writing Guidelines**:
- Use MECE method to list all functional requirements
- Differentiate between "Must-Have" and "Nice-to-Have"
- Technical requirements should be clear but not prescribe specific technical solutions (leave room for vendor innovation)

### Functional Requirements Matrix Template

| Req ID | Functional Domain | Requirement Description | Priority | Quantified Standard |
|--------|------------------|------------------------|:---:|---------------------|
| F-01 | POS-Ordering | Support QR ordering, server ordering, self-service kiosk | Must | <=2 taps to complete order |
| F-02 | POS-Payment | Support credit card / Apple Pay / Google Pay / stored value | Must | Payment success rate >99.5% |
| F-03 | POS-Refund | Support original payment method refund, partial refund | Must | Refund processing <5 min |
| F-04 | KDS-Routing | Auto-route by item type to different prep stations | Must | Latency <1 second |
| F-05 | CRM-Points | Earn points on spend + points redemption + points exchange | Must | Points posting delay <10 sec |
| ... | ... | ... | ... | ... |

### Technical Requirements Template

| Req ID | Technical Domain | Requirement Description | Priority |
|--------|-----------------|------------------------|:---:|
| T-01 | Architecture | Support cloud-native deployment, support elastic scaling | Must |
| T-02 | Resiliency | 99.9% availability, RTO <1 hour, RPO <5 min | Must |
| T-03 | API | Provide RESTful API, support OAuth 2.0 authentication | Must |
| T-04 | Data | Support data export, no data lock-in | Must |
| T-05 | Security | SOC 2 certification, encryption in transit + at rest | Must |

---

## Section 3: Implementation & Delivery Requirements

| Req ID | Implementation Requirement | Standard | Notes |
|--------|---------------------------|----------|-------|
| I-01 | Implementation timeline | <X months (first location go-live) | From contract signing date |
| I-02 | Training | Cover all store managers + regional managers | Including training manuals |
| I-03 | Data migration | Migrate X members + Y orders | Zero data loss |
| I-04 | Pilot | X pilot locations for X weeks | Pilot pass criteria in appendix |
| I-05 | Rollout cadence | X locations per week go-live | Must support phased rollout |

---

## Section 4: Service & SLA Requirements

| Service Item | SLA Standard | Monitoring Method | Penalty Mechanism |
|-------------|-------------|-------------------|-------------------|
| System Availability | >=99.9% (lunch/dinner peak >=99.95%) | Independent monitoring tool | 5% monthly fee reduction per 9 below target |
| Response Time | Peak page load <2 seconds | APM tool | 1% monthly fee reduction per violation |
| Incident Response | P0: 15-minute response | Ticketing system | $1,000 penalty per 30 min delay |
| Incident Recovery | P0: <1 hour recovery | Ticketing system | Per-minute penalty |
| Customer Support | 7x12 hours (peak hour coverage mandatory) | Ticketing system | Included in quarterly evaluation |
| Version Updates | 2 weeks advance notice + off-peak deployment window | Release calendar | -- |

### P0/P1/P2/P3 Classification Standard

| Level | Definition | Example | Response | Recovery |
|-------|-----------|---------|:---:|:---:|
| P0 | System unavailable / cannot process payments | POS down across all locations | 15 min | 1 hour |
| P1 | Core functionality unavailable | QR ordering down | 30 min | 4 hours |
| P2 | Partial functionality degraded | Report data delayed | 2 hours | 24 hours |
| P3 | Minor issue | UI display bug | 8 hours | Next release |

---

## Section 5: Vendor Qualification Requirements

- [ ] Founded >=3 years (reduces failure risk)
- [ ] Restaurant industry clients >=50
- [ ] At least 3 same-scale / same-format client case studies
- [ ] Can provide client references (including contact details, permitting reference checks)
- [ ] Technical team >=20 people
- [ ] Within 24 hours of project site (or remote with proven response capability)
- [ ] Provide most recent annual audited financial statements or equivalent financial health certification

---

## Section 6: Commercial Terms

| Term | Requirement | Notes |
|------|-------------|-------|
| Pricing Model | Subscription-based (per location / per order / hybrid) | Perpetual license only for exceptional cases |
| Payment Schedule | 3:3:3:1 (signing:go-live:acceptance:maintenance) | Adjustable to project specifics |
| Contract Term | 1 year + auto-renewal | Avoid long-term lock-in |
| Exit Clause | 3 months advance notice, no penalty | Data must be fully exportable |
| Price Protection | Renewal increase <= CPI + 3% | Prevent price gouging |
| Intellectual Property | Client data belongs to client | Clarify data processing rights |

---

## Section 7: Scoring Criteria (Transparent & Public)

Must disclose scoring weights in the RFP:

| Scoring Dimension | Weight |
|:---:|:---:|
| Product functionality fit | 30% |
| Technical architecture & scalability | 20% |
| Implementation & service capability | 15% |
| Vendor strength & stability | 15% |
| Pricing & commercial terms | 10% |
| Industry experience & case studies | 10% |

---

## Section 8: Response Format Requirements

- Deadline: [Date] [Time] (specify time zone)
- Response language: English
- File format: PDF + PPT (for presentation)
- Pricing template: Use the attached "Commercial Pricing Template"
- Clarification question deadline: [Date] (email questions only, unified response to all)

---

## RFP Full Process Timeline

```
T-14 days: Issue RFP to shortlisted vendors (3-5 vendors)
T-7 days:  Vendor question collection deadline; unified written/virtual clarification
T+0 days:  Vendor submits proposal + pricing (sealed)
T+3 days:  Internal review + scoring (2-3 people score independently, take average)
T+5 days:  Notify 2-3 vendors advancing to the next round
T+14 days: Each vendor: 2-hour live demo (including Q&A)
T+15 days: Team discussion + aggregate scoring + ranking
T+16 days: Notify selected and non-selected vendors
T+30 days: Contract signed
```

---

## Common RFP Mistakes & How to Avoid Them

| Mistake | Consequence | How to Avoid |
|---------|-------------|--------------|
| Requirements too broad and vague | Vendor quotes vary wildly, impossible to compare | Requirements must be specific, quantifiable, verifiable |
| Only comparing price, not TCO | Fall for low initial price, get gouged on service fees later | TCO model covering 3-5 years |
| Not requiring client references | Deceived by polished vendor demos | Require 3 contactable client references (mandatory) |
| Sending RFP to unsuitable vendors | Wastes everyone's time | Screen before issuing RFP |
| Scoring based on gut feel | Internal conflict, wrong vendor selected | Independent scoring + forced ranking + average |

---

## Deliverables
- Formal RFP document (8-section full version or simplified version)
- Vendor long list -> short list -> second-round list
- RFP schedule timeline

## Quality Checks
- [ ] Every functional requirement in the RFP has a clear quantified standard (not "supports XX" but "under XX conditions, within XX seconds")
- [ ] SLAs have penalty mechanisms (an SLA without teeth is worthless paper)
- [ ] Scoring weights are transparent and publicly disclosed
- [ ] At least 3 contactable client references are required
