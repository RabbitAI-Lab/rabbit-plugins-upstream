# Transport Digital Maturity Assessment Playbook

## Playbook Overview

| Item | Description |
|------|-------------|
| **Applicable scenarios** | A comprehensive digital maturity diagnosis for transport authorities and operators (transport departments / highway operators / port authorities / airport operators / metro & rail operators, etc.) |
| **Assessment model** | T-DMM Transport Digital Maturity Model — the five-dimension model (Infrastructure Capability / Data Intelligence / Business Application / Organization & Governance / Security Assurance) |
| **Maturity levels** | L1 Initial → L2 Departmental → L3 Organizational → L4 Quantified → L5 Leading |
| **Total duration** | 5–6 weeks (compressible to 3 weeks) |
| **Deliverables** | Maturity assessment report, gap analysis, benchmarking report, 3-year roadmap recommendations |
| **Assessment team** | 1 Project Manager + 2–3 assessment advisors + 1 data analyst |

---

## Phase 1: Preparation (Week 1)

### 1.1 Assemble the Assessment Team

**Roles and responsibilities:**

| Role | Headcount | Responsibilities | Required competencies |
|------|-----------|------------------|----------------------|
| Project Manager (PM) | 1 | Overall coordination, client communication, schedule management, deliverable presentation | Transport-sector project experience, client management |
| Lead Assessment Advisor | 1 | Assessment framework design, scoring facilitation, lead author of report | 5+ years in transport digitalization, fluent in T-DMM |
| Assessment Advisor | 1–2 | Document review, interview execution, data collection | Transport IT or consulting background |
| Data Analyst | 1 | Data processing, score computation, charting | Data analytics and visualization skills |
| Domain Expert (as needed) | 1–2 | Deep diagnosis of specific modes (e.g., ports, rail) | 10+ years in the sub-domain |

**✅ Team readiness checklist:**
- [ ] PM confirms the project charter (scope, deliverables, schedule, budget)
- [ ] All roles sign a Non-Disclosure Agreement (NDA)
- [ ] Create a project communication channel (recommended: Microsoft Teams / Slack)
- [ ] Set up a shared document library (recommended: SharePoint / Google Workspace / Confluence) with access controls
- [ ] Prepare the assessment toolkit (see 1.3)

### 1.2 Collect Documentation

**Formally send the *Documentation Collection Checklist* to the client, requesting delivery within Week 1:**

**Category A: Strategy & organization documents (mandatory)**
- [ ] The authority's current strategic / medium-to-long-term plan
- [ ] Annual work reports (last 3 years)
- [ ] Dedicated IT / digitalization plan
- [ ] Organization chart (including the positioning of the IT/digital function)
- [ ] Compilation of IT governance policies
- [ ] IT budget and actual spend for the past 3 years

**Category B: Systems & technical documents (mandatory)**
- [ ] Information system asset catalog / equipment register
- [ ] Network topology diagram, data-center architecture diagram
- [ ] List of core business systems (name, vendor, version, deployment year, number of users)
- [ ] Data exchange / sharing platform technical documentation (if any)
- [ ] Cybersecurity assessment / audit report (if any)
- [ ] Acceptance documentation for IT projects over the past 2 years

**Category C: Business & performance documents (optional)**
- [ ] Transport operations annual / quarterly report
- [ ] KPI performance framework documentation
- [ ] Recent IT inspection / operations & maintenance (O&M) records
- [ ] IT-related complaints / suggestions records
- [ ] Third-party assessment / audit reports (if any)
- [ ] Relevant public-sector performance assessment materials

**📋 Documentation tracking template:**

| # | Document name | Category | Owner | Submission status | Date | Completeness | Notes |
|---|---------------|----------|-------|-------------------|------|--------------|-------|
| 1 | XX Plan | A | Director Zhang | Submitted | Jul 10 | Complete | |
| 2 | XX Topology | B | Engineer Wang | Pending | - | - | Reminded twice; expected Jul 12 |

