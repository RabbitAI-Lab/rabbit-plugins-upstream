# Smart Rail Transit Construction Proposal

> **Version**: V1.0
> **Date**: ____/__/__
> **Prepared by**: _________
> **Reviewed by**: _________
> **Approved by**: _________

---

## Executive Summary

### Project Positioning
The smart-rail modernization program for the [City Name] rail transit [line name / network] leverages digital and intelligent technologies to raise operational efficiency, safety, and service quality across the network, supporting [City Name]'s ambition to build a modern, integrated transport system.

### Objectives
By [target year], achieve:
- **Safety**: reduce operational incident rate by ____%; cut fault-response time to under ____ minutes
- **Efficiency**: train punctuality of ____%; peak headway compressed to ____ minutes
- **Service**: passenger satisfaction raised to ____/100; station throughput improved by ____%
- **Cost**: operating labor cost reduced by ____%; energy cost reduced by ____%

### Investment Overview
| Item | Value |
|------|------|
| Total estimated investment | $____ million |
| Construction period | ____ months |
| Estimated annual operating savings | $____ million / year |
| Payback period | ____ years |
| Financial IRR | ____% |
| Economic IRR (incl. social benefits) | ____% |

---

## 1. Project Overview

### 1.1 Background

#### 1.1.1 Current State of Urban Rail
[City Name] rail transit currently operates ____ lines, ____ km of route, ____ stations, with an average daily ridership of ____ million passenger-trips, accounting for ____% of the public-transport modal share.

#### 1.1.2 Regulatory and Policy Anchors
- National / supranational: EU Urban Mobility Framework, UNECE / TSI (Technical Specifications for Interoperability) for rail, national digital-infrastructure strategy
- Regional: [regional policy / funding programme name]
- Local: [municipal transport / smart-city programme name]

#### 1.1.3 Need for the Project
[Briefly describe the main challenges in current operations — e.g., asset ageing, peak-demand pressure, safety risk, rising labor cost]

### 1.2 Line Profile

| Item | Detail |
|------|------|
| Line name | [Line name] |
| Line length | ____ km (underground ____ km / elevated ____ km / at-grade ____ km) |
| Number of stations | ____ (underground ____ / elevated ____ / at-grade ____) |
| Depots / stabling yards | ____ |
| Train formation | ____ cars per train, [rolling stock type] |
| Design maximum speed | ____ km/h |
| Signaling system | [existing signaling type and supplier] |
| Opening date | ____/__ |
| Average daily ridership | ____ million passenger-trips |
| Peak directional passenger flow | ____ thousand pax/h |

### 1.3 Current-State Assessment

#### 1.3.1 Existing Signaling System Assessment
| Dimension | Current state | Issues | Improvement direction |
|----------|----------|----------|----------|
| System type | [CBTC / fixed-block / other] | [specific issue] | [improvement direction] |
| Supplier | [Supplier name] | [supply / spares risk] | [mitigation strategy] |
| Years in service | ____ years | [asset-degradation level] | [renewal timing] |
| Minimum headway | ____ s | [meets demand?] | [optimization target] |
| SIL safety level | [SIL level] | [meets latest standard?] | [upgrade path] |
| Interoperability | [supported?] | [cross-line operation barriers] | [upgrade plan] |

#### 1.3.2 Inventory of Existing Systems
| System category | System name | Version / model | Supplier | Commission year | Coverage | Health (1–5) |
|----------|----------|-----------|--------|----------|----------|:-----------:|
| Signaling | | | | | | |
| ISCS (integrated supervision) | | | | | | |
| Communications | | | | | | |
| AFC fare collection | | | | | | |
| PIS passenger information | | | | | | |
| PA public address | | | | | | |
| CCTV video surveillance | | | | | | |
| BAS building automation | | | | | | |
| FAS fire alarm | | | | | | |
| PSCADA power supervision | | | | | | |
| Platform screen / safety doors | | | | | | |
| ACS access control | | | | | | |

---

## 2. Goals and Vision

### 2.1 Overall Vision
Build a "[adjective] smart rail system" delivering ____, ____, ____, ____ across a [four / multi]-dimensional target set.

