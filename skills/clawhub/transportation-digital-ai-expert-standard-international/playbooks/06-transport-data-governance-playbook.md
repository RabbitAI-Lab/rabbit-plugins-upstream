# Transport Data Governance Launch Playbook

## Playbook Overview

| Item | Description |
|------|-------------|
| **Applicable scenarios** | Transport authorities (transport departments / highway operators / transit authorities, etc.) launching systematic data governance for the first time |
| **Core philosophy** | Data governance is not an IT project; it is a management & organizational change. Without executive sponsorship, cross-department coordination, and accountability mechanisms, it will fail |
| **Key success factors** | Executive sponsor (top-down), business-unit participation (not IT solo), right Quick Wins, and the trinity of policy + platform + culture |
| **Total duration** | 6–12 months (org setup 1 mo + asset inventory 2 mo + standards 2 mo + ongoing quality mgmt + security & compliance 1 mo) |
| **Deliverables** | Data-governance charter, data-asset catalog, data standards, data-quality report, data security classification scheme |
| **Core team** | 1 data-governance PM + 1 data architect + 2–3 data stewards + data liaisons from each business unit |

---

## Phase 1: Organization Setup (Weeks 1–4)

### 1.1 Establish the Data Governance Committee

**Why organization first:**
Transport data lives across dozens of systems — signal systems, enforcement cameras, ANPR, emergency-services dispatch, maintenance, tolling, transit dispatch, GPS positioning, video surveillance — owned by different business units and vendors. Without a strong organization pushing, no one voluntarily "hands over" their data.

**Three-tier data-governance structure:**

```
┌──────────────────────────────────────────────────────────┐
│   Data Governance Steering Committee (quarterly)           │
│   Chair: top executive or CIO sponsor / GM                 │
│   Members: heads of business units + head of IT function   │
│   Duties: data strategy, approve standards, resolve cross-  │
│           dept disputes, approve budget                     │
└──────────────────────────────────────────────────────────┘
                          │
┌──────────────────────────────────────────────────────────┐
│   Data Governance Working Group (1–2× / month)             │
│   Lead: head of IT function                                │
│   Members: data stewards from units + governance team + legal/compliance │
│   Duties: set standards, coordinate execution, monitor quality, accept outputs │
└──────────────────────────────────────────────────────────┘
                          │
┌──────────────────────────────────────────────────────────┐
│   Data Governance Execution Team (daily)                   │
│   Data Steward × 1 per business domain                     │
│   Data Engineer × 2–3 (ETL / data quality / data platform) │
│   Data Architect × 1 (data model / standards / architecture)│
└──────────────────────────────────────────────────────────┘
```

### 1.2 Data Governance Committee Charter Template

```
[XX Transport Authority Data Governance Committee Charter]

Article 1 — General Principles
To strengthen management of the authority's transport-data assets, improve data quality,
safeguard data security, and promote data sharing, this Data Governance Committee
(hereinafter "the Committee") is established under the data-security law and
data-protection regulation.

Article 2 — Duties
1. Approve the data-governance strategy and annual plan
2. Approve data-management policies and standards
3. Coordinate cross-department data sharing and dispute resolution
4. Approve the data security classification & grading scheme
5. Assess each department's data-governance performance

Article 3 — Composition
Chair: [executive / CIO sponsor]
Vice-chair: [head of IT function]
Members: [heads of business units + legal/compliance + admin + subordinate units]

Article 4 — Operating mechanism
1. The Committee meets in full session quarterly
2. Ad-hoc meetings may be called for major matters
3. Resolutions pass with majority approval of members
4. Daily work is carried by the Working Group

Article 5 — Assessment
Data-governance performance is included in each department's annual KPI, weight ≥5%.

Article 6 — Supplementary
This charter takes effect upon issuance.
```

### 1.3 Data Steward Nomination

**Data Steward profile:**

| Requirement | Description |
|-------------|-------------|
| Post | Permanent business-unit staff (not outsourced / intern), 3+ yr domain experience |
| Capability | Knows the unit's business data, some IT literacy (no coding required) |
| Time | At least 30% of working time on data-governance matters |
| Communication | Can "translate" between business and technical teams |
| Reporting | Administratively under the business unit; governance work reports to the Working Group |

