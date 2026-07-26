# Full-Chain 130-Scenario Benchmark Checklist
## 130-Scenario Digital Transformation Benchmark Checklist

---

## 1. Tool Overview

This checklist covers 12 core transport business chains and 130 digitalization scenarios, providing a full-chain self-assessment and benchmarking tool. Each scenario includes description, key capability, technical / data needs, industry maturity, investment range, and implementation duration, plus a 0–4 self-score and gap-analysis framework.

### 12 Business Chains
| ID | Chain | # Scenarios | Core Theme |
|----|-------|-------------|------------|
| C1 | Integrated Traffic Operations Monitoring | 15 | Sensing, monitoring, warning, dispatch |
| C2 | Urban Traffic Management & Control | 15 | Signals, guidance, network management |
| C3 | Public Transit Operations | 12 | Bus, metro, dispatch, info service |
| C4 | Highway / Motorway Operations | 12 | Tolling, maintenance, safety, service areas |
| C5 | Transport Infrastructure Management | 10 | Bridges/tunnels, pavement, asset management |
| C6 | Enforcement & Safety | 10 | Enforcement, incidents, emergency, safety |
| C7 | Mobility-as-a-Service (MaaS) | 10 | Info service, payment, intermodal |
| C8 | Logistics & Freight | 10 | Freight platforms, multimodal, urban delivery |
| C9 | Parking Management | 8 | On-street, off-street, guidance, sharing |
| C10 | Transport Planning & Decision | 10 | Planning, simulation, evaluation, policy |
| C11 | Green Transport & Carbon Management | 8 | Carbon monitoring, NEV, green mobility |
| C12 | Frontier Technology Innovation | 10 | AV, low-altitude, LLM, digital twin |

### Self-Score Rubric (0–4)
| Score | Label | Description |
|-------|-------|-------------|
| 0 | Not Started | No relevant plan or action |
| 1 | Basic | Plan / pilot exists; basic functionality |
| 2 | Partial | Some scenarios live in production |
| 3 | Advanced | Full deployment; significant effect |
| 4 | Leading | Industry benchmark; outstanding innovation |

> **Currency note:** Investment values are re-based to US$ millions (1 RMB ≈ $0.14).

---

## 2. Complete Scenario List

### C1: Integrated Traffic Operations Monitoring (15 scenarios)
| ID | Scenario | Description | Key Capability | Tech Needs | Maturity | Invest ($M) | Months | Self |
|----|---------|-------------|----------------|-----------|----------|-------------|--------|------|
| C1.1 | Real-time traffic-state monitoring | Citywide / network-wide real-time state monitoring | Multi-source fusion, heatmap, metric calc | Big-data platform, GIS | ★★★★ | 0.7–2.1 | 6–12 | ___ |
| C1.2 | TMC cockpit / video wall | Visualization wall for the urban traffic command center | Viz engine, executive cockpit | Video-wall HW, viz SW | ★★★★★ | 0.42–1.40 | 3–6 | ___ |
| C1.3 | Traffic index / health scoring | City traffic index computation & publishing | Index algorithm, multi-metric fusion | Data warehouse, compute engine | ★★★★ | 0.14–0.42 | 3–6 | ___ |
| C1.4 | Multi-modal OD analysis | OD matrix across travel modes within the city | Cell-signal, smart-card, GPS fusion | Big-data platform, privacy computing | ★★★☆ | 0.42–1.12 | 6–12 | ___ |
| C1.5 | Traffic-state prediction | 15-min to 24-hr traffic-state forecast | Time-series, deep learning | GPU / ML platform | ★★★☆ | 0.28–0.70 | 6–9 | ___ |
| C1.6 | Major-event traffic assurance | Monitoring & assurance during large events / games | Plan mgmt, real-time dispatch | Video, dispatch platform | ★★★★ | 0.28–0.70 | 3–6 | ___ |
| C1.7 | Adverse-weather traffic control | Monitoring & control in heavy rain / fog / snow / ice | Weather forecast, coordinated control | Weather sensors, VMS | ★★★☆ | 0.42–1.12 | 6–12 | ___ |
| C1.8 | Holiday traffic prediction | Pre-holiday flow prediction & assurance plan | Historical analysis, prediction | Big-data platform | ★★★★ | 0.14–0.42 | 3–6 | ___ |
| C1.9 | Key-vehicle monitoring | Dynamic monitoring of regulated fleets (coaches, hazmat, school buses) | GNSS tracking, geo-fence | Tracking terminal, comms network | ★★★★★ | 0.42–1.12 | 3–6 | ___ |
| C1.10 | Traffic carbon-emission monitoring | Real-time city transport CO2 monitoring & stats | Emission accounting, data collection | Carbon platform | ★★☆☆ | 0.28–0.70 | 6–12 | ___ |
| C1.11 | Cross-agency info sharing | Data sharing across police / transport / planning / environment | Data exchange, access control, security review | Data-sharing platform, API gateway | ★★★☆ | 0.28–0.70 | 6–12 | ___ |
| C1.12 | Public travel-info service | Real-time public travel-info publishing | Multi-channel publish (app / mini-program / sign / radio) | Publish engine, user profiling | ★★★★ | 0.28–0.84 | 6–9 | ___ |
| C1.13 | Traffic TV / social auto-publish | Auto-publishing to TV & social media | Auto content gen, multi-channel | AIGC / template engine | ★★☆☆ | 0.07–0.28 | 3–6 | ___ |
| C1.14 | Regional integration monitoring | Metro-area integrated traffic-state monitoring | Cross-region data collaboration, unified standards | Cross-region exchange platform | ★★☆☆ | 0.7–2.1 | 9–18 | ___ |
| C1.15 | AI daily / weekly traffic report | Auto-written AI traffic-analysis reports | NLG, template gen, data analysis | LLM / NLG engine | ★★★☆ | 0.07–0.28 | 3–6 | ___ |

