# AI Scenario Priority Scorecard (RICE++)
## AI Scenario Priority Scorecard for Transportation

---

## 1. Tool Overview

This tool uses the RICE++ six-dimension scoring model (Reach + Impact + Confidence + Effort + Strategy + Data) to systematically prioritize AI application scenarios in transportation. It ships with 25 pre-scored transport AI scenarios that can be used directly or adjusted to your context.

### Use Cases
- AI strategy planning and investment decisions
- Annual AI project kickoff review
- AI prioritization for digital-transformation programs
- AI implementation roadmap (Phase 1 / 2 / 3)
- AI project portfolio management

---

## 2. RICE++ Six-Dimension Scoring Model

### 2.1 Dimension Definitions & Criteria
| Dim | English | Weight | Description | Range |
|-----|---------|--------|-------------|-------|
| R | Reach | 20% | User / business coverage | 1–5 |
| I | Impact | 25% | Improvement to core business | 1–5 |
| C | Confidence | 15% | Technical feasibility & data readiness | 1–5 |
| E | Effort | 15% | Investment (people / budget / time); lower cost = higher score | 1–5 (5 = very low) |
| S | Strategy | 15% | Strategic alignment | 1–5 |
| D | Data | 10% | Data readiness & availability | 1–5 |

### 2.2 Detailed Criteria per Dimension

#### R — Reach
| Score | Criteria | Example |
|-------|----------|---------|
| 1 | Single department / single scenario | Model validation in a test environment |
| 2 | 2–3 departments or business lines | AI at a single corridor / pilot zone |
| 3 | Citywide / group-wide, multi-department | Citywide signal optimization |
| 4 | Industry-wide / cross-city | National / multi-city transport AI platform |
| 5 | Public users + industry + exportable | MaaS AI recommendation for hundreds of millions of users |

#### I — Impact
| Score | Criteria | Example |
|-------|----------|---------|
| 1 | Marginal (< 5% efficiency gain) | Report automation |
| 2 | Moderate (5%–15%) | Video event-detection assist |
| 3 | Significant (15%–30%) | AI signal-timing optimization |
| 4 | Transformative (30%–50%) | Autonomous-dispatch coordination |
| 5 | Disruptive (> 50% or new business model) | Unmanned operation |

#### C — Confidence
| Score | Criteria | Example |
|-------|----------|---------|
| 1 | Pure exploration; unproven approach | Training a transport LLM from scratch |
| 2 | Lab-validated; no production case | New algorithm theory validation |
| 3 | Industry success exists, but high adaptation needed | CV scenario (needs local labeled data) |
| 4 | Mature tech; in-house similar experience | ALPR, video structuring |
| 5 | Off-the-shelf; large-scale proven | Calling a cloud API |

#### E — Effort
| Score | Criteria | Example (reference investment) |
|-------|----------|--------------------------------|
| 5 (very low) | Months, < $0.7M, < 3 people, ready APIs | Calling an OCR API |
| 4 (low) | Quarter, $0.7M–$2.8M, 3–5 people | Fine-tuning a pre-trained model |
| 3 (medium) | Half-year, $2.8M–$7M, 5–10 people | Custom CV model dev + deployment |
| 2 (high) | Year, $7M–$28M, 10–30 people | Full AI platform build-out |
| 1 (very high) | 2yr+, > $28M, 30+ team | Train an LLM from scratch |

#### S — Strategy
| Score | Criteria |
|-------|----------|
| 1 | No direct link to strategy |
| 2 | Indirectly supports a strategic goal |
| 3 | Directly supports a strategic goal |
| 4 | Supports multiple goals; strategic priority |
| 5 | Core strategic project; executive attention |

#### D — Data
| Score | Criteria |
|-------|----------|
| 1 | Data does not exist; must collect / label from scratch |
| 2 | Exists but messy / poor quality; heavy cleansing |
| 3 | Exists with some standards; light processing |
| 4 | Standardized storage; ready for training |
| 5 | Rich, high-quality labeled data; continuously accumulated |

---