### 2.2 Quantified Target Framework
| Dimension | Metric | Baseline | Phase-1 target | Phase-2 target | Industry benchmark |
|----------|------|:------:|:------------:|:------------:|:------:|
| Safety | Incident rate (per million train-km) | | | | < 0.5 |
| Safety | Mean time to repair MTTR (min) | | | | < 30 |
| Efficiency | Train punctuality | | | | > 99.5% |
| Efficiency | Peak headway (s) | | | | < 90 |
| Efficiency | Load-factor balance | | | | > 85% |
| Service | Passenger satisfaction (score) | | | | > 90 |
| Service | Avg. station passage time (min) | | | | < 3 |
| Cost | Energy per train-km (kWh/train-km) | | | | < 2.0 |
| Cost | Operating staff (FTE per route-km) | | | | < 35 |
| Green | Regenerative-braking energy utilization | | | | > 30% |
| Green | Station energy intensity (kWh/m²) | | | | < 100 |

---

## 3. Overall Architecture

### 3.1 Five-Layer Architecture
```
┌──────────────────────────────────────────────────────┐
│  Layer 5  Intelligent Applications                     │
│  Smart dispatching | Smart stations | Smart O&M        │
│  Smart customer service | Smart security              │
│  Energy management | Emergency command | Flow forecast │
│  Digital twin                                          │
├──────────────────────────────────────────────────────┤
│  Layer 4  Data Platform                                │
│  Data lake | Data warehouse | Data governance          │
│  AI/ML platform | Digital-twin engine                  │
├──────────────────────────────────────────────────────┤
│  Layer 3  Convergence Platform                         │
│  TCS cloud | Video fusion | IoT platform | BIM         │
│  Spatio-temporal platform                              │
├──────────────────────────────────────────────────────┤
│  Layer 2  Network / Transport                           │
│  FRMCS (5G-R) / LTE-M | Backbone transport | Wi-Fi 6   │
│  UWB positioning | Time synchronization                │
├──────────────────────────────────────────────────────┤
│  Layer 1  Sensing & Actuation                          │
│  Signaling | Supervision | Sensors | Cameras           │
│  Gates | Platform doors | Rolling stock                │
│  PLC | Fans | Pumps | Escalators | HVAC | Lighting | Fire│
└──────────────────────────────────────────────────────┘
```

### 3.2 Technology Stack
| Layer | Key technologies | Recommended approach | Sourcing / supply-chain |
|------|----------|----------|:--------:|
| Sensing | Video AI / mmWave radar / LiDAR / IoT sensors | [approach] | [full / partial / none] |
| Network | FRMCS (5G-R) / LTE-M / industrial Ethernet / TSN | [approach] | [full / partial / none] |
| Platform | Cloud / IoT platform / big data / AI / digital twin | [approach] | [full / partial / none] |
| Application | Signaling / ISCS / AFC / PIS / PHM / BIM | [approach] | [full / partial / none] |
| Security | IEC 62443 SL3 / NIS2 / Signaling SIL4 | [approach] | [full / partial / none] |

### 3.3 Security Classification
The system is classified overall at IEC 62443 [SL2 / SL3], where:
- Signaling SIL level: [SIL requirement]
- Critical-infrastructure protection level: [NIS2 / CER classification]
- Data security classification: [classification scheme]

---

## 4. Subsystem Detailed Design

### 4.1 Signaling System (CBTC → TACS Evolution)

#### 4.1.1 Technology-Route Options
| Option | A: CBTC upgrade | B: Greenfield TACS | C: Hybrid |
|------|:---:|:---:|:---:|
| Core tech | Upgrade conventional CBTC to 2.0 | Train-to-train comms + autonomous operation | TACS core + CBTC periphery |
| Min. headway | ____s | ____s | ____s |
| Interoperability | [supported?] | [supported?] | [supported?] |
| Onboard equipment cost | $____k | $____k | $____k |
| Retrofit difficulty | Medium | High | Medium-High |
| Operational impact | ___ days suspension | ___ days suspension | ___ days suspension |
| Recommended use | Existing-line upgrade | New lines | Phased transition |

> **Recommended option**: [selection and rationale]

