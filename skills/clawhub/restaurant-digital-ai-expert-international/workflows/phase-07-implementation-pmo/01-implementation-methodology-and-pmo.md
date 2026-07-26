# 01-Implementation Methodology & PMO

## Triggers
- Digital project has been approved, entering formal implementation phase

---

## Restaurant Digital Implementation 8-Stage Methodology

```
Initiation -> Requirements Deepening -> Solution Design -> Development/Configuration -> Testing -> Pilot Go-Live -> Rollout -> Operations Optimization
```

---

## Phase 1: Initiation (2-4 weeks)

### Project Charter

| Element | Content |
|---------|---------|
| Project Name | [XX] Restaurant Digital Transformation |
| Project Objectives | SMART (e.g., Complete POS replacement across 100 locations within 6 months; improve labor efficiency by 10%) |
| Project Scope | In-scope list + Out-of-scope list |
| Project Budget | Total budget + line-item budget + emergency contingency |
| Project Timeline | Key milestones + target go-live date |
| Core Team | Client PM + Vendor PM + Key Stakeholders |
| Success Criteria | Quantified metrics (e.g., system usage rate >90% 30 days post go-live) |
| Exit Criteria | Under what conditions is the project deemed "failed" / should be paused |

### Project Team Structure

```
                           Project Sponsor = CEO / VP of Operations
                                        |
                          +-------------+-------------+
                          |                           |
                    Client PM                     Vendor PM
                 (Internal IT/Ops)            (Vendor/Implementation Partner)
                          |                           |
              +-----------+-----------+      +--------+--------+
              |                       |      |                 |
        Business Lead           Tech Lead   Implementation   Tech Consultant
        (VP of Ops)           (IT Manager)  Consultant       (Remote)
              |                       |      (On-site)
        Location Reps            Dev/QA Team
        (Store Managers)
```

### Project Governance

| Governance Mechanism | Participants | Frequency | Agenda |
|---------------------|-------------|-----------|--------|
| Project Kickoff | All Stakeholders | Once | Objectives, scope, plan, roles & responsibilities |
| Weekly Status Meeting | Core Project Team | Weekly | Progress, issues, risks, next-week plan |
| Monthly Steering Committee | Sponsor + Core Team | Monthly | Major decisions, budget adjustments, risk approvals |
| Change Control Board | Sponsor + PM | As needed | Scope changes, budget adjustments, schedule adjustments |

---

## Phase 2: Requirements Deepening (2-4 weeks)

Building on RFP requirements, dive deep into each business scenario:

### Key Areas Requiring Deepening

| Area | Deepening Content |
|------|-------------------|
| Business Processes | "One order's journey from QR scan to dish completion" -- map current state and future state |
| Edge Cases | Refunds, order modifications, network outage, peak-hour add-ons, delivery platform disconnection... |
| Data Standards | Menu item coding rules, location coding rules, data dictionary |
| Integration Interfaces | Data fields, frequency, exception handling per interface |
| Permission Matrix | Who can view what, modify what, delete what (role-based) |

### Requirements Confirmation Meeting

- Hold 1-2 confirmation meetings per business module
- Must include: Client Business Lead + Client Tech + Vendor Implementation + Vendor Tech
- Deliverable: Signed-off Software Requirements Specification (SRS)

---

## Phase 3: Solution Design (3-6 weeks)

### Design Documents the Vendor Must Deliver

| Document | Content |
|----------|---------|
| Technical Architecture Design | Deployment architecture, network topology, DR plan |
| Detailed Functional Design | Page prototypes, interaction logic, data flows per function |
| Data Model Design | Database design, data dictionary |
| Integration Interface Design | API specs, field definitions, error codes |
| Data Migration Plan | What data to migrate, how to clean, how to verify |
| User Permission Design | Role-permission matrix |

---

## Phase 4: Development / Configuration (4-12 weeks, depending on complexity)

### Restaurant-Specific Development Considerations

