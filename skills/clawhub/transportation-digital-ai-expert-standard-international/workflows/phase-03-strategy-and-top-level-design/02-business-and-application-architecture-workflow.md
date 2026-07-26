# 02-Business and Application Architecture Design Workflow

## I. Workflow Overview

```
+-----------------------------------------------------------------------------+
|            Business & Application Architecture Design Workflow             |
+-----------------------------------------------------------------------------+
|                                                                             |
|  +----------+   +----------+   +----------+   +----------+                  |
|  |1. Business|-->|2. Business|-->|3. App     |-->|4. App     |           |
|  |  Capability|  |  Process  |   |  Function |   |  Boundary |            |
|  |  Modeling |   |  Reengineer|   |  Define   |   |  & Inter. |            |
|  +----------+   +----------+   +----------+   +----------+                  |
|       |              |              |              |                        |
|       v              v              v              v                        |
|  +----------+   +----------+   +----------+   +----------+                  |
|  |5. App     |-->|6. Deploy |-->|7. Integr.|-->|8. Arch.   |             |
|  |  Arch.    |   |  View    |   |  Arch.   |   |  Review   |              |
|  |  Diagram  |   |          |   |  Design  |   |  & Release|             |
|  +----------+   +----------+   +----------+   +----------+                  |
|                                                                             |
|  Method: TOGAF ADM | CBM (Component Business Model) | DDD                    |
+-----------------------------------------------------------------------------+
```

## II. Applicable Scenarios

This workflow applies to the Business Architecture and Application Architecture design for transport-sector clients — the critical bridge connecting strategy to technical delivery.

## III. Prerequisites and Inputs

| Input | Source | Description |
|-------|------|------|
| Digital vision & strategic goals | Phase 03-01 | Strategy direction & KPIs |
| Business Requirements Document (BRD) | Phase 02-02 | Detailed business needs |
| IT systems inventory report | Phase 02-03 | Existing systems & interfaces |
| Gap-analysis report | Phase 02-04 | Opportunities & priorities |

---

## IV. Detailed Steps

---

### Step 1: Business Capability Modeling

**Goal**: Build the client's core business-capability model and identify capability areas needing digital enhancement.

**Inputs**: Strategic goals, BRD, industry best practice
**Outputs**: Business Capability Map

**Guidance:**

**1.1 Transport business-capability reference model (CBM L1)**

```
Transport business-capability reference model:

+-----------------------------------------------------------------------+
|                       Strategy & Management Layer                      |
|  +--------+ +--------+ +--------+ +--------+                          |
|  |Strategy| |Invest. | |Perf.   | |Industry|                          |
|  |planning| |mgmt    | |mgmt    | |research|                          |
|  +--------+ +--------+ +--------+ +--------+                          |
+-----------------------------------------------------------------------+
|                       Core Business Layer                              |
|  +--------+ +--------+ +--------+ +--------+                          |
|  |Network | |Emergen.| |Maint.  | |Toll   |                          |
|  |monitor | |command | |mgmt    | |ops    |                          |
|  +--------+ +--------+ +--------+ +--------+                          |
|  +--------+ +--------+ +--------+ +--------+                          |
|  |Travel  | |Asset   | |Project | |Safety  |                          |
|  |service | |mgmt    | |eng.    | |mgmt    |                          |
|  +--------+ +--------+ +--------+ +--------+                          |
+-----------------------------------------------------------------------+
|                       Support & Assurance Layer                         |
|  +--------+ +--------+ +--------+ +--------+                          |
|  |HR      | |Finance | |Procure| |Legal & |                          |
|  |        | |        | |ment    | |Compl.  |                          |
|  +--------+ +--------+ +--------+ +--------+                          |
+-----------------------------------------------------------------------+
```

**1.2 Business-capability heat map**

Two-dimension assessment per capability, generate heat map:

| Capability | Strategy support (1–5) | Current digital level (1–5) | Priority |
|---------|:---:|:---:|:---:|
| Network operations monitoring | 5 | 2 | **Top** |
| Emergency command & dispatch | 5 | 3 | **Top** |
| Maintenance management | 4 | 2 | Priority |
| Toll operations | 4 | 4 | Optimize |
| Traveler service | 3 | 2 | Mid-term |
| Asset management | 3 | 1 | Mid-term |
| Project engineering | 2 | 2 | Defer |
| ... | ... | ... | ... |

