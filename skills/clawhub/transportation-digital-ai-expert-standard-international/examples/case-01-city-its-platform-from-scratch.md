# Case 01: Building a City Intelligent Transportation Management Platform from the Ground Up

## Case Overview

| Dimension | Detail |
|-----------|--------|
| City type | Mid-sized European city (Antwerp metropolitan area, Belgium) |
| Population | ~1.2 million metro (530,000 in the city core) |
| Signalized intersections | 680 |
| Registered vehicles | ~700,000 (growing ~3% per year) |
| Legacy traffic system | Legacy UTC controllers with semi-actuated local control; no integrated ATMS |
| Total investment | €110 million (over three years) |
| Delivery period | 2021–2023 (three phases across three years) |
| Core objective | Stand up a city-scale Intelligent Transportation Management Platform (ITMP) delivering adaptive signal control, real-time situational awareness, and multi-agency emergency coordination |

---

## 1. Background and Pain Points

### 1.1 The State of Urban Mobility

The City of Antwerp (a pseudonymized composite drawn from a real mid-sized European metropolitan program) sits at the heart of a major port and logistics region. By the end of 2020 the city core held roughly 530,000 residents and ~700,000 registered vehicles, growing at about 3% annually. The metropolitan road network carried 680 signalized intersections, of which roughly 40% (272) still ran fixed-time, isolated control with no network coordination. The remaining 408 intersections were connected to a legacy Urban Traffic Control (UTC) system, but most operated in semi-actuated, manually tuned mode.

### 1.2 Core Pain Points

**Three problems kept city leadership awake at night:**

1. **Pervasive peak-hour congestion.** Average central-business-district (CBD) speeds during the morning and evening peaks fell to 18 km/h, dropping below 10 km/h on the busiest commercial corridors. The municipal 311/contact-center logged more than 300 mobility complaints per month.

2. **Slow incident response.** From call-taking to on-scene response, the average incident clearance time was 28 minutes, creating elevated secondary-crash risk. The traffic operations center (TOC) dispatched crews mainly by two-way radio, with no visual common operating picture.

3. **Severe data silos.** The police traffic department, the mobility/transport authority, the public-works department, and the regional spatial-planning agency each ran their own systems, none interoperating. Even within the traffic department, signal, ANPR (automatic number-plate recognition), enforcement, and dispatch systems were isolated islands.

### 1.3 The Turning Point

In October 2020, city leadership received a dedicated briefing on urban congestion governance and directed: *"Study the advanced programs of leading cities, and solve our mobility problems with digital means."* A Smart Mobility Steering Committee chaired by the Deputy Mayor for Mobility was formed, and a feasibility study for a city-scale Intelligent Transportation Management Platform (ITMP) was launched.

---

## 2. T-DMM Diagnosis and Blueprint Design

### 2.1 T-DMM Maturity Diagnosis

An independent consortium applied the **Transport Digital Maturity Model (T-DMM)** to benchmark the city. Results:

| Assessment dimension | Score (out of 5) | Level | Key finding |
|---------------------|------------------|-------|-------------|
| Sensing infrastructure | 1.8 | L1 | Field-device coverage below 40%; intelligent video analytics <5% |
| Data governance | 1.2 | L1 | No unified data standard; poor quality; >30% missing data |
| Algorithm capability | 0.5 | L1 | No in-house AI team; signal timing relied on manual experience |
| Business applications | 1.5 | L1 | Only basic signal control and enforcement; low intelligence |
| Infrastructure | 2.0 | L2 | Server room adequate, but no cloud compute capacity |
| Organization capability | 1.0 | L1 | No dedicated data/technology team; outsourced maintenance |
| **Composite** | **1.3** | **L1–L2** | Early stage of digitalization |

### 2.2 Three-Year Blueprint

Based on the T-DMM diagnosis, the program adopted a "three-step" roadmap:

**Phase 1 (2021): Build the foundation**
- Network-enable 120 priority intersections + pilot AI signal optimization
- Cloud upgrade of the traffic data center (private cloud)
- Unified data hub (consolidating police, mobility authority, and transit data)
- Situational-awareness wall (Mobility Operations Coordination Center 1.0)
- Budget: €36 million

**Phase 2 (2022): Build the platform**
- Network-enable the remaining 560 intersections + citywide AI signal optimization
- Core ITMP (pan-sensing, analytics, signal optimization, dynamic messaging)
- Regulated-fleet supervision (coaches, hazardous-goods, construction vehicles)
- Public mobility information service
- Budget: €45 million

**Phase 3 (2023): Optimize operations**
- Citywide digital twin
- Continuous AI signal-optimization iteration (deep reinforcement learning)
- Emergency coordination (police / fire / medical)
- Emissions monitoring and green-mobility analytics
- Institutionalize O&M operating model
- Budget: €29 million

---

## 3. Implementation

### 3.1 Step 1: Signal Controller Network Enablement

**Technology selection**

The program faced a key decision: retain the legacy UTC protocol or migrate to a modern, open-controlled architecture. After evaluation it chose open-standard controllers with a unified signal-control platform because:
- The legacy system was closed, with limited APIs that prevented an AI optimization loop
- Open controllers support **NTCIP 1202 / 1209 / 2110** and **ISO 14827 (DATEX)** profiles, interoperating across multi-vendor field equipment
- Local/EU service response was fast — faults attended within 30 minutes

Siemens Mobility was selected as the signal-system integrator; 120 intersections were fitted with intelligent controllers supporting multi-source detection (inductive loop, video, radar).

**Implementation difficulties and responses**
- **Difficulty 1 — Construction traffic management.** Working 120 intersections simultaneously was highly disruptive.
  - *Solution:* "Night works + daytime restoration" with each intersection completed within 3 days, plus temporary portable signals.
