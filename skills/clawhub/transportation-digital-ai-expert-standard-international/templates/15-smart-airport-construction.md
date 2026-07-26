# Smart Airport Construction Proposal

> **Version**: V1.0
> **Date**: ____/__/__
> **Prepared by**: _________
> **Reviewed by**: _________
> **Approved by**: _________

---

## Executive Summary

### Project Positioning
The smart-airport program for [Airport Name] applies digital and intelligent technologies to raise operational efficiency, safety, passenger experience, and green/sustainable performance, supporting [Airport Name]'s ambition to become an [international / regional] aviation hub.

### Objectives
By [target year], achieve:
- **Flight regularity**: flight pushback/dispatch regularity ≥ ____%; A-CDM milestone compliance > ____%
- **Passenger experience**: end-to-end self-service + biometrics coverage > ____%; average queue time reduced by ____%
- **Operational efficiency**: stand utilization up ____%; baggage mishandling rate < ____%
- **Safety**: safety incidents reduced ____%; screening throughput up ____%
- **Green**: CO₂ per passenger down ____%; fixed-ground-power (FGP) usage > ____%
- **Non-aeronautical revenue**: retail / advertising / data-service revenue up ____%

### Investment Overview
| Item | Value |
|------|------|
| Total estimated investment | $____ million |
| Construction period | ____ months (in [two / three] phases) |
| Estimated annual operational benefit | $____ million / year |
| Payback period | ____ years |
| Financial IRR | ____% |

---

## 1. Airport Profile

### 1.1 Basic Information
| Item | Detail |
|------|------|
| Airport name | [Airport Name] |
| Reference code (ICAO) | [4F / 4E / 4D / 4C] |
| Runways | ____ ( [spec] ) |
| Terminal area | ____ ×10³ m² (T1 / T2 / ...) |
| Stands | ____ (contact ____ / remote ____) |
| Annual passengers | ____ million ( [year] data) |
| Annual cargo | ____ ×10³ tonnes |
| Annual movements | ____ ×10³ |
| Served destinations | ____ (domestic ____ / intl & regional ____) |
| Base carriers | [airline list] |
| Operating model | [group-managed / single-entity] |

### 1.2 Current Operations Assessment

#### 1.2.1 Operational Efficiency
| Metric | Current | Industry avg. | Benchmark | Rating |
|------|:------:|:------:|:------:|:----:|
| Dispatch regularity | __% | 85% | >90% | [excellent/good/fair/poor] |
| Avg. taxi time | __min | 18min | <15min | |
| Contact-stand utilization | __% | 75% | >85% | |
| Avg. security queue | __min | 10min | <5min | |
| Avg. baggage claim wait | __min | 15min | <10min | |
| Min. connection time (MCT) | __min | 90min | <60min | |
| Originating on-time door close | __% | 90% | >95% | |

#### 1.2.2 Existing Information Systems
| Category | System | Supplier | Year | Coverage | Health (1–5) |
|----------|----------|--------|----------|----------|:-----------:|
| AODB (airport ops DB) | | | | | |
| RMS (resource mgmt) | | | | | |
| FIDS (flight info display) | | | | | |
| BHS (baggage handling) | | | | | |
| BRS (baggage reconciliation) | | | | | |
| CUTE/CUPPS (check-in / DCS) | | | | | |
| SACS (security screening) | | | | | |
| CCTV | | | | | |
| PA (public address) | | | | | |
| Access control | | | | | |
| AODB / Gantt / charts | | | | | |
| A-CDM | | | | | |

---

## 2. Vision and Goals

### 2.1 Overall Vision
Build a "[adjective] smart airport" delivering a ____, ____, ____, ____ four-dimensional intelligent operations and service system.

### 2.2 Quantified Target Framework
| Dimension | Key metric | Baseline | Phase-1 | Phase-2 | Global benchmark |
|----------|----------|:------:|:------:|:------:|:------:|
| Efficiency | Dispatch regularity | | | | >92% |
| Efficiency | Contact-stand utilization | | | | >88% |
| Experience | End-to-end self-service ratio | | | | >80% |
| Experience | Security queue (min) | | | | <3min |
| Experience | MCT (min) | | | | <45min |
| Safety | Prohibited-item miss rate | | | | <0.01% |
| Safety | Runway / apron safety events | | | | 0 |
| Green | CO₂ per passenger (kg/pax) | | | | <2.0 |
| Green | FGP usage rate | | | | >95% |
| Coordination | A-CDM milestone compliance | | | | >95% |
| Value | Non-aero revenue share | | | | >50% |

