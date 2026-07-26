# 02-System Launch & Acceptance

## Triggers
- System development/configuration is complete, ready for go-live

---

## Step 1: Pre-Launch Verification

### Final Pre-Launch Checklist (Mandatory for All Projects)

#### Technical Readiness

| # | Check Item | Standard | Pass? |
|---|-----------|----------|:---:|
| 1 | All P0/P1 bugs resolved | P0=0, P1=0 | [ ] |
| 2 | Peak stress test passed | Lunch peak concurrency x1.5 multiplier passed | [ ] |
| 3 | Network outage recovery test passed | Offline mode -> Recovery -> Data sync | [ ] |
| 4 | Data migration complete + verified | Migrated data count = source data count, key fields zero loss | [ ] |
| 5 | DR plan ready | RTO <1 hour, RPO <5 min tested | [ ] |
| 6 | Monitoring & alerts configured | System down / response timeout / payment failure -> Slack / Teams / WhatsApp alerts | [ ] |
| 7 | Rollback plan ready | Can roll back to previous version within 30 minutes | [ ] |
| 8 | All API / interface integration tested | All upstream/downstream system interfaces operational | [ ] |

#### Business Readiness

| # | Check Item | Standard | Pass? |
|---|-----------|----------|:---:|
| 9 | All frontline users trained | 100% training attendance + 100% assessment pass rate | [ ] |
| 10 | Operations manuals delivered | 1-page ultra-minimal version + video tutorials | [ ] |
| 11 | Super users designated | 1-2 "system champions" per location | [ ] |
| 12 | Initial data entry complete | Menu / pricing / members / supplier master data | [ ] |
| 13 | Old/new system parallel run plan confirmed | 1-2 weeks parallel + cutover timing | [ ] |
| 14 | Customer notification (if guest-impacting) | Inform "system upgrade underway, may be slightly slower" | [ ] |

#### Environment Readiness

| # | Check Item | Standard | Pass? |
|---|-----------|----------|:---:|
| 15 | In-store WiFi full coverage | Kitchen / POS / dining area signal strength -65dBm or better | [ ] |
| 16 | Cellular (4G/5G) backup ready | At least 1 cellular router per location | [ ] |
| 17 | Hardware installed + tested | POS / KDS / printers / routers all operational | [ ] |
| 18 | Uninterrupted power | UPS installed and tested | [ ] |

---

## Step 2: Go-Live Execution

### Go-Live Day Schedule (Example: Tuesday 08:00 Go-Live)

| Time | Action | Owner | Notes |
|------|-------|--------|-------|
| **D-1 20:00** | Final all-staff go-live notification (messaging app + in-store posting) | PM | Include go-live day contact numbers |
| **D-Day 07:00** | Project team on-site | All | Client IT + Vendor + On-site support |
| **07:30** | Production deployment / update | Vendor Tech | Verify core functions |
| **08:00** | System cutover -- legacy system set to "read-only" | Vendor | -- |
| **08:15** | New system startup + full workflow test | Both parties | Payment -> KDS -> Print -> Payment |
| **09:00** | Staff arrive -> 5-minute huddle: explain new system | Store Manager + PM | "New system today, don't panic" |
| **09:30** | First batch of test orders | Staff simulation | At least 10 orders covering all payment types |
| **10:00** | Begin serving real guests | All Staff | -- |
| **10:00-11:00** | Low-traffic settling-in | All Staff | Report issues immediately |
| **11:00-14:00** | LUNCH PEAK MONITORING | Full team on-site | Do not leave |
| **14:00-14:30** | Lunch peak debrief (15 min) | PM + Store Manager | What went wrong, how to fix |
| **17:00-21:00** | DINNER PEAK MONITORING | Full team on-site | Do not leave |
| **21:00-21:30** | Day 1 debrief (30 min) | PM + Store Manager + All Staff | Issue list + owner + fix timeline |

### Go-Live Day Roles & Responsibilities

| Role | Responsibility | Must NOT Do |
|------|---------------|-------------|
| Client PM | Overall coordination, decision-making | Must not leave the site |
| Vendor PM | Overall coordination, decision-making | Must not leave the site |
| Vendor Tech | On-site bug fixes | Do not chat with store staff (distracts focus) |
| Client IT | Hardware / network issues, assist vendor | Must be on-site |
| Store Manager | Calm staff emotions, maintain store operations | Do not scold staff for "not knowing how to use it" |
| Super Users (System Champions) | Help colleagues operate, answer simple questions | Must not be impatient |

---

## Step 3: Post-Launch Stabilization Period (1-4 Weeks)

### Issue Response Classification

| Level | Definition | Response Time | Resolution Time | Example |
|-------|-----------|:---:|:---:|---------|
| P0 | System unusable | 15 min | 1 hour | POS down across entire location |
| P1 | Core function unavailable | 30 min | 4 hours | QR ordering unavailable |
| P2 | Partial function degraded | 2 hours | 24 hours | Report data delayed |
| P3 | Minor issue | 8 hours | Next release | UI display bug |

### Daily Debrief Cadence

| Day | Debrief Length | Participants | Focus |
|:---:|:---:|------|------|
| D+1 | 30 min | PM + Full Team + Store Manager | List all issues |
| D+2 | 20 min | PM + Store Manager + Super Users | Top 3 issues |
| D+3~D+5 | 15 min | PM + Super Users | Newly discovered issues |
| D+6~D+14 | 10 min | PM + Super Users | Any more issues? |
| D+15+ | 10 min/week | PM + Store Manager | Usage status + optimization suggestions |