#### 4.1.2 Signaling Function List
| # | Function module | Description | Priority |
|:---:|----------|----------|:------:|
| 1 | ATP Automatic Train Protection | [description, SIL level] | Mandatory |
| 2 | ATO Automatic Train Operation | [description, incl. eco-driving curve optimization] | Mandatory |
| 3 | ATS Automatic Train Supervision | [description, incl. AI dynamic adjustment] | Mandatory |
| 4 | Moving block | [description] | Mandatory |
| 5 | GoA4 driverless (FAO) | [description] | [per line] |
| 6 | Interoperability | [cross-line operation capability] | [per network] |
| 7 | Autonomous train perception | [obstacle detection / collision avoidance] | Recommended |
| 8 | Virtual coupling | [dynamic formation] | Optional |
| 9 | AI timetable optimization | [demand-responsive dynamic adjustment] | Recommended |

#### 4.1.3 CBTC → TACS Evolution Path
| Phase | Time | Work scope | Key milestone | Investment |
|------|------|----------|------------|:----:|
| Phase 1 | ____ | [CBTC baseline upgrade / redundancy enhancement] | [milestone] | $___k |
| Phase 2 | ____ | [train-ground comms enhancement / trackside simplification] | [milestone] | $___k |
| Phase 3 | ____ | [train-to-train comms / autonomous-operation pilot] | [milestone] | $___k |
| Phase 4 | ____ | [full TACS / interoperability] | [milestone] | $___k |

### 4.2 Integrated Supervision System (ISCS)

#### 4.2.1 Positioning
Provides integrated monitoring and control of all electromechanical, environmental, and passenger-flow assets across the line / network, supporting normal operations, fault handling, and emergency command.

#### 4.2.2 Integration Scope
```
ISCS (Integrated Supervision System)
├── Deep integration
│   ├── PSCADA (power supervision)
│   ├── BAS (building automation)
│   ├── FAS (fire detection & alarm)
│   └── [other deep-integrated systems]
├── Interconnection
│   ├── ATS (automatic train supervision)
│   ├── AFC ( fare collection)
│   ├── PIS (passenger information)
│   ├── PA (public address)
│   ├── CCTV (video surveillance)
│   ├── ACS (access control)
│   ├── PSD (platform screen doors)
│   └── [other interconnected systems]
└── Shared interfaces
    ├── CLK (clock)
    ├── TEL/ALARM (telephone / alarm)
    └── [other shared systems]
```

#### 4.2.3 ISCS Function Matrix
| Domain | Function module | Description | Priority |
|--------|----------|----------|:------:|
| Central supervision | Network-wide asset status overview | [description] | Mandatory |
| Central supervision | Remote device control | [description] | Mandatory |
| Interlock control | Fire mode | Fire → FAS → ISCS → BAS + PA + CCTV + PSD + escalators | Mandatory |
| Interlock control | Congestion mode | Crowd → AFC → ISCS → PA + PIS + escalators | Mandatory |
| Interlock control | Normal mode | Timetable / eco / peak-period modes | Recommended |
| Smart alerting | Equipment fault early-warning | [IoT + AI asset-degradation trend prediction] | Recommended |
| Smart alerting | Abnormal-flow early-warning | [video-AI density / dwell / wrong-way detection] | Recommended |
| Energy management | Real-time energy monitoring | [per-system / per-station / per-period metering] | Mandatory |
| Energy management | Energy-saving optimization | [AI-driven ventilation / lighting / escalator control] | Recommended |
| Emergency command | One-click emergency linkage | Pre-set emergency modes (fire / flood / security) | Mandatory |
| Emergency command | Emergency resource management | [visual management of supplies / staff / vehicles] | Recommended |

### 4.3 Smart Stations

#### 4.3.1 Design Philosophy
Passenger-centric, delivering an intelligent end-to-end experience across "entry → security → waiting → boarding → exit".