**Priority = Strategy support × (5 − current digital level)**

---

### Step 2: Business Process Mapping and Reengineering

**Goal**: Map core business processes and identify optimization / reengineering opportunities.

**Inputs**: Business-capability map, AS-IS processes from BRD
**Outputs**: TO-BE process design, process-optimization suggestions

**Guidance:**

**2.1 Process levels**

```
Process hierarchy:

Level 1: Value-chain process (Value Chain)
  e.g., "Network operations management" → 6 L2 processes

Level 2: Process area
  e.g., "Incident detection & handling" → 4 L3 processes

Level 3: Business sub-process
  e.g., "Automated traffic-incident detection" → 5 L4 steps

Level 4: Activity
  e.g., "Video AI analysis finds abnormal incident"
```

**2.2 TO-BE process design principles**

| Principle | Description |
|------|------|
| Data-driven | Decision points supported by data, not just experience |
| Automation-first | Automate steps where possible (RPA / AI) |
| Closed-loop | Process has start and end, forming PDCA loop |
| Clear roles | RACI per step |
| Exception handling | Branch paths for exceptions |

**2.3 Process-optimization patterns**

| Pattern | Description | Example |
|---------|------|------|
| Eliminate | Remove unnecessary steps | Drop paper sign-off |
| Simplify | Simplify complex steps | Auto-fill forms |
| Integrate | Merge scattered steps | SSO across systems |
| Automate | Tech replaces manual | AI auto-defect ID |
| Optimize | Redesign better path | Smart incident dispatch routing |

---

### Step 3: Application Function Definition

**Goal**: Based on process design, define the application functions and modules supporting each process.

**Inputs**: TO-BE processes, capability heat map
**Outputs**: Application-function list, module structure

**Guidance:**

**3.1 Application-function decomposition**

```
Capability → App module → Function point

Example:
Network ops monitoring (L1 capability)
├── Operations-monitoring module
│   ├── Real-time traffic-flow monitoring
│   ├── Congestion auto-alert
│   ├── Speed situational analysis
│   └── Network-health assessment
├── Video-AI-analysis module
│   ├── Abnormal-event detection (stopped/reverse/pedestrian/debris)
│   ├── Flow statistics & classification
│   ├── Adverse-weather recognition
│   └── Intelligent video patrol
├── Situational-awareness module
│   ├── Network common-operating-picture
│   ├── Multi-source data fusion
│   ├── Short-term prediction
│   └── Simulation & rehearsal
└── Alert-publishing module
    ├── VMS auto-publish
    ├── Navigation-app push
    ├── SMS / voice notification
    └── Alert-effectiveness evaluation
```

**3.2 Function-point description template**

```
Function-point card:

ID: FUN-MON-001
Name: Real-time traffic-flow monitoring
Module: Operations-monitoring
Background: Need real-time road traffic-flow & speed situational awareness
Description: Based on multi-source data (microwave / video / ETC / probe vehicle)
             show real-time network flow, render congestion as heat map,
             aggregate by road / direction / time
Input: Microwave, video detection, ETC gantry, probe-vehicle GPS
Process: Multi-source fusion → flow calc → speed estimate → congestion judge
Output: Real-time congestion heat map, flow/speed trend, congestion alert
Roles: Monitor, duty supervisor, info-center director
Precondition: Data sources connected, network GIS basemap configured
Postcondition: Data update frequency <1 min
Non-functional: Map render <2s, data latency <30s, 1000+ segments at once
Dependencies: GIS service, real-time data-ingest service
```

**3.3 Application-module prioritization**

Map from the capability heat map:
- High-priority capability → build-first modules
- Low-priority capability → later-iteration modules

---

### Step 4: Application Boundary and Interaction Definition

**Goal**: Define each application's boundary, responsibility, and interaction relationships.

**Inputs**: Application-function list, existing-system list
**Outputs**: Application-boundary definition, inter-system interaction matrix

**Guidance:**

**4.1 Boundary principles**

| Principle | Description |
|------|------|
| High cohesion | Related functions in one app |
| Low coupling | Minimize inter-app dependencies |
| Single responsibility | Clear, non-overlapping duty per app |
| Standardized interface | Apps interact via standard API |
| Data autonomy | App owns its data; share via API |

