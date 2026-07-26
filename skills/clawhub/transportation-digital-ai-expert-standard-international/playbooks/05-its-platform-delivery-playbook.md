# Intelligent Transport Management Platform — Project Delivery Playbook

## Playbook Overview

| Item | Description |
|------|-------------|
| **Applicable scenarios** | Delivery execution of large transport-digitalization projects such as intelligent transport management platforms / transport operations coordination centers (TOCC) / cloud-control platforms |
| **Project type** | Mainly software platform + data integration; may include hardware / device deployment |
| **Typical scale** | $0.4M–$7M+ (RMB 3M–50M+), 6–18 month delivery |
| **Core philosophy** | ITS platform delivery = software engineering + transport engineering + data engineering + organizational change + project process, all in one |
| **Biggest challenges** | Data integration (interfacing N legacy systems, each with pitfalls), changing requirements (public-sector leadership turnover / shifting priorities), hard acceptance ("how intelligent" is hard to quantify) |
| **Delivery team** | 1 PM + 1 architect + 6–12 front/back/data/AI devs + 2–3 testers + 2–4 implementation engineers + 1 UI/UX |

---

## Phase 0: Project Kickoff (Weeks 1–2 after contract signature)

### 0.1 Team Formation & Mobilization

**Project team configuration template (example: a $2M ITS platform project, RMB 15M):**

| Role | Headcount | Experience | On-site | Responsibility |
|------|-----------|------------|---------|----------------|
| Project Manager (PM) | 1 | 5+ yr transport-IT PM, PMP / PRINCE2 | 100% | Overall delivery, client comms, scope/schedule/quality/risk |
| Solution Architect | 1 | 8+ yr transport architecture, fluent in ISO 27001 / sovereignty / cloud-native | 50% | Architecture, hard-tech problem-solving, tech review |
| Front-end Dev | 2–3 | 3+ yr, viz (ECharts / Mapbox / Three.js) | 80% | Traffic cockpit, dashboard, business pages |
| Back-end Dev | 3–4 | 3+ yr, microservices / MQ / API gateway | 80% | Business logic, data services, integration |
| Data Engineer | 2 | 3+ yr, data warehouse / ETL / big-data platform | 100% | Data aggregation, governance, modeling, dev |
| AI Engineer | 1 | 3+ yr transport-AI | 50% | AI algorithm dev & tuning |
| Test Engineer | 2 | 3+ yr, incl. automation & security testing | 80% | Functional / perf / security / UAT support |
| Implementation Engineer | 2–3 | 2+ yr, Linux / network / DB O&M | 100% | Env deploy, data integration, config |
| UI/UX Designer | 1 | 3+ yr, transport viz | As needed | Interface & interaction design |

