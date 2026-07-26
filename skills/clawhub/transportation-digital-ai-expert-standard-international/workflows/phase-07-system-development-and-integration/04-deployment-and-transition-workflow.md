# 04 — Deployment & Transition Management Workflow

## 1. Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                Deployment & Transition Management Map                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │1.Go-live │──>│2.Production│──>│3.Data     │──>│4.Dress    │        │
│  │  Plan     │   │  Env Prep │   │  Migration│   │  Rehearsal│        │
│  │          │   │          │   │  & Verify │   │  & Dry-run│        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│       │              │              │              │                │
│       v              v              v              v                │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │5.Cutover │──>│6.War Room│──>│7.Hypercare│──>│8.O&M      │        │
│  │  Switch   │   │  Support  │   │  Period   │   │  Handover │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│                                                                     │
│  Core strategy: Canary release | Rollback plan | 7×24 War Room     │
│    | 30-day Hypercare                                            │
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Detailed Steps

---

### Step 1: Go-live Plan

**Objective**: Define a detailed cutover plan and contingency (rollback) plan.

**Guidance:**

**1.1 Go-live plan core elements**

```
Go-live plan document:

1. Go-live objective & scope
   - Which systems, modules, functions go live this time
   - What is out of scope for this release

2. Cutover strategy selection

   ┌───────────────┬─────────────────┬──────────────┐
   │   Strategy    │   Applicable      │   Risk       │
   ├───────────────┼─────────────────┼──────────────┤
   │ Big Bang      │ Greenfield, no   │ High (no     │
   │ (one-shot)    │ legacy system    │ exit)        │
   ├───────────────┼─────────────────┼──────────────┤
   │ Parallel run  │ Replace legacy   │ Medium (high │
   │               │ needs transition │ cost)        │
   ├───────────────┼─────────────────┼──────────────┤
   │ Canary        │ Large user-base  │ Low (roll-   │
   │               │ system           │ back-able)  │
   ├───────────────┼─────────────────┼──────────────┤
   │ Geographic    │ Multi-region     │ Low (phased  │
   │ batch         │ deployment       │ control)    │
   └───────────────┴─────────────────┴──────────────┘

3. Detailed cutover steps
   (each step with owner, time, verification method, in timeline order)

4. Rollback plan
   - Rollback trigger conditions
   - Rollback steps
   - Post-rollback verification
   - Estimated rollback duration

5. Go-live team
   - Roles, responsibilities, contact info

6. Go-live window
   - Date, time, expected duration
   - Recommendation: Fri evening → Sun early morning (least traffic impact)
```

**1.2 Transport-system go-live special considerations**

| Factor | Note |
|---------|------|
| Avoid major holidays / large public events | Avoid launching during peak travel periods / major public events |
| Traffic off-peak window | Low volume late night → early morning |
| Internal before external | Client internal first → service window → public users |
| Business continuity | Core monitoring system must not lose monitoring during launch |

---

### Step 2: Production Environment Preparation

**Objective**: Ensure the production environment is ready and verified.

**Guidance:**

**2.1 Production environment checklist**

```
Production environment checklist:

□ Hardware resources
  □ Servers racked and in place
  □ Network config (IP / VLAN / firewall policy)
  □ Storage mounted, capacity checked
  □ GPU resources (if AI inference needed)

□ Software resources
  □ OS installed and hardened
  □ Middleware (DB / message queue / K8s, etc.) installed
  □ Application deployment package ready
  □ SSL certificate
  □ Monitoring agent deployed

□ Network & security
  □ DNS resolution effective
  □ Load-balancer config
  □ WAF rules configured
  □ Firewall ports opened
  □ VPN / dedicated line connectivity

□ O&M readiness
  □ Backup strategy configured
  □ Monitoring & alerting configured
  □ Log collection configured
  □ O&M accounts and permissions
```

---

### Step 3: Data Migration & Verification

**Objective**: Safely and completely migrate data from the legacy system (if any) to the new system.

**Guidance:**

**3.1 Data migration four-step method**

