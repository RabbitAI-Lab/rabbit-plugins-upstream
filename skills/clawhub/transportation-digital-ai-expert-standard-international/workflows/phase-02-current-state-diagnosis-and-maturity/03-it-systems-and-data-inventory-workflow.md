# 03-IT Systems and Data Inventory Workflow

## I. Workflow Overview

```
+-----------------------------------------------------------------------------+
|                  IT Systems & Data Inventory Workflow                       |
+-----------------------------------------------------------------------------+
|                                                                             |
|  +----------+   +----------+   +----------+   +----------+                  |
|  |1. Inventory|-->|2. System |-->|3. Interface|-->|4. Data    |           |
|  |  Planning|   |  Asset    |   |  Relation |   |  Quality  |             |
|  |  & Tools |   |  Inventory|   |  Mapping  |   |  Assessment|            |
|  +----------+   +----------+   +----------+   +----------+                  |
|       |              |              |              |                        |
|       v              v              v              v                        |
|  +----------+   +----------+   +----------+   +----------+                  |
|  |5. Infra  |-->|6. Security|-->|7. Inventory|-->|8. Improve-|            |
|  |  Assess  |   |  Assess  |   |  Report   |   |  ment &   |            |
|  |          |   |          |   |  Author   |   |  Present  |            |
|  +----------+   +----------+   +----------+   +----------+                  |
|                                                                             |
|  Dimensions: Applications | Data | Interfaces | Infrastructure | Security | Ops |
+-----------------------------------------------------------------------------+
```

## II. Applicable Scenarios

This workflow applies to a comprehensive inventory of a transport-sector client's IT system assets, data resources, technical infrastructure, and cybersecurity current state, providing baseline information for subsequent architecture design, system integration, and modernization.

## III. Prerequisites and Inputs

| Input | Source | Description |
|-------|------|------|
| Contract / SOW | Project initiation docs | Inventory scope & requirements |
| Client IT contacts | Client | Liaison info |
| System / network / data policies | Client | Existing standards |
| Inventory toolset | Tech team | Scan / detect / analysis tools |

---

## IV. Detailed Steps

---

### Step 1: Inventory Planning and Tool Preparation (1–2 days)

**Goal**: Set the inventory plan and prepare tools and templates.

**Inputs**: Project scope, client IT org info
**Outputs**: Inventory plan, checklist templates, tool-deployment confirmation

**Guidance:**

**1.1 Six-dimension inventory checklist**

```
IT current-state inventory — six dimensions:

  Applications (App)          Data Resources (Data)
  ┌──────────────┐    ┌──────────────┐
  │·System list   │    │·Data catalog  │
  │·Function list │    │·Data volume   │
  │·Tech stack    │    │·Data standards│
  │·Usage         │    │·Data quality  │
  │·Vendor info   │    │·Data flow     │
  │·Ops status    │    │·Data assets   │
  └──────┬───────┘    └──────┬───────┘
        │                   │
   ┌────┴───────────────────┴────┐
   │        IT Inventory          │
   └────┬───────────────────┬────┘
        │                   │
 ┌──────┴───────┐    ┌──────┴───────┐
 │·Server list   │    │·Cybersecurity │
 │·Network topo  │    │·Data security │
 │·Cloud resources│   │·Classification│
 │·Storage        │   │·Security incidents│
 │·Middleware     │   │·Security policy│
 │·Data-center    │   │·Incident response│
 └──────────────┘    └──────────────┘
 Infrastructure (Infra)    Security (Security)

 Interface Integration (API)   Ops Capability (Ops)
 ┌──────────────┐    ┌──────────────┐
 │·System interfaces│  │·Ops team      │
 │·Data exchange   │  │·Monitoring    │
 │·Interface tech  │  │·Ops process   │
 │·Integration arch│  │·DR capability │
 │·External systems│  │·SLA level     │
 └──────────────┘    └──────────────┘
```

**1.2 Inventory method selection**

| Method | Scenario | Pros | Cons |
|---------|---------|------|------|
| Document review | Mature IT docs | Non-intrusive, comprehensive | May be outdated |
| Interview | Background & usage | Deep info | Subjective, slow |
| System demo | Functions & UI | Intuitive | Surface only |
| Auto scan | Network / host / DB | Objective, comprehensive | May affect business |
| Code review | Core-system source analysis | Deep technical detail | Needs source access |
| Log analysis | Runtime state | Real-data based | Needs log access |

---

### Step 2: System Asset Inventory

**Goal**: Build a complete client IT-system list, recording each system's key attributes.

**Inputs**: Inventory template, client IT cooperation
**Outputs**: System asset list, system evaluation matrix

