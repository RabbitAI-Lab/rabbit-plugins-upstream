# 03-Data and Technology Architecture Design Workflow

## I. Workflow Overview

```
+-----------------------------------------------------------------------------+
|              Data & Technology Architecture Design Workflow              |
+-----------------------------------------------------------------------------+
|                                                                             |
|  +----------+   +----------+   +----------+   +----------+                  |
|  |1. Data    |-->|2. Lake & |-->|3. Tech   |-->|4. Tech   |               |
|  |  Arch.    |   |  Warehouse|   |  Selection|   |  Platform |               |
|  |  Landscape|   |  Design  |   |  & Eval. |   |  Design  |               |
|  +----------+   +----------+   +----------+   +----------+                  |
|       |              |              |              |                        |
|       v              v              v              v                        |
|  +----------+   +----------+   +----------+   +----------+                  |
|  |5. Integrat|-->|6. Tech    |-->|7. Security|-->|8. Arch.  |             |
|  |  ion Arch.|   |  Sovereignty|  |  Arch.   |   |  Review  |              |
|  |  Detail   |   |  & Compl. |   |  Design  |   |  & Base  |              |
|  +----------+   +----------+   +----------+   +----------+                  |
|                                                                             |
|  Stack covers: Data | App | Integration | IoT | AI | Security | Sovereignty|
+-----------------------------------------------------------------------------+
```

## II. Applicable Scenarios

This workflow applies to the complete design of the client's **Data Architecture** (data resources → data lake → data warehouse → data marts → data services) and **Technology Architecture** (stack selection, platform architecture, integration architecture, deployment architecture, security architecture).

## III. Prerequisites and Inputs

| Input | Source | Description |
|-------|------|------|
| Business Requirements Document (BRD) | Phase 02-02 | Business scenarios & needs |
| IT systems inventory report | Phase 02-03 | Existing systems & data state |
| Application-architecture design | Phase 03-02 | App modules & interactions |
| National / sector technical standards | Standards | ISO / IEEE / SAE / NTCIP / DATEX II etc. |

---

## IV. Detailed Steps

---

### Step 1: Data-Architecture Landscape Design

**Goal**: Design the full-lifecycle data-architecture landscape.

**Inputs**: Business needs, application architecture, data current state
**Outputs**: Data-architecture landscape, data-domain split, data-flow diagram

**Guidance:**

**1.1 Data-architecture landscape model**

```
Smart-mobility data-architecture landscape:

+-----------------------------------------------------------------+
|                         Data Consumption Layer                   |
|  +--------+ +--------+ +--------+ +--------+                    |
|  |Exec    | |Business| |AI      | |Data    |                    |
|  |cockpit | |reports | |decision| |sharing |                    |
|  |        | |        | |        | |(agency/|                    |
|  |        | |        | |        | |3rd party)|                  |
|  +--------+ +--------+ +--------+ +--------+                    |
+-----------------------------------------------------------------+
|                         Data Service Layer                       |
|  +-------------------------------------------------------+      |
|  |          Unified Data Service (API Gateway)           |      |
|  |  +--------+ +--------+ +--------+ +--------+          |      |
|  |  |Query   | |Analytic| |Push    | |Subscribe|         |      |
|  |  +--------+ +--------+ +--------+ +--------+          |      |
|  +-------------------------------------------------------+      |
+-----------------------------------------------------------------+
|                         Data Compute Layer                       |
|  +-------------------------------------------------------+      |
|  |       Data Lake + Data Warehouse (DW)                 |      |
|  |  +--------+ +--------+ +--------+                    |      |
|  |  | ODS    | | DWD    | | DWS    |                    |      |
|  |  | (source| | (clean | | (theme |                    |      |
|  |  |  raw)  | |  & int)| |  aggr) |                    |      |
|  |  +--------+ +--------+ +--------+                    |      |
|  |  +--------+ +--------+                              |      |
|  |  | ADS    | | DIM    |                              |      |
|  |  | (app   | | (dim   |                              |      |
|  |  |  metrics)|(data) |                              |      |
|  |  +--------+ +--------+                              |      |
|  +-------------------------------------------------------+      |
+-----------------------------------------------------------------+
|                         Data Collection Layer                    |
|  +--------+ +--------+ +--------+ +--------+                    |
|  |Device  | |System  | |File    | |Internet|                   |
|  |direct  | |interface| |import | |collect |                   |
|  |(IoT/vid)| |(API/DB)| |(CSV/Exc)| |(feed/sub|                 |
|  +--------+ +--------+ +--------+ +--------+                    |
+-----------------------------------------------------------------+
+-----------------------------------------------------------------+
|                         Data Governance Layer                    |
|  Standards | Metadata | Quality | Security                       |
|  Master-data | Lineage | Lifecycle | Asset catalog              |
+-----------------------------------------------------------------+
```