**Data steward responsibility list:**
- [ ] Inventory the unit's data assets (systems, tables, fields, data dictionary)
- [ ] Define the domain's data standards and quality rules
- [ ] Own the quality of the unit's data (entry norms, exception handling)
- [ ] Approve the unit's data-sharing requests
- [ ] Attend the Working Group's monthly meeting
- [ ] Participate in data security classification

### 1.4 RACI Matrix (data-governance responsibilities)

| Activity / decision | Steering | CIO/IT head | Gov PM | Data architect | Data steward | Biz-unit head | Data steward (liaison) | Legal/compliance |
|---------------------|----------|-------------|-------|----------------|--------------|---------------|-------------------------|------------------|
| Approve data strategy | A | R | C | C | C | C | I | I |
| Set data standards | I | A | R | R | C | C | C | C |
| Data-asset inventory | I | A | R | C | R | I | C | I |
| Define quality rules | I | I | A | C | R | I | C | I |
| Monitor data quality | I | I | A | C | R | I | R | I |
| Approve data sharing | I | I | R | C | I | A | C | C |
| Data security classification | I | A | R | C | C | C | C | C |
| Resolve exec disputes | A | R | C | I | I | C | I | I |

> R=Responsible, A=Accountable, C=Consulted, I=Informed

---

## Phase 2: Data-Asset Inventory (Weeks 5–12)

### 2.1 System Census

**System census questionnaire (sent to each business-system and data-source owner):**

| # | Question | Answer |
|---|----------|--------|
| 1 | System / data-source name | Metro Traffic Signal Control System |
| 2 | Owning department | Traffic Operations Division |
| 3 | System vendor | Siemens Mobility |
| 4 | Launch year | 2019 |
| 5 | Main functions | Signal control, timing optimization, green-wave coordination |
| 6 | DB type & version | PostgreSQL 12 |
| 7 | Approx. table count | 45 tables |
| 8 | Top 5 core tables | signal_plan, detector_data, intersection_config, green_wave, timing_log |
| 9 | Daily data growth | ~500 MB/day |
| 10 | Cumulative volume | ~3 TB (since 2019) |
| 11 | Main field types | intersection_id, direction, lane, detector data (flow/speed/occupancy), signal state, timing plan |
| 12 | Contains personal / private data? | No (device & aggregate stats only) |
| 13 | Update frequency | Detector: 1 min; timing plan: on demand |
| 14 | Data dictionary complete? | Partial (core tables documented, auxiliary not) |
| 15 | Already shared externally? | Yes, to the command-center dashboard via API |
| 16 | Data owner | Engineer Wang (tel: +1-xxx) |
| 17 | Vendor tech support contact | Engineer Li (Siemens, tel: +1-xxx) |

### 2.2 Data-Catalog Tool Selection

**Data-catalog platform options:**

| Option | When | Strengths | Limits |
|--------|-------|-----------|--------|
| Commercial catalog (Alation / Collibra / Informatica) | Large org, ample budget, needs automation | Auto-discovery, lineage, AI tagging | Expensive (seven figures), complex, sovereign-cloud fit unverified |
| Cloud-native governance suites (AWS Glue DataBrew / Azure Purview / Google Cloud Data Catalog) | Mid budget, cloud-bound | Deep cloud-ecosystem integration | Ecosystem lock-in, not fully neutral |
| Open source (Apache Atlas / DataHub / Amundsen) | Strong tech team, limited budget | Free, customizable | Self-deploy & operate, weaker UI |
| Lightweight in-house (Airtable / Google Sheets + scripts) | Starting out, <50 sources | Zero cost, fast start | Weak, not scalable, no lineage |

**Starting recommendation:** If just beginning, <50 sources, <5 people, strongly recommend starting with "Excel / Google Sheets" for the catalog — get a catalog first, then consider tools. Don't buy a seven-figure platform upfront (it will likely become a showpiece).

### 2.3 Cataloging Process

**Seven-step data-asset cataloging:**