**Team-formation checklist:**
- [ ] Key persons (PM / architect) on board and consistent with the tech proposal (deviation needs client's written consent)
- [ ] All on-site staff signed NDAs
- [ ] All on-site staff completed security clearance / background check (if client requires)
- [ ] Created project Teams / Slack channel + shared document library
- [ ] Set up SVN / Git repos + CI/CD pipeline
- [ ] Created project wiki / knowledge base (Confluence / Notion / SharePoint)
- [ ] PMP / PRINCE2 and relevant certificates ready for client verification

### 0.2 Kickoff Meeting

**Kickoff agenda (120 min):**

| Time | Segment | Content | Presenter / participants |
|------|---------|---------|--------------------------|
| 0–15 min | Introductions | Client & vendor project teams | Both PMs |
| 15–30 min | Project overview | Goals, scope, deliverables, schedule | Vendor PM |
| 30–45 min | Governance | Governance structure, comms cadence, escalation path | Vendor PM |
| 45–55 min | Near-term plan | Detailed next-4-week plan, client cooperation needed | Vendor PM |
| 55–70 min | Executive remarks | Client leadership's expectations & requirements | Client leadership |
| 70–90 min | Q&A & discussion | Open discussion | All |
| 90–120 min | Group photo + working lunch | Build informal rapport | All |

**Kickoff deliverables:**
- [ ] Project Charter — signed by both
- [ ] Master Schedule — confirmed by both
- [ ] Project org structure & contact list
- [ ] Communications management plan
- [ ] Meeting minutes (sent within 24 h)

### 0.3 Governance Structure

**Three-tier governance:**

```
┌─────────────────────────────────────────────┐
│   Steering Committee (monthly)                │
│   Client leadership + Vendor VP + both PMs + supervisor (if any) │
│   Decisions: budget change, scope change, key risk, acceptance │
└─────────────────────────────────────────────┘
                      │
┌─────────────────────────────────────────────┐
│   Weekly Project Meeting (weekly)             │
│   Client PM + Vendor PM + both core teams + supervisor │
│   Decisions: schedule, resourcing, risk, tech disputes │
└─────────────────────────────────────────────┘
                      │
┌─────────────────────────────────────────────┐
│   Daily Standup (15 min daily)                │
│   Vendor technical team internal              │
│   Sync: yesterday / today / blockers / asks   │
└─────────────────────────────────────────────┘
```

### 0.4 Baseline the Project Plan

**Master Schedule template structure:**

| WBS | Task | Start | End | Duration | Predecessor | Owner | Deliverable | Milestone |
|-----|------|-------|-----|----------|-------------|-------|-------------|-----------|
| 1.0 | Kickoff | D0 | D0+14 | 2 wk | - | PM | Project charter | M0-Kickoff |
| 2.0 | Requirements & design | D0+15 | D0+90 | 10 wk | 1.0 | Architect | Req spec, design docs | M1-Design review |
| 3.0 | Platform dev | D0+61 | D0+240 | 26 wk | 2.0SS+30d | Dev team | Iterative releases | |
| 3.1 | Sprint1-core framework | D0+61 | D0+90 | 4 wk | | | Sprint1 | |
| 3.2 | Sprint2-traffic monitoring | D0+91 | D0+120 | 4 wk | 3.1 | | Sprint2 | |
| 3.3 | ... | | | | | | | |
| 4.0 | Data integration & governance | D0+15 | D0+210 | 28 wk | 2.0SS | Data team | Integration done | |
| 5.0 | Integration testing | D0+241 | D0+300 | 8 wk | 3.0, 4.0 | Test team | Test report | M2-Integration |
| 6.0 | UAT | D0+301 | D0+340 | 6 wk | 5.0 | PM + client | UAT sign-off | M3-UAT |
| 7.0 | Deployment & go-live | D0+341 | D0+360 | 3 wk | 6.0 | Impl team | Go-live confirmation | M4-Go-live |
| 8.0 | Pilot ops & optimization | D0+361 | D0+420 | 8 wk | 7.0 | PM | Pilot-ops report | M5-Initial acceptance |
| 9.0 | Formal acceptance & handover | D0+421 | D0+450 | 4 wk | 8.0 | PM | Final acceptance cert | M6-Final acceptance |

---

## Phase 1: Requirements & Design (Weeks 3–12)

### 1.1 Detailed Requirements Workshops

**Workshop series (recommend 2×/week, 3 h each, 4–6 weeks):**

| Week | Theme | Participants | Output |
|------|-------|--------------|--------|
| W3 | Overall business-process mapping | Client business leads + vendor BA/architect | AS-IS process, TO-BE blueprint |
| W4 | Traffic monitoring & situational awareness | Control center / traffic ops | Monitoring metrics, alert rules |
| W5 | Signal control & traffic organization | Traffic ops / signal optimization | Signal-optimization needs, eval criteria |
| W6 | Analytics & decision support | Business-unit heads | KPI defs, report / dashboard needs |
| W7 | Incident mgmt & emergency command | Control center / emergency office | Incident taxonomy, handling flow, linkage |
| W8 | Data integration & sharing | IT function | Source list, interface needs, sharing scope |
| W9 | NFR confirmation | IT O&M team | Performance, security, O&M needs |
| W10 | Requirements review & sign-off | Both core teams | Signed Requirements Spec V1.0 |

**Workshop execution guide:**
1. Send agenda & pre-read (prior output) 3 days ahead
2. 80% of time for "aligning understanding", 20% for "confirming records"
3. Use user-story format: As a [role], I want [function] so that [value]
4. Confirm ambiguous requirements on the spot with flow/prototype/table — don't "discuss later"
5. Send minutes + updated doc within 24 h

### 1.2 Architecture Design

**Five-layer architecture diagrams (mandatory):**

| Layer | Content | Deliverable |
|-------|---------|-------------|
| Business architecture | Processes, capability map, org & roles | Business-architecture diagram + capability list |
| Application architecture | Module split, inter-module interaction, roles & permissions | App-architecture diagram + function list |
| Data architecture | Data domains, data model (ER), data-flow, warehouse layering | Data-architecture diagram + data dictionary |
| Technical architecture | Component selection, deployment topology, containerization / microservices | Tech-architecture diagram + deployment diagram |
| Security architecture | Network zoning, access control, data security, accreditation mapping | Security-architecture diagram + policy table |

**Design-review entry criteria:**
- [ ] All five architecture diagrams complete
- [ ] Core tech selection justified (≥3-way comparison)
- [ ] Legacy-system integration plan clear
- [ ] Data architecture has full source list + field-level mapping
- [ ] Security architecture mapped item-by-item to ISO 27001 / Level 3 equivalent
- [ ] Client technical team previewed docs ≥3 days ahead

**Design-review process (120 min):**
1. Architect presents (45 min): each layer's decisions & rationale
2. Client technical team questions (45 min): feasibility, performance, security, scalability
3. Consensus & to-dos (30 min): revised version within 3 days, request sign-off

### 1.3 Data Integration Design

**Elements that data-integration design must include:**

| Element | Description |
|---------|-------------|
| Source list | Per source: system name, vendor, protocol, format, frequency, volume |
| Field-level mapping | Exact source→target field mapping, with transformation rules (code/unit/cleaning) |
| Interface plan | Tech per interface type (API / MQ / ETL / file / DB direct) |
| Data-quality standard | Quality reqs (completeness / accuracy / timeliness) & monitoring rules |
| Exception handling | Detection & recovery for data outage / delay / dirty data |
| Data security | Transport encryption, storage encryption, masking rules, access control |

**Early identification of interface-integration risks:**
- [ ] Any vendor unwilling to provide interfaces? (contractual obligation, exec escalation, fallback)
- [ ] Any legacy data format non-standard / undocumented? (reverse-engineering effort & risk estimate)
- [ ] Any external-org data (e.g., emergency services / 911 / 112, meteorological agency, internet companies)? (high coordination cost, start early)
- [ ] Any legacy system (10+ yr) with weak interface capability? (may need data-collection gateway / middleware)
- [ ] Any ambiguous data-sovereignty boundary? (e.g., cross-department sharing needs an agreement)

---

## Phase 2: Development (Weeks 9–34, ~6 months, overlaps design by 3 weeks)

### 2.1 Agile Sprint Structure

**Recommended Scrum (ITS-platform-adapted):**

| Element | Standard Scrum | ITS-platform adaptation |
|---------|----------------|-------------------------|
| Sprint length | 2 wk | 3–4 wk (transport scenarios complex; 2 wk too short) |
| Sprint planning | Day 1, 4 h | Day 1, 4 h |
| Daily standup | 15 min | 15 min |
| Sprint review | Last day, 2 h | Last day, 2 h (invite client business staff) |
| Sprint retro | Last day, 1.5 h | Last day, 1.5 h (internal) |

**Sprint cadence example:**

| Sprint | Period | Goal | Key user stories |
|--------|--------|------|------------------|
| Sprint 1 | W9–W12 | Framework + first feature live | Microservice base, API gateway, unified auth, base data model |
| Sprint 2 | W13–W16 | Traffic situational monitoring | Real-time map, flow stats, device-status monitoring |
| Sprint 3 | W17–W20 | AI incident detection | Video-AI detection, auto-alert, incident closed-loop |
| Sprint 4 | W21–W24 | Signal optimization | Timing-plan mgmt, effect eval, recommendation engine v1 |
| Sprint 5 | W25–W28 | Analytics & reporting | KPI dashboard, auto report gen, custom analysis |
| Sprint 6 | W29–W32 | Digital twin | 3D road-network render, vehicle simulation, incident replay |
| Sprint 7 | W33–W36 | Integration & optimization | All sources integrated, perf tuning, bug fixes |

### 2.2 Development Standards

**Code-management standards:**
- [ ] Git Flow or GitHub Flow — main branch always deployable
- [ ] Feature branch naming: `feature/[module]-[feature]` (e.g., `feature/traffic-detection-ai-event`)
- [ ] Code review: every PR needs ≥1 approval before merge
- [ ] Commit message standard: `type(scope): description` (e.g., `feat(detection): add wrong-way AI detection`)

**Code-review checklist:**
- [ ] Logic correctness — implements the user story?
- [ ] Edge cases — empty data / huge values / concurrency / offline handled?
- [ ] Performance — N+1 queries, bad loops, unpaginated full scans?
- [ ] Security — injection risk, sensitive-data logging, unauthorized access?
- [ ] Maintainability — clear naming, adequate comments, no duplication?
- [ ] Test coverage — unit / integration on critical paths?

### 2.3 Daily Standup Agenda

**15-min standard standup template:**

| Segment | Time | Each speaks |
|---------|------|-------------|
| Yesterday | Round-robin | "Yesterday I finished [task], hit [blocker] (if any)" |
| Today | Round-robin | "Today I will finish [task]" |
| Blockers / asks | Raise hand | "I need [XX]'s help with [YY]" |
| PM addendum | 2 min | Project-level info (client dynamics / risk alert / milestone reminder) |

**Standup rules:**
- Late-comer contributes to the team coffee fund — discipline matters
- Each speaks ≤2 min — only "what I did / will do"; deep discussion offline
- Don't solve, only identify; solve in a separate meeting
- PM logs all blockers and follows up immediately

---

## Phase 3: Integration & Testing (Weeks 35–46)

### 3.1 Integration Test Plan

**Test-strategy pyramid:**

```
        ╱  UAT ╲          ← Client business-staff acceptance
       ╱  E2E  ╲         ← End-to-end flow test
      ╱ Integration ╲    ← Module integration + data-flow test
     ╱  API test   ╲     ← Automated API interface test
    ╱   Unit test   ╲    ← Function / class level
```

**Test types & scope:**

| Type | Scope | Tool | Owner | Pass criterion |
|------|-------|------|-------|----------------|
| Unit | Core logic, algorithms | JUnit / pytest / Jest | Dev self-test | Coverage >70% |
| API | All API interfaces | Postman / JMeter / scripts | Test engineer | All interfaces normal |
| Integration | Module interaction, end-to-end data flow | Manual + auto | Test engineer | Core flows pass |
| Performance | Concurrent users, data-volume ceiling | JMeter / Locust | Test + architect | Meets NFR |
| Security | SQLi / XSS / privilege / sensitive data | Burp Suite / OWASP ZAP | Security eng / external | No high-risk vuln |
| Compatibility | Browser / OS / resolution | BrowserStack / manual | Test engineer | Major browsers compatible |
| UAT | Real business scenarios | Manual + client | Client + vendor support | UAT sign-off |

### 3.2 Performance Test Scenarios

**Typical ITS-platform performance scenarios:**

| Scenario | Metric | Target | Method |
|---------|--------|--------|--------|
| Dashboard home load | First-screen load | <3 s | Simulate normal network, FCP/LCP |
| 10K video concurrent ingest | CPU/mem/bandwidth | CPU<70%, mem<80%, no frame loss | Inject simulated video |
| 1000-intersection real-time compute | Compute latency | <500 ms | 1000 streams concurrent write+read |
| 1-yr historical query | Query response | <5 s | ~TB-scale 1-yr range query |
| 500 concurrent logins | Login response | <2 s | JMeter 500 concurrency |
| Data-outage recovery | Re-alignment after outage | Replenish within 5 min | Simulate 30-min outage then recover |

### 3.3 UAT Guide

**UAT execution steps:**

| Step | Content | Time | Owner |
|------|---------|------|-------|
| 1. UAT plan | Write UAT cases (from user-story acceptance), assign testers & schedule | W43 | Client PM + vendor PM |
| 2. UAT training | Train client UAT staff on system operation (2–4 h) | W43 | Vendor trainer |
| 3. UAT env | Build UAT env (same config as production) | W43 | Vendor impl |
| 4. Round-1 UAT | Execute cases, log defects | W44–W45 | Client business staff |
| 5. Defect fix | Vendor fixes (severity: critical<1 d, major<3 d, minor<1 wk) | W44–W46 | Vendor dev |
| 6. Round-2 UAT (regression) | Verify fixes + re-run partial cases | W46–W47 | Client business staff |
| 7. UAT sign-off | All critical/major closed, client signs UAT pass report | W47 | Client PM |

**UAT test-case template:**

| ID | Module | Scenario | Precondition | Steps | Expected | Actual | Pass/Fail | Defect ID |
|----|--------|----------|--------------|-------|----------|--------|-----------|-----------|
| UAT-001 | Situation | View real-time map | Logged in, map permission | 1. Enter home 2. View network color 3. Click segment for detail | Network colored by congestion; click shows flow/speed | | | |

### 3.4 Defect-Management Process

**Defect severity levels:**

| Level | Definition | Response | Fix time | Example |
|-------|------------|----------|----------|---------|
| P0 Blocker | System crash, core function unusable | 1 h | 24 h | Cannot log in, blank dashboard |
| P1 Critical | Core function affected but runs | 4 h | 3 d | Real-time data delay >5 min, alert not triggered |
| P2 Major | Non-core anomaly, inaccurate data | 1 d | 1 wk | Report deviation >10%, history query timeout |
| P3 Minor | UI anomaly, wrong copy, occasional small bug | 3 d | Next sprint | Layout misalign, date widget anomaly |
| P4 Suggestion | Improvement idea | None | Backlog | "Add PDF export to reports" |

**Defect tools:** Jira / Azure DevOps / Linear

**Defect flow:** 1. Submit (tester/user) → 2. Triage (lead judges dup & severity) → 3. Assign (dev lead) → 4. Fix → 5. Verify (tester regression) → 6. Close (lead confirms)

---

## Phase 4: Deployment & Go-Live (Weeks 47–50)

### 4.1 Cutover Plan

**Cutover plan template:**

1. **Cutover overview**
   - Goal, scope, time window (recommend Fri 22:00 – Sat 06:00)
   - Impact (which systems/users, downtime)

2. **Pre-cutover prep**
   - Production env ready (servers/network/storage/security)
   - Data-migration plan (full/incremental/batch)
   - All external-dependency integrations tested

3. **Cutover steps (to the minute)**
   ```
   22:00 - Publish downtime notice
   22:15 - Stop old-system writes
   22:30 - Full data backup
   23:00 - Run DB migration script
   23:30 - Deploy new version
   00:00 - Start new system, verify core functions
   00:30 - Data-consistency check
   02:00 - Open internal validation
   04:00 - Performance stress test
   05:00 - Prepare open (clear cache, warm up)
   06:00 - Officially open
   06:00-12:00 - Production monitoring + standby
   ```

4. **Cutover support team**
   - Commander (PM) ×1: decisions & external comms
   - DBA ×1: migration, rollback
   - App deploy ×2: version, config changes
   - Test verify ×2: quick core-function verification
   - Network/infra ×1: network/firewall/load balancer
   - Vendor support: DB / cloud / security device emergency contacts

### 4.2 Rollback Plan

**Rollback triggers:**
- [ ] Critical function severely anomalous, unfixable within 30 min
- [ ] Large-scale data corruption/loss (>5% of records)
- [ ] Severe performance degradation (response >10× normal)
- [ ] Security vulnerability triggered

**Rollback steps:**
1. Commander declares rollback (phone + group, dual channel)
2. Cut external access to new system (firewall / LB to maintenance page)
3. Stop all new-system services & DB connections
4. Restore DB to pre-cutover backup
5. Start old-system application
6. Verify core functions
7. Restore external access
8. Send rollback-complete notice

**Rollback downtime cap:** Complete rollback & restore service within 2 hours.

### 4.3 Go-Live Checklist (50+ items)

**A. Infrastructure & environment (12):**
- [ ] 1. Production servers configured per architecture (CPU/mem/disk/net)
- [ ] 2. OS installed & hardened (minimal install, latest security patches)
- [ ] 3. DB installed & configured (primary-standby/cluster, backup enabled)
- [ ] 4. Middleware (Nginx/Redis/Kafka/ES) installed & configured
- [ ] 5. Firewall rules configured (only necessary ports open)
- [ ] 6. SSL certificate deployed (HTTPS enforced site-wide)
- [ ] 7. Load balancer configured & verified
- [ ] 8. Log collection (ELK/cloud logging) configured
- [ ] 9. Monitoring & alerting (Prometheus/Zabbix) configured
- [ ] 10. Backup system configured & first full backup done
- [ ] 11. Time sync (NTP) configured
- [ ] 12. DNS resolution configured

**B. Application deployment (10):**
- [ ] 13. All microservices deployed to production
- [ ] 14. Configs adjusted for production
- [ ] 15. DB schema migration scripts executed
- [ ] 16. Initial data (dict/zones/users) imported
- [ ] 17. Scheduled jobs / CronJobs configured
- [ ] 18. File storage (OSS/MinIO) configured
- [ ] 19. CDN configured (if frontend static assets)
- [ ] 20. MQ (Kafka/RabbitMQ) topics created
- [ ] 21. API-gateway routes verified
- [ ] 22. Version number updated (for traceability)

**C. Data integration (8):**
- [ ] 23. All source interfaces connected
- [ ] 24. Real-time data flow connected & verified
- [ ] 25. Historical data migration complete
- [ ] 26. Data-quality check passed (completeness/accuracy sampling)
- [ ] 27. Data-sync monitoring configured (outage alert)
- [ ] 28. Data-masking rules active
- [ ] 29. Data-backup strategy configured
- [ ] 30. Data dictionary updated to production

**D. Security & compliance (8):**
- [ ] 31. Security accreditation body completed assessment (or confirmed post-go-live)
- [ ] 32. Penetration test complete, high-risk vulns fixed
- [ ] 33. Accounts assigned by least-privilege
- [ ] 34. Password policy enforced (complexity + 90-day expiry + no reuse)
- [ ] 35. Audit logging enabled
- [ ] 36. Sensitive-data encrypted storage verified
- [ ] 37. API auth + rate-limit configured
- [ ] 38. Code security scan complete

**E. Business validation (8):**
- [ ] 39. 10 core business flows end-to-end pass
- [ ] 40. Dashboard / cockpit data correct
- [ ] 41. AI incident-detection accuracy meets target
- [ ] 42. Report data sampled against source consistent
- [ ] 43. Different-role permissions verified
- [ ] 44. Browser compatibility (Chrome/Edge/Safari)
- [ ] 45. Mobile adaptation (if any)
- [ ] 46. Third-party integration joint-debug passed

**F. O&M readiness (6):**
- [ ] 47. O&M manual delivered (accounts, daily checks, fault SOP)
- [ ] 48. Client O&M staff trained
- [ ] 49. O&M monitoring dashboard deployed (alert rules, contacts)
- [ ] 50. 7×24 emergency contact list configured
- [ ] 51. Knowledge base / FAQ built
- [ ] 52. DR switchover drill completed (if active-active/standby required)

### 4.4 War Room Setup

**During go-live (usually 48–72 h), set up a War Room:**

- Physical room (meeting room) + online War Room channel
- Big screen: system monitoring dashboard (CPU/mem/req rate/error rate/alerts)
- Staffing: 7×24 three shifts, each ≥ PM ×1 + dev ×1 + O&M ×1
- Comms: group message + phone tree (emergencies must be phoned, not just messaged)
- War log: hourly — time, system status, anomalies, handling, decisions
- Snacks / late-night food / coffee: stock the physical room

---

## Phase 5: Stabilization & Handover (Weeks 51–58)

### 5.1 Hypercare Management

**Hypercare (usually 1 month):**

| Period | Response SLA | Activity | Exit condition |
|--------|--------------|----------|----------------|
| Week 1 | Critical 15-min response, 7×24 on-site | Daily stability check, same-day user issues | No P0/P1 for 3 consecutive days |
| Week 2 | Critical 30-min response, on-site in work hours | Daily patrol, reinforced training, minor tuning | No P0 for 7 consecutive days |
| Week 3–4 | Critical 1-h response, remote | Weekly patrol, issue collection, fine-tuning | All issues closed or with clear plan |

### 5.2 Knowledge-Transfer Plan

**Knowledge-transfer matrix:**

| Area | Client receiver | Method | Materials | Verification |
|------|-----------------|--------|-----------|--------------|
| System architecture | Client tech lead | Architecture session (4 h) + code walkthrough (2 h) | Arch docs, deployment diagram | Client can independently draw & explain arch |
| Daily O&M | Client O&M engineer | Hands-on (2 wk) + O&M manual | O&M manual, SOP cards | Independently 3 patrols + 1 fault handling |
| Data management | Client data admin | Data-dictionary session + DQ-monitoring training | Data dict, DQ rules | Independently run DQ & fix |
| User operation | Client dept operators | Dept training + manual + video | Manual, video tutorial | Training pass rate >90% |
| App development | Client in-house dev team | API-doc session + env setup + sample code | API docs, SDK, samples | Independently build 1 simple feature |

### 5.3 Document Handover List

**Mandatory documents:**

| Category | Document | Version | Status |
|---------|----------|---------|--------|
| **Design** | Requirements specification | V2.0 | Final |
| | Business-architecture design | V1.0 | |
| | Application-architecture design | V1.0 | |
| | Data-architecture design (incl. data dict) | V1.0 | |
| | Technical-architecture design | V1.0 | |
| | Security-architecture design | V1.0 | |
| | Interface design doc (all APIs) | V1.0 | |
| **Development** | Source code (incl. build scripts) | Release 1.0 | |
| | DB DDL/DML scripts | Release 1.0 | |
| | Deploy scripts / config files | Release 1.0 | |
| **Testing** | Unit-test report | V1.0 | |
| | Integration-test report | V1.0 | |
| | Performance-test report | V1.0 | |
| | Security-test report | V1.0 | |
| | UAT report | V1.0 | Signed |
| **O&M** | O&M manual | V1.0 | |
| | Emergency plan (fault SOP) | V1.0 | |
| | Daily patrol checklist | V1.0 | |
| | DR switchover manual | V1.0 | |
| **Operations** | User manual (by role) | V1.0 | |
| | Admin manual | V1.0 | |
| | Training PPT + video | V1.0 | |
| **Management** | Project acceptance report | V1.0 | Signed |
| | Project summary report | V1.0 | |
| | Asset handover list | V1.0 | Signed |

### 5.4 Acceptance & Sign-off

**Three-stage acceptance:**

| Stage | Time | Content | Pass criterion |
|-------|------|---------|----------|
| Preliminary acceptance | After go-live + hypercare | All functions deployed, core KPIs met, no major fault in hypercare | Sign Preliminary Acceptance Cert → pay to XX% |
| Final acceptance | 3–6 mo after preliminary | Stable operation, all functions normal, all docs handed over, KT complete | Sign Final Acceptance Cert → pay to XX% |
| Warranty-end acceptance | 1–3 yr after final | SLA met in warranty, all open issues closed | Sign Warranty-End Confirmation → release retention |

**Acceptance meeting agenda (60 min):**
1. Vendor report: delivery summary (10 min)
2. Client report: usage & evaluation (10 min)
3. Supervisor / third-party report (if any, 10 min)
4. Acceptance-doc review (15 min)
5. Acceptance resolution (10 min): pass / conditional pass / fail
6. Sign acceptance docs (5 min)

---

## Appendix: Common Management Tools

### Appendix A: Meeting Cadence

| Meeting | Frequency | Duration | Participants | Purpose |
|---------|-----------|----------|--------------|---------|
| Daily standup | Daily | 15 min | Vendor team | Sync + blocker ID |
| Weekly project meeting | Weekly | 60 min | Both PMs + core teams | Status + risk + change + decision |
| Monthly steering committee | Monthly | 60 min | Both leadership + PMs + supervisor | Strategic decisions + budget/scope change + major risk |
| Sprint review | Per sprint | 90 min | Vendor team + client business reps | Sprint demo + feedback |
| Tech workshop | As needed | 2–4 h | Both tech leads | Hard-tech problem-solving, architecture disputes |
| Risk review | Every 2 wk | 30 min | Vendor PM + core team | Update RAID log + risk tracking |

### Appendix B: Weekly Report Template

```
Project Weekly Report
Project: XX City Intelligent Transport Management Platform
Period: 2026.07.01 - 2026.07.07
Reporter: Zhang San (Vendor PM)

1. This week
1. Completed traffic-situation monitoring module Sprint 3 dev (80%)
2. Completed XX system data-interface integration (12/18 done, 6 pending coordination)
3. Completed round-1 integration test (23 defects found, 15 fixed)

2. Next week
1. Finish Sprint 3 remaining dev (est. 07.12)
2. Start Sprint 4 signal-optimization dev
3. Hold monthly steering committee (07.10)

3. Risks & issues
| ID | Risk/issue | Level | Impact | Status | Response |
|----|-----------|-------|--------|--------|----------|
| R01 | XX vendor interface doc not provided | High | Possible 2-wk delay | Escalated to client PM | Fallback: DB direct connect |

4. Needs from client
1. Coordinate XX vendor to provide interface doc (R01)
2. Confirm construction window during the upcoming public-holiday period
```

### Appendix C: Risk Escalation Path

| Level | Response | Escalate to | Condition |
|-------|----------|-------------|-----------|
| L1 Low | Track | PM | - |
| L2 Medium | Plan response within 48 h | PM | May affect non-critical milestone |
| L3 High | Plan response + notify client PM within 24 h | Client PM | May affect critical milestone or SLA |
| L4 Critical | Launch emergency within 4 h + notify steering committee | Both leadership | May cause project failure / major delay / safety incident |

### Appendix D: Change-Request Template

```
Project Change Request (CR)
CR ID: CR-2026-007
Raised by: Li Si (Client lead)
Date: 2026.07.05

Description: Add a "transport sentiment monitoring" module that auto-captures transport sentiment from social media / hotline complaints / news, with auto-classification and emotion analysis.

Reason: Agency executive has repeatedly stressed the importance of sentiment; requires the system to have sentiment-monitoring capability.

Impact assessment:
- Scope: +1 module (~8 function points)
- Schedule: +4 weeks (Sprint 8 extension)
- Cost: +~$50K (8 person-months × ~$6.5K)
- Risk: Sentiment data source needs third-party procurement; vendor-selection risk

Conclusion: Recommend approval (technically feasible; schedule to 2027.01.31; cost +~$50K)

Approval:
□ Client PM   □ Vendor PM   □ Supervisor   □ Steering Committee
```

### Appendix E: Top 15 Delivery Pitfalls

| # | Pitfall | Symptom | Prevention / response |
|---|---------|---------|------------------------|
| 1 | Requirement gold-plating | Client keeps adding "just add XX feature" | Strict CR flow — any new need is formal change with time/cost impact |
| 2 | Data-integration black hole | Integrating N legacy systems, each with unexpected pitfalls | Do a technical PoC per system in design (at least one joint debug); don't defer pitfalls to late dev |
| 3 | Uncooperative vendor | Legacy-system vendor refuses interface citing "impact on live network" | Contractually define interface-open obligation, exec push, or client administrative order if needed |
| 4 | Vague acceptance criteria | Contract says "achieve intelligent management", unquantifiable | Put acceptance criteria in the Requirements Spec in design — only testable items written, written items must be tested |
| 5 | Dashboard obsession | 80% effort on fancy dashboard, 20% on backend & data governance | PM controls — dashboard is the face, backend is the soul. Review backend progress weekly |
| 6 | Over-promised AI | Promised "95% AI accuracy", reality 70% | Validate AI metrics via PoC; add contract disclaimer "accuracy subject to data quality" |
| 7 | Staff pulled away | Core staff reassigned mid-project | Contractual key-person lock + internal back-to-back coverage |
| 8 | Client leadership turnover | Sponsor / IT director replaced; new lead "starts over" | Anchor the project to institutional documents (e.g., the strategic five-year plan); proactively report value to the new leader in week 1 |
| 9 | Ignored security accreditation | Near go-live, realize accreditation needs 2–3 months | Start accreditation-body selection & assessment in week 1 |
| 10 | Under-estimated performance | Test env (50 intersections) fine; production (500) collapses | Performance test in production-proportional env; simulate ≥1-yr data volume |
| 11 | Security incident | Attacked / data leak after go-live | Must complete security + penetration test before go-live; Level 3 equivalent non-negotiable |
| 12 | Token training | Client says "got it" but can't actually use it | Training assessment + 1-week follow-up + hypercare Q&A anytime |
| 13 | Missing docs | Code left, dev team gone, client can't understand | Docs are an acceptance deliverable; incomplete docs = no acceptance |
| 14 | O&M vacuum | After delivery, no one runs O&M | Start O&M-team transition late in project — O&M staff join hypercare |
| 15 | Retention black hole | Client withholds retention citing "not intelligent enough" | Contractual, quantifiable, verifiable acceptance; per-milestone sign-off |

---

> **Legal notice**: This playbook is protected under applicable copyright law. Without the author's written authorization, no commercial use is permitted (including resale, bundling, commercial training, or SaaS-ification).
> **Disclaimer**: The methodology herein is for learning reference only and does not constitute professional advice of any kind. Security and management decisions in actual delivery must be made by certified professionals.
> **Author**: yinjianheng (Yin Jianheng) | yinjianheng@foxmail.com | WeChat: YJH-yinjianheng