**C1 subtotal: ___/60**

---

### C2: Urban Traffic Management & Control (15 scenarios)
| ID | Scenario | Description | Key Capability | Tech Needs | Maturity | Invest ($M) | Months | Self |
|----|---------|-------------|----------------|-----------|----------|-------------|--------|------|
| C2.1 | Isolated adaptive signal control | Per-intersection adaptive timing | Vehicle detection, timing optimization | Detectors, controller | ★★★★★ | 0.42–1.12 | 3–6 | ___ |
| C2.2 | Arterial green-wave coordination | Bidirectional green-wave on arterials | Green-wave algorithm, offset opt. | Controller, comms | ★★★★ | 0.7–2.1 | 6–12 | ___ |
| C2.3 | Area-wide signal coordination | City-area signal coordination | Multi-agent opt., area modeling | Area control platform | ★★★☆ | 1.40–4.20 | 12–18 | ___ |
| C2.4 | AI signal-timing optimization | RL-based signal-timing AI | Deep RL, simulation validation | GPU, sim engine | ★★★☆ | 0.7–2.1 | 12–18 | ___ |
| C2.5 | Transit signal priority | Transit priority at intersections | Transit positioning, priority policy | On-board terminal, signal comms | ★★★★ | 0.42–1.12 | 6–12 | ___ |
| C2.6 | Emergency-vehicle priority | Ambulance / fire / police priority | RFID / GNSS, emergency priority | On-board terminal, controller | ★★★☆ | 0.14–0.42 | 3–6 | ___ |
| C2.7 | Reversible-lane control | Tidal / reversible lane control | Flow detection, switch control | Variable signs, detectors | ★★★★ | 0.28–0.70 | 3–6 | ___ |
| C2.8 | Variable speed limit | Dynamic speed mgmt on motorway / expressway | Speed coordination, flow model | VSL signs, flow detection | ★★★★ | 0.42–1.12 | 6–12 | ___ |
| C2.9 | Ramp metering | On-ramp smart control on viaduct / expressway | Queue detection, merge control | Ramp signal, detector | ★★★☆ | 0.42–1.12 | 6–12 | ___ |
| C2.10 | Traffic guidance system | VMS / sign / nav-app congestion guidance | Flow fusion, best-route calc | VMS, navigation API | ★★★★ | 0.7–2.1 | 6–12 | ___ |
| C2.11 | Work-zone traffic mgmt | Traffic org & control in work zones | Work permit, traffic-org plan | Work-zone mgmt platform | ★★☆☆ | 0.14–0.42 | 3–6 | ___ |
| C2.12 | Digital traffic-org evaluation | Digital evaluation of one-way / no-left / restriction plans | Scenario simulation, effect eval | Sim engine, data analysis | ★★☆☆ | 0.28–0.70 | 6–12 | ___ |
| C2.13 | HOV / HOT lane mgmt | High-occupancy / priced-lane mgmt | Vehicle detection, auto toll | HOV detection, toll system | ★☆☆☆ | 0.7–2.8 | 9–18 | ___ |
| C2.14 | Congestion root-cause analysis | Auto congestion-cause analysis & location | Causal analysis, root-cause | Big-data analytics | ★★★☆ | 0.14–0.42 | 3–6 | ___ |
| C2.15 | Regional OD-based control | OD-based regional demand mgmt | Boundary control, OD estimation | Detector network, compute center | ★★☆☆ | 0.7–2.1 | 9–18 | ___ |

**C2 subtotal: ___/60**

---