**Guidance:**

**2.1 System asset registration template**

| Attribute | Description | Example |
|------|------|------|
| System ID | Unique ID | SYS-001 |
| System name | Formal name | Motorway Tolling Management System |
| Business domain | Domain | Toll operations |
| Builder | Dev / integrator | XX Technology Co. |
| Build year | First go-live year | 2018 |
| Last update | Last major version | 2022-Q3 |
| Architecture | B/S / C/S / hybrid | B/S |
| Language | Main language | Java |
| Database | DB type & version | Oracle 12c |
| OS | Deployment OS | CentOS 7 |
| Deployment | Physical / VM / container / cloud | VM |
| Users | Active users | ~500 |
| Data volume | Cumulative | ~2 TB |
| Integrated systems | Connected systems | Monitoring, ETC system |
| Ops status | Normal / partial fault / retired | Normal |
| Vendor status | Still cooperating? | Terminated |
| Source-code availability | Hold source? | Partial |
| Tech-debt assessment | 1–5 (1 good, 5 severe) | 3 |
| Security level | Classification rating | Level 2 |

**2.2 Typical transport-system catalog (reference)**

```
Transport system categories (reference):

I. Network operations monitoring
  □ Traffic-flow monitoring system
  □ Video-surveillance platform
  □ Incident-detection system
  □ Weather-monitoring system
  □ Bridge / tunnel structural-health monitoring
  □ Network-status assessment system

II. Emergency command & dispatch
  □ Emergency command platform
  □ Video-conference system
  □ Emergency-resource management
  □ Contingency-plan management
  □ GIS common-operating-picture

III. Maintenance management
  □ Maintenance management system
  □ Pavement management system (PMS)
  □ Bridge management system (BMS)
  □ Daily-inspection system
  □ Maintenance decision-support

IV. Tolling operations
  □ ETC (electronic toll collection) system
  □ MTC (manual toll collection) system
  □ Tolling-split & settlement system
  □ Toll-audit system
  □ Lane-control system

V. Traveler services
  □ Public travel-service platform
  □ Variable-message-sign (VMS) publishing
  □ Service / hotline system
  □ Social-media publishing

VI. General management
  □ OA / office system
  □ Finance / ERP system
  □ HR system
  □ Asset / equipment management
  □ Project / engineering management
  □ Records management
```

**2.3 Five-dimension system scoring**

Score each system on 5 dimensions (1–5):

| Dimension | Scoring |
|------|---------|
| Business support | Adequacy of support to current business |
| Tech advancement | Stack modernity, nearing EOL? |
| Maintainability | Source / docs / vendor support |
| Extensibility | Ease of extending function & performance |
| Security & compliance | Meets current security & compliance |

**Composite health = average of five.**

- Health ≥ 4: healthy, keep
- Health 3–3.9: optimize, upgrade when opportune
- Health 2–2.9: refurbish, include in modernization plan
- Health < 2: replace, add to retirement list

---

### Step 3: Interface Relationship Mapping

**Goal**: Clarify inter-system interfaces and data exchange, draw the integration current-state diagram.

**Inputs**: System asset list, tech-team interviews
**Outputs**: Interface list, integration current-state diagram, interface-issue log

**Guidance:**

**3.1 Interface registration template**

| Attribute | Description |
|------|------|
| Interface ID | INTF-001 |
| Source system | Tolling management system |
| Target system | Toll settlement system |
| Type | Upload / push / real-time query / file exchange |
| Transport | API / message queue / file / DB direct-connect |
| Trigger | Scheduled / event / manual |
| Protocol | HTTP / REST / SOAP / TCP / FTP |
| Data format | JSON / XML / CSV / custom |
| Frequency | Real-time / hourly / daily |
| Bidirectional | Yes / No |
| Reliability | High / medium / low |
| Monitoring | Monitored / not |

**3.2 Integration diagram**

Recommended format:
```
┌──────────┐  HTTP/JSON  ┌──────────┐
│ Tolling  │───────────>│ Settlement│
└──────────┘             └──────────┘
      │
      │ DB direct-connect (not recommended)
      v
┌──────────┐
│ Reporting │
└──────────┘
```

**3.3 Integration issue checklist**

| Issue type | Symptom | Impact |
|---------|------|------|
| Point-to-point | Direct calls, no middleware | High coupling, hard to manage |
| Data inconsistency | Same data differs across systems | Wrong decisions |
| No interface monitoring | Failures unnoticed | Data loss |
| Missing docs | No / outdated interface docs | Hard maintenance |
| Performance bottleneck | Bulk transfer hurts business | System lag |
| Security risk | Cleartext / no auth | Data leakage |