---

## 3. Overall Architecture

### 3.1 Six-Layer Architecture
```
┌──────────────────────────────────────────────────────────────┐
│  Layer 6  User Experience                                      │
│  Airline/airport app | Mobile web | Website | Kiosks          │
│  Service robots | Call center                                     │
├──────────────────────────────────────────────────────────────┤
│  Layer 5  Business Applications                                │
│  A-CDM | Smart terminal | Smart apron | Smart baggage          │
│  Smart commercial | Smart security | Energy | APOC             │
│  Digital twin | Emergency command | Green airport | Data services│
├──────────────────────────────────────────────────────────────┤
│  Layer 4  Data & AI                                            │
│  Data lake | Data governance | AI/ML platform | Knowledge graph│
│  Passenger profile | Flight forecast | Resource optimization    │
│  Anomaly detection | BI decision support                        │
├──────────────────────────────────────────────────────────────┤
│  Layer 3  Convergence Platform                                 │
│  AODB 2.0 | IoT platform | Video-fusion | High-precision locating│
│  GIS/BIM | Unified messaging | Integration bus (ESB / API GW)    │
├──────────────────────────────────────────────────────────────┤
│  Layer 2  Communications Network                               │
│  Private 5G | Wi-Fi 6 | AeroMACS | L-band data link | Fiber    │
│  IoT access (LoRaWAN / NB-IoT) | Indoor locating (UWB / BLE)    │
├──────────────────────────────────────────────────────────────┤
│  Layer 1  Sensing & Actuation                                 │
│  Radar (SMR / MLAT) | Cameras | Sensors | Self-service        │
│  Gates | Biometrics | Baggage RFID | Fixed ground power        │
│  Vehicle locating | Drone detection | Met stations              │
└──────────────────────────────────────────────────────────────┘
```

### 3.2 Key Technology Selection
| Domain | Recommended | Alternative | Sourcing | Note |
|--------|----------|----------|:--------:|------|
| Comms | Private 5G + AeroMACS | Private LTE | Partial local | Subject to spectrum license |
| Locating | UWB + BLE + GNSS | Wi-Fi RTT | Local | Indoor-outdoor fusion |
| Biometrics | Face + iris + fingerprint | Palm vein | Partial local | Privacy compliance review |
| IoT | LoRaWAN + NB-IoT | Zigbee | Partial local | |
| AI/ML | GPU cluster + MLOps platform | Cloud AI services | Partial local | Data stays on-site |
| Digital twin | Unreal/Unity + GIS + BIM | Unity + GIS | Partial local | High-fidelity + real-time |

---

## 4. Subsystem Detailed Design

### 4.1 A-CDM (Airport Collaborative Decision Making)

#### 4.1.1 Overview
A-CDM is the core platform where airport, ATC, airlines, and ground handlers share operational information and make collaborative decisions, covering the full flight lifecycle (origin off-block → arrival → landing → taxi-in → turnaround → pushback → taxi-out → takeoff → departure).

#### 4.1.2 Milestone Management
| # | Milestone | Name | Time base | Data source | Alert rule |
|:---:|----------|:--------:|--------|----------|
| M1 | ATC flight plan activated | EOBT-3h | ATC/FMP | Alert if not activated |
| M2 | Origin off-block (EOBT-2h) | EOBT-2h | ACARS/ADS-B | Origin delay → downstream alert |
| M3 | Final approach | ALDT-30min | Radar/ADS-B | Auto-estimate TOBT |
| M4 | Landing (ALDT) | ALDT | Surface radar/ADS-B | Update TOBT |
| M5 | On-block (AIBT) | AIBT | Video AI / ground app | Abnormal taxi-time alert |
| M6 | Turnaround start | AIBT+5min | Ground app / sensor | Delayed-start alert |
| M7 | Jet bridge / stairs dock | AIBT+2min | Sensor / IoT | Abnormal-dock alert |
| M8 | Boarding | TOBT-30min | Gate system | Passengers-missing alert |
| M9 | Doors closed (ARDT) | ARDT | Gate / video | Door-close delay alert |
| M10 | Pushback (ASRT) | ASRT | Surface radar / ground app | Pushback-wait timeout alert |
| M11 | Takeoff (ATOT) | ATOT | Surface / en-route radar | Takeoff-delay alert |
| M12 | Handed to en-route | ATOT+15min | ATC | |

