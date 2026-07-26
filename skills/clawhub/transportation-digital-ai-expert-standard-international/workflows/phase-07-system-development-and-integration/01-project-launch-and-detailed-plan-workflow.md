# 01 — Project Launch & Detailed Planning Workflow

## 1. Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│               Project Launch & Detailed Planning Map                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │1.Handover│──>│2.Team     │──>│3.Kickoff │──>│4.WBS      │        │
│  │  & Absorb│   │  Form &   │   │  Meeting  │   │  & Plan   │        │
│  │          │   │  Charter  │   │          │   │          │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│       │              │              │              │                │
│       v              v              v              v                │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │5.Resource│──>│6.Risk     │──>│7.Mgmt    │──>│8.Launch   │        │
│  │  Load &  │   │  Register │   │  Plans    │   │  Readiness│        │
│  │  Schedule│   │  Build    │   │  Author   │   │  Review   │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Detailed Steps

---

### Step 1: Handover Reception & Absorption

**Objective**: Pre-sales team fully transfers project information to the delivery team.

**Inputs**: Contract, SOW, pre-sales materials
**Outputs**: Handover acknowledgment, project-readiness assessment

**Guidance:**

**1.1 Handover checklist**

```
Handover package contents:
□ Signed contract and all annexes
□ Statement of Work (SOW)
□ Technical solution (solution version)
□ Requirements research records (if any)
□ Client relationship map
□ Key risks and watch-items
□ Pre-sales commitment list (pay special attention to verbal commitments)
□ Client expectation-management notes
```

**1.2 Special review of "pre-sales commitments"**

Verify whether commitments made during pre-sales fall within the contract scope:
- Verbal commitments not written into the contract → assess delivery cost and risk
- Commitments beyond contract scope → clarify boundaries with the client

---

### Step 2: Team Formation & Charter Issuance

**Objective**: Form the project team; issue the project charter.

**Guidance:**

**2.1 Typical team structure for intelligent-transport projects**

```
Project team organization:

                    ┌─────────────────┐
                    │ Steering Committee│
                    │ (both Sponsors)    │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              v              v              v
        ┌──────────┐  ┌──────────┐  ┌──────────┐
        │ Our PM    │  │ Client PM │  │ PMO /      │
        │ (PM)      │  │ (CPM)     │  │ Supervisor │
        └─────┬────┘  └─────┬────┘  └─────┬────┘
              │              │              │
              └──────────────┼──────────────┘
                             │
    ┌──────────┬──────────┬──┴──────┬──────────┬──────────┐
    │          │          │        │          │          │
    v          v          v        v          v          v
┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐
│Architect││Back-end ││Front-end││Data Eng.││AI Eng. ││Test Eng.│
│(1)     ││(3-5)   ││(2-3)   ││(2)     ││(2-3)   ││(2)     │
└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘
```

**2.2 Core elements of the project charter**

| Element | Content |
|------|------|
| Project objectives | SMART-formatted objectives |
| Scope | Scope description + boundaries |
| Key milestones | Major delivery and review nodes |
| Core team | Both parties' core members and responsibilities |
| Budget summary | Total budget and major line items |
| Approval requirements | Authority for change / acceptance |
| Charter sign-off | Both Sponsors' signatures |

---

### Step 3: Kickoff Meeting

**Objective**: Formally launch the project; align both parties' understanding and expectations.

**Guidance:**

**3.1 Kickoff agenda** (half day)

| Time | Segment | Content |
|------|------|------|
| 09:00-09:20 | Opening | Both decision-makers' remarks, project background |
| 09:20-09:50 | Intro | Objectives, scope, solution overview |
| 09:50-10:30 | Execution plan | Project plan, milestones, team intro |
| 10:30-10:45 | Break | |
| 10:45-11:15 | Collaboration framework | Comms/operating framework, issue-escalation path, change process |
| 11:15-11:45 | Near-term plan | First-30-days detailed plan, client cooperation items |
| 11:45-12:00 | Wrap-up | Mutual confirmation, group photo |

---

### Step 4: WBS Decomposition & Planning

**Objective**: Decompose the project into manageable work packages; author the detailed schedule.

**Guidance:**

**4.1 Reference WBS for intelligent-transport projects**

```
Intelligent-transport project WBS — level 1:

1.0 Project Management
  1.1 Initiation
  1.2 Monitoring & Control
  1.3 Closeout

2.0 Requirements & Design
  2.1 Requirements research & confirmation
  2.2 System design (high-level + detailed)
  2.3 UI/UX design
  2.4 Database design
  2.5 Interface design

3.0 Platform Build
  3.1 Foundation platform
  3.2 Data platform
  3.3 AI platform
  3.4 Integration platform
  3.5 DevOps environment

4.0 Application Development
  4.1 [Module 1] development
  4.2 [Module 2] development
  ... (expand by application module)

5.0 System Integration
  5.1 Interface development
  5.2 Internal system integration
  5.3 External system connection
  5.4 Joint commissioning test

6.0 Testing
  6.1 Unit testing
  6.2 Integration testing
  6.3 Performance testing
  6.4 Security testing
  6.5 UAT (user acceptance testing)

7.0 Deployment & Go-live
  7.1 Production environment prep
  7.2 Data migration
  7.3 System deployment
  7.4 Cutover
  7.5 Go-live support

8.0 Training & Knowledge Transfer
  8.1 Admin training
  8.2 User training
  8.3 Document delivery

9.0 O&M Handover
  9.1 O&M document delivery
  9.2 O&M team training
  9.3 Transition-period support
```