---

### Step 4: Data Quality Assessment

**Goal**: Assess the client's data resources and data-quality current state.

**Inputs**: System asset list, data dictionary, data samples
**Outputs**: Data-resource list, data-quality report, data-issue register

**Guidance:**

**4.1 Data-resource inventory dimensions**

| Dimension | Content |
|------|---------|
| Data catalog | Which datasets / DBs / tables |
| Data standards | Unified data standards & coding specs? |
| Data volume | Per-system volume (GB/TB/PB) |
| Master-data mgmt | How core master data (org / people / equipment / road sections) managed |
| Metadata mgmt | Metadata system or docs? |

**4.2 Data-quality six-dimension assessment**

```
Data-quality model:

  Completeness
  Is data complete, what is the missing rate?
  ┌─────────┐
  │         │  Consistency
  │  Data   │  Same data consistent across systems?
  │  Quality├── Accuracy
  │         │  Data accurately reflects reality?
  │         ├── Timeliness
  │         │  Update latency meets business need?
  └─────────┘
  Uniqueness            Validity
  Duplicate records?    Format conforms to spec?
```

**4.3 Data-quality sampling method**

| Item | Method | Sample |
|-------|------|:---:|
| Completeness | Null-rate per field | Full |
| Consistency | Cross-system key-field compare | 100–200 rows |
| Accuracy | vs. reality / third-party data | 50–100 rows |
| Timeliness | Check update-lag vs. business time | Full / time window |
| Uniqueness | Check PK / business-key duplicates | Full |
| Validity | Regex / dictionary validation | 100–200 rows |

**4.4 Data-quality issue severity**

| Level | Standard | Handling |
|:---:|------|---------|
| P0-Critical | Affects core decisions or safety | Fix immediately |
| P1-Major | Clearly affects analytics or process | Fix within 1 week |
| P2-Moderate | Minor / local issue | Fix this month |
| P3-Minor | No usage impact, format polish | Into iteration |

---

### Step 5: Infrastructure Assessment

**Goal**: Assess the client's IT-infrastructure current state and capability.

**Inputs**: Infrastructure list, network topology, monitoring data
**Outputs**: Infrastructure report, capacity analysis, risk list

**Guidance:**

**5.1 Infrastructure assessment checklist**

| Category | Items | Focus |
|------|-------|-------|
| Compute | Server count, spec, virtualization rate | Headroom, aging, cloud level |
| Storage | Type, capacity, utilization | Performance, scalability, backup |
| Network | Bandwidth, topology, redundancy | Backbone BW, internal/external isolation, remote access |
| Cloud | Using cloud? provider? volume? | Cloud-native, hybrid-cloud mgmt |
| Data center | Tier, power, cooling, physical security | Meets classification requirements |
| Monitoring | Coverage, alerting | Unified monitoring? |

**5.2 Transport-specific infrastructure focus**

| Focus | Description |
|-------|------|
| Field devices | Networking & power of cameras, VMS, detectors, weather stations |
| Communications | Corridor comms network (industrial Ethernet / PTN / OTN) health |
| IoT platform | IoT device-mgmt platform, terminal onboarding |
| Video resources | Storage capacity, analytics GPU, video-networking standard (e.g., ONVIF Profile / ISO 30143) |
| Edge computing | Edge nodes at toll plazas / corridor |
| V2X | RSU, MEC and other V2X-infrastructure deployment |

---

### Step 6: Security Current-State Assessment

**Goal**: Assess the client's information-security state and identify risks.

**Inputs**: Security policies, classification assessment report, incident logs
**Outputs**: Security report, risk list, compliance-gap analysis

**Guidance:**

**6.1 Security assessment dimensions**

| Dimension | Content | Method |
|------|---------|------|
| Security mgmt | Policy, org, people | Doc review + interview |
| Physical security | Data-center, equipment protection | On-site check |
| Network security | Firewall, WAF, IDS/IPS, VPN | Doc review + scan |
| Host security | Server config, patch mgmt | Scan + sampling |
| App security | Web / API / mobile security | Pen-test (authorized) |
| Data security | Encryption, masking, backup, classification | Doc review + sampling |
| Compliance | Classification rating, assessment, remediation | Doc review |

**6.2 Transport-specific security focus**

- Tolling-data security (involves fund settlement)
- Video-surveillance security (public safety & personal privacy)
- Industrial control system (ICS / SCADA) security (field-device control)
- V2X communication security (V2X security-certificate framework)
- Critical-infrastructure (CII) identification & protection

---

### Step 7: Inventory Report Authoring