### C3: Public Transit Operations (12 scenarios)
| ID | Scenario | Description | Key Capability | Tech Needs | Maturity | Invest ($M) | Months | Self |
|----|---------|-------------|----------------|-----------|----------|-------------|--------|------|
| C3.1 | Transit smart dispatch | Real-time GPS-based bus dispatch | Real-time positioning, dispatch algo | GNSS terminal, dispatch platform | ★★★★★ | 0.42–1.40 | 6–12 | ___ |
| C3.2 | AI transit scheduling | AI-generated schedules from demand | Demand forecast, smart scheduling | Big data, optimization | ★★★☆ | 0.28–0.70 | 6–12 | ___ |
| C3.3 | Transit OD analysis | Boarding/alighting OD analysis | Smart-card / scan-data mining | Big-data platform | ★★★★ | 0.14–0.42 | 3–6 | ___ |
| C3.4 | AI network optimization | Network optimization from demand & growth | Network model, multi-objective opt. | Optimization solver | ★★☆☆ | 0.28–0.70 | 6–12 | ___ |
| C3.5 | Demand-responsive transit (DRT) | Dynamic demand-responsive service | Real-time matching, dynamic routing | DRT platform, user app | ★★★☆ | 0.7–2.8 | 9–18 | ___ |
| C3.6 | Real-time transit info | Real-time arrival / crowding prediction | ETA prediction, crowding est. | On-board terminal, app | ★★★★ | 0.28–0.70 | 6–9 | ___ |
| C3.7 | Transit electronic stops | Platform screens with real-time arrivals | LED sign, remote update | E-stop HW, comms | ★★★★★ | 0.42–1.12 | 3–6 | ___ |
| C3.8 | Smart metro operations | Metro flow analysis / train dispatch / energy | APC, energy mgmt, dispatch opt. | Metro ATS / AFC integration | ★★★☆ | 0.7–2.8 | 9–18 | ___ |
| C3.9 | Urban-rural transit integration | Unified mgmt & info for urban-rural bus | Unified mgmt, integrated dispatch | Transit mgmt platform | ★★☆☆ | 0.42–1.12 | 6–12 | ___ |
| C3.10 | Transit safety-driving monitor | Driver behavior analysis & warning | DMS / ADAS, behavior analysis | On-board DMS / ADAS | ★★★★ | 0.28–0.84 | 6–9 | ___ |
| C3.11 | Digital transit KPI | Data-based automatic service-quality scoring | Metric calc, auto scoring | Data-analysis platform | ★★★☆ | 0.14–0.42 | 3–6 | ___ |
| C3.12 | Accessible mobility service | Assisted mobility for elderly / PWD | Accessibility info, booking | App / service platform | ★★☆☆ | 0.14–0.42 | 3–6 | ___ |

**C3 subtotal: ___/48**

---

### C4: Highway / Motorway Operations (12 scenarios)
| ID | Scenario | Description | Key Capability | Tech Needs | Maturity | Invest ($M) | Months | Self |
|----|---------|-------------|----------------|-----------|----------|-------------|--------|------|
| C4.1 | Free-flow ETC tolling | Gantry + ETC non-stop tolling | High-precision OBU / RSU | ETC gantry, toll platform | ★★★★★ | 4.2–11.2 /100km | 12–24 | ___ |
| C4.2 | Smart toll robot | Self-service / unattended toll terminal | AI recognition, self-pay | Toll-robot HW | ★★★★ | 0.7–2.1 | 3–6 | ___ |
| C4.3 | Digital toll audit | AI-based toll evasion detection & recovery | Path reconstruction, anomaly detect | Big-data platform, AI | ★★★★ | 0.28–0.70 | 6–9 | ___ |
| C4.4 | Network operations monitoring | Whole-network state monitoring | Holographic sensing, event detect | Video / radar / sensor | ★★★★ | 1.40–4.20 /100km | 9–18 | ___ |
| C4.5 | Smart tunnel control | Lighting / ventilation / fire control in tunnels | Multi-system linkage, env control | PLC / sensor / actuator | ★★★★ | 0.7–2.8 /tunnel | 6–12 | ___ |
| C4.6 | Smart service area | Service-area flow / vehicle analysis, smart guidance | Flow analysis, smart service | IoT sensor, AI analysis | ★★★☆ | 0.28–1.12 /area | 3–6 | ___ |
| C4.7 | Automated pavement inspection | UAV / inspection vehicle + AI defect ID | CV detection, GIS tagging | UAV / vehicle, AI | ★★★☆ | 0.42–1.40 | 6–12 | ___ |
| C4.8 | Bridge structural health monitoring | Real-time large-bridge health monitoring | Sensor network, warning model | Sensors, acquisition system | ★★★★ | 0.7–2.8 /bridge | 6–12 | ___ |
| C4.9 | Slope / geohazard monitoring | Roadside slope & geohazard early warning | GNSS monitoring, InSAR | Sensors, satellite data | ★★★★ | 0.42–1.40 /section | 6–12 | ___ |
| C4.10 | Smart maintenance mgmt | Data-driven preventive maintenance decisions | Pavement performance decay predict | Maintenance platform | ★★★☆ | 0.28–0.70 | 6–12 | ___ |
| C4.11 | All-weather operation | Assisted operation in fog / ice / snow | Weather monitoring, V2X | Weather station, V2X, VMS | ★★★☆ | 2.8–7.0 /100km | 12–24 | ___ |
| C4.12 | Highway energy management | Solar / storage / EV-charger mgmt at areas & tunnels | Microgrid, energy mgmt | PV, storage, chargers | ★★★☆ | 0.7–2.8 | 9–18 | ___ |

**C4 subtotal: ___/48**

