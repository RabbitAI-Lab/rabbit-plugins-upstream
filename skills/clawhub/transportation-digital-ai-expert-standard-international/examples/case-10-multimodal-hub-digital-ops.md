# Case 10: Digital Operations of a Multimodal Transport Hub

## Case Overview

| Dimension | Detail |
|-----------|--------|
| Hub type | High-speed rail + metro + bus + taxi/rideshare + private vehicle intermodal hub |
| Location | Major European metropolitan sub-center |
| Scale | 520,000 m² GFA (rail hall 180,000 m² + ancillary 340,000 m²) |
| Daily passengers | Design 500k/day (recent actual ~350k; long-term 500k) |
| Modes | HSR (4 platforms / 8 tracks), 3 metro lines, 28 bus routes, 16 taxi ranks |
| Digital investment | €25 million (2.25% of €1.1B total) |
| Delivery period | 2019–2022 (civil + digital built in parallel) |
| Operator | Hub management company (rail authority + transport agency + metro + commercial JV) |

---

## 1. "Digital From the First Day of Design"

### 1.1 An Unusual Decision

In 2020, during the hub's design phase, leadership decided: "This hub should be digital from day one — no bolting IT on after construction." Concretely, BIM became a *contractual deliverable* equal to detailed design drawings — the first time in the region's hub program that BIM was written into the EPC contract.

### 1.2 The Hub's Complexity

- **Multiple principals:** rail (national operator), metro (3 lines, 2 operating companies), bus (2 companies), taxi, rideshare, private vehicles, 200+ commercial tenants, property management — at least 8 independent operators
- **High-density crowd flow:** design 500k/day; peak simultaneous crowd 35,000
- **Large volume:** 4 underground levels (deepest −32 m), 5 above; indoor navigation far harder than ordinary buildings
- **Safety-sensitive:** security, fire, mass-evacuation requirements extreme

---

## 2. Digital System Panorama

"1 foundation + 8 applications": one data foundation (BIM + CIM + IoT digital twin), eight smart applications.

### 2.1 BIM Digital-Twin Foundation (€5.3M)

**Build phase (2019–2022):**
- Design BIM (LOD300) → construction BIM (LOD400) → as-built BIM (LOD500)
- All disciplines (arch, struct, MEP, fit-out)
- BIM as the sole coordination basis — clash detection resolved 5,200+ conflicts pre-construction, avoiding >€110M rework

**Operations phase (2022+):**
- As-built BIM → operational digital twin, fused with 12 classes / 38,000 IoT points
- Integrated with GIS into CIM, linking hub to 3 km² of surrounding city
- Live data: passenger flow, equipment status, environment (temp/CO₂/PM2.5), energy, security, fire

### 2.2 Passenger-Service Applications (4 subsystems)

**(1) AI Crowd Prediction & Control (€1.7M)**

| Input | Target | Window | Accuracy |
|-------|--------|--------|----------|
| HSR timetable + booking data | Rail arrivals | 1–4 h | MAPE <8% |
| Metro gate data | Metro↔rail transfers | 30 min | MAPE <12% |
| History + weather + calendar | Composite flow | 24 h–7 d | MAPE <15% |
| Video AI live count | Zone density | real-time | >95% |

**Control triggers:**
- >80% capacity → Level-3 alert (more staff)
- >95% → Level-2 (flow control: close some entrances, lengthen security wait)
- >110% → Level-1 (metro skip-stop, rail inflow limit)

**(2) AR Indoor Navigation (€0.85M)**
- App: AR live navigation ("point camera, see arrow + distance")
- Covers halls, concourses, platforms, transfer corridors, retail, parking
- "To platform X" → optimal route considering live crowding, elevator status
- 8,000+ daily navigation requests

**(3) Multimodal Transfer Optimization (€1.1M)**
1. **Timetable coordination:** ensure ≥1 metro line + 2 bus routes running when last HSR arrives (auto-detect gaps)
2. **Dynamic transfer guidance:** reroute when a corridor crowds
3. **Taxi/rideshare matching:** predict taxi demand 30 min after HSR arrival; push to taxi/rideshare platforms
4. **Transfer-time estimate:** live "to rail gate ≈ X min" at each mode entrance

**(4) Accessibility Service (€0.4M)**
- Visually impaired: app voice nav + Bluetooth beacons (2–3 m)
- Wheelchair: app-booked accessible route + priority elevator
- Hearing impaired: video (sign-language) + text screens
- Seniors: large-font app + one-tap human help

### 2.3 Safety Management (€3.9M)

**(1) AI Video Analytics**

2,200+ HD cameras; traditional "watch screens" used <5% of video. AI delivered:

| Function | Spec |
|----------|------|
| Face recognition (watchlist) | Identify within 3 s of entry |
| Abnormal behavior | Run, gather, fall, fight, left-object, intrusion — 15 classes |
| Crowd-density heatmap | Updated every 5 s, 1 m² grid |
| Left-object | Unattended >3 min alerts |
| Fire-lane occupancy | >1 min alerts |
| Escalator anomaly | Reverse, fall, crowd → auto stop |