**Goal**: Consolidate findings into a comprehensive, clear IT inventory report.

**Inputs**: All inventory results
**Outputs**: IT inventory report

**Guidance:**

**7.1 Report structure**

```
IT Inventory Report contents:

1. Executive summary (2–3 pages)

2. Inventory overview
   - Goals & scope
   - Method & process
   - People & timing

3. Application systems
   - Full system-asset list
   - System-health matrix
   - Tech-stack distribution
   - Vendor distribution

4. Data current state
   - Data-resource list
   - Data-quality assessment
   - Standards & governance
   - Data-security issues

5. Interfaces & integration
   - Interface list
   - Integration diagram
   - Integration issues

6. Infrastructure
   - Resource list & capacity
   - Network topology & bandwidth
   - Cloud state

7. Information security
   - Security policy
   - Security controls
   - Classification-compliance state
   - Key risk list

8. Ops capability
   - Ops team & process
   - Monitoring & alerting
   - DR & emergency

9. Synthesis & recommendations
   - Overall conclusion
   - Top 10 core issues
   - Improvement-priority suggestions
```

---

### Step 8: Improvement Recommendations and Presentation

**Goal**: Propose practical improvements from findings and present to the client.

**Inputs**: Inventory report
**Outputs**: Improvement plan, presentation deck, client feedback

**Guidance:**

**8.1 Improvement tiers**

| Tier | Horizon | Example |
|------|:---:|---------|
| Emergency fix | ≤1 month | High-risk vuln fix, key-interface monitoring |
| Short-term opt. | 1–3 mo | Retired-system data migration, data-quality campaign |
| Mid-term refurb. | 3–12 mo | Legacy-system replacement / upgrade, network re-arch |
| Long-term plan | 1–3 yr | Full cloudification, microservices, data-platform build |

**8.2 Presentation notes**
- Separate "urgent issues" from "optimization suggestions"
- Quantify impact (business / efficiency loss / security risk)
- Attach rough effort estimate per suggestion
- Avoid over-criticizing the status quo; frame as "building on a strong base"

---

## V. Roles and Responsibilities (RACI Matrix)

| Activity | Tech assessor | PM | Client IT | Client business | Security expert |
|------|:---:|:---:|:---:|:---:|:---:|
| Inventory planning | **R/A** | C | C | I | C |
| System inventory | **R** | I | C | C | I |
| Interface analysis | **R** | I | C | I | I |
| Data-quality assessment | **R** | I | C | C | I |
| Infrastructure assessment | **R** | I | C | I | I |
| Security assessment | C | I | C | I | **R/A** |
| Report authoring | **R/A** | C | I | I | C |
| Results presentation | C | **R/A** | C | I | I |

---

## VI. Key Checkpoints

| # | Checkpoint | Pass criterion |
|---|--------|---------|
| CP1 | Plan approval | Client agrees scope & plan |
| CP2 | System-list completeness | 100% of in-use systems registered |
| CP3 | Data sampling complete | >80% of core tables covered |
| CP4 | Interface docs collected | >90% of key-system interfaces registered |
| CP5 | Security scan complete | Risk list output |
| CP6 | Internal report review | Passed |

---

## VII. Estimated Duration

| Client scale | Duration | Team |
|---------|:---:|---------|
| Small (<20 systems) | 1–2 wks | 2–3 |
| Medium (20–50) | 2–4 wks | 3–5 |
| Large (>50) | 4–8 wks | 5–8 |

---

## VIII. Common Pitfalls and Countermeasures

| # | Pitfall | Countermeasure |
|---|------|------|
| 1 | Client withholds system access | Use demo + screenshots; note "not deeply assessed due to access limits" |
| 2 | Client hides systems | Cross-confirm via multiple channels (business + IT interview + network scan) |
| 3 | Too technical for client | Tiered output: technical report to IT, exec summary to decision makers |
| 4 | Scan triggers security alerts | Pre-notice, run in window, use non-intrusive methods |
| 5 | Subjective judgement over objective | Quantify with data; label subjective as "interview-based" |

---

## IX. Outputs List

1. **IT system-asset list** (.xlsx)
2. **System-health matrix** (.xlsx)
3. **Interface & integration diagram** (.pptx / Visio)
4. **Data-resource list** (.xlsx)
5. **Data-quality assessment report** (.docx)
6. **Infrastructure assessment report** (.docx)
7. **Security current-state report** (.docx)
8. **IT inventory master report** (.docx + .pptx)

---

> **Version**: V1.0 | **Date**: 2025-07 | **Applies to**: Comprehensive IT inventory for transport-sector clients