---

### C5: Transport Infrastructure Management (10 scenarios)
| ID | Scenario | Description | Key Capability | Tech Needs | Maturity | Invest ($M) | Months | Self |
|----|---------|-------------|----------------|-----------|----------|-------------|--------|------|
| C5.1 | Infrastructure asset digitization | Inventory & digitize signs / markings / barriers / signals | Asset coding, GIS mapping | Mobile capture, GIS | ★★★☆ | 0.28–1.12 | 6–12 | ___ |
| C5.2 | BIM + GIS infrastructure mgmt | Full-lifecycle infrastructure mgmt on BIM + GIS | BIM modeling, GIS fusion | BIM platform, GIS engine | ★★★☆ | 1.40–4.20 | 12–24 | ___ |
| C5.3 | Facility-condition AI inspection | AI condition-rate inspection of signs / markings / barriers | CV detection, condition assess | Inspection vehicle / AI, mobile | ★★☆☆ | 0.28–0.70 | 6–12 | ___ |
| C5.4 | Pavement performance eval & predict | AI eval & predict of roughness / distress / rut / skid | Time-series, multi-metric fusion | Inspection data, AI model | ★★★☆ | 0.14–0.42 | 6–9 | ___ |
| C5.5 | Digital maintenance work order | Mobile / digital maintenance work-order mgmt | Mobile order, workflow automation | Mobile app, workflow engine | ★★★★ | 0.14–0.42 | 3–6 | ___ |
| C5.6 | Electromechanical remote monitoring | Remote monitoring of signals / CCTV / lighting | Device monitoring, remote control | IoT platform, SCADA | ★★★★ | 0.28–0.70 | 6–9 | ___ |
| C5.7 | Infrastructure coding-standard mgmt | Unified coding & data standards | Coding system, data dictionary | MDM | ★★☆☆ | 0.14–0.42 | 6–9 | ___ |
| C5.8 | Bridge full-lifecycle digital archive | Design / build / operate / maintain digital archive | Digital archive, BIM linkage | Archive platform, BIM | ★★☆☆ | 0.28–0.70 | 6–12 | ___ |
| C5.9 | Infrastructure investment prioritization | Data-based investment prioritization | Multi-factor eval, ranking | Data-analysis platform | ★★☆☆ | 0.14–0.42 | 3–6 | ___ |
| C5.10 | Underground utility digitization | BIM / GIS for underground utilities | 3D utility modeling, clash detect | BIM / GIS, detection device | ★★☆☆ | 0.7–2.1 | 9–18 | ___ |

**C5 subtotal: ___/40**

---

### C6: Enforcement & Safety (10 scenarios)
| ID | Scenario | Description | Key Capability | Tech Needs | Maturity | Invest ($M) | Months | Self |
|----|---------|-------------|----------------|-----------|----------|-------------|--------|------|
| C6.1 | AI non-site enforcement | AI auto-detection & evidence of violations | Video analysis, violation ID | Video AI, evidence platform | ★★★★ | 0.7–2.8 | 6–12 | ___ |
| C6.2 | Quick crash handling & claim | Fast handling / liability / claim for minor crashes | Liability, online claim | Quick-handling platform, video | ★★★★ | 0.28–0.70 | 6–9 | ___ |
| C6.3 | Road-safety risk situation | Citywide safety-risk situational awareness & hotspots | Risk modeling, hotspot analysis | GIS, risk engine | ★★★☆ | 0.42–1.12 | 6–12 | ___ |
| C6.4 | Hazard-point identification | Data-based automatic hazard-point ID | Crash analysis, hazard ID | Data-analysis platform | ★★★☆ | 0.14–0.42 | 3–6 | ___ |
| C6.5 | Digital emergency plan | Digital emergency plans & automated response flow | Digital plan, workflow automation | Emergency mgmt platform | ★★★☆ | 0.14–0.42 | 3–6 | ___ |
| C6.6 | Emergency command & dispatch | Multi-agency emergency linked command | Multi-agency linkage, resource dispatch | Command platform, GIS | ★★★★ | 0.7–2.1 | 6–12 | ___ |
| C6.7 | Regulated-vehicle smart supervision | Smart supervision of dump / hazmat / school buses | Geo-fence, route monitoring | IoT terminal, supervision platform | ★★★★ | 0.42–1.40 | 6–9 | ___ |
| C6.8 | Illegal-parking auto capture | Auto capture & reminder in no-park zones | CV detection, auto evidence | Video AI, geo-fence | ★★★★★ | 0.28–0.70 | 3–6 | ___ |
| C6.9 | Pedestrian / micromobility enforcement | Jaywalking / micromobility violation monitoring | Video analysis, face ID | Video AI, identity DB | ★★★☆ | 0.28–0.70 | 3–6 | ___ |
| C6.10 | Drunk / drug-driving prevention | Digital prevention & detection | Linked alcohol test, data mgmt | IoT device, mgmt platform | ★★☆☆ | 0.14–0.42 | 3–6 | ___ |

**C6 subtotal: ___/40**