- **Difficulty 2 — Infrastructure gaps.** 18 intersections lacked stable power; 12 lacked fiber backhaul.
  - *Solution:* Coordinated with the utility for capacity upgrades and deployed 4G/5G wireless modules as fiber backup.

### 3.2 Step 2: AI Signal Optimization

**Algorithm approach**

A three-layer optimization architecture:
1. **Isolated adaptive:** dynamic green-time adjustment from real-time flow
2. **Corridor coordination:** green-wave optimization via deep reinforcement learning
3. **Area-wide coordination:** multi-agent reinforcement learning across the network

**Key innovations**
1. **Multi-source data fusion for timing:** fusing ANPR, enforcement, floating-car GPS, and map-provider data (TomTom/HERE APIs) to build a full-sample OD matrix
2. **Human-in-the-loop closed loop:** AI proposes timing plans; an experienced traffic engineer reviews and approves; approved plans auto-deploy; effects are measured and the model iterates — "AI generate → human review → auto-deploy → evaluate → retrain"

**Results after 6 months on the 120-intersection pilot:**
- Average intersection delay −22%
- Green-wave corridor travel time −18%
- Peak-hour throughput +12%

### 3.3 Step 3: Mobility Operations Coordination Center

The Mobility Operations Coordination Center (MOCC) is the "visual window" of the ITMP, integrating police, mobility authority, transit agency, taxi, and ride-hail data across six modules:

1. **Situational awareness:** live flow and pedestrian heat maps, congestion index, incident distribution
2. **Signal optimization:** timing-plan management, effect evaluation, green-wave visualization
3. **Emergency command:** automated incident detection, unit dispatch, green-wave escort
4. **Regulated fleets:** real-time tracking and trajectory playback for coaches, hazmat, and construction vehicles
5. **Information release:** dynamic message signs (DMS), app, and SMS multi-channel dissemination
6. **Decision analytics:** automated weekly/monthly mobility reports and congestion-root-cause analysis

---

## 4. Outcomes (as of end of 2023)

| Metric | Before (2020) | After (2023) | Change |
|--------|---------------|--------------|--------|
| CBD peak average speed | 18 km/h | 21.2 km/h | +17.8% |
| CBD core peak speed | 9.5 km/h | 12.3 km/h | +29.5% |
| Peak congestion index | 1.85 | 1.38 | −25.4% |
| Average incident on-scene time | 28 min | 11 min | −60.7% |
| Signal-networked rate | 59% | 100% | +41pp |
| AI-optimized intersections | 0 | 680 (full coverage) | — |
| Monthly mobility complaints | 320 | 145 | −54.7% |
| Mobility data sources integrated | 3 | 12 | +300% |

---

## 5. Lessons Learned

### 5.1 Success Factors
1. **Top-level commitment:** The decision-maker chaired the program; the Deputy Mayor reviewed progress monthly, driving efficient cross-agency coordination.
2. **Diagnose before you build:** The T-DMM diagnosis objectively framed the baseline and avoided "blind project launching."
3. **Small-steps, fast-wins strategy:** Pilot 120 intersections first, prove the effect with data, then scale citywide.
4. **Data-driven decision making:** Every optimization result was evidenced with data and reported to leadership via a performance dashboard.
5. **Ecosystem partnership model:** Core platform kept under sovereign control; AI algorithms co-developed with a university lab; O&M outsourced to local SMEs.

### 5.2 Pitfalls
1. **Data quality was underestimated.** Initial plate-recognition accuracy was only 82% and GPS drift was severe; ~4 months were spent lifting data quality to usable levels.
   - *Lesson:* Budget 25–30% of the program for data governance — non-negotiable.
2. **Departmental silos are harder than technology.** The mobility authority initially resisted sharing bus and taxi data; two months of coordination plus the Deputy Mayor's direct push were required.
   - *Lesson:* Data sharing is an institutional and governance problem, not a technical one. Establish a citywide mobility-data governance charter defining "who provides, who is accountable, who uses, who benefits."
3. **AI is not a silver bullet.** The first signal-optimization model performed poorly in rain and holiday scenarios due to sparse training data.
   - *Lesson:* AI needs continuous iteration; at least one year of data accumulation is required to cover scenarios. Start with "AI-assisted + human decision," gradually transitioning to AI autonomy.
4. **O&M was forgotten.** Post-acceptance, the O&M team shrank from 15 to 5 and failure rates rose noticeably.
   - *Lesson:* Define a 3–5 year O&M budget at launch (typically 15–20% of build cost per year) and fold it into recurring appropriations.

### 5.3 Advice for Peer Cities
1. **Don't aim for "everything at once":** A mid-sized city need not benchmark against a mega-city "transportation brain"; first solve the most painful problems — signal optimization and incident response.
2. **Prefer open, standards-based solutions:** Better value, stronger service, and resilience against supply-chain shocks.
3. **Retain talent:** Staff at least 3–5 in-house engineers rather than fully outsourcing.
4. **Establish a data-sharing governance framework** before launch via a public-sector charter.
5. **Reserve room for iteration:** Keep the architecture open for future capabilities (LLMs, V2X/C-ITS).

---

## 6. Key Data

| Item | Figure |
|------|--------|
| Daily platform data throughput | 230 million records |
| AI timing plans generated per day | 5,000+ |
| Concurrent platform users | 200+ |
| Automated incident detections per day | 1,200+ |
| Green-wave corridors | 42 (68 km total) |
| Citizen mobility app registrations | 320,000 |
| Investment payback period | ~3.5 years (estimated from congestion-reduction economic benefit) |

---

*Case authored: March 2024 | Sources: project acceptance report, independent evaluation report*
