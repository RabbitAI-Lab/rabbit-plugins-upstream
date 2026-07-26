# Transport IoT Sensing System Plan

> **Version**: V1.0
> **Date**: ____ / __ / __
> **Prepared by**: _________
> **Reviewed by**: _________
> **Approved by**: _________

---

## Executive Summary

### Project Positioning
The [City / Region / Corridor Name] Transport IoT Sensing System Programme builds transport IoT infrastructure characterized by "full-awareness, ubiquitous connectivity, edge intelligence, and cloud fusion", providing a precise, real-time, and reliable data foundation for all smart-mobility scenarios.

### Objectives
By [Target Year], achieve:
- Sensing coverage: arterials ____% / collectors ____% / key nodes ____%
- Sensing accuracy: vehicle detection > ____%, event detection > ____%
- Comm. reliability: device online > ____%, data arrival > ____%
- Edge-compute coverage: ____% of junctions / segments with edge compute
- Manageable & controllable devices: device online management rate 100%

### Investment Overview
| Item | Value |
|------|------|
| Total estimated investment | $____ million |
| Construction period | ____ months |
| Annual O&M cost | $____ million / year |
| Device lifecycle | ____ years |

---

## 1. Current State Assessment

### 1.1 Existing Sensing Infrastructure
| Means | Qty | Coverage | Specs | Health (1–5) | Reusable? |
|----------|:----:|----------|----------|:-----------:|:----------:|
| Traffic video camera | __ | [range] | [px / focal] | | [Y / N / part] |
| ANPR / enforcement | __ | [range] | [params] | | |
| Inductive loop | __ | [range] | [params] | | |
| Magnetic / microwave detector | __ | [range] | [params] | | |
| Microwave / radar detector | __ | [range] | [params] | | |
| Weather station | __ | [range] | [params] | | |
| Environmental station | __ | [range] | [params] | | |
| Bridge health monitoring | __ | [range] | [params] | | |
| Toll / ETC gantry | __ | [range] | | | |

### 1.2 Existing Communications Infrastructure
| Means | Coverage | Bandwidth | Latency | Reliability | Assessment |
|----------|----------|:----:|:---:|:------:|------|
| Fiber backbone | | | | | |
| 4G / 5G | | | | | |
| NB-IoT | | | | | |
| Other (LoRa / Zigbee / etc.) | | | | | |

### 1.3 Pain-Point Analysis
| Pain | Symptom | Impact |
|------|------|------|
| Insufficient coverage | Many collectors / local / rural roads lack sensing | Monitoring blind spots |
| Single-dimension sensing | Reliance on video only; few radar / LiDAR | Weak adverse-weather / night sensing |
| Aging devices | Many beyond service life, high failure | Poor data / high O&M cost |
| No edge compute | All data sent to centre | Bandwidth pressure / high latency |
| Data silos | Sensors from different systems / vendors not interlinked | No cross-sensor fusion |
| No unified management | No IoT device-management platform | Opaque device status / slow fault detection |

---

## 2. Overall Architecture