## 3. 25 Pre-Scored Transport AI Scenarios

### 3.1 Pre-Scored Overview
| # | AI Scenario | R | I | C | E | S | D | Weighted | Priority |
|---|-------------|---|---|---|---|---|---|----------|----------|
| 1 | Automatic video traffic-event detection | 4 | 3 | 4 | 4 | 4 | 4 | 3.75 | P0 |
| 2 | AI signal-timing optimization | 4 | 4 | 4 | 3 | 5 | 4 | 4.00 | P0 |
| 3 | Intelligent assistant / FAQ chatbot | 5 | 2 | 5 | 5 | 3 | 5 | 3.95 | P0 |
| 4 | License-plate / vehicle-type recognition | 5 | 3 | 5 | 5 | 4 | 5 | 4.40 | P0 |
| 5 | Traffic-flow prediction | 4 | 4 | 4 | 3 | 5 | 4 | 4.00 | P0 |
| 6 | Route recommendation optimization | 5 | 3 | 4 | 4 | 4 | 4 | 3.95 | P0 |
| 7 | Transit intelligent scheduling / dispatch | 3 | 4 | 4 | 3 | 4 | 3 | 3.55 | P1 |
| 8 | Traffic incident impact assessment | 3 | 3 | 3 | 3 | 4 | 3 | 3.15 | P1 |
| 9 | Parking-demand prediction | 4 | 3 | 4 | 4 | 3 | 3 | 3.55 | P1 |
| 10 | Pavement-defect auto-recognition | 3 | 3 | 4 | 3 | 3 | 3 | 3.15 | P1 |
| 11 | Transport public-sentiment analysis | 4 | 2 | 5 | 4 | 3 | 4 | 3.55 | P1 |
| 12 | Driving-behavior analysis | 3 | 3 | 4 | 3 | 3 | 3 | 3.15 | P1 |
| 13 | Traffic safety-risk prediction | 3 | 4 | 3 | 3 | 4 | 3 | 3.40 | P1 |
| 14 | Transport LLM intelligent Q&A | 4 | 4 | 2 | 2 | 5 | 3 | 3.40 | P2 |
| 15 | Digital-twin traffic simulation | 3 | 4 | 2 | 2 | 4 | 3 | 3.10 | P2 |
| 16 | V2X cooperative-ITS decisioning | 3 | 4 | 2 | 1 | 4 | 3 | 2.95 | P2 |
| 17 | Autonomous bus dispatch | 2 | 4 | 2 | 1 | 3 | 2 | 2.45 | P2 |
| 18 | MaaS multi-modal recommendation | 4 | 3 | 3 | 2 | 4 | 3 | 3.25 | P2 |
| 19 | AI carbon-emission monitoring & prediction | 3 | 3 | 3 | 3 | 3 | 2 | 2.95 | P2 |
| 20 | AI emergency-resource dispatch | 2 | 4 | 3 | 2 | 4 | 2 | 2.95 | P2 |
| 21 | Intelligent regulatory-compliance review | 3 | 2 | 3 | 3 | 2 | 3 | 2.65 | P2 |
| 22 | AI asphalt / concrete mix optimization | 2 | 3 | 2 | 2 | 2 | 2 | 2.20 | P3 |
| 23 | AI-assisted transport planning & design | 2 | 3 | 2 | 2 | 3 | 2 | 2.45 | P3 |
| 24 | Low-altitude UAV infrastructure inspection | 3 | 3 | 2 | 2 | 3 | 2 | 2.65 | P3 |
| 25 | Driver fatigue detection | 3 | 3 | 4 | 3 | 2 | 3 | 3.05 | P3 |

### 3.2 Scenario Details

**Scenario 1: Automatic video traffic-event detection**
- Description: Real-time CV analysis of surveillance video to detect accidents, congestion, wrong-way driving, pedestrian incursions, etc.
- Key capabilities: Video structuring, object detection, multi-target tracking, event classification
- Tech needs: GPU servers, video-ingest gateway, CV framework
- Data needs: 10,000+ hours labeled traffic video (varied weather / lighting / scenes)
- Industry maturity: ★★★★☆ (mature)
- Typical investment: $4.2M–$11M (incl. GPU hardware)
- Duration: 6–12 months
- Est. ROI: 80% less manual patrol; event detection time −60%