**4.2 Schedule authoring essentials**

| Essential | Description |
|------|------|
| Critical path | Identify and mark the project critical path |
| Buffer | Reserve 10–15% buffer on the critical path |
| Dependency mgmt | Clearly mark FS/SS/FF dependencies between packages |
| Milestones | 5–8 major milestones, each with deliverable & acceptance criteria |
| Client nodes | Mark nodes requiring client cooperation (approval / data / environment) |

---

### Step 5: Resource Loading & Scheduling

**Objective**: Assign people to specific work packages; resolve resource conflicts.

**Guidance:**

**5.1 Resource histogram**

Plot monthly personnel-demand histogram; identify peaks and troughs.

**5.2 Resolving key resource conflicts**

| Conflict scenario | Resolution |
|---------|---------|
| AI engineer needed by two projects simultaneously | Stagger schedule or bring in external resources |
| Test-environment conflict | Reservation system + fast environment provisioning |
| Insufficient client resources | Give client a "resource-need forecast" one month ahead |

---

### Step 6: Risk Register Build

**Objective**: Identify and manage delivery risks.

**Guidance:**

**6.1 Typical delivery risks for intelligent-transport projects**

| Risk | Prob. | Impact | Response |
|------|:---:|:---:|------|
| Frequent client requirement changes | High | Med | Strict change control + requirement freeze window |
| Difficulty obtaining data | High | High | Early dedicated data governance |
| Unstable third-party system API | Med | Med | Early joint debugging + interface monitoring |
| Key-person attrition | Med | High | Knowledge backup + A/B-role operating model |
| Performance shortfall | Med | High | Early performance testing + architecture review |
| Schedule slip | Med | High | Critical-path mgmt + periodic health check |

**6.2 Risk register template**

| ID | Risk description | Category | Prob. | Impact | Level | Strategy | Owner | Trigger |
|----|---------|------|:---:|:---:|:---:|---------|-------|---------|
| R01 | ... | Requirement | H | H | H | Mitigate + contingency | PM | ... |

---

### Step 7: Management Plans Authoring

**Objective**: Author the domain-specific management plans.

**Guidance:**

**7.1 Management plan list**

- Scope management plan
- Schedule management plan
- Cost management plan
- Quality management plan
- Communications management plan
- Risk management plan
- Configuration management plan
- Change management plan

---

### Step 8: Launch-Readiness Review

**Objective**: Confirm all launch conditions are in place.

**Guidance:**

**8.1 Launch-readiness checklist**

```
Launch-readiness checklist:

□ Project charter signed
□ Core team in place
□ Detailed project plan approved
□ PM tooling set up (Jira / Azure DevOps / Microsoft Teams)
□ Code repository / Git established
□ CI/CD pipeline initialized
□ Dev / test environments ready
□ Client resources committed (coordination staff / data / interfaces)
□ Kickoff meeting completed
□ First contract payment received (per payment schedule)
```

---

## 3. Roles & Responsibilities (RACI Matrix)

| Activity | PM | Architect | Tech Lead | Client PM | Sponsor |
|------|:---:|:---:|:---:|:---:|:---:|
| Handover | **R/A** | I | I | I | I |
| Team formation | **R/A** | C | C | I | C |
| Kickoff | **R/A** | C | C | C | **C** |
| WBS & plan | **R/A** | C | C | C | I |
| Resource allocation | **R/A** | I | I | I | I |
| Risk register | **R/A** | C | C | C | I |
| Management plans | **R/A** | I | I | C | I |
| Launch review | **R** | I | I | C | **A** |

---

## 4. Key Checkpoints

| # | Checkpoint | Pass standard |
|---|--------|---------|
| CP1 | Handover complete | Handover package 100% complete |
| CP2 | Team in place | Core team fully staffed |
| CP3 | Kickoff done | Both decision-makers attended and reached consensus |
| CP4 | Plan reviewed | Critical path sound, buffer sufficient |
| CP5 | Launch ready | All launch-checklist items pass |

---

## 5. Estimated Duration: 1–2 weeks

---

## 6. Output Catalog

1. **Pre-sales → Delivery handover package** (.docx)
2. **Project charter** (.docx)
3. **Kickoff materials & minutes** (.pptx + .docx)
4. **WBS & detailed schedule** (.xlsx / .mpp)
5. **Resource histogram** (.xlsx)
6. **Risk register** (.xlsx)
7. **Project management plan** (.docx)
8. **Launch-readiness review record** (.docx)

---

> **Version**: V1.0 | **Date**: 2025-07 | **Methodology**: PMBOK