### 1.3 Configure the Assessment Toolkit

**Toolkit inventory:**

| Tool | Purpose | Recommended option | Preparation requirement |
|------|---------|--------------------|-------------------------|
| Maturity scoring sheet | Five-dimension scoring | Excel / Google Sheets (with auto-calculation formulas) | Includes 5 dimensions, 25 sub-dimensions, L1–L5 definitions |
| Interview template | Structured interviews | Word / Confluence | 30+ standardized questions with space for notes |
| System inventory sheet | IT asset census | Excel (dropdowns + conditional formatting) | Classified by business chain, technology stack annotated |
| Data quality checklist | Data assessment | Excel (with scoring formulas) | Covers completeness / accuracy / consistency / timeliness / uniqueness |
| Benchmarking radar chart | Visualization | PowerPoint / Google Slides | Pre-loaded with industry benchmark data |
| Project calendar | Schedule management | Excel Gantt / Teams calendar | Key milestones and client participation nodes flagged |

**Scoring-sheet structure example (T-DMM five-dimension model):**

| Dimension | Weight | Sub-dimension 1 | Sub-dimension 2 | Sub-dimension 3 | Sub-dimension 4 | Sub-dimension 5 |
|-----------|--------|-----------------|-----------------|-----------------|-----------------|-----------------|
| Infrastructure Capability | 25% | Sensor coverage | Communications network coverage | Cloud computing resources | Edge computing capability | Endpoint intelligence |
| Data Intelligence | 25% | Data collection completeness | Data governance maturity | Data sharing capability | Data analytics capability | AI application maturity |
| Business Application | 25% | Core business coverage | System integration | User experience | Process digitalization | Decision-support capability |
| Organization & Governance | 15% | Digital strategy | Organization & talent | Process & policy | Funding assurance | Innovation culture |
| Security Assurance | 10% | Cybersecurity | Data security | Physical security | Business continuity | Compliance management |

### 1.4 Kickoff Meeting with the Client

**Kickoff agenda (90 minutes):**

| Time | Segment | Content | Presenter |
|------|---------|---------|-----------|
| 0–15 min | Introductions | Assessment team and client core personnel introductions | PM |
| 15–25 min | Project briefing | Assessment objectives, method, duration, deliverables | Lead Advisor |
| 25–45 min | Work arrangement | Detailed schedule, required cooperation, interview list, supplementary materials | PM |
| 45–60 min | Executive remarks | Client decision-maker's expectations and requirements | Client decision-maker |
| 60–75 min | Q&A | Questions and suggestions from client departments | All |
| 75–90 min | Wrap-up | Confirm next-step actions and owners | PM |

**Pre-kickoff preparation:**
- [ ] Send meeting invite and agenda 3 days in advance
- [ ] Collect the client participants' names and titles in advance
- [ ] Prepare the deck (15–20 slides recommended): overview, methodology, team, success cases
- [ ] Prepare a signed one-page A4 *Statement of Cooperation*
- [ ] Test projection and the online meeting link

---

## Phase 2: Data Collection (Weeks 2–3)

### 2.1 Interview Guide

#### 2.1.1 Interviewee Priority and Recommended Duration

| Priority | Interviewee | Recommended # | Duration | Format |
|----------|-------------|---------------|----------|--------|
| P0 Must | Executive sponsor / GM accountable for digitalization | 1 | 60 min | 1-on-1 |
| P0 Must | Head of IT / digital function | 1 | 90 min | 1-on-1 |
| P0 Must | Heads of core business units (control center / traffic ops / maintenance / operations) | 3–5 | 45 min each | 1-on-1 |
| P1 Should | Front-line IT staff / system administrators | 3–5 | 30 min each | 1-on-1 |
| P1 Should | Head of finance | 1 | 30 min | 1-on-1 |
| P2 Optional | Front-line enforcement / operators / duty officers | 5–8 | 20 min each | Focus group |
| P2 Optional | Heads of planning / legal & regulatory | 1–2 | 30 min each | 1-on-1 |