---

### C7: Mobility-as-a-Service (10 scenarios)
| ID | Scenario | Description | Key Capability | Tech Needs | Maturity | Invest ($M) | Months | Self |
|----|---------|-------------|----------------|-----------|----------|-------------|--------|------|
| C7.1 | One-stop mobility app | Portal integrating bus / metro / taxi / bike / parking | Multi-modal integration, unified pay | App / mini-program, payment gateway | ★★★☆ | 0.7–2.8 | 9–18 | ___ |
| C7.2 | Real-time bus / metro info | Real-time arrival & crowding queries | Real-time fusion, ETA calc | Data API, compute engine | ★★★★ | 0.14–0.56 | 3–6 | ___ |
| C7.3 | Multi-modal trip planning | Bus + metro + walk + bike trip planning | Multi-modal routing algo | Routing engine | ★★★☆ | 0.28–0.70 | 6–9 | ___ |
| C7.4 | MaaS unified payment | Frictionless / post-pay across modes | Unified payment, credit system | Payment platform, credit scoring | ★★★☆ | 0.42–1.12 | 9–12 | ___ |
| C7.5 | Carbon-credit / green-mobility incentive | Green-mobility incentive via carbon credits | Carbon-credit calc, incentive issue | Carbon platform, rewards store | ★★★☆ | 0.28–0.70 | 6–9 | ___ |
| C7.6 | Accessible / senior mobility | Age-friendly & accessible MaaS | Accessibility info, voice interaction | Senior-friendly UI, voice engine | ★★☆☆ | 0.14–0.42 | 3–6 | ___ |
| C7.7 | Shared-mobility integration | Unified access to bike / ride-hail / car-share | Shared-mobility API integration | API mgmt, data fusion | ★★★☆ | 0.28–0.70 | 6–9 | ___ |
| C7.8 | Dynamic mobility package / subscription | Monthly / annual mobility packages | Package design, benefit mgmt | Billing engine, benefit mgmt | ★★☆☆ | 0.28–0.70 | 6–9 | ___ |
| C7.9 | MaaS operations analytics | Operation analytics & user profiling | User analysis, funnel analysis | Data-analysis platform | ★★★☆ | 0.14–0.42 | 3–6 | ___ |
| C7.10 | Scenic / commercial-district mobility | Custom mobility for tourism / commercial | Scenario service package | Customized platform | ★★☆☆ | 0.14–0.70 | 3–9 | ___ |

**C7 subtotal: ___/40**

---

### C8: Logistics & Freight (10 scenarios)
| ID | Scenario | Description | Key Capability | Tech Needs | Maturity | Invest ($M) | Months | Self |
|----|---------|-------------|----------------|-----------|----------|-------------|--------|------|
| C8.1 | Digital freight platform | Internet + freight matching & capacity mgmt | Source / capacity matching | Freight platform, app | ★★★★ | 0.7–2.8 | 9–18 | ___ |
| C8.2 | Multimodal single-document | Road-rail-water-air e-waybill, through-bill | Waybill standardization, data flow | Blockchain, EDI | ★★☆☆ | 0.7–2.8 | 12–24 | ___ |
| C8.3 | Urban green delivery | Permit mgmt / routing / NEV promotion for urban delivery | Delivery mgmt, route opt. | Delivery platform | ★★★☆ | 0.28–0.70 | 6–9 | ___ |
| C8.4 | Port / terminal logistics digitization | Digital warehousing & dispatch at ports / dry ports / airports | WMS / TOS, vehicle dispatch | Logistics platform, IoT | ★★★☆ | 1.40–7.0 | 12–24 | ___ |
| C8.5 | Hazmat transport supervision | End-to-end digital supervision of hazmat | Full tracking, safety warning | IoT terminal, supervision platform | ★★★★ | 0.42–1.40 | 6–12 | ___ |
| C8.6 | Cold-chain monitoring | Temperature / location monitoring of cold chain | Temp-humidity monitoring, warning | IoT sensor, temp platform | ★★★★ | 0.14–0.70 | 3–6 | ___ |
| C8.7 | Truck remote weigh-in-motion | Non-stop overload detection | WIM weighing, AI recognition | Dynamic scale, AI | ★★★★ | 0.7–2.8 | 6–12 | ___ |
| C8.8 | Autonomous delivery | Autonomous vehicle / drone last-mile delivery | Auto delivery, routing | AV / drone, dispatch platform | ★★☆☆ | 0.7–4.2 | 12–24 | ___ |
| C8.9 | Freight big-data analytics | Freight OD / commodity / flow analytics | Freight economics, forecasting | Big-data platform | ★★☆☆ | 0.28–0.70 | 6–9 | ___ |
| C8.10 | Road-freight carbon tracking | Freight emission monitoring & footprint tracking | Emission calc, carbon labeling | Carbon platform | ★☆☆☆ | 0.28–0.70 | 9–12 | ___ |

**C8 subtotal: ___/40**

---