#### 4.3.2 Smart-Station Function Matrix
| Scenario | Function module | Technology | Expected effect | Priority |
|------|----------|----------|----------|:------:|
| **Flow mgmt** | Real-time flow sensing | Video AI + Wi-Fi probe + heat map | >95% in-station density awareness | Mandatory |
| **Flow mgmt** | Flow forecasting | Deep learning + OD matrix + events calendar | 15-min granularity, >85% accuracy | Recommended |
| **Flow mgmt** | Flow guidance | Dynamic signage + app push + smart PA | +20% throughput at bottlenecks | Recommended |
| **Flow mgmt** | Crowd-control strategy | AI-generated control plan + simulation | Scientific crowd control | Recommended |
| **Security** | Smart screening | CT scanner + AI image analysis + centralized adjudication + auto-tray return | 2–3× screening throughput | Recommended |
| **Security** | Abnormal-behavior detection | Video AI (fight / run / fall / dwell / wrong-way / left item) | <5s anomaly alert | Recommended |
| **Security** | Intrusion detection | LiDAR + video analytics | Seconds-level intrusion alarm | Mandatory |
| **Security** | Electronic patrol | NFC / RFID + mobile app | Traceable, auditable patrols | Recommended |
| **Info** | Smart PIS | Dynamic LCD + LED + kiosk + app push | Multi-modal information | Mandatory |
| **Info** | Smart guidance | Indoor navigation + BLE beacons + AR navigation | <3m in-station accuracy | Recommended |
| **Info** | Commercial info | Nearby retail / tourism recommendations | Non-fare revenue uplift | Optional |
| **Environment** | Smart HVAC | AI + chilled-water / ventilation optimization | −15–25% station energy | Recommended |
| **Environment** | Smart lighting | Occupancy + daylight harvesting + LED | −30–50% lighting energy | Recommended |
| **Environment** | Environment monitoring | PM2.5 / CO2 / temp-humidity / noise | Real-time comfort quantification | Recommended |
| **Accessibility** | Accessible navigation | App accessibility mode + voice guidance + tactile-path monitoring | Friendly for visually impaired / wheelchair users | Mandatory |
| **Accessibility** | Assisted-travel booking | Online booking + on-site meet + end-to-end escort | Higher service for special-needs pax | Recommended |

### 4.4 Smart O&M (Predictive Maintenance)

#### 4.4.1 PHM Predictive Maintenance
| Asset | Monitored params | Sensor / tech | Fault type | Lead time | Expected effect |
|----------|----------|-------------|----------|:----------:|----------|
| Bogie / running gear | Vibration / temp / speed | Accelerometer + temp sensor | Bearing / gear / wheel faults | 7–30 days | −60–80% unplanned stoppages |
| Pantograph / catenary | Image / temp / stagger | Vision AI + IR + laser | Wear / arcing / clamp looseness | 3–14 days | −50–70% pantograph faults |
| Track | Gauge / profile / alignment | Inspection train + INS | Geometry exceedance / rail defect | 1–6 months | >99% defect detection |
| Points / switches | Current / power / time / gap | Point-gap monitor + AI | Jam / false indication | 1–7 days | −40–60% point faults |
| Signaling equipment | Electrical / optical power / axle-counter | Online monitoring + trend | Signal / point-machine / axle-counter faults | 3–30 days | −50–70% signaling faults |
| Power equipment | Partial discharge / temp / DGA / insulation | Online monitoring + oil analysis | Transformer / switchgear / cable faults | 7–90 days | −50–80% power faults |
| Escalators | Vibration / temp / current / speed | IoT + edge compute | Drive / handrail / step faults | 3–14 days | −50%+ downtime |
| Platform doors | Current / time / closing force | Dynamic analysis + AI | Jam / unlock / control fault | 1–7 days | −40–60% door faults |
| HVAC | Vibration / temp / pressure / efficiency | IoT + efficiency model | Cooling degradation / compressor fault | 7–30 days | −10–20% HVAC energy |

#### 4.4.2 Intelligent Inspection Robots
| Scenario | Robot type | Scope | Frequency | Coverage |
|----------|-----------|----------|:----:|----------|
| Tunnel inspection | Rail-guided robot / UAV | Structure / leakage / piping / FOD | Daily / Weekly | Whole tunnel |
| Undercarriage | Fixed / mobile robot | Undercarriage parts / bolts / pipes | Daily | Depot |
| Station patrol | Wheeled / tracked security robot | Suspicious acts / left items / temp-humidity / smoke | 24/7 | Station public area |
| Substation | Wheeled robot | Meter reading / temp / PD / abnormal sound | Daily / Weekly | All substations |
| Catenary | UAV / onboard vision | Geometry / wear / FOD | Weekly / Monthly | Whole line |

### 4.5 Passenger Service

#### 4.5.1 Smart Fare Collection
| Function | Technology | Description | Priority |
|------|----------|------|:------:|
| QR-code gate | App / bank / transit QR | Regional interoperability | Mandatory |
| NFC gate | Phone NFC / wearable / open-loop EMV | Supports Calypso / ITSO / EMV | Recommended |
| Face recognition gate | 1:1 match + liveness | [privacy-by-design required] | Optional |
| Palm print / vein | Contactless biometrics | Hygienic / efficient / secure | Optional |
| Account-based (post-pay) | Ride now, pay later + credit | Linked payment account | Recommended |
| Frictionless pay | Multi-modal fusion + account | Ultimate ticketing experience | Long-term |
| Smart customer service | AI voice + remote agent + kiosk | Self-service ticketing / trip info | Mandatory |

