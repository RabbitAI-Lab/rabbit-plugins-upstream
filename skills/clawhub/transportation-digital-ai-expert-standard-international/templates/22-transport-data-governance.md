# Transport Data Governance Plan

> **Version**: V1.0
> **Date**: ____ / __ / __
> **Prepared by**: _________
> **Reviewed by**: _________
> **Approved by**: _________

---

## Executive Summary

### Project Positioning
The [Agency / City Name] Transport Data Governance Programme establishes a governance system characterized by "unified standards, trusted quality, secured data, and efficient service". It transforms transport data from a "burden" into an "asset" that underpins digital transformation and intelligent upgrading.

### Objectives
By [Target Year], achieve:
- Data aggregation rate: core business systems aggregated ≥ ____%
- Data quality pass rate: composite 6-dimension quality score > ____
- Standardization: share of standardized data items > ____%
- Data sharing: internal sharing average response time < ____ days
- Data assetization: ____ data asset classes entitled & valued
- Data security: data security incidents = 0

### Investment Overview
| Item | Value |
|------|------|
| Total estimated investment | $____ million |
| Construction period | ____ months |
| Annual data operating cost | $____ million / year |

---

## 1. Current State Assessment

### 1.1 Data Asset Inventory
| No. | Data domain | Content | Volume | Format | Frequency | Source system | Data owner | Quality (1–5) |
|:---:|--------|----------|:------:|----------|:--------:|----------|:---------:|:-----------:|
| 1 | Road operations | Flow / speed / occupancy / congestion index | __ / day | Structured | 5 min | | | |
| 2 | Signal control | Timing plans / detector data / logs | __ / day | Structured | Real-time | | | |
| 3 | ANPR / enforcement | Passage / plate / speed / violations | __ / day | Semi-structured | Real-time | | | |
| 4 | Bus | GPS / smart card / dispatch / network | __ / day | Structured | Real-time | | | |
| 5 | Metro / rail | AFC / ridership / operations / assets | __ / day | Structured | Real-time | | | |
| 6 | Taxi / ride-hail | GPS trajectory / orders / fare | __ / day | Structured | Real-time | | | |
| 7 | Parking | Spaces / payment / entry-exit | __ / day | Structured | Near-real-time | | | |
| 8 | Crash / violation | Crash / violation records | __ / day | Structured | Daily | | | |
| 9 | Video | Surveillance streams / images | __ TB / day | Unstructured | Real-time | | | |
| 10 | GIS / map | Network / POI / interest points | __ GB | Vector / raster | Quarterly | | | |
| 11 | ... | | | | | | | |

### 1.2 Data Problem Diagnosis
| Problem | Symptom | Impact | Severity |
|----------|----------|------|:--------:|
| Inconsistent standards | Same junction coded differently across systems | Data cannot be linked | High |
| Poor quality | GPS drift / detector faults cause missing / wrong data | Inaccurate analysis | High |
| Data silos | Traffic-police / transport / bus / municipal data isolated | No integrated analysis | High |
| Missing data dictionary | Many field meanings unclear, unexplained | Data unusable | Medium |
| Missing history | Historical data not archived or lost | No trend analysis | Medium |
| Security risk | Sensitive data (face / plate / trajectory) not masked | Compliance risk | High |
| Difficult sharing | Cross-agency data requests complex, slow | Low collaboration efficiency | Medium |

### 1.3 Data Management Maturity Assessment
| Dimension | Current (1–5) | Benchmark | Gap |
|----------|:-----------:|:------:|----------|
| Data strategy & organization | | 5 | |
| Data standards management | | 5 | |
| Data quality management | | 4 | |
| Data architecture management | | 4 | |
| Data security management | | 5 | |
| Data sharing & service | | 4 | |
| Data asset management | | 3 | |

---

## 2. Data Governance Framework

### 2.1 Overall Framework (aligned to DAMA / DMBOK)
```
                    ┌─────────────────────────────┐
                    │     Data Governance Board     │
                    │   (strategy / resources / review)│
                    └─────────────┬───────────────┘
                                  │
    ┌──────────┬─────────┬───────┼────────┬──────────┬──────────┐
    │          │         │       │        │          │          │
┌───┴───┐ ┌───┴───┐ ┌──┴──┐ ┌─┴──┐ ┌──┴───┐ ┌──┴───┐ ┌──┴──────┐
│Data   │ │Data   │ │Data │ │Data│ │Data  │ │Data  │ │Data     │
│Stand. │ │Qual.  │ │Arch.│ │Sec.│ │Meta. │ │Master│ │Sharing  │
│Mgmt   │ │Mgmt   │ │Mgmt │ │Mgmt│ │Mgmt  │ │Data  │ │& Service│
└───────┘ └───────┘ └─────┘ └────┘ └──────┘ └──────┘ └─────────┘
    │          │         │       │        │          │          │
    └──────────┴─────────┴───────┼────────┴──────────┴──────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │   Full Lifecycle Management  │
                    │ create→collect→store→process │
                    │ →analyze→share→archive→destroy│
                    └───────────────────────────┘
```