### 2.1 Four-Layer Architecture
```
┌────────────────────────────────────────────────────────────┐
│  Layer 4  Platform & Application Layer                      │
│  ┌────────────┬────────────┬────────────┬──────────────┐   │
│  │IoT Device  │Data Ingest │Edge-Cloud  │Data Service  │   │
│  │Mgmt Platform│& Processing│Coordination │& Open API    │   │
│  │Register/   │Msg Queue/  │Model Push/ │Catalog/      │   │
│  │Config/     │Stream/     │Algo Update/│API Gateway/  │   │
│  │Monitor/OTA/│Batch/Store │Resource Sched│Data Sandbox │   │
│  │Alarm/O&M   │            │            │              │   │
│  └────────────┴────────────┴────────────┴──────────────┘   │
├────────────────────────────────────────────────────────────┤
│  Layer 3  Edge Computing Layer                              │
│  ┌──────────┬──────────┬──────────┬────────────────────┐   │
│  │MEC Node  │Smart     │Edge AI   │Edge-Cloud          │   │
│  │Compute    │Gateway   │Inference │Data Sync           │   │
│  │GPU Infer. │Protocol  │Object    │Lightweight Model  │   │
│  │Fusion    │Convert   │Event ID  │Incremental Sync    │   │
│  └──────────┴──────────┴──────────┴────────────────────┘   │
├────────────────────────────────────────────────────────────┤
│  Layer 2  Communications Layer                              │
│  ┌──────┬──────┬──────┬──────┬──────┬──────┬────────────┐  │
│  │Fiber │5G/4G │NB-IoT│LoRa  │DSRC/ │Sat.  │Industrial  │  │
│  │Back. │      │      │      │C-V2X │      │Ethernet/TSN│  │
│  └──────┴──────┴──────┴──────┴──────┴──────┴────────────┘  │
├────────────────────────────────────────────────────────────┤
│  Layer 1  Sensing & Acquisition Layer                       │
│  ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────────┐  │
│  │Video│mm  │LiDAR│Mag.│Wx  │Env.│Struct│Acous│On- │Drone  │  │
│  │Cam │Wave│      │    │    │    │Health│    │Board│       │  │
│  └────┴────┴────┴────┴────┴────┴────┴────┴────┴────────┘  │
└────────────────────────────────────────────────────────────┘
```

---

## 3. Sensing Layer Design

### 3.1 Full Sensor Catalogue
| Class | Sensor type | Object | Key spec | Location | Data (per device / day) |
|------|-----------|----------|----------|----------|:----------------:|
| **Vision** | HD bullet / PTZ camera | Vehicle / pedestrian / event | [px / fps / IR] | Junction / corridor | 50–200 GB |
| **Vision** | Holistic junction camera | Full-junction 3D sensing | [multi-cam / fusion] | Junction gantry | 200–500 GB |
| **Vision** | Thermal camera | Pedestrian / animal / fire | [res / temp range] | Tunnel / mountain / perimeter | 20–50 GB |
| **Vision** | Panoramic stitching camera | Area panorama | [360° / 180°] | Hub / plaza | 100–200 GB |
| **Radar** | mmWave traffic radar | Trajectory / speed / count | [range / FoV / 4D] | Junction / corridor | 1–5 MB |
| **Radar** | Wide-area radar | 256 targets tracked | [range > 300 m] | Expressway / motorway | 5–10 MB |
| **Radar** | 4D imaging radar | Contour / height + speed + azimuth + elevation | [4D point cloud] | Priority junction | 50–100 MB |
| **LiDAR** | Roadside LiDAR | Road / vehicle / pedestrian 3D point cloud | [lines / range / accuracy] | Priority junction / hub | 200–500 GB |
| **LiDAR** | Tunnel LiDAR | In-tunnel vehicle / fire / deformation | [dust / moisture proof] | Tunnel ceiling | 100–200 GB |
| **Magnetic** | Magnetic / microwave detector | Presence / passage / speed / class | [accuracy / life] | Road surface / roadside | < 1 MB |
| **Weather** | Visibility sensor | Visibility | [10 m–50 km] | Motorway / bridge | < 1 MB |
| **Weather** | Pavement-state sensor | Pavement temp. / dry-wet / ice-snow / friction | [multi-param] | Embedded in pavement | < 1 MB |
| **Weather** | Wind speed / direction | Wind speed / direction | [range / accuracy] | Bridge / viaduct | < 1 MB |
| **Weather** | Rain sensor | Rainfall / intensity | [resolution] | Roadside | < 1 MB |
| **Env.** | Air-quality sensor | PM2.5 / PM10 / CO / NO2 / O3 | [accuracy] | Tunnel / roadside | < 1 MB |
| **Env.** | Noise sensor | Traffic noise / level | [freq range / dBA] | Sensitive segments | < 1 MB |
| **Struct.** | Bridge health monitoring | Strain / vibration / displacement / tilt / cable force | [accuracy / sampling] | Bridge critical section | 1–100 MB |
| **Struct.** | Slope / landslide monitoring | Deep / surface displacement / groundwater / rainfall | [accuracy] | Slope / embankment | < 50 MB |
| **Struct.** | Tunnel structure monitoring | Deformation / crack / leak / convergence | [accuracy] | Tunnel lining | 1–50 MB |
| **Acoustic** | Acoustic event detection | Crash / horn / brake / gunshot | [class count] | Tunnel / junction | 10–50 MB |
| **Comm.** | RSU (V2X) | V2I / V2P comm. / signal push | [PC5 / Uu / DSRC] | Junction / corridor | 1–10 MB |
| **Comm.** | OBU (V2X) | Onboard V2X comm. | [PC5 / Uu] | Vehicle | 1–10 MB |
| **Position** | GNSS / RTK base station | Differential correction | [accuracy / coverage] | High point / base | < 1 MB |
| **Position** | UWB base station | Indoor / tunnel positioning | [accuracy 10–30 cm] | Tunnel / underground | < 1 MB |