#### 4.5.2 Real-Time Information Service
| Info type | Channel | Content | Frequency |
|----------|----------|------|:--------:|
| Arrival info | PIS / app / platform PA | Second-accurate countdown | Real-time |
| Car crowding | PIS / app / door projection | Per-car crowding heat map | Real-time |
| First / last train | App / PIS / web | Timetable | Static + dynamic |
| Delay / fault | Multi-channel push | Cause / ETA / alternatives | Event-driven |
| Transfer info | In-station / app | Route / time / alternatives | Real-time |
| First/last-mile | App / PIS | Bus / bike-share / taxi | Real-time |

#### 4.5.3 Accessibility Service
| Service | Content | Technology |
|----------|----------|----------|
| Accessible path | Step-free from street to platform | Accessible elevator + tactile + ramp + wide gate |
| Voice guidance | Navigation for visually impaired | App BLE voice + directional speakers |
| Wheelchair service | Booking + assisted boarding | Online booking + staff meet + ramp |
| Hearing-impaired | Text / sign-language info | PIS text + sign-language video + app text |
| Assisted-travel booking | Online booking + on-site meet | App / mini-program + CRM + staff app |

### 4.6 Energy Management

#### 4.6.1 Energy-Management Architecture
```
Regen braking energy ─┐
Rooftop PV ───────────┤
Storage ──────────────┼──→ Energy Mgmt Platform ──→ Saving strategy
Grid supply ──────────┤                    ├→ Alert: abnormal-energy alarm
Traction energy ──────┤                    ├→ Benchmark: per-line / per-station
Station energy ───────┘                    └→ Optimize: AI energy control
```

#### 4.6.2 Key Energy-Saving Measures
| Direction | Measure | Expected saving | Investment | Payback |
|----------|----------|:----------:|:--------:|:------:|
| Traction | Eco-driving curve (coasting + regen) | 10–20% | $___k | ___ y |
| Traction | Regen energy recovery (storage / inverter feedback) | 5–15% | $___k | ___ y |
| Station HVAC | Variable-speed + AI optimization | 15–30% | $___k | ___ y |
| Station lighting | LED + smart control (lux / occupancy) | 30–50% | $___k | ___ y |
| Escalators | VSD + smart start-stop (occupancy) | 20–30% | $___k | ___ y |
| Renewables | Depot / station rooftop PV | 1–5% | $___k | ___ y |
| Overall | EMS + energy benchmarking | 5–10% | $___k | ___ y |

### 4.7 Safety and Emergency

#### 4.7.1 Protection System
| Layer | Content | Technology | Standard |
|----------|----------|----------|----------|
| Physical | Perimeter / intrusion / access / screening | LiDAR + video AI + face + X-ray/CT | EN 50126 / 50128 / 50129 |
| Operational | SIL4 / track inspection / train supervision | ATP/ATO redundancy + obstacle detection + derailment detection | EN 50126/50128/50129 |
| Fire | Detection + interlock + evacuation guidance | FAS + ISCS linkage + smart signage | EN 54 / NFPA 72 / ISO 7240 |
| Flood | Flood warning + barriers + drainage | Level sensor + video AI + remote gates | [local flood standard] |
| Cyber | IEC 62443 + NIS2 + signaling security | Defense-in-depth + audit + threat sensing | IEC 62443 / NIS2 |
| Security | Face + behavior analytics + panic alarm | Video AI + watchlist + connected alarm | [security standard] |

#### 4.7.2 Emergency-Plan Framework
| Category | Plan name | Trigger | Response flow | Drill freq. |
|----------|----------|----------|----------|:--------:|
| Natural disaster | Storm / typhoon / earthquake / ice | [trigger] | [flow] | Semi-annual |
| Equipment fault | Signaling fault / power loss / rolling-stock fault | [trigger] | [flow] | Quarterly |
| Public security | Fire / explosion / hazmat / security incident | [trigger] | [flow] | Semi-annual |
| Crowd | Sudden surge / major event | [trigger] | [flow] | Quarterly |
| Public health | Pandemic | [trigger] | [flow] | Annual |