**1.2 Transport data-domain split**

| Domain | Sub-domain | Core entities |
|-------|------|-------------|
| Infrastructure | Road / bridge-tunnel / station / equipment | Section, bridge, tunnel, toll plaza, service area, camera, VMS |
| Operations monitoring | Flow / incident / environment | Flow, speed, occupancy, incident, weather |
| Toll operations | Tolling / split / audit | Transactions, ETC trades, split records, blacklist |
| Maintenance | Defect / repair / material | Defect records, work orders, plans, material use |
| Safety mgmt | Emergency / risk / accident | Contingency plans, resources, safety events, risk assessment |
| Traveler service | Travel / publish / inquiry | Road status, trip planning, hotline tickets |
| Enterprise mgmt | HR / finance / asset / project | Org, people, budget, contract, asset ledger |
| External data | Weather / map / sentiment | Weather forecast, POI, traffic sentiment |

**1.3 Data-flow diagram**

Use flow icons to show:
- Where data comes from (sources)
- What processing it passes (ETL / ELT)
- Where stored (lake / warehouse / mart)
- Who consumes (which apps / reports / AI models)

---

### Step 2: Data Lake & Warehouse Design

**Goal**: Design the layered data storage and compute architecture.

**Inputs**: Data-domain split, volume estimate, performance needs
**Outputs**: Lake-warehouse design, layered model, ETL / ELT design

**Guidance:**

**2.1 Layering principles**

| Layer | Name | Responsibility | Retention |
|------|------|------|---------|
| ODS | Source layer | Raw landing, source structure unchanged | As needed (3–12 mo) |
| DWD | Detail layer | Clean, standardize, light aggregation | 3–5 yr |
| DWS | Summary layer | Theme aggregation, pre-compute | 5–10 yr |
| ADS | App layer | App-oriented metric wide-tables | On demand |
| DIM | Dimension layer | Unified dimension data | Long-term |

**2.2 Transport-specific data models**

```
Core transport data models:

DWD_traffic_flow_detail:
  - Section ID, direction, lane
  - Time (5-min granularity)
  - Flow, speed, occupancy
  - Vehicle-type distribution
  - Source tag (microwave / video / ETC / probe)

DWD_incident_detail:
  - Incident ID, type (accident / congestion / work / weather / debris)
  - Detect / confirm / handle / recover time
  - Location (section + milepost + lat-lng)
  - Detection method (AI / manual / hotline)
  - Impact (queue length / delay)
  - Handling-record link

DWS_network_daily:
  - Section ID, date
  - Avg / peak flow, peak hour
  - Congestion index, duration, length
  - Incident count, publish count
  - YoY / MoM metrics

ADS_exec_cockpit:
  - Today's network-health index
  - This week's congestion-control result
  - This month's safety-score
```

**2.3 Real-time vs. batch channels**

| Channel | Tech | Latency | Scenario |
|------|------|:---:|---------|
| Real-time stream | Kafka + Flink / Spark Streaming | <1 s | Event alert, live dashboard, dynamic dispatch |
| Near-line | Spark Streaming | sec–min | Situational assessment, dynamic prediction |
| Offline batch | Spark / Hive on HDFS | hr–day | Daily / monthly reports, AI training, mining |

