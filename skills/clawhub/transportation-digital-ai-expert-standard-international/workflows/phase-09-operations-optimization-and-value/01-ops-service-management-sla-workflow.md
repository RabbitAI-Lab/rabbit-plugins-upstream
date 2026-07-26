# 01 — O&M Service Management & SLA Monitoring Workflow

## 1. Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│              O&M Service Mgmt & SLA Monitoring Map                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │1.O&M      │──>│2.Incident│──>│3.Problem │──>│4.Change   │        │
│  │  Framework│   │  Mgmt    │   │  Mgmt    │   │  Mgmt     │        │
│  │  Build    │   │  Process │   │  Process │   │  Process  │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│       │              │              │              │                │
│       v              v              v              v                │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │5.SLA      │──>│6.Monitor │──>│7.O&M     │──>│8.Continuous│       │
│  │  Define & │   │  & Alert│   │  Report &│   │  Improve  │        │
│  │  Measure  │   │  System │   │  Review  │   │  Plan     │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│                                                                     │
│  Standards: ITIL 4 | ISO 20000 | security-baseline O&M requirements│
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Detailed Steps

---

### Step 1: O&M System Build

**Objective**: Establish an O&M management system aligned with ITIL.

**Guidance:**

**1.1 O&M organization**

```
Intelligent-transport system O&M team:

┌──────────────┐
│  O&M Manager  │ (1)
└──────┬───────┘
       │
 ┌─────┼─────┬─────────┬─────────┐
 │     │     │         │         │
 v     v     v         v         v
┌────┐┌────┐┌────┐  ┌────┐  ┌────────┐
│L1   ││L2   ││L3   │  │Mon. │  │Data O&M │
│Service││Tech ││Expert│  │Team │  │Team    │
│Desk ││Supp.││(R&D)│  │(2)  │  │(2)     │
│(2)  ││(3)  ││     │  │    │  │        │
└────┘└────┘└────┘  └────┘  └────────┘
```

**1.2 O&M toolchain**

| Category | Recommended tools | Use |
|---------|---------|------|
| ITSM / ticketing | Jira Service Management / Azure DevOps | Incident / problem / change |
| Monitoring | Prometheus + Grafana / Zabbix | Infra monitoring |
| APM | SkyWalking / Pinpoint | App performance monitoring |
| Logging | ELK (Elasticsearch + Logstash + Kibana) | Log collection & analysis |
| Alerting | AlertManager / PagerDuty | Alert notification & escalation |
| CMDB | iTop / in-house | Configuration management DB |
| Automation | Ansible / Jenkins | Automated O&M |

---

### Step 2: Incident Management Process

**Objective**: Establish a standardized incident process; ensure rapid service restoration.

**Guidance:**

**2.1 Incident management flow**

```
Incident management flow:

  User report / monitoring alert
        │
        v
  ┌──────────────┐
  │ 1. Log & classify│
  └──────┬───────┘
         │
         v
  ┌──────────────┐
  │ 2. Triage &   │
  │   L1 handling │──── resolved ──→ close incident
  └──────┬───────┘
         │ unresolved
         v
  ┌──────────────┐
  │ 3. Escalate L2│──── resolved ──→ close + knowledge base
  └──────┬───────┘
         │ unresolved
         v
  ┌──────────────┐
  │ 4. Escalate L3│──── resolved ──→ close + KB + RCA
  │   (R&D)      │
  └──────────────┘
```

**2.2 Incident priority matrix**

| | High impact | Med impact | Low impact |
|------|:---:|:---:|:---:|
| Urgent | P0 Critical | P1 High | P2 Medium |
| Normal | P1 High | P2 Medium | P3 Low |
| Low | P2 Medium | P3 Low | P4 Planned |

---

### Step 3: Problem Management Process

**Objective**: Analyze incident root cause; prevent recurrence.

**Guidance:**

**3.1 Problem vs. Incident**

| | Incident | Problem |
|---|---|---|
| Definition | Unplanned event causing service disruption / quality drop | Unknown root cause of one or more incidents |
| Goal | Restore service ASAP | Find root cause and fix permanently |
| Relation | Incident may trigger problem | Problem fix prevents repeat incidents |

**3.2 Root-Cause Analysis (RCA) methods**

| Method | Scenario | Steps |
|------|---------|------|
| 5-Whys | Simple problems | Ask "why" five times |
| Fishbone | Multi-factor problems | Man / Machine / Material / Method / Environment |
| Fault tree | Complex system failures | Decompose from top event downward |

---

### Step 4: Change Management Process

**Objective**: Govern IT change; reduce change risk.

**Guidance:**

**4.1 Change classification**

| Type | Description | Approval | Window |
|------|------|:---:|------|
| Standard | Pre-authorized routine change | Change Manager | Routine window |
| Normal | Needs assessment & approval | CAB (Change Advisory Board) | Planned window |
| Emergency | Urgent fix for major incident | ECAB (Emergency CAB) | Immediate |