### 4.8 Digital Twin

#### 4.8.1 Digital-Twin Levels
| Level | Name | Content | Precision | Use case |
|:---:|------|------|:---:|----------|
| L1 | City | Network overview in city | 100 m | Network planning / public reporting |
| L2 | Line | Whole-line 3D model | 10 m | Line operations monitoring |
| L3 | Station | Full-element station 3D model | 1 m | Station mgmt / flow simulation |
| L4 | Equipment | Key-equipment fine model | 1 cm | O&M / fault rehearsal |
| L5 | Component | BIM component-level model | 1 mm | Precision repair / spares |

#### 4.8.2 Digital-Twin Use Cases
| Scenario | Description | Data source | Effect |
|------|----------|--------|------|
| Network status | Real-time mapping of train position / speed / headway | ATS + rolling stock | At-a-glance operations |
| Station flow sim | Peak crowd evacuation simulation | Video AI + flow model | Validate control plan |
| Fault rehearsal | Impact spread after a fault | ISCS + BIM | Pre-rehearse response |
| Construction mgmt | 3D visualization of work zones | Scheduling + positioning | Construction safety |
| Emergency drill | Virtual fire / flood drill | Twin + CFD | Low-cost frequent drills |
| Energy heat map | 3D station / tunnel energy | EMS + IoT | Locate anomalies |

---

## 5. Implementation Plan

### 5.1 Principles
- **Minimize operational impact**: work / commissioning in non-revenue windows (00:00–04:00)
- **Phased rollout**: single-station pilot → single-line rollout → network coverage
- **Smooth transition**: old/new systems run in parallel for ____ months for zero-risk cutover
- **Safety first**: any safety-related change requires SIL safety assessment

### 5.2 Phases
| Phase | Time | Scope | Milestone | Investment |
|------|------|----------|--------|:----:|
| Phase 1 (pilot) | ____/__–__ | [1–2 stations: smart station + signaling baseline upgrade] | [milestone] | $___k |
| Phase 2 (rollout) | ____/__–__ | [all stations + ISCS upgrade + deep signaling retrofit] | [milestone] | $___k |
| Phase 3 (intelligent) | ____/__–__ | [AI / digital twin / PHM full deployment] | [milestone] | $___k |
| Phase 4 (network) | ____/__–__ | [multi-line interoperability + network platform] | [milestone] | $___k |

### 5.3 Operational-Impact Minimization
| Work | Window | Impact | Mitigation |
|----------|----------|:----------:|----------|
| Signaling upgrade | Night possession (00:00–04:00) | None | Pre-commissioning + rollback plan |
| Station equipment | Night / post-last-train | Low | Zoned work + temporary barriers + signage |
| Network retrofit | Night | None | Redundant network + hot standby |
| Software upgrade | Night cutover window | Low | A/B canary + auto-rollback |
| System cutover | Weekend / holiday | Medium | Full rehearsal + bus-bridge plan |
| Platform-door retrofit | Night, segmented | Medium | One-door-at-a-time + extra patrol |

---

## 6. Testing and Commissioning

### 6.1 Test Strategy
| Type | Content | Phase | Owner |
|----------|----------|:--------:|--------|
| FAT (Factory Acceptance Test) | Pre-shipment equipment / software test | Production | Supplier + Client |
| SAT (Site Acceptance Test) | Post-installation unit test | Installation | Supplier + Supervision |
| Interface test | Inter-system interface / protocol / data | Integration | Integrator + Suppliers |
| SIT (System Integration Test) | Full functional / performance / reliability | Integration | Integrator |
| Operational-scenario test | Normal / degraded / emergency | Pre-revenue | Integrator + Operator |
| 144-hour endurance test | Continuous-stability run | Pre-revenue | Operator + Integrator |
| RAM validation | Reliability / Availability / Maintainability | Pre-revenue | Operator |
| Safety assessment | Independent Safety Assessment (ISA) | Before revenue | 3rd-party assessor |