### 3.2 Deployment Density Guide
| Road type | Sensor combo | Spacing | Mount | Power | Backhaul |
|----------|-----------|:--------:|----------|----------|----------|
| **Motorway** | Camera + mmWave radar + weather | 500–1000 m | Gantry / L-pole | Mains / solar | Fiber / 5G |
| **Urban expressway** | Camera + mmWave radar | 300–500 m | L-pole / gantry | Mains | Fiber |
| **Urban arterial (junction)** | Enforcement + camera + radar (+ LiDAR) | Per junction | Signal / enforcement pole | Mains / tap | Fiber |
| **Urban arterial (segment)** | Camera + magnetic / microwave | 300–500 m | L-pole | Mains | Fiber / 5G |
| **Urban collector / local** | Camera (+ magnetic) | 500–800 m | Pole / shared | Mains / streetlight | 5G / 4G |
| **Tunnel** | Camera + thermal + LiDAR + env. + struct. | 50–100 m | Tunnel wall / ceiling | Tunnel supply | Fiber |
| **Bridge** | Camera + radar + struct. + weather | 100–200 m | Tower / barrier | Bridge supply | Fiber |
| **Slope / hazard section** | Camera + slope monitor + weather | By geology | Pole | Solar | 4G / 5G |
| **Rural road** | Camera (+ magnetic) key nodes | Key points only | Shared / standalone | Solar | 4G |

### 3.3 Power Supply Options
| Method | Scenario | Pros | Cons | Cost order |
|----------|----------|------|------|:------:|
| Mains connection | Urban roads / powered | Stable & reliable | Requires power approval / heavy works | $[3k–8k] / point |
| Streetlight tap | Roads with streetlights | Low cost / fast | Coordinate with streetlight authority | $[1k–3k] / point |
| Signal / enforcement tap | Near signal / enforcement pole | Low cost | Limited power / coordination | $[1k–2k] / point |
| Solar + battery | Motorway / remote / no power | Standalone / green | Weather-dependent / big battery | $[5k–15k] / point |
| Wind-solar hybrid | Windy remote areas | All-weather | High cost / complex O&M | $[10k–20k] / point |

---

## 4. Communications Layer Design

### 4.1 Technology Selection
| Technology | Bandwidth | Latency | Range | Power | Typical use | Compliance |
|----------|:----:|:---:|:-------:|:---:|----------|:--------:|
| **Fiber (wired)** | > 1 Gbps | < 1 ms | 10–80 km | High | Backbone / fixed | Open standard |
| **5G NR** | > 100 Mbps | < 10 ms | 200–500 m | Med | Video / V2X / edge | 3GPP / standard |
| **4G LTE** | > 10 Mbps | 50 ms | 1–5 km | Med | Non-real-time / backup | 3GPP / standard |
| **NB-IoT** | < 250 kbps | 1–10 s | 10–50 km | Very low | Sensors (mag / wx / env) | 3GPP / standard |
| **LoRa / LoRaWAN** | < 50 kbps | 1–10 s | 2–20 km | Very low | Low-power sensors | Open standard |
| **C-V2X PC5** | > 30 Mbps | < 10 ms | 300–1000 m | Med | V2I / V2V | 3GPP / standard |
| **Wi-Fi 6** | > 1 Gbps | < 10 ms | 50–200 m | Med | Hub / yard / indoor | IEEE 802.11ax |
| **Industrial Eth. / TSN** | > 1 Gbps | < 1 ms | < 100 m | Med | Device interconnect (cabinet) | IEEE 802.1 / TSN |
| **Satellite** | 1–100 Mbps | 30–250 ms | Global | High | Remote / emergency backup | Inmarsat / Iridium / LEO |
| **Bluetooth / BLE** | < 2 Mbps | < 10 ms | 10–100 m | Very low | Indoor position / near-field | Bluetooth SIG |