#### 2.1.2 Role-based Interview Question Banks

> **Below is a 30+ question bank; select by respondent role. Keep each interview to 45–60 minutes with 10–12 core questions.**

---

**A. Questions for the digitalization executive sponsor (strategic layer)**

| # | Question | Dimension assessed |
|---|----------|--------------------|
| 1 | Please describe the overall objectives of the authority's strategic plan for IT/digitalization and current progress. | Strategic alignment |
| 2 | What do you see as the main driver of digitalization here? (top-down mandate / business pressure / proactive innovation) | Change motivation |
| 3 | What was the largest IT investment over the past 3 years, and how is its impact measured? | Investment decision |
| 4 | Is the IT function positioned as a service unit or a strategic unit? Is the budget adequate? | Organization & governance |
| 5 | What is the biggest current weakness in IT? (technology / talent / data / funding / operating model) | Pain-point identification |
| 6 | What are your expectations for digital transformation over the next 3 years? (list the 3 most important goals) | Goal expectation |
| 7 | Is cross-department data sharing smooth? What resistance have you encountered? | Collaborative governance |
| 8 | What is your stance on AI / big-data technologies in transport scenarios? Any willingness to pilot? | Innovation appetite |
| 9 | What share of the total budget goes to IT, and what is the trend year over year? | Funding assurance |
| 10 | What IT/digitalization KPIs does the supervising authority use to assess you? | External drivers |

---

**B. Questions for the head of IT / digital function (management layer)**

| # | Question | Dimension assessed |
|---|----------|--------------------|
| 1 | Please sketch the current overall IT architecture, labeling core systems and data flows. | Technical architecture |
| 2 | Server / storage deployment model? (on-prem / colocation / industry cloud / public cloud) | Infrastructure |
| 3 | Is there a unified data center / data platform? What sources feed it? | Data capability |
| 4 | Usage frequency of core business systems? What pain points do front-line staff report? | System application |
| 5 | How well are systems interconnected? How many interfaces, and are they standardized? | Integration |
| 6 | Size and skill mix of the IT O&M team? (network / systems / development / data / security) | Talent |
| 7 | What cybersecurity measures are in place? Any certification (e.g., ISO/IEC 27001)? At what level? | Security assurance |
| 8 | Is there a CI/CD or DevOps pipeline? How frequently are systems iterated? | Development capability |
| 9 | How dependent are you on vendors? Do you hold source code / in-house O&M capability for core systems? | Technology sovereignty |
| 10 | What was the largest IT incident in the past 3 years, and how was it handled? | Resilience |

---

**C. Questions for heads of core business units (business layer)**

| # | Question | Dimension assessed |
|---|----------|--------------------|
| 1 | Which information systems do you use daily? Do they meet business needs? | Business coverage |
| 2 | What is the most time-consuming manual / repetitive work? Would you like it automated? | Efficiency pain point |
| 3 | Can you get real-time data when making decisions? How accurate is it? | Data support |
| 4 | Is data exchange with other departments smooth? Any "data silos"? | Data sharing |
| 5 | How receptive are you to new systems / processes? What training support do you want? | Change readiness |
| 6 | If you had an "intelligent transport management platform," what would you most want it to solve? | Business need |
| 7 | During emergencies, can the existing IT systems provide effective support? | Emergency support |

---

**D. Questions for front-line IT staff (execution layer)**

| # | Question | Dimension assessed |
|---|----------|--------------------|
| 1 | What is the most time-consuming part of daily O&M? Is it automated yet? | O&M efficiency |
| 2 | Bug-fix cycle? Are you satisfied with vendor response times? | Service quality |
| 3 | Assessment of the current tech stack (database / middleware / frontend framework) | Technical debt |
| 4 | Is there system documentation / a knowledge base? How long for a new hire to ramp up? | Knowledge management |
| 5 | Are training opportunities and learning resources sufficient? | Talent development |