**Scenario 2: AI signal-timing optimization**
- Description: Deep-RL dynamic signal timing for urban intersections; arterial / area coordination
- Key capabilities: Reinforcement learning, traffic-flow modeling, multi-agent coordination
- Tech needs: GPU / edge nodes, signal-controller comms interface
- Data needs: Intersection flow (6mo+), timing plans, travel-time data
- Industry maturity: ★★★★☆ (validated in some cities)
- Typical investment: $7M–$21M (50+ intersections)
- Duration: 12–18 months
- Est. ROI: +15–25% intersection throughput; −20% average stops

**Scenario 3: Intelligent assistant / FAQ chatbot**
- Description: LLM / knowledge-graph based transport-service Q&A covering regulation queries, service handling, complaints
- Key capabilities: NLU, knowledge base, multi-turn dialogue, sentiment
- Tech needs: LLM API / on-prem deployment, knowledge platform
- Data needs: 100k+ historical service dialogues, regulatory docs
- Industry maturity: ★★★★★ (very mature)
- Typical investment: $1.4M–$4.2M
- Duration: 3–6 months
- Est. ROI: 60% less service staff; 7×24 coverage

**Scenario 4: License-plate / vehicle-type recognition**
- Description: High-accuracy ALPR, vehicle classification, feature extraction in traffic scenes
- Key capabilities: OCR, object detection, fine-grained classification
- Tech needs: GPU / edge box
- Data needs: Multi-region plate samples, multi-angle vehicle images
- Industry maturity: ★★★★★ (very mature, accuracy > 99%)
- Typical investment: $0.7M–$2.8M (software)
- Duration: 1–3 months
- Est. ROI: Replaces manual entry; +90% efficiency

**Scenario 5: Traffic-flow prediction**
- Description: Deep learning forecasts of 15-min to 24-hr traffic flow from historical + real-time data
- Key capabilities: Time-series forecasting, spatio-temporal GNN, multi-source fusion
- Tech needs: GPU server, big-data platform
- Data needs: 1yr+ historical flow, weather, holiday calendar
- Industry maturity: ★★★★☆
- Typical investment: $2.8M–$7M
- Duration: 6–9 months
- Est. ROI: Earlier control decisions; congestion-warning accuracy > 85%

**Scenario 6: Route recommendation optimization**
- Description: Smart route recommendation from real-time state, user preference, multi-modal combos
- Key capabilities: Routing algorithms, RL, multi-objective optimization
- Tech needs: Routing engine, real-time traffic service
- Data needs: Road network, real-time traffic, transit timetables, POI
- Industry maturity: ★★★★☆
- Typical investment: $4.2M–$11M
- Duration: 6–12 months
- Est. ROI: 8–12% average travel-time saving for users

**Scenario 7: Transit intelligent scheduling / dispatch**
- Description: Demand-forecast based timetable optimization and dynamic vehicle dispatch
- Key capabilities: Operations research, demand forecasting, MILP
- Tech needs: Optimization solver, transit dispatch interface
- Data needs: Smart-card / scan data, GPS traces, line OD data
- Industry maturity: ★★★☆☆
- Typical investment: $2.8M–$7M
- Duration: 6–12 months
- Est. ROI: −10–15% operating cost; −15% passenger wait

**Scenario 8: Traffic incident impact assessment**
- Description: AI estimates the scope and severity of network impact when incidents / works occur
- Key capabilities: Traffic simulation, impact propagation, causal inference
- Tech needs: Simulation engine, GPU acceleration
- Data needs: Road-network topology, historical incident-impact data
- Industry maturity: ★★★☆☆
- Typical investment: $2.8M–$5.6M
- Duration: 6–12 months
- Est. ROI: +30% emergency-response efficiency

