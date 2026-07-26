# Transport AI Applications Framework

> This document systematically sets out the in-depth application framework for artificial intelligence in the transport sector, covering the full technology stack, the deep architecture of 25 AI scenarios, the model-training pipeline, edge–cloud collaborative decision-making, MLOps, transport-AI-specific challenges, an evaluation system, measured case-study performance, technology-maturity evolution, and AI ethics governance. It is an authoritative technical reference for transport-AI project planning, selection, and deployment.

---

## Table of Contents

1. [Seven-Layer Transport AI Technology Stack](#i-seven-layer-transport-ai-technology-stack)
2. [Deep Architecture of 25 AI Scenarios](#ii-deep-architecture-of-25-ai-scenarios)
3. [Full Transport AI Model-Training Lifecycle](#iii-full-transport-ai-model-training-lifecycle)
4. [Edge-AI and Cloud-AI Decision Framework](#iv-edge-ai-and-cloud-ai-decision-framework)
5. [Transport-AI-Specific Challenges and Engineering Responses](#v-transport-ai-specific-challenges-and-engineering-responses)
6. [AI Evaluation System and Benchmark Data](#vi-ai-evaluation-system-and-benchmark-data)
7. [Transport MLOps System](#vii-transport-mlops-system)
8. [High-Value Cases and Measured Performance](#viii-high-value-cases-and-measured-performance)
9. [Technology-Maturity Roadmap 2024–2030](#ix-technology-maturity-roadmap-2024-2030)
10. [Transport AI Ethics and Safety Governance](#x-transport-ai-ethics-and-safety-governance)
11. [Transport AI Investment-Decision Framework](#xi-transport-ai-investment-decision-framework)

---

## I. Seven-Layer Transport AI Technology Stack

### 1.1 Seven-Layer Stack Diagram

```
┌──────────────────────────────────────────────────────────────────────┐
│ L7 Application & Solution Layer                                           │
│    AI Signal Control | Incident Detection | Flow Forecast | PHM O&M    │
│    Autonomous Driving | Foundation Models                                  │
├──────────────────────────────────────────────────────────────────────┤
│ L6 Agent & Orchestration Layer                                             │
│    Multi-Agent Coordination (MARL) | Human-in-the-Loop | RAG | Agent WF  │
├──────────────────────────────────────────────────────────────────────┤
│ L5 Model & Algorithm Layer                                                 │
│    CV Foundation Models | LLM | Temporal Transformer | GNN | RL | Fusion  │
├──────────────────────────────────────────────────────────────────────┤
│ L4 Framework & Tool Layer                                                  │
│    PyTorch | TensorFlow | JAX | Model Compression / Quantization          │
├──────────────────────────────────────────────────────────────────────┤
│ L3 Data & Feature Layer                                                    │
│    Data Lake | Feature Engineering | Labeling | Pipelines | Quality | FL   │
├──────────────────────────────────────────────────────────────────────┤
│ L2 Compute & Silicon Layer                                                 │
│    GPU Clusters (NVIDIA) | NPU / Edge AI Chips | Cloud Inference Cards     │
├──────────────────────────────────────────────────────────────────────┤
│ L1 Sensing & Connectivity Layer                                            │
│    Cameras | mmWave Radar | LiDAR | IoT Sensors | V2X | GNSS Positioning  │
└──────────────────────────────────────────────────────────────────────┘
```

### 1.2 Core AI Algorithm Classification and Capability Matrix

| AI Category | Core Algorithms | Transport Scenarios | Maturity (1–5) | Sourcing | Key Challenge |
|-----------|-----------------|:-------------------:|:--------------:|---------|--------------|
| **Computer Vision (CV)** | YOLOv8–v10, DETR, SAM2, ViT, BEVFormer, 3D GS | 12+ | 5 | Open (OpenMMLab / robust open CV) | Adverse weather / night / occlusion |
| **NLP (LLM)** | GPT, Claude, Llama, Gemini, Mistral, Qwen | 6+ | 4 | Open + commercial | Hallucination / domain fit / latency |
| **Time-Series Forecast** | Transformer, Informer, PatchTST, TimesNet, TiDE | 5+ | 5 | Mostly open | Long-horizon accuracy / incidents |
| **GNN** | GCN, GAT, GraphSAGE, STGNN, DCRNN | 4+ | 4 | Open (DGL / PyG) | Large-graph training efficiency |
| **RL** | PPO, SAC, MADDPG, QMIX, MAPPO | 3+ | 3 | Open + in-house | Safety constraints / Sim2Real gap |
| **Multimodal Fusion** | CLIP, ALBEF, multimodal Transformer, VideoLLM | 5+ | 3 | Open + commercial | Spatio-temporal alignment / missing modalities |
| **Knowledge Graph** | TransE, GraphRAG, Neo4j, LLM+KG | 4+ | 3 | Commercial + open | Auto-construction / freshness |
| **OR Optimization** | OR-Tools, Gurobi, heuristics, meta-heuristics | 5+ | 5 | Open + commercial | Large combinatorial solve speed |
| **Anomaly Detection** | IsolationForest, LSTM-AE, DeepSVDD, TranAD | 4+ | 4 | Mostly open | Unknown anomaly types |
| **Generative AI** | Diffusion, GAN, VAE, video gen | 3+ | 2 | Emerging | Physical plausibility of scenes |

### 1.3 AI Compute Requirement Ladder by Modality

| Scenario | Training Compute | Inference Compute | Recommended Silicon | Deploy | Max Latency |
|----------|:---------------:|:----------------:|---------------------|-------|:-----------:|
| AI signal optimization | Med (1–3 GPU-week) | Low (edge NPU) | NVIDIA Jetson / Intel NPU | Edge | <50 ms |
| AI incident detection (video) | High (4–10 GPU-wk) | Med (edge GPU) | NVIDIA Jetson Orin | Edge | <100 ms |
| Citywide flow forecast | Med (2–5 GPU-wk) | Low (CPU ok) | General GPU / CPU | Cloud | <2 s |
| AV BEV perception | Very high (1000+ GPU-wk) | Very high (onboard) | NVIDIA Orin / DRIVE | Onboard | <30 ms |
| Transport LLM (100B+) | Very high (3000+ GPU-wk) | High (multi-GPU cloud) | H100 × 8+ | Cloud | <3 s |
| Rail PHM | Low (<1 GPU-wk) | Very low (MCU) | Edge MCU / CPU | Edge | <100 ms |
| Digital-twin render | N/A | Very high (GPU) | NVIDIA RTX A6000 / L40S | Cloud + client | <33 ms |
| AAM UTM trajectory | Med (2–4 GPU-wk) | Low (CPU ok) | General GPU | Cloud + edge | <100 ms |
| Toll audit (offline) | Low (<1 GPU-wk) | Very low (batch) | CPU cluster | Cloud | N/A (offline) |
| Bridge SHM anomaly | Low (CPU-wk) | Low (edge CPU) | Edge gateway CPU | Edge | <500 ms |

---

## II. Deep Architecture of 25 AI Scenarios

### Scenario Index

| # | Scenario | Mode | Core AI Tech | TRL | Investment / unit | Typical ROI |
|---|----------|------|--------------|:---:|:-----------------:|:-----------:|
| 1 | AI signal optimization | Urban road | MARL + GNN + MPC | 8 | $7k–$70k | 1.5–3 yr |
| 2 | AI incident detection | Urban / highway | YOLO + MTT + multimodal | 8 | $1.4k–$7k / roadside | 1–2 yr |
| 3 | AI traffic forecast | All modes | Transformer + GNN | 7 | $0.7M–$7M / city | Indirect |
| 4 | AI autonomous driving | Road | BEV + Transformer + E2E | 6 | $B (full stack) | 8–15 yr |
| 5 | AI maintenance decision | Highway / road | CV + PHM + optim. | 7 | $1.4M–$7M / 100km | 2–4 yr |
| 6 | AI safety-risk forecast | All modes | XGBoost + causal inference | 7 | $0.7M–$4.2M / city | 1–3 yr |
| 7 | AI dynamic pricing | Highway / parking | RL + game theory | 6 | $1.4M–$7M | 1–3 yr |
| 8 | AI smart port | Port | CV + OR + MIP | 8 | $10M–$100M / terminal | 3–7 yr |
| 9 | AI airport A-CDM | Aviation | Time-series + solver | 8 | $14M–$70M | 2–4 yr |
| 10 | AI rail PHM | Rail / metro | Temporal anomaly + transfer | 8 | $7M–$28M / line | 2–4 yr |
| 11 | AI multimodal dispatch | Logistics | Combinatorial + RL | 6 | $2.8M–$14M | 2–4 yr |
| 12 | AI low-altitude UTM | AAM | Conflict detect + trajectory | 5 | $7M–$70M | 5–10 yr |
| 13 | Transport LLM | All modes | LLM + RAG + KG + Agent | 5 | $1.4M–$14M | 3–5 yr |
| 14 | AI carbon monitoring | All modes | Emission model + fusion | 6 | $0.7M–$7M | Indirect |
| 15 | AI smart scheduling | Bus | OR + demand forecast | 8 | $0.7M–$4.2M | 1–2 yr |
| 16 | AI disaster warning | Highway / rail | Weather + RS + graph | 6 | $2.8M–$28M | Social benefit |
| 17 | AI smart assistant | All modes | LLM + RAG + ASR + TTS | 7 | $0.4M–$2.8M | <1 yr |
| 18 | AI enforcement evidence | Urban / highway | CV + MTT + ReID | 9 | $1.4M–$7M | 1–2 yr |
| 19 | AI planning & design | Urban / highway | Multi-agent sim + gen-AI | 5 | $1.4M–$14M | Indirect |
| 20 | AI bridge/tunnel SHM | Bridges / tunnels | Acoustic + vibration + DL | 7 | $1.4M–$14M / structure | 3–5 yr |
| 21 | AI econometric forecast | Macro | Econometrics + ML | 6 | $0.7M–$2.8M | Indirect |
| 22 | AI driver training | Training | VR/AR + behavior analysis | 5 | $0.4M–$1.4M | 1–2 yr |
| 23 | AI age-friendly mobility | Bus / MaaS | LLM + voice + rec. | 5 | $0.7M–$2.8M | Social benefit |
| 24 | AI cost estimation review | Construction | NLP + KG + forecast | 6 | $1.4M–$7M | 1–3 yr |
| 25 | AI public-sentiment mgmt | All modes | NLP + sentiment | 7 | $0.4M–$2.1M | <1 yr |

### Scenario 1: AI Traffic-Signal Optimization (Deep Technical Plan)

**Architecture (three-stage evolution):**

**Stage I — Offline learning + online inference (current mainstream)**
- Data: ≥6 months of intersection detector + ANPR + floating-car data (5-min granularity)
- Training: cloud cluster (A100 × 8), offline RL training in SUMO / VISSIM simulation
- Policy network: PPO / SAC; state = queue length | saturation | phase duration | time-of-day; action = [phase selection + duration adjustment]
- Inference: edge industrial PC, per-cycle (<500 ms) inference → phase suggestion
- Safety layer: hard constraints (min-green ≥ 7 s, max-cycle ≤ 180 s) + conflicting-phase interlock + heartbeat-timeout fallback to fixed timing
- Deployment condition: intersection sensing coverage >70%, signal connectivity >80%

**Stage II — Multi-agent regional coordination (current frontier)**
- Coordination: QMIX / MAPPO CTDE (centralized training, decentralized execution)
- Intersection as graph node, GAT extracts spatial dependency, neighbors share latent state
- Sub-area auto-partition: spectral clustering on flow correlation and travel time
- Coordination layer: cloud pushes coordination params every 15 min (green-wave band / offset / unified cycle)

**Stage III — AI-native citywide control (2027+)**
- Transport LLM + RL hybrid: LLM understands high-level semantics ("stadium let-out") → coarse strategy; RL refines execution
- Cross-modal coordination: signal + VMS + navigation app + bus dispatch unified optimization
- Online continual learning: production data feeds back in real time, weekly incremental model update

**Performance data (representative city deployment, e.g., Singapore / Tokyo):**
- 150+ intersections: AM-peak speed +24%, delay −25%, stops −35%
- ~6,800 t CO2 abated per year
- Payback ~1.5 years

### Scenario 2: AI Incident Detection (Architecture)

**Sensing layer:**
- Video RTSP (1080p / 4K) → decode → YOLOv8 detection → DeepSORT tracking → trajectory analysis
- mmWave radar point cloud (20 Hz) → clustering → speed / accel / heading → road-coordinate projection
- Radar-video late fusion: timestamp alignment (PTP / NTP) → joint extrinsic calibration → feature-level fusion

**Detection layer (parallel pipeline):**
```
video stream → [stopped-vehicle: static object + dwell]
             → [wrong-way: trajectory vs lane direction >150°]
             → [pedestrian on highway: pedestrian in high-speed lane]
             → [debris: small static object + avoidance behavior]
             → [congestion: multi-object speed drop + queue growth]
             → [smoke/fire: flame/smoke detector]
             → [collision: multi-vehicle abnormal decel + position change]
```
Each stream outputs confidence 0–100 + event type + key-frame snapshot + location.

**Verification layer (false-positive reduction):**
- Multi-camera cross-validation: trajectory continuity across adjacent cameras
- Radar + video cross-validation: both detect anomaly and agree on type
- PSAP / 112 dispatch-data real-time comparison: secondary confirmation of existing alerts
- Human-feedback loop: FP / FN fed back into retraining set

**Performance baseline:**
- Daytime recall >98%, night >93%, rain/fog >88%
- Detection latency <3 s (edge inference), end-to-end alert push <8 s
- False-alarm rate <0.5 / device / day (radar-video fused), <2 / day (vision-only)
- Measured on a European highway corridor (e.g., Germany A9 / Netherlands A58): 99% detection accuracy, <3 s response

### Scenario 3: AI Traffic-Flow Forecast (Architecture)

**Multi-horizon forecasting:**
| Horizon | Use | Model | Input | MAPE target |
|:-------:|------|------|------|:-----------:|
| 5 min | Real-time control / dynamic guidance | ST-GNN + Transformer | Real-time speed + detector + signal state | <6% |
| 15 min | Proactive control / bus dispatch | Informer + PatchTST | Above + short-term weather | <8% |
| 1 hr | Guidance / ramp-metering | Transformer + TFT | + calendar + mid-term weather | <10% |
| 24 hr | Work-zone / control planning | N-BEATS + TFT | + events + work zones | <15% |
| 7 day | Situation analysis | Prophet + LSTM | Macro trend | <20% |

**Spatio-temporal joint modeling:**
- Network as graph: node = intersection/segment, edge = physical connection, weight = travel time / correlation
- Spatial encoding: GAT learns adaptive neighbor weights; upstream 3–5 km segments most correlated on highways
- Temporal encoding: multi-head attention captures daily / weekly / holiday patterns; Transformer decoder autoregressive generation
- Exogenous injection: weather embedding (one-hot + learnable), holiday embedding, event / work-zone mask

**Uncertainty quantification:**
- Deep Ensemble: 5 independent models, mean + std
- Quantile Regression: predict P10 / P50 / P90
- Output: point forecast + interval + confidence

### Scenario 4: Transport LLM

**"1 + N + X + Agent" architecture:**

**"1" — General transport LLM base:**
- Base choice: Llama / GPT / Claude / Gemini / Mistral (per deployment & sovereignty needs)
- Domain continued pre-training: inject ≥500 GB transport corpus (regulations / standards / textbooks / papers / reports / cases / operational data)
- Params: 7B–100B+ (7B for on-prem, 100B+ for cloud)
- Multimodal extension: understand CCTV frames, map / GIS snapshots, structured-data tables, video keyframes

**"N" — N vertical LoRA fine-tunes:**
| Vertical | Added Training Data | Key Capability | LoRA Params |
|----------|-------------------|---------------|-----------|
| Traffic management | Traffic regs + cases + signal-policy libs | Signal advice / incident assess / plan gen | ~50M |
| Highway | Tolling regs + maintenance std + safety manual | Toll audit / maintenance / incident analysis | ~40M |
| Rail & metro | Signaling regs + O&M manual + fault cases | Fault diag / repair advice / dispatch Q&A | ~45M |
| Port & shipping | TOS manual + port regs + maritime law | Dispatch advice / compliance / efficiency | ~40M |
| Traffic safety | Accident DB + safety checklists + emergency plans | Risk analysis / compliance / response | ~50M |

**"X" — X professional Agents:**
- Signal-optimization Agent: "PM peak outbound congestion" → coordinated signal plan
- Incident-assessment Agent: event description → standard assessment report + action + resource dispatch
- Report-writing Agent: auto-generate daily / weekly / monthly / emergency reports
- Design Agent: project requirements → initial technical plan + cost estimate
- Knowledge-Q&A Agent: conversational retrieval over regs / standards / cases
- Compliance Agent: technical plan vs standard gap analysis

**RAG system:**
- Knowledge base: transport law library (500+ docs) + standards library (2000+ standards) + case library (10,000+ cases) + plan library (5,000+ plans)
- Embedding: BGE-M3 / multilingual sentence embeddings, 1024 / 2048 dim
- Retrieval: hybrid (vector similarity + BM25 + KG relations)
- Hallucination control: sentence-level source alignment, citations

**Performance baseline:**
- Transport Q&A accuracy: 92% (base), 96% (RAG)
- Report quality: human review 4.2 / 5.0
- Hallucination rate: <5% (RAG-constrained), <15% (no RAG)
- Inference latency: <2 s (interactive), <30 s (long report)

### Scenarios 5–25: Quick Architecture Reference

| Scenario | Key Model Choice | Core Input | Output | Deployment |
|---------|-----------------|----------|--------|-----------|
| 5. AI maintenance | YOLOv8 + U-Net + degradation model | Pavement 3D point cloud, images, sensor series | Defect type / loc / severity + rehab ranking | Vehicle + cloud |
| 6. AI safety forecast | XGBoost + ST-GNN + causal forest | Accidents + violations + geometry + flow + weather | Risk heatmap + blackspot ranking + fixes | Cloud |
| 7. AI dynamic pricing | DQN / PPO + elasticity model | Transaction + flow + time + elasticity | Real-time optimal rate | Cloud + edge |
| 8. AI port | YOLOv8 + DeepSORT + MIP + DRL | Video + CCTV + TOS + AIS + equip state | Quay / AGV / yard dispatch | Edge + cloud |
| 9. AI airport | XGBoost + LSTM + solver | Flights + weather + gate + ground nodes + history | ETA + gate assign + ground dispatch | Cloud + local |
| 10. AI rail PHM | LSTM-AE + Transformer + 1D-CNN | Sensor series + maint records + design | Anomaly + RUL + repair advice | Edge + cloud |
| 11. AI multimodal | MIP + RL + LNS | Waybill + capacity + hub + location + traffic | Optimal transfer + live re-dispatch | Cloud |
| 12. AI low-altitude UTM | Kalman + Transformer + GNN + conflict | Flight plan + radar + ADS-B + weather + airspace | Trajectory + conflict alert + re-plan | Cloud + edge |
| 13. Transport LLM | LLM + RAG + KG + LoRA | See above | See above | Cloud |
| 14. AI carbon | MOVES + COPERT + fusion | GPS + vehicle attr + speed + grade | Road / zone / vehicle emissions + trend | Cloud |
| 15. AI scheduling | GA + MIP + demand forecast | Demand + trips + drivers + vehicles + regs | Optimal roster + live adjust | Cloud |
| 16. AI disaster warning | Weather model + InSAR + LSTM | Weather + RS + geology + history | Hazard prob + scope + alert level | Cloud |
| 17. AI assistant | LLM + RAG + ASR + TTS | FAQ + regs + cases + dialog history | Multi-turn reply + ticket creation | Cloud |
| 18. AI enforcement | YOLOv8 + DeepSORT + OCR + behavior | Video + vehicle DB + violation rules | Evidence chain (image + video + desc) | Edge |
| 19. AI planning | Multi-agent sim + GAN + gen-AI | Network + OD + pop + land use + plan lib | Option comparison + assessment | Cloud |
| 20. AI bridge/tunnel SHM | Acoustic + LSTM-AE + vibration | Multi-sensor series + inspect + design | Anomaly + damage loc + trend | Edge + cloud |
| 21. AI econ forecast | VAR + LSTM + econometric mix | Econ indicators + volume + invest + regs | Forecast + scenario analysis | Cloud |
| 22. AI driver training | VR/AR + behavior + knowledge tracing | Driving behavior + trajectory + exam data | Personalized coaching + plan | Local + cloud |
| 23. AI age-friendly | LLM + voice + intent + rec | Need + facility + pref + voice | Best trip plan + voice guidance | Cloud + mobile |
| 24. AI cost estimation | NLP + KG + XGBoost forecast | Quota lib + history + market price + drawings | Cost est + anomaly review + report | Cloud |
| 25. AI sentiment | BERT + sentiment + LDA | Social + news + complaints + hotline | Sentiment trend + alert + advice | Cloud |

---

## III. Full Transport AI Model-Training Lifecycle

### 3.1 Standard Project Lifecycle

```
┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐
│Need  │→│Data  │→│Feat  │→│Model │→│Eval  │→│Deploy│→│Ops   │
│Anal. │ │Prep  │ │Eng   │ │Train │ │Review│ │      │ │Iter  │
└──────┘  └──────┘  └──────┘  └──────┘  └──────┘  └──────┘  └──────┘
  1–2 wk    4–8 wk    2–4 wk    4–12 wk   1–3 wk    2–6 wk    ongoing
```

### 3.2 Stage Details

**Phase 1: Needs Analysis & Feasibility**
| Check | Pass Criteria | If Fail |
|-------|--------------|--------|
| Clear business value | ROI or social benefit quantifiable | Redefine or drop |
| Data feasibility | Minimum dataset usable, quality acceptable | Build data collection first |
| Tech feasibility | Mature open or commercial product exists | Build vs buy |
| Safety feasibility | Non-safety-critical or safety layer addable | Add safety redundancy |
| Compliance feasibility | Meets data-security / privacy law | Complete compliance review first |

**Phase 2: Data Preparation**
| Step | Tool / Method | Deliverable | Quality |
|------|--------------|------------|--------|
| Source survey | Data catalog + interviews | Source list + data dictionary | Cover all needs |
| Collection | Kafka / CDC / API / batch | Raw dataset | Complete + timely |
| Cleaning | Python (Pandas) + Spark | Cleaned dataset | Missing <5%, anomaly <1% |
| Labeling | LabelStudio / CVAT + pre-label | Labeled dataset | Agreement >95%, IoU >0.85 |
| Quality report | Great Expectations / custom | Quality report | Completeness / accuracy / consistency / timeliness |

**Labeling strategy (transport specifics):**
- Safety-critical (incident / hazard): expert labeling + multi-round cross-validation, tolerance <0.1%
- Efficiency (forecast / signal): auto-label + spot-check, tolerance <5%
- Information (assistant / Q&A): LLM-assisted + human review, tolerance <10%
- Label cost reference: 2D box $0.07–0.28 / box, 3D point-cloud $0.28–1.1 / box, segmentation $0.7–2.8 / image, text QA $0.7–4.2 / item

**Phase 3: Feature Engineering (transport features)**
| Category | Typical Features | Method |
|---------|-----------------|--------|
| Temporal | Peak / off-peak / low, weekday, holiday, special event | one-hot + embedding |
| Spatial | Location code, road class, lanes, speed limit, network correlation | GNN embed + static code |
| Flow | Speed / flow / saturation / queue absolute + delta | Sliding-window stats + diff |
| Environment | Weather, light, temp, visibility | one-hot + normalize |
| Behavior | Driving pattern, trip chain, route preference | Sequence mining + clustering |
| Device | Model, install loc, maint history, fault freq | Category code + anomaly flag |

**Phase 4: Model Training**
- Frameworks: PyTorch (70%) > TensorFlow (20%) > JAX (10%)
- Distributed: DeepSpeed ZeRO-3 (LLM) / DDP (small) / FSDP
- Precision: FP16 / BF16 mixed + INT8 / INT4 quantized inference
- LR: CosineAnnealing + LinearWarmup (10% steps)
- Regularization: Dropout (0.1–0.3) + WeightDecay (0.01–0.1) + LabelSmoothing (0.05–0.1)
- Augmentation (vision): Mosaic / MixUp / CutMix, random brightness / contrast / rain-fog sim
- Augmentation (time-series): TimeWarping, MagnitudeWarping, Jittering, Scaling

**Phase 5: Model Evaluation**
| Dimension | General Metric | Transport Metric | Frequency |
|----------|---------------|-----------------|----------|
| Accuracy | Acc / Prec / Recall / F1 / mAP / AUC | Incident latency (s), ETA error (min), congestion accuracy | Each train |
| Robustness | OOD degradation, adversarial | Adverse weather, occlusion, new-city transfer | Each train |
| Efficiency | P50 / P95 / P99 latency, QPS | End-to-end (incl. comms), throughput (streams/device) | Pre-deploy |
| Fairness | Per-group performance diff | Core vs suburb, peak vs off-peak | Quarterly |
| Safety | Fault injection, safe-failure prob | Rule fallback accuracy, heartbeat recovery | Pre-deploy |
| Explainability | SHAP / LIME / GradCAM | Engineer comprehension score | Per version |

**Phase 6: Deployment** — see Section IV.
**Phase 7: Ops iteration** — see Section VII.

---

## IV. Edge-AI and Cloud-AI Decision Framework

### 4.1 Deployment Location Decision Tree

```
AI task hard-real-time? (<50 ms)
├─ Yes → Large data volume? (video / radar stream)
│   ├─ Yes → [Edge] roadside AI box / industrial PC
│   └─ No  → [Onboard] embedded MCU / NPU
└─ No → Model params >10B?
    ├─ Yes → [Cloud] GPU / NPU cluster inference
    └─ No → Small data & non-real-time?
        ├─ Yes → [Cloud] economical
        └─ No → Network reliable?
            ├─ Yes → [Cloud inference + edge fallback]
            └─ No → [Edge-primary + cloud training]
```

### 4.2 Deployment Recommendation by Mode

| Mode | Strategy | Edge Device | Cloud Need | Key Consideration |
|------|---------|------------|-----------|------------------|
| AI signal control | Edge inference + cloud train | NVIDIA Jetson / industrial PC | Train cluster | Survive offline, <50 ms |
| AI incident detection | Edge inference + cloud aggregate | Bosch / NVIDIA Jetson Orin | Video cloud + alert platform | High video volume (4–8 Mbps/stream) |
| AI flow forecast | Cloud train + infer | N/A | GPU cluster | Non-real-time, heavy compute |
| Autonomous driving | Onboard perceive + decide | NVIDIA Orin / DRIVE | Data-loop platform | Hard real-time <30 ms, ASIL-D |
| Transport LLM | Cloud train + infer | N/A (too large) | Multi-node | >10B params, no edge |
| Rail PHM | Edge / onboard infer | Embedded MCU / ARM | Aggregate + train | Low sensor BW, high real-time |
| AI tally (port) | Edge inference | NVIDIA Jetson Orin | Data summary | Hi-res video, low local latency |
| Low-altitude UTM | Edge + cloud hybrid | NVIDIA Jetson / edge | Wide-area coordination | Local conflict at edge, global in cloud |

### 4.3 Edge-AI Hardware Selection Map

| Platform | AI Compute (INT8) | Power | Use | Unit Price | Env. |
|----------|:----------------:|:----:|-----|-----------|:----:|
| NVIDIA Jetson Orin Nano | 40 TOPS | 15 W | Light inference (1–4 streams) | $0.4–0.7k | IP40 |
| NVIDIA Jetson Orin NX | 100 TOPS | 25 W | High-perf edge AI | $0.8–1.7k | IP40 |
| NVIDIA Jetson Orin AGX | 275 TOPS | 60 W | AV / radar-video fusion | $2–3.5k | IP40 |
| Intel Movidius / Arc edge | 10–40 TOPS | 15–40 W | Vision / analytics | $0.5–2k | IP65 |
| Bosch / Siemens traffic edge | 4–32 TOPS | 15–45 W | Monitoring-specific AI | $0.7–2.8k | IP65 |
| Qualcomm / Ambarella CV | 10–50 TOPS | 5–20 W | Low-power edge | $0.1–0.5k | IP40 |
| Automotive SoC (e.g., NVIDIA DRIVE / Intel) | 100–250 TOPS | 30–60 W | In-vehicle AV | $0.7–1.4k | Automotive-grade |

### 4.4 Cloud Training-Cluster Configuration Guide

| Scale | Training Config | Inference Config | Storage | Network | Reference Price |
|-------|----------------|-----------------|---------|--------|----------------|
| Small (1–3 models) | 4× A100 / H100 | 2× A100 / H100 | 50 TB NVMe | 25 GbE | $1.4–4.2M |
| Medium (5–10 models) | 8× A100 / H100 | 4× A100 / H100 | 100 TB | 100 GbE | $4.2–11M |
| Large (LLM + multi-scene) | 32× H100 | 8× H100 | 500 TB | 200 GbE | $21–70M |
| XL (city AI training center) | 128× H100 | 32× H100 | 2 PB | 400 GbE | $70M–280M |

---

## V. Transport-AI-Specific Challenges and Engineering Responses

### 5.1 Ten Transport-AI Challenges & Solutions

| # | Challenge | Severity | Frequency | Engineering Solution | Theory |
|---|----------|:--------:|:--------:|---------------------|-------|
| 1 | **Long-tail** | Very high | Low | Sim scenario gen (Diffusion) + few-shot + rule fallback | Extreme Value Theory |
| 2 | **Safety-critical** | Very high | Low | SIL assessment + independent monitor + temporal redundancy + fail-safe | ISO 26262 / SOTIF |
| 3 | **Real-time constraint** | High | High | Quant (INT8/INT4) + prune + distill + AI chip + edge + compile opt | Real-Time Systems |
| 4 | **Multi-agent non-stationarity** | High | Ongoing | CTDE + coordination protocol + hierarchy (global→region→local) | Game Theory + MARL |
| 5 | **Data silos & privacy** | High | Ongoing | Federated learning (FedAvg/FedProx) + DP (ε<8) + MPC + data-stays-put | FL + DP |
| 6 | **Concept drift** | Med | Ongoing | Drift detect (ADWIN/DDM) + periodic retrain + cautious online + HITL | Concept Drift |
| 7 | **Multimodal spatio-temporal align** | Med | High | HW time-sync (PTP/gPTP <1 µs) + joint calib + interp + late-fusion check | Sensor Fusion |
| 8 | **Explainability** | Med | On-demand | SHAP + LIME + Grad-CAM + symbolic rules + decision trace | XAI |
| 9 | **Fairness dispute** | Med | Ongoing | Stratified eval + fairness constraint (Equalized Odds) + transparent report | Algorithmic Fairness |
| 10 | **Adversarial vulnerability** | High | Low | Adv training (FGSM/PGD) + input transform + physical validation + anomaly detect | Adversarial Robustness |

### 5.2 Transport AI Safety Integrity Level (T-AI-SIL)

| T-AI-SIL | Description | Failure Consequence | Use | Development Requirement |
|:--------:|-------------|---------------------|-----|------------------------|
| 0 | No safety impact | User inconvenience | Info display / stats / report | Standard AI dev |
| 1 | Minor impact | Efficiency drop | Guidance / ETA / parking | Basic validation + monitoring |
| 2 | Moderate impact | Service interruption | Incident detect / demand / bus dispatch | Robustness test + explain + data quality |
| 3 | High impact | Possible injury | AI signal / AV decision / tunnel link | Formal verification + independent monitor + redundancy |
| 4 | Extreme impact | Possible multiple fatalities | Train control / ATC | Full-lifecycle cert + 3rd-party independent assessment |

### 5.3 Sim2Real Gap Strategy

| Gap Source | Impact | Strategy |
|-----------|--------|---------|
| Perception-noise difference | Detect / recognize drop | Domain randomization + real fine-tune + GAN domain transfer |
| Behavior difference | RL policy fails | Real-data calibrate driver model + adversarial imitation |
| Sensor-layout difference | Blind spot / overlap | Multi-device layout sim + robustness (sensor Dropout) |
| Comm latency / loss | Coordination fails | Latency-injection train + decentralized + local fallback |
| Vague safety boundary | Over / under-conservative | Constrained RL + safety-efficiency tradeoff + safety layer |

---

## VI. AI Evaluation System and Benchmark Data

### 6.1 General Evaluation Framework (7 dimensions)

| Dimension | Metric | Transport Consideration | Method |
|:---------:|--------|-------------------------|-------|
| **Accuracy** | Acc/Prec/Recall/F1/mAP/MOTA | Split by scenario (day/night/rain/fog) | Stratified test set |
| **Robustness** | Degradation rate | Sensor fault / comm loss / weather | Fault injection + OOD |
| **Real-time** | P50/P95/P99, QPS | End-to-end (comm+decode+infer+exec) | Load test + prod monitor |
| **Fairness** | Max diff, Equalized Odds | Region / time / group fairness | Stratified report |
| **Explainability** | Attribution consistency | Engineer trust | Expert review + interview |
| **Safety** | Safe-failure prob | Critical scenes (pedestrian / wrong-way) must pass | Red-team + fault tree |
| **Efficiency** | Train cost / $ | Inference energy (J/inference) | Resource + cost monitor |

### 6.2 Custom KPI Baselines by Scenario (2025 industry level)

| Scenario | Core Metric | Baseline | Leading | SOTA | Dataset / Method |
|---------|------------|:-------:|:-------:|:----:|------------------|
| AI signal | Delay reduction vs fixed | 12–18% | 22–25% | 30% | Floating-car + detector A/B |
| AI incident detect | Recall % | 88–92% | 97–99% | 99.5% | Human-labeled + replay |
| AI flow forecast | 15-min MAPE % | 10–15% | 6–8% | 4% | Historical backtest |
| AV perception | nuScenes NDS % | 68–72% | 75–78% | 82% | nuScenes / Waymo Open |
| Transport LLM | Q&A accuracy % | 85–90% | 92–96% | 97% | Human-labeled QA set |
| AI maintenance – crack | Crack recall (>2mm) % | 88–92% | 95–97% | 98% | Human + field |
| AI maintenance – PQI | 1-yr RQI MAE | 1.5–2.5 | 1.0–1.5 | 0.8 | Backtest |
| AI toll audit – evasion | Evasion recall % | 85–90% | 92–96% | 98% | Full manual review |
| AI tally – container | Container-no rate % | 95–98% | 98–99.5% | 99.8% | Manual stats |
| PHM – fault | 24-h-ahead precision % | 80–85% | 88–93% | 95% | Fault replay |
| A-CDM – ETA | ±3-min accuracy % | 75–82% | 85–92% | 95% | Actual flight compare |
| AI assistant | First-contact resolve % | 55–65% | 70–80% | 85% | Helpdesk stats |
| AI scheduling | Labor-hour saving % | 8–12% | 15–22% | 30% | A/B test |

### 6.3 Public Benchmark Datasets

| Dataset | Domain | Modality | Scale | License | Source |
|---------|--------|---------|-------|---------|--------|
| nuScenes | AV | Multimodal | 1,000 scenes, 1.4M frames | CC BY-NC-SA 4.0 | nuscenes.org |
| Waymo Open | AV | Multimodal | 1,950 segments, 570 h | Non-commercial | waymo.com/open |
| Argoverse 2 | Trajectory | LiDAR + HDMap | 250k scenes | CC BY-NC-SA 4.0 | argoverse.org |
| CityFlowV2 | Traffic video | Video | 3.25 h, 660k boxes | Research | AI City Challenge |
| METR-LA / PEMS-BAY | Flow | Time-series | Months, 207/325 sensors | Public | Caltrans / PeMS |
| RDD2022 | Pavement | Image | 47,420 imgs (6 countries) | CC BY 4.0 | CRDDC / U. Tokyo |
| RailSem19 | Rail | Image | 8,500 imgs | Research | WildDash |
| Traffic4cast | Forecast | Dynamic graph | 3 cities, months | Public | NeurIPS competition |
| CULane | Lane | Image | 133,235 imgs | Research | CUHK |
| BDD100K | AV | Multimodal | 100k videos | BSD | UC Berkeley |
| LUMPI / HighD | Trajectory | Naturalistic | Germany highways | Public | IKA RWTH |
| INRIX / TomTom Traffic | Flow | Aggregated | Global | Commercial | INRIX / TomTom |

---

## VII. Transport MLOps System

### 7.1 Full-Lifecycle MLOps Platform

```
┌──────────────────────────────────────────────────────────────────┐
│                    Transport MLOps Unified Platform                 │
├─────────────┬──────────────┬──────────────┬─────────────────────┤
│ Data Mgmt   │ Experiment    │ Model Mgmt   │ Deploy & Monitor     │
│             │              │              │                     │
│ Data version│ Exp tracking  │ Model registry│ CI/CD               │
│ Quality rpt │ HPO (Optuna)  │ Version+lineage│ Canary / A-B        │
│ Feature store│ Exp compare  │ Format convert│ Edge OTA push       │
│ Label mgmt  │ Distrib sched │ Eval+compliance│ Perf+drift monitor  │
│ Fed data    │ Resource mon  │ Security scan │ Alert + auto-rollback│
└─────────────┴──────────────┴──────────────┴─────────────────────┘
```

### 7.2 Continuous-Training Triggers

| Trigger | Detection | Threshold | Action | Risk Control |
|:-------:|----------|----------|--------|-------------|
| Data drift | PSI / KL / Hellinger | PSI > 0.25 | Full / incremental retrain | Canary validation |
| Perf degrade | Key KPI falling | 7-day drop >3% | Root-cause + rollback / retrain | Auto-rollback |
| Periodic | Time | Every 1–3 months | Full retrain | Standard release |
| New scenario | Manual | New area / road / device | Expand set + incr train | Limit canary |
| Safety event | Manual + auto | Any safety incident | Hotfix + full regression | Fast-track, top priority |
| New labels done | Data platform | New labels >20% | Incremental train | Normal flow |

### 7.3 MLOps Technology Selection Matrix

| Module | Open Source | Commercial Cloud | Recommendation (typical) |
|:------:|------------|------------------|:------------------------:|
| Experiment | MLflow | SageMaker / Vertex / Azure ML | MLflow |
| Feature store | Feast | SageMaker Feature Store | Feast |
| Model registry | MLflow Registry | SageMaker | Follow cloud |
| Orchestration | Airflow / Kubeflow | Step Functions / Vertex | Airflow |
| Monitoring | Evidently AI | SageMaker Model Monitor | Evidently |
| Serving | Triton / BentoML | SageMaker Endpoint | Triton (general) |
| CI/CD | GitHub Actions / Jenkins | CodePipeline / Cloud Build | Follow existing |
| Edge OTA | Mender / RAUC | AWS IoT Greengrass / Azure IoT | Per platform |
| Data quality | Great Expectations | Glue DQ / cloud DQ | GE |

### 7.4 Safe Model Release Flow

```
Training complete
  │
  ├─ 1. Offline eval (hold-out)
  │   └─ Pass → 2; Fail → back to train
  ├─ 2. Shadow mode (advise, don't execute; compare old vs new)
  │   └─ Run 1–2 weeks, collect comparison
  ├─ 3. Small canary (5% → 15% → 30%)
  │   └─ ≥3 days each, monitor safety + accuracy
  ├─ 4. Expand canary (50% → 100%)
  │   └─ Monitor 1–2 weeks
  └─ 5. Full deployment
      └─ 7×24 on-call monitoring
```

---

## VIII. High-Value Cases and Measured Performance

### 8.1 Urban AI Signal-Control Cases

**Singapore (LTA i-Transport + adaptive control)**
- 150+ intersections, MARL + coordinated control
- Deployment: sensing + edge compute + cloud coordination; investment ~$7M
- Result: AM-peak speed +24% (29→36 km/h), delay −25%, stops −35%
- Payback ~1.5 yr, ~6,800 t CO2/yr abated
- Key success: strong agency mandate + full sensing coverage + deep ops integration

**London (TfL SCOOT / adaptive + MaaS)**
- 600+ intersections AI-assisted optimization
- Result: central-area efficiency +15%, congestion ranking improved materially
- Innovation: "human-in-the-loop" — AI recommends, operator confirms, then executes
- Lesson: pure AI auto-control had ~60% real-world acceptance; HITL more viable

**Los Angeles (Metro / city DRL + MPC)**
- 116 intersections DRL + MPC joint optimization
- Result: arterial travel time −20%, stops −35%, annual saved travel value >$25M

### 8.2 Highway AI Cases

**Netherlands A58 / Germany A9 smart corridor**
- 113 km, 680 radar-video fusion units, investment ~$40M
- Result: incident detection 99% accuracy, <3 s response, false alarm <0.5/day
- Highlights: all-weather radar-video fusion + edge AI + digital twin + C-ITS

**US interstate AI toll audit**
- 4,800+ km highway, AI audit platform
- Result: 1.2M+ anomalous transactions/yr identified, ~$50M toll recovered
- Tech: XGBoost + GNN + rules hybrid

**European motorway AI incident detection**
- Result: proactive detection 15% (manual) → 85% (AI); detect time 8 min → 45 s
- Follow-on: auto VMS publish + navigation-app event push

### 8.3 Smart-Port AI Cases

**Rotterdam / PSA automated terminal**
- Global-leading automated terminal
- Result: quay rate +30%, horizontal transport +25%, energy/box −20%
- Tech: AI quay (vision + laser) + autonomous vehicles (5G + AV) + digital twin

**PSA Singapore**
- Mixed-mode operation (manual + automated), quay 42 moves/h
- AI tally accuracy 99.5%+, e-documents 95%
- Key innovation: mixed mode lowers automation barrier

### 8.4 Rail & Metro AI Cases

**Tokyo Metro PHM**
- Covers key assets (rolling stock / signaling / power / platform doors)
- Result: fault-warning accuracy >90%, >5-min delay −40%
- Model: preventive maintenance replacing scheduled

**London Underground AI demand forecast**
- All lines covered
- Result: 15-min demand forecast MAPE <9%, AM peak crowd-control precision +35%
- Tech: GNN + Transformer + LSTM Ensemble

---

## IX. Technology-Maturity Roadmap 2024–2030

### 9.1 Transport AI Maturity Roadmap

| AI Tech | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 |
|---------|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| CV AI (detect / recognize) | ● | ● | ● | ● | ● | ● | ● |
| CV AI (behavior understanding) | ◐ | ● | ● | ● | ● | ● | ● |
| AI signal (isolated) | ● | ● | ● | ● | ● | ● | ● |
| AI signal (regional coord) | ◐ | ◐ | ● | ● | ● | ● | ● |
| AI signal (citywide AI-native) | ○ | ◐ | ◐ | ◐ | ● | ● | ● |
| AI incident (video) | ● | ● | ● | ● | ● | ● | ● |
| AI incident (multimodal) | ◐ | ● | ● | ● | ● | ● | ● |
| AI forecast (short) | ● | ● | ● | ● | ● | ● | ● |
| AI forecast (long) | ◐ | ◐ | ● | ● | ● | ● | ● |
| AV L4 (Robotaxi) | ◐ | ◐ | ◐ | ● | ● | ● | ● |
| AV E2E | ○ | ◐ | ◐ | ◐ | ● | ● | ● |
| Transport LLM (base) | ◐ | ◐ | ● | ● | ● | ● | ● |
| Transport LLM (multi-agent) | ○ | ○ | ◐ | ◐ | ◐ | ● | ● |
| AI digital twin | ○ | ◐ | ◐ | ◐ | ● | ● | ● |
| AI maintenance decision | ◐ | ◐ | ● | ● | ● | ● | ● |
| AI port dispatch | ◐ | ● | ● | ● | ● | ● | ● |
| AI low-altitude UTM | ○ | ○ | ◐ | ◐ | ● | ● | ● |
| AI causal inference (safety) | ○ | ○ | ◐ | ◐ | ◐ | ● | ● |
| Quantum AI (optimization) | ○ | ○ | ○ | ○ | ○ | ◐ | ◐ |
| Embodied AI (transport robots) | ○ | ○ | ○ | ◐ | ◐ | ◐ | ◐ |

Legend: ○ R&D / PoC → ◐ pilot / small deploy → ● scale / mature

### 9.2 Key Milestone Forecast

| Year | Milestone | Impact |
|:----:|-----------|-------|
| 2025 | Citywide AI signal coverage >30k intersections globally | AI signal goes to scale |
| 2025 | Transport LLM enters government operations at scale | Reporting / assistant / Q&A standard |
| 2026 | First driverless L4 robotaxi commercial approvals | AV commercialization truly opens |
| 2026 | C-ITS / V2X standard family formalized (3GPP / ETSI / IEEE) | V2X industry standardization accelerates |
| 2027 | Low-altitude UTM platforms deployed citywide | AAM infrastructure matures |
| 2028 | AI-native signal control covers >20% of major cities | Transport AI enters AI-native phase |
| 2029 | Transport LLM agents embedded in daily decisions | HITL becomes new normal |
| 2030 | L4 AV at scale on open urban roads | Structural travel-pattern change |

---

## X. Transport AI Ethics and Safety Governance

### 10.1 Eight Ethical Principles and Operationalization

| Principle | Operational Requirement | Verification |
|----------|------------------------|-------------|
| **Safety first** | T-AI-SIL + independent monitor + fail-safe | Safety case + fault injection |
| **Fair & just** | Stratified performance report + vulnerable-group protection | Fairness metric + community hearing |
| **Transparent / explainable** | Key decisions explainable + human appeal + algorithm filing | XAI tool + comprehension test |
| **Privacy protection** | Data minimization + anonymization + privacy compute + lifecycle | PIA + technical assessment |
| **Human autonomy** | Human override + emergency takeover + human review of big decisions + appeal | Drill + takeover-time test |
| **Clear accountability** | Algorithm impact assessment + decision trace + liability insurance | Incident process + trace test |
| **Inclusive** | Age-friendly + accessible + rural coverage + affordable | Coverage stats + vulnerable survey |
| **Sustainable** | Energy optimize + carbon track + green-AI training | Carbon assessment + energy monitor |

### 10.2 Governance Framework

**Structure:**
- AI ethics board: cross-functional (tech + legal + business + public), quarterly
- Algorithm impact assessment: mandatory for high-risk, selective for low/medium
- Transport-AI filing: key systems filed + re-filed on major version
- Public participation: major AI projects published + hearing + feedback channel

**Human-in-the-loop design (4-level progression):**
```
L1: AI advises → human confirms → execute (daily)
L2: AI advises → execute (human can emergency-stop) (routine)
L3: AI executes → post-hoc human review (low-risk)
L4: AI executes → human cannot intervene (emergency, strictly limited)
```

### 10.3 Compliance Checklist

| Domain | Law / Standard | Use | Key Evidence |
|-------|---------------|-----|--------------|
| Personal data | GDPR / CCPA | Personal-data processing | DPIA + consent record + impact assess + anonymization |
| Data security | NIST CSF 2.0 / ISO 27001 | All transport data | Classification + security assessment + data catalog |
| Algorithm regulation | EU AI Act / national AI rules | Public-facing AI | Conformity / transparency report |
| Cyber (systems) | NIST CSF 2.0 / NIS2 | IT systems | CSF assessment + audit report |
| Critical infrastructure | NIS2 / CER Directive | Critical transport infra | CII designation + security testing + drills |
| Vehicle cyber | ISO 21434 / UN R155 | C-ITS / AV | TARA report + cyber case + key management |
| Autonomous driving | UNECE WP.29 / national AV acts | Public-road test / ops | Test permit + safety-driver + incident + mileage report |
| Cryptography | National crypto standards | CII + high-grade systems | Approved-algorithm use + crypto assessment |

---

## XI. Transport AI Investment-Decision Framework

### 11.1 Build vs Buy Matrix

| Factor | Lean Build | Lean Buy | Neutral |
|--------|:----------:|:--------:|:-------:|
| Core differentiation | Strong | Generic | Partial |
| Data sensitivity | Very high (CII) | Low | Medium |
| In-house AI team | >20 | <5 | 5–20 |
| Data exclusivity | High | None | Partial |
| Long-term commitment | 3 yr+ | Short | 1–3 yr |
| Tech barrier | Medium | High | Trainable |
| Budget | Ample | Tight | Moderate |
| Iteration frequency | High | Low | Medium |

**Recommended strategy:**
- Core AI capability (signal / incident / AV perception) → build + open-source co-build
- General AI capability (LLM base / vision framework) → leading vendor + open source
- Customized AI (fine-tune / business agents) → ecosystem partner + in-house
- Standard AI tools (MLOps / labeling / monitoring) → buy mature products

### 11.2 AI Investment Prioritization

**RICE++ six-dimension scoring** (see SKILL.md, Part IV):
- R (Reach): scope of users / business (1–5)
- I (Impact): core-business impact (1–5)
- C (Confidence): delivery confidence (1–5)
- E (Effort): implementation difficulty inverse (1–5, 1=hardest)
- S (Safety): safety-impact positive bonus (1–5)
- P (Policy): regulatory urgency positive bonus (1–5)
- **Priority = (R × I × C) / E + S + P**

**2025 transport-AI priority ranking (top 5):**

| Rank | Scenario | R | I | C | E | S | P | Score | Recommendation |
|:----:|----------|:-:|:-:|:-:|:-:|:-:|:-:|:-----:|----------------|
| 1 | AI incident detection | 5 | 5 | 5 | 4 | 5 | 4 | 40.25 | Scale now |
| 2 | AI signal optimization | 4 | 5 | 5 | 3 | 4 | 5 | 42.33 | Key push |
| 3 | AI smart assistant | 5 | 3 | 5 | 5 | 1 | 3 | 19.00 | Quick win |
| 4 | AI maintenance decision | 4 | 4 | 4 | 4 | 3 | 3 | 22.00 | Gradual rollout |
| 5 | AI safety-risk forecast | 4 | 5 | 4 | 3 | 5 | 4 | 35.67 | Key push |

---

> **Legal Notice**: This document is a reference file of the *Transportation Digital & AI Transformation Expert (Standard Edition)* Skill. AI applied to safety-critical transport scenarios must pass thorough simulation validation, closed-track testing, and safety review under the "safety first" principle. This document is for learning reference only and is not specific technical implementation advice or a safety guarantee.

> **Last updated**: July 2025 | **Version**: v2.0 | **Next update**: January 2026