### 2.2 System Inventory Template

**Register each system against the following template:**

| Field | Description | Example |
|-------|-------------|---------|
| System name | Official name | Traffic Signal Control System |
| Business chain | Traffic control / tolling / mobility service / safety supervision / asset management / logistics / integrated | Traffic signal control |
| Launch year | First deployment | 2019 |
| Last upgrade | Version / date | V3.2 / 2024.03 |
| Vendor | Original manufacturer | Siemens Mobility |
| Vendor contact | Commercial / technical support | Manager Zhang, +1-xxx |
| Deployment | On-prem / cloud / hybrid | On-prem |
| Users | DAU / MAU | 50+ |
| Key dependencies | Upstream systems relied upon | Enforcement camera data, inductive-loop data |
| Data output | Data exposed externally | Signal-timing plans, flow statistics |
| Interface protocol | API / SDK / file / database | REST API + MQTT |
| Source-code control | Full / partial / none | None |
| Security classification | Level 1 / 2 / 3 / 4 | Level 2 |
| Annual O&M cost | USD | ~$50K |
| User satisfaction | 1–5 | 3 |
| Known pain points | Main issues | Suboptimal coordination algorithm; product EOL |

### 2.3 Document Review Checklist

**Strategy & planning documents:**
- [ ] Are digitalization objectives clear and quantifiable?
- [ ] Does it cover the progression IT → digital → intelligent → smart?
- [ ] Does it benchmark against industry leaders or recognized standards?
- [ ] Is there a clear budget and resource-assurance plan?
- [ ] Is there an evaluation and performance framework?

**Technical architecture documents:**
- [ ] Is there a complete, up-to-date IT architecture diagram?
- [ ] Does it include DR / backup / active-active design?
- [ ] Does it follow open standards or mainstream technology routes?
- [ ] Is the security system aligned with ISO/IEC 27001 / NIS2 / critical-infrastructure protection?
- [ ] Is there a managed register of technical debt (obsolete components / EOL products)?

**Project management documents:**
- [ ] Are project initiation / acceptance materials complete for IT projects?
- [ ] Is there a clear project management process?
- [ ] Do acceptance criteria include quantified KPIs?
- [ ] Are there O&M handover and knowledge-transfer records?

**Data management documents:**
- [ ] Is there a data dictionary or metadata management?
- [ ] Is there a data-quality management policy?
- [ ] Is data classification & grading defined (core / important / general)?
- [ ] Does data sharing comply with data-protection regulations (e.g., GDPR)?

---

## Phase 3: Assessment Workshop (Week 4, Day 1, full day)

### 3.1 Workshop Design

**Participants:** Full assessment team + client core stakeholders (8–15 recommended)

**Ground rules:**
1. Phones on silent; 90-minute breaks between sessions
2. Each speaker limited to 3 minutes; facilitator intervenes if exceeded
3. Chatham House Rule — views may be cited without attribution
4. Scoring by anonymous vote (electronic clickers or Microsoft Forms)

**Workshop agenda (8 hours):**

| Time | Segment | Duration | Content | Method |
|------|---------|----------|---------|--------|
| 09:00–09:30 | Opening | 30 min | Re-state objectives, rules, introduce framework | Facilitator briefing |
| 09:30–10:30 | Findings presentation | 60 min | Team presents core findings from document review & interviews | Deck + Q&A |
| 10:30–10:45 | Break | 15 min | | |
| 10:45–12:00 | Dimension 1–2 scoring | 75 min | Infrastructure Capability + Data Intelligence | Per-sub-dimension discussion → anonymous scoring |
| 12:00–13:30 | Lunch | 90 min | | |
| 13:30–14:45 | Dimension 3 scoring | 75 min | Business Application | Per-sub-dimension discussion → anonymous scoring |
| 14:45–15:00 | Break | 15 min | | |
| 15:00–16:15 | Dimension 4–5 scoring | 75 min | Organization & Governance + Security Assurance | Per-sub-dimension discussion → anonymous scoring |
| 16:15–16:30 | Break | 15 min | | |
| 16:30–17:00 | Consensus calibration | 30 min | Re-discuss and adjust dimensions with large disagreement | Breakout + plenary consensus |
| 17:00–17:30 | Wrap-up | 30 min | First look at the five-star radar chart, next steps | Facilitator summary |

