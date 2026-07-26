# Smart Bus Construction Proposal

> **Version**: V1.0
> **Date**: ____/__/__
> **Prepared by**: _________
> **Reviewed by**: _________
> **Approved by**: _________

---

## Executive Summary

### Project Positioning
The [City Name] smart-bus program uses digital transformation to improve efficiency, safety, and service — building an "intelligent dispatch + precise service + safety control + green low-carbon" smart-bus system.

### Objectives
By [target year], achieve:
- Punctuality: from ____% to ____%
- Passenger satisfaction: from ____ to ____ /100
- Operating cost: cost per vehicle-km down ____%
- Modal share: from ____% to ____%
- Safety incidents: down ____%
- Electrification rate: reach ____%

### Investment Overview
| Item | Value |
|------|------|
| Total estimated investment | $____ million |
| Construction period | ____ months |
| Annual benefit (saving + uplift) | $____ million / year |
| Payback period | ____ years |

---

## 1. City Bus Status

### 1.1 Basic Information
| Item | Detail |
|------|------|
| Operator | [company name] |
| Routes | ____ (BRT ____ / standard ____ / micro ____ / custom ____) |
| Route length | ____ km |
| Fleet | ____ vehicles (EV ____, share ____%) |
| Daily ridership | ____ million |
| Modal share | ____% (all-mode trips) |
| Annual mileage | ____ ×10³ vehicle-km |
| Annual revenue | $____ million |
| Annual public subsidy | $____ million |
| Fare structure | Flat $__ / transfer discount / senior free, etc. |
| Payment | Cash / smart card / QR / NFC / bank card |
| Depots | Hub ____ / terminus ____ / stabling ____ / charge ____ |

### 1.2 Existing Systems
| System | Supplier | Year | Coverage | Health (1–5) |
|------|--------|----------|------|:-----------:|
| Intelligent dispatch | | | | |
| Card / ticketing | | | | |
| Onboard GPS / GNSS | | | | |
| Onboard video | | | | |
| Electronic stop sign | | | | |
| Real-time bus app link | | | | |
| ERP / finance | | | | |
| Charge mgmt | | | | |
| Maintenance | | | | |
| Safety mgmt | | | | |

### 1.3 Core Pain Points
| Pain | Symptom | Impact |
|------|------|------|
| Ridership decline | Bike-share / ride-hail / metro diversion | Revenue down, subsidy pressure |
| Coarse dispatch | Manual experience, headway / capacity mismatch | Peak crowding + off-peak empty |
| Poor perception | Inaccurate arrival / crowding / environment | Low satisfaction |
| Safety risk | Driver fatigue / distraction / violation | Safety hazard |
| High cost | Labor >50% + energy | Hard business |
| New modes | Ride-hail / bike-share / DRT diversion | Traditional model unsustainable |

---

## 2. Goals and Architecture

### 2.1 Goals
| Dimension | Metric | Baseline | Target | Means |
|----------|------|:---:|:---:|------|
| Efficiency | Cost per veh-km ($/veh-km) | | | Smart dispatch + EV |
| Efficiency | Peak load-balance | | | AI dispatch + express |
| Service | Arrival-time accuracy | | | Real-time bus + signal priority |
| Service | Satisfaction (/100) | | | App + info + environment |
| Safety | Crashes per M veh-km | | | ADAS + DSM + safety mgmt |
| Safety | Speeding / fatigue / violation count | | | Active safety |
| Green | Electrification rate | | | EV + smart charge |
| Green | CO₂ per veh-km | | | EV + eco-driving |
| Innovation | Non-fare revenue share | | | MaaS + data + commercial |

### 2.2 Architecture
```
┌────────────────────────────────────────────────────────────┐
│  Application Layer                                            │
│  ┌──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐│
│  │Smart │Real- │Smart │Signal│Safety│Pass. │Data  │MaaS  ││
│  │dispatch│bus  │ticket│prio. │mgmt  │service│net   │integ.││
│  └──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘│
├────────────────────────────────────────────────────────────┤
│  Platform Layer                                               │
│  ┌──────────┬──────────┬──────────┬──────────┬──────────┐  │
│  │IoT       │Big-data  │AI/ML     │GIS       │Payment   │  │
│  │onboard   │flow anal.│forecast/ │net/status│aggregate │  │
│  │mgmt      │          │optimize  │          │settle    │  │
│  └──────────┴──────────┴──────────┴──────────┴──────────┘  │
├────────────────────────────────────────────────────────────┤
│  Communication Layer                                          │
│  ┌──────────┬──────────┬──────────┬──────────────────────┐  │
│  │4G/5G     │DSRC/V2X  │Wi-Fi/BLE │CAN/Ethernet (in-vehicle)│  │
│  └──────────┴──────────┴──────────┴──────────────────────┘  │
├────────────────────────────────────────────────────────────┤
│  Terminal Layer                                               │
│  ┌──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐│
│  │GPS   │Video │CAN   │ADAS  │DSM   │Pay   │Sign  │App   ││
│  └──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘│
└────────────────────────────────────────────────────────────┘
```