### 6.2 Test-Scenario List (sample)
| # | Category | Scenario | Expected | Priority |
|:---:|----------|----------|----------|:------:|
| 1 | Normal | Weekday peak per timetable | Punctuality >99.5% | Must |
| 2 | Normal | Off-peak / weekend / holiday timetable | Execution >99% | Must |
| 3 | Degraded | ATP fault → degrade to restricted / telephone block | Safe degradation | Must |
| 4 | Degraded | ISCS single-point fault → backup OCC takes over | Switch <____s | Must |
| 5 | Emergency | Station fire → FAS+ISCS linkage + evacuation | Correct + on-time | Must |
| 6 | Emergency | Tunnel evacuation → tunnel evac + adjacent-station hold | Orderly command | Must |
| 7 | Emergency | Train fault rescue → push / tow to depot | Rescue <____min | Must |
| 8 | Performance | Peak-load stress test | Response / throughput met | Must |
| 9 | Performance | Wall refresh / concurrent-alarm stress | No lag / no lost alarm | Must |
| 10 | Security | Penetration test + security assessment | Pass ____ level | Must |

---

## 7. Training

### 7.1 Tiered Training
| Audience | Content | Method | Duration | Assessment |
|----------|----------|----------|:---:|:---:|
| Operations mgmt | Overview / data cockpit / reports / command | Class + hands-on | 2 d | Written |
| Dispatchers (OCC) | ISCS ops / signaling monitor / fault judge / emergency | Class + sim + hands-on | 5 d | Written + practical |
| Station staff | Smart-station / smart service / crowd control / emergency | Class + practical + drill | 3 d | Written + practical |
| Maintenance | System principles / upkeep / fault / PHM | Class + practical + shadow | 10 d | Written + practical + cert |
| IT O&M | Cloud / network / security / DB / ops | Class + practical + cert | 10 d | Written + practical + cert |
| Service staff | Smart service / AI knowledge base / remote agent | Class + practical | 2 d | Written + practical |

### 7.2 Training Deliverables
| Deliverable | Content | Due |
|--------|------|----------|
| Training material | Per-role PPT + manual + video | ____ wk before |
| Training platform | LMS + online exam | ____ wk before |
| Simulation env | System training sim (incl. fault injection) | ____ wk before |
| Exam bank | Per-role questions (≥200 / role) | ____ wk before |
| Training records | Sign-in / scores / cert / satisfaction | After training |

---

## 8. Operations and Maintenance Service

### 8.1 O&M Service Model
| Service | Content | Grade |
|----------|----------|----------|
| 7×24 hotline | Fault report / tech consult | Answer >95%, wait <30s |
| On-site O&M | [X] staff on-site (OCC + depot) | 5×8h or 7×24h |
| Remote O&M | Remote monitor / diagnose / fix | 7×24h response |
| Preventive maint. | Periodic inspection / service / update | Per maintenance manual |
| Emergency response | Rapid on-site for major faults | Arrive <____ h |
| Spares mgmt | Critical spares stock / mgmt / replace | Critical-spare availability >99% |

### 8.2 SLA Metrics
| Level | Definition | Response | On-site | Recovery | Availability |
|:--------:|------|:--------:|:--------:|:--------:|:----------:|
| P1 (critical) | Affects safety or whole-line ops | <5 min | <30 min | <2 h | 99.999% |
| P2 (major) | Affects part of station / system | <15 min | <2 h | <8 h | 99.99% |
| P3 (minor) | Single station / non-critical | <30 min | <4 h | <24 h | 99.9% |
| P4 (trivial) | No ops impact | <2 h | N/A | <48 h | 99.5% |

---

## 9. Investment Estimate

### 9.1 Per-System Investment
| # | System | Investment ($k) | Share |
|:---:|------|:--------------:|:---:|
| 1 | Signaling retrofit | $____ | __% |
| 2 | ISCS | $____ | __% |
| 3 | Communications upgrade | $____ | __% |
| 4 | Smart stations | $____ | __% |
| 5 | Smart O&M PHM | $____ | __% |
| 6 | AFC upgrade | $____ | __% |
| 7 | Energy management | $____ | __% |
| 8 | Digital-twin platform | $____ | __% |
| 9 | Safety & emergency | $____ | __% |
| 10 | Cloud & big data | $____ | __% |
| 11 | Network infrastructure | $____ | __% |
| 12 | System integration | $____ | __% |
| 13 | 3rd-party test / safety assessment | $____ | __% |
| 14 | Training | $____ | __% |
| 15 | Contingency | $____ | __% |
| | **Total** | **$____** | **100%** |