**4.2 Transport application-architecture reference model**

```
Smart-mobility application-architecture reference model:

+-----------------------------------------------------------------+
|                      User Interaction Layer                       |
|  +--------+ +--------+ +--------+ +--------------------+         |
|  |Video   | |PC work | |Mobile  | |Public-service app  |         |
|  |wall /  | |station | |app     | |(web / mini-program)|         |
|  |dashboard| |        | |        | |                    |         |
|  +--------+ +--------+ +--------+ +--------------------+         |
+-----------------------------------------------------------------+
|                      Business Application Layer                   |
|  +-------------------------------------------------------+       |
|  |      Smart-Mobility Business Middle Platform (microsvc)|       |
|  |  +--------+ +--------+ +--------+ +--------+          |       |
|  |  |Ops     | |Emerg.  | |Maint.  | |Toll    | ...    |       |
|  |  |monitor | |command | |mgmt    | |ops     |        |       |
|  |  |service | |service | |service | |service |        |       |
|  |  +--------+ +--------+ +--------+ +--------+          |       |
|  |  +--------+ +--------+ +--------+ +--------+          |       |
|  |  |Travel  | |Asset   | |Project | |Safety  | ...    |       |
|  |  |service | |mgmt    | |eng.    | |mgmt    |        |       |
|  |  +--------+ +--------+ +--------+ +--------+          |       |
|  +-------------------------------------------------------+       |
+-----------------------------------------------------------------+
|                      Shared Capability Layer                      |
|  +------+ +------+ +------+ +------+ +------+                    |
|  |User  | |Msg   | |GIS   | |Video | |AI    |                    |
|  |center| |center| |svc   | |svc   | |svc   |                    |
|  +------+ +------+ +------+ +------+ +------+                    |
|  +------+ +------+ +------+ +------+ +------+                    |
|  |Report| |Flow  | |Log   | |API   | |Config|                    |
|  |svc   | |engine| |svc   | |gateway| |center|                   |
|  +------+ +------+ +------+ +------+ +------+                    |
+-----------------------------------------------------------------+
```

**4.3 Application interaction matrix**

| | Ops monitor | Emerg. cmd | Maint. | Toll ops | GIS svc | AI svc |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| Ops monitor | - | Push event | Push defect | Query flow | Use basemap | Use ID |
| Emerg. cmd | Query situ | - | Dispatch res. | Query status | Use nav | Use predict |
| Maint. | Query road | Respond dispatch | - | - | Use locate | Use diagnose |
| Toll ops | Report flow | - | - | - | - | Use audit |

---

### Step 5: Application-Architecture Master Diagram

**Goal**: Draw the complete application-architecture master diagram, showing layers, module boundaries, and interactions.

**Inputs**: Function list, boundary def, interaction matrix
**Outputs**: Architecture master diagram, architecture description

**Guidance:**

**5.1 Diagram conventions**
- Clear layers: user interaction → business app → shared capability → data → infrastructure
- Color coding: new (green), refurbish (yellow), retain (blue), retire (red)
- Clear labels: system name, stack, deployment location
- Interface labels: main direction & protocol

**5.2 Architecture description should cover**
- Design principles
- Each layer's responsibility & composition
- Per-system summary
- Inter-system integration (with integration diagram)
- Connection strategy to existing systems
- Architecture evolution path

---

### Step 6: System Deployment View

**Goal**: Design the physical deployment plan for applications.

**Inputs**: Application-architecture design, infrastructure current state
**Outputs**: Deployment diagram, deployment description

**Guidance:**

**6.1 Deployment design elements**

| Element | Content |
|------|---------|
| Deployment env | Public / private / community cloud, hybrid |
| Network zones | Internet / DMZ / intranet / OT zone |
| HA | Cluster, load balancing, active-active |
| DR | Same-city / geo DR, RPO/RTO definition |
| Security domain | Domain split, east-west / north-south control |

**6.2 Transport deployment specifics**

- Field devices connect via OT network; need gap-firewall / firewall isolation
- Video streams demand high bandwidth; consider edge + cloud hybrid
- ETC / toll systems need dedicated networks with stricter isolation
- Public service needs internet egress (CDN + WAF + DDoS protection)