### 3.2 Scoring Meeting Design

**Scoring flow (each sub-dimension ~8–10 min):**

1. **Evidence statement (2 min):** Advisor lists objective evidence for the sub-dimension (document citations, interview excerpts)
2. **Client supplement (2 min):** Client adds missing info or corrects misunderstandings
3. **Independent scoring (2 min):** Each person anonymously picks a level 1–5 (Microsoft Forms / Teams poll / paper sticky notes)
4. **Reveal (1 min):** Show the score distribution (mean, variance, mode)
5. **Brief discussion (1–2 min):** If clear divergence (variance > 1.0), invite extreme-score holders to state rationale

**T-DMM scoring scale (per sub-dimension):**

| Level | Name | Criteria | Typical characteristics |
|-------|------|----------|-------------------------|
| 1 | Initial | No systematic management; depends on individuals | Manual operations, no docs, no policies |
| 2 | Departmental | Localized digitalization within a single department | Systems exist but siloed, stovepiped |
| 3 | Organizational | Cross-department integration, standardized coverage | Unified platform, data sharing, sound policies |
| 4 | Quantified | Data-driven decisions, continuous quantified optimization | KPI system, automated data collection, AI-assisted |
| 5 | Leading | Industry benchmark, enables others externally | Innovation leader, industry output, best practice |

**Scoring-bias checklist (to prevent scoring skew):**

| Bias type | Symptom | Mitigation |
|-----------|---------|------------|
| Halo effect | High scores everywhere because satisfied with one area | Facilitator stresses "this dimension only, don't relate to others" |
| Recency effect | Low scores everywhere because of a recent incident | Remind to consider the overall 1–2 year picture, not over-react to a single event |
| Leniency bias | Everyone scores 4–5 ("face saving") | Clarify L5 — only world-class / national benchmarks reach 5 |
| Severity bias | Everyone scores 1–2 ("IT has no value") | L1 = fully manual; check whether there truly are no systems |
| Central tendency | Everyone scores 3 ("neither good nor bad") | Require at least 2 pieces of evidence for L2 or L4 before scoring |
| Bandwagon effect | First speaker sways the whole room | Anonymous vote first, then discuss — avoid "echoing the boss" |

### 3.3 Consensus-Building Techniques

**Three-step method for handling disagreement:**

1. **Listen & understand (2 min):** Each of the two opposing sides states rationale for 1 minute, no interruption
2. **Find the anchor (3 min):** Facilitator guides both sides to shared understanding of "L2 vs L3" — they likely agree on "systems exist but not integrated," disagreeing only on whether that counts against a sub-dimension
3. **Compromise & record (2 min):** Take the median, but record the disagreement reason and analysis basis in the report notes

**Common scoring disputes and resolutions:**

| Dispute | Typical scenario | Resolution |
|---------|------------------|------------|
| "We have huge data volume, why only 3 for data capability?" | Massive data but weak analysis & application | Emphasize T-DMM assesses the full "data → insight → decision" chain, not just collection volume |
| "We deployed a major-vendor platform, surely L4?" | Advanced platform purchased but low usage | Ask: "What is the DAU? What % of decisions use platform data?" If insufficient, still L2–L3 |
| "We have a security certificate" | Certified but many known vulnerabilities unpatched | Separate "compliance" from "security" — certificate = compliance = at least L2, but patch rate reflects actual level |
| "AI is not a transport necessity" | Dismisses AI applications | AI signal control, AI maintenance, AI scheduling have mature deployments; show cases and ROI |
| "We're about the same as City X, they're L4 so we should be L4" | Peer comparison | No horizontal comparison; assess only this organization's five dimensions objectively. Benchmarking is a later step |