```
Step 1: Identify business domains
  └→ Split assets by domain (e.g., signal control / violation mgmt / incident handling / mobility service / highway maintenance / integrated mgmt)
  └→ Output: domain list (usually 6–12)

Step 2: Identify systems
  └→ Which IT systems / sources under each domain?
  └→ Output: system–domain mapping

Step 3: Identify datasets
  └→ Which tables / datasets under each system?
  └→ Output: dataset list (tag core/important/general)

Step 4: Identify fields
  └→ Core fields per dataset? Type/length/enum/business meaning?
  └→ Output: field-level data dictionary

Step 5: Identify relationships
  └→ Lineage & associations between datasets / fields?
  └→ Output: data-lineage diagram (core datasets first)

Step 6: Identify flows
  └→ Where from, where to, how does it flow?
  └→ Output: data-flow diagram

Step 7: Identify quality
  └→ Quality status per dataset? (from quick quality assessment, Phase 4)
  └→ Output: quality tags
```

**Data-asset catalog card example:**

| Attribute | Content |
|-----------|---------|
| Dataset ID | DS-SC-001 |
| Dataset name | Real-time intersection traffic-flow detection data |
| Business domain | Signal Control (SC) |
| Source system | Traffic Signal Control System |
| Description | Real-time detector flow data for 800 city intersections |
| Update frequency | 1 min |
| Core fields | intersection_id, direction, lane_no, volume, speed, occupancy, timestamp |
| Volume | ~14M records/day (800 intersections × 4 dir × 3 lanes × 1440 min) |
| Quality grade | B (completeness 90% / accuracy 95% / timeliness excellent) |
| Security grade | General data |
| Data owner | Engineer Zhao (Traffic Ops) |
| Tech owner | Engineer Qian (Information Center) |
| Sharing status | Shared (command-center dashboard, ITS platform) |

### 2.4 Data-Domain Definitions

**Typical transport data-domain split:**

| Domain | Code | Data types | Owning unit |
|--------|------|-----------|-------------|
| Traffic-flow detection | TF | Loop/radar/video flow, inductive-loop/WiFi probe, ETC-collected | Traffic ops / highway |
| Traffic events | TE | Crashes/congestion/work zone/control/adverse weather/major events | Command center |
| Signal control | SC | Timing plans, phases, green-wave, special-event routes | Traffic ops |
| Traffic violations | TV | Enforcement-camera capture, ANPR, violation handling, points | Traffic ops / ITS-tech |
| Infrastructure | IN | Road attributes, intersection geometry, signs/markings, controller/camera sites | Infrastructure / maintenance |
| Public transit | PT | Bus routes/stops, arrival/departure, ridership, payment | Transit authority |
| Mobility service | MS | Navigation data, shared bikes, ride-hail, parking guidance | Third-party + parking |
| Safety & emergency | EM | Emergency plans, resources, drills, dispatch records | Emergency office / command center |
| Asset management | AM | Equipment register, maintenance records, asset status, work orders | Maintenance / O&M |
| Integrated management | GM | Office OA, HR, finance, documents | Admin |
| Environment & weather | EN | Weather, air quality, road flooding | Met office / environment agency |
| V2X | VX | V2X messages, RSU status, OBU data | ITS-tech |

---

## Phase 3: Standards Development (Weeks 9–16, overlaps Phase 2)

### 3.1 Data-Standards Framework

**Four components of the data-standards system:**

| Standard type | Content | Example |
|---------------|---------|---------|
| **Foundation** | Data-element, coding, naming standards | Intersection-ID coding rule, device-type code table |
| **Model** | Conceptual / logical / physical data models | Traffic-flow fact + dimension design |
| **Quality** | Quality-dimension defs, rules, KPIs | Completeness >95%, timeliness delay <5 min |
| **Security** | Classification & grading, masking, access policy | Plate-number masking, personal-data protection |

### 3.2 Naming-Convention Design

**Database-object naming convention:**

