# Vehicle-Infrastructure-Cloud (VIC) Integrated Technology Whitepaper

> **Version**: V1.0.0 | **Updated**: July 2026 | **Scope**: Intelligent-transport planning & design / V2X technology selection / smart-highway project proposals / city-scale VIC pilot applications

---

## Table of Contents

1. [System Architecture Overview — the "1+N+X" Framework](#1-system-architecture-overview)
2. [Roadside Perception System Design](#2-roadside-perception-system-design)
3. [Communications System Design (C-V2X PC5 + Uu)](#3-communications-system-design)
4. [MEC Edge-Computing Platform](#4-mec-edge-computing-platform)
5. [Cloud-Control Platform Architecture](#5-cloud-control-platform-architecture)
6. [HD Map & Positioning System](#6-hd-map--positioning-system)
7. [Security Credential Management (SCMS/PKI)](#7-security-credential-management-scmspki)
8. [Interoperability & Standardization](#8-interoperability--standardization)
9. [Performance Benchmarks & SLA Metrics](#9-performance-benchmarks--sla-metrics)
10. [Deployment Models & Implementation Path](#10-deployment-models--implementation-path)
11. [Whole-Lifecycle Cost Model (CAPEX/OPEX/TCO)](#11-whole-lifecycle-cost-model)
12. [Global Deployment Comparison (China vs US vs EU vs Japan)](#12-global-deployment-comparison)
13. [Technology Evolution Roadmap (5G-V2X → 5G-A → 6G)](#13-technology-evolution-roadmap)
14. [Standards & Compliance Matrix](#14-standards--compliance-matrix)
15. [Appendix: Key Terminology](#15-appendix-key-terminology)

---

## 1. System Architecture Overview

### 1.1 The "1+N+X" Framework Defined

The Vehicle-Infrastructure-Cloud integrated architecture (internationally framed as **C-ITS / V2X** with a cloud-control layer) is logically divided into three tiers:

```
┌─────────────────────────────────────────────────────────────────────┐
│                       X: Multi-tier Cloud-Control Platform            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐ │
│  │ City-level│  │ Regional │  │ Edge     │  │ Cross-domain coord.  │ │
│  │ cloud     │  │ cloud    │  │ cloud    │  │ cloud (province/MEG) │ │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └──────────┬───────────┘ │
│       └──────────────┴─────────────┴───────────────────┘             │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                       N: Multi-level Communications Network            │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐                │
│  │ C-V2X PC5   │  │ 5G Uu interface│  │ Fiber backbone│                │
│  │ (direct)    │  │ (cellular)    │  │ (backhaul)    │                │
│  └──────┬──────┘  └──────┬───────┘  └──────┬───────┘                │
│         └────────────────┴────────────────┘                         │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                 1: Integrated Perception & Execution Layer             │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐            │
│  │ Roadside  │ │ Roadside  │ │ Roadside  │ │ On-board  │            │
│  │ perception│ │ compute   │ │ comms     │ │ unit      │            │
│  │ RSU/RCU   │ │ MEC/edge  │ │ RSU/5G    │ │ OBU/T-Box│            │
│  │ cam/radar │ │ fusion    │ │ PC5/NR-V2X│ │ V2X stack │            │
│  └───────────┘ └───────────┘ └───────────┘ └───────────┘            │
└─────────────────────────────────────────────────────────────────────┘
```

**Core data-flow paths**:

| Data flow | Path | Typical latency | Volume |
|----------|------|-----------------|--------|
| Perception sharing | Roadside RSU → OBU (PC5) | <20ms | 2–50 Mbps |
| Cooperative decision | Roadside MEC → vehicle OBU | <50ms | 1–10 Mbps |
| Remote monitoring | Roadside → regional → city cloud | <200ms | 50–200 Mbps |
| OTA update | City cloud → OBU (Uu) | Non-real-time | 1–5 GB/event |
| Digital-twin sync | Roadside → cloud-control | <500ms | 100–500 Mbps |

### 1.2 Cloud-Control Platform Tiered Architecture (X-tier detail)

| Tier | Deployment | Coverage | Core function | Typical hardware |
|------|-----------|----------|---------------|------------------|
| **Edge cloud (EU)** | Road/intersection cabinet | 1–3 km | Real-time fusion, cooperative control, ms-level warning | 2–4 GPU servers + 1–2 CPU servers |
| **Regional cloud (RU)** | District data center | 50–200 km² | Regional optimization, cross-intersection coordination, trajectory mgmt | 10–20 GPU + 20–40 CPU cluster |
| **City cloud (CU)** | City data center | Whole city | Holistic network, macro decisions, emergency command, city services | 50–100+ server cluster + big-data platform |
| **Cross-domain cloud (CC)** | Province / metro area | Cross-city | Cross-city travel, logistics dispatch, regional joint response | Provincial cloud infra |

### 1.3 Overall VIC Architecture Diagram

```
Vehicle Domain (V)                Roadside Domain (R)              Cloud Domain (C)
─────────────────              ─────────────────             ─────────────────
┌──────────────┐              ┌──────────────┐             ┌──────────────────┐
│ AV system    │◄────PC5────►│ Roadside unit│──fiber/5G─►│  Edge cloud        │
│ (L2+/L3/L4)  │              │ RSU + MEC    │             │  real-time fusion │
├──────────────┤              ├──────────────┤             ├──────────────────┤
│ HMI          │◄────PC5────►│ signal/CMS   │────5G────►│  Regional cloud    │
│ nav/infotain │              │ roadside RSU │             │  regional optimize │
├──────────────┤              ├──────────────┤             ├──────────────────┤
│ On-board OBU │───Uu────────►│ 5G gNB       │◄──fiber──►│  City cloud        │
│ T-Box/V2X    │              │ MEC+UPF      │             │  global decision  │
├──────────────┤              ├──────────────┤             ├──────────────────┤
│ Vehicle sensors│             │ HD-position  │──private──►│  HD-map platform  │
│ cam/radar    │              │ RTK/CORS     │             │  dynamic layers   │
└──────────────┘              └──────────────┘             └──────────────────┘
       │                              │                              │
       └──────────────────────────────┴──────────────────────────────┘
                   Unified security auth (SCMS/PKI)
           V2X-CA cert mgmt / anonymous cert / pseudonym rotation
```

---

## 2. Roadside Perception System Design

### 2.1 Sensor Selection Matrix

| Sensor type | Range | Resolution/accuracy | Frame rate | Bad-weather | Unit price (USD) | Use case | Example models |
|-----------|-------|--------------------|-----------|------------|-----------------|----------|----------------|
| **4K camera** | 150–300m | 3840×2160 | 25–30fps | ★★☆ (rain/fog) | $0.7–2.8k | Plate ID, event detection, VRUs | Bosch AUTODOME / Axis Q62 |
| **Near-IR camera** | 100–200m | 1920×1080 | 25–30fps | ★★★ (night) | $1.4–4.2k | Night detection, tunnel monitoring | Teledyne FLIR A700 |
| **mmWave radar (77–79GHz)** | 250–350m | 0.1m / 0.5° | 50ms | ★★★★★ (all-weather) | $2–5.6k | Vehicle detect/track, speed, all-weather | Continental ARS540 / Bosch |
| **4D mmWave radar** | 300–400m | 0.05m / 0.3° / 0.1° elev | 50ms | ★★★★★ | $7–11k | High-precision object ID, low-profile objects | Arbe Phoenix / Continental |
| **LiDAR (solid-state)** | 200–300m | ±2cm@100m | 10–20Hz | ★★★ (penetrates) | $11–21k | 3D object, road profile, positioning aid | Luminar Iris / InnovizTwo |
| **LiDAR (MEMS)** | 150–250m | ±3cm@100m | 10–20Hz | ★★★ | $4–8k | Intersection holistic sensing, pedestrian ID | Aeva Aeries II / Ouster |
| **Ultrasonic** | 5–10m | ±1cm | 50ms | ★★★★ | $140–420 | Parking, near-field | Bosch USS6 |
| **Magnetic / microwave detector** | Single lane | Count accuracy >98% | Real-time | ★★★★★ | $0.4–1.4k | Section flow, occupancy | SWARCO M100 / FLIR |

### 2.2 Typical Intersection Sensor Layout

**Standard urban cross intersection (4 approaches × 6 lanes)**:

```
                       North (through+left+right)
                              │
                    ┌─────────┼─────────┐
                    │ C1,R1   │ C2,R2   │
                    │  (L1)    │         │
       West ────────┤         │         ├────────── East
    (through+left+rt)│         │         │(through+left+rt)
                    │ C4,R4   │ C3,R3   │
                    │         │ (L2)    │
                    └─────────┼─────────┘
                              │
                       South (through+left+right)
```

| Location | Devices | Qty | Function | Height | Coverage |
|---------|---------|-----|----------|--------|----------|
| Diagonal pole A | 4K cam ×2 + mmWave ×1 + MEC ×1 | 1 set | All-direction vehicle detection, signal-state ID | 6–8m | 120° fan/unit |
| Diagonal pole B | 4K cam ×2 + LiDAR ×1 | 1 set | 3D object, pedestrian/cyclist ID | 6–8m | 120° fan/unit |
| Approach through | 4K cam ×1 + mmWave ×1 | 4 sets | Queue length, speed, arrival | 6–8m | 200m ahead |
| Crosswalk zone | 4K cam ×1 + ultrasonic ×2 | 4 sets | Pedestrian, red-light warning | 4–6m | Crosswalk area |
| Intersection center | MEC ×1 + RSU ×1 + GPS/GNSS antenna | 1 set | Fusion compute, V2X comms, time sync | Pole/cabinet | — |

**Single-intersection device summary**:

| Device | Qty | Unit price (USD) | Subtotal (USD) |
|--------|-----|------------------|----------------|
| 4K camera | 12 | $1.7k | $20k |
| mmWave radar | 6 | $3.5k | $21k |
| Solid-state LiDAR | 2 | $14k | $28k |
| MEC unit | 2 | $11k | $22k |
| RSU unit | 1 | $7k | $7k |
| Ultrasonic | 8 | $0.28k | $2.2k |
| Poles/cabinets/cabling/install | 1 set | $21k | $21k |
| **Single intersection total** | — | — | **~$120k** |

### 2.3 Multi-Sensor Fusion Algorithm Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                    MEC Fusion-Perception Pipeline                │
├────────────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐  │
│  │ Camera 1..n│  │ mmWave   │  │ LiDAR    │  │ V2X messages │  │
│  │ video     │  │ point cloud│  │ 3D cloud │  │ CAM/BSM/MSM  │  │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └──────┬───────┘  │
│       ▼             ▼             ▼               ▼           │
│  ┌─────────────┐ ┌────────────┐ ┌───────────┐ ┌───────────┐  │
│  │ YOLOv8/RT-  │ │ DBSCAN     │ │ PointPillar│ │ Msg parsing│  │
│  │ DETR detect │ │ cluster+KF │ │ VoxelNet  │ │ ASN.1 decode│ │
│  └──────┬──────┘ └─────┬──────┘ └─────┬─────┘ └─────┬─────┘  │
│         └──────────────┼──────────────┼─────────────┘         │
│                        ▼              ▼                         │
│              ┌─────────────────────────────┐                  │
│              │   Time sync + spatial align (PTP/gPTP+joint calib)│
│              └─────────────┬───────────────┘                  │
│                            ▼                                  │
│              ┌─────────────────────────────┐                  │
│              │   Hungarian/JPDA data association               │
│              └─────────────┬───────────────┘                  │
│                            ▼                                  │
│              ┌─────────────────────────────┐                  │
│              │   IMM-UKF/EKF fusion tracking (state+trajectory)│
│              └─────────────┬───────────────┘                  │
│                            ▼                                  │
│              ┌─────────────────────────────┐                  │
│              │   Road-user classification + behavior prediction │
│              └─────────────┬───────────────┘                  │
│                            ▼                                  │
│              ┌─────────────────────────────┐                  │
│              │   Fused object list output                              │
│              │   (ID, Type, Pos, Vel, Heading, Size, Conf, Traj_5s)   │
│              └─────────────────────────────┘                  │
└────────────────────────────────────────────────────────────────┘
```

**Key fusion KPIs**:

| Metric | Target | Condition |
|--------|--------|-----------|
| Detection mAP | ≥95% | Day/night/rain |
| Tracking MOTA | ≥90% | Urban/highway |
| ID-switch rate | <1% | Dense traffic |
| Perception latency (E2E) | <100ms | Sensor → fused output |
| Miss rate | <3% | All weather |
| False-alarm rate | <1% | All weather |
| Fused positioning accuracy | <0.5m | 95% confidence |

### 2.4 Roadside Sensor Calibration

| Calibration | Method | Tooling | Cycle | Accuracy |
|------------|--------|---------|-------|----------|
| Joint extrinsic | Multi-sensor checkerboard/joint calibration | Calib board, total station, laser tracker | At install | Trans <2cm / Rot <0.1° |
| Camera intrinsic | Zhang's method (multi-pose) | Chessboard + OpenCV | Quarterly / on replace | Principal-pt <2px |
| Radar-camera | Paired-point PnP | Corner reflector + landmarks | Install + 6mo | Extrinsic <3cm |
| LiDAR-IMU | LI-Calib / hand-eye | Calib bay / open road | Install + quarterly | Angle <0.05° |
| Online self-calib | SLAM + lane constraints | Built-in fusion | Continuous | Drift <5cm/h |

---

## 3. Communications System Design

### 3.1 C-V2X PC5 Direct Communication

| Parameter | LTE-V2X (Rel.14/15) | NR-V2X (Rel.16/17) |
|-----------|---------------------|---------------------|
| Band | 5905–5925 MHz | 5905–5925 MHz + possible extension |
| Channel bandwidth | 10/20 MHz | 10/20/40 MHz |
| Peak rate (PC5) | ~30 Mbps | ~100 Mbps+ |
| E2E latency | 20–100ms | 3–10ms (URLLC) |
| Reliability | 90–95% (PER<10%) | 99.999% (PER<0.001%) |
| Range | 300–1000m (LOS) | 500–1500m (LOS) |
| Max speed | 250 km/h | 500 km/h |
| Modulation | SC-FDMA / QPSK/16QAM | OFDMA / QPSK~256QAM |
| MIMO | 1×1 / 1×2 | 2×2 / 4×4 |
| Multicast/broadcast | Supported | Enhanced (QoS tiers) |

### 3.2 Uu Cellular Interface

| Parameter | 5G SA (Rel.16+) | 5G-A (Rel.18+) | Note |
|-----------|-----------------|-----------------|------|
| Downlink peak | 1–2 Gbps | 5–10 Gbps | eMBB |
| Uplink peak | 200–500 Mbps | 1–2 Gbps | Video backhaul |
| Control-plane latency | 10–20ms | 5–10ms | uRLLC |
| Reliability | 99.999% | 99.9999% | ITU IMT-2020 |
| Connection density | 1M/km² | 10M/km² | mMTC |
| Mobility | 500 km/h | 1000 km/h | HSR scenario |
| Timing accuracy | ±390ns | ±100ns | IEEE 1588v2 |
| Cellular positioning | 3–10m (outdoor) | <1m (outdoor) | NR Positioning |

### 3.3 Communications Network Topology

```
                         ┌──────────────────────┐
                         │   City cloud (CU)     │
                         │   5G core (5GC)       │
                         └──────────┬───────────┘
                                    │ N6/N9
                    ┌───────────────┼───────────────┐
                    ▼               ▼               ▼
            ┌──────────┐   ┌──────────┐   ┌──────────┐
            │ Regional │   │ UPF anchor│   │ 5G gNB   │
            │ MEC      │   │ (breakout)│   │ (macro)  │
            └─────┬────┘   └─────┬────┘   └─────┬────┘
        ┌─────────┼──────────────┼──────────────┼─────────┐
        ▼         ▼              ▼              ▼         ▼
   ┌────────┐ ┌────────┐  ┌────────┐    ┌────────┐ ┌────────┐
   │RSU+MEC│ │RSU+MEC│  │RSU+MEC│    │5G micro│ │5G micro│
   │ jct 1 │ │ jct 2 │  │ seg 3  │    │ +MEC   │ │ +MEC   │
   └────┬───┘ └────┬───┘  └────┬───┘    └────┬───┘ └────┬───┘
        │          │           │             │          │
   ┌────┼──────────┼───────────┼─────────────┼──────────┼────┐
   │    ▼  PC5     ▼  PC5      ▼  PC5        ▼  Uu     ▼  Uu │
   │ ┌────┐    ┌────┐     ┌────┐        ┌────┐     ┌────┐  │
   │ │OBU │    │OBU │     │OBU │        │OBU │     │OBU │  │
   │ │v1  │    │v2  │     │v3 │        │v4 │     │v5 │  │
   │ └────┘    └────┘     └────┘        └────┘     └────┘  │
   └────────────────────────────────────────────────────────┘
```

### 3.4 Communications Performance Budget

| Scenario | E2E latency budget | Comms | Compute | Process | 3GPP TS |
|---------|-------------------|-------|---------|---------|-----------|
| Forward collision warning (FCW) | <100ms | <50ms | <40ms | <10ms | TS 22.186 |
| Intersection collision warning (ICW) | <100ms | <50ms | <40ms | <10ms | TS 22.186 |
| Emergency vehicle priority | <100ms | <50ms | <30ms | <20ms | TS 22.186 |
| Cooperative ACC (CACC) | <50ms | <20ms | <20ms | <10ms | TS 22.886 |
| Remote driving | <20ms | <10ms | <5ms | <5ms | TS 22.186 |
| Sensor sharing (HD) | <100ms | <60ms | <30ms | <10ms | TS 22.886 |
| Vulnerable road-user warning (VRU) | <100ms | <50ms | <40ms | <10ms | TS 22.186 |
| Cooperative lane change | <50ms | <20ms | <20ms | <10ms | TS 22.886 |

### 3.5 RSU Deployment Density Model

**Highway**:
| Parameter | Value | Note |
|----------|-------|------|
| RSU spacing (urban highway) | 400–600m | Overlap ≥100m |
| RSU spacing (mountain highway) | 300–400m | Curve occlusion |
| Lanes per RSU | Bidirectional 8 | 4+4 |
| RSUs per km | 1.7–2.5 | + ramp/interchange |
| RSUs per 100 km | 170–250 | — |

**Urban**:
| Parameter | Value | Note |
|----------|-------|------|
| Intersection RSU | 1–2 per junction | Signalized mandatory |
| Urban segment RSU | 1 per 500–800m | Building occlusion |
| Elevated/expressway RSU | 1 per 300–500m | High-speed |
| RSUs per km² (downtown) | 8–15 | Dense junctions |

---

## 4. MEC Edge-Computing Platform

### 4.1 MEC Hardware Specification

| Component | Standard (urban junction) | Enhanced (highway/hub) | Vehicle-grade |
|----------|---------------------------|------------------------|---------------|
| **CPU** | Intel Xeon D-2146NT / 2×EPYC 7282 | 2×Xeon Gold 6338N | ARM Cortex-A78AE |
| **GPU/AI accel.** | NVIDIA A2 (16GB) ×2 | NVIDIA A100 (80GB) ×2 | NVIDIA Orin (275 TOPS) |
| **Memory** | 64–128 GB DDR4 ECC | 256–512 GB DDR4 ECC | 32 GB LPDDR5 |
| **Storage** | 2×1TB NVMe SSD (RAID1) | 4×2TB NVMe SSD (RAID10) | 256 GB eMMC + 512 GB SSD |
| **FPGA (opt.)** | Xilinx Alveo U50 | Xilinx Alveo U250 | — |
| **Time sync** | IEEE 1588v2 PTP + GPS/GNSS dual | + Rubidium backup | GPS/GNSS + PTP |
| **Network** | 2×25GbE + 4×1GbE | 2×100GbE + 4×25GbE | 2×10GbE + 4×1GbE |
| **5G** | Built-in 5G (SA/NSA) | + local UPF breakout | Built-in 5G |
| **Environment** | 0–50°C, IP65 | −20–60°C, IP66 | −40–85°C, IP67 |
| **Power** | Dual AC 220V / 48V DC | Dual AC / 48V DC | 12/24V DC |
| **Unit price** | $11–21k | $35–70k | $4–11k |

### 4.2 MEC Software Stack

```
┌─────────────────────────────────────────────────────────────┐
│                MEC Application Layer (V2X Apps)                │
│  ┌───────────┐ ┌──────────┐ ┌──────────┐ ┌───────────────┐ │
│  │ Fusion    │ │ Coop.    │ │ Collision│ │ Signal priority│ │
│  │Sensing svc   │ │ decision │ │ warning  │ │ / green wave  │ │
│  └─────┬─────┘ └────┬─────┘ └────┬─────┘ └───────┬───────┘ │
├────────┼─────────────┼────────────┼───────────────┼─────────┤
│        ▼             ▼            ▼               ▼         │
│  ┌─────┴─────────────┴────────────┴───────────────┴───────┐ │
│  │           MEC Middleware / V2X Service Framework        │ │
│  │  message routing │ service registry │ data cache │ API gw│ │
│  └──────────────────────┬────────────────────────────────┘ │
├──────────────────────────┼──────────────────────────────────┤
│                          ▼                                  │
│  ┌─────────────────────────────────────────────────────────┐│
│  │           AI Inference Framework & Model Management       ││
│  │  TensorRT │ ONNX Runtime │ (MindSpore opt.) │ quantization││
│  └──────────────────────────┬──────────────────────────────┘│
├──────────────────────────────┼──────────────────────────────┤
│                              ▼                              │
│  ┌─────────────────────────────────────────────────────────┐│
│  │            Container Orchestration & Platform Mgmt        ││
│  │  K3s/k8s │ Harbor │ Prometheus + Grafana │ EFK/LOKI      ││
│  └──────────────────────────┬──────────────────────────────┘│
├──────────────────────────────┼──────────────────────────────┤
│                              ▼                              │
│  ┌─────────────────────────────────────────────────────────┐│
│  │            OS & Driver Layer                              ││
│  │  Ubuntu 22.04 LTS │ (OpenEuler opt.) │ GPU drv │ NIC/FPGA ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

### 4.3 AI Inference Optimization

| Technique | Method | Effect | Difficulty |
|-----------|--------|--------|-----------|
| **INT8/FP16 quant.** | TensorRT PTQ/QAT | 2–4× faster, −75% size | ★★☆ |
| **Pruning** | Structured/unstructured | 1.5–2× faster, <1% acc loss | ★★★ |
| **Knowledge distillation** | Teacher-student | Small model ≈ 95% of large | ★★★★ |
| **Op fusion** | Conv+BN+ReLU, MHA fusion | 1.3–1.8× faster | ★★☆ |
| **TensorRT/ONNX** | Graph opt + kernel autotune | 2–5× faster | ★★☆ |
| **Batching** | Multi-frame/stream | +50–100% GPU util | ★★☆ |
| **CPU-GPU pipeline** | Pre/inf/post split | +30–50% throughput | ★★★ |
| **OTA model update** | Delta + A/B deploy | −80% bandwidth | ★★★ |

### 4.4 MEC-V2X Standard Message Set

| Message | Content | Rate | Priority | Standard |
|---------|---------|------|----------|----------|
| **MAP** | Intersection/segment topology, lane info | 1–2 Hz | High | SAE J2735 / ETSI IFN |
| **SPAT** | Signal phase, remaining time | 10 Hz | Highest | SAE J2735 / ETSI SPATEM |
| **RSI** | Roadside event (incident/workzone/congestion) | Event | High | SAE J2735 / ETSI IVIM |
| **RSM** | Roadside perception share (fused list) | 10 Hz | Highest | SAE J2735 / ETSI |
| **BSM** | Basic safety message | 10 Hz | Highest | SAE J2735 / ETSI CAM |
| **VIR** | In-vehicle intent/request | 1–5 Hz | Medium | OEM profile |
| **MEC-Cloud** | MEC→cloud report | 0.1–1 Hz | Low | OEM/operator profile |

---

## 5. Cloud-Control Platform Architecture

### 5.1 Overall Functional Architecture

```
┌──────────────────────────────────────────────────────────────────────────┐
│                     City-level Cloud-Control Platform (CU)                 │
├──────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐          │
│  │ Unified     │  │ Open        │  │ Operations mgmt          │          │
│  │ portal      │  │ platform    │  │                         │          │
│  │ · situation │  │ · API gw    │  │ · device mgmt           │          │
│  │ · command   │  │ · dev center│  │ · IAM                   │          │
│  │ · mobility  │  │ · app market│  │ · monitoring/alerting   │          │
│  │ · O&M       │  │ · data open │  │ · billing               │          │
│  └──────┬──────┘  └──────┬──────┘  └────────────┬────────────┘          │
├─────────┴──────────────────┴──────────────────────┴──────────────────────┤
│                       Business App Layer (100+ scenarios)                  │
│  Intelligent signal │ Transit priority │ Parking guidance │ Emergency      │
│  MaaS │ AV (C-V2X, remote drive, platoon) │ Logistics │ Safety mgmt       │
├──────────────────────────────────────────────────────────────────────────┤
│                         Capability Middle-Platform (PaaS)                  │
│  Digital twin │ AI platform │ Data platform │ Business platform           │
│  Security platform │ DevOps platform │ Integration │ O&M platform         │
├──────────────────────────────────────────────────────────────────────────┤
│                         Data Layer (DaaS)                                  │
│  Real-time (Kafka) │ Time-series (TDengine/InfluxDB) │ Structured (PG)    │
│  Unstructured (MinIO/OSS) │ Graph (Neo4j/JanusGraph)                       │
├──────────────────────────────────────────────────────────────────────────┤
│                         Infra Layer (IaaS / cloud-native)                  │
│  K8s / KubeEdge │ Istio/Envoy │ GPU cluster (NVIDIA) │ Ceph/HDFS │ Calico  │
└──────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Digital-Twin Engine Architecture

| Component | Function | Core tech | KPI |
|----------|----------|-----------|-----|
| 3D render engine | City-scale HD render | Cesium / Unity3D / UE5 | 1M+ entities <16ms/frame |
| Spatio-temporal engine | Trajectory replay, flow viz | GeoMesa + PostGIS | 100M+ GPS pts <500ms |
| Physics sim engine | Traffic flow sim, incident rehearsal | SUMO / VISSIM | 10k-vehicle real-time |
| Semantic layer engine | Dynamic signs, workzones, events | GeoJSON + WMS/WMTS | Layer switch <200ms |
| Low-code orchestration | Drag-drop scenario | Node-RED | Assembly <5 min |
| Scenario mgmt | Plan mgmt, comparison | Versioning + A/B | Switch <1s |

### 5.3 Data Pipeline Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                           Data Acquisition Layer                       │
│  MEC report (protobuf) │ RSU/OBD (JSON) │ signal (NTCIP/ISO) │        │
│  video (RTSP/HLS) │ 3rd-party API                                        │
├────────────────────────────────┼─────────────────────────────────────┤
│                                ▼                                       │
│              Message Queue Layer (Kafka / Pulsar)                      │
│   perception topic │ signal topic │ status topic │ event topic         │
├────────────────────────────────┼─────────────────────────────────────┤
│                                ▼                                       │
│              Stream Computing Layer (Flink / Spark Streaming)          │
│   cleaning │ correlation (multi-stream join) │ feature extraction │    │
│   real-time metric computation                                           │
├────────────────────────────────┼─────────────────────────────────────┤
│                                ▼                                       │
│              Storage Layer (multi-model)                                │
│   hot (Redis, <7d) │ warm (ClickHouse/TDengine, <3mo) │               │
│   cold (HDFS, >3mo) │ data lake (Iceberg + Hive)                       │
└──────────────────────────────────────────────────────────────────────┘
```

### 5.4 API Gateway Design

| API category | Count | Examples | Auth | Rate limit | SLA latency |
|-------------|-------|----------|------|-----------|-------------|
| Perception | 20+ | Real-time object query, trajectory, event subscribe | JWT + API Key | 1000 QPS/tenant | <100ms |
| Control | 15+ | Signal command, CMS publish, lane control | mTLS + JWT | 100 QPS/tenant | <200ms |
| Data | 30+ | Flow stats, OD, emissions, congestion index | JWT + API Key | 500 QPS/tenant | <500ms |
| Mobility | 25+ | Routing, transit, parking, charging | API Key (anon ok) | 2000 QPS | <200ms |
| Management | 20+ | Device reg, OTA, alerts | mTLS + RBAC | 50 QPS/tenant | <500ms |
| Open data | 15+ | Network, index, weather | API Key | 500 QPS | <300ms |

---

## 6. HD Map & Positioning System

### 6.1 HD Map Layers & Specs

| Layer | Content | Abs. accuracy | Rel. accuracy | Update | Data/km |
|-------|---------|---------------|---------------|--------|---------|
| Base road | Geometry, lanes, curvature, grade | <20cm | <10cm | Quarterly | 50–100 KB |
| Road facilities | Signs, signals, barriers | <20cm | <10cm | Monthly | 100–200 KB |
| Lane attributes | Type, turn restrictions, speed, bus lane | <20cm | <10cm | Monthly | 30–50 KB |
| Positioning features | Pole/building corner points | <15cm | <5cm | Quarterly | 200–500 KB |
| Real-time dynamic | Workzone, incident, weather, water | <50cm | <20cm | Min/event | 10–50 KB |
| Traffic info | Live conditions, congestion, events | — | — | Minute | 5–20 KB |
| POI/service | Charging, fuel, parking, toll | <50cm | <30cm | Weekly | 20–50 KB |

### 6.2 HD Positioning Technology Comparison

| Tech | Accuracy (95%) | Availability | Init | Coverage | Dependency | Cost |
|------|---------------|-------------|------|----------|-----------|------|
| **RTK** | 2–5cm | 95–98% | <10s | CORS network | 4G/5G + base | ~$14/mo |
| **PPP-RTK** | 5–10cm | 98–99.9% | 30s–2min | Wide/national | Sat correction | $14–70/mo |
| **NRTK** | 2–3cm | 95–99% | <5s | Province/city | CORS + private | CORS amortized |
| **PPP-AR** | 5–10cm | 90–95% | 10–30min | Global | Precise orbit/clock | $70–140/mo |
| **Visual SLAM** | 10–30cm | 80–95% | <1s (prior map) | Local | Camera + HD map | Compute cost |
| **LiDAR SLAM** | 5–10cm | 90–98% | <1s (prior map) | Local | LiDAR + HD map | High (LiDAR) |
| **UWB indoor** | 10–30cm | 95–99% | Instant | Indoor/tunnel | UWB anchors | $700–2.8k/anchor |
| **IMU** | Long-term drift | Short-term high | Instant | Global | High-end IMU | MEMS $0.1k / FOG $k |
| **Cellular (5G)** | 1–3m (R16) / <1m (R18) | 90–99% | <1s | Network | 5G base | Operator-provided |

### 6.3 Multi-Source Fusion Positioning

```
┌──────────────────────────────────────────────────────────────┐
│                     Multi-Source Fusion Engine                 │
│  ┌─────────┐ ┌─────────┐ ┌──────────┐ ┌────────┐ ┌────────┐ │
│  │GNSS/RTK │ │  IMU   │ │ LiDAR   │ │ Vision │ │ Wheel  │ │
│  └────┬────┘ └───┬─────┘ └────┬─────┘ └───┬────┘ └───┬────┘ │
│       ▼          ▼            ▼           ▼          ▼       │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  Factor Graph Optimization (GPS / IMU / LiDAR / Vision)│  │
│  │                        │                               │  │
│  │                        ▼                               │  │
│  │              GTSAM / g2o solver                        │  │
│  └───────────────────────┬────────────────────────────────┘  │
│                          ▼                                   │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  EKF / UKF online recursive estimate → 100–200 Hz      │  │
│  └───────────────────────┬────────────────────────────────┘  │
│                          ▼                                   │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  Output: 6DOF pose (x,y,z,roll,pitch,yaw) + covariance  │  │
│  │  Accuracy: horiz <5cm (RTK) / <30cm (no RTK); 100 Hz    │  │
│  └────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

### 6.4 CORS Reference-Station Network

| Parameter | Urban dense | Urban normal | Highway | Remote |
|----------|-----------|--------------|---------|--------|
| Station spacing | 15–25km | 25–40km | 30–50km | 50–80km |
| Coverage/station | ~500km² | ~1200km² | ~2000km² | ~5000km² |
| Build cost (w/ civil) | $21–35k | $17–25k | $14–21k | $21–42k (solar) |
| Annual O&M/station | $4–7k | $2.8–4.2k | $2.8–4.2k | $2.8–5.6k |
| Comms | Fiber + 4G backup | Fiber + 4G | 4G/5G + sat | Sat + 4G |
| Power | Grid + UPS | Grid + UPS | Grid + solar | Solar + battery |

---

## 7. Security Credential Management (SCMS/PKI)

### 7.1 SCMS Overall Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        SCMS Trust Domain                                  │
│  ┌──────────────────────────────────────────────┐                       │
│  │              SCMS Manager (policy)            │                       │
│  │   global policy / blacklist / anomaly detect  │                       │
│  └─────────────────────┬────────────────────────┘                       │
│         ┌──────────────┼──────────────┐                                 │
│         ▼              ▼              ▼                                 │
│  ┌────────────┐  ┌───────────┐  ┌───────────┐                          │
│  │  Root CA   │  │ Intermediate│  │ Pseudonym │                          │
│  │ (Elector)  │  │ CA (ICA)   │  │ CA (PCA)  │                          │
│  └─────┬──────┘  └─────┬─────┘  └─────┬─────┘                          │
│        ▼               ▼              ▼                                 │
│  ┌──────────────────────────────────────────────────────┐               │
│  │             Registration Authority (RA)               │               │
│  │   Enrollment RA            │  Pseudonym RA            │               │
│  └──────────┬──────────────────┼─────────────────────────┘               │
│             ▼                          ▼                                 │
│  ┌──────────────────────┐  ┌──────────────────────────┐                │
│  │  Long-term cert       │  │  Short-term pseudonym     │                │
│  │  · valid: 1 year      │  │  · valid: 1 week          │                │
│  │  · binds device ID    │  │  · no device binding      │                │
│  │  · comms encryption   │  │  · V2V/V2I msg signature  │                │
│  │  · OTA auth           │  │  · batch preload + rotate  │                │
│  └──────────────────────┘  └──────────────────────────┘                │
│  ┌──────────────────────────────────────────────────────┐               │
│  │  Revocation (CRL / OCSP) — periodic broadcast + realtime│              │
│  └──────────────────────────────────────────────────────┘               │
└─────────────────────────────────────────────────────────────────────────┘
```

### 7.2 Certificate Lifecycle Management

| Stage | Action | Time | Key flow |
|-------|--------|------|----------|
| 1. Factory provisioning | Write trust anchor (root CA pubkey) + unique device ID | Production | Secure element / HSM |
| 2. Enrollment request | Device submits ECR | <1 min | OBU → RA → ECA, verify ID |
| 3. Enrollment cert issue | ECA issues long-term cert | <10 s | Cert contains SSP |
| 4. Pseudonym request | Device requests batch pseudonyms | <5 s | OBU → PRA → PCA |
| 5. Pseudonym issue | PCA issues short-term anon certs | <1 min/batch | Batch 20, 1-week validity |
| 6. Use | Msg signing + encryption | Real-time | PC5 signing (ECDSA) |
| 7. Rotation | Renew before expiry | Auto | Request new batch 2 days ahead |
| 8. Revocation | Anomaly → revoke | <1 h | Network-wide CRL, OCSP realtime |
| 9. Expiry | Pseudonym auto-expires | On expiry | Falls back to spare cert |

### 7.3 Applied Cryptography in V2X

| Link | Algorithm | Use | Key length | Requirement |
|------|-----------|-----|-----------|-------------|
| V2X msg signature | ECDSA (FIPS 186) | PC5 msg signature | 256-bit | Mandatory |
| Comms encryption | AES (FIPS 197) | PC5/Uu symmetric | 128-bit | New systems must support |
| Cert-chain hash | SHA-2/SHA-3 (FIPS 180/202) | Cert fingerprint / digest | 256-bit | With ECDSA |
| Identity auth | ECDSA / (IBE opt.) | Device identity | 256-bit | Progressive |
| Low-power / high-speed | SNOW 3G / AES (3GPP) | Voice/video air interface | 128-bit | LTE/5G air |
| Key agreement | ECDH | OBU-RSU | — | Recommended |

> For China deployments, the SM series (SM2/SM3/SM4/SM9/ZUC) per national crypto law substitutes the above; for EU/US/NATO-aligned programs use FIPS 140-2/3-validated modules.

### 7.4 Secure-Element Specifications

| Parameter | OBU | RSU | MEC | Cloud HSM |
|----------|-----|-----|-----|-----------|
| Security grade | EAL4+ / FIPS 140-2 | EAL4+ / FIPS 140-2 | EAL5+ / FIPS 140-2 | EAL5+ / FIPS 140-2 |
| ECDSA speed | >500/s | >2000/s | >10000/s | >50000/s |
| AES throughput | >100 Mbps | >500 Mbps | >2 Gbps | >10 Gbps |
| Key storage | >50 pairs | >200 pairs | >1000 pairs | >10000 pairs |
| Tamper resistance | Active + self-destruct | Active + self-destruct | Cabinet-level | Room-level |
| Temp range | −40~+85°C | −40~+85°C | −20~+60°C | Room |
| Cert | FIPS 140-2 / CC EAL4+ | FIPS 140-2 / CC EAL4+ | FIPS 140-2 / CC EAL5+ | FIPS 140-2 / CC EAL5+ |

---

## 8. Interoperability & Standardization

### 8.1 Cross-Vendor Interoperability Framework

```
┌─────────────────────────────────────────────────────────────────────┐
│                       Interoperability Test Framework                  │
│  ┌──────────────────────────┐    ┌──────────────────────────┐      │
│  │    Conformance Testing    │    │   Interoperability Testing│      │
│  │  · protocol stack conform.│    │  · OBU-OBU (cross-brand) │      │
│  │  · message format verify  │    │  · OBU-RSU (cross-vendor)│      │
│  │  · security cert compat.  │    │  · RSU-MEC (cross-vendor)│      │
│  │  · perf. benchmark        │    │  · MEC-Cloud (cross-plat)│      │
│  └────────────┬─────────────┘    └────────────┬─────────────┘      │
│               └────────────────┬──────────────┘                    │
│                                ▼                                    │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                 Interop Certification System                  │  │
│  │  ETSI / C-ROADS │ USDOT / SAE │ 3rd-party labs (UTAC/DEKRA)  │ │
│  └──────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

### 8.2 Key Interoperability Interfaces

| Interface | Interop scope | Protocol / standard | Version | Key fields |
|----------|--------------|---------------------|---------|------------|
| OBU ↔ RSU (PC5) | Cross-brand V2V/V2I | ETSI EN 302 637 (CAM/DENM) / SAE J2735 | R15+ | BSM/CAM/RSI/RSM/MAP/SPAT |
| RSU ↔ MEC | Cross-vendor roadside compute | Proprietary + MQTT/HTTP2 | V1.0 | Perception/traffic event/control |
| MEC ↔ Regional cloud | Cross-vendor edge-cloud | OEM + gRPC/Protobuf | V1.0 | Fusion trajectory/junction state/signal plan |
| Regional ↔ City cloud | Cross-tier cloud | ISO 20546 / DATEX II (under alignment) | — | Regional stats/macro metrics/event |
| City ↔ Cross-domain cloud | Cross-city data share | C-RoadS / DATEX II | V0.5 | Cross-city route/OD/congestion |
| OBU ↔ TSP | OEM platform | NGTP / MOBI Alliance | V2.0 | Vehicle state/location/OTA |
| SCMS ↔ OBU/RSU | Cert request/distribute/revoke | IEEE 1609.2.1 + (C-)SCMS | V1.0 | Cert/CRL/CTL |

### 8.3 Cross-City VIC Interconnection

| Interop tier | Current | 2026–2027 target | 2028–2030 target |
|-------------|---------|------------------|------------------|
| Data-format unification | Each pilot city has its own | 16 pilot cities unify data dictionary | National unified transport data model |
| Message-set unification | SAE J2735 / ETSI (phase 1) | Unified enhanced message set V2.0 | National mandatory standard |
| Security interconnection | Independent SCMS per city | Federated SCMS between cities | National SCMS interoperability |
| OBU mutual recognition | Valid within city | Province-wide recognition | National recognition |
| Cloud-platform interconnection | Isolated systems | Regional cloud interconnect | National one-network cloud control |
| HD-map sharing | Each map provider independent | Common layer exchange | National one-map |
| Mobility-service interconnection | Independent apps | Metro-area MaaS interconnect | National one-stop mobility |

---

## 9. Performance Benchmarks & SLA Metrics

### 9.1 End-to-End Performance Baseline

| Scenario | Latency | Reliability | Availability | Throughput | Test standard |
|---------|---------|-------------|--------------|------------|---------------|
| V2V collision warning | <20ms (PC5) | 99.999% | 99.99% | 10 msg/s/veh | 3GPP TS 22.186 |
| V2I signal priority | <50ms (Uu) | 99.99% | 99.95% | 100 msg/s/jct | SAE J2735 |
| Roadside perception share | <100ms (E2E) | 99.9% | 99.95% | 50 Mbps/jct | OEM standard |
| Remote driving control | <20ms (RTT) | 99.9999% | 99.999% | 50 Mbps up + 10 Mbps down | 5G-V2X |
| Digital-twin sync | <500ms | 99.9% | 99.95% | 200 Mbps/region | OEM standard |
| OTA firmware | <30 min (100MB) | 99.999% (integrity) | 99.9% | 1000 concurrent/region | OEM/ISO |
| HD-map update | <5 min (dynamic) | 99.99% | 99.95% | 10 Mbps/veh | Map provider |
| Traffic-state compute | <60s (whole city) | 99.9% | 99.99% | 1M+ GPS pts/min | Industry practice |

### 9.2 Scalability Baseline

| Dimension | City cloud | Regional cloud | MEC edge | Note |
|----------|-----------|----------------|----------|------|
| Concurrent vehicles | 1M+ | 100k+ | 500+ | Online/served |
| Concurrent roadside devices | 100k+ | 10k+ | 100+ | RSU/MEC/signal |
| Message throughput | 10M msg/s | 1M msg/s | 100k msg/s | Peak |
| Video streams | 50k | 5k | 50 | 1080P H.265 |
| Storage | 10PB+ | 500TB+ | 10TB+ | Hot+cold |
| API QPS | 100k+ | 10k+ | 1000+ | Peak |
| GPU compute | 500+ PFlops (FP16) | 50+ PFlops | 50+ TOPS (INT8) | AI inference |
| Horizontal scaling | Linear (200+ nodes) | Linear (50+ nodes) | Limited (5 nodes) | — |

### 9.3 SLA Tiers & Penalty

| SLA tier | Availability | Annual downtime | Latency breach | System | Penalty |
|----------|-------------|-----------------|---------------|---------|---------|
| Tier 1 (critical) | 99.999% | <5.3 min | None allowed | V2X safety msg / signal control | 1h outage → 2× monthly fee |
| Tier 2 (important) | 99.99% | <52.6 min | <3/mo | Perception share / remote monitor | 1h outage → 1× monthly fee |
| Tier 3 (general) | 99.9% | <8.8 h | <10/mo | Mobility / info publish | 50% fee waiver |
| Tier 4 (tolerable) | 99.5% | <43.8 h | <50/mo | Analytics / reporting / mgmt | 25% fee waiver |

---

## 10. Deployment Models & Implementation Path

### 10.1 Deployment Mode Comparison

| Dimension | Greenfield | Brownfield | Hybrid |
|----------|-----------|------------|--------|
| Scenario | New district / smart highway / V2X zone | Old district retrofit / legacy upgrade | Partial city upgrade / phased |
| Difficulty | Medium (civil + coordination) | High (compat + cutover) | Medium-high |
| Cycle | 12–24 mo (100 km) | 18–36 mo (incl. transition) | 18–30 mo |
| Cost per km | Greenfield baseline | Save 30–50% (reuse) | Save 20–30% |
| Integration complexity | Low (new) | High (legacy compat) | Medium |
| Service interruption | None | Large (phased cutover) | Medium |
| Strategy | Integrated plan, build once | Zoned phased, old/new parallel | Backbone first, edges reuse |

### 10.2 Highway Deployment Plan

```
                Smart-Highway Deployment Cross-Section

     Roadside perception layer (one set per 300–600m)
   ┌─────────────────────────────────────────────────────────┐
   │  [camera]  [mmWave radar]  [MEC+RSU]  [env sensor]       │
   │   gantry/    gantry/         cabinet       visibility/    │
   │   pole       pole            (power)      road state      │
   └─────────────────────────────────────────────────────────┘
                              │
                              ▼
   ┌─────────────────────────────────────────────────────────┐
   │   Backbone comms (access point every 2–5 km)             │
   │   Fiber ring + 5G base (every 500m–1km) + edge DC (10–20km)│
   └─────────────────────────────────────────────────────────┘
                              │
                              ▼
   ┌─────────────────────────────────────────────────────────┐
   │   Cloud-control (regional / city / province)             │
   │   Holistic perception / active control / emergency /      │
   │   mobility service / autonomous driving                   │
   └─────────────────────────────────────────────────────────┘
```

**Phased highway implementation (per 100 km)**:

| Phase | Time | Build | Capability | Investment (USD) |
|-------|------|-------|-----------|------------------|
| Phase 1: Full perception | Yr 1 | Cameras/radar/RSU + fiber + MEC | Segment perception, incident detection, V2I warning | $11–17M |
| Phase 2: Cloud-control live | Yr 1–2 | Edge/regional cloud + data platform + signal link | Active control, dynamic speed, lane mgmt | $4–7M |
| Phase 3: Services online | Yr 2–3 | City cloud + mobility app + C-V2X services | V2X services, travel info | $2.8–4.2M |
| Phase 4: AV support | Yr 3–5 | L4 C-V2X enhancement + HD-map dynamic + remote drive | L4 AV, platooning | $4–7M |
| **Total** | 5 yr | — | **Full smart highway** | **$22–35M** |

### 10.3 Urban Phased Implementation

| Phase | Scope | Junctions | Build | Key deliverable |
|-------|-------|-----------|-------|-----------------|
| Phase 1: Flagship zone | 5–10 km² | 20–50 | Holistic junctions + edge + V2X RSU | Demo operation |
| Phase 2: Area coverage | 50–100 km² | 200–500 | Regional cloud + signal coordination + transit priority | Regional optimization |
| Phase 3: Citywide | Key areas | 1000–3000 | City cloud + MaaS + AV support | City intelligent-mobility platform |
| Phase 4: Metro linkage | Cross-city | — | Cross-domain cloud interconnect + integrated mobility | Metro coordinated control |

---

## 11. Whole-Lifecycle Cost Model (CAPEX/OPEX/TCO)

### 11.1 CAPEX Breakdown (per 100 km smart highway, USD)

| Category | Item | Qty | Unit (USD) | Subtotal (USD) | Share |
|---------|------|-----|-----------|----------------|------|
| Roadside perception | 4K camera | 600 | $1.7k | $1.0M | 4.8% |
| | mmWave radar | 300 | $3.5k | $1.05M | 5.0% |
| | LiDAR | 50 | $14k | $0.7M | 3.3% |
| | Env sensor | 100 | $4.2k | $0.42M | 2.0% |
| Compute & comms | MEC | 200 | $14k | $2.8M | 13.3% |
| | RSU | 250 | $7k | $1.75M | 8.3% |
| | 5G micro base | 100 | $11k | $1.1M | 5.3% |
| Network infra | Fiber (w/ conduit) | 100km | $42k/km | $4.2M | 20.0% |
| | OTN/PTN | 20 | $21k | $0.42M | 2.0% |
| | Switch/router | 50 | $2.8k | $0.14M | 0.7% |
| Cloud platform | Edge cloud cluster | 10 | $0.14M | $1.4M | 6.7% |
| | Regional cloud | 1 | $1.1M | $1.1M | 5.3% |
| | City cloud share | 0.2 | $2.8M | $0.56M | 2.7% |
| Civil works | Poles & base | 500 | $2.8k | $1.4M | 6.7% |
| | Cabinets & power | 200 | $7k | $1.4M | 6.7% |
| | Conduit/tray | 100km | $7k/km | $0.7M | 3.3% |
| Software | Cloud-control sw | 1 | $0.42M | $0.42M | 2.0% |
| | Digital twin | 1 | $0.28M | $0.28M | 1.3% |
| | AI platform/algo | 1 | $0.21M | $0.21M | 1.0% |
| Security | SCMS/PKI | 1 | $0.21M | $0.21M | 1.0% |
| | Network security | 1 | $0.14M | $0.14M | 0.7% |
| | Crypto infra | 1 | $0.11M | $0.11M | 0.5% |
| Design & integration | Design/consult | 1 | $0.42M | $0.42M | 2.0% |
| | System integration | 1 | $0.7M | $0.7M | 3.3% |
| **Total** | | | | **~$21M** | 100% |

### 11.2 Annual OPEX Estimate (USD)

| Category | Item | Annual (USD) | % of CAPEX |
|---------|------|--------------|-----------|
| Equipment maint. | Camera/radar/sensor replace (5%/yr) | $0.28M | 1.3% |
| | MEC/RSU/network repair (3%/yr) | $0.25M | 1.2% |
| Electricity | Roadside (2000 pts × 1kW × $0.11/kWh × 8760h) | $1.97M | 9.3% |
| | Room/cloud power | $0.28M | 1.3% |
| Comms | Fiber/5G lease | $0.42M | 2.0% |
| | IoT SIM traffic | $0.07M | 0.3% |
| Labor | O&M team (15 × $35k/yr) | $0.53M | 2.5% |
| | Security ops (5 × $42k/yr) | $0.21M | 1.0% |
| Software lic. | Cloud/DB/middleware | $0.28M | 1.3% |
| | Security sw / threat intel | $0.11M | 0.5% |
| Other | Insurance/spares/training | $0.14M | 0.7% |
| **Total** | | **~$4.55M** | **21.6%** |

### 11.3 10-Year TCO

| Year | CAPEX (USD) | OPEX (USD) | Cumulative (USD) | Note |
|------|-------------|------------|------------------|------|
| Y0 | $14M | 0 | $14M | Phase 1, 70% |
| Y1 | $7M | $2.1M | $23.1M | Phase 2, 30% + O&M |
| Y2 | 0 | $4.2M | $27.3M | Full O&M |
| Y3 | 0 | $4.5M | $31.8M | +3% inflation |
| Y4 | $4.2M | $4.6M | $40.6M | Equipment refresh |
| Y5 | 0 | $4.8M | $45.4M | |
| Y6 | $2.8M | $4.9M | $53.1M | Mid-life upgrade |
| Y7 | 0 | $5.0M | $58.1M | |
| Y8 | 0 | $5.2M | $63.3M | |
| Y9 | $1.4M | $5.3M | $70M | SW platform upgrade |
| Y10 | 0 | $5.5M | $75.5M | |
| **10-yr TCO** | **$29.4M** | **$46.1M** | **$75.5M** | CAPEX:OPEX ≈ 1:1.57 |

### 11.4 Single-Intersection TCO

| Item | Cost (USD) | Note |
|------|-----------|------|
| CAPEX | ~$120k | See §2.2 |
| Annual OPEX | $11k–17k | Power/maint/comms |
| 5-yr TCO | $175k–205k | |
| 10-yr TCO | $230k–290k | Incl. Y5 refresh |

---

## 12. Global Deployment Comparison (China vs US vs EU vs Japan)

### 12.1 Technology-Route Comparison

| Dimension | China | United States | Europe | Japan |
|----------|-------|---------------|--------|-------|
| Comms | C-V2X (LTE-V2X + NR-V2X) | DSRC → C-V2X transition | ITS-G5 (802.11p) + C-V2X hybrid | ITS Connect (760MHz) + C-V2X pilot |
| Spectrum | 5905–5925 MHz (20MHz) | 5895–5925 MHz (30MHz, FCC 2024 reallocation) | 5875–5925 MHz (50MHz, shared) | 755.5–764.5 MHz + 5.9GHz pilot |
| Leading arch. | VIC integrated (public top-down) | Vehicle-intelligent dominant | Hybrid cooperative ITS (C-ITS Platform) | Society 5.0 (industry-gov-academia) |
| Roadside deploy | Large-scale (national, 7→16 pilot cities) | Limited (on-demand, state-led) | Medium (C-Roads, 18 countries) | Medium (SIP-adus, highway flagships) |
| Cloud-control | City/regional/edge 3-tier | Mostly private platforms | C-ITS Central Station | Regional traffic mgmt center |
| HD map | State-controlled, 14 Class-A qualified | Commercial open (HERE/TomTom/Google) | Commercial + GDPR constraints | Commercial (DMP alliance) |
| Security | SM series + tier protection | IEEE 1609.2 SCMS | C-ITS CMS | ITS Connect security |
| Policy push | ★★★★★ (national strategy) | ★★★ (industry-driven) | ★★★★ (EU coordination) | ★★★★ (national projects) |

### 12.2 Investment-Scale Comparison

| Metric | China (2024–2027) | US (IIJA 2022–2026) | EU (2021–2027) | Japan (2022–2027) |
|--------|-------------------|---------------------|-----------------|-------------------|
| Public investment | ~$70B (V2X + smart mobility) | ~$200B (incl. roads/charging) | ~€30B (C-ITS + smart mobility) | ~$3.4B |
| Roadside RSU deployed | Target 50k+ (16 cities) | ~5k | ~15k (C-Roads) | ~3k |
| Intersections upgraded | Target 10k+ (first batch) | ~2k | ~5k | ~1.5k |
| L4 AV test mileage | 300M+ km | 150M+ km (Waymo/Cruise) | 50M+ km | 20M+ km |
| V2X vehicles deployed | ~5M (factory + aftermarket) | ~0.5M | ~0.3M | ~0.1M |

### 12.3 Regional Characteristics Summary

**China**: largest roadside infrastructure rollout; complete public top-down planning (investment + sector departments jointly); unified standards and control (SAE J2735/ETSI-aligned message set, national crypto, unified spectrum); highest 5G base density globally, underpinning C-V2X Uu.

**United States**: leading vehicle-intelligent tech (Waymo/Tesla/Cruise); market-driven, diverse competing tech routes; federal structure means state-by-state decisions, hard to unify; spectrum uncertainty from DSRC↔C-V2X transition.

**Europe**: the 18-country C-Roads Platform is a model for cross-border coordination; GDPR's high privacy bar affects data sharing; hybrid comms (ITS-G5 + C-V2X); strong emphasis on green and sustainable transport.

**Japan**: unique 760MHz ITS Connect (not globally compatible); SIP-adus national AV/C-V2X research program; aging-society-driven AV demand; greater challenge aligning with global standards.

---

## 13. Technology Evolution Roadmap (5G-V2X → 5G-A → 6G)

### 13.1 Three-Stage Evolution

```
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│  2024-2026    │     │  2027-2029    │     │  2030+         │
│  5G-V2X       │ ──► │  5G-Advanced  │ ──► │  6G-V2X        │
│  (Rel.16/17)  │     │  (Rel.18/19)  │     │  (IMT-2030)    │
└───────────────┘     └───────────────┘     └───────────────┘
        │                     │                     │
        ▼                     ▼                     ▼
 ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
 │ · NR-V2X PC5│      │ · 5G-A V2X  │      │ · THz comms │
 │ · 100Mbps   │      │ · sensing+comm│     │ · ISAC       │
 │ · <10ms     │      │ · AI-native  │     │ · 0.1ms      │
 │ · 99.999%   │      │ · 1Gbps+     │     │ · 99.99999%  │
 │ · basic pos.│      │ · cm-level pos│     │ · holographic │
 └─────────────┘      └─────────────┘      └─────────────┘
```

### 13.2 Capability Evolution

| Capability | 5G-V2X (2024–26) | 5G-A V2X (2027–29) | 6G-V2X (2030+) |
|-----------|------------------|---------------------|----------------|
| Peak rate | PC5 100Mbps, Uu 1–2Gbps | PC5 500Mbps, Uu 5–10Gbps | PC5 1–10Gbps, Uu 100Gbps+ |
| Latency | 3–10ms (URLLC) | 0.5–3ms | 0.1ms |
| Reliability | 99.999% | 99.9999% | 99.99999% |
| Positioning | 3–10m (outdoor) | <1m outdoor / <3m indoor | <1cm (ISAC) |
| Sensing | Comms/sensing separate | ISAC phase 1 | Full ISAC |
| AI integration | Edge inference | AI-native air interface | Fully autonomous AI network |
| Connection density | 1M/km² | 10M/km² | 100M/km² |
| Spectrum | Sub-6 + mmWave | + cmWave | + THz |
| Energy efficiency | Baseline | 10× | 100× |
| Mobility | 500 km/h | 1000 km/h | >1000 km/h |
| New capability | Basic V2X msgs | Cooperative sense/control | Holographic network / digital twin / remote holographic drive |

### 13.3 Key Breakthroughs (2027–2029, 5G-A)

| Tech | Note | Benefit to VIC | Standard |
|------|------|----------------|---------|
| Sidelink enhancement (NR SL) | Efficient PC5, multi-hop relay | Vehicle sensing share up to 500Mbps | 3GPP Rel.18 |
| ISAC phase 1 | Base-station sensing reuse | 5G base detects road objects, less dedicated sensors | 3GPP Rel.19 study |
| AI/ML for NR air interface | AI channel est., beam mgmt, positioning | Reliability ↑, cm-level positioning | 3GPP Rel.18/19 |
| NTN integration | Satellite-direct V2X (LEO) | Full coverage (remote highway/mountain) | 3GPP Rel.17/18 |
| MEC enhancement | Federated learning, edge co-inference | MEC cooperation, joint training | ETSI MEC R3 |
| RedCap/eRedCap V2X | Lightweight 5G module | Low-cost OBU proliferation | 3GPP Rel.17/18 |

### 13.4 Key Breakthroughs (2030+, 6G)

| Tech | Expected capability | Transformative impact |
|------|---------------------|----------------------|
| THz (100GHz–3THz) | Tbps transmission | On-vehicle holographic comms, real-time 8K/16K video share |
| Full ISAC | Base = radar + comms (hi-res imaging) | No extra roadside radar; base is the sensor |
| AI-native 6G | Self-optimize/heal/configure | Zero-touch transport private network |
| Holographic digital twin | Physical/digital ns-level sync | Citywide ms-level twin traffic rehearsal |
| Quantum-safe comms | PQC + QKD | Absolutely secure VIC comms |
| Semantic comms | Transmit "meaning" not bits | 1/100 bandwidth for full V2X |
| Cellular V2X 6G | 0.1ms + 99.99999% | L5 AV infrastructure complete |

---

## 14. Standards & Compliance Matrix

### 14.1 Communications Standards

| Standard | Name | Org | Version | Object | Requirement |
|---------|------|-----|---------|--------|-------------|
| 3GPP TS 22.186 | Enhanced V2X scenarios | 3GPP | Rel.17 | OBU/RSU/MEC | Mandatory |
| 3GPP TS 23.287 | 5G V2X architecture enh. | 3GPP | Rel.17 | 5GC/MEC | Mandatory |
| 3GPP TS 38.300 | NR overview (incl. SL) | 3GPP | Rel.17 | RSU/OBU | Mandatory |
| IEEE 802.11p | WAVE/DSRC | IEEE | 2010 | RSU/OBU (compat) | Reference |
| IEEE 1609.2 | V2X security services | IEEE | 2016 | SCMS/OBU | Reference |
| ETSI EN 302 637 | CAM/DENM (cooperative awareness/event) | ETSI | v2.0+ | OBU/RSU | Mandatory (EU) |
| SAE J2735 | V2X message set (BSM/MAP/SPAT/RSI/RSM) | SAE | 2020+ | OBU/RSU/MEC | Mandatory (US/intl) |

### 14.2 Message & Data Standards

| Standard | Name | Org | Version | Object | Requirement |
|---------|------|-----|---------|--------|-------------|
| SAE J2735 | V2X message set (phase 1) | SAE | 2020 | OBU/RSU/MEC | Mandatory |
| SAE J2945 | V2X msg tx requirements (phase 2) | SAE | 2016+ | OBU/RSU/MEC | Recommended |
| ISO 20546 | Traffic data exchange (DATEX II aligned) | ISO | — | Cloud/platform | Recommended |
| ASTM E2936 / EN 15450 | Traffic detector (microwave/video) | ASTM/EN | — | Roadside sensor | Mandatory (procurement) |

### 14.3 Platform & System Standards

| Standard | Name | Org | Version | Object | Requirement |
|---------|------|-----|---------|--------|-------------|
| ETSI MEC / C-ITS | Cloud-control overall tech. req. | ETSI | evolving | Cloud-control | Mandatory (EU, post-pub) |
| ISO 20900 / 14813 | ITS reference architecture | ISO | — | Cloud-control | Recommended |
| C-Roads spec | RSU–center data interface | C-Roads | 2020+ | RSU/cloud | Recommended |
| NIST SP 800-53 / ISO 27001 | Info-security baseline | NIST/ISO | — | Whole system | Mandatory |

### 14.4 Security Standards

| Standard | Name | Org | Version | Object | Requirement |
|---------|------|-----|---------|--------|-------------|
| IEEE 1609.2 | V2X security services | IEEE | 2016 | SCMS/OBU | Reference |
| ETSI TS 102 941 | C-ITS security (enrolment/authorization) | ETSI | v2.0+ | SCMS | Mandatory (EU) |
| ISO/SAE 21434 | Road-vehicle cybersecurity engineering | ISO | 2021 | Vehicle/OBU | Recommended (export required) |
| UNECE R155 | CSMS / cybersecurity regulation | UNECE | 2021 | Vehicle | Mandatory (type approval) |
| FIPS 140-2/3 | Cryptographic module validation | NIST | — | HSM/CA | Mandatory (US/gov) |
| NIST SP 800-53 | Security & privacy controls | NIST | Rev.5 | Whole system | Mandatory (US/gov) |

### 14.5 Positioning & Map Standards

| Standard | Name | Org | Version | Object | Requirement |
|---------|------|-----|---------|--------|-------------|
| ISO 20546 / OpenDRIVE | HD-map data model & exchange | ISO/ASAM | — | HD map | Mandatory (procurement) |
| ISO 19100 series | Geographic data quality/model | ISO | — | Map exchange | Mandatory |
| NMEA / RTCM | GNSS RTK differential messages | NMEA/RTCM | — | CORS/RTK | Mandatory |

### 14.6 ITU International Standards

| Standard | Name | Org | Scope |
|---------|------|-----|-------|
| ITU-T Y.4461 | V2X comms framework | ITU-T | Global V2X arch. reference |
| ITU-T Y.4469 | Autonomous-driving data-sharing framework | ITU-T | Data sharing |
| ITU-T Y.4470 | MEC in intelligent transport | ITU-T | MEC application |
| ITU-T Y.4480 | Digital twin in ITS | ITU-T | Digital twin |
| ITU-R M.2443 | ITS evolution in IMT | ITU-R | ITS spectrum & network evolution |

---

## 15. Appendix: Key Terminology

| Term | Full name | Description |
|------|-----------|-------------|
| BSM | Basic Safety Message | Core V2V message: position/speed/heading |
| C-ITS | Cooperative Intelligent Transport Systems | EU term for vehicle-infrastructure cooperation |
| C-V2X | Cellular Vehicle-to-Everything | 3GPP-based V2X communication |
| CAM | Cooperative Awareness Message | ETSI V2X perception-share message |
| CAPEX | Capital Expenditure | One-time build investment |
| CORS | Continuously Operating Reference Stations | GNSS differential ground-station network |
| CRL | Certificate Revocation List | List of revoked certificates |
| DENM | Decentralized Environmental Notification Message | ETSI V2X event message |
| DSRC | Dedicated Short Range Communications | 802.11p-based V2X (US legacy) |
| ECA | Enrollment Certificate Authority | Issues long-term certs in SCMS |
| EKF | Extended Kalman Filter | Nonlinear state estimation |
| gNB | next Generation Node B | 5G base station |
| HSM | Hardware Security Module | Key storage / crypto hardware |
| ICA | Intermediate Certificate Authority | Middle of trust chain |
| IMU | Inertial Measurement Unit | Accelerometer + gyroscope |
| ISAC | Integrated Sensing and Communication | Comms+sensing fusion (6G key) |
| ITS-G5 | Intelligent Transport Systems – G5 | EU 802.11p V2X brand |
| MaaS | Mobility as a Service | One-stop multi-modal mobility platform |
| MAP | Map Data Message | V2X intersection/segment topology |
| MEC | Multi-access Edge Computing | Roadside-adjacent compute |
| MOTA | Multiple Object Tracking Accuracy | Tracking performance metric |
| NR-V2X | New Radio V2X | 5G NR V2X Sidelink |
| NTN | Non-Terrestrial Network | Satellite/HAPS comms |
| OBU | On-Board Unit | Vehicle V2X terminal |
| OPEX | Operational Expenditure | Annual operation cost |
| OTN/PTN | Optical/Packet Transport Network | Fiber backbone transport |
| PCA | Pseudonym Certificate Authority | Issues anonymous certs in SCMS |
| PC5 | Proximity Communication 5 | 3GPP direct (Sidelink) interface |
| PPP-RTK | Precise Point Positioning – RTK | PPP wide-area + RTK precision |
| RA | Registration Authority | Verifies device ID, authorizes cert |
| RSI | Road Side Information | V2X roadside event/traffic message |
| RSM | Roadside Safety/Perception Message | V2X fused-perception share |
| RSU | Road Side Unit | Roadside V2X device |
| SCMS | Security Credential Management System | Complete V2X cert management |
| SLA | Service Level Agreement | Availability commitment |
| SPAT | Signal Phase And Timing | V2X signal-state message |
| SSP | Service Specific Permissions | Permitted V2X services in cert |
| TARA | Threat Analysis and Risk Assessment | ISO 21434 security method |
| TCO | Total Cost of Ownership | Whole-lifecycle cost |
| UPF | User Plane Function | 5G core data-forwarding node (local breakout) |
| URLLC | Ultra-Reliable Low Latency Communication | One of 5G three scenarios |
| Uu | User Equipment – Network Interface | Cellular air interface |
| V2I / V2N / V2P / V2V / V2X | Vehicle-to-Infra/Network/Pedestrian/Vehicle/Everything | V2X communication modes |

---

> **Authoring note**: This whitepaper is based on the *Intelligent Vehicle Innovation Development Strategy*, the *Connected-Vehicle Industry Development Plan*, and the CAICV Vehicle-Infrastructure-Cloud series. Technical parameters reference 3GPP Rel.16/17/18, SAE J2735, ETSI EN 302 637, IEEE 1609.2, ISO/SAE 21434, UNECE R155, and ITU-T Y.4461/4469/4470/4480. All data as of June 2026, for professional transport-digitalization planning and technical decision reference.

> **References**: 3GPP TS 22.186 / 23.287 / 38.300 · SAE J2735 / J2945 · ETSI EN 302 637 / TS 102 941 · ISO/SAE 21434:2021 · IEEE 1609.2-2016 · ISO 20546 / OpenDRIVE · NIST SP 800-53 / FIPS 140-2/3 · UNECE R155 · ITU-T Y.4461/4469/4470/4480

---

**Document version**: V1.0.0
**Last updated**: 2026-07-05
**Scope**: Intelligent-transport planning & design / V2X technology selection / smart-highway project proposals / city-scale VIC pilot applications
