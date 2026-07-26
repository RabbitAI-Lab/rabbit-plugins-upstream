# 02 — Agile Development & Iteration Management Workflow

## 1. Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│              Agile Development & Iteration Management Map              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │              Continuous Product Backlog Management             │  │
│  │  Epic/Feature/Story → Prioritize → Estimate → Multi-Sprint    │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │1.Sprint  │──>│2.Daily   │──>│3.CI &    │──>│4.Sprint   │        │
│  │  Planning│   │  Standup  │   │  Dev     │   │  Review   │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│       │                                              │              │
│       v                                              v              │
│  ┌──────────┐                                  ┌──────────┐        │
│  │5.Retro & │<─────────────────────────────────│ (next    │        │
│  │  Improve │                                  │  Sprint) │        │
│  └──────────┘                                  └──────────┘        │
│                                                                     │
│  Sprint length: 2 weeks (recommended) | Scrum ceremonies: 4        │
│    Tools: Jira / Trello / Azure DevOps                             │
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Applicable Scenarios

This workflow governs agile development management for intelligent-transport software. Given the public-sector and state-owned-enterprise client profile common in transportation, a hybrid "agile development + milestone delivery" model is recommended.

## 3. Hybrid Agile Model

### 3.1 Why do transport projects need hybrid agile?

| Transport-project trait | Pure-agile challenge | Hybrid approach |
|-------------|-----------|---------|
| Fixed-schedule + fixed-budget contract | Sprint scope cannot change indefinitely | Fixed scope baseline + controlled change |
| Public-sector acceptance needs full documentation | Code-heavy, doc-light | Sprint output updates docs in parallel |
| Multi-system integration needs overall planning | Sprint focuses locally | Architecture Sprint first (SAFe) |
| Clients unused to frequent participation | Sprint Review has no audience | Consolidate into monthly demo |
| Security clearance / compliance cert needs final version | Continuous delivery can't be filed | Phased releases + final version |

### 3.2 Recommended hybrid model

```
Recommended: Scrum + milestone management

One Sprint every 2 weeks (internal cadence)
One release every 4 weeks (internal milestone)
One client acceptance milestone every 2–3 months (client node)

┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
│Sprint│→│Sprint│→│Sprint│→│Sprint│→│Sprint│→│Sprint│→...
│  1   │ │  2   │ │  3   │ │  4   │ │  5   │ │  6   │
└──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘
   │        │        │        │        │        │
   └────────┼────────┘        └────────┼────────┘
            │                          │
            v                          v
     ┌─────────────┐          ┌─────────────┐
     │  Milestone M1│          │  Milestone M2│
     │ (client acc.) │          │ (client acc.) │
     └─────────────┘          └─────────────┘
```

---

## 4. Detailed Steps

---

### Step 1: Sprint Planning

**Objective**: Plan the content and goal of each Sprint (2 weeks).

**Inputs**: Product Backlog, previous Sprint's Velocity
**Outputs**: Sprint Backlog, Sprint goal

**Guidance:**

**1.1 Sprint planning meeting** (2–3 hrs, first morning of Sprint)

| Segment | Content | Duration |
|------|------|:---:|
| Sprint goal setting | PO presents this Sprint's business goal | 15 min |
| Capacity confirm | Team confirms available person-days | 10 min |
| Story selection | Pull Stories from top of Backlog by priority | 45 min |
| Task breakdown | Decompose each Story into tech tasks (≤1 day/task) | 60 min |
| Risk identification | Identify Sprint risks and dependencies | 15 min |

**1.2 Capacity planning**

```
Sprint capacity calculation:

Team size: N
Sprint working days: 10 days (2 weeks)
Effective working time: 6 hrs/day (minus meetings, comms, etc.)
Sprint capacity: N × 10 × 6 = ___ hours

Reserve buffer:
  - Urgent support and bug fixes: 20%
  - Technical debt / refactoring: 10%
  - Available dev capacity: capacity × 70%

Story Points planning:
  Based on average Velocity of last 3 Sprints
  Target Velocity = average Velocity × 90% (conservative estimate)
```

---

### Step 2: Daily Standup & Collaboration

**Objective**: Sync progress daily, surface issues, coordinate collaboration.

**Guidance:**

**2.1 Standup standard flow** (15 min, fixed time daily)

Each person answers three questions:
1. What did I complete yesterday?
2. What will I do today?
3. What is blocking me?

**2.2 Distributed-collaboration notes for transport projects**

- On-site client + remote hybrid teams are common
- Use Slack / Microsoft Teams for daily communication
- Client needs a liaison (preferably on-site)
- Keep written records of important communications (avoid verbal disputes)

---

### Step 3: Continuous Integration & Development

**Objective**: Ensure code quality and continuous deliverability.