#### 4.1.3 A-CDM Intelligent Optimization
| Scenario | AI model | Inputs | Expected effect |
|----------|--------|----------|----------|
| TOBT auto-forecast | Time-series + LSTM/Transformer | Origin off-block + en-route weather + taxi time | TOBT accuracy >90% |
| Dynamic stand allocation | Combinatorial + RL | Schedule + aircraft type + delay + preference | +10% contact-stand use |
| De-icing scheduling | Queueing + real-time opt. | Weather + flights + pads + trucks | +20% de-icing throughput |
| Mass-delay recovery | Multi-agent + constrained opt. | Delayed flights + resources + crew + pax | −30% recovery time |
| Taxi-route optimization | Path planning + conflict detect | Surface radar + stand + runway | −10% taxi time |

### 4.2 Smart Terminal

#### 4.2.1 Biometric "Single Token Journey"
```
Booking ──→ Check-in ──→ Bag drop ──→ Security ──→ Gate wait ──→ Boarding ──→ Arrival
  │           │            │            │           │           │           │
  └───────────┴────────────┴────────────┴───────────┴───────────┴───────────┘
            Single biometric token links the full journey
         (face / iris / fingerprint / palm-vein, multi-modal fusion)
```

| Node | Function | Technology | Effect |
|------|------|------|------|
| Self check-in | Biometric enrol + bind flight | Kiosk + face capture | Check-in <1 min |
| Self bag-drop | Face + self-print tag + drop | RFID tag + face match | Drop <2 min |
| Smart security | Face verify + CT + AI + auto-lane | Face + CT + AI | +2× throughput |
| Self boarding | Face boarding | Face + gate reader | <5 s/pax |
| Arrival guide | Baggage + last-mile guidance | App + BLE + indoor nav | Better arrival UX |

#### 4.2.2 Smart Security
| Module | Technology | Effect |
|----------|----------|------|
| Self verification | Face + e-passport chip read | <3 s/pax |
| CT scanner | 3D tomography + auto EDS | Laptops / liquids stay in bag |
| AI image analysis | Deep learning + prohibited-item DB (>50 classes) | >95% accuracy |
| Centralized adjudication | Remote central + cross-confirm | −30–50% labor |
| Auto tray return | Auto return + clean + disinfect | Better UX |
| MMW body scanner | Contactless full-body scan | Safe + efficient + private |
| Smart bag search | AI-assisted search + knowledge graph | +40% efficiency |
| Lane smart scheduling | Real-time flow forecast + lane opening | −30% queue |

#### 4.2.3 Passenger Self-Service / Smart Service
| Service | Description | Location |
|------|------|----------|
| CUSS kiosk | With biometric enrol | Departure hall / metro / parking |
| SBD bag-drop | With RFID tag printing | Departure hall |
| Info robot | Flight / navigation / translate / info | Throughout terminal |
| Smart navigation | AR nav + indoor locating + accessibility | Whole terminal |
| Smart restroom | Occupancy + environment + auto-clean | Terminal restrooms |
| Smart retail rec. | Profile + location + time targeting | App / mobile web |
| Rest / sleep pod | Scan-to-use + smart control | Gate area |
| Share charge / Wi-Fi / wheelchair | Scan-to-rent | Public areas |

### 4.3 Smart Apron

#### 4.3.1 Stand Intelligence Allocation
| Goal | Constraints | AI method | Effect |
|----------|----------|--------|------|
| Max contact-stand use | Type / task / time / preference | Combinatorial + heuristic | +10% |
| Min walking distance | Terminal layout / connection | Graph optimization | Better transfer UX |
| Optimal disruption adjust | Delay / stand fault | Real-time replan | −80% manual adjust |

#### 4.3.2 Ground Service Management
| Activity | Smart solution | Technology |
|----------|----------|----------|
| Baggage load/unload | RFID tracking + loading monitor | RFID + video AI + load sensor |
| Refueling | Smart dispatch + quantity monitor | IoT + optimization |
| Catering | Smart dispatch + temp monitor | Cold-chain IoT + dispatch |
| Potable / waste water | Smart fill / extract dispatch | IoT + optimization |
| De-icing | Smart pad dispatch + fluid mgmt | Queueing + weather alert |
| Cabin cleaning | Smart scheduling + QA | Video AI + mobile app |
| Cargo load | Smart tally + ULD mgmt | RFID + barcode + AGV |
| Vehicle dispatch | Unified GSE dispatch | GPS/RTK + opt. + geo-fence |