---

## Phase 4: Analysis & Report (Rest of Week 4)

### 4.1 Score Computation

**Computation steps:**
1. Take each sub-dimension's workshop consensus score (1–5)
2. Arithmetic mean of sub-dimensions = dimension score (1–5)
3. Dimension score × dimension weight = weighted dimension score
4. Sum of five weighted scores = total maturity index (max 5.0)

**Example computation (auto-completed by Excel formula):**

| Dimension | Weight | Sub-dimension mean | Dimension score | Weighted score |
|-----------|--------|--------------------|-----------------|----------------|
| Infrastructure Capability | 25% | (3+2+4+3+2)/5 | 2.8 | 0.70 |
| Data Intelligence | 25% | (2+2+1+3+1)/5 | 1.8 | 0.45 |
| Business Application | 25% | (3+4+3+2+3)/5 | 3.0 | 0.75 |
| Organization & Governance | 15% | (3+2+3+4+2)/5 | 2.8 | 0.42 |
| Security Assurance | 10% | (4+3+3+3+3)/5 | 3.2 | 0.32 |
| **Total maturity index** | | | | **2.64** |

### 4.2 Gap Analysis

**Gap-analysis matrix:**

| Dimension | Current score | Target level | Gap | Key gap description | Priority |
|-----------|---------------|--------------|-----|---------------------|----------|
| Infrastructure Capability | 2.8 | 3.5 | -0.7 | Insufficient sensor coverage; edge computing not yet deployed | High |
| Data Intelligence | 1.8 | 3.0 | -1.2 | Severe data silos; no unified data platform; no AI applications | Highest |
| Business Application | 3.0 | 3.5 | -0.5 | Core systems covered but integration insufficient | Medium |
| Organization & Governance | 2.8 | 3.5 | -0.7 | Digital strategy unclear; talent pipeline insufficient | High |
| Security Assurance | 3.2 | 4.0 | -0.8 | Critical-infrastructure protection needs uplift; data classification pending | Medium |

### 4.3 Benchmarking Analysis

**Recommended benchmarking dimensions (select 3–5 comparable peers):**

| Benchmark | Rationale | Data source |
|-----------|-----------|-------------|
| Average of peer cities / authorities globally | Understand relative position among peers | Industry whitepapers / public reports |
| Leading in-region authority (e.g., a top provincial agency) | Set a near-term catch-up target | Public cases + web research |
| National leader (e.g., a top metropolitan transport authority) | Set a long-term target | Public coverage + industry conferences |
| International leader (e.g., Singapore LTA) | Set a world-class vision | English sources + academic literature |

### 4.4 Report Authoring

**Standard T-DMM maturity assessment report structure:**

1. **Executive summary (2 pages)**
   - Total maturity index and five-dimension radar chart
   - Top 5 key findings
   - Top 5 priority recommendations

2. **Assessment overview (1 page)**
   - Scope, method, timing, team

3. **Detailed five-dimension assessment (3–5 pages per dimension)**
   - Dimension score and industry benchmark
   - Sub-dimension detailed analysis (each: evidence → score → analysis)
   - Strengths and weaknesses

4. **Gap analysis (2–3 pages)**
   - Ideal vs. reality gap matrix
   - Root-cause analysis of gaps

5. **Benchmark comparison (2–3 pages)**
   - Multi-benchmark radar overlay
   - Adoptable best practices

6. **Recommendations & roadmap (3–5 pages)**
   - Near / mid / long-term actions (by priority)
   - Key milestones and timing
   - Investment estimate summary