---

### Step 7: Integration Architecture Design

**Goal**: Design the technical solution for inter-system integration.

**Inputs**: Interaction matrix, existing interface state
**Outputs**: Integration-architecture design document

**Guidance**: See [Phase 03 Step 3 (Data & Tech Architecture)](../phase-03-strategy-and-top-level-design/03-data-and-tech-architecture-workflow.md).

---

### Step 8: Architecture Review and Release

**Goal**: Review the application-architecture deliverables for soundness and feasibility.

**Inputs**: Full architecture-design documents
**Outputs**: Review minutes, approved & issued architecture docs

**Guidance:**

**8.1 Architecture review checklist**

| Dimension | Check |
|---------|-------|
| Completeness | Covers all business needs? Any missing scenarios? |
| Consistency | Views consistent? Data flow reasonable? |
| Feasibility | Tech feasible? Resources sufficient? |
| Soundness | Module split reasonable? Interfaces reasonable? |
| Security | Meets classification requirements? Data security ensured? |
| Maintainability | Easy to operate? Monitoring complete? |
| Extensibility | Supports 3-yr growth & tech evolution? |
| Economy | Tech complexity controlled? TCO considered? |

**8.2 Review meeting**
- Attendees: our chief architect + tech lead; client IT lead + tech backbone
- Process: architecture presentation (30 min) → Q&A (30 min) → vote
- Conclusion: Pass / Conditional pass (note conditions) / Fail (note reasons)

---

## V. Roles and Responsibilities (RACI Matrix)

| Activity | Business architect | App architect | Tech expert | Client IT | Client business |
|------|:---:|:---:|:---:|:---:|:---:|
| Capability modeling | **R/A** | C | I | C | C |
| Process reengineer | **R** | C | I | C | **R** |
| App function define | C | **R/A** | C | C | C |
| Boundary & interaction | C | **R/A** | C | C | I |
| Arch master diagram | I | **R/A** | C | C | I |
| Deploy view | I | C | **R/A** | C | I |
| Integration arch | I | C | **R/A** | C | I |
| Arch review | C | C | C | **R** | I |

---

## VI. Key Checkpoints

| # | Checkpoint | Pass criterion |
|---|--------|---------|
| CP1 | Capability model review | All business domains covered, client business confirms |
| CP2 | TO-BE process confirmed | All core processes TO-BE designed |
| CP3 | Function completeness | Covers all core business needs |
| CP4 | Diagram review | Clear, complete, unambiguous |
| CP5 | Deploy plan confirmed | Client IT accepts plan |
| CP6 | Arch review passed | Formal pass, baseline established |

---

## VII. Estimated Duration

| Client scale | Business arch | App arch | Total |
|---------|:---:|:---:|:---:|
| Small | 1 wk | 1 wk | 2 wks |
| Medium | 2 wks | 2 wks | 4 wks |
| Large | 3–4 wks | 3–4 wks | 6–8 wks |

---

## VIII. Common Pitfalls and Countermeasures

| # | Pitfall | Countermeasure |
|---|------|------|
| 1 | Capability model detached from reality | Repeatedly confirm with business; validate with real scenarios |
| 2 | Chasing perfect TO-BE | TO-BE can be incrementally achieved; label phase targets |
| 3 | Over-introducing new tech | Justify every choice; avoid over-design |
| 4 | Ignore legacy-system integration | Draw existing systems and retain/refurbish/retire strategy |
| 5 | Overly long docs | Separate exec overview from detailed design |

---

## IX. Outputs List

1. **Business-capability map (CBM)** (.pptx)
2. **Business-capability heat map** (.xlsx)
3. **TO-BE process design** (.docx + Visio)
4. **Application-function list** (.xlsx)
5. **Application boundary & interaction definition** (.docx)
6. **Application-architecture master diagram** (.pptx / Visio)
7. **Deployment-architecture diagram** (.pptx / Visio)
8. **Integration-architecture design** (.pptx / Visio + .docx)
9. **Architecture design description** (.docx)
10. **Architecture review minutes** (.docx)

---

> **Version**: V1.0 | **Date**: 2025-07 | **Method**: TOGAF ADM + CBM + DDD