#### 4.3.3 Apron Safety
| Domain | Smart solution |
|----------|----------|
| FOD detection | Fixed / vehicle FOD radar + vision AI |
| Vehicle collision | GSE GPS/RTK + geo-fence + collision warning |
| Runway incursion | SMR + ADS-B + video AI fusion |
| Bird strike | Avian radar + AI ID + deterrent linkage |
| Drone incursion | Drone detect + ID + counter-UAS |
| Personnel safety | Smart badge locating + zone auth + violation AI |

### 4.4 ATC Integration

#### 4.4.1 Airport–ATC Data Sharing
| Direction | Content | Technology | Effect |
|----------|----------|----------|------|
| ATC → Airport | Arrival/departure sequencing / flow / reason | SWIM / AIDC / FMTP | Airport anticipates ATC constraints |
| Airport → ATC | TOBT / AOBT / stand / de-ice status | SWIM / AIDC | ATC knows surface state |
| Joint | Mass-delay / CDM response | A-CDM platform | Collaborative efficiency |

#### 4.4.2 Remote / Digital Tower
| Function | Description | Use case |
|------|------|----------|
| Panoramic video stitch | Multi-HD 360° view | Replace/supplement physical tower |
| AR annotation | Flight no. / altitude / speed overlay | Enhanced situational awareness |
| IR / low-vis enhancement | Night / fog / rain-snow enhancement | All-weather ops |
| AI conflict detection | Runway / taxiway conflict auto-detect | Safety enhancement |

### 4.5 Smart Baggage

#### 4.5.1 Full-Journey Tracking
```
Drop ──→ Collect ──→ Convey ──→ Sort ──→ Load ──→ Underbelly ──→ Unload ──→ Convey ──→ Claim
  │        │         │         │        │        │        │         │         │        │
  └────────┴─────────┴─────────┴────────┴────────┴────────┴─────────┴─────────┘
              RFID + barcode auto-capture at every node
              → Passenger app shows live bag location
              → Airport / airline full monitoring, auto-alert on anomaly
```

#### 4.5.2 Smart Sorting
| Tech | Description | Effect |
|------|------|------|
| RFID tag | UHF RFID tag (printable / chip) | Read >99.9% (barcode ~95%) |
| Auto sorter | High-speed tray / cross-belt | >6,000 bags/h |
| Early baggage storage | Automated EBS | Fully automated store/retrieve |
| AI vision assist | OCR + shape detect | Reads soiled / occluded tags |
| Transfer handling | Auto ID + fast transfer | −30% transfer time |

#### 4.5.3 Baggage Exception Management
| Exception | Detection | Handling |
|----------|----------|----------|
| Delay | Abnormal RFID node time | Auto-alert + priority transfer |
| Misload | RFID check at load | Real-time alarm + intercept |
| Damage | Vision AI damage detect | Auto photo + record + claim |

### 4.6 Passenger Experience

#### 4.6.1 Mobility App
| Phase | Functions |
|----------|----------|
| Pre-trip | Search / compare / book / check-in / seat / bag / meal |
| Departure | Reminders / directions / parking nav + booking / live traffic / ETA |
| Terminal | Indoor nav / security queue / gate guide / retail rec. |
| Boarding | Boarding reminder / gate-change push / mobile boarding pass + face |
| In-flight | N/A |
| Arrival | Bag location / claim guide / last-mile / car rental / ride-hail / hotel |
| Service | Flight status / delay cert. / support / lost & found / feedback |

#### 4.6.2 Smart Commercial
| Function | Description | Technology |
|------|------|------|
| Targeted marketing | Profile + location + history rec. | Big data + ML |
| Smart duty-free | Online order + offline pickup + face pay | Cross-border + RFID |
| Smart F&B | Scan-order + smart locker + robot delivery | IoT + robot |
| Targeted ads | Profile-based dynamic ads | Digital signage + AI |
| Loyalty | Airport membership + points + benefits | CRM + data platform |

### 4.7 APOC (Airport Operations Center)