7. **Appendix**
   - Interview list
   - System inventory
   - Detailed scores
   - Benchmark data sources

**Report authoring tips:**
- Every finding must pair "evidence + impact + recommendation"
- Lead with radar / bar / heat maps; compress pure text
- Keep the body to 30–40 pages; detail in appendix
- Annotate technical terms on first use
- Target readers: executives (care about conclusions & recommendations) + the CIO / IT director (care about detailed analysis & actions)

---

## Phase 5: Presentation & Roadmap (Week 5)

### 5.1 Executive Presentation Script

**Presentation structure (60 min recommended, incl. discussion):**

| Time | Segment | Key points | Notes |
|------|---------|------------|-------|
| 0–5 min | Opening | Thank for cooperation, re-state objectives | Set a positive tone; don't open with "big problems" |
| 5–10 min | Methodology intro | T-DMM model, 5-level definition | One chart explains it |
| 10–15 min | Overall score | Radar chart, index, industry benchmark | **Show the overview before the deep dive** |
| 15–35 min | Five-dimension detail | 3 min per dimension: score + top finding + top recommendation | At least one positive finding per dimension |
| 35–45 min | Benchmark comparison | Radar overlay, key gaps | Instill "stand still and fall behind" awareness |
| 45–50 min | Recommended roadmap | Near/mid/long-term actions, investment frame | Actionable, timed, budgeted at order-of-magnitude |
| 50–60 min | Q&A | Address decision-maker concerns | Pre-prepare 5–10 common Q&A responses |

**10 executive-presentation techniques:**
1. Set the tone: "This assessment found your organization is already industry-leading in XX, with clear headroom in YY"
2. Use the client's strategic language: "highly aligned with the XX objective in your strategic plan"
3. Pair every "problem" with 2 examples of "what's already done well"
4. Number-driven: quantify over qualify; compare rather than isolate
5. Benchmarking is not "compare who's worse/better" — it's to find the gap; the gap is the direction
6. Where budget is sensitive, talk value before investment
7. Prepare an "if the decision-maker remembers one thing" version — a 3-minute elevator pitch
8. Recommendations must have the four elements: who / what / how long / how much
9. Avoid tech jargon; use business language (even with technical decision-makers)
10. Proactively offer at the end: "We can help drive the next-phase project initiation and investment review"

### 5.2 Define Next Steps

**Standard post-presentation actions:**

| Time | Action | Owner | Output |
|------|--------|-------|--------|
| Within 3 days | Revise report per feedback | Assessment PM | Final PDF report |
| Within 1 week | Submit *Digital Transformation Recommendation Paper* | Lead Advisor | 10–15 page paper (next steps matter more than the assessment itself) |
| Within 2 weeks | Assist client with internal project-initiation application | Assessment PM + client liaison | Draft project-initiation request |
| Within 1 month | Follow-up: adoption of recommendations and further support needs | Assessment PM | Follow-up notes + second-engagement intent |

**Typical "assessment is not the end" follow-on services:**
- Deep planning: from "assessment + recommendations" to "3-year digital transformation master plan"
- Technology selection: from "know what to build" to "which vendor to choose"
- AI scenario deep-dive: from "want some AI" to "which scenario to pilot first, and how to compute ROI"
- Data governance: from "data is poor" to "establish a data-governance committee and standard system"
- Pilot verification: from "should do it" to "a 3-month quick-win PoC"

---

## Appendix: Common Pitfalls for First-Time Assessors & Mitigations

### Top 10 Pitfalls