| Consideration | Description |
|---------------|-------------|
| Peak Performance | Must stress test at peak lunch/dinner concurrency levels, not "average load" |
| Offline Mode | POS/KDS must support offline operation -- network outages are a norm for restaurants, not an exception |
| Print Stability | What happens when the printer connection fails? Auto-retry 3 times -> Alert -> Manual intervention |
| Payment Idempotency | User clicks pay repeatedly -> Must NEVER charge twice |
| Device Compatibility | In-store devices can be very old (older Android/iOS versions still in service) |

---

## Phase 5: Testing (3-6 weeks)

### Testing Levels

| Test Type | Executed By | Focus |
|-----------|-------------|-------|
| Unit Testing | Vendor Development | Code level |
| Integration Testing | Vendor QA | Interfaces + data flows |
| System Testing | Vendor QA | Full functionality + performance |
| Peak Stress Testing | Vendor + Client | Peak lunch/dinner concurrency simulation |
| **UAT** | Client Business + Store Manager Reps | Real-world scenario operations |
| Data Migration Testing | Both Parties | Migrate full dataset -> Compare and verify |

### Restaurant-Specific Test Scenario Checklist

```
[ ] Lunch peak: 60 people scan QR and order + pay simultaneously within 15 minutes
[ ] Dinner peak: KDS displays 80 pending orders simultaneously
[ ] Network outage recovery: Turn off WiFi -> POS offline payment for 30 min -> Restore WiFi -> Data sync
[ ] Printer out of paper: Kitchen print job mid-stream runs out -> Reload paper -> Auto-resume printing
[ ] Full refund flow: Customer returns dish -> POS refund -> KDS cancellation -> Inventory restock
[ ] Delivery aggregation: Uber Eats + DoorDash orders arrive simultaneously -> Aggregator drops zero, duplicates zero
[ ] Reconciliation: Daily settlement -- single/multi-item discrepancies detected and flagged
[ ] Permissions: Cashier attempts to refund a 3-day-old order -> System denies
```

---

## Phase 6: Pilot Go-Live (2-4 weeks)

### Pilot Location Selection

| Selection Criteria | Why |
|--------------------|-----|
| Store manager is cooperative (not the most distant) | Need a manager willing to provide feedback |
| Format and traffic are "typical" | Pilot conclusions must be generalizable |
| Do NOT pick the busiest flagship | If problems arise, the brand impact is too large |
| Not too remote (close to HQ / IT) | Easy for IT to reach quickly on-site |

### Pilot Go-Live Checklist

```
1 Week Before Go-Live:
[ ] Hardware installed and tested (POS terminals / KDS screens / printers / routers)
[ ] Network tested (WiFi signal + cellular backup + offline recovery test)
[ ] All staff training completed (100% assessment pass rate)
[ ] Data migrated (legacy system members / menu items / suppliers -> new system)
[ ] Go-live rehearsal: Run through the full workflow once

Go-Live Day:
[ ] Deployment complete by 8:00 AM
[ ] Vendor + Client IT on-site
[ ] 11:00-14:00 Peak monitoring
[ ] 17:00-21:00 Peak monitoring
[ ] 15-minute debrief after close each day

2 Weeks Post Go-Live:
[ ] Daily 15-minute debrief continues
[ ] Issue tracker: every item has an owner + target resolution date
[ ] Week 2: Gradually reduce on-site support -> remote support
```

---

## Phase 7: Rollout (at X locations/week cadence)

### Rollout Cadence Design

| Rollout Batch | Number of Locations | Pace | Selection Criteria |
|---------------|:---:|------|---------------------|
| Batch 1 (Pilot) | 1-3 locations | After 2 weeks stable operation | High cooperation + typical |
| Batch 2 | 5-10 locations | 2-3 per week | Same region |
| Batch 3 | 10-20 locations | 3-5 per week | Cover each region in batches |
| Batch 4 | All remaining | 5-10 per week | -- |