#### 4.7.1 Functional Architecture
```
                      APOC (Airport Operations Center)
                              │
    ┌─────────────┬─────────┬─┴───────┬─────────┬─────────────┐
    │             │         │         │         │             │
 Ops Monitor   Resource Disp.  Emergency   Info Publish   Analytics
    │             │         │         │         │             │
    ├ Flights    ├ Stands   ├ Plans    ├ AODB    ├ KPI dashboard
    ├ Pax service├ Gates    ├ Linkage  ├ Website  ├ Ops reports
    ├ Baggage    ├ Check-in ├ Drills   ├ App      ├ Trend analysis
    ├ Ground     ├ Bridges   ├ Replay   ├ Social   ├ Forecast/alert
    ├ Apron      ├ Vehicles  ├ Recovery ├ Screens  └ AI-assisted decisions
    └ Security    └ Staff    └ Recovery └ PA
```

### 4.8 Digital-Twin Airport

#### 4.8.1 Levels
| Level | Name | Content | Update | Precision |
|:---:|------|------|:--------:|:---:|
| L1 | Whole-airport | Runways + terminal + apron + airspace | Real-time | 1 m |
| L2 | Terminal | Depart / arrive / transfer / retail | Real-time | 10 cm |
| L3 | Apron | Stands / vehicles / equipment / pax / aircraft | Real-time | 1 m |
| L4 | Baggage system | Conveyor / sorter / carousel / EBS | Real-time | 1 cm |
| L5 | Equipment | FGP / jet bridge / elevator / HVAC / power | Near-real-time | 1 mm |

#### 4.8.2 Applications
| Scenario | Description | Value |
|------|------|------|
| Real-time status | All elements (aircraft / vehicle / pax / equipment / weather) mapped | Global control |
| Flow simulation | Peak / mass-delay / incident flow rehearsal | Scientific plans |
| Construction sim | Ops-while-constructing simulation + conflict detect | Safe construction |
| Carbon visualization | 3D emission source / sink / flow | Intuitive carbon mgmt |
| Emergency drill | Virtual fire / explosion / security drill | Low-cost + frequent |

### 4.9 Green Airport

#### 4.9.1 Carbon-Management System
| Module | Content | Standard |
|------|------|------|
| Emission monitoring | Per-zone / per-system / per-energy emission real-time | ISO 14064 / GHG Protocol |
| Carbon asset mgmt | Allowance mgmt + trading + neutrality pathway | ICAO CORSIA / EU ETS |
| Reduction measures | Renewables / efficiency / capture (long-term) | |

#### 4.9.2 Fixed Ground Power (FGP) — APU Alternative
| Equipment | Function | Coverage target | Plan |
|------|------|:----------:|----------|
| 400 Hz GPU | Replace aircraft APU power | 100% contact stands | by ____ |
| PCA pre-conditioned air | Replace aircraft APU HVAC | 100% contact stands | by ____ |
| Remote APU alt. | Mobile power / HVAC | >50% | by ____ |

#### 4.9.3 Other Green Measures
| Measure | Content | Effect |
|------|------|:------------:|
| PV power | [terminal / hangar / garage rooftop PV] | ____ MWh / yr |
| Ground power | Contact + remote full coverage | ____ t CO₂ / yr |
| New-energy GSE | [shuttle / stairs / baggage / guide electric] | ____ t CO₂ / yr |
| Smart lighting | [LED + smart control] | −40% lighting energy |
| Smart HVAC | [ice storage + VSD + AI] | −20% HVAC energy |
| Water mgmt | [rain harvest + reclaimed + smart irrigation] | −30–50% water |
| Waste mgmt | [sorting + aviation-waste smart handling] | −30% waste |

### 4.10 Safety and Emergency

#### 4.10.1 Protection System
| Domain | Content | Technology |
|--------|----------|----------|
| Terminal security | Entrance control / suspicious acts / items / persons | Face + video AI + access + X-ray |
| Apron security | FOD / runway incursion / vehicle collision / bird | FOD radar + video AI + SMR + avian radar |
| Perimeter security | Perimeter intrusion detection | Fiber vibration + thermal + radar + video AI |
| Cyber security | Ops / office / internet networks | IEC 62443 + defense-in-depth + SOC + zero-trust |
| Counter-UAS | Drone detect + ID + countermeasure | RF detect + radar + EO/IR + jam / capture |

#### 4.10.2 Emergency Command
| Module | Description |
|------|------|
| Digital plans | Plans for mass-delay / fire / explosion / hijack / severe weather / pandemic / earthquake |
| One-click linkage | Trigger → plan → resource → publish → evacuate |
| Resource mgmt | Real-time visible emergency supplies / equipment / staff / vehicles |
| Drills | Digital-twin virtual + live drills |
| Post-incident review | Full replay + analysis + improvement |

---

## 5. Phasing (Greenfield vs Brownfield)

