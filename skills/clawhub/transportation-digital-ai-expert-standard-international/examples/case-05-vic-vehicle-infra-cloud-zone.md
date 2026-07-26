# Case 05: A Vehicle–Infrastructure–Cloud (VIC) Pilot Zone

## Case Overview

| Dimension | Detail |
|-----------|--------|
| Project name | C-ITS Pilot Zone in a metropolitan technology region |
| Zone area | 30 km² |
| Road length | 85 km arterial + 120 km collector = 205 km |
| Total investment | €62 million (50% public, 50% industry) |
| Delivery period | 2021–2023 (three years) |
| Policy status | Among the first cohort of EU C-ITS / cooperative-ITS deployment zones |
| Operator | Regional development agency + regional smart-mobility company |

---

## 1. Background: Seizing the Connected & Automated Mobility Lane

### 1.1 A Continental Opportunity

The EU ITS Directive 2010/40/EU and the subsequent C-ITS deployment framework promoted cooperative intelligent transport systems. The member state launched a national call for C-ITS deployment zones, co-funded under the Connecting Europe Facility (CEF).

The technology region — ranked among the top EU tech hubs — hosts 3 OEMs (incl. a 300k-unit/yr EV plant) and 12 Tier-1 suppliers; automotive output is 45% of regional GDP. Winning a C-ITS zone would create a "manufacturing + smart mobility" dual engine.

### 1.2 Bid and Award

The region formed a bid consortium chaired by the agency director, with a technical university, a national research institute, and two global ITS suppliers. After 3 months of preparation (technical concept, use cases, business model), it was selected in the first cohort of 16 zones — the only one in its member state.

---

## 2. Build Content

### 2.1 Overall Architecture: "1+3+N"

- **1 cloud-control platform:** city-level VIC cloud-control foundation
- **3 regional MECs:** edge compute at three core intersections clusters
- **N use cases:** 15 V2X/C-ITS use cases + commercial pilots

### 2.2 Infrastructure Deployment

**Roadside sensing (200+ nodes):**

| Device | Qty | Coverage | Unit cost (€k) |
|--------|-----|----------|----------------|
| Millimeter-wave radar | 260 | Every signalized intersection (both ways) + crash-blackspots | 35 |
| HD AI camera | 420 | 4 directions per signalized intersection | 18 |
| Lidar | 85 | Key intersections + school zones + blackspots | 150 |
| Edge compute (MEC) | 120 | Shared every 2–3 intersections | 120 |
| Roadside unit (RSU) | 150 | ETSI ITS-G5 / C-V2X PC5; all 94 signalized intersections + 56 key segments | 80 |

**Communications:**
- 5G: 25 new/upgraded base stations, SA full coverage in zone
- Fiber: 85 km new along arterials to all RSUs/MECs
- Latency: RSU–MEC <5 ms, MEC–cloud <20 ms

**HD map & positioning:**
- Full-coverage HD map (absolute <20 cm, relative <10 cm)
- 3 GNSS augmentation (PPP-RTK) stations for cm-level dynamic positioning

**Cloud-control platform:**
- Deployed on the regional public-services cloud (elastic)
- Core: sensor fusion, traffic prediction, cooperative decision, V2X message distribution, data management
- 8 TB/day processed; 100k msgs/sec V2X capacity

### 2.3 Fifteen Use Cases

| # | Class | Use case | Technique | Effect |
|---|-------|----------|-----------|--------|
| 1 | Safety | Intersection collision warning | RSU broadcasts signal + surrounding-vehicle info | −40% intersection crashes |
| 2 | Safety | Vulnerable-road-user warning | Lidar detection + VRU trajectory prediction | −55% conflicts |
| 3 | Safety | Emergency-vehicle priority | Green wave auto-triggered on dispatch | −35% EV travel time |
| 4 | Efficiency | Green-wave speed guidance | Optimal speed from signal countdown | −30% stops |
| 5 | Efficiency | Dynamic lane management | Lane function by real-time demand | +10% throughput |
| 6 | Efficiency | Adaptive signal control | Multi-intersection AI coordination | −22% delay |
| 7 | Info | Ahead congestion/crash warning | Roadside + vehicle-reported detection | −85% secondary crashes |
| 8 | Info | Adverse-weather warning | Roadside weather station + V2X | −30% weather crashes |
| 9 | Service | Autonomous shuttle | 5 fixed routes, L4 | 2,000+ rides/day |
| 10 | Service | Delivery robots | 20 units (two logistics platforms) | 30 communities, 3,000 orders/day |
| 11 | Service | Automated valet parking (AVP) | 3 large parking facilities | −80% search time |
| 12 | Mgmt | Automated road-defect inspection | Bus-mounted AI cameras | 10× inspection efficiency |
| 13 | Mgmt | Construction-truck supervision | Geo-fence + V2X violation alert | −90% illegal dumping |
| 14 | Innovation | Digital-twin traffic simulation | Zone-wide twin for decisions | +50% decision efficiency |
| 15 | Innovation | Carbon-credit trading | V2X-guided eco-driving → tradable credits | ~1,200 t CO₂/yr saved |

---

## 3. Five-Ministry Coordination — the Hardest "Non-Technical" Challenge

C-ITS deployment is jointly advanced by multiple ministries; coordination complexity exceeded expectations:

| Ministry | Mandate | Core interest | Coordination friction |
|----------|---------|---------------|------------------------|
| Economic affairs / industry | Lead, industry promotion | Boost local CAM industry | Focus on industry, not field outcomes |
| Transport (road authority) | Road infrastructure, safety | Safety, liability clarity | Wary of AV-induced risk |
| Interior / police | Traffic law, security | Safety, incident liability | Concern over new crash liability |
| Digital / telecom | Comms standards | Standards compliance | Awaits EU roadside-infra standards |
| Spatial planning | Geodata, HD maps | Geodata security, privacy | HD-map geodata handling, GDPR |