### C9: Parking Management (8 scenarios)
| ID | Scenario | Description | Key Capability | Tech Needs | Maturity | Invest ($M) | Months | Self |
|----|---------|-------------|----------------|-----------|----------|-------------|--------|------|
| C9.1 | On-street smart parking | On-street detection + charging + enforcement | Space detection, auto billing | Magnetometer / overhead video, platform | ★★★★ | 0.7–2.8 | 6–12 | ___ |
| C9.2 | Off-street lot networking | Unified lot data access & publishing | Data access, standardization | Data gateway | ★★★★ | 0.28–1.12 | 3–6 | ___ |
| C9.3 | City parking guidance | 3-tier parking guidance (arterial / sub / entrance) | Vacancy stats, guidance publish | VMS, data platform | ★★★★ | 0.42–1.40 | 6–9 | ___ |
| C9.4 | Shared / off-peak parking | Office / residential / mall space sharing | Sharing match, permission mgmt | Sharing platform, app | ★★★☆ | 0.28–0.70 | 6–9 | ___ |
| C9.5 | Reserved parking | Pre-book spaces at hospitals / key sites | Booking mgmt, credit framework | Booking platform | ★★★☆ | 0.28–0.70 | 6–9 | ___ |
| C9.6 | Frictionless parking payment | Auto-charge via plate recognition | Plate recognition, password-free pay | Payment gateway, OCR | ★★★★ | 0.14–0.42 | 3–6 | ___ |
| C9.7 | EV-charger space mgmt | Integrated EV-charger space mgmt & booking | Charger mgmt, space linkage | Charging platform, IoT | ★★★☆ | 0.28–1.12 | 6–12 | ___ |
| C9.8 | Parking big-data analytics | Behavior analysis / demand forecast / pricing opt. | Demand modeling, price elasticity | Big-data platform | ★★☆☆ | 0.14–0.42 | 3–6 | ___ |

**C9 subtotal: ___/32**

---

### C10: Transport Planning & Decision (10 scenarios)
| ID | Scenario | Description | Key Capability | Tech Needs | Maturity | Invest ($M) | Months | Self |
|----|---------|-------------|----------------|-----------|----------|-------------|--------|------|
| C10.1 | Planning data platform | Aggregation of comprehensive planning data | Multi-source aggregation, viz | Data platform, GIS | ★★★☆ | 0.42–1.12 | 6–12 | ___ |
| C10.2 | Demand forecasting model | Big-data based demand forecasting | 4-step / activity-based | Model engine | ★★★★ | 0.28–0.70 | 6–9 | ___ |
| C10.3 | Simulation evaluation | Micro / meso / macro simulation | Sim modeling, plan eval | Sim SW (PTV Vissim / TransCAD) | ★★★★ | 0.28–1.40 | 6–12 | ___ |
| C10.4 | AI-assisted design | AI-assisted road / intersection design | Generative AI, plan opt. | AI + CAD platform | ★☆☆☆ | 0.42–1.12 | 12–18 | ___ |
| C10.5 | Digital traffic-impact review | Digital transport-impact review of projects | Auto eval, report gen | Evaluation platform | ★★☆☆ | 0.14–0.42 | 3–6 | ___ |
| C10.6 | Policy-effect evaluation | Simulate / evaluate restriction / plate / toll policies | Policy modeling, effect eval | Sim platform, data analysis | ★★☆☆ | 0.28–0.70 | 6–12 | ___ |
| C10.7 | Investment decision support | Data-based investment prioritization & portfolio opt. | Portfolio opt., multi-factor eval | Decision-support platform | ★★☆☆ | 0.28–0.70 | 6–9 | ___ |
| C10.8 | Automated white-paper / yearbook | Auto data aggregation & layout of annual reports | Auto aggregation, report automation | Reporting platform | ★★★☆ | 0.07–0.28 | 3–6 | ___ |
| C10.9 | City-checkup transport metrics | Auto calc & eval of transport metrics in city checkup | Metric system, auto calc | Compute engine | ★★☆☆ | 0.14–0.42 | 3–6 | ___ |
| C10.10 | Digital-twin planning | Digital-twin based plan simulation & eval | Digital twin, simulation | Digital-twin platform | ★★☆☆ | 1.40–7.0 | 18–36 | ___ |

**C10 subtotal: ___/40**

---

