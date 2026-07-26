# 01-Operations Optimization & Value Tracking

## Triggers
- Beginning 3 months after system go-live and entering the operations phase, execute on a regular cadence

---

## Step 1: Establish the Digital Health Dashboard

### System Health Metrics (Monthly Tracking)

| Metric Category | KPI | Target | Warning Threshold |
|----------------|-----|:---:|:---:|
| **Availability** | System uptime | >=99.9% | <99.5% |
| **Availability** | P0 incidents / month | 0 | >=1 |
| **Availability** | Mean time to recovery | <1 hour | >2 hours |
| **Adoption** | Location daily active rate (>=1 transaction completed) | >95% | <85% |
| **Adoption** | Core feature usage rate (QR ordering, loyalty, etc.) | >80% | <60% |
| **Data Quality** | Daily revenue data completeness (auto-collected vs. manual) | >95% | <90% |
| **Data Quality** | Member data field completeness | >90% | <75% |
| **Satisfaction** | Location user satisfaction (quarterly survey) | >4.0/5 | <3.5/5 |
| **Satisfaction** | IT ticket average resolution time | <24 hours | >48 hours |
| **Value** | Digital ROI (tracked quarterly) | >=80% of business case target | <50% of business case target |

### Data Quality Is the Foundation of Digital Health

| Common Data Quality Issue | Root Cause | Fix |
|--------------------------|------------|-----|
| Location daily revenue doesn't match POS | Manual edits / delayed entry | Auto-collection + discrepancy alerts |
| Menu item names inconsistent across locations | No master data standard | Establish menu item master data + coding standards |
| Member phone numbers largely empty / incorrect | Staff fills in whatever / "didn't bother to ask" | Phone verification + completeness incentive |
| Inventory data significantly different from actual | Infrequent / careless stocktaking | Mobile stocktaking + variance KPI + accountability |
| Different systems' data doesn't reconcile | Interface not configured / delayed | Auto-reconciliation + auto-flag discrepancies |

---

## Step 2: Value Tracking

### Track Whether the Original ROI Promises Are Being Fulfilled

#### Quarterly Check

| Originally Promised Benefit | Actual Result | Gap | Root Cause Analysis | Improvement Action |
|---------------------------|---------------|:---:|--------------------|--------------------|
| Labor efficiency +10% | +7% actual | -3% | 2 locations have low system usage | Strengthen training + store manager incentive |
| Reconciliation time: 30 min/day saved | 25 min saved | -5 min | Some manual adjustments still needed | Optimize reconciliation rules |
| ... | ... | ... | ... | ... |

### Common Reasons Value Falls Short

| Reason | Symptom | Countermeasure |
|--------|---------|----------------|
| System used, but not used correctly | Only the most basic features used | Deep training + benchmark case sharing |
| Poor data quality -> nobody trusts the system | Reports are inaccurate | Data governance initiative |
| Business changes -> old configuration no longer fits | Business evolved but system config didn't | Regular system configuration audit |
| No clear KPI driving behavior | Can't see difference between using and not using | Embed digital KPIs into performance evaluation |
| Change management wasn't thorough enough | Frontline resistance continues | Re-initiate change management |

---

## Step 3: Continuous Improvement Flywheel

```
           Measure Current State
                   |
         +---------+---------+
         |                   |
    Optimize Process    Find Bottlenecks (Data-Driven)
         |                   |
         +---------+---------+
                   |
           Develop Improvement Plan

One full flywheel rotation = 1 quarter
Each rotation -> Digital maturity increases by ~0.2 level
```

### 5 Must-Ask Questions Every Quarter

| # | Question | Who Answers |
|---|----------|-------------|
| 1 | This quarter, how much did the system save us / earn us? | CIO / IT Manager |
| 2 | Which location uses the system best? Worst? Why? | VP of Operations |
| 3 | What is the current biggest data quality issue? What decision did it affect? | Data Owner |
| 4 | What are the top 3 frontline complaints about the system? | Regional Manager |
| 5 | What new digital moves are competitors making? Are we falling behind? | Strategy / Market Intelligence |

---

## Step 4: System Optimization Requirements Management

### Requirements Collection Channels

| Channel | Method | Frequency |
|---------|--------|-----------|
| Location Feedback | "System Venting Channel" (messaging group: 1 designated person per location can post) | Anytime |
| Data Discovery | Modules with low usage rates -> Why is nobody using them? | Monthly |
| Competitive Analysis | Competitor app / loyalty program experience comparison | Quarterly |
| Consumer Feedback | Customer complaints: "Your XX process is way too complicated" | Anytime |
| Vendor Updates | SaaS vendor new feature releases | Per vendor cadence |

### Requirements Prioritization (Maintenance Mode vs. Build Mode)

| Requirement Type | Handling Approach | Response Time |
|-----------------|-------------------|:---:|
| Bug Fixes | Fix immediately | P0: 1h, P1: 4h |
| Small Optimizations (1-3 dev days) | Bundle into bi-weekly releases | 2-4 weeks |
| Medium Optimizations (1-4 weeks) | Allocate 30% of dev capacity | Per quarter |
| Large Features / Modules | Include in next phase project planning | Per Phase 2 project initiation |

---

## Step 5: Vendor Relationship Management

### Annual Vendor Health Check

| Check Dimension | Green (OK) | Yellow (Watch) | Red (Act) |
|----------------|------------|---------------|-----------|
| SLA Compliance | 12 consecutive months compliant | Any 1 month non-compliant | 2 consecutive months or P0 non-compliant |
| Product Updates | Quarterly updates + annual major version | 6 months no update | 1 year no feature update |
| Company Financials | Steady growth | Funding slowing | Layoffs / mounting losses / negative news |
| Service Team | Core team stable | 1 CSM change | Large-scale team replacement |
| Renewal Attitude | Proactively engaged | No proactive contact | Attitude deterioration |

### Vendor Red-Flag Action Plan

```
When a red flag is triggered:
1. Within 2 weeks: Meet with vendor executive leadership to understand the real situation
2. Initiate "Plan B" (backup vendor) pre-evaluation (do not inform the current vendor)
3. Ensure data has complete export + backup
4. Contract level: Confirm exit clause + data migration clause are executable
5. If necessary, initiate formal vendor replacement process
```

---

## Step 6: Knowledge Management & Handover

### Prevent "When the person leaves, the knowledge leaves too"

| Knowledge Asset | Management Approach | Update Frequency |
|-----------------|--------------------|:---:|
| System Operations Manual | Documentation + drills | After every change |
| FAQ / Common Issues | Online knowledge base (Notion / Confluence / SharePoint) | Monthly |
| Training Materials | Recorded videos + assessment question bank | After every new feature release |
| Vendor Contact Info | Centralized management (not personal messaging apps) | As needed |
| Decision Memos | "Why we chose this CRM vendor at the time" | After every major decision |

---

## Deliverables
- Digital health dashboard (monthly / quarterly)
- Value tracking report (quarterly)
- System optimization requirements list (prioritized)
- Vendor health assessment report (annual)

## Quality Checks
- [ ] Dashboard is not just "created" -- someone is "actively watching" it (named owner)
- [ ] Value tracking compares original ROI promises vs. actual results
- [ ] Every optimization requirement has clear priority and expected benefit
- [ ] Vendor health is assessed (don't wait until the vendor goes under to start looking)
- [ ] Knowledge management has basic mechanisms in place (prevent key-person departure = digital regression)