---

## Step 4: UAT (User Acceptance Testing)

### UAT is NOT "let users try it out" -- it's "verify against criteria, one by one"

#### UAT Participants

| Role | Rationale |
|------|-----------|
| Client Business Lead (VP of Ops) | Verify business requirements are met |
| Store Manager Representatives (1-2) | Verify real-world usability |
| Client IT Representative | Verify technical deliverables |
| Client Finance Representative | Verify financial / reconciliation functions |
| Data Owner | Verify data quality and reporting |

#### UAT Scenario Checklist (Every Scenario Must Pass)

```
POS Payment Flows:
[ ] Dine-in order -> Add item -> Remove item -> Settle (with member discount + coupon + points)
[ ] Delivery order received -> Kitchen print -> Order ready -> Driver pickup
[ ] QR code order -> Add to cart -> Pay -> KDS display -> Dish complete

Exception Scenarios:
[ ] Network disconnect -> Offline payment -> Network restore -> Data sync (zero loss)
[ ] Printer out of paper -> Reload -> Auto-resume printing
[ ] Payment failed -> Refund -> Duplicate payment prevention
[ ] Peak concurrency: XX orders/min sustained XX minutes without latency

Reconciliation Scenarios:
[ ] Uber Eats / DoorDash / Dine-in / Private domain orders auto-aggregated
[ ] Daily settlement: cash + online payment three-way reconciliation
[ ] Orders with discrepancy >$XX auto-flagged

Data Scenarios:
[ ] Member data migrated from legacy -> new system (count matches + fields complete)
[ ] Menu data migrated from legacy -> new system (cost cards complete)

Reporting Scenarios:
[ ] Daily / weekly / monthly reports generated within XX minutes
[ ] All platforms (PC / mobile / tablet) display correctly

Permission Scenarios:
[ ] Cashier cannot view cost data
[ ] Store manager cannot modify settled orders
[ ] Regional manager can see all locations within their region
```

#### UAT Sign-Off Process

Only after all UAT scenarios pass and all participants have signed does the project enter the acceptance phase.

---

## Step 5: Formal Acceptance

### Acceptance Deliverables Checklist

| # | Deliverable | Acceptance Criteria | Owner |
|---|------------|---------------------|--------|
| 1 | System Functionality | All UAT scenarios passed + signed | Business Lead |
| 2 | User Documentation | Operations manual (1-page + full version) + video tutorials + FAQ | Vendor |
| 3 | Technical Documentation | Architecture design + API docs + Data dictionary + Deployment guide | Vendor Tech |
| 4 | Operations Manual | Daily monitoring + Fault handling + Backup/recovery + Upgrade procedures | Vendor |
| 5 | Training Materials | Training slides + Assessment questions + List of certified personnel | Vendor |
| 6 | Test Reports | Unit / Integration / Performance / UAT -- all test reports | Vendor QA |
| 7 | Data Migration Report | Migration scope + Data volume + Verification results | Vendor |
| 8 | Source Code (if applicable) | Custom development source code + deployment scripts | Vendor Tech |
| 9 | Licenses / Authorization | Valid license files for all software | Vendor |
| 10 | Operations Handover | Client IT can independently operate + Vendor confirmation | Both IT Teams |

### Acceptance Sign-Off Process

```
Vendor submits acceptance request -> Client IT initial review (within 3 business days)
  -> Pass -> UAT execution (confirm each item against scenario checklist)
    -> All pass -> All UAT participants sign
      -> Client PM compiles acceptance report
        -> Client Project Sponsor final sign-off
          -> Formal acceptance -> Enter maintenance period
```

### Handling Failed Acceptance

If any UAT scenario does not pass:
1. List non-passing items; vendor fixes within a deadline
2. After fixes, re-execute UAT for that scenario only
3. Maximum 3 attempts per scenario (avoid "fix-test-fix-test" death loop)
4. If still failing after 3 attempts -> escalate to Project Steering Committee

---

## Post-Acceptance: Entering the Maintenance Period

### Conditions for Starting Maintenance Period

- [ ] Acceptance sign-off complete
- [ ] System running stably for >=2 weeks (zero P0/P1 incidents)
- [ ] Client IT team capable of independent operations (or vendor maintenance contract in place)
- [ ] Maintenance SLA confirmed and signed

### Post-Acceptance Does NOT Mean the Vendor Can "Withdraw"

| Phase | Duration | Vendor Responsibility |
|-------|:---:|-----------------------|
| Warranty Period | 3-6 months post go-live | Free bug fixes for all issues; on-site or remote support |
| Maintenance Period | After warranty | Service per maintenance contract SLA |

---

## Deliverables
- Final pre-launch checklist (all items passed)
- Go-live execution plan (including hour-by-hour D-Day schedule)
- UAT report (all participants signed)
- Acceptance report (with complete deliverables checklist)
- Operations handover confirmation

## Quality Checks
- [ ] All 18 pre-launch checklist items passed (no "we'll fix it after go-live" mentality)
- [ ] Go-live day schedule is precise to the hour
- [ ] P0 incident response <15 minutes
- [ ] UAT scenarios cover "Normal + Exception + Peak"
- [ ] Acceptance has formal signatures, not verbal "looks good"