**(2) Evacuation Simulation & Live Guidance**
- Agent-based model (AnyLogic) simulating 35,000-person evacuation
- Live: actual distribution → optimal path → signs + app guidance
- Monthly drill: auto-generated bottleneck report

### 2.4 Energy Management (€1.4M)

| Strategy | Content | Saving |
|----------|---------|--------|
| Smart lighting | By crowd, daylight, time | −35% |
| HVAC optimization | By crowd heatmap | −20% |
| Elevator smart dispatch | Sleep/idle vs run groups | −15% |
| PV + storage | 1.2 MW roof PV + storage, peak arbitrage | 8% renewable |

**Annual saving:** ~9M kWh (≈€7.2M), ~3,800 t CO₂ cut.

### 2.5 Commercial Operations (€1.1M)
- **Crowd-heatmap rent pricing:** rent by actual footfall, not designed — shared with tenants
- **Tenant smart mgmt:** sales, conversion, energy, complaints online
- **Personalized recommendation:** by passenger profile (member + behavior), app offers; conversion 0.3% → 4.2%
- **Result:** year-1 commercial rent +23% vs forecast

---

## 3. The "Last Mile" from BIM to Operations

### 3.1 Information Gap — An Industry Disease

BIM is beloved in design/construction but operations teams often "can't read, won't use, don't trust" it — a "pretty model on a hard drive." The hub broke this:

1. **Operations embedded early:** ops reps in BIM review from design, ensuring ops-needed info (model, install date, warranty, manual links)
2. **"As-built = digital twin" standard:** acceptance required BIM complete, accurate, and "operable" (clickable equipment, queryable space)
3. **BIM-FM integration:** BIM ↔ facility-management system; locate equipment in 3D, view records, raise work orders
4. **Model lightweighting:** design GB-level → ops MB-level (keep ops info, drop design detail)

### 3.2 Ops Team's "Digital Awakening"

Initially, mostly 40+ traditional facility staff resisted: "We used Excel for 20 years — why learn this?" The turning point: a 2023 fire-main break — traditional locate/valve/shut would take 30 min; via the twin they located the pipe, viewed upstream/downstream valves, one-click shut plan — 5 min, avoiding ~200 m² of flooded retail.

**From then, "the digital twin is awesome" became their mantra.**

---

## 4. Multi-Stakeholder Governance

8 operators coordinating is the core challenge; silos and blame-shifting were the norm.

### 4.1 Joint Operations Center (JOC)

All operators staff the JOC:
- Seats: rail dispatch, metro dispatch, bus dispatch, taxi dispatch, property, security, duty GM
- Mode: routine per-line; emergencies unified (duty GM highest)
- Data: all shared to one platform (sensitive data masked)

### 4.2 Digital Coordination Tools

| Tool | Function | Effect |
|------|----------|--------|
| Event-mgmt platform | Any party reports (e.g., escalator fault) → all synced → traceable | Response 15→3 min |
| Shared situational board | All KPIs live (flow, punctuality, parking) | Transparency, less "why won't you cooperate" |
| Joint KPI | Combined KPIs (transfer efficiency, satisfaction), not siloed | Drives proactive collaboration |

---

## 5. Outcomes

| Metric | Design target | Actual | vs |
|--------|--------------|--------|-----|
| Transfer time (rail→metro) | ≤8 min | 5.5 min | −31.3% |
| Transfer time (rail→bus) | ≤12 min | 8.2 min | −31.7% |
| Flow prediction (1 h) | >85% | 92% | +7pp |
| Equipment response | <10 min | 3 min | −70% |
| Energy | baseline | −25% | — |
| Commercial rent | €21M/yr exp. | €25.5M/yr | +23.3% |
| Satisfaction | >4.0/5 | 4.6/5 | +0.6 |
| Safety | — | zero major incident | — |
| Evacuation drill | — | 8 min (35k) | — |
| BIM conflicts found | — | 5,200+ | avoided >€110M |

---

## 6. Lessons

1. **"Digital-native" beats "digital-patch":** embedding digital at design (BIM-in-EPC) added ~3% cost but cut digital-twin formation time >60% and lowered TCO. Applies to all new large hubs.
2. **BIM's life is in operations:** value is only 30% if it stops at design/construction. Real release is in operations — equipment, space, emergency. Contracts should include "operability" BIM-delivery standards.
3. **Multi-principal governance needs "physical concentration + data sharing":** a JOC alone is insufficient — after returning to offices, silos resume. Build shared data + event platform (institution + tool).
4. **AI video analytics: not "more is better":** 2,200 cameras all-AI means high GPU cost and false alarms. Use tiering — 200 security-sensitive streams always-on, others on-demand — saved ~40% compute.
5. **Don't ignore the elderly and the digital divide:** though 350k app users, ~20% (mostly seniors) don't use smartphones. Keep human desks, paper maps, public phones — "no passenger lost to the divide."
6. **Data-asset value is just emerging:** the hub's accumulated flow/equipment/operations data is the most precious digital asset. It now shares bidirectionally with the city ITMP — hub flow prediction helps the city pre-judge surrounding pressure, and city data helps the hub optimize external connections. This "hub–city" data synergy is the future of smart cities.

---

*Case authored: June 2024 | Sources: hub management annual report, BIM acceptance report, passenger-satisfaction survey*