| Object | Convention | Example | Note |
|--------|-----------|---------|------|
| Database | `db_<domain>_<env>` | `db_sc_prod` | Signal domain – production |
| Schema | `<domain>_<sub>` | `sc_detection` | Signal – detection sub-domain |
| Table | `<layer>_<domain>_<content>_<granularity>` | `dwd_sc_detector_1min` | DWD – signal – detector – 1-min |
| Field | `<modifier>_<subject>_<attr>` or `<subject>_<attr>` | `avg_speed`, `lane_volume` | Snake case (lower + underscore) |
| Index | `idx_<tbl_abbr>_<field>` | `idx_detector_1min_ts` | prefix idx + abbr + field |
| View | `v_<domain>_<content>` | `v_sc_intersection_status` | prefix v_ |
| Stored proc | `sp_<func>_<obj>` | `sp_agg_daily_traffic` | prefix sp_ |

**Layer naming (warehouse layering):**

| Layer | Prefix | Note |
|-------|--------|------|
| ODS operational | `ods_` | Raw, consistent with source |
| DWD detail | `dwd_` | Cleaned detail |
| DWS summary | `dws_` | Dimension-aggregated |
| ADS application | `ads_` | Application-facing data products |
| DIM dimension | `dim_` | Dimension tables |

### 3.3 Coding-Standard Design

**Transport-entity coding examples:**

| Entity | Format | Example | Note |
|--------|--------|---------|------|
| Intersection / node | Region code + serial | MET-00101 | Metro-district intersection #101 |
| Road segment | Intersection ID + "-" + Intersection ID | MET-00101-MET-00105 | Segment 101→105 |
| Signal controller | SC + region + serial | SC1001 | Controller #001 |
| Enforcement camera | EP + region + serial | EP0512 | Camera #0512 |
| Bus stop | BS + region + serial | BS00001 | |
| Motorway | M + number | M25 | (UK) / I-95 (US) equivalent |
| National/state road | N + number | N1 | National highway |
| District | 6-digit area code | 110105 | Central District |

### 3.4 Data-Model Design

**Generic transport star-model example:**

```
Fact table: FACT_TRAFFIC_FLOW
├── DIM_TIME (time dimension)
│   ├── time_key, minute, hour, day, week, month, year
│   ├── is_peak_hour, is_holiday, is_weekend
├── DIM_INTERSECTION (intersection dimension)
│   ├── intersection_id, intersection_name, district
│   ├── road_class, lanes_count, signal_controller_type
├── DIM_DIRECTION (direction dimension)
│   ├── direction_id, direction_name (E/S/W/N)
├── DIM_LANE (lane dimension)
│   ├── lane_id, lane_type (through/left/right/U-turn)
├── Measures:
│   ├── volume (flow / veh)
│   ├── avg_speed (avg speed / km/h)
│   ├── occupancy (%)
│   ├── queue_length (m)
│   ├── headway (s)
```

---

## Phase 4: Quality Management (starts Week 8, ongoing)

### 4.1 Data-Quality Rule Design

**Examples across the six transport-data quality dimensions:**

**1. Completeness:**
| Rule ID | Description | Dataset | Target | Trigger |
|---------|-------------|---------|--------|---------|
| COMP-001 | intersection_id not null | Flow detection | 100% | Null rate >0.1% alerts |
| COMP-002 | At least one of flow/speed/occupancy has value | Flow detection | >99% | All-three-null >1% |
| COMP-003 | Every record has a timestamp | All real-time | 100% | Missing timestamp alerts |

**2. Accuracy:**
| Rule ID | Description | Dataset | Method | Target |
|---------|-------------|---------|--------|--------|
| ACC-001 | Speed within reasonable range | Detector | 0≤speed≤120 km/h (urban) or 150 (highway) | Out-of-range <0.1% |
| ACC-002 | Occupancy 0–100% | Detector | 0≤occupancy≤100 | Out-of-range = 0 |
| ACC-003 | intersection_id exists in standard code library | All intersection | Join DIM_INTERSECTION | Match >99% |

