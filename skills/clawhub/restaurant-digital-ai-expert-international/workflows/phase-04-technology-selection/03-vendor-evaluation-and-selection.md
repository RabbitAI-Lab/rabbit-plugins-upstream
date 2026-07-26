# 03-Vendor Evaluation & Selection

## Triggers
- RFP responses have been collected; need to conduct final evaluation and selection decision

---

## Step 1: Form the Evaluation Committee

### Committee Composition (5-7 people)

| Role | Responsibility | Mandatory? |
|------|---------------|:---:|
| Business Lead (e.g., VP of Operations) | Evaluate business requirement fit | Mandatory |
| Technical Lead (CTO / IT Director) | Evaluate technical architecture and scalability | Mandatory |
| Finance Lead | Evaluate TCO and commercial terms | Mandatory |
| Frontline User Representative (Store Manager / Chef) | Evaluate usability and real-world applicability | Mandatory |
| CEO / Owner | Final decision-maker | Mandatory for large projects |
| External Advisor (optional) | Professional supplementation + neutral perspective | Recommended |

> Must include frontline user representatives. Countless restaurant IT projects have died because "management thought it was great but frontline staff couldn't use it."

---

## Step 2: Standardize Scoring Criteria

### Restaurant Vendor 7-Dimension Scoring Matrix

See `tools/restaurant-tech-selection-decision-matrix.md`

**Core 7 Dimensions**:

| Dimension | Weight | 0 (Poor) | 1 (Adequate) | 2 (Good) | 3 (Excellent) |
|-----------|:---:|----------|-------------|---------|---------------|
| **Product Functionality Fit** | 25% | <50% | 50-70% | 70-90% | >90% |
| **Technical Architecture** | 20% | Monolithic / legacy | Early microservices | Mature cloud-native | SaaS + multi-cloud |
| **Restaurant Industry Experience** | 15% | No experience | 1-2 clients | 5+ clients | Same-format benchmark |
| **Company Stability** | 15% | Startup / <10 people | Series A / 20-50 | Series C / 100+ | Public / Profitable |
| **Service & Support** | 10% | Remote only | Regional office | Local team | Dedicated CSM |
| **Integration & Openness** | 10% | No API | RESTful API | Open platform | API + ISV ecosystem |
| **Pricing & TCO** | 5% | >1.5x budget | 1-1.5x budget | Within budget | <80% of budget |

---

## Step 3: Independent Scoring by Each Evaluator

### Scoring Process (Eliminate Bias)

1. **Independent scoring**: Each evaluator scores independently, no discussion, no influence
2. **Standardized scoring**: Use the unified scoring card (see `templates/technology-selection-and-vendor-evaluation-template.md`)
3. **Forced ranking**: Each evaluator must rank 1>2>3>..., no ties allowed
4. **Take the mean**: Remove the highest and lowest scores, take the mean of remaining scores
5. **Weighted calculation**: Apply dimension weights to calculate the total weighted score

### Scoring Cautions

- **Don't be dazzled by demos**: Demos are carefully designed happy paths. Ask "What about scenario XXX?"
- **Don't be intimidated by brand names**: Big brand != right fit (Oracle MICROS for a small independent is a disaster)
- **Don't be seduced by low prices**: Look at TCO, not first-year cost
- **Must make reference calls**: Contact 3 existing clients (not vendor-selected) for real-world experience

---

## Step 4: Client Reference Checks

### Reference Check Question List

| # | Question |
|---|----------|
| 1 | How long have you been using it? How many locations? |
| 2 | What was the biggest pitfall during implementation? |
| 3 | What was the worst system failure you experienced? How long to recover? |
| 4 | Does the vendor's response time truly meet the SLA? (actual experience, not what the contract says) |
| 5 | What "gotchas" did you not anticipate about the system? |
| 6 | Did they raise prices at renewal? By how much? |
| 7 | If you could choose again, would you still pick this vendor? Why? |
| 8 | What features were marketed well but are actually hard to use? |

> Key technique: Question 7 is the "killer question" -- it filters out 90% of "it's okay" responses.
> Don't ask leading questions like "Is the product good?" Ask open-ended questions and let them share specific experiences.

---

## Step 5: PoC / Pilot Validation

### When Is a PoC Needed?

| Situation | PoC Needed? |
|-----------|:---:|
| Contract value >$200K | Mandatory |
| Involves core system replacement (POS / CRM) | Mandatory |
| Vendor founded <3 years / first-time partnership | Mandatory |
| Contract value <$20K and is a supplementary system | Optional |
| Market-recognized mature product (e.g., Toast POS) | Optional |

### PoC Design Principles

