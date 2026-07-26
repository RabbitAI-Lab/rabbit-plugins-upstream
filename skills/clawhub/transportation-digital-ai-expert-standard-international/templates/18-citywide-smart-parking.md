# Citywide Smart Parking Construction Proposal

> **Version**: V1.0
> **Date**: ____/__/__
> **Prepared by**: _________
> **Reviewed by**: _________
> **Approved by**: _________

---

## Executive Summary

### Project Positioning
The [City Name] citywide smart-parking program builds an integrated "on-street + off-street + guidance + platform" system, achieving one-network management of parking resources, one-tap space navigation, frictionless payment, and one-screen control.

### Objectives
By [target year], achieve:
- Parking spaces connected to city platform: ____ ×10³ (on-street ____k + off-street ____k)
- Unmanned on-street payment coverage: ____%
- Unmanned off-street payment coverage: ____%
- Guidance-system coverage: core district ____% / citywide ____%
- Space turnover: from ____ times/day to ____ times/day
- Fee collection rate: from ____% to ____%
- Shared (off-peak) spaces: ____ ×10³
- Average search time: from ____ min to ____ min

### Investment Overview
| Item | Value |
|------|------|
| Total estimated investment | $____ million |
| Construction period | ____ months |
| Forecast annual operating revenue | $____ million / year |
| Payback period | ____ years |
| Operating model | [public self-build / PPP / BOT / concession] |

---

## 1. City Parking Status

### 1.1 Basic Information
| Item | Detail |
|------|------|
| City name | [City Name] |
| Resident population | ____ million |
| Registered vehicles | ____ million (cars ____ million) |
| Urban area | ____ km² |
| Core urban area | ____ km² |

### 1.2 Supply–Demand Analysis
| Metric | Value | Benchmark | Conclusion |
|------|:----:|:------:|------|
| Total spaces | ____ ×10³ | | |
| Of which: built-on parking | ____ ×10³ | | |
| Of which: off-street public | ____ ×10³ | | |
| Of which: on-street | ____ ×10³ | | |
| Cars | ____ million | | |
| Spaces per car | ____ | 1.1–1.3 | [short / sufficient] |
| Core-district gap | ____ ×10³ | | [gap note] |
| Avg. search time | ____ min | <5 min | [gap] |
| On-street turnover | ____ /day | >5 /day | [low] |
| Fee collection rate | ____% | >90% | [low] |

### 1.3 Core Pain Points
| Pain | Symptom | Impact |
|------|------|------|
| Hard to find | Drivers spend ____ min searching | More non-recurrent traffic, emissions, poor UX |
| Revenue leakage | Manual on-street collection, high leakage | Loss to public / operator |
| Data silos | Lots operated independently, no interop | No city guidance, no sharing |
| Low turnover | Some areas occupy on-street spaces long | Core area worse |
| EV gap | Insufficient / faulty chargers | Slows EV adoption |
| Coarse mgmt | No data-driven fine management | No basis for planning / pricing / enforcement |

---

## 2. Overall Architecture