**Scenario 9: Parking-demand prediction**
- Description: AI predicts parking demand by time / zone to support guidance and pricing
- Key capabilities: Spatio-temporal prediction, clustering, elasticity modeling
- Tech needs: Data platform, prediction API
- Data needs: 1yr+ lot in/out data, surrounding POI, event calendar
- Industry maturity: ★★★★☆
- Typical investment: $1.4M–$4.2M
- Duration: 3–6 months
- Est. ROI: +15–20% space utilization

**Scenario 10: Pavement-defect auto-recognition**
- Description: On-vehicle / inspection video auto-detects cracks, potholes, rutting
- Key capabilities: Semantic segmentation, anomaly detection, defect grading
- Tech needs: GPU / edge device, inspection vehicle / UAV
- Data needs: 100k+ labeled pavement-defect samples
- Industry maturity: ★★★★☆
- Typical investment: $2.8M–$7M
- Duration: 6–12 months
- Est. ROI: +80% inspection efficiency; −20% maintenance cost

**Scenario 11: Transport public-sentiment analysis**
- Description: NLP real-time monitoring & sentiment analysis of social media / complaint channels
- Key capabilities: Sentiment, NER, topic clustering, trend forecast
- Tech needs: NLP platform, data-collection tool
- Data needs: Social media data, complaint records
- Industry maturity: ★★★★☆
- Typical investment: $1.4M–$4.2M
- Duration: 3–6 months
- Est. ROI: +70% sentiment-response speed

**Scenario 12: Driving-behavior analysis**
- Description: OBD / GPS based driver profiling and safety scoring
- Key capabilities: Behavior clustering, anomaly detection, scoring
- Tech needs: Big-data platform, stream-compute engine
- Data needs: OBD data (100k+ vehicles / 1yr+), crash records
- Industry maturity: ★★★★☆
- Typical investment: $2.8M–$5.6M
- Duration: 6–12 months
- Est. ROI: −15–25% crash rate

**Scenario 13: Traffic safety-risk prediction**
- Description: Multi-source data predicts high-risk times / segments; proactive prevention
- Key capabilities: Risk modeling, spatio-temporal analysis, causal inference
- Tech needs: ML platform, GIS
- Data needs: 3yr+ crash history, road attributes, flow, weather
- Industry maturity: ★★★☆☆
- Typical investment: $4.2M–$8.4M
- Duration: 9–15 months
- Est. ROI: −10–20% crashes

**Scenario 14: Transport LLM intelligent Q&A**
- Description: Domain LLM for transport; NL queries, plan recommendation, report generation
- Key capabilities: Domain fine-tuning, RAG, prompt engineering, multimodal
- Tech needs: GPU cluster (A100/H100), LLM framework, vector DB
- Data needs: Transport text (tens of millions of docs), standards, regulations
- Industry maturity: ★★☆☆☆ (evolving fast)
- Typical investment: $7M–$28M
- Duration: 6–18 months
- Est. ROI: +50% decision efficiency; +80% knowledge-retrieval efficiency

**Scenario 15: Digital-twin traffic simulation**
- Description: AI-driven simulation & plan evaluation on a digital-twin platform
- Key capabilities: Micro / meso simulation, agent modeling, twin rendering
- Tech needs: High-performance GPU cluster, simulation engine, twin platform
- Data needs: High-def road network, real-time traffic, vehicle OD
- Industry maturity: ★★☆☆☆
- Typical investment: $14M–$42M
- Duration: 12–24 months
- Est. ROI: +60% plan-evaluation efficiency

**Scenario 16: V2X cooperative-ITS decisioning**
- Description: Real-time AI decisions from cooperative-ITS data (green-wave, collision warning, lane advice)
- Key capabilities: Real-time inference, multi-source fusion, edge AI
- Tech needs: Edge compute unit, 5G / C-V2X, low-latency AI framework
- Data needs: V2X messages, HD map, real-time traffic state
- Industry maturity: ★★☆☆☆
- Typical investment: $28M–$70M (scaled)
- Duration: 18–36 months
- Est. ROI: +20–30% throughput (V2X corridors)