**3. Consistency:**
| Rule ID | Description | Dataset | Method |
|---------|-------------|---------|--------|
| CON-001 | Flow from different detectors roughly consistent (dev <15%) | Loop vs radar vs video | Cross-validation |
| CON-002 | Intersection total in-flow ≈ total out-flow (err <10%) | In/out flow | In/out balance check |
| CON-003 | Device status consistent between signal & asset systems | Signal vs asset | Periodic reconciliation |

**4. Timeliness:**
| Rule ID | Description | Target | Trigger |
|---------|-------------|--------|---------|
| TIME-001 | Flow data latency ingestion→lake | <1 min | >5 min alerts |
| TIME-002 | Incident recorded latency | <30 s | >2 min alerts |
| TIME-003 | Video-AI event-analysis latency | <3 s | >10 s alerts |

**5. Uniqueness:**
| Rule ID | Description | Method |
|---------|-------------|--------|
| UNIQ-001 | (intersection_id + timestamp + direction + lane) unique | GROUP BY combo, HAVING COUNT(*) > 1 |

**6. Conformity:**
| Rule ID | Description | Method |
|---------|-------------|--------|
| NORM-001 | Date format YYYY-MM-DD HH:MM:SS | Regex |
| NORM-002 | Plate number conforms to standard format (incl. EV plates) | Regex |

### 4.2 Quality-Monitoring Dashboard Design

**Key dashboard metrics (for the Working Group):**

| Area | Shows | Visualization |
|------|-------|---------------|
| Overview | Global quality score (weighted), trend | Big number + trend line |
| By domain | Quality-score ranking per domain | Bar chart |
| By dimension | Completeness/accuracy/consistency/timeliness/uniqueness scores | Radar |
| By source | Quality ranking per source (find "troublemakers") | Heatmap |
| Issue trend | New vs resolved issues weekly | Line |
| Issue list | Open issues ranked (severity + age) | Table |

### 4.3 Data-Quality Issue Management

```
Discover issue → log ticket → root-cause analysis → fix plan
                                        ↓
                              Short-term fix (correct data)
                              Long-term fix (source-system / process change)
                                        ↓
                              Verify fix → close ticket → update rules
```

**Quality-issue ticket template:**

| Field | Content |
|-------|---------|
| Ticket ID | DQ-2026-0158 |
| Found at | 2026.07.05 14:30 |
| How found | Auto-alert / manual / user feedback |
| Dataset | Radar detector flow data |
| Description | Intersection MET-00101 (Main St – Central Ave), northbound, zero for 3 days |
| Quality dimension | Accuracy |
| Severity | High (affects AI signal-control training) |
| Impact | Northbound timing-plan recommendation for that intersection |
| Root cause | Northbound radar sensor fault (confirmed 07.05 15:00) |
| Fix plan | Short: flag direction unavailable; Long: replace radar sensor |
| Owner | Engineer Qian (Info Center) / hardware vendor after-sales |
| Target date | Short 07.05 17:00 / Long 07.12 |
| Verify | Observe 3 days after recovery |
| Status | In progress |

### 4.4 Data-Quality SLA

**Suggested data-quality SLA:**

| Grade | Completeness | Accuracy | Timeliness | Response | Fix SLA |
|-------|-------------|----------|------------|----------|---------|
| Core (safety / core business) | ≥99.5% | ≥99% | Real-time | 1-h response | P0:4h, P1:24h |
| Important (mgmt decisions) | ≥98% | ≥95% | Within T+1h | 4-h response | P1:3d, P2:1w |
| General (auxiliary / stats) | ≥95% | ≥90% | Within T+1d | 24-h response | P2:2w |

---

## Phase 5: Security & Compliance (Weeks 12–16)

### 5.1 Data Classification & Grading

**Three-tier transport-data classification:**

| Grade | Definition | Examples | Protection |
|-------|------------|----------|-----------|
| **Core** | Leakage may endanger critical transport infrastructure & operations | Citywide signal-control logic & parameters, original structural-monitoring data of key bridges/tunnels, emergency traffic-control plans, no-fly-zone data | Highest: physical isolation or private network, full encryption, dual control, audit |
| **Important** | Leakage may affect public interest, operations order, or citizen privacy | Vehicle-trajectory data (>50 vehicles), HD ANPR images, full flow data, timing plans, toll records, BRT/metro ridership, emergency plans | Strong: encrypted in transit & at rest, access audit, mask before analysis |
| **General** | Limited impact if leaked, but still managed | Static road attributes, bus route/stop info, aggregate stats (no person/vehicle), equipment register, weather | Basic: access control, logging |

