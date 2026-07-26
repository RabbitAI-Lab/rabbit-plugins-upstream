# Vehicle-to-Everything (V2X) Technical Solution

> **Project Name:** [XX Corridor / Zone] Connected & Cooperative ITS (C-ITS) / V2X Deployment
> **Authoring Team:** [Team Name]
> **Date Prepared:** [YYYY-MM-DD]
> **Version:** V[X.X]

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Current Road & Traffic Analysis](#2-current-road--traffic-analysis)
3. [Design Principles & Standards Compliance](#3-design-principles--standards-compliance)
4. [System Overall Architecture](#4-system-overall-architecture)
5. [Roadside Infrastructure Design](#5-roadside-infrastructure-design)
6. [On-Board Unit Specifications](#6-on-board-unit-specifications)
7. [Cloud-Control Platform Design](#7-cloud-control-platform-design)
8. [Use-Case Design](#8-use-case-design)
9. [Data Flow & Interface Design](#9-data-flow--interface-design)
10. [Security Framework (PKI / SCMS)](#10-security-framework-pki--scms)
11. [Deployment Plan](#11-deployment-plan)
12. [Testing & Validation Plan](#12-testing--validation-plan)
13. [Operations & Maintenance Plan](#13-operations--maintenance-plan)
14. [Investment Estimate](#14-investment-estimate)
15. [Appendix](#15-appendix)

---

## 1. Project Overview

### 1.1 Background

[Briefly describe the V2X technology backdrop, policy drivers, and industry trends.]

> **Example:** "V2X is core infrastructure for automated driving and smart mobility. National transport strategies call for advancing 'connected and intelligent vehicles (smart vehicles, autonomous driving, V2X)'. The Intelligent Vehicle Innovation Strategy targets meaningful progress in smart transport and city-infrastructure by 2025, with next-generation vehicular wireless networks (C-V2X) progressively deployed on selected urban corridors and highways."

### 1.2 Objectives

| Type | Description | Metric |
|------|-------------|--------|
| Safety | Reduce crashes through V2X warnings | Crash rate at relevant junctions/corridors down [≥XX%] |
| Efficiency | Optimize timing & speed guidance, cut stops | Arterial throughput up [≥XX%] |
| Service | Provide real-time road info to vehicles | Info coverage [≥XX%] |
| Validation | Validate V2X in real road conditions | [XX] use cases tested & validated |
| Industry | Stimulate local connected-vehicle ecosystem | [XX] |

### 1.3 Scope

| Dimension | Scope |
|-----------|-------|
| **Corridor / zone** | [XX Road / XX junction / XX zone], total ~[XX] km |
| **Junctions** | [XX] signalized junctions |
| **RSU deployment** | [XX] Road-Side Units (RSU) |
| **Sensing devices** | [XX] cameras, [XX] mmWave radars, [XX] LiDARs |
| **MEC deployment** | [XX] roadside edge-compute nodes |
| **On-board units** | [XX] OBUs (bus / taxi / fleet / test vehicles) |
| **Road class** | [Urban arterial / expressway / highway / campus road] |

---

## 2. Current Road & Traffic Analysis

### 2.1 Road Infrastructure Status

| Road | Class | Lanes | Length (km) | Design Speed | Current Control | AADT |
|------|-------|-------|-------------|--------------|-----------------|------|
| [XX Rd] | [Arterial] | [6 lanes] | [X.X] | [60 km/h] | [Fixed / adaptive] | [XX,XXX] |
| [XX Rd] | [Expressway] | [8 lanes] | [X.X] | [80 km/h] | [No signal] | [XX,XXX] |
| ... | ... | ... | ... | ... | ... | ... |

### 2.2 Traffic Characteristics

| Metric | Data | Note |
|--------|------|------|
| Peak-hour volume | [XXXX] pcu/h | [AM / PM peak] |
| Avg. travel speed | [XX] km/h | Peak |
| Crash blackspots | [XX] | [Junctions/segments with ≥X crashes in past year] |
| Conflict hot-zones | [XX] | [Frequent conflict areas] |
| Bus routes | [XX] | [Routes in project scope] |

### 2.3 Communications & Duct Status

| Infrastructure | Status | Meets V2X need? | Note |
|---------------|--------|-----------------|------|
| Fiber duct | [Yes / No / Partial] | [Yes / No / Expand] | [Note] |
| 5G coverage | [Covered / Partial / None] | [Yes / No] | [Operator / signal] |
| C-V2X coverage | [Covered / None] | [Yes / No] | [Band / range] |
| Power | [Existing / new] | [Yes / Retrofit] | [Note] |
| Poles / gantries | [Reusable / new] | — | [Note] |

---

## 3. Design Principles & Standards Compliance

### 3.1 Design Principles

| Principle | Description |
|-----------|-------------|
| **Safety first** | V2X exists primarily to improve safety; must not introduce new risks |
| **Standards first** | Strictly follow int'l & regional V2X standards for interoperability across brands |
| **Smooth evolution** | Support evolution from LTE-V2X to 5G NR-V2X, from warning to cooperative control |
| **Cloud-edge synergy** | Roadside edge + central cloud-control for low latency & global optimization |
| **Secure & trustworthy** | PKI / SCMS for auth, encryption, integrity of vehicle-road-cloud comms |
| **Open & compatible** | Interoperate across vehicle brands, terminal & roadside vendors |
| **Cost-effective** | Reuse existing poles / networks / controllers; avoid rip-and-replace |

### 3.2 Standards Complied With

| Category | Standard | Title | Applies To |
|----------|----------|-------|------------|
| **Comm protocol** | ETSI EN 302 637 / 3GPP R14–R16 | C-ITS CAM/DENM; LTE-V2X / NR-V2X | 4, 9 |
| | IEEE 802.11p / ETSI ITS-G5 | DSRC / ITS-G5 direct comm (alt. to C-V2X) | 4 |
| **Message set** | SAE J2735 | DSRC / C-V2X Message Set Dictionary (BSM, MAP, SPAT, TIM) | 8, 9 |
| | ETSI EN 302 637-2/3 | CAM (Cooperative Awareness) / DENM (Decentralized Env. Notification) | 8, 9 |
| **Security** | IEEE 1609.2 | WAVE / C-ITS security services | 10 |
| | IEEE 1609.2a | Additional crypto suites for V2X | 10 |
| **Device** | ETSI EN 302 858 / C-V2X RSU spec | RSU device technical requirements | 5 |
| **Testing** | C-ITS test specs / SAE J2945/1 | V2X communications performance test methods | 12 |
| **Data** | ISO 17419 / ISO 14825 | C-ITS interface mgmt / geographic data files | 9 |
| **Cooperative** | ISO 20900 / SAE J3216 | V2X; cooperative driving automation (DDDAS) | 8 |

---

## 4. System Overall Architecture

### 4.1 "Endpoint–Edge–Cloud" Three-Layer Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Cloud-Control Platform (Cloud)           │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌───────────────┐  │
│  │ Data       │ │ Global    │ │ Use-case  │ │ Security Cert    │  │
│  │ Aggregation│ │ Scheduling│ │ Service   │ │ Mgmt (SCMS/CA)  │  │
│  └──────────┘ └──────────┘ └──────────┘ └───────────────┘  │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌───────────────┐  │
│  │ Device     │ │ O&M      │ │ Open API  │ │ Digital Twin /   │  │
│  │ Mgmt       │ │ Monitor   │ │          │ │ Visualization    │  │
│  └──────────┘ └──────────┘ └──────────┘ └───────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                  Roadside Edge Layer (Edge / MEC)             │
│  ┌──────────────────────────────────────────────────┐       │
│  │              Edge Compute Node (MEC)                │       │
│  │  ┌────────┐ ┌────────┐ ┌────────┐ ┌──────────┐  │       │
│  │  │Multi-src│ │Local    │ │V2X msg │ │Signal      │  │       │
│  │  │Fusion  │ │Decision │ │Process │ │controller   │  │       │
│  │  └────────┘ └────────┘ └────────┘ └──────────┘  │       │
│  └──────────────────────────────────────────────────┘       │
│           │              │              │                    │
│  ┌────────▼──┐  ┌────────▼──┐  ┌────────▼──┐               │
│  │   RSU     │  │ Cam/Radar │  │  Signal    │               │
│  │ (PC5/Uu)  │  │ (sensing) │  │  Controller│               │
│  └───────────┘  └───────────┘  └───────────┘               │
├─────────────────────────────────────────────────────────────┤
│                    Vehicle Terminal Layer (Vehicle)           │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐          │
│  │ Bus OBU │ │ Taxi OBU│ │ Fleet OBU│ │ Test OBU │  ...     │
│  │(factory/│ │(after-  │ │(after-  │ │(after-  │          │
│  │ retrofit)│ │ market) │ │ market) │ │ market) │          │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘          │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 V2X Communication Architecture

| Mode | Interface | Band | Latency | Bandwidth | Use Cases |
|------|-----------|------|---------|-----------|-----------|
| **LTE-V2X PC5** | Direct comm | 5.9 GHz | < 20 ms | Medium | V2V/V2I safety (BSM/CAM, RSI, RSM, MAP, SPAT) |
| **LTE-Uu / 5G Uu** | Cellular | Operator band | < 100 ms | High | V2N high-bandwidth (map update, video) |
| **5G NR-V2X** | Direct + cellular | 5.9 GHz + operator | < 5 ms | High | Future advanced automated-driving apps |

### 4.3 Technology-Route Selection

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Comms mode | [C-V2X PC5 primary, 5G Uu secondary] | [Maturity, ecosystem, standards direction] |
| Roadside sensing | [Camera + mmWave radar fusion] | [Best cost/perf for current use cases] |
| Edge compute | [Deploy MEC] | [Meets <20 ms latency requirement] |
| Security | [PKI/SCMS with international crypto: ECDSA-256 + AES-128-CCM] | [Meets security & privacy compliance] |

---

## 5. Roadside Infrastructure Design

### 5.1 RSU Deployment

#### 5.1.1 Site Plan

| ID | Location | Type | Coverage | Mounting | Comms |
|----|----------|------|----------|----------|-------|
| RSU-01 | [XX Rd × XX Rd junction] | Junction | [4 approaches, ~300 m] | [Signal-pole mount] | C-V2X PC5 |
| RSU-02 | [XX corridor mid] | Segment | [Both ways, ~500 m] | [New L-pole] | C-V2X PC5 |
| RSU-03 | [XX tunnel entrance] | Special | [Tunnel mouth, ~200 m] | [Gantry] | C-V2X PC5 |
| ... | ... | ... | ... | ... | ... |

#### 5.1.2 RSU Spec

| Parameter | Requirement |
|-----------|-------------|
| Comms mode | C-V2X PC5 (5.9 GHz) |
| Tx power | 23 dBm |
| Coverage | ≥ 500 m (LOS) |
| Latency | ≤ 20 ms (PC5 Mode 4 / sidelink) |
| Band | 5905–5925 MHz |
| Positioning | GNSS (multi-constellation), timing accuracy ≤ 1 μs |
| Network | 1×1000M Ethernet (fiber) + 4G/5G backup |
| V2X messages | BSM/CAM, RSI, RSM, MAP, SPAT, TIM |
| Security | ECDSA-256 + AES-128-CCM; PKI certificate mgmt |
| Temp | −40 °C ~ +85 °C |
| Ingress | ≥ IP67 |
| Power | PoE / AC 220 V |

### 5.2 Sensing Device Deployment

#### 5.2.1 Cameras

| Model / Spec | Resolution | Focal / FOV | Mount | Qty | Use |
|--------------|-----------|-------------|-------|-----|-----|
| [Panoramic bullet] | [8 MP] | [2.8–12 mm] | [Signal-pole] | [XX] | Panoramic monitoring |
| [AI camera] | [4 MP] | [Fixed 6 mm] | [L-pole arm] | [XX] | Vehicle detect, ANPR, event detect |

#### 5.2.2 mmWave Radar

| Model / Spec | Range | FOV | Mount | Qty | Use |
|--------------|-------|-----|-------|-----|-----|
| [XX] | [250 m] | [H ±XX° / V ±X°] | [L-pole arm] | [XX] | Position / speed / trajectory |

#### 5.2.3 LiDAR (optional)

| Model / Spec | Lines | Range | FOV | Mount | Qty | Use |
|--------------|-------|-------|-----|-------|-----|-----|
| [XX] | [128] | [200 m @10% reflectivity] | 360° | [Junction high-point] | [X] | High-precision detection & classification |

### 5.3 MEC Spec

| Parameter | Requirement |
|-----------|-------------|
| CPU | [e.g., 2× Intel Xeon 32-core] |
| GPU / NPU | [e.g., 1× NVIDIA T4 / L4] |
| Memory | ≥ [64] GB |
| Storage | ≥ [2] TB SSD |
| Network | 2×10GE SFP+ (fiber uplink), 4×GE RJ45 |
| OS | [Linux — Ubuntu / RHEL] |
| Functions | Multi-source fusion, V2X msg generation/routing, local decision, signal linkage |
| Temp | −40 °C ~ +70 °C |
| Ingress | ≥ IP65 |

### 5.4 Poles, Power & Comms

| Type | Description |
|------|-------------|
| Poles | Prefer existing signal / enforcement / surveillance poles; new L-poles 6–8 m, arm 4–8 m |
| Power | Prefer existing signal/surveillance power; new points tap nearest cabinet; UPS at key points |
| Comms | Prefer existing fiber ducts; no-duct points use [new fiber / 5G CPE / microwave backhaul] |

---

## 6. On-Board Unit Specifications

### 6.1 OBU Types

| Type | Vehicle | Mount | Qty |
|------|---------|-------|-----|
| Factory OBU | [New buses / specific test fleet] | Factory-integrated | [XX] |
| After-market OBU (mirror-type) | [Taxi / ride-hail] | Replace rear-view mirror | [XX] |
| After-market OBU (box-type) | [Bus / fleet / police / sanitation] | Windshield / dash | [XX] |

### 6.2 OBU Spec

| Parameter | Requirement |
|-----------|-------------|
| Comms | C-V2X PC5 + 4G/5G Uu |
| Positioning | GNSS (multi-constellation), accuracy ≤ 1.5 m (RTK cm-level) |
| HMI | [After-market: 5"/7" touch + voice] / [Factory: head-unit display] |
| CAN | Standard CAN/LIN (factory), read speed/steer/brake/light |
| V2X messages | BSM/CAM send (≥10 Hz), receive RSI/RSM/MAP/SPAT |
| Security | ECDSA-256 + AES-128-CCM; PKI/SCMS |
| Temp | −40 °C ~ +85 °C |
| Storage | ≥ [32] GB |
| Power | 12 V / 24 V vehicle adapt |

---

## 7. Cloud-Control Platform Design

### 7.1 Functional Architecture

| Domain | Module | Description |
|--------|--------|-------------|
| **Device mgmt** | RSU / sensing / OBU / MEC mgmt | Register / config / monitor / OTA |
| **Data aggregation** | V2X / sensing / vehicle / GIS | Real-time + batch ingest & store |
| **Service** | Scenario orchestration, event handling, msg distribution, open API | Core business logic |
| **Global decision** | Area signal opt., dynamic lane, route coordination, emergency priority | Cross-junction global optimization |
| **Security cert** | SCMS / CA mgmt, issue / renew / revoke | Basis of secure V2X (Ch.10) |
| **Visualization** | GIS situation, vehicle heatmap, device status, scenario KPIs | Wall + PC |

### 7.2 Cloud Deployment

| Item | Description |
|------|-------------|
| Environment | [Public / private / hybrid cloud] |
| Compute | [XX cores / XX GB RAM / XX TB SSD] |
| Database | [Time-series: TimescaleDB / InfluxDB] + [RDBMS: PostgreSQL] + [Cache: Redis] |
| Message bus | [Kafka / Pulsar] for V2X streams |
| Container | [Kubernetes] for microservices |

---

## 8. Use-Case Design

### 8.1 Classification (Day I / Day II)

| Phase | Typical Use Cases | Description |
|-------|-------------------|-------------|
| **Day I (near-term)** | Safety warning + efficiency | Driver assistance; warn driver, no vehicle control |
| **Day II (long-term)** | Cooperative control | Perception/s intent sharing, cooperative decision, partial control |

### 8.2 Day I Use-Case List

#### 8.2.1 Safety Use Cases

| ID | Name | Description | Trigger | Method | Effect |
|----|------|-------------|---------|--------|--------|
| S-01 | **Intersection collision warning** | RSU detects collision risk, warns vehicles | Fusion + BSM risk analysis | RSU→OBU (RSM) | Junction crash ↓[XX%] |
| S-02 | **VRU collision warning** | Detects pedestrian / cyclist on carriageway, warns nearby vehicles | Cam+radar VRU track | RSU→OBU (RSM) + V2P | Pedestrian crash ↓[XX%] |
| S-03 | **Emergency-vehicle warning** | Fire/ambulance/police broadcast position, ask yield | Emergency OBU special BSM | V2V (BSM) | Emergency travel time ↓[XX%] |
| S-04 | **Work-zone / incident warning** | RSU warns approaching vehicles of work/incident | MAP + alert config | RSU→OBU (RSI) | Intrusion crash ↓ |
| S-05 | **Hazardous-section warning** | Curve / steep / tunnel / blackspot warning | Geo-fence + position | RSU→OBU (RSI) | Crash ↓ |
| S-06 | **Adverse-weather warning** | Visibility / weather station triggers warning | Weather sensor | RSU→OBU (RSI) | Weather crash ↓ |
| S-07 | **Red-light warning** | Detects possible red-light run, warns | Signal state + pos/speed | RSU→OBU (RSM) | Red-light crash ↓ |
| S-08 | **Ahead-congestion warning** | Detects downstream congestion, warns upstream | Sensing / floating car | RSU→OBU (RSI) | Rear-end crash ↓ |

#### 8.2.2 Efficiency Use Cases

| ID | Name | Description | Trigger | Method | Effect |
|----|------|-------------|---------|--------|--------|
| E-01 | **Green-wave speed guidance** | Recommends optimal speed for green passage | SPAT + pos/speed | RSU→OBU (SPAT+MAP) | Stops ↓[XX%] |
| E-02 | **Transit priority** | Bus near junction → RSU extends green / shortens red | Bus OBU request | OBU→RSU→Controller | Bus delay ↓[XX%] |
| E-03 | **Dynamic lane mgmt** | Publish variable-lane info via V2X by demand | Flow monitor | RSU→OBU (RSI) | Capacity ↑[XX%] |

#### 8.2.3 Service Use Cases

| ID | Name | Description | Method | Effect |
|----|------|-------------|--------|--------|
| SV-01 | **In-vehicle sign reminder** | Push speed/regulatory/warning signs to cabin | RSU→OBU (RSI) | Sign awareness ↑ |
| SV-02 | **Real-time conditions** | Provide ahead road conditions | Cloud→OBU (V2N) | Experience ↑ |
| SV-03 | **Parking guidance** | Push destination parking availability + nav | Cloud→OBU (V2N) | Parking efficiency ↑ |

### 8.3 Day II Outlook

| ID | Name | Description | Tech Need |
|----|------|-------------|-----------|
| D2-01 | **Cooperative lane change** | Vehicle broadcasts intent, coordinates | 5G NR-V2X + high-precision positioning |
| D2-02 | **Sensor sharing** | Vehicles share perception ("see for me") | High-bandwidth V2V + fusion |
| D2-03 | **Cooperative intersection** | Signal-free junction negotiates order | NR-V2X + intent protocol |
| D2-04 | **Platooning** | Vehicles form platoon, shorter gap, less energy | NR-V2X + high-precision control |

---

## 9. Data Flow & Interface Design

### 9.1 Core V2X Message Set

| Message | Short | Sender | Freq | Content |
|---------|-------|--------|------|---------|
| **Basic Safety Message (CAM/BSM)** | BSM | OBU | 10 Hz | Pos, speed, heading, accel, brake, size |
| **Road Side Information** | RSI | RSU | 1–5 Hz | Road events: crash, work, congestion, weather, signs |
| **Road Side Safety Message** | RSM | RSU | 10 Hz | Roadside-detected road users (veh/ped/cyclist) |
| **MAP Message** | MAP | RSU | 1 Hz | Lane-level junction/segment topology |
| **Signal Phase and Timing** | SPAT | RSU (from controller) | 10 Hz | Current phase + remaining time |
| **Traveler Information Msg** | TIM | RSU | On demand | Service info (parking, charging) |

### 9.2 Data Flow

```
OBU ──BSM──► RSU ──BSM fwd + RSM gen──► nearby OBU  (V2V via RSU)
OBU ──VehData──► MEC ──result──► RSU ──msg──► OBU
RSU ──RSI/RSM/MAP/SPAT──► OBU  (I2V)
Cam/Radar ──raw──► MEC ──perception──► RSU ──RSM──► OBU
Signal controller ──SPAT──► RSU ──SPAT──► OBU
RSU/OBU/MEC ──status+log──► Cloud  (mgmt plane)
Cloud ──global policy──► MEC/RSU  (decision push)
OBU/RSU ──BSM/perception──► Cloud  (data plane, global analysis)
```

### 9.3 Interface Spec

| Interface | Protocol | Note |
|-----------|----------|------|
| RSU ↔ OBU (PC5) | C-V2X PC5 / 3GPP | Direct comm |
| RSU ↔ MEC | TCP/IP (fiber) | Raw up / decision down |
| RSU/OBU ↔ Cloud (Uu) | HTTPS / MQTT | Mgmt + data |
| MEC ↔ Cloud | HTTPS / gRPC | Mgmt + data + decision |
| RSU ↔ Signal controller | [NTCIP / UTF-8 TISC / proprietary driver] | Signal linkage |
| OBU ↔ Vehicle CAN | CAN 2.0B / CAN-FD | Vehicle info |

---

## 10. Security Framework (PKI / SCMS)

### 10.1 V2X Security Architecture

V2X secure communication is built on **PKI (Public Key Infrastructure)**, using **SCMS (Security Credential Management System)** to authenticate vehicles / roadside devices and secure messages.

```
┌──────────────────────────────────────────────┐
│              Root CA                            │
│         (National / regional C-ITS Root CA)     │
└──────────────────┬───────────────────────────┘
                   │
    ┌──────────────┼──────────────┐
    ▼              ▼              ▼
┌─────────┐  ┌─────────┐  ┌─────────┐
│ Enroll   │  │ Enroll   │  │ Pseudonym│
│ CA (ECA) │  │ CA (ECA) │  │ CA (PCA) │
└────┬────┘  └────┬────┘  └────┬────┘
     │            │            │
     ▼            ▼            ▼
┌─────────┐  ┌─────────┐  ┌─────────┐
│ Enroll    │  │ Enroll    │  │ Pseudonym │
│ Cert       │  │ Cert      │  │ Cert      │
│ (long-term)│  │ (long-term)│  │ (short-term│
│           │  │           │  │ anonymous) │
└─────────┘  └─────────┘  └─────────┘
    OBU         RSU          OBU
 (enroll auth)(identity auth)(broadcast sign)
```

### 10.2 Security Operations

| Service | Implementation |
|---------|----------------|
| **Identity auth** | Certificate-based authentication |
| **Message signing** | Each V2X message signed with private key (ECDSA-256) |
| **Message integrity** | Digital signature guarantees no tampering |
| **Privacy** | Pseudonym certificates — vehicle rotates certs periodically, hides long-term identity |
| **Revocation** | CRL updated periodically; revoke non-compliant / stolen devices |
| **Crypto** | International: ECDSA-256 + AES-128-CCM (per IEEE 1609.2 / SCMS) |

### 10.3 Security Deployment Strategy

| Phase | Strategy |
|-------|----------|
| **Build** | Connect to national / regional C-ITS trust framework (e.g., ETSI C-ITS PKI / US DOT SCMS) |
| **Pilot** | Use test certificates to validate secure comms |
| **Operation** | Switch to production certificates; establish local cert-management process |

---

## 11. Deployment Plan

### 11.1 Phasing

| Phase | Time | Scope | Content |
|-------|------|-------|---------|
| **Phase 1 Pilot** | [YYYY.MM–YYYY.MM] | [XX junctions + XX corridor, ~XX km] | [X] RSU, [X] sensing, [X] MEC, [X] OBU; validate [X] core scenarios |
| **Phase 2 Expand** | [YYYY.MM–YYYY.MM] | [Expand to XX km] | Add [X] RSU, [X] sensing, [X] OBU; add [X] scenarios |
| **Phase 3 Full cover** | [YYYY.MM–YYYY.MM] | [Whole zone] | Complete remaining sites; deepen scenarios |

### 11.2 Per-Site Deployment Flow

```
Site survey → design → civil works (base/duct/pole) → equipment install
    → power/comms commissioning → config → integration test → scenario validation → go-live
```

| Step | Duration | Key Point |
|------|----------|-----------|
| Site survey | [X] d | Confirm pole, power, comms route |
| Civil works | [X] d | Base, duct, pole |
| Equipment install | [X] d | RSU / cam / radar / MEC |
| Test & accept | [X] d | Config, integration, scenario validation |

---

## 12. Testing & Validation Plan

### 12.1 Test Stages

| Stage | Content | Location | Cycle |
|-------|---------|---------|-------|
| **Lab test** | Protocol conformance, message format, cert function | [Test lab] | [X] wks |
| **Closed-field** | End-to-end scenario test on closed track | [Test track] | [X] wks |
| **Open-road** | Real-traffic test on deployed segment | [Deployed segment] | [X] wks |
| **Pilot ops** | Continuous monitoring & fix after go-live | [Production] | [X] months |

### 12.2 Test Cases

| ID | Item | Method | Pass Criteria |
|----|------|--------|---------------|
| T-01 | PC5 performance | Drive test RSSI/RSRP, latency, loss | 400 m loss < 5%, latency < 20 ms |
| T-02 | BSM/CAM tx-rx | OBU sends, road tool verifies | Fields correct, 10 Hz |
| T-03 | MAP/SPAT | RSU sends, OBU receives | Content matches reality |
| T-04 | Collision warning (S-01) | Simulate collision | Timely ≥95%, false <5% |
| T-05 | Green-wave guidance (E-01) | Real vehicle | Reasonable speed, fewer stops |
| T-06 | Cert auth | Issue/use/revoke lifecycle | Full lifecycle passes |
| T-07 | Multi-vendor OBU interop | Two brands tx-rx | Interop ≥99% |
| T-08 | Availability | 24×7 run | Availability ≥99.9% |

---

## 13. Operations & Maintenance Plan

### 13.1 O&M Content

| Object | Content | Cadence |
|--------|---------|---------|
| RSU | Status monitor, coverage test, firmware upgrade | 24×7 / quarterly |
| Sensing | Lens clean check, image quality, radar calibration | Monthly |
| MEC | CPU/GPU/mem/disk monitor, sw upgrade, log rotate | 24×7 |
| OBU | Online monitor, cert expiry check, OTA | Continuous |
| Cloud | Health check, DB maint, backup/restore | 24×7 / daily |
| Security cert | Expiry alert, CRL update, batch renew | Continuous |

### 13.2 O&M Team

| Role | Headcount | Skills |
|------|-----------|--------|
| V2X O&M engineer | [X] | Protocols, roadside, network |
| App O&M engineer | [X] | Cloud, DB, middleware |
| Security O&M engineer | [X] | PKI, certs, network security |
| 24h duty | [X] | Fault response, first-line |

---

## 14. Investment Estimate

### 14.1 Investment Summary

| Category | Phase 1 | Phase 2 | Phase 3 | Total |
|----------|---------|---------|---------|-------|
| Roadside (RSU+MEC+sensing) | [€XXX k] | [€XXX k] | [€XX k] | [€XXX k] |
| OBU | [€XX k] | [€XX k] | [€X k] | [€XX k] |
| Cloud platform | [€XX k] | [€XX k] | [€X k] | [€XX k] |
| Civil (pole/duct/base) | [€XX k] | [€XX k] | [€X k] | [€XX k] |
| Power & comms | [€XX k] | [€X k] | [€X k] | [€XX k] |
| System integration | [€XX k] | [€XX k] | [€X k] | [€XX k] |
| Test & validation | [€X k] | [€X k] | [€X k] | [€X k] |
| O&M (1 yr) | [€X k] | [€X k] | [€X k] | [€X k] |
| Contingency | [€X k] | [€X k] | [€X k] | [€X k] |
| **Total** | **[€XXX k]** | **[€XXX k]** | **[€XX k]** | **[€XXX k]** |

### 14.2 Typical Cost per Junction

| Item / Works | Unit Price (€k) |
|--------------|-----------------|
| RSU (1 set) | [X] |
| AI camera (2) | [X] |
| mmWave radar (2) | [X] |
| MEC (1) | [X] |
| Pole + base + duct | [X] |
| Power + comms | [X] |
| Install + commission | [X] |
| **Per junction total** | **[€XX k]** |

---

## 15. Appendix

### Appendix A: Acronyms

| Acronym | Full Name |
|---------|-----------|
| V2X | Vehicle-to-Everything |
| V2V | Vehicle-to-Vehicle |
| V2I | Vehicle-to-Infrastructure |
| V2N | Vehicle-to-Network |
| V2P | Vehicle-to-Pedestrian |
| RSU | Road Side Unit |
| OBU | On-Board Unit |
| MEC | Multi-access Edge Computing |
| C-V2X | Cellular V2X |
| NR-V2X | New Radio V2X (5G-V2X) |
| PC5 | Direct communication interface (sidelink) |
| Uu | Cellular interface |
| BSM/CAM | Basic Safety / Cooperative Awareness Message |
| RSI | Road Side Information |
| RSM | Road Side Safety Message |
| MAP | Map Data message |
| SPAT | Signal Phase And Timing |
| TIM | Traveler Information Message |
| PKI | Public Key Infrastructure |
| SCMS | Security Credential Management System |
| CA | Certificate Authority |

### Appendix B: Typical Deployment Layout Description

[Attach CAD / GIS of the corridor / junction marking RSU, camera, radar, MEC positions. Example text:]

> "Take [XX Rd × XX Rd junction]: one RSU on each of the four signal-poles (covers 4 approaches); one AI camera + one mmWave radar on the NW and SE L-poles (full coverage); MEC in the SE composite cabinet; RSU fiber-linked to MEC; MEC uplinks via fiber to the cloud-control platform."

### Appendix C: Reference Cases

| Project | Location | Scale | Feature |
|---------|----------|-------|---------|
| [Singapore C-ITS / NCS pilot] | Singapore | [XX km] | [C-ITS corridor] |
| [Rotterdam Port automated trucking] | Rotterdam | [XX km] | [C-V2X + automated trucks] |
| [US DOT / Ann Arbor C-ITS] | Michigan, USA | [XX km] | [Large-scale V2X pilot] |
| [...] | [...] | [...] | [...] |

---

> **Prepared by:** [Authoring Team]
> **Reviewed by:** [Reviewer]
> **Approved by:** [Approver]
> **Date:** [YYYY-MM-DD]
