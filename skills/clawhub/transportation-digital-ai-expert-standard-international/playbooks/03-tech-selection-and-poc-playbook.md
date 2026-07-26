# Technology Selection & PoC Execution Playbook

## Playbook Overview

| Item | Description |
|------|-------------|
| **Applicable scenarios** | Transport authorities / enterprises selecting a critical technology solution or platform (e.g., intelligent transport management platform, AI signal-control system, digital-twin platform, traffic controllers, RSUs), using structured selection and PoC validation to choose right |
| **Core tools** | Transport-tech selection seven-dimension decision matrix (Functional fit / Technical architecture / Regulatory & sovereignty compliance / Critical-infrastructure protection / Vendor capability / Cost-performance / Implementation risk) + PoC five-step validation method |
| **Total duration** | 12–16 weeks (incl. 4–6 week PoC) |
| **Deliverables** | Requirements specification, RFP/RFI documents, vendor long list / short list, PoC evaluation report, vendor recommendation report |
| **Assessment team** | 1 solution architect + 1 business analyst + 1 procurement / commercial lead + 1 PM + 1–2 PoC test engineers |

---

## Phase 1: Requirements Definition (Weeks 1–2)

### 1.1 Functional Requirements Template

**Define functional requirements line by line using the template below. Tag each with M (Must) / S (Should) / C (Could) / W (Won't — this phase).**

| Req ID | Requirement name | Description | MoSCoW | Acceptance criteria | Linked scenario |
|--------|------------------|-------------|--------|---------------------|-----------------|
| FR-001 | Real-time flow data ingestion | System shall ingest multi-source flow data (loops, radar, video, GPS probes) with end-to-end latency ≤500 ms | M | ≥4 sources ingested, latency <500 ms | Traffic-state awareness |
| FR-002 | Automatic incident detection | System shall support video-AI detection of crashes, congestion, wrong-way, pedestrian intrusion, debris | M | Detection accuracy >90%, false-positive <15% | AI video event detection |
| FR-003 | Signal-timing recommendation | System shall auto-generate and recommend timing plans from real-time flow for engineer confirmation & push | S | Plan generated <30 s, one-click push | AI signal control |
| FR-004 | Open data API | System shall provide RESTful APIs for third parties to retrieve masked traffic data | S | API response <200 ms, with auth & rate-limit | Data openness & sharing |
| FR-005 | Digital-twin 3D visualization | System shall provide WebGL-based 3D digital twin, rendering >1000 intersections | C | >30 fps @1000 intersections | Digital-twin display |
| ... | ... | ... | ... | ... | ... |

### 1.2 Non-Functional Requirements Template

| Req ID | Category | Description | Quantified metric | Priority |
|--------|----------|-------------|-------------------|----------|
| NFR-001 | Performance | Concurrent processing | >5000 video streams, >1000 intersections real-time compute | M |
| NFR-002 | Availability | System uptime | Core SLA >99.9% (annual downtime <8.76 h) | M |
| NFR-003 | Scalability | Horizontal scaling | Scale from 100 to 10000 intersections without re-architecture | M |
| NFR-004 | Security | Security accreditation | Meets ISO/IEC 27001 / NIST CSF accreditation (Level 3 equivalent) | M |
| NFR-005 | Regulatory & sovereignty | Local/regional compliance | Support regional data-residency, sovereign-cloud, open standards | M |
| NFR-006 | Data security | Data classification | Support core/important/general tiering, automated masking engine | M |
| NFR-007 | Maintainability | O&M friendliness | Unified monitoring, log center, automated alerting | S |
| NFR-008 | Compatibility | Legacy integration | Integrate mainstream signal systems (Siemens, Cubic, Thales, Kapsch) | M |
| NFR-009 | DR | Backup & recovery | RPO<15 min, RTO<2 h, active-active supported | S |
| NFR-010 | Internationalization | Multi-language | Not required for now | W |

### 1.3 RFP/RFI Structure Template

**RFI (Request for Information) structure — for the long-list stage:**

1. **Project background** (0.5 pg): org intro, purpose of this RFI
2. **Requirements overview** (1–2 pg): summary of key functional & non-functional requirements
3. **Vendor information requested** (30 questions, see 2.2)
4. **Response-format requirements** (0.5 pg): format, deadline, submission method
5. **Evaluation-process description** (0.5 pg): next steps (RFI → short list → RFP → PoC → final)
6. **Disclaimer**: RFI is not a procurement commitment

**RFP (Request for Proposal) structure — for the short-list stage:**

1. **Technical proposal instructions** (2 pg): overview, schedule, rules, open scoring criteria
2. **Technical requirements specification** (10–15 pg): generated from 1.1 and 1.2
3. **Commercial requirements** (2 pg): pricing template, payment terms, warranty, training
4. **Draft contract terms** (3–5 pg): SLA, IP, confidentiality, breach liability
5. **Scoring criteria** (1 pg): 70% technical + 30% commercial (with sub-weights)

### 1.4 Weight-Setting Workshop

**Participants:** Business + technical + procurement, 2–3 each

**Method:** Simplified AHP — pairwise comparison matrix

**Steps:**
1. List the 7 scoring dimensions (function / technology / sovereignty / CIP / vendor / cost / risk)
2. Each person fills a pairwise matrix ("how much more important is A than B": 1–9, 1=equal, 9=A far more important)
3. Aggregate matrices → geometric mean → consistency check (CR<0.1 passes)
4. Normalize to dimension weights

**Example weights (typical ITS platform project):**

| Dimension | Weight | Note |
|-----------|--------|------|
| Functional fit | 25% | Meeting business needs comes first |
| Technical-architecture modernity | 15% | Must support next 5 years |
| Regulatory & sovereignty compliance | 15% | Hard requirement for large projects; weight rising |
| Critical-infrastructure protection | 10% | Mandatory for CII orgs; optional otherwise |
| Vendor capability | 15% | Implementation & O&M as important as product quality |
| Cost-performance | 15% | Large projects not cheapest-only, but budget discipline is strict |
| Implementation risk | 5% | Penalty, not bonus |

---

## Phase 2: Market Scan & Long List (Weeks 3–4)

### 2.1 Vendor Research Sources

| Source | Best for | How to obtain | Reliability |
|--------|----------|---------------|-------------|
| Public procurement portals | Historical awards, prices, competitors | Public query (EU TED, US SAM.gov, state/provincial portals) | ★★★★★ |
| Industry research reports | Market share, trends, competitive landscape | Purchase / subscribe (Gartner, IDC, ABI Research) | ★★★★ |
| Gartner / IDC / Forrester | Global tech ratings, magic quadrants | Purchase / subscribe | ★★★★ |
| Industry expos / forums | Latest products, tech routes | Attend (ITS World Congress, Intertraffic, etc.) | ★★★★ |
| Vendor websites | Product intro, cases, whitepapers | Public browse | ★★★ |
| Peer referral / word-of-mouth | Real usage, hidden issues | Informal channels (LinkedIn, industry events) | ★★★★ (cross-verify) |
| Trial / PoC | Real product performance | Run with vendor | ★★★★★ |
| Social media / tech blogs | Developer ecosystem, activity | GitHub / Stack Overflow / professional forums | ★★★ |

### 2.2 RFI 30-Question Template

**Send a standard RFI questionnaire to each candidate vendor; 30 core questions below:**

**Company basics (Q1–5):**
1. Full legal name, HQ location, registered capital, founding year, ownership structure
2. Years in transport, cumulative deliveries, Top 3 comparable projects (client, value, year)
3. Total headcount, R&D share, size of transport technical team
4. Certifications: ISO 9001 / CMMI / ISO 27001 / ISO 20000?
5. Any major litigation, penalties, or significant project delays in last 3 years?

**Product & technology (Q6–15):**
6. Provide the product architecture diagram (compute / storage / middleware / application layers)
7. Development language & tech stack? Database choice?
8. Does it support sovereign / regional deployment? (Annotate CPU/OS/DB/middleware compatibility with regional requirements)
9. API openness? Full API docs and SDK?
10. Max concurrency? Per-intersection compute latency?
11. How is data security handled? ISO/IEC 27001 / NIST CSF accredited?
12. Multi-tenant / multi-tier deployment supported?
13. AI/ML capability? Which framework? In-house?
14. Version iteration cycle? Notable updates in the last year?
15. Technology roadmap for the next 3 years?

**Implementation & delivery (Q16–22):**
16. Typical time from contract to go-live for a comparable project?
17. How is the delivery team structured? PM experience requirements?
18. Custom development supported? Typical share of project?
19. Post-go-live O&M model? (on-site / remote / response time / SLA)
20. Training system? Courses and materials?
21. If vendor changed mid-project, how are knowledge transfer & data migration handled?
22. On-time delivery rate and customer satisfaction over the last 3 years?

**Commercial & partnership (Q23–30):**
23. Pricing model? (license / subscription / usage / custom) Public price list?
24. Typical 3-yr TCO (license + implementation + O&M + upgrade) range?
25. Willing to do PoC? How and under what conditions?
26. How is IP handled? Is source code for custom work delivered?
27. Renewal terms post-warranty? Lock-in risk?
28. Participation in standards bodies (ISO / IEEE / NTCIP / DATEX II / SAE)?
29. Specific capability or certification for critical-infrastructure protection (e.g., NIS2, IEC 62443)?
30. Provide 3 reference customers (contact name, title, phone/email)

### 2.3 Long-List Inclusion Criteria

**Minimum threshold (all Must conditions required):**

| Condition | Must standard |
|-----------|---------------|
| Industry experience | ≥3 comparable transport project deliveries |
| Technical architecture | Clear architecture, no obviously obsolete stack |
| Sovereignty compliance | At least partial regional compliance (CPU or OS or DB — at least one) |
| Company scale | >30 R&D staff or transport revenue >$3M/yr |
| Service capability | Local office / partner at project site (or committed) |
| Legal risk | No major litigation or penalties |
| PoC willingness | Willing in principle (terms negotiable later) |

**Long-list outcome:**
> Typically select 10–15 of 30–50 vendors into the long list

---

## Phase 3: Short List & Solution Evaluation (Weeks 5–6)

### 3.1 Solution Scorecard

**Select 3–5 from the long list into the short list, based on RFI replies and proposal scores.**

| Dimension | Weight | Vendor A | Vendor B | Vendor C | Vendor D | Vendor E |
|-----------|--------|---------|---------|---------|---------|---------|
| Functional fit (5-pt sub-scale) | 25% | score | score | score | score | score |
| Technical architecture | 15% | score | score | score | score | score |
| Regulatory & sovereignty | 15% | score | score | score | score | score |
| Critical-infra protection | 10% | score | score | score | score | score |
| Vendor capability | 15% | score | score | score | score | score |
| Cost-performance | 15% | score | score | score | score | score |
| Implementation risk | 5% | score | score | score | score | score |
| **Weighted total** | **100%** | **X.XX** | **X.XX** | **X.XX** | **X.XX** | **X.XX** |
| **Rank** | | | | | | |
| **Short-list?** | | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |

### 3.2 Vendor Demo Evaluation Sheet

**Demo Day scorecard:**

| Item | Weight | Score (1–5) | Notes |
|------|--------|-------------|-------|
| Demo preparedness | 5% | | Met scenario brief? Environment ready? Any tech failure? |
| Core-function demo | 30% | | Covered how many Must FRs? Real & usable (not PPT)? |
| Technical presentation | 20% | | Architecture clear? Answers professional? |
| Business understanding | 15% | | Transport-domain grasp? Business, not just tech, language? |
| User experience | 10% | | Smooth flow? Friendly UI? Ease of learning? |
| Team quality | 10% | | PM & architect professionalism, communication, adaptability |
| Openness & ecosystem | 5% | | API openness, ISV ecosystem, community activity |
| Pricing transparency | 5% | | Clear quote? Hidden fees? |

**Demo Day organization guide:**
- Allocate 2 hours per vendor (15 min setup + 90 min demo + 15 min Q&A)
- Send demo scenario list 2 weeks ahead (Top 5 core scenarios to demo)
- No PPT + screen-recording — must be a live demo of the real system
- All evaluators score independently after the demo, no on-site discussion
- If possible, record demos for later review

### 3.3 Customer-Reference Interview Script

**Phone / video interview the recommended reference customers; script below:**

| # | Question | Focus |
|---|----------|-------|
| 1 | When did you buy what product from vendor X? | Confirm project is real |
| 2 | What was the project scale and scope? | Comparability to your need |
| 3 | Time from kickoff to go-live? Any delay? | Delivery capability |
| 4 | Did core functions meet expectations post-go-live? | Real product performance |
| 5 | How stable? Any major outages? | Product quality |
| 6 | Satisfaction with support & after-sales? | Service capability |
| 7 | Biggest challenge working with the vendor? | Hidden issues |
| 8 | If you chose again, would you pick them? Why? | Overall satisfaction |
| 9 | Anything you wish you'd known upfront but didn't? | "Pitfall" mining |
| 10 | Any other advice for us? | Open close |

**Reference-interview notes:**
- Interview ≥2 customers, ≥2 people each (IT head + business head)
- Vendors may only recommend "friendly" customers — proactively find non-recommended ones via industry circles for cross-verification
- If a vendor cannot provide 3 reachable references → red flag, lower trust
- Archive the reference-interview report as part of the evaluation file

---

## Phase 4: PoC Design & Execution (Weeks 7–12)

### 4.1 PoC Scope Template

**PoC Scope Document (1-page A4):**

```
PoC name: [XX Intelligent Transport Management Platform — Zone Adaptive Signal Control PoC]
Objective: Validate whether XX platform's adaptive signal control meets requirements in a real
traffic environment (10 intersections in District X, City Y)

Participating vendors:
- Vendor A (short-list #1)
- Vendor B (short-list #2)
- Vendor C (short-list #3, candidate)

PoC period: 6 weeks (2026.08.01 – 2026.09.12)

Test scenarios (4 core):
1. Isolated-intersection adaptive signal control
2. Green-wave coordination of a 3-intersection arterial
3. Peak saturated-flow adaptive control
4. Signal emergency plan under special events (crash / work zone)

Test data:
- Real-time video per intersection (2–4 streams)
- Loop / radar flow (6 mo history + real-time)
- Controller status data
- Weather data

Test environment:
- Vendor-provided servers / cloud (not connected to production)
- Mirror / bypass data feed (no impact on live network)

Key success metrics:
| Metric | Target | Measurement |
|--------|--------|-------------|
| Travel-delay reduction | >10% | Probe-vehicle before/after |
| Avg stops reduction | >15% | Video-AI count |
| Compute latency | <200 ms | Timed feed-to-plan |
| Availability | >99% (during PoC) | Monitoring auto-log |
| Traffic-engineer satisfaction | >4.0/5.0 | Weekly survey |

PoC plan:
- Wk1: env deploy, data feed, base-function verification
- Wk2–3: scenarios 1–2
- Wk4–5: scenarios 3–4
- Wk6: effect evaluation, report

PoC budget: $XXK (travel, equipment rental, traffic-management coordination, etc.)
```

### 4.2 Test-Scenario Design Template

**Describe each test scenario with the template below:**

| Field | Content |
|-------|---------|
| Scenario ID | TC-01 |
| Scenario name | Isolated-intersection adaptive signal control |
| Business context | Intersection X at arterial/minor-road junction; pronounced AM/PM tidal flow; different weekend pattern |
| Test steps | 1. Ingest real-time flow (loop+video) → 2. Auto-generate timing from real-time flow → 3. Engineer reviews → 4. Controller executes new plan → 5. Run 7 days, collect effect data |
| Input data | Loop flow (1-min), video (1 stream/direction), signal state, time/date |
| Expected behavior | Re-evaluate timing every 15 min; auto-recommend new plan when flow changes >20% |
| Success criteria | Travel delay −>10%; peak-direction green extended, off-peak shortened |
| Failure criteria | Delay rises not falls; plan flips cause driver confusion (>3/hr) |
| Data collection | Probe data (1-wk baseline vs during PoC), timing logs, engineer rating |

### 4.3 PoC Evaluation Scorecard

**Score each participating vendor independently against the scorecard:**

| Dimension | Sub-item | Weight | Vendor A | Vendor B | Vendor C |
|-----------|----------|--------|---------|---------|---------|
| **Function implementation (35%)** | Scenario 1 pass rate | 10% | X% | X% | X% |
| | Scenario 2 pass rate | 10% | X% | X% | X% |
| | Scenario 3 pass rate | 10% | X% | X% | X% |
| | Scenario 4 pass rate | 5% | X% | X% | X% |
| **Performance (25%)** | Compute latency | 10% | X ms | X ms | X ms |
| | Availability | 10% | X% | X% | X% |
| | Concurrency | 5% | X streams | X streams | X streams |
| **Usability & experience (15%)** | Flow smoothness | 5% | score | score | score |
| | Alert / notice reasonableness | 5% | score | score | score |
| | Docs / help quality | 5% | score | score | score |
| **Integration & openness (15%)** | API ease | 5% | score | score | score |
| | Data import/export | 5% | score | score | score |
| | 3rd-party integration | 5% | score | score | score |
| **Teamwork (10%)** | Responsiveness | 4% | score | score | score |
| | Problem-solving | 3% | score | score | score |
| | Proactivity & professionalism | 3% | score | score | score |
| **Weighted total** | | **100%** | **X.XX** | **X.XX** | **X.XX** |
| **Rank** | | | | | |

### 4.4 PoC Logistics Checklist

**Hardware / environment:**
- [ ] Each vendor's servers / cloud ready on time
- [ ] Network bandwidth sufficient (test video + data volume)
- [ ] Production data-feed interface opened and tested
- [ ] Test intersections' traffic-impact assessment filed
- [ ] Test-environment access assigned (VPN / bastion host)

**People:**
- [ ] Each vendor's on-site engineers present
- [ ] Client full-time participants confirmed (traffic engineer / IT O&M)
- [ ] Third-party data-collection agency (if any) contracted
- [ ] Traffic-management / work-zone coordination (if needed) reported to authority

**Process:**
- [ ] PoC kickoff held; scope & schedule signed by all
- [ ] Daily standup cadence established (15 min: done / today / blockers / plan)
- [ ] Weekly progress review cadence established (sync with key stakeholders)
- [ ] Data-collection tools (probe / survey / monitoring) ready
- [ ] Rollback plan confirmed (what if PoC impacts live network)

**Legal / commercial:**
- [ ] NDA signed
- [ ] PoC cost allocation in writing (who bears what)
- [ ] PoC data ownership clarified (belongs to client)
- [ ] PoC failure implies no procurement commitment (in writing)

### 4.5 Common PoC Pitfalls & Avoidance

| # | Pitfall | Symptom | Avoidance |
|---|---------|---------|-----------|
| 1 | Scope creep | Vendor shows extras; client says "test that too" | Scope doc signed by both; any new need goes through formal change control |
| 2 | Vendor "special forces" | HQ R&D director on-site, 24-h code fixes — but the delivery team isn't that caliber | Require the delivery team (not pre-sales, not HQ R&D) to run PoC; commit delivery-team composition in proposal |
| 3 | Dumbbell effect | Functions A and B each demoed, but never A→B end-to-end | Scenario design must cover end-to-end flows, not isolated functions |
| 4 | Data cheating | Pretrained models, cached results, idealized data | Require client's real (masked) data, real-time compute (not offline batch), sufficient volume |
| 5 | Happy-path only | Only "all normal" tested; no anomalies/edge/stress | ≥30% of cases cover anomalies (delay / missing / anomalous / concurrency / power-loss recovery) |
| 6 | Bandwagon effect | Vendor A looks great, subconsciously scores B and C high too | Score each vendor independently; don't share scores until all PoCs done |
| 7 | No PoC budget | No PoC line in budget; execution constrained | Reserve PoC budget in RFP (recommend 2–5% of total) |
| 8 | PoC = free early delivery | Vendor turns PoC into real delivery, then "holds the system hostage" | PoC environment physically isolated from production; vendor must purge all data & code after PoC |

---

## Phase 5: Final Selection & Negotiation (Weeks 13–16)

### 5.1 Recommendation Report Template

**Standard vendor recommendation report structure:**

1. **Executive summary (1 pg)**
   - Recommended vendor & ranking
   - 2–3 key reasons for the decision

2. **Selection-process recap (1 pg)**
   - Timeline (RFI → short list → RFP → Demo Day → PoC → final)
   - Participants, evaluation method

3. **Per-vendor detail (3–4 pg each)**
   - Functional-fit analysis
   - PoC performance summary
   - Technical-architecture assessment
   - Sovereignty-compliance assessment
   - Commercial-condition analysis
   - Strengths & risks

4. **Comparison matrix (2 pg)**
   - Seven-dimension radar overlay
   - Phased TCO comparison
   - SWOT

5. **Recommendation (1 pg)**
   - First / second / not-recommended, with reasons
   - Suggested negotiation strategy & key terms

6. **Appendix**
   - PoC detailed scores
   - Reference-interview notes
   - RFI reply summary

### 5.2 Negotiation Strategy

**Seven-step negotiation prep:**

| Step | Content | Output |
|------|---------|--------|
| 1. BATNA analysis | If talks with #1 fail, who's #2? How much worse? | BATNA card |
| 2. Negotiation-zone analysis | Study the gap between vendor's "lowest acceptable" and "initial quote" | Zone estimate |
| 3. Term priority | List must-hold terms (source delivery, sovereignty cert) vs tradable (payment rhythm) | Term-priority matrix |
| 4. Price breakdown | Split total into license / implementation / training / O&M / upgrade; benchmark each | Price-breakdown sheet |
| 5. Competitive play | Appropriately let vendor know strong competitors exist (without disclosing scores); create FOMO | Competitive-posture comms |
| 6. Bundle vs split | Whether to bundle follow-on projects (better price) or split (lower lock-in) | Bundle/split strategy |
| 7. Negotiation script | Design rhythm: what first, who opens, when to reveal BATNA | Negotiation script |

**Key negotiation terms checklist:**

| Term | Suggested position | Flexibility |
|------|--------------------|-------------|
| IP (custom work) | Require source delivery + client ownership | Floor: irrevocable perpetual license to client |
| License model | Prefer perpetual (CapEx) over subscription (OpEx) | If subscription mandatory, lock 3–5 yr price + cap |
| Annual maintenance increase | Yr1 in project fee; later ≤15%/yr of contract | Accept 10–15% but price-protect to yr 5 |
| Source escrow | Require third-party source escrow (prevent unmaintainable if vendor bankrupt/acquired) | Strong client need, don't concede |
| SLA & penalty | Availability 99.9%+; outage penalty (suggest: 0.1% of contract per extra hour) | SLA tunable, but penalty mechanism mandatory |
| Lock-in clause | Ban hidden lock-in ("must use vendor's matching hardware/upgrade only") | Non-negotiable |
| Payment rhythm | Suggest 3:3:3:1 (sign / initial acceptance / final acceptance / warranty end); lower advance | Negotiable, but retention ≥10% |
| Key-person lock | Changing PM / architect needs client's written consent | Non-negotiable |

### 5.3 Contract Review Checklist

**24-item pre-signature review:**

**Commercial (8):**
- [ ] Total price matches negotiation; no hidden fees
- [ ] Payment terms & rhythm match negotiation
- [ ] Warranty & maintenance clear, incl. SLA & service catalog
- [ ] IP terms clear — focus: custom-source ownership
- [ ] Breach-liability terms clear and reciprocal
- [ ] Confidentiality covers both sides
- [ ] Dispute resolution (arbitration / litigation) & jurisdiction clear
- [ ] Force-majeure clause reasonable

**Technical (10):**
- [ ] Requirements spec attached, version & date noted
- [ ] Acceptance criteria & process clear (initial / final / warranty-end)
- [ ] Deliverables list complete (code / docs / training / O&M manual / test report)
- [ ] Source escrow clause included (or alternative)
- [ ] Performance metrics in contract (concurrency / latency / availability / data cap)
- [ ] Data-security & privacy terms comply with GDPR / data-protection law
- [ ] Sovereignty-compliance commitment included (esp. public / large projects)
- [ ] Third-party software/component license compliance warranted by vendor
- [ ] CIP special clauses (if applicable)
- [ ] Tech-support response time & escalation clear

**Project (6):**
- [ ] Implementation plan attached (WBS & key milestones)
- [ ] Staffing requirements (key persons, qualifications, change needs consent)
- [ ] Change-management process (esp. requirement-change review & pricing)
- [ ] Late-delivery penalty clause
- [ ] Training plan (count, headcount, method, materials)
- [ ] Knowledge-transfer plan (O&M manual, architecture docs, common-fault handling)

---

## Appendix: PoC Project Plan Template

| Week | Dates | Milestone | Task | Owner | Deliverable |
|------|-------|-----------|------|-------|-------------|
| W1 | 08.01–08.07 | PoC kickoff | Kickoff, env deploy, network, data feed | All | Env-ready confirmation |
| W2 | 08.08–08.14 | TC-01 start | Isolated-intersection signal control | Vendor + client engineer | Scenario-1 report (draft) |
| W3 | 08.15–08.21 | TC-01 done + TC-02 start | Final scenario-1 + scenario-2 start | Vendor | Scenario-1 final |
| W4 | 08.22–08.28 | TC-02 done + TC-03 start | Green-wave + peak stress | Vendor | Scenario-2 final |
| W5 | 08.29–09.04 | TC-03 done + TC-04 start | Event emergency scenario | Vendor | Scenario-3 final |
| W6 | 09.05–09.11 | TC-04 done + eval | Final test, effect eval, archive | PoC eval team | PoC comprehensive evaluation report |
| W6+1 | 09.12 | Teardown | Vendor removes env, returns data | Vendor | Teardown confirmation |

**Daily standup agenda (15 min):**
1. What did you finish yesterday? (each vendor, one sentence)
2. What will you do today?
3. Any blockers?
4. Who needs to help with what?

**Weekly progress check:**
- Every Friday PM, each vendor submits weekly report + next-week plan
- PoC eval team checks parity of progress (prevent one vendor "rushing" more tests, unfair)
- Log any deviation from PoC scope

---

> **Legal notice**: This playbook is protected under applicable copyright law. Without the author's written authorization, no commercial use is permitted (including resale, bundling, commercial training, or SaaS-ification).
> **Disclaimer**: The methodology herein is for learning reference only and does not constitute professional advice of any kind. Technology-selection and procurement decisions should rest on sufficient technical validation, legal review, and commercial negotiation.
> **Author**: yinjianheng (Yin Jianheng) | yinjianheng@foxmail.com | WeChat: YJH-yinjianheng