| # | Pitfall | Symptom | Mitigation |
|---|---------|---------|------------|
| 1 | Over-reliance on documents | Score only from documents, ignore reality | Triangulate: documents + interviews + live system demo |
| 2 | Single-source interviews | Only interview executives, miss front-line truth | At least 30% of interviews at the front line |
| 3 | Score inflation | Give L4/L5 "to keep the client happy" | Hold the L5 bar — only benchmarks earn 5. A first assessment averaging 2.0–3.0 is normal |
| 4 | Vague recommendations | "Strengthen data governance" / "improve AI" | Every recommendation includes: who / what / how long / how much / how to measure success |
| 5 | Ignore change readiness | Perfect plan, but no thought to whether the org can absorb it | At least half a page on change-management assessment |
| 6 | Try to cover everything | Scope too broad, depth insufficient | Focus on client's Top 3 pain points; light-touch the rest |
| 7 | No quantitative baseline | All "fair" / "average" / "to be improved" | Quantify where possible (%, ranking, count) |
| 8 | Ignore security dimension | Focus only on business & infrastructure; security = "certified" | Critical-infrastructure + data-security + personal-data assessment deserves at least one chapter |
| 9 | Underestimate governance complexity | Recommend cross-department consolidation without considering departmental interests | Understand the organizational roots of "data barriers"; reflect coordination paths in recommendations |
| 10 | Draggy report | 50+ pages, dense jargon, executives won't finish | Executive summary ≤ 2 pages; core report ≤ 40 pages |

### Characteristics of a Successful Assessment

- [ ] The main decision-maker says: "We knew these problems, but this is the first time they've been laid out so systematically"
- [ ] After delivery, the client proactively invites the next phase
- [ ] At least 2–3 Quick Wins "deployable within 3 months with visible results"
- [ ] The five-dimension scores withstand internal cross-validation (all departments agree)
- [ ] The output can be used by the client for upward reporting and budget justification

---

## Appendix: Assessment Toolkit Templates

### Template A: T-DMM Maturity Scorecard (Excel / Google Sheets)

> **Note: below is a reference structure for paper / spreadsheet. In practice build an Excel / Google Sheets version with auto-calculation formulas.**

**L1–L5 anchor descriptions:**

| Dimension | Sub-dimension | L1 Initial | L2 Departmental | L3 Organizational | L4 Quantified | L5 Leading |
|-----------|---------------|------------|-----------------|-------------------|---------------|------------|
| Infrastructure Capability | Sensor coverage | <30% of key corridors sensed | 30–60% sensed, partially shared | 60–90% sensed, unified mgmt | >90% sensed, active monitoring | Full-modal sensor fusion + predictive |
| Infrastructure Capability | Communications coverage | Office network mainly | Private business network at key nodes | Unified backbone + access | 5G + fiber dual-redundant | 5G + V2X + satellite ubiquitous |
| ... | ... | ... | ... | ... | ... | ... |

### Template B: Interview Plan Template

| Date | Time | Interviewee | Title | Role category | Question-bank version | Interviewer | Recorder | Location | Notes |
|------|------|------------|-------|---------------|----------------------|-------------|----------|----------|-------|
| Jul 20 | 09:00 | Deputy Director Zhang | Exec sponsor for digitalization | Strategic | Version A (exec) | Advisor Li | Assistant Wang | 3F meeting room | Brief sent |

### Template C: Assessment Log (fill before end of day)

| Date | Completed today | Key findings | Obstacles | Client cooperation needed | Tomorrow's plan |
|------|-----------------|--------------|-----------|---------------------------|-----------------|
| Jul 20 | 3 interviews done | Only 2 staff support all systems | One dept head traveling, reschedule | Ask Dir. Wang for Jul 22 alternative | Complete IT architecture review |

---

> **Legal notice**: This playbook is protected under applicable copyright law. Without the author's written authorization, no commercial use is permitted (including resale, bundling, commercial training, or SaaS-ification).
> **Disclaimer**: The methodology herein is for learning reference only and does not constitute professional advice of any kind. Practitioners should adapt it to their specific context and bear responsibility for assessment conclusions.
> **Author**: yinjianheng (Yin Jianheng) | yinjianheng@foxmail.com | WeChat: YJH-yinjianheng