---

### Step 3: Technology Selection and Evaluation

**Goal**: Systematically evaluate and select the stack for each technology domain.

**Inputs**: Data architecture, application architecture, non-functional needs
**Outputs**: Tech-selection matrix, selection rationale report

**Guidance:**

**3.1 Full-stack selection framework**

```
Smart-mobility tech-stack framework:

+-----------------------------------------------------------------+
|  Frontend     |  Backend      |  Data         |  AI / Algorithms   |
|  ·Vue3/React  |  ·Java/Go     |  ·Hadoop/Spark| ·PyTorch / TF     |
|  ·GIS: Cesium|  ·Spring Cloud|  ·Flink/Kafka | ·CNN / YOLO        |
|  ·ECharts/D3  |  ·K8s+Docker  |  ·Doris/ClickH| ·NLP / LLM         |
|  ·Cross-platform| ·Nacos/Gateway| ·Hudi/Iceberg| ·MLOps            |
+-----------------------------------------------------------------+
|  IoT          |  Integration  |  Security      |  Sovereignty        |
|  ·EMQX        |  ·API Gateway |  ·WAF          |  ·Local OS         |
|  ·ThingsBoard |  ·ESB / MQ    |  ·IDS / IPS    |  ·Local RDBMS      |
|  ·Edge gateway|  ·ETL tools   |  ·Bastion host |  ·Local middleware  |
|  ·MQTT / CoAP |  ·Data-exchange|  ·Log/SIEM     |  ·Local CPU/cloud  |
+-----------------------------------------------------------------+
```

**3.2 Tech-selection evaluation matrix**

| Dimension | Weight | Description |
|------|:---:|------|
| Function fit | 25% | Match to requirements |
| Performance & scale | 20% | Throughput, concurrency, elasticity |
| Maturity & community | 15% | Product maturity, community, docs |
| Vendor support | 10% | Vendor capability, local service |
| Transport fit | 10% | Transport-sector case evidence |
| Sovereignty / compliance | 10% | Meets tech-sovereignty / local-content mandate |
| TCO | 10% | License + implementation + O&M |

**3.3 Transport key-selection points**

| Domain | Key tech | Consideration |
|------|---------|---------|
| GIS engine | Cesium / MapBox / Leaflet | 3D, mass road-network rendering, trajectory replay |
| Video AI | YOLO series + custom models | Transport-scene accuracy, inference speed, edge deploy |
| Stream compute | Flink | Windowing, CEP, state management |
| Time-series DB | TDengine / IoTDB / Druid | Mass device time-series ingest, downsampling |
| Graph DB | Neo4j / Nebula | Network-topology analysis, shortest path, correlation |
| Message queue | Kafka / Pulsar | Video & device-data throughput |

---

### Step 4: Technology-Platform Architecture Design

**Goal**: Design a unified tech platform supporting development, deployment, and operations.

**Inputs**: Tech selection, application architecture, deployment strategy
**Outputs**: Platform-architecture diagram, platform design spec

**Guidance:**

**4.1 Unified smart-mobility tech platform**

```
+-----------------------------------------------------------------+
|                      DevOps & Ops Layer                          |
|  CI/CD (Jenkins/GitLab) | Orchestration (K8s) | Monitor (Prom) |
|  Logs (ELK) | Tracing (SkyWalking) | Config (Nacos/Apollo)  |
+-----------------------------------------------------------------+
|                     Microservice Runtime Base                   |
|  Registry/discovery | API gateway | LB | Circuit-break | TX    |
+-----------------------------------------------------------------+
|                     Shared Service Layer                        |
|  SSO | Message center | File storage | Workflow engine | Reports |
+-----------------------------------------------------------------+
|                     Data & AI Platform                         |
|  Ingestion | Dev (ETL) | Governance | BI | Train/infer   |
+-----------------------------------------------------------------+
|                     IaaS / Cloud Platform                       |
|  Compute (bare/VM/K8s) | Storage (block/obj/file) | Network    |
+-----------------------------------------------------------------+
```