```
Data migration four steps:

1. Pre-migration check
   □ Data-volume estimate (rows, size)
   □ Data cleansing (dirty / duplicate data)
   □ Character-set / encoding consistency
   □ Data dictionary / master-data alignment

2. Trial migration (non-production)
   □ Run a full migration in test env
   □ Verify post-migration completeness & accuracy
   □ Record migration duration

3. Formal migration
   □ Stop legacy-system writes
   □ Export → transform → import
   □ Full + incremental sync

4. Post-migration verification
   □ Row count reconciliation (source vs. target)
   □ Sampling reconciliation (random 100 rows, field-by-field)
   □ Key business-data reconciliation
   □ Business-unit confirmation
```

**3.2 Data verification SQL example**

```sql
-- Row-count consistency check
SELECT 'source' as db, count(*) FROM source_db.traffic_event
UNION ALL
SELECT 'target' as db, count(*) FROM target_db.traffic_event;

-- Key-data sampling reconciliation
SELECT s.event_id, s.event_type, s.event_time,
       t.event_id, t.event_type, t.event_time
FROM source_db.traffic_event s
FULL OUTER JOIN target_db.traffic_event t ON s.event_id = t.event_id
WHERE s.event_type != t.event_type
   OR ABS(s.event_time - t.event_time) > 1;
```

---

### Step 4: Dress Rehearsal & Dry-run

**Objective**: Ensure a flawless go-live through repeated rehearsals.

**Guidance:**

**4.1 Rehearsal types**

| Type | Count | Environment | Purpose |
|---------|:---:|------|------|
| Technical rehearsal | 2–3 | Test env | Verify deploy scripts, cutover steps |
| Full-process rehearsal | 1–2 | Pre-prod env | Fully simulate go-live end-to-end |
| Rollback rehearsal | 1–2 | Test env | Validate rollback-plan feasibility |

**4.2 Go-live runbook**

```
Runbook structure:

I. Go-live operation steps (hyper-detailed)
   Each step contains:
   · Step number & name
   · Action (command / operation)
   · Executor
   · Estimated duration
   · Verification method
   · Exception handling

Example:
  Step 03: Stop legacy system service
  Action: systemctl stop old-system
  Executor: Ops engineer — Zhang San
  Est. duration: 1 min
  Verify: systemctl status old-system → inactive
  Exception: If cannot stop cleanly, run kill -15 <pid>, wait 30s;
             if still running, notify TL whether to kill -9

II. Versions & configuration
III. Rollback steps
IV. Contacts & escalation path
```

---

### Step 5: Formal Cutover

**Objective**: Execute the cutover per the runbook.

**Guidance:**

**5.1 Go-live day timeline example**

```
Go-live day timeline (example: Fri 22:00 launch):

┌──────────┬──────────────────────────────────────┐
│  21:00   │ War Room assemble, roles confirmed, tools checked │
│  21:30   │ Pre-launch check (env / data / backup / notice sent)│
│  22:00   │ Launch begins — system enters maintenance mode     │
│  22:05   │ Step 1: Stop legacy system service                 │
│  22:10   │ Step 2: Database backup                            │
│  22:30   │ Step 3: Data migration (if needed)                │
│  23:30   │ Step 4: Deploy new version                        │
│  23:45   │ Step 5: Start new system services                 │
│  00:00   │ Step 6: Smoke test (core function verify)         │
│  00:30   │ Step 7: Integration test (key interfaces)         │
│  01:30   │ Step 8: Regression test (full-function spot-check)│
│  02:00   │ Step 9: Exit maintenance mode                     │
│  02:30   │ Go-live success confirm / or execute rollback     │
│  03:00   │ Day's launch work ends; War Room enters support   │
└──────────┴──────────────────────────────────────┘
```

---

### Step 6: War Room Support

**Objective**: Intensively monitor for 48–72 hours post-launch; respond rapidly.

**Guidance:**

**6.1 War Room configuration**

| Element | Note |
|------|------|
| Location | Dedicated room or online War Room (Teams / Zoom standing meeting) |
| Staff | Dev / test / O&M / PM + client IT rep |
| Monitoring wall | Core business KPI dashboard, system health monitoring |
| Comms | Dedicated Slack / Teams channel + walkie-talkie (if available) |
| Shift plan | 3 shifts (8 hrs each) for 7×24 coverage |
| Food | Meals and drinks prepared (long watch) |