### 2.2 Governance Principles
| Principle | Explanation |
|------|------|
| Business-driven | Governance serves business needs; not governance for its own sake |
| Standards first | Define standards before building systems; avoid "pollute-then-clean" |
| Source governance | Manage quality at the point of generation |
| Continuous improvement | Not a one-off project but an ongoing operation |
| Secure & compliant | Strictly comply with GDPR / EU data strategy / NIS2 / IEC 62443 |
| Value-oriented | Ultimate goal is releasing data value |

---

## 3. Detailed Design

### 3.1 Data Architecture

#### 3.1.1 Layered Data Architecture
```
┌──────────────────────────────────────────────────────────────┐
│  ADS (Application Data Service Layer)                         │
│  Themed data for business apps: congestion / safety / bus /   │
│  parking analytics; BI datasets / API services / data products│
├──────────────────────────────────────────────────────────────┤
│  DWS (Data Warehouse Summary Layer)                           │
│  Lightly summarized common-dimension data: hourly / daily /   │
│  weekly / monthly by theme: flow / safety / bus / parking     │
├──────────────────────────────────────────────────────────────┤
│  DWD (Detail Data Layer)                                      │
│  Cleaned / standardized / linked business detail data         │
│  Unified dimensions (time / space / device / vehicle / person)│
├──────────────────────────────────────────────────────────────┤
│  ODS (Operational Data Store Layer)                           │
│  1:1 raw mirror, no cleaning; full raw trace retained         │
├──────────────────────────────────────────────────────────────┤
│  Ingestion Layer                                              │
│  Kafka real-time stream + batch (Airflow / Flink CDC) + API   │
│  + file                                                       │
└──────────────────────────────────────────────────────────────┘
```

#### 3.1.2 Data Lake / Warehouse Technology Selection
| Component | Recommended | Alternative | Compliance fit | Function |
|----------|----------|------|:--------:|------|
| Real-time messaging | Kafka | Pulsar | Open source / neutral | Real-time ingestion |
| Batch ETL | Airflow / Flink CDC | NiFi | Open source / neutral | Batch ingestion |
| Stream compute | Flink / Spark Streaming | Storm | Open source / neutral | Real-time processing |
| Batch compute | Spark / Hive on Tez | MapReduce | Open source / neutral | Offline processing |
| Lake storage | S3 / ADLS / MinIO | HDFS | Cloud / neutral | Data storage |
| Warehouse | Snowflake / BigQuery / ClickHouse / StarRocks | Redshift | Cloud / neutral | OLAP query |
| Metadata | DataHub / Atlas | Amundsen | Open source / neutral | Metadata |
| Scheduler | Airflow / DolphinScheduler | Azkaban | Open source / neutral | Orchestration |
| Data quality | Great Expectations / Griffin | Deequ | Open source / neutral | Quality monitoring |

### 3.2 Data Standards

#### 3.2.1 Standards System
| Category | Content | Example | Reference |
|----------|----------|------|------|
| Naming | DB / table / field / index naming rules | `dwd_traffic_flow_5min` | Project spec |
| Coding | Unified coding for junction / segment / zone / device / vehicle | Junction ID = 6-digit area + 4-digit seq. | ISO 14825 / project spec |
| Data type | Unified date / time / lat-long / speed units | Time = ISO 8601 / lat-long = WGS84 | International |
| Interface | Data-exchange API / SDK / file format spec | RESTful + JSON / SFTP + CSV | ISO 20022 / project spec |
| Dictionary | Unified code tables (crash / violation / weather / pavement state) | Crash type: 01=rear-end 02=side… | ISO 14825 / project spec |
| Quality | Per-item quality rules: completeness / accuracy / timeliness / uniqueness | Flow completeness > 95% | Project spec |

#### 3.2.2 Unified Data Coding (example)
| Object | Rule | Length | Example |
|----------|----------|:---:|------|
| Junction | Area (6) + sequence (4) | 10 | 4403050001 |
| Segment | Road class (2) + sequence (6) + direction (1) | 9 | 010000011 |
| Detector | Junction code (10) + type (2) + sequence (2) | 14 | 4403050001LD01 |
| Bus route | Route type (2) + sequence (4) | 6 | 010001 |
| Bus stop | Area (6) + direction (1) + sequence (4) | 11 | 44030510001 |