**4.2 Platform core-capability list**

| Capability domain | Core capability | Description |
|-------|---------|------|
| Dev framework | Scaffold, code generator | Efficiency & code standards |
| API mgmt | Design / gateway / docs / test | Full API lifecycle |
| Microservice gov. | Registry / route / limit / break | Stable microservices |
| Container platform | K8s cluster, image repo | Standard deploy & elastic scale |
| DevOps | CI/CD pipeline, quality gate | Auto build/test/deploy |
| Observability | Monitor / log / tracing | Health visibility & alerting |
| Data platform | Ingest / dev / govern / serve | One-stop data dev |
| AI platform | Sample / train / infer / monitor | Full AI-model lifecycle |

---

### Step 5: Integration-Architecture Detailed Design

**Goal**: Design the detailed technical solution for inter-system integration.

**Inputs**: Interaction matrix, existing interfaces, tech selection
**Outputs**: Integration-architecture design, interface spec, data-exchange standard

**Guidance:**

**5.1 Integration pattern selection**

| Pattern | Scenario | Implementation |
|---------|---------|---------|
| API sync call | Real-time query / action | REST / gRPC + API gateway |
| Async messaging | Event notify / data sync | Kafka / MQ |
| File exchange | Batch data exchange | SFTP + parser |
| DB sharing | Read-only access | Data virtualization / federation |
| ETL / ELT | Batch aggregation | DataX / SeaTunnel |

**5.2 Integration standards**

Must unify:
- API design (RESTful / naming / version / paging / error codes)
- Message format (header / body / serialization)
- Interface auth (OAuth 2.0 / JWT / API Key)
- Data format (JSON Schema / XML Schema)
- Error handling (retry / compensate / dead-letter)
- Interface docs (Swagger / OpenAPI 3.0)

---

### Step 6: Technology-Sovereignty and Compliance Design

**Goal**: Ensure the technology architecture meets technology-sovereignty (local-content) mandates and compliance standards.

**Inputs**: Tech selection, sovereignty policy, compliance requirements
**Outputs**: Sovereignty-adaptation plan, compliance matrix

**Guidance:**

**6.1 Sovereignty adoption roadmap**

```
Sovereignty adoption timeline:

Phase 1 (Yr 1–2): Office systems + non-core business systems
  - Office suite → sovereign office tools
  - Mail / conferencing → local solution

Phase 2 (Yr 2–3): Core business-system adaptation
  - Database → sovereign RDBMS
  - Middleware → sovereign middleware
  - OS → sovereign Linux distribution

Phase 3 (Yr 3–4): Full sovereignty
  - CPU → sovereign ARM / compatible processors
  - Cloud → sovereign / local cloud
  - Security products → sovereign security appliances
```

**6.2 Sovereignty-adaptation strategies**

| Strategy | Description | Scenario |
|------|------|---------|
| Greenfield | New system directly on sovereign stack | New systems |
| Parallel replace | Run old & new in parallel, then switch | Core systems |
| Refactor & migrate | Migrate existing system to sovereign platform | Systems with source code |
| Containerize | Containerize existing system on sovereign OS | Short-term transition |

---

### Step 7: Security-Architecture Design

**Goal**: Design a comprehensive cybersecurity architecture.

**Inputs**: Classification requirements, compliance, business-security needs
**Outputs**: Security-architecture diagram, security design

**Guidance:**

**7.1 Defense-in-depth security architecture**

```
Security architecture — defense-in-depth:

  Internet       DMZ            Core           OT zone
  +--------+    +--------+    +----------+    +----------+
  |CDN+WAF |    |Reverse |    |App server|    |PLC/RTU   |
  |DDoS    | →  |proxy   | →  |DB server| ←  |SCADA     |
  |DNS prot|    |WAF     |    |Big-data |    |Edge comp |
  +--------+    +--------+    +----------+    +----------+
       |             |              |               |
       +-------------+--------------+---------------+
                      |
              +---------------+
              | Security mgmt  |
              | SOC/SIEM/SOAR  |
              | Log/SIEM/bastion|
              | Vuln scan/pen   |
              +---------------+
```