**Scenario 17: Autonomous bus dispatch**
- Description: Intelligent dispatch & operations management for autonomous buses
- Key capabilities: AV decisioning, fleet dispatch, remote monitoring
- Tech needs: AV vehicles, roadside sensing, cloud-control platform
- Data needs: HD maps, pilot operations data
- Industry maturity: ★★☆☆☆
- Typical investment: $70M+ (vehicles + infrastructure)
- Duration: 24–36 months
- Est. ROI: −60–80% labor cost (operations)

**Scenario 18: MaaS multi-modal recommendation**
- Description: Optimal multi-modal trip combo recommendation from user profile + real-time state
- Key capabilities: Multi-objective optimization, user profiling, recommender
- Tech needs: MaaS platform, real-time data fusion
- Data needs: User trip data, real-time traffic, weather, events
- Industry maturity: ★★★☆☆
- Typical investment: $4.2M–$11M
- Duration: 6–12 months
- Est. ROI: +3–5% transit mode share

**Scenario 19: AI carbon-emission monitoring & prediction**
- Description: AI real-time monitoring, prediction, and decarbonization recommendations for transport emissions
- Key capabilities: Time-series forecast, emission modeling, optimization
- Tech needs: Big-data platform, ML framework
- Data needs: Traffic flow, speed, vehicle type, emission factors
- Industry maturity: ★★★☆☆
- Typical investment: $2.8M–$7M
- Duration: 6–12 months
- Est. ROI: +80% emission-accounting efficiency; carbon-trade revenue

**Scenario 20: AI emergency-resource dispatch**
- Description: AI dispatch of emergency resources (rescue, medical, police) on incidents
- Key capabilities: Resource optimization, real-time dispatch, multi-objective
- Tech needs: Solver, stream-compute platform, GIS
- Data needs: Resource locations, real-time road state, incident history
- Industry maturity: ★★★☆☆
- Typical investment: $4.2M–$8.4M
- Duration: 9–15 months
- Est. ROI: −25–40% emergency response time

**Scenario 21: Intelligent regulatory-compliance review**
- Description: AI auto-checks transport plans / designs / operations against regulations
- Key capabilities: NLU, knowledge graph, rule engine
- Tech needs: NLP platform, KG engine
- Data needs: Regulation library, review records
- Industry maturity: ★★☆☆☆
- Typical investment: $2.8M–$5.6M
- Duration: 6–12 months
- Est. ROI: +50% review efficiency

**Scenario 22: AI asphalt / concrete mix optimization**
- Description: AI optimizes asphalt / concrete mix from historical performance data
- Key capabilities: Material modeling, regression, optimization
- Tech needs: ML platform, material DB
- Data needs: 5yr+ pavement performance, material params, climate
- Industry maturity: ★★☆☆☆
- Typical investment: $2.8M–$7M
- Duration: 12–24 months
- Est. ROI: +15–20% pavement life

**Scenario 23: AI-assisted transport planning & design**
- Description: AI assists alignment, intersection, and traffic-organization design
- Key capabilities: Generative design, multi-objective optimization, simulation
- Tech needs: AI + CAD/CAE, GPU cluster
- Data needs: Terrain / geo data, demand forecast, code library
- Industry maturity: ★★☆☆☆
- Typical investment: $4.2M–$11M
- Duration: 12–18 months
- Est. ROI: +40–60% design efficiency

**Scenario 24: Low-altitude UAV infrastructure inspection**
- Description: UAV + AI inspection of highways / bridges / tunnels
- Key capabilities: Autonomous flight, defect detection, 3D modeling
- Tech needs: UAV platform, edge AI, 5G
- Data needs: Infrastructure 3D models, defect sample library
- Industry maturity: ★★☆☆☆
- Typical investment: $7M–$21M
- Duration: 12–18 months
- Est. ROI: 5x+ inspection efficiency; −90% high-altitude manual work