### 3.3 Data Quality Management

#### 3.3.1 Six-Dimension Quality Assessment
| Dimension | Definition | Metric | Rule example |
|----------|------|----------|----------|
| Completeness | No missing data | Field fill rate / record completeness | 288 flow records / day (5-min) |
| Accuracy | Reflects reality | Deviation from truth / % | GPS drift filter (Δspeed > 50 km/h = anomaly) |
| Consistency | Consistent across sources | Cross-validation pass rate | ANPR vs. loop flow deviation < 15% |
| Timeliness | Arrives per agreed frequency | Arrival latency / frequency compliance | Real-time < 1 min, batch < 1 h |
| Uniqueness | No duplicates | Primary-key uniqueness / dup rate | No duplicate records at same detector+timestamp |
| Validity | Conforms to business rules | Format / range / enum / rule compliance | Speed in [0, 120] km/h |

#### 3.3.2 Quality Monitoring & Remediation
| Step | Measure | Tool / Method |
|------|------|----------|
| Prevention | Entry validation / sensor calibration / source-side checks | Front-end rules + device O&M |
| In-process monitor | Real-time quality monitor + auto-alert + ticket | Quality platform + rule engine |
| Remediation | Imputation / correction / dedup / consistency fix | Auto-scripts + manual review |
| Closed loop | Issue → detect → attribute → fix → verify → prevent → assess | Quality ticket + KB + KPI |

#### 3.3.3 Quality KPIs
| KPI | Target | Frequency | Owner |
|-----|:------:|:--------:|----------|
| Core data completeness | > 95% | Real-time | Source system owner |
| Core data accuracy | > 98% | Daily / Weekly | Source system owner |
| Timeliness compliance | > 99% | Real-time | Source + link |
| Duplicate rate | < 0.1% | Daily | Data platform |
| Remediation closed-loop rate | > 90% | Monthly | Governance team |

### 3.4 Metadata Management

#### 3.4.1 Metadata Classification
| Type | Content | Collection | User |
|-----------|------|----------|--------|
| Business metadata | Definition / meaning / calc. logic / owner / class / security level | Manual + AI assist | Business / analyst |
| Technical metadata | DB / table / field / ETL / lineage / volume / frequency / partition | Auto (DB / ETL) | Engineer / DBA |
| Operational metadata | Job logs / access logs / quality logs / flow records | Auto (scheduler / quality / gateway) | O&M / governance |

#### 3.4.2 Data Lineage
| Function | Explanation |
|------|------|
| Field-level lineage | End-to-end from source field → ODS → DWD → DWS → ADS → API output |
| Impact analysis | Upstream change → auto downstream impact analysis |
| Traceability | Report / API problem → trace back to source |
| Lineage visualization | DAG view of full data flow path |

### 3.5 Master Data Management

#### 3.5.1 Master Data Domains
| Domain | Content | Owner | Source | Consuming systems |
|----------|-----------|:---------:|----------|----------|
| Road network | Road / junction / segment / ramp / interchange | Planning authority | GIS | All transport systems |
| Devices | Signal / detector / VMS / CCTV / RSU / enforcement | Asset management | Asset system | Business systems |
| Bus route / stop | Route / stop / hub / depot / charger | Bus operator | Bus / metro system | Dispatch / info service |
| Vehicles | Bus / taxi / ride-hail / freight / official | Respective units | Vehicle system | Business systems |
| Persons | Drivers / operators / O&M | Respective units | HR / management | Safety / dispatch |
| Organizations | Police / transport / bus / municipal / data agency | Registry / units | Org management | Access / stats |
| Geo zones | Admin / traffic analysis zone / district / grid | Departments | Business systems | Stats / analysis |

#### 3.5.2 Master Data Functions
| Function | Explanation |
|------|------|
| Creation | Unified entry + unique code + required-field validation |
| Cleansing | Auto-identify duplicate / conflict + manual merge / arbitration |
| Distribution | On approval, auto-sync to subscribed downstream systems |
| Change | Request → approve → consistency check → distribute → version retained |
| Mapping | Cross-system code mapping (e.g., police junction ID vs. transport junction ID) |

### 3.6 Data Security & Classification