### C11: Green Transport & Carbon Management (8 scenarios)
| ID | Scenario | Description | Key Capability | Tech Needs | Maturity | Invest ($M) | Months | Self |
|----|---------|-------------|----------------|-----------|----------|-------------|--------|------|
| C11.1 | Carbon-emission monitoring platform | Real-time city transport CO2 monitoring & stats | Emission accounting, data collection | Carbon platform | ★★☆☆ | 0.42–1.12 | 6–12 | ___ |
| C11.2 | Green-mobility carbon credit | Carbon-credit incentive for walk / bike / transit | Credit calc, incentive ops | Carbon-credit platform | ★★★☆ | 0.28–0.70 | 6–9 | ___ |
| C11.3 | NEV monitoring & mgmt | EV / FCEV operation monitoring & analysis | Telematics data collection | NEV telematics platform | ★★★★ | 0.28–0.70 | 6–9 | ___ |
| C11.4 | Smart charging-infra mgmt | Smart O&M & dispatch of chargers / swap stations | Device monitoring, smart dispatch | IoT platform, charging mgmt | ★★★☆ | 0.28–1.12 | 6–12 | ___ |
| C11.5 | Peak-carbon path simulation | Emission-trend simulation & peak-path comparison | Peak-carbon modeling, scenarios | Carbon-sim platform | ★★☆☆ | 0.28–0.70 | 6–12 | ___ |
| C11.6 | Low-carbon zone mgmt | Low-carbon demo-zone emission monitoring & eval | Zone emission monitoring, effect eval | Monitoring device, eval platform | ★★☆☆ | 0.42–1.40 | 9–18 | ___ |
| C11.7 | Carbon-trading support | Transport carbon-allowance mgmt & trading decision | Allowance calc, trading support | Carbon-asset platform | ★☆☆☆ | 0.14–0.70 | 6–12 | ___ |
| C11.8 | Green-transport certification | Digital eval of green-transport city / enterprise | Metric system, auto scoring | Evaluation platform | ★★☆☆ | 0.14–0.42 | 3–6 | ___ |

**C11 subtotal: ___/32**

---

### C12: Frontier Technology Innovation (10 scenarios)
| ID | Scenario | Description | Key Capability | Tech Needs | Maturity | Invest ($M) | Months | Self |
|----|---------|-------------|----------------|-----------|----------|-------------|--------|------|
| C12.1 | V2X cooperative-ITS | C-V2X vehicle-infra comm & cooperative apps | V2X comm, cooperative apps | RSU / OBU, comms network | ★★★☆ | 2.8–7.0 | 18–36 | ___ |
| C12.2 | AV open-testing zone | Digital infra for AV testing | Test scenario library, data capture | Roadside sensing, data platform | ★★★☆ | 4.2–14.0 | 18–36 | ___ |
| C12.3 | Transport digital-twin platform | City / highway digital-twin platform | Twin modeling, real-time fusion | Twin engine, GPU | ★★☆☆ | 2.8–7.0 | 12–24 | ___ |
| C12.4 | Transport domain LLM | Train & deploy a transport-specific LLM | LLM fine-tune, RAG | GPU cluster, LLM framework | ★★☆☆ | 0.7–4.2 | 9–18 | ___ |
| C12.5 | Blockchain transport apps | Blockchain for data sharing / supply chain | Blockchain platform, smart contract | Blockchain infra | ★★☆☆ | 0.28–1.40 | 6–12 | ___ |
| C12.6 | Low-altitude economy (UAV) | UAV in logistics / inspection / traffic mgmt | UAV platform, UTM | UAV, comms, UTM platform | ★★☆☆ | 0.7–4.2 | 12–24 | ___ |
| C12.7 | Quantum-comm transport apps | Quantum-encrypted transport info security | Quantum encryption, QKD | Quantum-comm device | ★☆☆☆ | 1.40–7.0 | 24–36 | ___ |
| C12.8 | 6G / ISAC | 6G integrated sensing-communication in transport | ISAC | 6G / ISAC device | ★☆☆☆ | 1.40–7.0 | 36+ | ___ |
| C12.9 | Transport metaverse apps | VR / AR / MR in training & design | VR / AR dev, 3D rendering | VR / AR device, 3D engine | ★☆☆☆ | 0.28–1.40 | 6–12 | ___ |
| C12.10 | Embodied-AI O&M | Embodied-AI robots for facility O&M | Embodied AI, robot control | Robot HW, AI algorithm | ★☆☆☆ | 0.7–4.2 | 12–24 | ___ |

**C12 subtotal: ___/40**

---

## 3. Benchmark Aggregation

### 3.1 Chain Score Summary
| Chain | # Scenarios | Max | Self | Rate | Industry Avg | Gap | Priority |
|-------|-------------|-----|------|------|--------------|-----|----------|
| C1 Integrated Ops Monitoring | 15 | 60 | ___ | ___% | 35–45 | ___ | ___ |
| C2 Urban Traffic Control | 15 | 60 | ___ | ___% | 30–42 | ___ | ___ |
| C3 Transit Operations | 12 | 48 | ___ | ___% | 28–36 | ___ | ___ |
| C4 Highway / Motorway Ops | 12 | 48 | ___ | ___% | 25–35 | ___ | ___ |
| C5 Infrastructure Mgmt | 10 | 40 | ___ | ___% | 18–28 | ___ | ___ |
| C6 Enforcement & Safety | 10 | 40 | ___ | ___% | 25–32 | ___ | ___ |
| C7 MaaS | 10 | 40 | ___ | ___% | 15–25 | ___ | ___ |
| C8 Logistics & Freight | 10 | 40 | ___ | ___% | 15–22 | ___ | ___ |
| C9 Parking Mgmt | 8 | 32 | ___ | ___% | 15–22 | ___ | ___ |
| C10 Planning & Decision | 10 | 40 | ___ | ___% | 18–25 | ___ | ___ |
| C11 Green & Carbon | 8 | 32 | ___ | ___% | 8–15 | ___ | ___ |
| C12 Frontier Innovation | 10 | 40 | ___ | ___% | 5–12 | ___ | ___ |
| **Total** | **130** | **520** | **___** | **___%** | **~45–58%** | | |