---

## 3. Subsystem Detailed Design

### 3.1 Intelligent Dispatch

#### 3.1.1 AI Dispatch Optimization
| Direction | Traditional | AI | Expected |
|----------|----------|--------|----------|
| Headway | Fixed / peak-off-peak table | Real flow + history + AI dynamic | Load balance +20% |
| Capacity match | Fixed fleet | Real flow + OD + AI recommend | Cost −10% |
| Timetable | Manual | AI assist + sim validate | 5× faster |
| Vehicle dispatch | Manual | Auto match vehicle + driver + shift | 3× faster |
| Emergency dispatch | Manual + phone | Auto detect + AI alt + one-tap | Response −70% |
| Express / short-turn | Experience | AI peak-section + express recommend | Section capacity +15% |

#### 3.1.2 Dispatch Functions
| Module | Description |
|----------|----------|
| Real-time monitor | All vehicles GPS / GNSS + speed + dir + flow on GIS |
| Planning & shift | Timetable / vehicle / driver scheduling + auto-check (hours / rules / rest) |
| Real-time dispatch | Traffic monitor / big-gap alert / auto headway / cross-line / short-turn |
| Stats | Ops KPI dashboard: punctuality / veh-km / pax-km / load / energy / revenue |
| Video linkage | Dispatch pulls any vehicle video |

### 3.2 Real-Time Bus Info

#### 3.2.1 Arrival Forecast
| Element | Source | Algorithm | Target |
|----------|----------|------|:------:|
| Arrival time | GPS/GNSS + history + live traffic + signal | Time-series + LSTM / GBDT | Err <1 min (within 15 min) |
| In-vehicle crowding | Card / QR + video AI + load sensor | Fusion + OD model | >85% |
| Line / stop crowding | Same | Same | >85% |
| Delay forecast | GPS + traffic + signal + weather + event | Multi-factor | 15 min early |

#### 3.2.2 Channels
| Channel | Content | Frequency | Tech |
|------|------|:--------:|----------|
| E-stop sign | Line / arrival / crowding / weather / notice | Real-time | LCD/LED + 4G |
| Mobile app | Line / real-time / crowding / transfer / arrival alert | Real-time | Own app + Google/TomTom + mobile web |
| In-vehicle screen | Next stop / map / transfer / arrival | Real-time | LCD + auto-announce |
| Platform PA | Arrival / safety / emergency | Real-time | Speaker / directional |
| Voice query | Seniors call hotline voice query | Real-time | IVR + AI voice |

### 3.3 Smart Ticketing

#### 3.3.1 Diverse Payment
| Method | Tech | Target | Pro | Challenge |
|----------|----------|:--------:|------|------|
| Smart card | Open-loop EMV / ITSO / Calypso | Installed base | Mature / offline | Recharge / loss |
| QR | Wallet / bank / city app | Mainstream | No card | Network / scan speed |
| NFC | Phone / watch / bank card | Growing | Convenient / EMV | Terminal coverage |
| Face | 1:N + liveness + account | Pilot | Frictionless / hygienic | Privacy / enrol / light |
| Palm / vein | Contactless + secure | Exploring | Hygienic / secure | Cost / enrol / std |

#### 3.3.2 Ticketing Management
| Function | Description |
|------|------|
| Unified clearing | Multi-channel unified clearing / reconcile / settle / error |
| Fare policy | Flat / distance / transfer discount / concession / day / week / month pass |
| OD analysis | Card / QR infer OD matrix |
| Passenger profile | Frequency / time / line / transfer preference |
| Fare audit | Anomaly detect / fare-evasion / audit trace |

### 3.4 Bus Signal Priority

#### 3.4.1 Priority Strategies
| Strategy | Description | Use |
|------|------|------|
| Passive | Preset green-wave / bus phase in timing | Corridor / no detection |
| Active | Detect approaching → extend green / shorten red / insert phase | Detected junction |
| Adaptive | AI balance bus priority + general traffic (Pareto) | AI signal junction |
| Unconditional | Priority on arrival (BRT) | BRT lane |
| Conditional | Trigger only if late > X min | General line |

