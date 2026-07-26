# 02 — Vendor Evaluation & Selection

> **Trigger**: Short-list confirmed (3-4 vendors), entering deep evaluation
> **Deliverables**: 7-dimension scoring report + PoC report + customer reference check records + final recommendation

---

## 1. Vendor Evaluation Full Process

```
RFP Issued → 7-Dimension Scoring → Demo Validation → PoC Validation → Customer Reference Checks → Contract Review → Final Decision
  (1 week)      (1 week)             (1 week)         (2-3 weeks)           (1 week)                 (1 week)          (1 day)
```

---

## 2. Seven-Dimension Scoring Matrix

Detailed tool: see `tools/retail-technology-selection-decision-matrix.md`

### Summary Scoring Table

| Vendor | Format Fit (25) | TCO (20) | API (15) | Omnichannel (12) | Implementation (10) | Stability (10) | Compliance (8) | **Total** |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | | | | | | | | |
| B | | | | | | | | |
| C | | | | | | | | |

### Scoring Practical Advice

- **Format Fit**: Have 2-3 business users (store manager / procurement / operations) watch the demo together and score
- **TCO**: Require vendors to break down pricing line by line — never accept a "lump-sum" quote; you won't know where the money is going
- **API**: Have a technical person audit the API documentation + test-call at least 3 critical endpoints
- **Stability**: Never accept "we're very stable" — demand data: (1) P0 incident count and duration over the past 12 months (2) SLA attainment rate

---

## 3. PoC Validation (Mandatory for Core Systems)

### PoC Objective
Validate system performance under "real business scenarios + real data + real load."

### PoC Checklist

| Validation Scenario | Method | Pass Criteria |
|------|------|------|
| Core business scenarios (at least 5) | Run complete workflows with real business data | 5 scenarios, 3 runs each, 0 errors |
| Peak performance stress test | Simulate 3x peak transaction volume | Checkout response <2 seconds |
| Key integration validation | Integrate with 1-2 core existing systems | Accurate bidirectional data sync |
| Staff user experience | Real staff trial for 2 days | Satisfaction >80%, operation speed not slower than current system |
| Offline capability | Network down for 30 min → restore | No data loss + auto-sync |
| Exception scenarios | Power outage / network disconnect / erroneous input | System does not crash + data consistency maintained |

### PoC Pass Criteria

- Must-haves: >=90% pass
- Should-haves: >=70% pass
- Zero P0-level defects

---

## 4. Customer Reference Checks

### Reference Targets
- At least 2 customers of similar scale / retail format
- At least 1 customer with >12 months of usage (can tell you about long-term issues)
- Ideally 1 customer who migrated from a competitor (can tell you about switching costs)

### Reference Check Question List

| Category | Question |
|------|------|
| Satisfaction | "On a scale of 1-10, how would you rate this system / vendor? Why?" |
| Pain Points | "What gives you the biggest headache?" |
| Hidden Costs | "Did you actually spend more than the quote? Where did the extra costs come from?" |
| Implementation | "They promised go-live in 3 months — how long did it actually take?" |
| Service | "How quickly are issues resolved? Fastest P0 resolution time?" |
| Renewal | "Will you renew when the contract is up? Why / why not?" |
| Advice | "If you could choose again, would you still pick them? What would you tell your past self?" |

---

## 5. Contract Review — Key Clauses

| Clause | Recommended Minimum | Why |
|------|------|------|
| **SLA** | Availability >=99.5%, written into the contract | Service without SLA = no guarantee |
| **Response Time** | P0: 15-min response + 2-hour resolution | POS down = business down |
| **Penalties** | SLA breach → monthly fee reduction / per-incident compensation | SLA without teeth = no SLA |
| **Exit Clause** | Complete data export within 30 days (standard format), zero cost | Your data is yours; no lock-in |
| **Data Ownership** | Explicitly state all data belongs to the client | Vendor using your data to train their AI → that's additional value exchange |
| **Price Increase Cap** | Annual increase <=5% or CPI+3% (whichever is lower) | Prevent cheap years 1-3, then double in year 4 |
| **Implementation Delay** | Vendor-caused delay → daily penalty of 0.1% of contract value | Deadline without penalty = no deadline |
| **Source Code Escrow** | If vendor goes bankrupt / discontinues → source code escrow release | Protect your investment |
| **Jurisdiction** | Client's local jurisdiction | Cross-border litigation is extremely expensive |

---

## 6. Final Decision Report Structure

Template: see `templates/technology-selection-and-vendor-evaluation-template.md`

```
1. Selection overview
2. Requirements summary
3. Candidate vendors
4. 7-dimension scoring matrix
5. TCO comparison (3-year / 5-year)
6. PoC results
7. Customer reference check summary
8. Risk assessment
9. Final recommendation + rationale
```

---

## 7. Common Pitfalls

1. **Being dazzled by vendor "big-name" client lists**: They served Walmart but that doesn't mean they'll serve you well
2. **Over-focusing on feature count**: More features != better fit → focus on Must-have requirements
3. **Ignoring the implementation team**: The pre-sales team you met before signing was impressive, but the implementation team changes after signing → meet the implementation team
4. **Not reading the contract fine print**: Auto-renewal clauses, price escalation clauses, data usage clauses may be hidden in appendices