### Rollout Period Key Principles

```
1. Don't accelerate to meet a deadline
   If pilot location issues haven't been fixed, do NOT force the next batch.
   -> Stabilize the standard version first, then scale.

2. Use regions as rollout units
   Concentrated rollout in one region -> IT support concentrated -> Regional manager can oversee.

3. New locations: new system directly. Existing locations: phased migration.
   Newly opening locations go live on the new system directly (lower switching cost).
   Existing locations migrate on schedule.

4. "Go-live day is NEVER Friday"
   Friday go-live -> Weekend high traffic + IT unavailable -> Asking for trouble.
   Recommended: Tuesday or Wednesday.
```

---

## Phase 8: Operations Optimization

### Transitioning from "Project Mode" to "Operations Mode"

| Dimension | Project Mode | Operations Mode |
|-----------|-------------|-----------------|
| Goal | System go-live | System used well |
| Cadence | Sprint | Continuous |
| Team | Project team | IT Operations + Business |
| Focus | Schedule / Scope / Cost | SLA / Usage Rate / Satisfaction / Continuous Improvement |

### Transition Criteria

- [ ] All locations have been live for >=1 month
- [ ] System stability: 30-day availability >99.5%
- [ ] User activity: Store manager daily active rate >90%
- [ ] Data quality: Key data (daily revenue / order count / members) completeness >95%
- [ ] Issue response: Average resolution time <24 hours
- [ ] Documentation handoff: Operations manual + issue handling manual delivered

---

## PMO Day-to-Day Management Tools

### Weekly Status Report (1 Page)

```
Project Name: [XX]                                Date: [XX]
Overall Progress: XX% (P1: XX% | P2: XX% | P3: XX%)

Completed This Week:
- [X] XX
- [X] XX

Planned Next Week:
- [ ] XX
- [ ] XX

Top 3 Risks:
1. XX (Impact: XX | Mitigation: XX | Owner: XX)
2. XX
3. XX

Decisions Needed from Management:
- [ ] XX (Option A / B / C)
```

### Issue Tracker

| ID | Issue | Severity | Discovered | Owner | Target Resolution | Status |
|:---:|------|:---:|---|---|---|---|
| ISS-001 | Location XX POS slow during peak | P1 | 6/1 | John | 6/5 | In Progress |
| ISS-002 | Member points posting delay | P2 | 6/2 | Jane | 6/8 | Pending Confirmation |

---

## Common Restaurant Implementation Pitfalls

| Pitfall | Consequence | Countermeasure |
|---------|-------------|----------------|
| Launching multiple systems simultaneously | Each one done poorly, staff overwhelmed | Only one core system per phase |
| Full rollout before pilot is proven | Problems multiplied x number of locations | Pilot proven -> 2 weeks stable -> scale |
| Testing only in "test environment" | Real environment reveals countless issues | Test with real data + real hardware |
| Ignoring WiFi / cellular conditions | Peak-hour network outage -> POS down -> total collapse | Signal test before go-live + cellular backup |
| No rollback plan | System crashes -> helpless | Confirm rollback path before any change |
| Vendor team mid-project personnel change | New person has no project context | Contract stipulates core personnel cannot change + backup personnel |
| Go-live on Friday | Weekend problems, nobody available | Go-live on Tuesday or Wednesday |

---

## Deliverables
- Project Charter
- Detailed Implementation Plan (with WBS / Gantt)
- Project Governance Structure
- Risk Register
- Weekly Status Report Template

## Quality Checks
- [ ] Project Charter has clear "Success Criteria" and "Exit Criteria"
- [ ] Pilot location selection has criteria (not random)
- [ ] All key test scenarios cover "Peak" and "Network Outage"
- [ ] Rollback plan exists
- [ ] Rollout plan is the most conservative (max 3-5 locations/week)
- [ ] No "Friday go-live" in rollout schedule