#### 3.4.2 Detection
| Method | Range | Accuracy | Cost | Use |
|----------|:------:|:---:|:---:|------|
| RFID | >300 m | >99% | Low | Roadside reader + onboard tag |
| DSRC (5.8 GHz) | >500 m | >99% | Med | National transit-priority std |
| C-V2X PC5 | >500 m | >99% | High | V2X city |
| GPS + geo-fence | Unlimited | 95% | Low | GPS covered, no high precision |

### 3.5 Fleet Management

#### 3.5.1 EV Charge Management
| Function | Description |
|------|------|
| Charge monitor | Charger status / power / SOC / record real-time |
| Smart charge | Time-of-use + dispatch + battery → optimal (off-peak / fast-slow mix) |
| Smart charging | Coordinate with grid, dynamic power (avoid peak-on-peak) |
| Battery health | SOC / SOH + temp + fault + life predict |
| V2G pilot | Retire-before / surplus capacity discharge to grid |

#### 3.5.2 Maintenance
| Function | Description |
|------|------|
| Preventive | Auto plan by mileage / time |
| Condition-based | PHM from onboard CAN / IoT |
| Work order | Auto → dispatch → repair → QA → settle |
| Spares | Inventory / consume / procure |
| Tire | RFID track + wear + retread decision |

### 3.6 Safety Management

#### 3.6.1 Active Safety (ADAS + DSM)
| Domain | Detection | Tech | Alert |
|----------|----------|------|----------|
| **Forward ADAS** | Forward collision (FCW) | Stereo / mono + radar | Sound + light + brake pre-tension |
| | Lane departure (LDW) | Vision lane | Sound + light |
| | Headway too close (HMW) | Vision + radar | Sound + light |
| | Pedestrian (PCW) | Vision + radar + AI | Sound + light + brake |
| | Speed-sign (TSR) | Vision AI + map speed | Overspeed alarm |
| **Driver DSM** | Fatigue (eye close / yawn) | IR vision + AI keypoint | Sound + light + vibrate + platform |
| | Distraction (phone / smoke / glance) | Same | Sound + light + platform |
| | Abnormal driving (harsh accel/brake/turn) | CAN + IMU + GPS | Sound + platform |
| | Driver ID | Face | Unauthorized cannot start |
| **Right blind spot** | Pedestrian / bike right side | Vision + ultrasonic / radar | Sound + light + external speaker |
| **Cabin safety** | Cabin anomaly (fight / fall / item / crowd) | Cabin video AI | Platform + PA |
| | Panic button | Driver / passenger trigger | Audible + platform + police link |

#### 3.6.2 Safety Closed Loop
```
Risk ID → real-time alert → platform log → work order → training → KPI → data review
```

### 3.7 Passenger Service

#### 3.7.1 App Functions
| Module | Description |
|----------|----------|
| Real-time bus | Nearby lines / stops / vehicle / arrival / crowding |
| Trip plan | Origin → dest multimodal (bus + metro + walk + bike + ride-hail) |
| Ticketing | Scan ride / e-card / top-up / buy / e-invoice |
| Custom bus | Demand submit + line vote + book + pay (DRT) |
| Info | Notice / line change / lost & found / survey |
| Profile | Ride / spend / points / coupon / loyal benefits |

#### 3.7.2 In-Vehicle Info
| Device | Function |
|------|------|
| LCD screen | Map / position / next stop / arrival / transfer / ad / public |
| Wi-Fi | Free Wi-Fi (4G/5G CPE) |
| USB charge | Seat USB |
| PA | Auto announce + safety + weather |

### 3.8 Analytics and Network Optimization

#### 3.8.1 Analysis System
| Topic | Content | Source | Freq |
|----------|----------|--------|:----:|
| Flow | OD / section / transfer / spatiotemporal / trend | Card + QR + video | D/W/M |
| Network | Coverage / duplication / directness / access / connection | Network + flow + GIS | Q/Yr |
| Efficiency | Veh-km / pax-km / load / punctuality / energy / cost | Dispatch + ticket + CAN | D/W/M |
| Profile | Frequency / time / line / transfer / pay pref. | Ticket + app | M |
| Connection | Metro / bus / bike-share / ride-hail | Multi-source | Q |

#### 3.8.2 AI Network Optimization
| Scenario | AI | Input | Expected |
|----------|--------|----------|----------|
| Network | Multi-objective (coverage + efficiency + cost) | OD + network + road + cost | Line-change proposal |
| Stop | Stop spacing / position / connection | Walk access + OD | Stop optimization |
| Fare | Elasticity + revenue | Fare + flow + competition | Fare proposal |
| Subsidy | Cost + fare + policy subsidy | Cost + revenue | Subsidy rationale |

### 3.9 DRT (Demand-Responsive Transit) Pilot

