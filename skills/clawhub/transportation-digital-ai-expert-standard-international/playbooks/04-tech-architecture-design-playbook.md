# Technical Solution Architecture Design Playbook

## Playbook Overview

| Item | Description |
|------|-------------|
| **Applicable scenarios** | Architecture design for transport technology solutions — from requirements understanding to an implementable technical plan, covering intelligent transport management platforms, transport operations coordination centers (TOCC), V2X, smart highways, MaaS platforms, and other typical transport systems |
| **Core philosophy** | "Business drives architecture; architecture serves business" — the essence of transport architecture is finding the optimal technical expression for transport business problems |
| **Total duration** | 4–8 weeks (requirements analysis → architecture design → tech selection → plan authoring → review) |
| **Deliverables** | Requirements analysis doc, architecture design spec, tech-selection report, implementation plan, risk assessment report |
| **Design team** | 1 solution architect + 1 transport-domain expert + domain experts as needed (data / AI / security / integration) + 1 technical writer |

---

## Phase 1: Requirements Understanding & Modeling (Weeks 1–2)

### 1.1 Transport Business-Modeling Method

The starting point of a transport solution is not technology selection but a deep understanding of the transport business. Use the framework below to structure business needs:

**Five-layer business-analysis framework:**

| Layer | Analyzes | Output | Key question |
|-------|----------|--------|--------------|
| **User layer** | Pain & expectations of travelers / operators / managers / maintainers | User personas + journey maps | Who uses it? Where's the pain? |
| **Scenario layer** | Concrete scenarios (e.g., "AM-peak signal control", "ETC exception handling") | Scenario cards (5–10) | What scenario? Frequency? Consequence? |
| **Process layer** | End-to-end business processes (e.g., "incident detect → confirm → dispatch → handle → recover") | Process diagrams | How does the flow go? Where's the bottleneck? |
| **Data layer** | Data flow / sources / quality / standards | Data-flow diagram + data dictionary | Where from? Where to? Quality? |
| **System layer** | Existing systems / interfaces / constraints / migration needs | System-context diagram | What systems interact? What constraints? |

### 1.2 Mapping Business to Technical Requirements

| Business requirement | Technical translation | Example |
|----------------------|----------------------|---------|
| "Managers want real-time citywide traffic situation" | Real-time ingestion + dashboard viz + <500 ms latency | Ingestion (Flink) + OLAP engine + WebGL rendering |
| "Timing engineers want AI-assisted timing" | Flow-forecast model + optimization solver + human-in-the-loop workflow | RL signal-control model + plan-recommendation engine + one-click push |
| "Public wants bus location on their phone" | High-concurrency query API + location cache + GPS cleaning | Redis cluster + location microservice + public API gateway |

---

## Phase 2: Architecture Design (Weeks 3–5)

### 2.1 Four-Layer Architecture Method

#### 2.1.1 Logical architecture (what it does)

Define functional module decomposition and responsibilities:

```
┌────────────────────────────────────────────┐
│              Application layer              │
│  Signal control │ Incident mgmt │ Guidance │ Situational awareness │
├────────────────────────────────────────────┤
│              Service layer                  │
│  Ingestion │ Stream compute │ AI inference │ API Gateway │
├────────────────────────────────────────────┤
│              Data layer                     │
│  Real-time DB │ History DB │ Data lake │ Cache │ Message queue │
├────────────────────────────────────────────┤
│           Infrastructure layer              │
│  Compute │ Storage │ Network │ Security │ Container orchestration │
└────────────────────────────────────────────┘
```

**Design principles:**
- One-way inter-layer dependency (upper depends on lower; lower unaware of upper)
- Within a layer, split horizontally by business domain (e.g., app layer splits signal control / incident mgmt)
- Sink cross-layer shared components (auth / logging / config)

#### 2.1.2 Physical architecture (where it deploys)

Define the physical deployment topology:

| Node | Deploys | Scale reference | Key constraint |
|------|---------|-----------------|----------------|
| Roadside edge | Sensor fusion / signal control / incident detection | 1–2 MECs per intersection | Latency <10 ms / industrial grade |
| Regional aggregation | Arterial coordination / regional optimization | 1 node per 50–200 intersections | Latency <100 ms |
| Central cloud / IDC | Big-data analytics / AI training / mgmt platform | Active-active primary+standby | Availability >99.9% |
| DR center | Data backup / cold-standby apps | Off-site | RPO<1 h / RTO<4 h |

#### 2.1.3 Data architecture (how data flows and stores)

```
Source → Ingestion (Kafka) → Stream processing (Flink) → Real-time DB (Redis/ClickHouse)
                            ↓                              ↓
                        Data lake (Iceberg) → Offline warehouse (StarRocks) → BI/reporting
                            ↓
                        Feature engineering → AI training → Model serving
```

**Data-classification strategy:**

| Data type | Storage engine | Retention | Access pattern |
|-----------|----------------|-----------|----------------|
| Real-time sensing (radar / video trajectory) | Kafka → Redis | 24 h | Real-time stream + short-window query |
| Business-state (timing / guidance content) | PostgreSQL | Permanent | OLTP read/write |
| Historical analytics (daily/weekly/monthly reports) | StarRocks/ClickHouse | 3 yr | OLAP aggregate query |
| Archive (compliance retention) | Object storage (Iceberg) | 10 yr+ | Low-frequency batch query |

#### 2.1.4 Security architecture (how it's protected)

Follow the "four-horizontal, three-vertical" security framework in Part 7 of SKILL.md; focus design on:

1. **Network segmentation**: OT domain (signal control / sensing) / IT domain (mgmt platform / analytics) / DMZ (external services) — three-tier isolation
2. **Identity & auth**: Unified IAM + MFA + fine-grained RBAC
3. **Data security**: Classification & grading → masking engine → dynamic data masking → audit logging
4. **Zero trust**: Micro-segmentation + continuous verification, especially in OT/IT convergence

### 2.2 Key Transport-System Architecture Decisions

| Decision | Lightweight (small / single-mode) | Standard (mid / multi-mode) | Flagship (large / city-scale) |
|----------|-----------------------------------|------------------------------|-------------------------------|
| **Ingestion** | REST API | API gateway (Kong/APISIX) | API gateway + service mesh (Istio) |
| **Message queue** | Redis Streams | Kafka | Pulsar (multi-tenant) |
| **Real-time compute** | In-app streaming | Flink / Flink SQL | Flink + RisingWave |
| **Database** | PostgreSQL | PostgreSQL + Redis + Elasticsearch | Multi-engine (PostgreSQL+Redis+ES+StarRocks+Cassandra) |
| **Container orchestration** | Docker Compose | K3s | Kubernetes + Istio mesh |
| **Monitoring/O&M** | Prometheus + Grafana | Prometheus + Loki + Tempo + Grafana | Unified observability (SkyWalking) |

---

## Phase 3: Technology Selection (Weeks 4–6)

### 3.1 Technology-Selection Decision Tree

Sort selection priority by these principles:

1. **Business-fit first**: Pick what best solves the transport business problem, not the most "advanced"
2. **Open standards first**: Prefer open protocols / open APIs / open source to reduce vendor lock-in
3. **Ecosystem maturity first**: Prefer ecosystems with active community / rich docs / ample talent
4. **Performance vs cost balance**: Under performance requirements, pick the lowest-TCO option

### 3.2 Key-Selection Comparison Template

| Domain | Candidate A | Candidate B | Candidate C | Recommended | Rationale |
|--------|-------------|-------------|-------------|:-----------:|-----------|
| Message queue | Kafka | Pulsar | Redis Streams | | |
| Stream compute | Flink | Spark Streaming | RisingWave | | |
| OLAP engine | StarRocks | ClickHouse | Doris | | |
| Time-series DB | TDengine | TimescaleDB | InfluxDB | | |
| Search engine | Elasticsearch | OpenSearch | Meilisearch | | |

### 3.3 Vendor Independence & Substitutability Assessment

| Component | Current choice | Lock-in risk (1–5) | Migration cost | Alternative | Substitutability |
|-----------|----------------|:------------------:|----------------|-------------|:----------------:|
| [Component] | [Vendor / product] | [score] | [High/Med/Low] | [Alt product] | [assessment] |

**Core principle**: For every component with a "5 lock-in risk," there must be a documented migration plan and cost estimate.

---

## Phase 4: Plan Authoring & Review (Weeks 6–8)

### 4.1 Technical-Solution Document Structure

A complete technical solution should contain:

```
1. Solution summary (1 pg)
2. Business understanding & requirements analysis
3. Overall architecture design
   3.1 Logical architecture
   3.2 Physical architecture
   3.3 Data architecture
   3.4 Security architecture
4. Key technology notes
   4.1 Core algorithm / model description
   4.2 Key tech-selection rationale
   4.3 Innovation points & differentiation
5. System integration plan
6. Implementation plan & resource needs
7. O&M plan & SLA
8. Risk assessment & mitigation
9. Reference cases
Appendix: technical spec / interface spec / test plan
```

### 4.2 Architecture-Review Checklist

| Dimension | Check | Pass criterion |
|-----------|-------|----------------|
| **Completeness** | All four architectures (logical/physical/data/security) present? | All four, no major gaps |
| **Consistency** | Do logical modules map to physical nodes? | Traceable mapping |
| **Feasibility** | Any unrealistic design (single point / over-complex)? | Confirmed feasible by ≥2 architects |
| **Scalability** | Does 3× growth need re-architecture? | 3× needs only horizontal scale-out |
| **Security** | Can security design pass review? | Meets the corresponding security-accreditation level |
| **Operability** | Monitoring / logs / alerts / backup covered? | O&M team agrees it's operable |

### 4.3 Common Architecture Anti-Patterns

| Anti-pattern | Symptom | Consequence | Correction |
|--------------|---------|-------------|------------|
| **Over-engineering** | A 10-intersection project designed with data mesh + event sourcing + service mesh | 2× implementation cost / team can't handle | Choose complexity by scale (see 2.2) |
| **Dashboard-driven design** | Architecture decided by "what leaders see on the screen" | Fragile system / stale data / becomes a showpiece | Drive by business & data flow; dashboard is output, not input |
| **Tech stacking** | Using new tech for its own sake (e.g., blockchain on a simple CRUD) | Complexity explosion / reliability drop | Every tech choice has a clear rationale & alternative comparison |
| **Vendor-lock design** | Architecture deeply bound to one vendor's proprietary protocol | Hard upgrades / runaway cost | Standardized interfaces / exportable data / periodic competitive review |
| **Slide architecture** | Only pretty diagrams, no detailed design or interface defs | Architecture rebuilt in dev | Design must descend to interface & data-model level |

---

> **Relationship to SKILL.md**: SKILL.md is the knowledge reference (the "what"); this playbook is the execution guide (the "how"). During architecture design, match patterns against the architecture patterns in Part 10 of SKILL.md, and use this playbook's phased flow to advance systematically.