**Scenario 25: Driver fatigue detection**
- Description: In-cab camera AI detects fatigue / distraction in real time with warning
- Key capabilities: Facial landmark detection, behavior recognition, real-time inference
- Tech needs: In-vehicle edge compute, DMS algorithm
- Data needs: Driver facial data (DMS labeled)
- Industry maturity: ★★★★☆
- Typical investment: $1.4M–$4.2M
- Duration: 3–6 months
- Est. ROI: −40–60% fatigue-related crashes

---

## 4. Weight Calibration Workshop Guide

### 4.1 Process
```
Step 1: Each scorer independently proposes weights (5 min)
Step 2: Show all weights; discuss gaps (10 min)
Step 3: Debate the most divergent dimension (10 min)
Step 4: Reach consensus or take the average (5 min)
Step 5: Lock weights; proceed to scenario scoring
```

### 4.2 Calibration Template
| Dimension | Rater 1 | Rater 2 | Rater 3 | Rater 4 | Rater 5 | Avg | Final |
|-----------|---------|---------|---------|---------|---------|-----|-------|
| R (Reach) | __% | __% | __% | __% | __% | __% | __% |
| I (Impact) | __% | __% | __% | __% | __% | __% | __% |
| C (Confidence) | __% | __% | __% | __% | __% | __% | __% |
| E (Effort) | __% | __% | __% | __% | __% | __% | __% |
| S (Strategy) | __% | __% | __% | __% | __% | __% | __% |
| D (Data) | __% | __% | __% | __% | __% | __% | __% |
| **Total** | **100%** | **100%** | **100%** | **100%** | **100%** | **100%** | **100%** |

### 4.3 Common Calibration Scenarios
| Org Type | Suggested Weight Adjustments |
|----------|------------------------------|
| Public sector / transport authorities | S (Strategy) ↑ to 20–25%; C (Confidence) ↑ |
| Transport investment holding groups | I (Impact) ↑ to 30–35%; C (Confidence) ↑ |
| Technology startups | C (Confidence) ↓; I (innovation impact) ↑ |
| Operations-focused companies | E (Effort) ↑; I (Impact) ↑ |
| Research / academic institutions | C (feasibility) may drop; exploration weight up |

---

## 5. Auto-Scoring Formulas

### 5.1 Weighted Score
```
Scenario Score = R×Wr + I×Wi + C×Wc + E×We + S×Ws + D×Wd
```
where Wr+Wi+Wc+We+Ws+Wd = 1.0

### 5.2 Priority Bands
| Score | Priority | Strategy |
|-------|----------|----------|
| ≥ 3.5 | P0 — act now | Start immediately; MVP within 6 months |
| 3.0 – 3.5 | P1 — near-term | Start within 6–12 months |
| 2.5 – 3.0 | P2 — pipeline | Validate & prepare within 12–18 months |
| < 2.5 | P3 — watch | Monitor; re-evaluate when conditions mature |

### 5.3 Quick-Win Identifier
```
Quick-Win = (Confidence ≥ 4) AND (Effort ≥ 4) AND (Impact ≥ 3)
i.e., mature tech + low cost + baseline business impact

Quick-Wins in the pre-scored set:
  1. License-plate / vehicle-type recognition (C=5, E=5, I=3) ✓
  2. Intelligent assistant / FAQ (C=5, E=5, I=2) — confirm I
  3. Video event detection (C=4, E=4, I=3) ✓
  4. Parking-demand prediction (C=4, E=4, I=3) ✓
```

---

## 6. Implementation Cost-Estimation Guide

### 6.1 Effort & Duration
| Complexity | Team | Key Roles | Duration | Est. Cost |
|------------|------|-----------|----------|-----------|
| Simple (API call) | 2–3 | 1 back-end + 1 front-end + 1 algo | 1–3 mo | $0.4M–$1.4M |
| Medium (custom model) | 5–8 | 2 algo + 2 back-end + 1 FE + 1 PM + 1 QA | 6–9 mo | $2.8M–$7M |
| Complex (platform) | 10–20 | 4 algo + 4 BE + 2 FE + 2 data + 1 PM + 1 architect + 1 QA | 12–18 mo | $11M–$28M |
| Very complex (LLM) | 20+ | 6 algo + 4 BE + 2 FE + 4 data + 2 PM + 1 architect | 18–24 mo | $28M–$70M |

