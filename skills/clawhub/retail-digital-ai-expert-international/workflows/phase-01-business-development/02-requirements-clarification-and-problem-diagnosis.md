# 02 — Requirements Clarification & Problem Diagnosis

> **Trigger**: Client shows initial interest after first communication
> **Prerequisites**: Client communication notes + publicly available information
> **Deliverables**: Problem diagnosis report (3-5 pages) + preliminary recommendations

---

## 1. MECE Five-Dimension Diagnostic Framework

Decompose the client's problems using MECE (Mutually Exclusive, Collectively Exhaustive) across five dimensions:

### Dimension 1: Traffic (Customer Flow)

| Checkpoint | Diagnostic Question | Digital Attribution |
|------|------|------|
| Foot traffic | Average daily footfall? Store entry rate? | AI site selection, footfall analytics |
| Online traffic | Website UVs? E-commerce visitors? | SEO/SEM, content marketing, platform traffic |
| Member reach | How many members can you reach? Reach rate? | Member base, marketing automation reach rate |
| Delivery/O2O traffic | Uber Eats / DoorDash / Deliveroo exposure? | O2O platform presence, ratings, delivery coverage |
| Competitive diversion | What new stores opened nearby? | Competitive monitoring, differentiation |

### Dimension 2: Conversion Rate (Transaction Issues)

| Checkpoint | Diagnostic Question | Digital Attribution |
|------|------|------|
| Product strength | Is category mix reasonable? SKU breadth/depth? | Category analysis, ABC analysis, price bands |
| Merchandising | Are displays appealing? Is store flow logical? | Planogram, heat maps, AI visual merchandising |
| Pricing | Is pricing competitive? Are promotions effective? | Competitive price benchmarking, dynamic pricing, promo ROI |
| Sales associates | Do associates know what customers want? | AI-guided selling, customer profiles, product knowledge base |
| Experience | Is checkout fast? Are there queues? Is the environment good? | POS speed, self-checkout, in-store IoT |

### Dimension 3: Average Transaction Value (Value Issues)

| Checkpoint | Diagnostic Question | Digital Attribution |
|------|------|------|
| Units Per Transaction (UPT) | How many items per transaction on average? | Smart recommendations, cross-merchandising |
| Category upgrade | Are customers buying premium or entry-level? | Price band analysis, category migration |
| Member value | Member ATV vs. non-member? | CDP tagging, member segmentation, loyalty design |

### Dimension 4: Gross Margin (Profit Issues)

| Checkpoint | Diagnostic Question | Digital Attribution |
|------|------|------|
| Procurement cost | Are your purchasing costs higher than competitors? | SRM, centralized procurement platform, supplier price comparison |
| Shrinkage | What's your shrinkage rate? Causes? | Expiry management, AI loss prevention, shrinkage analysis |
| Over-promotion | What % of sales are on promotion? Is it excessive? | Promo ROI analysis, over-promotion alerts |
| Underpricing | Is your pricing strategy too conservative? | Pricing models, margin analysis |

### Dimension 5: Cost Structure (Efficiency Issues)

| Checkpoint | Diagnostic Question | Digital Attribution |
|------|------|------|
| Labor cost | Revenue per employee? Scheduling efficiency? | AI scheduling, self-checkout, workforce productivity BI |
| Inventory cost | Inventory turnover? Slow-moving inventory %? | Smart replenishment, demand forecasting, inventory optimization |
| Rent | Sales per square foot? | Productivity BI, store optimization |
| Energy | Are utility costs reasonable? | IoT energy management |
| IT cost | IT spend as % of revenue? System redundancy? | TCO analysis, system consolidation |

---

## 2. Three-Step Diagnostic Method

### Step 1: Data Collection (1-3 days)

| Data Type | Specific Data | Source |
|------|------|------|
| Financial data | Revenue / gross margin / net profit / cost breakdown (12 months) | Accounting system / Excel |
| Operational data | Foot traffic / ATV / conversion rate / UPT / turnover (12 months) | POS / ERP |
| Product data | SKU count / categories / ABC classification / sell-through rate / out-of-stock rate | Inventory management |
| Member data | Member count / repurchase rate / churn rate / stored value | CRM |
| System data | System inventory / utilization rate / satisfaction | IT |

### Step 2: Problem Identification (1-2 days)

Use the 5-Whys method to reach root cause:

```
"Inventory is inaccurate" →
  Why? → "Cycle counts are not timely" →
  Why? → "Staff find it too cumbersome" →
  Why? → "A full count takes 2 hours" →
  Why? → "No handheld scanners, everything is manual pen and paper" →
  Why? → "Owner doesn't see the need to buy scanners"

Root cause: Not "inventory inaccuracy" — it's "owner doesn't understand the cost of the problem"
```

### Step 3: Quantify Impact (1 day)

Calculate "the cost of not solving" for each problem:

| Problem | Quantified Calculation | Annual Loss |
|------|------|:---:|
| Inventory inaccuracy | 80% accuracy → oversell / stockout / shrinkage: [$X]K inventory × 15% deviation | $[X]K |
| No membership program | Cannot reach repeat customers → low repurchase rate: monthly revenue × repurchase gap × margin | $[X]K |
| Manual reconciliation | Store manager 30 min/day × 365 days × $[X]/hr | $[X]K |

---

## 3. Diagnosis Report Structure (3-5 pages)

```
Page 1: Key Findings (1-sentence conclusion + TOP 3 problems + total cost of inaction)
Page 2: MECE Five-Dimension Analysis (five-dimension radar chart + key gaps)
Page 3: Root Cause Analysis (5-Why root causes for 3-5 core problems)
Page 4: Preliminary Recommendations (3 directions + investment/return estimates)
Page 5: Suggested Next Steps (detailed diagnostic / selection / pilot)
```

---

## 4. Common Pitfalls

1. **Too many problems**: Listing 20 problems → client doesn't know what to solve first → focus on TOP 3
2. **No quantification**: "Inefficient" → client doesn't understand → "30 minutes wasted daily = $[X] annual loss"
3. **Shallow attribution**: "POS is too old" → Why haven't they replaced it? → Root cause: "Owner doesn't know how much better a new POS is"
4. **Solutions too early**: Recommending specific systems during diagnosis → confirm the problem before prescribing the medicine