### 2.1 System Architecture
```
┌──────────────────────────────────────────────────────────────┐
│                 City Smart-Parking Cloud Platform              │
│  ┌──────────┬──────────┬──────────┬──────────┬─────────────┐ │
│  │Regulation│Operations │Guidance  │Data      │Public       │ │
│  │map       │platform  │network   │services  │services     │ │
│  └──────────┴──────────┴──────────┴──────────┴─────────────┘ │
├──────────────────────────────────────────────────────────────┤
│                       Data Middle Platform                     │
│  ┌──────────┬──────────┬──────────┬──────────┬─────────────┐ │
│  │Ingestion │Governance │Analytics │Sharing  │AI engine    │ │
│  │standard  │clean/qual │profile/  │API/open │demand/price │ │
│  │          │          │forecast  │         │/dispatch    │ │
│  └──────────┴──────────┴──────────┴──────────┴─────────────┘ │
├──────────────────────────────────────────────────────────────┤
│       On-street          │          Off-street                 │
│  ┌───┬───┬───┬──────┐  │  ┌──────┬──────┬──────┬──────────┐  │
│  │High│Mag.│Video│Patrol│  │ │Plate │ETC  │AGV  │Charger   │  │
│  │cam │    │post│ vehicle│  │ │recog.│pay  │park │integrated│  │
│  └───┴───┴───┴──────┘  │  └──────┴──────┴──────┴──────────┘  │
├──────────────────────────────────────────────────────────────┤
│                         Guidance                               │
│  ┌──────────┬──────────┬──────────┬──────────┬─────────────┐ │
│  │L1 sign   │L2 sign   │L3 sign   │Mobile app│In-vehicle   │ │
│  │(arterial)│(collector)│(lot ent.)│(nav+pay)│(map app)    │ │
│  └──────────┴──────────┴──────────┴──────────┴─────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

### 2.2 Technology Selection
| Domain | Recommended | Alternative | Sourcing | Scenario |
|--------|----------|----------|:--------:|----------|
| On-street detection | High-mast video + AI | Mag + patrol / video post | Local | Urban roads |
| Off-street detection | Plate recog. + ETC antenna | Video + BLE | Local | Lot / garage |
| Comms | 4G/5G + NB-IoT | LoRa / Wi-Fi | Partial local | Device backhaul |
| Payment | Aggregated pay (wallet / card / ETC) | Cash / card | Local | All |
| Platform | Cloud-native + microservice + big data | Monolith + bare metal | Partial local | Platform |
| AI | Plate / space / demand forecast | | Partial local | AI functions |

---

## 3. Subsystem Detailed Design

### 3.1 On-Street Parking

#### 3.1.1 Detection Comparison
| Option | High-mast video | Video post | Mag + patrol | Mag + PDA |
|------|:---:|:---:|:---:|:---:|
| Spaces per device | 8–12 / pole | 1–2 / post | 1 / sensor | 1 / sensor |
| Detection accuracy | >98% | >99% | >97% | >95% |
| Plate recognition | Yes | Yes | No | No |
| Evidence | Full (photo/video) | Full | Patrol photo needed | Manual photo |
| Install difficulty | Med (pole + power) | Low | Low (ground) | Low |
| Build cost / space | $200–500 | $300–600 | $80–150 | $50–100 |
| O&M cost | Low | Med | High (patrol) | High (manual) |
| Scenario | Arterial / CBD | Non-arterial | Backstreet | Remote / low density |

> **Recommended**: high-mast video for CBD / arterial; mag + patrol for non-arterial — balancing coverage and cost.

#### 3.1.2 On-Street Flow
```
Vehicle enters → high-mast / mag auto-detect → plate + start timer
    → app / SMS push parking info
    → vehicle leaves → auto stop timer → bill generated
    → app / mobile web / push payment notice
    → user pays online (wallet / card / ETC) or frictionless auto-debit
    → paid / overdue → arrears record → recovery