### 5.1 Greenfield (New Airport)
| Phase | Time | Scope | Investment |
|------|------|------|:----:|
| 1 (Civil works) | ____ | [conduits / trays / IDF / low-voltage pre-bury + core-system procurement] | $___k |
| 2 (Fit-out / install) | ____ | [low-voltage install + system integration] | $___k |
| 3 (Commissioning / trial) | ____ | [system I/F test + scenario test + drill + trial ops] | $___k |
| 4 (Transition / optimize) | ____/__–__ | [old-airport transition + ops optimization] | $___k |

### 5.2 Brownfield (Existing Airport Upgrade)
| Phase | Time | Scope | Ops impact | Investment |
|------|------|------|:----------:|:----:|
| 1 (non-core pilot) | ____ | [T2 pilot smart terminal + A-CDM upgrade] | Low | $___k |
| 2 (core rollout) | ____ | [T1 upgrade + smart apron + APOC] | Medium | $___k |
| 3 (intelligent uplift) | ____ | [AI + digital twin + green airport] | Low | $___k |
| 4 (new runway / terminal) | ____ | [new area to Greenfield standard] | — | $___k |

---

## 6. Operations and Maintenance

### 6.1 O&M Team
| Team | Headcount | Responsibility |
|------|:---:|------|
| IT O&M | __ | Network / server / storage / security |
| Business-system O&M | __ | AODB / A-CDM / RMS / BHS |
| Edge-device O&M | __ | Kiosks / gates / displays / PA / CCTV |
| Low-voltage O&M | __ | Cabling / IDF / trays / conduits |
| 7×24 duty | __ | AOC duty / emergency response |

### 6.2 SLA
| System | Availability | MTTR | RTO | RPO |
|------|:----------:|:----:|:---:|:---:|
| AODB | 99.99% | <30min | <15min | 0 |
| A-CDM | 99.99% | <30min | <15min | 0 |
| FIDS | 99.9% | <2h | <1h | <5min |
| Baggage | 99.95% | <1h | <30min | <5min |
| Security | 99.95% | <30min | <15min | 0 |
| CCTV | 99.9% | <4h | N/A | N/A |
| Wi-Fi | 99.9% | <2h | <1h | N/A |

---

## 7. Investment and Benefits

### 7.1 Per-System Investment
| # | System | Investment ($k) | Share |
|:---:|------|:-----------:|:---:|
| 1 | A-CDM | $____ | __% |
| 2 | Smart terminal | $____ | __% |
| 3 | Smart apron | $____ | __% |
| 4 | ATC integration | $____ | __% |
| 5 | Smart baggage | $____ | __% |
| 6 | Passenger experience | $____ | __% |
| 7 | APOC | $____ | __% |
| 8 | Digital twin | $____ | __% |
| 9 | Green airport | $____ | __% |
| 10 | Safety & emergency | $____ | __% |
| 11 | Cloud & big data | $____ | __% |
| 12 | Network infrastructure | $____ | __% |
| 13 | System integration | $____ | __% |
| 14 | Training | $____ | __% |
| 15 | Contingency | $____ | __% |
| | **Total** | **$____** | **100%** |

### 7.2 Benefit Analysis
| Type | Item | Annual quantified benefit |
|----------|--------|:----------:|
| Economic | Labor cost saving | $____k |
| Economic | Energy cost saving | $____k |
| Economic | Non-aero revenue growth | $____k |
| Economic | Punctuality uplift (less compensation) | $____k |
| Social | Passenger time saving | ____k h / yr |
| Social | Carbon reduction | ____ t CO₂ / yr |
| Social | Jobs created | ____ |
| Safety | Incident-rate reduction | ____% |

---

> **Usage note**: This template fits new-build or expansion/upgrade airport smart-program proposals. Greenfield and Brownfield strategies differ significantly; for Brownfield, emphasize ops-while-constructing methods and system-cutover plans. Replace `[placeholder]` with project data. Have it reviewed by aviation engineers and a safety assessor.

> **Legal notice**: This template is protected by applicable copyright law and is provided for personal study and reference only; commercial use requires the author's written permission.

> **Disclaimer**: This template is for study and reference only and does not constitute professional advice of any kind. Aviation safety is life-dependent; any implementation must pass civil-aviation authority approval, independent safety assessment, and full drill validation before deployment. The author accepts no liability for any loss arising from use of or reliance on this template.

> **Author**: yinjianheng | yinjianheng@foxmail.com