**Classification steps:**
1. Inventory all data assets (from Phase 2)
2. Tag a preliminary security grade per dataset
3. Working Group review (esp. core/important vs general boundary disputes)
4. Legal / compliance review (ensure compliance with data-security & sector rules)
5. Steering Committee approval
6. Publish the formal *Data Classification & Grading List* as a policy document

### 5.2 Access-Control Strategy

**Least-privilege implementation:**

| Role | Scope | Type | Approval |
|------|-------|------|----------|
| Data analyst | General + masked important (own unit) | Read-only | Unit head |
| Data engineer | All data (incl. raw important, excl. core) | Read/write | Info Center head |
| Data steward | All data in owned domain | R/W + manage | Info Center + unit dual approval |
| AI modeler | Masked training data | Read-only | Info Center head + Gov PM |
| External partner | General data only via API | Read-only + rate-limit | Info Center head + legal |
| Supervising authority | Per data-sharing agreement | Per agreement | Per sharing policy |

### 5.3 Data-Masking Rules

**Common transport data-masking table:**

| Type | Raw example | Method | Masked example |
|------|-------------|--------|----------------|
| License plate | CA 1ABC234 | Partial mask (keep 1st & last) | CA ***4 |
| Face image | (face image) | Gaussian blur / pixelate | (blurred) |
| National ID | 11010519900307XXXX | Mask middle 10 | 1101**********XXXX |
| Phone | +1-415-555-2678 | Mask middle 4 | +1-415-***-2678 |
| Precise coordinates | 120.155070, 30.274150 | Reduce precision | 120.155, 30.274 |
| Vehicle VIN | 1HGCM82633A123456 | Mask last 6 | 1HGCM82633A****** |
| Toll card | 6217001234567890123 | Mask middle | 6217***********0123 |
| Home address | 128 Main St, Apt 502 | Keep to district only | Central District, [redacted] |

**Masking implementation advice:**
- Store raw data in production (strong access control + audit)
- Use masked data in dev / test / analytics environments
- Data APIs mask by default on output (unless specially approved)
- Implement masking as an automated engine in the data-service layer (not manual)

### 5.4 Compliance Checklist

**Data-security regulation compliance:**
- [ ] Data-security management policy established?
- [ ] Data classified & graded?
- [ ] Data-security owner & body designated?
- [ ] Risk assessment of data activities performed (esp. important-data processing)?
- [ ] Data-security incident response plan established?
- [ ] Staff trained on data security?
- [ ] Cross-border transfer (if any) passed security assessment (e.g., GDPR Chapter V)?
- [ ] Data-security audit mechanism established?

**Personal-data protection compliance (if processing personal data):**
- [ ] Valid legal basis / consent obtained?
- [ ] Personal-data protection policy & notice published?
- [ ] Data-subject rights (access / rectify / erase) provided?
- [ ] Privacy / DPIA impact assessment performed?
- [ ] Personal-data protection officer designated?
- [ ] Enhanced measures for sensitive personal data?
- [ ] Personal-data breach reporting mechanism established?

**Critical-infrastructure (CII) compliance (if applicable):**
- [ ] CII identified (e.g., signal control / command systems)?
- [ ] Dedicated security body established?
- [ ] Security testing & risk assessment at least annually?
- [ ] Emergency drills at least annually?
- [ ] Incident reporting deadline met (major event within 30 min)?
- [ ] Procured network products/services passed security review?

---

## Appendix A: Data-Governance Maturity Self-Assessment