### 3.1 Coordination Framework

The agency established a "1+5+N" framework:
- **1:** deputy minister as convenor
- **5:** the five ministries' vice-directors as standing members
- **N:** enterprises / research bodies per agenda

**Key mechanisms:** bi-weekly coordination meetings; a "problem express lane" (cross-ministry issues on the table within 24 h); KPI-linked performance appraisal.

### 3.2 Three Typical Cases

**Case 1 — HD-map geodata handling (spatial planning vs industry):** National geodata law requires obfuscation of commercial HD maps. OEMs reported 5–10 m random error after obfuscation, harming L4 safety.
*Resolution:* after 5 months, a compromise — public roads use the compliant obfuscated map; test corridors may apply for temporary raw-accuracy permits with confidentiality controls (no map data may be uploaded off-vehicle).

**Case 2 — AV accident liability gap (interior vs transport):** No clear liable party (owner? supplier? roadside operator?) under existing traffic law.
*Resolution:* with courts and justice, issued a *Pilot-Zone AV Test Accident Handling Guideline* establishing three-tier liability: system failure → supplier; erroneous roadside info → operator; supervisor/driver negligence → human. A mandatory AV test-data reporting platform was built.

**Case 3 — Inconsistent build standards (digital vs industry):** Roadside MEC/RSU dimensions varied; the road authority required unified pole standards before mass install.
*Resolution:* industry + suppliers issued a *Pilot-Zone Roadside Smart-Infrastructure Installation Spec* (pole interface, power, comms, thermal), approved by the road authority as a regional standard.

---

## 4. Technical Challenge: Cross-OEM Interoperability

### 4.1 The Worst Headache

C-ITS value hinges on vehicle–infrastructure–cloud interoperability. In practice, different OEMs' OBU implementations of ETSI ITS-G5 / C-V2X diverged, causing "roadside sends, vehicle doesn't receive or mis-parses."

The zone met interoperability issues across ≥5 OEMs and 3 chipset families:
- ASN.1 codec deviation from standard on one chipset
- Inconsistent coordinate handling in MAP/SPAT messages
- Divergent certificate schemes (self-signed vs trial CA)

### 4.2 Interoperability Test System

The zone invested €11M in a "C-ITS interoperability lab":
1. Standardized test cases (covering ETSI Day-1 messages: CAM, DENM, MAP, SPAT, IVI)
2. Automated toolchain — any new OEM OBU must pass 146 interoperability tests before onboarding
3. An "interoperability knowledge base" of all resolved cases

Over 18 months, V2X message delivery success rose from 62% to 97.8%.

---

## 5. Business-Model Exploration

### 5.1 "Build-first-use-later" vs "Use-driven-build"

Initial skepticism: "€62M of hardware — who uses it, how to recover?"

Decision: "use-driven build" — infrastructure and commercial operation advance together.

### 5.2 Five Commercial Paths

| Path | Model | Progress | Annual revenue (2023) |
|------|-------|----------|------------------------|
| Autonomous shuttle | Public-procured service | 5 routes | €7M (public purchase) |
| Delivery robots | Platform fee (€0.5/order) | 20 units, 3,000/day | €0.75M |
| AVP | Parking-operator fee (€3/space/month) | 3 facilities | €0.25M |
| V2X data service | OEM/map-provider fee (per call) | 2 OEMs, 1 map co. | €1.7M |
| CAMS test service | Test-track rental + certification | 8 OEMs | €6.3M |
| **Total** | — | — | **≈€15.9M** |

**Frankly:** revenue far short of investment (€62M; optimistic ROI ~2.5%). But the main value is not direct revenue:
1. **Industry pull:** attracted 4 CAM enterprises to set up R&D/test bases; ~€420M co-investment expected in 3 yrs
2. **City-brand uplift:** the "C-ITS pioneer" brand brought clear premium in investment promotion
3. **Talent stock:** a 300+ person CAM talent pool

---

## 6. Outcomes

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Road sensing coverage | 12% (legacy video only) | 100% (multi-source) | +88pp |
| RSU-covered intersections | 0 | 94 (100% of signalized) | full |
| V2X daily messages | 0 | 220k | — |
| AV open roads | 0 | 85 km | — |
| AV shuttle rides | 0 | 600k/yr | — |
| Zone traffic efficiency | baseline | +12% | shorter travel |
| Intersection safety events | baseline | −40% | collision warning |
| 5G coverage | 45% | 100% | +55pp |
| New CAM enterprises | — | 12 | — |
| Induced investment | — | €450M (3 yrs) | — |

---

## 7. Lessons

1. **Inter-ministerial governance is the key to success:** harder than technology. The "1+5+N" framework + KPI linkage worked; build such governance at bid time.
2. **Interoperability: standard first or product first?** Standards need real products to "wear in." The zone's lab fed into the EU C-ROADS interoperability methodology.
3. **"Use-driven build" beats "build-first-use-later":** the 15 use cases advanced with infrastructure, making build more precise.
4. **Business model still needs exploration:** rely on public funding + industry pull for now; each zone should pilot 1–2 closed-loop commercial use cases (delivery, AVP).
5. **Safety redundancy is non-negotiable:** V2X is unreliable (loss, jitter); on-board systems must not depend solely on roadside messages. Follow "roadside assists, on-board decides."
6. **Public experience is the best promotion:** the free AV shuttle (2,000+ rides/day) is the most powerful public-education tool. Every zone should offer ≥1–2 free citizen experiences.

---

*Case authored: June 2024 | Sources: pilot-zone acceptance report, operations annual report, independent evaluation*