**7.2 Security-capability list**

| Domain | Capability | Description |
|-------|---------|------|
| Perimeter | Firewall / WAF / IDS / IPS / DDoS | Boundary protection |
| Identity | SSO / MFA / zero-trust | Authn & access control |
| Data | Encryption / masking / classification | Data full-lifecycle security |
| App | Code review / WAF / API security | App-layer protection |
| Endpoint | EDR / NAC | Endpoint security |
| Security ops | SOC / SIEM / situational awareness | Monitoring & response |
| Crypto | FIPS / national-standard crypto / KMS | Compliant crypto |

---

### Step 8: Architecture Review and Baseline Release

**Goal**: Complete data & tech-architecture review and establish the architecture baseline.

**Inputs**: All architecture-design documents
**Outputs**: Review minutes, issued architecture baseline

**Guidance**: See [Phase 03 Step 2 (Business & Application Architecture)](../phase-03-strategy-and-top-level-design/02-business-and-application-architecture-workflow.md) Step 8.

---

## V. Roles and Responsibilities (RACI Matrix)

| Activity | Data architect | Tech architect | Security expert | Client IT | Sovereignty advisor |
|------|:---:|:---:|:---:|:---:|:---:|
| Data-arch landscape | **R/A** | C | C | C | I |
| Lake & warehouse | **R/A** | C | C | I | I |
| Tech selection | C | **R/A** | C | C | C |
| Tech platform | C | **R/A** | C | I | C |
| Integration arch | I | **R/A** | I | C | I |
| Sovereignty adapt | I | C | I | I | **R/A** |
| Security arch | I | C | **R/A** | I | I |
| Arch review | C | C | C | **R/A** | I |

---

## VI. Key Checkpoints

| # | Checkpoint | Pass criterion |
|---|--------|---------|
| CP1 | Data-domain split | All business data domains covered |
| CP2 | Data layering | ODS/DWD/DWS/ADS/DIM clear |
| CP3 | Tech-selection rationale | Each choice has complete eval matrix |
| CP4 | Platform completeness | DevOps / microsvc / data / AI covered |
| CP5 | Sovereignty plan feasible | Timeline & feasibility argued |
| CP6 | Security compliant | Meets classification Level-3 tech & mgmt |

---

## VII. Estimated Duration

| Type | Small | Medium | Large |
|---------|:---:|:---:|:---:|
| Data-arch design | 1 wk | 2–3 wks | 3–5 wks |
| Tech-arch design | 1 wk | 2–3 wks | 3–5 wks |
| Sovereignty & security | 0.5 wk | 1 wk | 1–2 wks |
| **Total** | **2.5 wks** | **5–7 wks** | **7–12 wks** |

---

## VIII. Common Pitfalls and Countermeasures

| # | Pitfall | Countermeasure |
|---|------|------|
| 1 | Chasing novel tech | Prefer mature, transport-proven tech |
| 2 | Data-arch ignores legacy | Design migration & bridge plans |
| 3 | Ignore sovereignty constraints on selection | Bring sovereignty expert early; consider in selection |
| 4 | Security as afterthought | Embed security throughout design, not a patch |
| 5 | Over-design hurts delivery | MVP principle: core arch first, layer capabilities |

---

## IX. Outputs List

1. **Data-architecture landscape** (.pptx)
2. **Data-domain split & data model** (.docx + .xlsx)
3. **Data lake-warehouse design** (.docx)
4. **Tech-selection evaluation matrix** (.xlsx)
5. **Tech-selection rationale report** (.docx)
6. **Tech-platform design spec** (.docx)
7. **Integration-architecture design** (.docx)
8. **Interface specification** (.docx + Swagger)
9. **Sovereignty-adaptation plan** (.docx)
10. **Security-architecture design** (.docx)
11. **Architecture review minutes** (.docx)

---

> **Version**: V1.0 | **Date**: 2025-07 | **Stack ref**: Hadoop ecosystem / Spring Cloud / K8s / sovereign products