| Dimension | Initial (L1) | Departmental (L2) | Organizational (L3) | Quantified (L4) | Leading (L5) | Current |
|-----------|--------------|--------------------|----------------------|-----------------|--------------|---------|
| Org & policy | No dedicated mgmt | Part-time data mgmt | Committee + dedicated stewards | In KPI, regular audit | Data-driven culture | |
| Asset mgmt | No catalog | Some system docs | Full catalog, dict covers core | Automated catalog + lineage | AI-driven active metadata | |
| Standards | No unified standard | Some system naming | Org-wide standard published | Standard adoption >90% monitored | Industry-standard contributor | |
| Quality | Discovered via complaints | Some system checks | Org-wide rules + monitoring | Auto-monitor + active fix | Quality prediction (AI risk) | |
| Security | No classification | Basic access control | Formal classification + access approval | Automated masking + behavior audit | Zero-trust + data-security AI | |

---

## Appendix B: Stakeholder Communication Templates

**5-minute pitch to the executive on first reporting data governance:**
> "Leader, we want to launch data governance. Simply put — we have XX IT systems from XX vendors, data doesn't interoperate and quality varies. Now we're building the ITS platform / AI signal control; if the data foundation is weak, the best upper-layer apps are castles in the air. I suggest half a year, three things first: one, build the organization (assign people to own data); two, take inventory (what data we have, what's good/bad); three, set standards (unified coding & naming). No big budget needed — just cross-department cooperation."

**3-minute pitch to a business-unit head:**
> "Data governance isn't IT's job; it helps your unit use its own data. For example, your daily transport-operations report — if data auto-aggregates, that's at least 2 FTE saved. The 'this system's data is wrong' problem is exactly what governance solves. What we need is simple: name a business-savvy person as data liaison, ~half a day per week."

**1-minute pitch to front-line staff:**
> "You're all annoyed by duplicate entry and mismatches, right? We're doing data governance to untangle those messy sources, so you hand-key fewer forms, call less for data, and stop being an Excel mover."

---

## Appendix C: Quick Win Identification

**Data-governance Quick Wins (visible in 3 months):**

| Quick Win | Effect | Investment | Influence |
|-----------|--------|------------|-----------|
| Unified intersection-coding standard | Multi-system intersection data finally matches | Low (coordinate + issue) | High (fixes long-standing silos) |
| Publish first batch of data catalog | Exec finally knows "what data I have" | Low (Excel) | High (visible governance output) |
| Fix Top 3 data-quality issues | Most painful bugs fixed systematically | Medium (vendor coordination) | High (instant trust) |
| Build data-quality monitoring dashboard | Exec sees "what level quality is at" | Medium (dev resources) | High (visual drives improvement) |
| Auto-aggregate crash data | Was 3-day manual, now real-time | Medium (interface emergency services) | High (instant labor saving) |

---

## Appendix D: Resistance Management

**Common resistance & responses:**

| Resistance | Source | Response |
|-----------|--------|----------|
| "The data is ours" | Unit unwilling to share | Build a "data-sharing responsibility list" (issued by Steering Committee, defining each unit's mandatory shares); separate "data ownership" from "data-sharing obligation" |
| "No time to cooperate" | Unit already busy | Put in KPI; start stewards at 30%, not 100% |
| "Our system is too old to change" | Legacy tech debt | Don't change source first — build governance platform doing quality checks & cleaning at the data exit |
| "Who's responsible if something breaks after change" | Vendor fears instability | Use bypass / mirror to get data — don't intrude source (at least initially) |
| "Where does governance money come from" | Finance | Run the numbers: how much labor waste & bad decisions cost yearly from poor data |
| "This is another IT thing, nothing to do with us" | Business unit | Co-define quality rules with business — not IT defines rules, business says "I require this data" |
| "Governance is endless, when does it end" | Executive | Phase delivery: Phase 1 (3 mo) = catalog + Top 3 fixes; Phase 2 (6 mo) = standards + quality monitoring; continuous |

---

> **Legal notice**: This playbook is protected under applicable copyright law. Without the author's written authorization, no commercial use is permitted (including resale, bundling, commercial training, or SaaS-ification).
> **Disclaimer**: The methodology herein is for learning reference only and does not constitute professional advice of any kind. Data-security compliance should be advised by licensed legal professionals.
> **Author**: yinjianheng (Yin Jianheng) | yinjianheng@foxmail.com | WeChat: YJH-yinjianheng