**4.2 Change-window settings**

- Routine window: Thu 22:00–02:00 (traffic off-peak)
- Emergency window: 24/7 (but needs ECAB approval)
- Change freeze: prohibited during peak travel periods / major public events / major political events

---

### Step 5: SLA Definition & Measurement

**Objective**: Define clear SLAs and measure them continuously.

**Guidance:**

**5.1 Reference SLA for intelligent-transport systems**

| Metric | Definition | Target | Method |
|---------|------|:---:|---------|
| Availability | Core-system monthly uptime ratio | ≥99.9% | Monitoring |
| MTTR | Mean time to repair | P0<4h, P1<8h | ITSM stats |
| MTBF | Mean time between failures | >720h | ITSM stats |
| Response time | From report to first response | P0<15min, P1<30min | ITSM stats |
| On-site time | From report to engineer on-site | Urban<2h, suburban<4h | Service log |
| Data backup | RPO (recovery point) | <1 hour | Backup log |
| Recovery | RTO (recovery time) | <4 hours | Drill log |

**5.2 Monthly SLA dashboard**

| Metric | Target | Actual | Met | Trend |
|------|:---:|:---:|:---:|:---:|
| Availability | ≥99.9% | 99.95% | ✅ | → |
| P0 response | <15min | 8min | ✅ | ↗ |
| P1 resolution | <8h | 6.5h | ✅ | ↗ |
| ... | ... | ... | ... | ... |

---

### Step 6: Monitoring & Alerting System

**Objective**: Build a comprehensive monitoring & alerting system.

**Guidance:**

**6.1 Monitoring matrix**

| Layer | Object | Metrics | Tool |
|-------|---------|---------|------|
| Infra | Server / net / storage | CPU / mem / disk / traffic | Prometheus / Zabbix |
| App | Microservice / API | QPS / latency / error rate | SkyWalking |
| DB | MySQL / Oracle / Redis | Connections / slow query / buffer | Prometheus Exporter |
| Business | Core business metrics | Event-detection rate / data latency | In-house / BI |
| Security | Attacks / anomalies | Attack alert / abnormal login | SIEM / WAF |
| Field devices | Cameras / VMS signs | Online rate / failure rate | IoT platform |

**6.2 Alert escalation rules**

| Level | Condition | Notify | Escalate |
|:---:|------|---------|:---:|
| P0 | Core system unavailable | Phone + SMS + group | 15min → duty manager |
| P1 | Core function degraded | SMS + group | 30min → O&M manager |
| P2 | Non-core function abnormal | Group | 2h → O&M engineer |

---

### Step 7: O&M Report & Service Review

**Objective**: Periodically author O&M reports; run service reviews.

**Guidance:**

**7.1 O&M report system**

| Type | Content | Freq | Audience |
|---------|------|:---:|------|
| Daily | Key incidents, alerts, handling | Daily | O&M team |
| Weekly | Incident stats, SLA trend, key problems | Weekly | PM |
| Monthly | Monthly SLA, capacity trend, improvement plan | Monthly | Management |
| Quarterly | Quarterly service review, optimization advice | Quarterly | Sponsor |

**7.2 Monthly service-review agenda**

| Segment | Content | Duration |
|------|------|:---:|
| SLA review | This month's SLA achievement | 15min |
| Incident analysis | Top 5 incident types & handling | 15min |
| Improvement progress | Last period's improvement items | 10min |
| Next-period plan | Next month's focus | 10min |
| Discussion | Client feedback & issues | 10min |

---

### Step 8: Continuous Improvement Plan

**Objective**: Based on O&M data and client feedback, plan and run continuous improvement.

**Guidance:**

**8.1 SIP (Service Improvement Plan) template**

| SIP ID | Item | Source | Current | Target | Plan | Owner | Due |
|---------|-------|------|---------|---------|---------|-------|:---:|
| SIP-001 | API latency optimization | SLA data | P99=800ms | P99<500ms | ... | Zhang | 6/30 |
| SIP-002 | Reduce incident repeat rate | RCA | 30% repeat | <15% | ... | Li | 7/15 |

---

## 3. Key Checkpoints

| # | Checkpoint | Pass standard |
|---|--------|---------|
| CP1 | ITSM live | Incident / problem / change flows online |
| CP2 | Monitoring coverage | Core systems 100% monitored |
| CP3 | Monthly SLA met | SLA achievement rate >95% |

---

## 4. Output Catalog

1. **O&M system design** (.docx)
2. **SLA definition document** (.docx)
3. **Monitoring & alerting config manual** (.docx)
4. **O&M operations manual** (.docx)
5. **Monthly SLA report** (.pptx / .xlsx)
6. **Service-review minutes** (.docx)
7. **Continuous improvement plan (SIP)** (.xlsx)

---

> **Version**: V1.0 | **Date**: 2025-07 | **Standard**: ITIL 4