### 6.2 Cost Quick-Reference by Scenario
| Scenario | Software/Algo | HW/Cloud | Data | Labor | Total | Duration |
|----------|---------------|----------|------|-------|-------|----------|
| ALPR | $0.4M–$0.7M | $0.7M–$1.4M | $0.14M–$0.28M | $0.4M–$0.7M | $1.7M–$3.1M | 1–3 mo |
| Video event detection | $1.4M–$2.8M | $2.8M–$5.6M | $0.42M–$0.7M | $1.1M–$2.1M | $5.7M–$11M | 6–12 mo |
| AI signal optimization | $2.8M–$5.6M | $1.4M–$4.2M | $0.7M–$1.4M | $2.1M–$4.2M | $7M–$15M | 12–18 mo |
| Flow prediction | $1.4M–$2.8M | $0.7M–$1.4M | $0.42M–$0.7M | $1.1M–$2.1M | $3.6M–$7M | 6–9 mo |
| Transport LLM | $4.2M–$11M | $4.2M–$8.4M | $1.4M–$2.8M | $4.2M–$8.4M | $14M–$30M | 12–24 mo |
| Digital-twin simulation | $5.6M–$11M | $4.2M–$8.4M | $1.4M–$2.8M | $4.2M–$8.4M | $15M–$30M | 12–24 mo |

---

## 7. Scenario Dependency Graph
```
Layer 1 (Foundations)
┌────────────┐   ┌────────────┐   ┌────────────┐
│ ALPR (4)   │   │ Video event│   │ Flow pred. │
│ (4)        │   │ detect (1) │   │ (5)        │
└─────┬──────┘   └─────┬──────┘   └─────┬──────┘
      │                │                │
      ▼                ▼                ▼
Layer 2 (Applications) — depend on foundations
┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐
│ AI signal  │ │Safety-risk │ │Route rec.  │ │Parking     │
│ opt (2)    │ │pred (13)   │ │(6)        │ │pred (9)    │
└─────┬──────┘ └─────┬──────┘ └─────┬──────┘ └─────┬──────┘
      │              │              │              │
      ▼              ▼              ▼              ▼
Layer 3 (Advanced)
┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐
│ V2X (16)   │ │Digi-twin   │ │Transport   │ │MaaS rec.   │
│            │ │(15)        │ │LLM (14)    │ │(18)        │
└─────┬──────┘ └─────┬──────┘ └─────┬──────┘ └─────┬──────┘
      │              │              │              │
      ▼              ▼              ▼              ▼
Layer 4 (Transformative)
┌────────────┐ ┌────────────┐
│ AV bus     │ │ City ITS   │
│ dispatch(17)│ │ platform   │
└────────────┘ └────────────┘
```

---

## 8. Phased Implementation Logic

### Phase 1 (0–12 mo): Foundations & quick wins
| Scenario | Rationale |
|----------|-----------|
| ALPR | Quick-win; most mature tech |
| Video event detection | Direct ops efficiency; clear ROI |
| AI signal-timing optimization | Core business improvement; visible impact |
| Intelligent assistant / FAQ | Low cost, fast deploy, strong user perception |
| Traffic-flow prediction | Foundation for upper-layer apps |

### Phase 2 (12–24 mo): Expand scenarios & build platform
| Scenario | Rationale |
|----------|-----------|
| Route recommendation | User-side value; MaaS foundation |
| Transit scheduling | Ops efficiency |
| Safety-risk prediction | High safety value |
| Parking-demand prediction | Urban-governance need |
| MaaS multi-modal recommendation | Mobility-service integration |
| Transport LLM (lite) | Platformize AI capability |