```
A PoC is not "try it out" -- it's "validate key assumptions under extreme conditions"

Correct approach:
- Select 1-3 locations (include the busiest and most remote)
- Real operations for 2-4 weeks
- Use real order volumes (no "test environments")
- Cover core scenarios comprehensively (peak / offline / refunds / reconciliation...)
- Define "pass criteria": e.g., POS handles 100 orders/min peak concurrency without lag
```

### PoC Pass Criteria Template

| Test Scenario | Pass Criteria | Actual Result | Pass? |
|--------------|---------------|---------------|:---:|
| Lunch peak payment | 60 orders/min sustained 30 min without lag | | |
| Network outage | Offline mode processes payments normally, no data loss on recovery | | |
| Cross-platform reconciliation | Uber Eats + DoorDash + dine-in auto-reconciliation, discrepancy <0.1% | | |
| Member data migration | 100K member records migrated, zero loss | | |
| Concurrent logins | 50 accounts login simultaneously without timeout | | |
| Report generation | 100-location daily report generated within 5 minutes | | |

---

## Step 6: Negotiation & Contract

### Negotiation Strategy

| Negotiation Point | Target | Leverage | Bottom Line |
|-------------------|--------|----------|-------------|
| Price | Get the best price | "We're still evaluating vendor X" | Budget ceiling |
| Payment schedule | 3:3:3:1 | "Pay 30% upfront, 30% at go-live" | 4:3:3 |
| Service | Dedicated Customer Success Manager | "Your service terms fall short of vendor X" | Standard service acceptable |
| SLA | Demand penalty clauses | "Restaurant peak downtime is existential" | Non-binding SLA without penalties unacceptable |
| Data | Data belongs to us + exportable anytime | "Data sovereignty is our bottom line" | Non-negotiable |
| Termination | No penalty, complete data export | "We refuse to be locked in" | Non-negotiable |

### Contract Review Checklist (Legal + Advisor Joint Review)

- [ ] Data ownership explicit (client data belongs to client, not vendor)
- [ ] Termination clause clear (notice period, data export process, whether penalties apply)
- [ ] SLA has actual enforceability (monitoring method + penalty provisions)
- [ ] Renewal price increase limitation clause (avoid "signed 1 year, year 2 price jumps 50%")
- [ ] Intellectual property terms (IP ownership for custom development)
- [ ] Vendor acquisition or insolvency data migration plan
- [ ] Dispute resolution venue in client's jurisdiction (not vendor's HQ jurisdiction)
- [ ] GDPR / applicable data protection law compliance

---

## Step 7: Final Selection Report

### Report Structure

```
1. Project Overview
2. Evaluation Process Recap
3. Vendor Score Summary (including scoring matrix)
4. SWOT Analysis per Vendor
5. Reference Check Results Summary
6. PoC Results (if conducted)
7. Recommendation Ranking (1st choice and 2nd choice)
8. Recommendation Rationale (3 core points)
9. Risk Assessment (Top 3 risks + mitigation measures)
10. Next-Step Action Recommendations
```

---

## Special Scenario Guidance

### Scenario 1: Two Vendors with Very Close Scores (<5% Gap)

Use the following tiebreaker sequence:
1. Reference check results (most authentic)
2. Restaurant industry focus (more specialized > more general)
3. Service response speed (local team > remote support)
4. Company financial health (survives 3 years > burning cash for growth)

### Scenario 2: The Owner Has a "Relationship" with a Specific Vendor

Handling approach:
- Don't reject outright (don't challenge the owner's relationships)
- Method: Have the "relationship vendor" also go through the complete evaluation process and score alongside others
- If the relationship vendor genuinely scores highest -> No problem, select them (everyone wins)
- If the relationship vendor scores last -> Place the scoring matrix in front of the owner, let the data speak
- Experience: In 80% of cases, the data will lead the owner to change their mind themselves

### Scenario 3: The Affordable Vendor Scores Poorly, the Top Scorer Is Too Expensive

Handling approach:
- Expand RFP scope to find mid-range new vendors
- Negotiate with both top scorers simultaneously (let them compete)
- Re-examine requirement priorities, cut "nice-to-have" items to reduce total cost

---

## Deliverables
- Vendor scoring matrix (7-dimension weighted)
- Client reference check report
- PoC test report (if applicable)
- Final selection report + recommendation

## Quality Checks
- [ ] Every evaluator scored independently, with scoring cards archived
- [ ] Reference check calls were made for every shortlisted vendor
- [ ] Core systems underwent PoC with documented pass criteria
- [ ] Final selection report includes Top 3 risks + mitigation measures
- [ ] Contract data ownership clause has been confirmed