### 3.2 Maturity Distribution
| Score | # Scenarios | Share | Example |
|-------|-------------|-------|---------|
| 4 (Leading) | ___ | ___% | |
| 3 (Advanced) | ___ | ___% | |
| 2 (Partial) | ___ | ___% | |
| 1 (Basic) | ___ | ___% | |
| 0 (Not started) | ___ | ___% | |

### 3.3 Gap & Priority Analysis
| # | Biggest-gap Scenario | Current | Target | Gap | Largest industry-gap area |
|---|----------------------|---------|--------|-----|---------------------------|
| 1 | | __ | __ | 4 | |
| 2 | | __ | __ | 3 | |
| 3 | | __ | __ | 3 | |
| 4 | | __ | __ | 3 | |
| 5 | | __ | __ | 3 | |

---

## 4. Scenario → System → Vendor Quick Mapping
| Core Scenario | Core System | Vendor Category | Example Vendors |
|--------------|-------------|-----------------|-----------------|
| Traffic ops monitoring (TMC) | Big-data platform + visualization | Smart-mobility / transport tech | Siemens Mobility, Thales, Cisco, Cubic, IBM |
| Signal control | Traffic signal control system | Signal-control specialist | Siemens Mobility, Swarco, Yunex, Iteris, Q-Free, Bosch |
| Transit dispatch | Smart transit dispatch system | Transit IT | Clever Devices, Trapeze (Conduent), Init (Siemens), GMV |
| Smart motorway | Integrated motorway control platform | Motorway tech | Kapsch, TransCore, Siemens Mobility, Thales, Yunex |
| Parking mgmt | City parking platform | Parking tech | Flowbird, Scheidt & Bachmann, ParkMobile, T2 Systems, Indra |
| MaaS mobility | MaaS platform | Maps + payment + mobility | Moovit, Google Maps, Citymapper, Whim, Transit |
| Enforcement | Non-site enforcement platform | Security / enforcement | Axis, Genetec, Bosch, Hexagon |
| Simulation | Traffic simulation software | Sim vendor | PTV Group, Transoft, Aimsun, Citilabs |
| Digital twin | Digital-twin platform | Twin / visualization | Bentley, Hexagon, Unity, NVIDIA Omniverse, Cityzenith |
| AI apps | AI platform + algorithms | AI / big-data | Microsoft Azure, AWS, Google Cloud, IBM, Palantir, NVIDIA |
| LLM | LLM platform | LLM / cloud vendor | OpenAI, Anthropic, Google Gemini, Meta Llama, Azure OpenAI |
| Carbon monitoring | Carbon-mgmt platform | Environment / carbon tech | ICROA, Verra, South Pole, Watershed, Persefoni |

---

## 5. Industry Benchmark Snapshot
| Scenario Group | Global Benchmark | City / Org | Benchmark Point |
|---------------|-----------------|-----------|-----------------|
| Integrated TMC | London TfL / Singapore LTA | London / Singapore | Digital twin + AI + 100+ cross-agency scenarios |
| Signal control | Pittsburgh Surtrac / London SCOOT | Pittsburgh / London | Citywide AI signal optimization |
| Transit dispatch | LA Metro / TfL buses | Los Angeles / London | DRT + AI scheduling |
| MaaS | Helsinki Whim | Helsinki | Carbon credits + MaaS |
| Smart motorway | A14 Brescia–Bologna / Colorado smart corridor | Italy / Colorado | All-weather + V2X |
| Parking | San Francisco / Amsterdam | San Francisco / Amsterdam | Hospital reservation + frictionless pay |
| Enforcement | London / Singapore | London / Singapore | Full-scenario AI enforcement |
| Digital twin | Helsinki / Singapore digital twins | Helsinki / Singapore | Urban digital twin |
| Carbon mgmt | Transport carbon programs (e.g., Chooose, MaaS credits) | Global | Carbon-credit emission reduction trading |
| Low-altitude economy | Drone-delivery programs (Zipline, Wing, Dubai RTA) | Global | UAV logistics + UTM + regulation |

---

## 6. Implementation Notes
1. **Self-scoring**: Joint business + technical team scores each scenario independently (0–4).
2. **External validation**: Invite external experts / consultants to independently validate key scenarios.
3. **Benchmark**: Reference Section 5 global benchmarks and Section 3 industry averages.
4. **Gap analysis**: Flag "not started / basic" (≤1) and scenarios with industry gap > 2.
5. **Prioritize**: Rank by business impact, cost, and maturity.
6. **Roadmap**: Build a 3-year digital-transformation roadmap with phased target scenarios.
7. **Re-assess**: Full re-assessment every 12 months.