### 4.2 Link Design
```
Sensor / device ──┬──→ Smart gateway ──→ Fiber / 5G ──→ Data centre
                  │
                  ├──→ 5G CPE ──→ 5G base ──→ Data centre
                  │
                  ├──→ NB-IoT / LoRa ──→ Base / gateway ──→ Data centre
                  │
                  └──→ MEC edge node (local processing)
```

### 4.3 Network Reliability
| Measure | Explanation |
|----------|------|
| Link redundancy | Critical nodes: fiber + 5G dual-link auto-failover |
| Local cache | Store locally on outage (≥ 7 days), retransmit on recovery |
| QoS | Priority tiers: safety / emergency > flow > video > environment |
| Network monitoring | Real-time status + link-quality + auto-alert |

---

## 5. Edge Computing Layer Design

### 5.1 MEC Edge Nodes
| Location | Hardware | Compute | Main tasks | Qty |
|----------|----------|:---:|----------|:---:|
| Junction MEC | [industrial edge server / GPU box] | > [10/20/50/100] TOPS | Multi-sensor fusion + object detection + flow extraction + signal state + event ID | __ |
| Segment MEC | [industrial edge server] | > 20 TOPS | Radar + video fusion + trajectory + anomaly + queuing | __ |
| Tunnel MEC | [industrial control grade] | > 20 TOPS | Tunnel full sensing + fire detection + tracking + device control | __ |
| Hub MEC | [high-perf edge server] | > 100 TOPS | Multi-source fusion + crowd analysis + safety + emergency linkage | __ |

### 5.2 Edge AI Capabilities
| AI task | Model | Accuracy | Latency | Location |
|--------|------|:---:|:--------:|----------|
| Vehicle detection & classification | YOLO-series / lightweight detector | mAP > 90% | < 30 ms | Junction / segment MEC |
| Pedestrian / micromobility detection | Same | mAP > 85% | < 30 ms | Junction MEC |
| License-plate recognition | LPRNet / lightweight OCR | Accuracy > 98% | < 50 ms | Junction MEC |
| Multi-object tracking | DeepSORT / ByteTrack | MOTA > 80% | Real-time | Junction / segment MEC |
| Traffic event detection | Classification + temporal | > 95% recall | < 100 ms | Junction / segment MEC |
| Traffic parameter extraction | Statistics / regression | Accuracy > 95% | < 100 ms | Junction / segment MEC |
| Pavement distress detection | Classification / segmentation | > 90% | Non-real-time | Inspection vehicle / drone |
| Structural anomaly detection | Anomaly / temporal | > 90% | Non-real-time | Bridge / slope |

### 5.3 Edge-Cloud Coordination
| Mode | Explanation |
|------|------|
| Tiered processing | Real-time / safety at edge; statistics / analysis to cloud |
| Cloud training | Cloud trains on full data → compress / distill → push to edge |
| Edge incremental learning | Local incremental learning → upload gradients → cloud aggregation (federated) |
| Unified cloud scheduling | Cloud manages model versions / config / algo upgrades for all edge nodes |

---

## 6. Platform Layer Design

### 6.1 IoT Device Management Platform
| Module | Explanation |
|----------|----------|
| **Device registration** | Info entry / class / location / vendor / model / firmware / install date / maintenance cycle |
| **Device auth** | Certificate / key / access auth (per-device / per-type secret) |
| **Device monitoring** | Online state / CPU / memory / temp. / signal / power real-time |
| **Device config** | Remote param / firmware OTA / algo update / restart |
| **Device alarm** | Offline / fault / abnormal value / env. anomaly / unauthorized access |
| **Device topology** | Physical / logical topology graph (sensor → gateway → MEC → centre) |
| **O&M management** | Inspection plan / maintenance reminder / repair log / spare parts / fault KB |
| **Data analytics** | Health score / fault prediction / life prediction / O&M cost analysis |