**6.2 War Room escalation framework**

```
Issue escalation path:

L1: Technical team resolves on its own (within 10 min)
  └→ L2: Escalate to architect / tech lead (unresolved in 30 min)
       └→ L3: Escalate to PM (unresolved in 1 hr, impacting business)
            └→ L4: Escalate to program director / client Sponsor (major incident)
```

---

### Step 7: Hypercare Transition Period

**Objective**: 30-day intensive support post-launch; rapidly respond to user issues.

**Guidance:**

**7.1 Hypercare schedule**

| Window | Focus |
|-------|---------|
| D+0 ~ D+3 (War Room) | 7×24 watch, rapid response, 3× daily issue sync |
| D+4 ~ D+14 (intensive) | Working-hours watch + off-hours on-call, daily issue digest |
| D+15 ~ D+30 (transition) | Normal working-hours support, weekly issue digest, begin O&M handover |

**7.2 Hypercare KPIs**

| KPI | Target |
|------|:---:|
| P0 issue response time | <15 min |
| P0 issue resolution time | <4 hrs |
| P1 issue response time | <1 hr |
| P1 issue resolution time | <24 hrs |
| User satisfaction | >80 |

---

### Step 8: Formal O&M Handover

**Objective**: Complete the formal handover from project team to O&M team.

**Guidance:**

**8.1 O&M handover checklist**

```
Handover list:

□ O&M documentation
  □ System O&M manual
  □ Deployment architecture diagram (final)
  □ Contingency / BCP plan
  □ Daily inspection manual
  □ Common-issue handling manual

□ System access
  □ O&M accounts and permissions transferred
  □ Server / DB / middleware access
  □ Monitoring-platform access

□ Code & configuration
  □ Source-code repository access
  □ Configuration-file management
  □ CI/CD configuration

□ Knowledge transfer
  □ O&M training completed (≥2 sessions)
  □ O&M team shadowing ≥1 week
  □ Simulation drill of key issues

□ Contract handover
  □ O&M SLA confirmed
  □ Ticketing-system process confirmed
  □ Escalation path confirmed

□ Sign-off
  □ O&M team signs acceptance confirmation
  □ Project team signs delivery confirmation
```

---

## 3. Roles & Responsibilities (RACI Matrix)

| Activity | PM | Tech Lead | Ops Engineer | Test Lead | Client IT |
|------|:---:|:---:|:---:|:---:|:---:|
| Go-live plan | **R/A** | C | C | I | C |
| Env prep | I | C | **R/A** | I | C |
| Data migration | I | C | **R** | **C** | C |
| Dress rehearsal | C | **R** | C | C | I |
| Formal cutover | C | **R** | **R** | C | C |
| War Room | **A** | **R** | C | C | C |
| Hypercare | C | **R** | C | C | C |
| O&M handover | **R/A** | C | C | I | C |

---

## 4. Key Checkpoints

| # | Checkpoint | Pass standard |
|---|--------|---------|
| CP1 | Go-live plan review | Plan approved, rollback feasible |
| CP2 | Rehearsal success | ≥1 full-process rehearsal succeeds |
| CP3 | Launch success | Smoke test + core-function verification pass |
| CP4 | War Room ends | No P0 in 48 h, P1 <5 |
| CP5 | Hypercare ends | 7 consecutive days with no new P1 |
| CP6 | O&M handover | O&M team signs acceptance confirmation |

---

## 5. Estimated Duration

| Stage | Duration |
|------|:---:|
| Go-live plan + prep | 1–2 wks |
| Rehearsal + dry-run | 1 wk |
| Formal launch | 1 night (4–8 hrs) |
| War Room | 2–3 days |
| Hypercare | 30 days |
| O&M handover | 1–2 wks |

---

## 6. Output Catalog

1. **Go-live plan document (with rollback plan)** (.docx)
2. **Go-live runbook** (.docx)
3. **Data migration plan & verification report** (.docx)
4. **Go-live rehearsal record** (.docx)
5. **War Room duty log** (.xlsx)
6. **Hypercare issue tracker** (.xlsx)
7. **O&M handover package** (.docx + manuals)
8. **System O&M manual** (.docx)

---

> **Version**: V1.0 | **Date**: 2025-07