```

#### 3.1.3 Arrears Recovery
| Method | Description |
|------|------|
| SMS / app push | Auto push arrears reminder + payment link |
| Roadside patrol | Patrol posts reminder on arrears vehicle |
| Registry linkage | Link to vehicle-registry system; clear before inspection / transfer (needs legal basis) |
| Credit score | Link to city credit / mobility-credit system (some regions) |
| Legal action | Sue malicious large arrears |

### 3.2 Off-Street Parking

#### 3.2.1 Standard Parking Management
| Hardware | Function | Recommended |
|------|------|----------|
| Entry gate + plate recog. | Auto entry ID + raise | 3 MP + light + anti-crush radar |
| Exit gate + plate + ETC | Exit ID + ETC + aggregated pay | Same + ETC antenna |
| Space camera | Detect occupancy | 2–6 spaces / camera |
| Space sign | Floors / zones free count | Each floor entrance |
| Find-my-car terminal | Plate → location | Elevator / corridor |
| Indoor nav | App BLE / Wi-Fi / UWB | Beacons by area |
| Pay terminal | Manual / exception / no-plate | Exit booth |
| Cloud seat | Remote talk / raise / exception | Central |
| Charger | Slow / fast / ultra-fast | By ratio |

#### 3.2.2 Lot Access Modes
| Mode | Description | For | Cost |
|----------|------|----------|:----:|
| Direct | Lot system directly to city platform (unified std) | Public new-build | Low |
| Gateway | Protocol-conversion gateway to platform | Existing / non-standard | Med |
| Data-report | Lot ops report space data periodically / real-time | Commercial / no retrofit | Low (data only) |
| Full managed | Lot fully operated by platform party | Owner lacks ops capability | High (full) |

### 3.3 Guidance System

#### 3.3.1 Three-Level Guidance
| Level | Location | Content | Count | Backhaul |
|:---:|------|----------|:-------:|----------|
| L1 sign | City entrance / arterial / ring | Zone: major areas + free spaces overview | __ | 4G / fiber |
| L2 sign | Collector / CBD / hospital | Road: lot name / distance / free / fee | __ | 4G |
| L3 sign | Lot entrance | Space: floors / zones free / fee | __ | 4G / wired |

#### 3.3.2 Mobile / In-Vehicle Guidance
| Channel | Function | Note |
|------|------|------|
| Google Maps / TomTom / HERE / Waze | Destination → nearby lots + free + fee + nav | Partner with major map apps |
| City parking app / mobile web | Search + book + nav + pay + invoice | City-built |
| In-vehicle nav | Head-unit search + nav + book | OEM partnership (factory / aftermarket) |

### 3.4 City Parking Platform

#### 3.4.1 Function Matrix
| Domain | Module | Description |
|--------|----------|----------|
| **Regulation** | City parking map | GIS of all resources (on/off-street / EV) + live occupancy + trend |
| | Ops monitor | Device online / orders / revenue / turnover / violation / complaint |
| | Enforcement linkage | Auto illegal-parking detect → municipal / police → closed loop |
| | Arrears recovery | Arrears mgmt / remind / recover / credit linkage |
| **Operations** | On-street ops | Space mgmt / orders / finance / patrol / recovery |
| | Off-street ops | Lot mgmt / gate / settle / monthly / reconcile / report |
| | Charging ops | Charger mgmt / charge orders / billing / split |
| | Monthly mgmt | Online monthly buy / renew / permit |
| **Guidance** | Sign mgmt | Sign status / publish / auto free-space update |
| | Nav linkage | Google / TomTom / in-vehicle data |
| **Data** | Analytics | Parking profile (tidal / daily / weekly / seasonal) / hotspot / forecast / pricing |
| | Sharing | Share parking data with TOCC / police / municipal / planning |
| | Open | Open masked parking-data API to public / firms / developers |
| **Public** | App / mobile web | Search / nav / book / pay / invoice / monthly / charge |
| | E-invoice | Auto / manual e-invoice |
| | Service center | Online + phone + FAQ |

#### 3.4.2 Unified Payment
| Method | On-street | Off-street | Charge | Note |
|----------|:---:|:---:|:---:|------|
| Wallet (Apple/Google Pay) | Y | Y | Y | Scan / frictionless |
| Bank card | Y | Y | Y | Scan / frictionless |
| ETC | — | Y | — | Lot ETC debits |
| CBDC | Y | Y | Y | Central-bank digital currency |
| City transit card | Y | Y | Y | Transit / citizen card |

### 3.5 Shared Parking (Off-Peak)

#### 3.5.1 Modes
| Mode | Description | Example |
|------|------|----------|
| Residential–office | Daytime home spaces → office users; night office spaces → residents | Building ↔ residential reciprocity |
| Commercial–residential | Night mall spaces → residents monthly | Mall night monthly |
| Hospital-near | Hospital shortage → nearby residential / mall spaces | Peripheral relief |
| Public-sector | Agency internal lots open off-peak | Agency yard off-peak |

#### 3.5.2 Platform Functions
| Function | Description |
|------|------|
| Space publish | Owner publishes shareable spaces (time / price / rule) |
| Book / rent | Search → book → nav → enter (plate / QR) → exit → settle |
| Credit mgmt | Overstay / breach → credit score → affects future use |
| Revenue split | Platform + owner auto split by ratio |
| Overstay alert | Remind before expiry + overstay surcharge |

### 3.6 Charger Integration

#### 3.6.1 Charge–Parking Fusion
| Scenario | Solution |
|------|------|
| On-street charge | Slow charger beside on-street space (lamp-post / standalone); charge + parking bundled |
| Off-street charge | Fast / ultra-fast zone + slow zone; charger linked to parking (free parking X h while charging) |
| Charger data | Location / power / status / price / queue → into city guidance |
| Smart charging | Coordinate with grid (off-peak first / power limit / demand mgmt) |
| PV-storage-charge-V2G | PV + storage + charge + discharge (V2G) showcase station |

---

## 4. Implementation Strategy

### 4.1 Phased Rollout
| Phase | Time | Scope | Content | Spaces connected | Investment |
|------|------|------|------|:---------:|:----:|
| 1 (pilot) | ____ | [core / 1–2 districts] | Core on-street + key lots + platform 1.0 + guidance 1.0 + app 1.0 | ____k | $___k |
| 2 (core) | ____ | [core urban] | All core on-street + off-street + sharing + analytics + guidance 2.0 | ____k | $___k |
| 3 (citywide) | ____ | [citywide] | All on/off-street + charge fusion + AI forecast + data assetization | ____k | $___k |

### 4.2 Priority Matrix
| Priority | Area type | On-street | Off-street | Signs | Reason |
|:------:|----------|:-------:|:------:|:-----:|------|
| P0 | Core CBD | High-mast | Full | L1+L2+L3 | Worst conflict / highest fee |
| P0 | Major hospital | High-mast / mag | Nearby | L2+L3 | Public pain / attention |
| P1 | Old town / dense residential | Mag + patrol | Sharing | L2+L3 | Big gap / tight supply |
| P1 | Transport hub (rail / airport) | Video | Full | L2+L3 | High flow / price lever |
| P2 | Collector / general | Mag + patrol | Data link | L2+L3 | General need |
| P3 | Suburb / low density | Defer | Data link | Defer | Low need |

---

## 5. Operating Plan

### 5.1 Operating Model
| Model | Description | Pros/Cons | For |
|------|------|--------|:---:|
| Public self-build | Public invest + municipal / transit-co op | Public revenue / less expertise | Small city |
| PPP | Private build-operate / regulated | Pro ops / complex split | Mid city |
| BOT / concession | 10–30 yr concession | Fast start / price oversight | Large city |
| Hybrid | On-street public + off-street market + unified platform | Flexible / harder mgmt | Mega city |

> **Recommended**: [per city size and capability]

### 5.2 Team
| Role | Headcount | Responsibility |
|------|:---:|------|
| Ops director | 1 | Overall |
| Platform ops | __ | Platform / data / service |
| On-street patrol | __ | Device patrol / recovery / order |
| Off-street O&M | __ | Lot device O&M / exception |
| Service | __ | 7×12 phone + online |
| Market / BD | __ | Lot access negotiation / partnership |
| Finance / legal | __ | Settle / reconcile / legal |

### 5.3 Pricing Strategy
| Principle | Description |
|----------|------|
| Zonal differentiation | Core > outer > suburb, price lever on supply-demand |
| Time differentiation | Day > night; weekday > weekend (reverse for malls) |
| Tiered | Free X min → 1st hr Y → then Z / 30 min, faster turnover |
| Night discount | Night (20:00–08:00) monthly discount for residents |
| EV incentive | EV free / half first X h (per guidance) |
| Shared pricing | Shared space priced by owner + platform fee |

---

## 6. Investment and Revenue

### 6.1 Investment Estimate
| # | Item | Estimate ($k) | Note |
|:---:|----------|:----------:|------|
| 1 | On-street front-end | $____ | High-mast / mag / patrol |
| 2 | Off-street retrofit | $____ | Plate / gate / ETC support |
| 3 | Guidance signs | $____ | L1 __ + L2 __ + L3 __ |
| 4 | Comms & power | $____ | 4G/5G module / leased line / power |
| 5 | Cloud platform | $____ | Server / cloud / platform sw |
| 6 | App / mobile web | $____ | iOS / Android / web |
| 7 | System integration | $____ | Data link / 3rd-party |
| 8 | Ops center | $____ | Call / monitor center |
| 9 | Contingency | $____ | |
| | **Total** | **$____** | |

### 6.2 Revenue Model
| Item | Basis | Annual ($k) |
|----------|----------|:----------------:|
| On-street fee | __k spaces × $__/day × 365 × __% collection | $____ |
| Off-street platform fee | __k spaces × $__/mo × 12 | $____ |
| Charge service fee | __ chargers × __ kWh/day × $__/kWh × 365 | $____ |
| Ad revenue | Signs + app / mobile web | $____ |
| Data service | Parking analytics / report | $____ |
| Sharing commission | __k shared × $__/mo × __% × 12 | $____ |
| **Total** | | **$____** |

---

## 7. Safeguards

### 7.1 Policy Safeguards
| Policy | Content |
|------|------|
| Parking mgmt ordinance | Revise city parking rules: on-street legality, arrears recovery, sharing rules |
| Pricing | Differentiated pricing standard + approval / filing |
| Data sharing | Drive agencies / lot operators to share data |
| EV incentive | Charger funding / EV parking discount |

### 7.2 Organization
Recommend a smart-parking steering group chaired by [city deputy leader], with members from [municipal / police-traffic / transport / investment / funding / data].

### 7.3 Public Communication
| Stage | Strategy |
|------|------|
| Pre-build | Promote public benefit, publish parking white paper, collect input |
| During | Regular progress, minimize disruption |
| Pre-launch | Multi-channel warm-up, coupons / trial, drive download / sign-up |
| Ops | Service / complaint handling, publish ops data, accept oversight |

---

> **Usage note**: This template fits a citywide smart-parking proposal. Core success factors: front-end selection (high-mast vs mag), lot-access negotiation, pricing design, and legal support for arrears recovery. Replace `[placeholder]` with project data.

> **Legal notice**: This template is protected by applicable copyright law and is provided for personal study and reference only; commercial use requires the author's written permission.

> **Disclaimer**: This template is for study and reference only and does not constitute professional advice of any kind. Parking fees involve public interest; implementation must pass price hearing, legality review, and public-sector approval. The author accepts no liability for any loss arising from use of or reliance on this template.

> **Author**: yinjianheng | yinjianheng@foxmail.com