### 6.2 Data Ingestion Platform
| Function | Explanation |
|------|------|
| **Multi-protocol ingest** | MQTT / CoAP / HTTP / gRPC / Modbus / OPC-UA / ONVIF (video) / RTSP |
| **Message routing** | Rule-based routing (device → queue / store / stream / API) |
| **Data parsing** | Standard data model + protocol adapter auto-convert |
| **Data quality** | Real-time validation (format / range / frequency / completeness) |
| **Flow control** | Ingress throttle / peak-shaving / QoS tiers |
| **Storage** | Hot (TSDB) / warm (object) / cold (archive) + tiered strategy |

### 6.3 AI Algorithm Management Platform
| Function | Explanation |
|------|------|
| **Model registry** | Unified version / accuracy / target-hardware for all models |
| **Model training** | Cloud training + labeling + evaluation + auto-tuning |
| **Model deploy** | One-click to edge node + canary + A/B test |
| **Model monitoring** | Accuracy / latency / throughput / resource real-time + drift alert |
| **Model optimization** | Compression / quantization / distillation / pruning for edge |
| **Federated learning** | Privacy-preserving distributed training framework |

---

## 7. Deployment Plan

### 7.1 Deployment Principles
| Principle | Explanation |
|------|------|
| Maximize existing poles | Prefer shared poles (signal / enforcement / streetlight / sign); minimize new |
| Multi-function pole | New poles use smart multi-function design (sensing + comm. + lighting + sign + charging) |
| Modular design | Modular sensor install for easy maintenance / replacement / upgrade |
| Protection grade | Outdoor IP65+, lightning / moisture / salt-fog / corrosion proof |
| EMC | EMC design among sensor / comm. / power devices |

### 7.2 Smart Multi-Function Pole
| Function | Optional module | Explanation |
|----------|----------|------|
| Base lighting | LED streetlight | Base, smart control |
| Sensing | Camera / radar / weather / env. | Plug-and-play standard interface |
| Communications | 5G small cell / AP / RSU / LoRa gateway | Reserved mount + power + fiber |
| Info release | LED info screen / broadcast | |
| Edge compute | MEC cabinet | Integrated pole-side cabinet |
| Charging | EV charger (slow / fast) | Roadside parking charging |
| Aesthetics | Form / color / cultural element | Harmonize with cityscape |

### 7.3 Protection Design
| Item | Measure | Standard |
|--------|----------|------|
| Water / dust | Sealed housing + junction box + breather | IP65 / IP67 |
| Lightning | Power (class I+II) + signal + ground < 4 Ω | IEC 62305 |
| Temp. control | Heater (cold start) + fan / TEC + sunshade | -40 °C ~ +70 °C |
| Wind | Pole wind-load calc + wind-resistant design | Local wind-pressure code |
| Corrosion | Hot-dip galvanize + paint / powder + stainless fasteners | ISO 12944 |
| Anti-theft / vandal | Tamper screws + tilt / vibration alarm + video | |
| EMC | Shielding + equipotential bond + filter | IEC 61000 |

---

## 8. Operations & Maintenance

### 8.1 O&M System
| Task | Method | Frequency | Tool / System |
|----------|------|:----:|----------|
| Daily patrol | Remote auto-patrol | Daily | IoT platform |
| Periodic patrol | Manual on-site | Monthly / quarterly | Patrol app + checklist |
| Fault repair | Remote diag → on-site fix | Event-driven | Work-order system |
| Device cleaning | Manual (lens / radome / cooling) | Semi-annual | Maintenance plan |
| Device calibration | Sensor calibration / verification | Annual | Calibration + record |
| Firmware upgrade | OTA remote | As needed | IoT platform OTA |
| Model update | Cloud train → OTA push | As needed / periodic | AI platform |

### 8.2 SLA Targets
| Indicator | Target |
|------|:------:|
| Device online rate (annual) | > 99.5% |
| Device online rate (core) | > 99.9% |
| Data arrival rate | > 99.5% |
| Fault response time | < 30 min |
| Fault repair (general) | < 24 h |
| Fault repair (critical) | < 4 h |
| Data accuracy compliance | > 95% |

