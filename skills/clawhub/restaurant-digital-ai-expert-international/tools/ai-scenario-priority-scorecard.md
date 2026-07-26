# AI Scenario Priority Scorecard (Standalone Tool)

## Tool Description

This tool enables rapid evaluation and prioritization of restaurant AI use cases. Includes: scoring rubric, format-based default recommendations, and implementation guidance.

---

## Step 1: List Scenarios

List all AI application scenarios under consideration:

| # | Scenario Name | Brief Description |
|---|---------------|-------------------|
| 1 | [e.g., AI Voice Ordering] | [e.g., Voice-based drive-thru ordering replacing staff] |
| 2 | [...] | [...] |
| 3 | [...] | [...] |
| ... | ... | ... |

---

## Step 2: RICE+ Scoring

Score each dimension 1-5:

| Score | R - Reach | I - Business Impact | C - Confidence / Feasibility | E - Effort (lower is better) | + AI Fit |
|:---:|-----------|---------------------|------------------------------|------------------------------|----------|
| 1 | Single role | Annual <$5K | Technology immature | >12 months / >$200K | Better without AI |
| 2 | 1-2 stores | <1% improvement | Limited case studies | 6-12 months / $50-200K | AI is helpful |
| 3 | 30-60% of stores | 1-5% improvement | Multiple case studies | 3-6 months / $20-50K | AI among best options |
| 4 | 60-90% of stores | 5-15% improvement | Mature technology | 1-3 months / $5-20K | AI is best solution |
| 5 | All stores | >15% improvement | Off-the-shelf products | <1 month / <$5K | AI is indispensable |

Scoring table:

| Scenario | R (25%) | I (30%) | C (20%) | E (15%) | +AI (10%) | **Total** | Rank |
|----------|:---:|:---:|:---:|:---:|:---:|--------|:---:|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

> E is reverse-scored (higher = harder). Convert to (6 - E) or equivalent before multiplying weight.

---

## Step 3: Format-Based Default Recommendations

| Format | P0 - Immediate | P1 - Short-Term | P2 - Medium-Term |
|--------|----------------|-----------------|------------------|
| Street Food / Single Store | AI customer service, delivery AI | -- | -- |
| Independent Casual (1-3) | Loyalty AI recommendations, AI CS | Demand forecasting, sentiment analysis | AI ordering |
| Tea & Coffee (1-10) | In-app AI recommendations, precision loyalty marketing | Demand forecasting, AI scheduling | Dynamic pricing |
| Hot Pot (1-50) | Queue wait-time AI prediction, loyalty AI | AI scheduling, demand forecasting | AI kitchen QA |
| QSR Chain (10+) | Voice AI, demand forecasting, AI scheduling | AI visual QA, dynamic pricing | Full-chain AI |
| Fine Dining (1-10) | AI guest profiles, personalized experience | Sentiment analysis, intelligent CS | AI menu pairing |
| Catering / Institutional (1-500) | Food safety AI, demand forecasting | AI scheduling, energy optimization | Kitchen automation |
| Cloud Kitchen (1-100) | Demand forecasting, AI pricing | Multi-platform AI operations | AI visual QA |
| Franchise Chain (100+) | Demand forecasting, AI franchisee diagnostics | AI inspection / audit | AI full-chain |
| Global 10K+ Stores | Full-stack AI continuous rollout | New scenario validation | Autonomous operations |

---

## Step 4: Implementation Roadmap

### If you selected 1 P0 scenario:
```
Week 1-2:   Data preparation + vendor/team finalization
Week 3-6:   MVP development + internal testing
Week 7-8:   Pilot in 1-2 stores
Week 9-12:  Evaluate results -> Optimize -> Expand rollout
```

### If you selected 2-3 P0 scenarios:
```
Month 1-2:  Scenario 1 (fastest to show results) -> Validate -> Deliver
Month 2-4:  Scenario 2 (reuse learnings/methodology from Scenario 1)
Month 3-6:  Scenario 3
```

> **Golden Rule**: It is better to do 1 scenario exceptionally well (>80% adoption, positive ROI) than 3 scenarios at 60% each.

---

## Typical Deliverables

After completing scoring, output:
1. **Priority Matrix** (P0 / P1 / P2 / P3)
2. **1-page ROI estimate per P0 scenario**
3. **3-month implementation plan**
4. **Success metric definitions**

---

> **Reminder**: AI is not the goal -- ROI is. No matter how high a scenario scores, if the ROI does not work out, it is not worth pursuing. Conversely, a high-ROI scenario is worth serious evaluation even if its score is only moderate.