#### 3.9.1 Modes
| Mode | Description | Use |
|------|------|----------|
| Micro feeder | Metro / hub → residential / office short feeder | Last mile |
| Low-density | Suburb / industrial / scenic not covered | Low density / night |
| Peak custom | Commuter residential → CBD direct | Peak commute |
| Instant hail | Ride-hail-like instant bus | Off-peak low demand |
| Booking | Book [30 min / 1 h / 1 d] ahead shared bus | Predictable demand |

#### 3.9.2 DRT Platform
| Function | Description |
|------|------|
| User | Hail → match → dynamic route → guide → pay → rate |
| Backend | Order aggregate → dynamic route → vehicle-order match → dispatch → capacity monitor |
| Pricing | Dynamic (distance + time + sharing + peak surge) |

### 3.10 MaaS Integration

#### 3.10.1 MaaS Consolidation
| Mode | Content | Depth |
|--------------|----------|:--------:|
| Bus | Live position / arrival / line / fare / pay | Deep (own) |
| Metro / light rail | Live timetable / fare / crowding | Medium (data link) |
| Bike-share | Stations / available / unlock | Medium (API) |
| Ride-hail / taxi | One-tap hail / est. price | Medium (API) |
| Intercity | Train / coach / flight schedule | Light (info) |
| P+R park & ride | Parking + bus bundle | Medium (data + pay) |

#### 3.10.2 MaaS Unified Payment
| Method | Description |
|----------|------|
| Unified account | One account binds multi-mode pay + points + loyal benefits |
| Mileage exchange | Bus / metro / bike-share mileage / points fungible |
| Package | Bus + metro + bike-share commute pass |
| One-code pass | One QR for bus / metro / P+R parking |

---

## 4. Implementation Plan

| Phase | Time | Content | Investment | Milestone |
|------|------|------|:----:|--------|
| 1 | ____/__–__ | Dispatch upgrade + real-time bus full cover + e-stop (key) + ticketing (QR/NFC) + ADAS/DSM pilot (100 veh) | $___k | Core online |
| 2 | ____/__–__ | Signal priority (core corridor) + PHM + DRT pilot (low density) + MaaS + EV scale | $___k | Intelligence up |
| 3 | ____/__–__ | AI network optimization + AI dispatch full + DRT expand + V2X + V2G + data assetization | $___k | Innovation works |

---

## 5. Investment Estimate

### 5.1 Breakdown
| # | Item | Estimate ($k) | Share |
|:---:|------|:----------:|:---:|
| 1 | Intelligent dispatch upgrade | $____ | __% |
| 2 | Onboard terminal (GPS / video / CAN / DVR) | $____ | __% |
| 3 | ADAS + DSM active safety | $____ | __% |
| 4 | Smart ticketing (POS upgrade + face pilot) | $____ | __% |
| 5 | Electronic stop signs | $____ | __% |
| 6 | Passenger app / mobile web | $____ | __% |
| 7 | Bus signal priority | $____ | __% |
| 8 | EV charge mgmt platform | $____ | __% |
| 9 | PHM maintenance | $____ | __% |
| 10 | DRT / MaaS platform | $____ | __% |
| 11 | Data center / cloud | $____ | __% |
| 12 | Cyber security | $____ | __% |
| 13 | Integration + 3rd-party test | $____ | __% |
| 14 | Training | $____ | __% |
| 15 | Contingency | $____ | __% |
| | **Total** | **$____** | **100%** |

### 5.2 Benefit Analysis
| Type | Item | Annual quantified |
|----------|--------|:----------:|
| Economic | Ops cost saving (fuel / power / labor / maint) | $____k |
| Economic | Fare revenue growth (ridership + less evasion) | $____k |
| Economic | Non-fare (ad + data + charge) | $____k |
| Social | Passenger time saving | ____k h / yr |
| Social | Carbon reduction | ____ t CO₂ / yr |
| Social | Fewer car trips | ____k trips / yr |
| Safety | Incidents reduced | ____ / yr |

---

> **Usage note**: This template fits a city bus group's smart-upgrade proposal. Bus ROI must combine ridership rebound, cost saving, and non-fare revenue; build a clear input-output chain. Replace `[placeholder]` with project data.

> **Legal notice**: This template is protected by applicable copyright law and is provided for personal study and reference only; commercial use requires the author's written permission.

> **Disclaimer**: This template is for study and reference only and does not constitute professional advice of any kind. Bus operations involve public safety; ADAS/DSM deployment needs thorough testing, and driver biometrics must comply with privacy regulation. The author accepts no liability for any loss arising from use of or reliance on this template.

> **Author**: yinjianheng | yinjianheng@foxmail.com