#### 3.6.1 Data Classification & Grading
| Level | Definition | Example | Protection |
|:--------:|------|----------|----------|
| L1 (Critical) | Leak harms public interest / critical infrastructure | Sensitive geospatial / critical routes / detailed CI data | Physical isolation + encryption + review |
| L2 (Important) | Leak harms important interests | Full ANPR passage / face / OD trajectory / signal timing | Encryption + masking + approval + review |
| L3 (Sensitive) | Contains personal information | Plate / face / identity / phone / payment | Masking / de-identification + authorization + minimization |
| L4 (Internal) | Internal use only | Flow stats / reports / O&M logs / design docs | Access control + leak prevention |
| L5 (Public) | Open to public | Real-time traffic / bus routes / parking spaces / index | Public API / download |

#### 3.6.2 Security Technical Measures
| Measure | Explanation | Technical solution |
|----------|------|----------|
| Access control | Fine-grained data access control | RBAC / ABAC + row / column level |
| Data masking | Dynamic / static masking | Plate (AB**·*1) / face (blur) / trajectory (300 m grid) / phone (masked) |
| Encryption | At rest + in transit | AES-256 / TLS 1.3 |
| Watermark | Traceability + leak tracking | Digital / blind watermark |
| Audit log | Full data-operation audit | Who + when + what + action + result |
| DLP | Abnormal access / download / transfer detection | DLP + UEBA |
| Privacy computing | Multi-party analysis without leaving domain | Federated learning / MPC / TEE |

#### 3.6.3 Compliance Requirements
| Regulation / Standard | Core requirement | Implementation |
|-----------|----------|----------|
| GDPR (EU) / applicable privacy law | Lawful basis / consent / minimization / purpose limit / erasure | Privacy notice + minimization + masking + erasure workflow |
| EU data strategy / national data act | Data classification / protection / important-data register / risk assessment | Classification + security assessment + important-data register |
| NIS2 / critical-infrastructure directive | CII protection | CII identification + security planning + controls |
| IEC 62443 | Industrial / OT security | Zone & conduit + security levels |
| Geo-spatial data regulation | Geospatial data compliance | Licensed basemap + no restricted-area capture |
| Sector data rules | Sector-specific data security | Face / plate / trajectory masking + no cross-border transfer |

### 3.7 Data Sharing & Service

#### 3.7.1 Sharing Platform
| Function | Explanation |
|------|------|
| Data catalog | Publish transport data asset catalog (name / class / fields / format / frequency / owner / level / terms) |
| API gateway | Unified API mgmt: auth / throttling / versioning / monitoring / billing |
| Request workflow | Online request → review (auto / manual) → authorize → use → revoke |
| Data sandbox | Safe environment providing masked data for external exploration |
| Service monitoring | API call volume / success / latency / anomaly monitoring |

#### 3.7.2 Sharing Tiers
| Tier | Audience | Scope | Approval | Charging |
|:--------:|------|----------|----------|:--------:|
| Unconditional | Public | L5 public data | None | Free |
| Inter-agency | Public-sector departments | L2–L4 masked | Data-sharing agreement + approval | Free |
| Conditional | Partners / researchers | L3–L4 masked / de-identified | Agreement + approval + commitment | May charge |
| Restricted | Case-by-case | L1–L2 (partly masked) | Senior approval + secure environment | Per-project |
| Not shared | — | L1 critical | — | — |

### 3.8 Data Assetization & Valuation

#### 3.8.1 Assetization Path
```
Data resource → entitlement → valuation → registration
    → accounting (where permitted) → trading / data products → operation
```

#### 3.8.2 Valuation Methods
| Method | Explanation | Use case |
|----------|------|----------|
| Cost | Cost of collection / governance / storage / O&M | Internal / accounting |
| Income | Discounted direct / indirect benefit | Commercial data products |
| Market | Reference comparable market prices | Traded data |
| Composite | Cost + income + market + scenario | External valuation / investment |

#### 3.8.3 Data Products
| Product | Content | Target user | Model |
|----------|------|----------|----------|
| Real-time traffic API | Congestion / speed / incident data | Nav / ride-hail / insurance / logistics | API subscription |
| Traffic index report | Monthly / quarterly / annual report + data | Planning / real estate / retail / consulting | Report sale |
| OD / footfall API | Zone / district / hub OD & footfall | Retail / advertising | API subscription |
| Parking data API | City-wide spaces / price / forecast | Parking app / OEM / insurer | API subscription |
| Safety assessment data | Risk score / blackspot / rating | Insurance / UBI / AV | Data license |
| Planning dataset | Historical volume / OD / trip characteristics | Design institutes / consultants | Dataset sale |

### 3.9 Data Operations

