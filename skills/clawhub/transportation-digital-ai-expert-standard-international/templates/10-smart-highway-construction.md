# Smart Highway Construction Proposal

> **Project Name:** [XX Motorway] Smart Highway Program
> **Scope:** [XX Motorway, Section XX–XX], total length [XX] km
> **Authoring Team:** [Team Name]
> **Date Prepared:** [YYYY-MM-DD]
> **Version:** V[X.X]

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Corridor Status Analysis](#2-corridor-status-analysis)
3. [Overall Architecture Design](#3-overall-architecture-design)
4. [Subsystem 1: Smart Monitoring & Sensing](#4-subsystem-1-smart-monitoring--sensing)
5. [Subsystem 2: Smart Tolling](#5-subsystem-2-smart-tolling)
6. [Subsystem 3: Active Traffic Management](#6-subsystem-3-active-traffic-management)
7. [Subsystem 4: Smart Service Area](#7-subsystem-4-smart-service-area)
8. [Subsystem 5: Smart Tunnel](#8-subsystem-5-smart-tunnel)
9. [Subsystem 6: Bridge Health Monitoring](#9-subsystem-6-bridge-health-monitoring)
10. [Subsystem 7: Slope Monitoring](#10-subsystem-7-slope-monitoring)
11. [Subsystem 8: Weather Monitoring & Warning](#11-subsystem-8-weather-monitoring--warning)
12. [Subsystem 9: Emergency Command & Dispatch](#12-subsystem-9-emergency-command--dispatch)
13. [Subsystem 10: Digital Twin Platform](#13-subsystem-10-digital-twin-platform)
14. [Subsystem 11: V2X & Automated-Driving Support](#14-subsystem-11-v2x--automated-driving-support)
15. [System Integration & Data Sharing](#15-system-integration--data-sharing)
16. [Implementation Plan](#16-implementation-plan)
17. [Operations & Maintenance Plan](#17-operations--maintenance-plan)
18. [Investment Estimate](#18-investment-estimate)
19. [Appendix](#19-appendix)

---

## 1. Project Overview

### 1.1 Background

[Briefly describe the policy context, industry trends, and the necessity of smartening this corridor. 2–3 paragraphs.]

> **Example:** "National transport strategies call for 'vigorously developing smart mobility'. Programs for 'new infrastructure' in transport emphasize raising the intelligence level of highways. Leading jurisdictions have accelerated smart-motorway programs — e.g., Germany's Autobahn digital test fields (A9/A95), the EU ITS Corridors (Rotterdam–Frankfurt–Vienna), and the Colorado/E-470 smart-corridor pilots — with proven safety and efficiency gains. [XX Motorway], the artery connecting [XX] and [XX], already carries [XX]k vehicles/day; its current IT level cannot meet safe, efficient, and green operations, so intelligent upgrade is urgent."

### 1.2 Objectives

| Category | Description | Metric |
|----------|-------------|--------|
| **Safety** | Lower crash rate, shorten rescue time | Crashes per 10k veh ↓ [≥XX%]; incident detection ≤ [XX] s |
| **Efficiency** | Raise throughput, cut congestion | Peak avg. speed ↑ [≥XX%] |
| **Service** | Improve public travel experience | Satisfaction ≥ [XX] |
| **Cost** | Lower O&M cost | Maintenance cost ↓ [≥XX%]; toll staffing cost ↓ [≥XX%] |
| **Green** | Cut emissions | Annual CO₂ ↓ [≥XX] tonnes |

### 1.3 Scope

| Dimension | Content |
|-----------|---------|
| Corridor | [XX Motorway, XX–XX], chainage [KXX+XXX — KXX+XXX], length [XX] km |
| Lanes | [X lanes per direction] (incl. [X] hard shoulder) |
| Interchanges | [XX] |
| Toll plazas | [XX] (incl. [XX] mainline, [XX] ramp) |
| Service areas | [XX] pairs |
| Tunnels | [XX] (longest [XX] m, total [XX] m) |
| Bridges | [XX] (incl. [XX] special-structure) |
| Slopes | [XX] (incl. [XX] high slopes) |

---

## 2. Corridor Status Analysis

### 2.1 Traffic Status

| Metric | Value | Note |
|--------|-------|------|
| AADT | [XX,XXX] veh/day | [202X] |
| Avg. standard daily flow | [XX,XXX] pcu/day | |
| Peak-hour volume | [X,XXX] pcu/h | [Direction / time] |
| Truck share | [XX%] | |
| AADT growth (3-yr) | [XX%] | |
| Avg. travel speed | [XX] km/h | Peak |
| Congestion frequency | [X]/month | [Jam ≥1 km, ≥30 min] |

### 2.2 Safety Status

| Metric | Value | Industry Avg | Note |
|--------|-------|--------------|------|
| Crashes per 10k veh | [X.X] | [X.X] | |
| Annual crashes | [XX] | — | |
| Blackspots | [XX] | — | [≥X crashes in 3 yr] |
| Fog / adverse-weather segments | [XX] | — | |
| Avg. incident detection time | [XX] min | — | [Manual patrol + calls] |
| Avg. emergency arrival | [XX] min | — | |

### 2.3 Existing IT Systems

| System | Status | Problem |
|--------|--------|---------|
| Video surveillance | [XX] cams, coverage [XX%] | [Most SD, poor night, no AI] |
| Microwave detectors | [XX] | [Aged >8 yr, hard to maintain] |
| Tolling | [Networked toll system VX.X] | [No free-flow] |
| CMS (variable signs) | [XX] | [Insufficient, untimely updates] |
| Comms | [OTN/SDH] | [Bandwidth insufficient for HD video] |
| Power | [XX roadside cabinets] | [Unstable in parts] |

### 2.4 Pain-Point Summary

1. **Weak sensing:** low cam coverage, single detection, no AI analytics
2. **Passive control:** reactive only, no active / predictive control
3. **Toll efficiency:** ramp-plaza queues at peak, no free-flow
4. **Poor service area:** weak parking guidance, charging, retail intelligence
5. **Tunnel risk:** monitoring blind spots, weak emergency response
6. **Crude structure monitoring:** manual inspection, no real-time online monitoring
7. **Severe silos:** independent systems, no data interchange, no coordination

---

## 3. Overall Architecture Design

### 3.1 "1+1+4+11" Overall Architecture

```
                       Smart Highway Overall Architecture

┌──────────────────────────────────────────────────────────────┐
│               App Layer — 11 Subsystems                        │
│  ┌────┐┌────┐┌────┐┌────┐┌────┐┌────┐┌────┐                 │
│  │Mon ││Toll││Ctrl││Svc ││Tun ││Brg ││Slop│ ...               │
│  │    ││    ││    ││Area││    ││Hlth││Mon │                     │
│  └────┘└────┘└────┘└────┘└────┘└────┘└────┘                 │
├──────────────────────────────────────────────────────────────┤
│          Platform — 1 Data Hub + 1 Digital-Twin Platform       │
│  ┌──────────────────────┐  ┌──────────────────────┐         │
│  │   Highway Data Hub     │  │   Digital Twin        │         │
│  │ (aggregate, govern,    │  │ (3D viz / simulation) │         │
│  │  serve all data)       │  │                       │         │
│  └──────────────────────┘  └──────────────────────┘         │
├──────────────────────────────────────────────────────────────┤
│        Transport — 4 Networks (comms / power / positioning /   │
│                          security)                             │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────────┐            │
│  │Fiber    │ │5G/WiFi6│ │GNSS hi-│ │Cyber-security│           │
│  │backbone │ │wireless│ │precision│ │ (ISO 27001  │           │
│  │        │ │        │ │        │ │  / IEC 62443)│           │
│  └────────┘ └────────┘ └────────┘ └────────────┘            │
├──────────────────────────────────────────────────────────────┤
│   Sensing — full awareness (vision + radar + lidar-radar +     │
│                         ultrasonic + fiber + weather)          │
│  ┌────┐┌────┐┌────┐┌────┐┌────┐┌────┐┌────┐┌────┐          │
│  │Video││mmW ││LiDAR││Ultra││Fiber││Temp││Strain││Tilt│ ...   │
│  │     ││Rad ││     ││Sonic││Vib ││    ││     ││    │        │
│  └────┘└────┘└────┘└────┘└────┘└────┘└────┘└────┘          │
└──────────────────────────────────────────────────────────────┘
```

### 3.2 Key Design Concepts

| Concept | Description |
|---------|-------------|
| **Full awareness** | Fuse video, radar, lidar-radar, fiber vibration, weather — "all-weather, full-coverage, all-element" sensing |
| **Cloud-edge synergy** | Roadside edge for real-time decision (<100 ms); corridor center / cloud for global analysis & AI training |
| **Data-driven** | Data hub as core; aggregate all sensing & business data; "data → insight → decision → action" loop |
| **Digital base** | HD map-based corridor digital twin — "visible, measurable, controllable, serviceable" |
| **Active control** | From reactive to proactive warning, dynamic control, diversion |
| **Green / low-carbon** | Smart lighting, energy mgmt, PV — lower O&M energy |

---

## 4. Subsystem 1: Smart Monitoring & Sensing

### 4.1 Overview

Build a multi-dimensional sensing system covering the whole corridor — real-time, precise awareness of traffic state, incidents, and road environment.

### 4.2 Device Deployment

| Device | Density | Location | Qty | Senses |
|--------|---------|----------|-----|--------|
| **HD AI camera** | 1 pair per [1–2] km | Roadside post / gantry | [XX] | Vehicle, params, events, ANPR |
| **mmWave radar** | per [500 m–1 km] | Roadside post, shared pole | [XX] | Position, speed, trajectory (all-weather) |
| **Lidar-radar all-in-one** | per [200–500 m] key | Roadside / gantry | [XX] | Fused, high-precision trajectory |
| **LiDAR** | [Interchange / service-area entry] | High-point / gantry | [XX] | High-precision detection & classification |
| **Fiber vibration** | [Slope / barrier] | Shared / dedicated fiber | [XX] km | Barrier hit, intrusion, slope vibration |
| **Drone (optional)** | [X] + [X] hangars | Center / service area | [X] | Remote patrol, crash recon, emergency |

### 4.3 AI Analytics

| Capability | Approach | Detects | Target |
|-----------|----------|---------|--------|
| Traffic params | CV detection + tracking | Flow, speed, class, occupancy, queue | ≥ [95%] |
| Incident | CV + time-series | Stop, wrong-way, pedestrian, debris, jam, smoke/fire | Acc ≥[95%], recall ≥[90%] |
| Vehicle ID | CV + deep metric | Plate, class, color, make | Plate ≥[98%], class ≥[95%] |
| Anomaly driving | CV + trajectory | Speeding, slow, frequent lane change, shoulder use | ≥ [90%] |

### 4.4 Key Metrics

| Metric | Target |
|--------|--------|
| Sensing coverage | Mainline [99%], ramp/service [95%] |
| Incident detection latency | ≤ [10] s |
| Param refresh | ≤ [1] min (key ≤[5] s) |
| Night / adverse-weather availability | All-weather ≥ [95%] |

---

## 5. Subsystem 2: Smart Tolling

### 5.1 Overview

On the existing networked toll system, build free-flow tolling (ETC gantry + AI audit) and smart toll plazas.

### 5.2 Free-Flow Tolling (ETC Gantry + AI Audit)

| Item | Description |
|------|-------------|
| **ETC gantry** | [Per international EFC standard (ISO 14906 / EN 15509); existing [XX], add [XX]] |
| **ANPR** | Gantry HD plate recognition, rate ≥ [99%] |
| **AI audit** | AI-based path reconstruction & evasion analysis — abnormal path (short path / long time), class mismatch, tag/licence mismatch |
| **Online charging** | Multi-path online precise charging |
| **Exceptions** | Fast handling of ETC exceptions (insufficient balance, failed tag) |

### 5.3 Smart Toll Plaza

| Item | Description |
|------|-------------|
| **Ramp pre-transaction + quick verify** | ETC pre-tx at ramp; plaza only quick verify & release, fewer stops |
| **Narrow / island-free** | Reduce or remove physical islands → more lanes, higher throughput |
| **Self-service pay / card** | Replace manual MTC lanes; ETC + mobile + cash |
| **Plaza digital twin** | Real-time lane status, queue, exceptions |
| **Lane-level guidance** | Dynamic LED guide to optimal lane |
| **Lane robot** | Remote video / voice assist for exceptions |

### 5.4 Key Metrics

| Metric | Target |
|--------|--------|
| ETC pass rate | ≥ [99.9%] |
| MTC avg. time | ≤ [8] s/veh (incl. pay) |
| Plaza peak queue | ≤ [X] veh/lane |
| Evasion detection | ↑ [≥XX%] |
| ANPR accuracy | ≥ [99%] (all-weather) |

---

## 6. Subsystem 3: Active Traffic Management

### 6.1 Overview

Shift from "passive response" to "active control" — real-time monitoring, predictive warning, automated strategy, precise guidance for fine-grained management.

### 6.2 Control Strategy Set

| Strategy | Trigger | Action | Priority |
|----------|---------|--------|----------|
| **Lane control** | Crash occupies lane | Close lane upstream, CMS lane-closed | P0 |
| **Dynamic hard-shoulder** | Peak congestion | Open shoulder (only if video+radar confirm safe) | P1 |
| **Variable speed limit** | Congestion / weather / work | Step down (e.g., 120→80→60 km/h) | P0 |
| **Ramp control** | Mainline jam + ramp queue | Ramp signal metering (ALINEA / fuzzy) | P1 |
| **Diversion** | Severe mainline jam | CMS + nav app alternate route | P1 |
| **Work-zone control** | Maintenance | Step-down + lane-close upstream | P0 |

### 6.3 Control Platform Functions

| Module | Description |
|--------|-------------|
| **Situation assessment** | Real-time LOS (A–F) per segment |
| **Congestion forecast** | Short-term (15/30/60 min) forecast from history + real-time |
| **Strategy generation** | Rule-based auto-match & recommend (+ human confirm) |
| **Strategy simulation** | Simulate effect in digital twin before execution |
| **Strategy execution** | One-click push to CMS / signal / LCS / nav app |
| **Effect evaluation** | Before/after comparison |

### 6.4 Publishing Terminals

| Terminal | Location / Qty | Function |
|----------|----------------|----------|
| Mainline CMS (large) | [1 per 3–5 km, XX] | Conditions, control, guidance |
| Ramp CMS | [1 per ramp, XX] | Ramp control |
| Lane Control Signal (LCS) | [1 group per 500 m key] | Lane open/closed/limit |
| Smart fog lights | [1 pair per 25 m fog-prone, XX] | Fog guidance + anti-collision |
| Broadcast / directional speaker | [Interchange / service area, XX] | Voice safety alert |
| Nav-app partnership | [TomTom / HERE / regional] | Conditions + control + incident push |

---

## 7. Subsystem 4: Smart Service Area

### 7.1 Overview

Build a "smart, green, welcoming" service area — better public experience and O&M efficiency.

### 7.2 Build Content

| Module | Content | Description |
|--------|---------|-------------|
| **Smart parking** | Space detect (mag/video), guidance, find-my-car | Entry screen shows free spaces, bay lights guide |
| **Smart charging** | Charger mgmt, booking, smart charging | [XX] kW fast, [XX] bays |
| **Smart lighting** | Auto-dim by people/cars/time | Save ≥ [XX%] |
| **Smart restroom** | Stall occupancy, env (odor/temp/humid), smart cleaning | Entry screen shows stall status |
| **Smart retail** | Unmanned store, self-checkout, membership, targeted promo | Raise revenue |
| **Hazmat mgmt** | Dedicated hazmat zone: video + thermal imaging | Compliance + safety |
| **Info publishing** | Area screens: weather, road, retail, events | Omni-channel |
| **Energy mgmt** | Water/elec/gas monitor, PV (roof + canopy) | Green-area certification |

---

## 8. Subsystem 5: Smart Tunnel

### 8.1 Overview

Tunnel safety is paramount. Build a 3-tier "front sensing + edge decision + center control" smart tunnel safety system.

### 8.2 Build Content

| Module | Content |
|--------|---------|
| **Full tunnel sensing** | HD cam + mmWave radar every [100–200] m; lidar-radar at portal |
| **AI event detection** | Stop, wrong-way, pedestrian, debris, smoke, fire, crash auto-detect |
| **Portal safety control** | Portal sign, LCS, signal linkage |
| **Smart lighting** | Auto by outside luminance + flow (portal/transition/mid/exit) — save + safe |
| **Ventilation linkage** | CO/VI/wind → fan strategy linkage |
| **Fire linkage** | Fire auto-detect → video confirm → plan (broadcast / smoke / egress / suppression) |
| **Broadcast / comms** | Full FM coverage (auto emergency insert on FM break) + emergency phone |
| **Egress guidance** | Smart egress lights (dynamic escape direction by fire location) |
| **Digital-twin tunnel** | 3D model + real-time data mapping |

---

## 9. Subsystem 6: Bridge Health Monitoring

### 9.1 Overview

Online structural-health monitoring for special bridges (cable-stayed / suspension / continuous rigid / long-span).

### 9.2 Monitoring Content

| Item | Sensor | Description |
|------|--------|-------------|
| **Displacement / deformation** | GNSS, displacement gauge, tiltmeter | Girder deflection, tower top, bearing |
| **Stress / strain** | Strain gauge, FBG | Key-section stress |
| **Cable / hanger force** | Accelerometer + spectrum | Stay / hanger force |
| **Vibration** | Accelerometer | Natural frequency, damping, mode |
| **Temperature** | Temp sensor | Structural temp field |
| **Wind load** | Anemometer, wind-pressure | Site wind speed/dir |
| **WIM** | Bending-plate / piezoelectric | Heavy-vehicle load ID |

### 9.3 Warning & Assessment

| Function | Description |
|----------|-------------|
| **Tiered warning** | Yellow (watch) → Orange (inspect) → Red (limit/load) |
| **Safety assessment** | Online safety state per design-code requirements |
| **Life prediction** | Degradation trend from long-term monitoring |

---

## 10. Subsystem 7: Slope Monitoring

### 10.1 Overview

Real-time online monitoring of high / unstable slopes to prevent landslides.

### 10.2 Monitoring Content

| Item | Sensor | Accuracy |
|------|--------|---------|
| **Surface displacement** | GNSS (multi-constellation) | [±2 mm + 1 ppm] |
| **Deep displacement** | Inclinometer (fixed) | [±0.01°] |
| **Groundwater** | Piezometer | [±0.1% FS] |
| **Rainfall** | Tipping-bucket gauge | [0.5 mm] |
| **Crack** | Crack meter | [±0.1 mm] |
| **Anchor force** | Anchor load cell | [±0.5% FS] |
| **Video** | HD PTZ | Remote patrol |

### 10.3 Warning Model

- Multi-parameter (displacement rate + rainfall + groundwater) composite algorithm
- Three tiers: Blue (notice) → Yellow (alert) → Red (alarm)
- Auto-push to maintenance, safety, emergency managers

---

## 11. Subsystem 8: Weather Monitoring & Warning

### 11.1 Overview

Build a highway weather-station network for precise adverse-weather monitoring & warning.

### 11.2 Station Network

| Device | Elements | Principle | Qty |
|--------|----------|----------|-----|
| **Full met station** | Temp, humidity, pressure, wind, rain | 1 per [20–30] km | [XX] |
| **Visibility sensor** | Visibility | 1 per [5–10] km fog-prone | [XX] |
| **Road-surface sensor** | Pavement temp, wetness, water/ice/snow | Bridge / tunnel mouth / long downgrade / icing-prone | [XX] |
| **Weather-phenomenon sensor** | Rain/snow/fog/haze ID | Key segments | [XX] |

### 11.3 Warning & Application

| Warning | Publish / linkage |
|---------|-------------------|
| Fog | CMS + auto fog lights + variable speed linkage |
| Ice | CMS + variable speed + de-icing linkage |
| Heavy rain / snow | CMS + variable speed + possible closure |
| High wind | CMS + variable speed + (extreme) closure / restriction |

---

## 12. Subsystem 9: Emergency Command & Dispatch

### 12.1 Overview

"Peacetime + wartime" emergency command — full digital chain: detect → assess → dispatch → handle → evaluate.

### 12.2 Modules

| Module | Function |
|--------|----------|
| **Smart intake** | AI auto-detect + public call (phone / app / SOS pillar) + patrol + 3rd-party |
| **Event assessment** | GIS locate + video confirm + impact estimate |
| **Plan match** | Auto-recommend digital plan by type/level/location |
| **Resource dispatch** | Rescue resources (road authority / police / ambulance / fire / tow / maintenance) one-map, optimized dispatch |
| **Joint command** | AV fusion (center ↔ field), order issue, track |
| **Info linkage** | One-click to CMS / LCS / app / radio / nav app |
| **E-sandbox** | Digital-twin scenario replay & drill |
| **Post-analysis** | Full response replay, timeliness analysis, improvement |

---

## 13. Subsystem 10: Digital Twin Platform

### 13.1 Overview

HD map + BIM + GIS + IoT — a digital mirror of the motorway.

### 13.2 Data Base

| Layer | Content |
|-------|---------|
| **HD map** | Lane-level (abs ≤20 cm, rel ≤10 cm): lane lines, signs/markings, barriers |
| **BIM** | Plaza / service area / tunnel / bridge 3D BIM (LOD 300–400) |
| **Oblique photo** | Drone oblique photogrammetry 3D reality model |
| **IoT data** | All sensing / monitoring device real-time data |

### 13.3 Twin Applications

| Application | Description |
|-------------|-------------|
| **Traffic twin** | Real-time vehicle position / speed / trajectory across corridor |
| **Device O&M twin** | Device status, fault locate, repair trace |
| **Structure twin** | Bridge / slope / tunnel 3D + live monitoring overlay |
| **Simulation** | "What-if": closure / speed / diversion impact |
| **Emergency drill** | Drill in twin without disturbing real traffic |
| **Show & report** | Immersive wall for visits / reports / decisions |

---

## 14. Subsystem 11: V2X & Automated-Driving Support

### 14.1 Overview

Deploy C-V2X roadside to support connected vehicles (V2I), and underpin L3/L4 automated driving.

### 14.2 Build Content

| Item | Description |
|------|-------------|
| **RSU deployment** | RSU (C-V2X PC5) at interchanges, service-area entries, tunnel mouths, blackspots |
| **Sensing share** | Roadside perception → vehicle via V2X (RSM/RSI) |
| **Event publish** | Roadside events (crash / work / jam / weather) via V2X real-time |
| **Speed guidance** | Upstream speed/lane advice at work/crash zones |
| **In-vehicle signing** | Speed / lane / exit info pushed to cabin |
| **AD support** | Beyond-line-of-sight perception (roadside → vehicle) to cover single-vehicle blind spots |

---

## 15. System Integration & Data Sharing

### 15.1 Integration Architecture

```
                        ┌──────────────────┐
                        │  Corridor Mgmt    │
                        │  Center (Smart    │
                        │   Highway Platform)│
                        └────────┬─────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              ▼                  ▼                  ▼
    ┌─────────────┐    ┌─────────────┐    ┌─────────────────┐
    │ Sensing/      │    │  Tolling      │    │ Structure Monitor │
    │ Control devices│    │ (ETC gantry / │    │ (bridge/slope/    │
    │ (cam/radar/   │    │  plaza)       │    │  tunnel)          │
    │  CMS/signal)  │    │              │    │                   │
    └─────────────┘    └─────────────┘    └─────────────────┘
```

### 15.2 External Data Sharing

| Recipient | Content | Method |
|-----------|---------|--------|
| [Regional toll authority] | Toll, flow, incident | [API / message queue] |
| [National / regional transport operations center] | Operations monitoring, incident | [API / message queue] |
| [Highway police] | Violation, crash | [Dedicated / API] |
| [National met service] | Weather (receive + share) | [API] |
| [Map / nav provider] | Conditions, control, incident | [API] |

---

## 16. Implementation Plan

### 16.1 Phasing

| Phase | Time | Key Content |
|-------|------|-------------|
| **Phase 1: Base sensing + core control** | [X] mo | ① Full video+radar coverage; ② Data Hub V1.0; ③ Active-control base + core CMS/LCS; ④ Corridor-level digital-twin base map |
| **Phase 2: Smart toll + tunnel + bridge** | [X] mo | ① Smart plaza retrofit; ② Smart tunnel (sense+AI+linkage); ③ Bridge health; ④ Slope monitoring |
| **Phase 3: Smart service area + V2X + deepen** | [X] mo | ① Smart service area; ② C-V2X RSU; ③ Digital-twin deepen; ④ AI scenario expand |

---

## 17. Operations & Maintenance Plan

### 17.1 O&M Organization

| Team | Headcount | Duty |
|------|-----------|------|
| Field maintenance | [X] | Cam/radar/RSU/CMS/sensor inspection & repair |
| System O&M | [X] | Platform, server, network, DB |
| Electro-mechanical O&M | [X] | Power, ventilation, lighting |

### 17.2 O&M SLA

| Metric | Target |
|--------|--------|
| Field device online rate | ≥ [98%] |
| Platform availability | ≥ [99.9%] |
| Fault response | ≤ [30] min |
| Fault repair | ≤ [4] h (general), ≤ [24] h (major) |
| Inspection cycle | Field monthly, tunnel/bridge quarterly |

---

## 18. Investment Estimate

### 18.1 Investment Summary

| Subsystem | Phase 1 | Phase 2 | Phase 3 | Total |
|----------|---------|---------|---------|-------|
| 1. Smart monitoring & sensing | [€XXX k] | [€XX k] | — | [€XXX k] |
| 2. Smart tolling | — | [€XXX k] | — | [€XXX k] |
| 3. Active traffic mgmt | [€XXX k] | [€XX k] | [€X k] | [€XXX k] |
| 4. Smart service area | — | — | [€XX k] | [€XX k] |
| 5. Smart tunnel | — | [€XXX k] | — | [€XXX k] |
| 6. Bridge health | — | [€XX k] | — | [€XX k] |
| 7. Slope monitoring | — | [€XX k] | — | [€XX k] |
| 8. Weather | [€XX k] | [€X k] | — | [€XX k] |
| 9. Emergency command | [€XX k] | [€X k] | [€X k] | [€XX k] |
| 10. Digital twin | [€XX k] | [€X k] | [€X k] | [€XX k] |
| 11. V2X | — | — | [€XX k] | [€XX k] |
| System integration | [€X k] | [€X k] | [€X k] | [€X k] |
| Contingency | [€X k] | [€X k] | [€X k] | [€X k] |
| **Total** | **[€XXXX k]** | **[€XXXX k]** | **[€XXX k]** | **[€XXXX k]** |

### 18.2 Annual O&M Estimate

| Item | Annual (€k) |
|------|-------------|
| Field device maintenance | [€XX k] |
| Platform O&M | [€XX k] |
| Electro-mechanical O&M | [€XX k] |
| Comms fee | [€XX k] |
| Power | [€XX k] |
| **Annual total** | **[€XXX k]** |

---

## 19. Appendix

### Appendix A: Design Standards

| Standard | Title |
|----------|-------|
| EU Directive 2004/54/EC | Min. safety requirements for tunnels in the trans-European road network |
| IEC 62305 | Protection against lightning |
| ISO/IEC 27001 + IEC 62443 | Information & OT security |
| ISO 14906 / EN 15509 | Electronic fee collection — application interface |
| ASTM E1318 | Weigh-in-motion (WIM) |
| AASHTO / EN 13036 / PIARC | Highway / pavement / tunnel & bridge guidance (regional equivalents) |
| ISO 18649 / fib Model Code | Structural-health-monitoring guidance |
| ETSI C-ITS / SAE J2735 | V2X message & security (Subsystem 11) |

### Appendix B: Acronyms

| Acronym | Full Name |
|---------|-----------|
| CMS | Changeable Message Sign |
| LCS | Lane Control Signal |
| WIM | Weigh-In-Motion |
| BIM | Building Information Modeling |
| GIS | Geographic Information System |
| C-V2X | Cellular Vehicle-to-Everything |
| RSU | Road Side Unit |
| HD Map | High-Definition Map |
| LOS | Level of Service |

### Appendix C: Reference Cases

| Project | Scale | Highlight |
|---------|-------|-----------|
| [German Autobahn digital test field (A9/A95)] | [XX km] | [Active control + V2X + free-flow] |
| [EU ITS Corridor (Rotterdam–Vienna)] | [XX km] | [Cross-border C-ITS] |
| [Regional smart-motorway pilot] | [XX km] | [Full awareness + digital twin] |
| ... | ... | ... |

---

> **Prepared by:** [Authoring Team]
> **Reviewed by:** [Reviewer]
> **Approved by:** [Approver]
> **Date:** [YYYY-MM-DD]
