# 01 — Implementation Methodology & PMO

> **Trigger**: Contract signed, project officially launched
> **Deliverables**: Project plan + governance mechanisms + risk management + go-live report + acceptance report

---

## 1. Retail System Implementation — 8 Stages

```
① Project Kickoff → ② Requirements Confirmation → ③ Solution Design → ④ System Configuration / Development →
⑤ Integration & Testing → ⑥ Data Migration → ⑦ Training & UAT → ⑧ Pilot & Rollout
```

| Stage | Core Activities | Duration | Exit Criteria |
|------|------|:---:|------|
| **① Project Kickoff** | Kickoff meeting, team formation, project charter | 1 week | Charter signed |
| **② Requirements Confirmation** | Detailed requirements document, process mapping, gap analysis | 1-2 weeks | Requirements sign-off |
| **③ Solution Design** | Technical solution, architecture design, integration design | 1-2 weeks | Design review approved |
| **④ Configuration / Development** | System configuration, custom development, unit testing | 2-4 weeks | Unit tests passed |
| **⑤ Integration & Testing** | System integration, SIT, performance testing | 2-4 weeks | Integration tests passed |
| **⑥ Data Migration** | Data cleansing, migration scripts, validation | 1-2 weeks | Data validation passed (error <2%) |
| **⑦ Training & UAT** | User training, UAT testing, acceptance sign-off | 2-3 weeks | UAT sign-off |
| **⑧ Pilot & Rollout** | Pilot store go-live → stabilization → full rollout | 4-8 weeks | All stores live + 2 weeks stable operation |

---

## 2. Project Governance

### Three-Tier Governance Structure

| Tier | Composition | Frequency | Responsibilities |
|------|------|:---:|------|
| **Steering Committee** | CEO + CFO + CTO + Sponsor | Monthly / major decisions | Strategic decisions, major changes, resource approval |
| **Project Status Meeting** | PM + Core team + Vendor PM | Weekly | Progress tracking, risk identification, issue resolution |
| **Daily Standup** | Execution team | Daily (critical phases) | Yesterday's progress + today's plan + blockers |

### Project Roles & Responsibilities

| Role | Responsibilities | Commitment |
|------|------|:---:|
| **Project Sponsor** | Strategic decisions, resource assurance, obstacle removal | 5-10% |
| **Project Manager (PM)** | Day-to-day management, progress, risk, communication | 100% |
| **Business Lead** | Requirements confirmation, process decisions, UAT sign-off | 30-50% |
| **Technical Lead** | Technical solution, integration, go-live | 50-100% |
| **Vendor Project Manager** | Vendor-side management, delivery | Per contract |

---

## 3. Retail-Specific Implementation Pitfalls & Countermeasures

| # | Pitfall | Typical Scenario | Countermeasure |
|---|------|------|------|
| 1 | **Underestimating data migration** | "Just export and import the data" → inventory inaccurate, members lost | Pre-audit data → allocate 2-3x time → mandatory migration validation |
| 2 | **Ignoring hardware compatibility** | New POS software doesn't work with old printers / cash drawers | Test all peripherals in advance → prepare compatibility plan |
| 3 | **Unreliable network** | Store 4G/WiFi unstable → POS offline mode doesn't work | Must test offline mode → 4G backup plan |
| 4 | **Go-live during peak season** | Going live during Black Friday / Christmas / holiday season | Absolutely forbidden to go live during peak periods |
| 5 | **Big-bang rollout** | 35 stores go live simultaneously → firefighting everywhere | Pilot → Rollout → Full coverage (minimum 2 weeks stabilization per batch) |
| 6 | **Franchisee system switch** | Can't export data from the legacy system → franchisee revolt | Negotiate data export with legacy vendor in advance → proactive franchisee communication |
| 7 | **Ignoring store equipment differences** | Large and small stores have different hardware needs | Prepare separate hardware plans per store type |
| 8 | **"Drop and run" training** | 1 day of training then go-live → staff can't use it → blame the system | On-site support for at least 1 week → ensure "someone to ask" |

---

## 4. Go-Live Checklist (18 Must-Check Items)

| # | Check Item | Pass Criteria | Status |
|---|------|------|:---:|
| 1 | All functions UAT passed | 100% Must requirements passed | |
| 2 | Performance stress test passed | 3x peak volume, response <2s | |
| 3 | Data migration validation complete | Spot-check error <2% | |
| 4 | All integrations passed | End-to-end tests passed | |
| 5 | Training complete | Pass rate >95% | |
| 6 | SOP operations manual in place | At least 1 copy per store | |
| 7 | Disaster recovery plan ready | Drill completed | |
| 8 | Rollback plan ready | Drill completed (rollback within 30 minutes) | |
| 9 | Go-live approval signed | Sponsor + Business Lead | |
| 10 | Go-live notification sent to all | At least 3 days' notice | |
| 11 | Day 1 on-site support arranged | At least 1 person per store | |
| 12 | Week 1 support arranged | 7×12 hour support | |
| 13 | Help desk / hotline ready | Call answer rate >90% | |
| 14 | Monitoring & alerts ready | CPU / memory / disk / error rate | |
| 15 | Data backup ready | Auto backup + manual backup verified | |
| 16 | Network / power ready | Backup 4G + UPS | |
| 17 | Emergency contact list | Known to all staff | |
| 18 | Go-live sign-off confirmation | All passed → signed → ready to go live | |

---

## 5. Pilot Strategy

### Pilot Store Selection Criteria

| Criteria | Description |
|------|------|
| Representative | Covers major store types (large / small / community / urban) |
| Manageable | Close to HQ, cooperative store manager, moderate foot traffic |
| Low risk | Not a top-revenue store (manageable impact if issues arise) |
| Quantity | 1-3 stores (don't do too many — you can't manage more) |

### Pilot Phases

```
Pilot Go-Live (Week 1-2):
  Day 1: On-site support 12 hours → log all issues
  Day 2-3: Stabilization observation → fix critical issues
  Day 4-7: Daily operations → collect feedback

Stabilization (Week 3-4):
  → 2 consecutive weeks of stable operation
  → Key metrics achieved (checkout speed / inventory accuracy / DAU rate)
  → Pilot success confirmed → ready for rollout

Rollout (Week 5-12):
  → 5-10 stores per batch (no more than support capacity)
  → Each batch stabilizes for at least 1 week before starting the next
```

---

## 6. Acceptance Criteria

### System Acceptance Standards

| Metric | Standard | Measurement Method |
|------|------|------|
| Functional completeness | Must requirements 100% passed | Requirements traceability matrix |
| Performance | 3x peak volume, response <2s | Stress test report |
| Availability | >99.5% | 30-day operations monitoring |
| Data accuracy | Inventory accuracy >95% | Spot-check validation |
| Training pass rate | >95% | Exam scores |
| System DAU rate | >85% | 2 weeks post-go-live system statistics |

Acceptance template: `templates/project-acceptance-report-template.md`

---

## 7. Risk Management

| # | Risk | Probability | Impact | Mitigation |
|---|------|:---:|:---:|------|
| 1 | Data migration quality issues | High | High | Pre-audit data + multiple validation rounds + data rollback plan |
| 2 | User resistance | High | Medium | ADKAR change management + sufficient training + immediate rewards |
| 3 | Integration complexity exceeds estimates | Medium | High | Pre-PoC integration point validation + buffer time |
| 4 | Vendor delivery quality poor | Medium | High | Contractual penalties + weekly acceptance + escalate on schedule slippage |
| 5 | Scope creep | Medium | Medium | Change control process + CR approval required |

---

> Project plan template: `templates/project-implementation-plan-template.md`