#### 3.9.1 Operational KPIs
| Dimension | Indicator | Target |
|----------|----------|:------:|
| Coverage | Core system ingestion rate | > 95% |
| Quality | Composite quality score | > 90 |
| Timeliness | Real-time latency compliance | > 99% |
| Sharing | Request approval time | < 3 business days |
| Security | Data security incidents | 0 |
| Usage | Monthly API calls | > ____ M |
| Value | Product revenue / savings | $____ M / yr |
| Satisfaction | Internal / external satisfaction | > 85 |

#### 3.9.2 Operating Cadence
| Cadence | Content | Frequency |
|------|------|:----:|
| Quality report | Per-domain / per-source quality + ranking | Weekly / Monthly |
| Governance board | Review progress / resolve cross-agency issues | Quarterly |
| Security review | Compliance review (access / log / masking / leak risk) | Semi-annual |
| Value assessment | Catalog update + valuation refresh | Annual |

---

## 4. Organization Design

### 4.1 Governance Organization
```
                     Data Governance Board
                  (decision: exec sponsor + dept heads)
                            │
              ┌─────────────┼─────────────┐
              │             │             │
         Data Mgmt      Data Tech      Data Security
         (business)    (IT)          (security / legal)
              │             │             │
    ┌─────────┼─────────┐   │   ┌─────────┼─────────┐
    │         │         │   │   │         │         │
  Data      Data       Data  │  Security  Compliance  Audit
  Owner     Steward    Steward│  Mgmt      Mgmt       Mgmt
  (biz)     (biz)      (IT)  │
```

### 4.2 Key Roles & Responsibilities
| Role | Position | Responsibility | Requirement |
|------|------|------|----------|
| Governance Board | Decision | Strategy / standards / major investment / coordination | Exec leadership |
| CDO | Execution lead | Overall governance / report to board | IT + business acumen |
| Data Owner (business) | Data sovereign | Ultimate responsibility for quality / security / sharing | Dept head |
| Data Steward (business) | Business execution | Business metadata / definitions / quality rules / sharing approval | Business expert |
| Data Steward (IT) | Technical execution | Technical metadata / architecture / quality / security impl. | Data engineer |
| Data Engineer | Technical execution | ETL / modeling / quality scripts / API | Big-data / warehouse |
| Data Security Officer | Security | Classification / policy / audit / compliance | Security background |
| Governance Specialist | Daily ops | Quality monitoring / tracking / report / training | Analysis / coordination |

### 4.3 Capability Building
| Audience | Content | Duration | Certification |
|----------|----------|:---:|:---:|
| Board / executives | Value / framework / practice / roles | Half-day | — |
| Owner / steward | Standards / quality / metadata / master / security | 2 days | Internal |
| Data engineer | Architecture / ETL / modeling / quality / lineage / API | 5 days | Internal |
| Analyst / user | Catalog / request / self-service / security | 1 day | — |

---

## 5. Implementation Roadmap

### 5.1 Strategy
| Principle | Explanation |
|------|------|
| Urgent first | Prioritize most critical, highest-use data (P0) |
| Use drives governance | Drive governance via a concrete scenario (congestion / safety) |
| Standards before quality | Unify standards before quality; avoid concurrent pollution |
| Inside before cross-agency | Link within one agency, then expand |
| Platform + process + org in parallel | Tech / process / capability three lines together |

### 5.2 Phased Implementation
| Phase | Time | Content | Milestone | Investment |
|------|------|------|--------|:----:|
| Phase 1 (Foundation) | ____ / __ – __ | Establish org + standards + data lake / warehouse + first 5–10 core domains + catalog 1.0 | Core data usable | $___ M |
| Phase 2 (Full rollout) | ____ / __ – __ | All domains + full quality monitoring + metadata + master + sharing platform + security grading | Fully compliant | $___ M |
| Phase 3 (Intelligent) | ____ / __ – __ | AI-assisted governance + auto lineage + valuation + productization + federated / privacy computing | Assetized operation | $___ M |

---

> **Usage note**: This template is for city / transport-agency / operator data governance plans. The core of data governance is "30% technology, 70% management, 120% organization" — the platform is only a vehicle; the real difficulty is cross-agency coordination and organizational change. Replace `[placeholder]` content with actual project data.

> **Legal notice**: This template is protected by copyright and related laws. It is provided for individual study and reference only; commercial use requires the author's written authorization.

> **Disclaimer**: This template is for study and reference only and does not constitute professional advice. Data governance involves GDPR / privacy-law compliance; obtain legal counsel during implementation. The author accepts no liability for any loss arising from the use of or reliance on this template.

> **Author**: yinjianheng | yinjianheng@foxmail.com