### 9.2 Phased Investment
| Year | Investment ($k) | Main use |
|:----:|:--------------:|----------|
| Y1 | $____ | Phase 1 pilot: ____ |
| Y2 | $____ | Phase 2 rollout: ____ |
| Y3 | $____ | Phase 3 intelligent: ____ |
| Y4–5 | $____ | Phase 4 network: ____ |
| **Total** | **$____** | |

---

## 10. Benefit Analysis

### 10.1 Economic Benefits
| Item | Basis | Annual ($k) |
|--------|----------|:-------------:|
| Labor saving | [role] −____ FTE × $____/FTE-yr | $____ |
| Energy saving | Energy −____% × annual $____k | $____ |
| Maintenance saving | Faults −____% + spares optimization | $____ |
| Non-fare revenue | Retail / ads / data services | $____ |
| Other | [note] | $____ |
| **Total** | | **$____** |

### 10.2 Social Benefits
| Item | Metric |
|--------|----------|
| Congestion relief | Modal-share uplift removes ____k vehicles/day from roads |
| Carbon reduction | ____ tonnes CO₂e / year |
| Travel-time saving | ____k passenger-hours / year |
| Safety uplift | ____ fewer safety incidents / year |
| Jobs | ____ new jobs created |

### 10.3 Safety Benefits
| Item | Metric |
|--------|----------|
| Signaling safety | SIL4 assurance, signaling-related risk −____% |
| Asset safety | PHM predictive maintenance, asset-caused incidents −____% |
| Emergency response | Response time cut from ____ min to ____ min |

---

## 11. Risk and Mitigation

| Risk category | Description | Impact | Likelihood | Mitigation |
|----------|----------|:--------:|:--------:|----------|
| Technology | Immaturity of new tech (TACS/AI) | High | Medium | Thorough PoC + parallel with proven solution |
| Construction | Night work affects next-day ops | High | Medium | Strict process + rollback + extra testing |
| Supply | Import-equipment disruption / chip restrictions | High | Medium | Local-content alternative + critical spares |
| Safety | Incident during cutover | Very high | Low | Independent safety assessment + multi-level verification + staged cutover |
| Management | Multi-vendor coordination difficulty | Medium | High | Lead systems integrator + clear interface standards + KPI |
| Cost | Budget overrun | Medium | Medium | 15–20% contingency + phased approval |

---

## 12. Organizational Assurance

### 12.1 Project Organization
```
                 Steering Committee (Client executive sponsor + Vendor executive)
                              │
              ┌───────────────┼───────────────┐
              │               │               │
         Program Director   Expert Panel      Supervision (Owner's Engineer)
              │
    ┌─────────┼─────────┐
    │         │         │
  PMO      Tech Mgmt    Quality Mgmt
    │         │         │
    ├─── Signaling team
    ├─── ISCS team
    ├─── Smart-station team
    ├─── O&M systems team
    ├─── Network / Security team
    ├─── Testing team
    └─── Training team
```

### 12.2 Key Roles
| Role | Responsibility | Qualification |
|------|------|------|
| Program Director | Overall accountability, resources, major decisions | 15+ yrs rail IT |
| Signaling expert | Signaling technical authority / SIL assurance | 10+ yrs rail signaling |
| ISCS expert | ISCS design / integration | 10+ yrs supervision |
| Network / security expert | Comms / network / cyber design | 10+ yrs comms / security |
| BIM / digital-twin expert | BIM modeling / twin platform | 8+ yrs BIM / twin |
| Test manager | Test strategy / plan / exec / report | 10+ yrs rail-system test |
| Operator liaison | Client ops requirements / training / handover | Core client ops staff |

---

> **Usage note**: This is a complete framework template for a smart rail transit construction proposal. Populate it per the actual line, scale, technology selection, and budget. Replace `[placeholder]` with project data and `____` with specifics. Have it reviewed by signaling, ISCS, communications, and security engineers before use.

> **Legal notice**: This template is protected by applicable copyright law and is provided for personal study and reference only; commercial use requires the author's written permission.

> **Disclaimer**: This template is for study and reference only and does not constitute professional advice of any kind. Rail systems are safety-critical and life-dependent; any implementation must undergo full SIL safety assessment, simulation, pilot validation, and independent safety review before deployment. The author accepts no liability for any loss arising from use of or reliance on this template.

> **Author**: yinjianheng | yinjianheng@foxmail.com