### Phase 3 (24–36 mo): Foresight & innovation leadership
| Scenario | Rationale |
|----------|-----------|
| Transport LLM (full) | Core competitiveness |
| Digital-twin simulation | Decision support |
| V2X cooperative-ITS decisioning | AV preparation |
| Low-altitude UAV inspection | New-domain positioning |
| Autonomous bus dispatch | Forward-looking positioning |

---

## 9. ROI Quick-Reference
| Scenario | Typical Invest ($M) | Annual Benefit ($M) | Payback | 3-yr ROI | Main Benefit Source |
|----------|---------------------|---------------------|---------|----------|---------------------|
| ALPR | 2.1 | 1.1–1.7 | < 2 yr | 160–240% | Labor substitution |
| Video event detection | 8.4 | 4.2–7.0 | 1.5–2 yr | 150–250% | Ops efficiency + safety |
| AI signal optimization | 11 | 5.6–11 | 1–2 yr | 150–300% | Throughput + emissions |
| Flow prediction | 4.9 | 2.1–3.5 | 1.5–2.5 yr | 130–215% | Decision support |
| Route recommendation | 7 | 2.8–4.9 | 1.5–2.5 yr | 120–210% | UX + guidance |
| Transit scheduling | 4.9 | 2.8–5.6 | 1–2 yr | 170–340% | Operating cost |
| Transport LLM | 21 | 7–14 | 1.5–3 yr | 100–200% | Efficiency + knowledge |
| Digital twin | 21 | 7–11 | 2–3 yr | 100–160% | Decision optimization |

---

## 10. Make vs. Buy Guidance (by scenario)
| Scenario | Strategy | Rationale |
|----------|----------|----------|
| ALPR | Buy (mature solution) | Extremely mature; no differentiation in building |
| Video event detection | Buy + customize | Foundation mature; needs domain adaptation |
| AI signal optimization | Buy + customize / co-dev | Core differentiator; needs local training |
| Flow prediction | Buy + customize | Algorithm mature; data is the key |
| Intelligent assistant | Buy (API) | Cloud API is sufficient |
| Route recommendation | Buy + co-dev | Algorithm + data both matter |
| Transit scheduling | Buy or Make | Depends on scale and ambition |
| Transport LLM | Buy + fine-tune | Buy base model; do domain fine-tune |
| Digital twin | Buy platform + Make scenarios | Buy platform; build scenarios |
| Driving-behavior analysis | Make | Needs deep integration with business systems |

---

## 11. Scenario Scoring Worksheet
```
============================================================================
                  AI Scenario Priority Scoring Worksheet
============================================================================

Date: ________________  Scorer: ________________

Instructions:
1. Score each scenario on the 6 dimensions (1–5)
2. Confirm weights (default or custom)
3. Compute weighted score; auto-rank

Weights (sum = 100%):
R=___%  I=___%  C=___%  E=___%  S=___%  D=___%

| Scenario | R | I | C | E | S | D | Weighted | Priority |
|----------|---|---|---|---|---|---|----------|----------|
| 1. ______ |   |   |   |   |   |   | ____ | __ |
| 2. ______ |   |   |   |   |   |   | ____ | __ |
| 3. ______ |   |   |   |   |   |   | ____ | __ |
| ...       |   |   |   |   |   |   | ____ | __ |
| n. ______ |   |   |   |   |   |   | ____ | __ |

============================================================================
```

---

## 12. Usage Instructions
1. **Filter scenarios**: Pick relevant scenarios from the 25 pre-scored (add your own as needed).
2. **Calibrate weights**: Run a 5–7 person weight-calibration workshop (Section 4).
3. **Score independently**: Each person scores every scenario's 6 dimensions (1–5).
4. **Aggregate**: Use the weighted formula for composite scores.
5. **Rank**: Sort high to low; assign P0 / P1 / P2 / P3.
6. **Find Quick-Wins**: Filter high-confidence + low-effort + high-impact.
7. **Phase planning**: Build Phase 1/2/3 plans using the dependency graph.
8. **Estimate investment**: Use Section 6 for phase budgets.
9. **Re-assess periodically**: Recommended every 6 months as tech and needs evolve.