**Guidance:**

**3.1 Branching strategy**

```
Recommended: Git Flow (simplified)

  master (production)
    │
    └── develop (dev mainline)
          │
          ├── feature/story-001
          ├── feature/story-002
          ├── bugfix/xxx
          └── release/v1.2.0

Rules:
  · feature branches cut from develop, merge back to develop
  · release branches cut from develop, merge to master and develop
  · each master merge = one release
  · feature branch lifetime ≤ 1 Sprint
```

**3.2 CI/CD pipeline**

```
Code commit → code scan (SonarQube) → unit test → build →
  automated test → deploy to test env → (manual) deploy to prod
```

**3.3 Quality gates**

| Gate | Standard | Fail consequence |
|------|------|-----------|
| Code coverage | >70% | Return to rewrite tests |
| Code scan | 0 Critical / Blocker | Return to fix |
| Unit tests | All pass | Return to fix |
| Security scan | 0 high-risk vulnerabilities | Return to fix |

---

### Step 4: Sprint Review

**Objective**: Demo Sprint output to stakeholders; collect feedback.

**Guidance:**

**4.1 Sprint Review flow** (1 hr, last afternoon of Sprint)

| Segment | Content | Duration |
|------|------|:---:|
| Sprint goal recap | Recap this Sprint's goal and completion | 5 min |
| Feature demo | Demo completed Stories one by one (focus) | 30 min |
| Stakeholder feedback | Collect issues and improvement suggestions | 15 min |
| Backlog adjustment | Adjust subsequent Backlog per feedback | 10 min |

**4.2 Transport-client Review notes**

- Clients may be unaccustomed to attending every 2 weeks; switch to monthly demo
- Demo environment must be stable (use test env, not Live Demo)
- Prepare a contingency if "the client says it's not what they imagined"

---

### Step 5: Retrospective & Continuous Improvement

**Objective**: Review the Sprint process; identify improvement opportunities.

**Guidance:**

**5.1 Sprint Retrospective** (1 hr, last day of Sprint)

```
Retro three questions:

1. Start (what should we start doing?)
   - Which good practices should we start?

2. Stop (what should we stop doing?)
   - Which behaviors hinder efficiency and should stop?

3. Continue (what should we keep doing?)
   - Which good practices should we keep?

Pick 1–2 improvement items per Sprint; validate next Sprint
```

**5.2 Team Velocity tracking**

```
Velocity trend:

 Sprint │ Planned │ Actual │ Trend
────────┼─────────┼────────┼─────
 S1     │ 25 SP   │ 22 SP  │ -
 S2     │ 24 SP   │ 24 SP  │ ↗
 S3     │ 26 SP   │ 28 SP  │ ↗↗
 S4     │ 28 SP   │ 26 SP  │ ↘

 4-Sprint average Velocity: 25 SP
 Reference for later Sprints: 25 SP × 90% = 22.5 SP
```

---

## 5. Roles & Responsibilities (RACI Matrix)

| Activity | Scrum Master | Product Owner | Dev Team | Client PO (business) |
|------|:---:|:---:|:---:|:---:|
| Backlog mgmt | C | **R/A** | C | C |
| Sprint planning | **R** | **A** | C | I |
| Daily standup | **R** | C | C | I |
| Dev & test | I | I | **R/A** | I |
| Sprint Review | C | **R** | C | **C** |
| Retro & improve | **R/A** | C | C | I |

---

## 6. Key Checkpoints

| # | Checkpoint | Pass standard |
|---|--------|---------|
| CP1 | Sprint Backlog ready | Each Story has task breakdown and estimate |
| CP2 | CI/CD running | Daily build success rate >90% |
| CP3 | Sprint goal met | Committed Stories 100% complete |
| CP4 | Quality gates | Code coverage and scan standards met |
| CP5 | Velocity stable | Velocity variance <20% across 3 consecutive Sprints |

---

## 7. Estimated Duration

| Activity | Frequency | Duration each |
|------|:---:|:---:|
| Sprint planning | Bi-weekly | 2–3 hrs |
| Daily standup | Daily | 15 min |
| Sprint Review | Bi-weekly | 1 hr |
| Sprint Retro | Bi-weekly | 1 hr |
| Backlog grooming | Weekly | 1 hr |

---

## 8. Output Catalog

1. **Product Backlog** (Jira / Azure DevOps)
2. **Sprint Backlog** (Jira / Azure DevOps)
3. **Sprint burndown chart** (Jira auto)
4. **Sprint Review demo video / screenshots** (archived)
5. **Sprint Retrospective minutes** (.docx)
6. **Velocity trend report** (Jira auto)

---

> **Version**: V1.0 | **Date**: 2025-07 | **Methodology**: Scrum + SAFe