---

## 9. Security System

### 9.1 Device Security
| Measure | Explanation |
|----------|------|
| Device identity | Per-device secret: unique certificate / X.509 key |
| Secure boot | Firmware signature check + tamper resistance |
| Secure comm. | MQTT / TLS + HTTPS + DTLS encryption |
| Intrusion detection | Abnormal access / behavior detection |
| Physical security | Tamper detection / anti-theft / anti-vandal |

### 9.2 Data Security
| Measure | Explanation |
|----------|------|
| Transport encryption | TLS 1.3 / DTLS end-to-end |
| At-rest encryption | AES-256 data encryption |
| Access control | Role- and device-based data access |
| Data masking | Real-time face / plate masking in video streams |
| DLP | DLP + abnormal-access detection + watermark |
| Retention | Retain raw data & audit logs per regulation |

---

## 10. Standards Compliance

| Category | Standard | Title | Application |
|----------|----------|----------|------|
| Video surveillance | ONVIF Profile T / S | Network video interface | Video ingest |
| Video security | ISO / IEC 27001 | Information security management | Video security |
| Traffic info collection | ISO 14825 (GDF) | Geographic data files | Data coding |
| Traffic detection | IEEE / ISO 14825 | Traffic data collection | Detector standard |
| IoT device | oneM2M / ISO / IEC 21823 | IoT interoperability & sharing | IoT interop |
| IoT security | ISO / IEC 27001 / ETSI | IoT security reference | IoT security |
| Comm. security | ETSI / IEEE 1609 / ISO 21434 | V2X / automotive cybersecurity | V2X security |
| Smart pole | Local / sector standard | Smart multi-function pole spec | Pole design |
| Lightning & grounding | IEC 62305 | Protection against lightning | Lightning |
| Comm. line | ISO / IEC generic cabling | Fiber cabling design | Fiber wiring |

---

## 11. Investment Estimate

| No. | Item | Qty | Unit price ($k) | Amount ($k) | Share |
|:---:|----------|:---:|:-----------:|:----------:|:---:|
| 1 | HD camera | __ | $__ | $____ | __% |
| 2 | mmWave radar | __ | $__ | $____ | __% |
| 3 | LiDAR | __ | $__ | $____ | __% |
| 4 | Magnetic / microwave detector | __ | $__ | $____ | __% |
| 5 | Weather sensor | __ | $__ | $____ | __% |
| 6 | Env. sensor | __ | $__ | $____ | __% |
| 7 | Structural health monitoring | __ | $__ | $____ | __% |
| 8 | Edge compute MEC | __ | $__ | $____ | __% |
| 9 | RSU (V2X roadside unit) | __ | $__ | $____ | __% |
| 10 | Communications network | Package | — | $____ | __% |
| 11 | Power works | __ pts | $__ | $____ | __% |
| 12 | Poles / base / civil | __ pts | $__ | $____ | __% |
| 13 | IoT management platform | 1 set | — | $____ | __% |
| 14 | Data ingestion platform | 1 set | — | $____ | __% |
| 15 | AI algorithm platform | 1 set | — | $____ | __% |
| 16 | Security system | Package | — | $____ | __% |
| 17 | O&M (3 years) | Package | — | $____ | __% |
| 18 | Contingency | — | — | $____ | __% |
| | **Total** | | | **$____** | **100%** |

---

> **Usage note**: This template is for new-build or upgrade plans of urban-road / motorway / bridge / tunnel / hub sensing systems. Sensor selection must weigh reuse of existing devices and the technology evolution path; avoid premature investment in immature tech. Replace `[placeholder]` content with actual project data.

> **Legal notice**: This template is protected by copyright and related laws. It is provided for individual study and reference only; commercial use requires the author's written authorization.

> **Disclaimer**: This template is for study and reference only and does not constitute professional advice. Transport IoT involves large volumes of sensitive video (face / plate) and geospatial data; strictly comply with GDPR / privacy law / geospatial-data regulation. Conduct compliance review before implementation. The author accepts no liability for any loss arising from the use of or reliance on this template.

> **Author**: yinjianheng | yinjianheng@foxmail.com
