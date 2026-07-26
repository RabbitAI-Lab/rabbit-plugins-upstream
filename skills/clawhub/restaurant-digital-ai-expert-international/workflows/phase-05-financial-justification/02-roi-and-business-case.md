# 02-ROI & Business Case

## Triggers
- After the TCO model is established, build an ROI analysis to support the investment decision

---

## Restaurant Digital ROI Analysis Framework

### Benefit Panorama (5 Categories)

```
ROI = (Cost Reduction Benefits + Efficiency Benefits + Revenue Growth Benefits + Risk Mitigation Benefits + Strategic Value)
     / Total TCO Investment
```

---

## Step 1: Benefit Quantification

### Benefit Category 1: Cost Reduction (Easiest to Quantify)

| Cost Reduction Item | Quantification Method | Unit of Calculation |
|---------------------|----------------------|---------------------|
| Server staff reduction | (Original headcount - New headcount) x Annual salary | Per location |
| Cashier reduction | Cashier role halved after QR ordering adoption x Annual salary | Per location |
| Food waste reduction | (Original waste rate - New waste rate) x Monthly purchases x 12 | Per location / per month |
| Delivery commission reduction | Private domain order share increase x (Uber Eats commission rate - private domain rate) | Per order |
| Reconciliation time reduction | (Original hours - New hours) x Manager hourly rate x Locations x 365 | Per location |
| Printing / materials reduction | Digital menus replace paper x Safety stock x 12 | Per location |

### Benefit Category 2: Efficiency Gains

| Efficiency Item | Quantification Method | Notes |
|-----------------|----------------------|-------|
| Table turn improvement | Additional daily turns x Average check x Seats x 365 | Relatively easy to quantify |
| Kitchen speed improvement | Additional peak-hour output x Average check x Peak hours | KDS impact |
| Labor efficiency improvement | Change in Revenue / Headcount | Composite metric |
| Inventory turnover acceleration | Days reduction in turnover x Average daily inventory value | Reduced working capital |

### Benefit Category 3: Revenue Growth

| Revenue Growth Item | Quantification Method | Notes |
|--------------------|----------------------|-------|
| Member spend increase | Monthly member spend increase x Member count x 12 | CRM impact |
| Repeat purchase rate increase | Additional repeat orders x Average check x Active customers | Targeted marketing |
| Average check increase | (New avg check - Old avg check) x Monthly orders x 12 | Recommendation algorithms |
| Private domain order growth | New private domain orders x Average check x 12 | Lower commission + more revenue |
| New location profitability acceleration | Months earlier to profitability x Average monthly profit x New locations/year | Site selection + standardization |

### Benefit Category 4: Risk Mitigation

| Risk | Mitigation Benefit Quantification | Probability |
|------|----------------------------------|:---:|
| Food safety incident | Reduced incident probability x (Average claim cost + brand damage) | Annual probability |
| Data loss | (1 - Recovery probability) x Data reconstruction cost | Annual probability |
| Franchisee default | Bad debt reduction x Probability | -- |
| Procurement fraud | Abnormal purchase amount reduction x Probability | -- |

### Benefit Category 5: Strategic Value (Qualitative -> Quantitative Translation)

| Strategic Value | Quantification Approach |
|-----------------|------------------------|
| Brand digital image | "Increased franchisee attractiveness -> Franchise fee can increase by X%" |
| Data asset value | "Data-driven decisions reduce major mistakes = average annual savings of $Y" |
| Organizational capability | "In-house IT team capability -> Reduce external procurement = annual savings of $Z" |

---

## Step 2: Core ROI Calculation

### Basic Formulas

```
Annual ROI = (Annual Digital Benefits - Annual Digital Costs) / Annual Digital Costs x 100%

Payback Period = Cumulative Investment / Annualized Net Benefits

NPV (3-Year) = Sum[(Year Benefits - Year Costs) / (1 + Discount Rate)^n] - Initial Investment
```

### Suggested Discount Rates

| Enterprise Type | Suggested Discount Rate | Rationale |
|-----------------|:---:|-----------|
| Independent / Small | 8-10% | Benchmark against small business loan rates |
| Regional Chain | 10-12% | Benchmark against restaurant industry average cost of capital |
| National Chain | 10-15% | Accounting for higher opportunity cost |
| VC-Backed Brand | 15-25% | Venture-stage risk profile |

---

## Step 3: Sensitivity Analysis

### Must Test 3 Scenarios

| Scenario | Cost Assumption | Benefit Assumption | Use |
|----------|----------------|-------------------|-----|
| Optimistic | Costs within budget | Benefits meet expectations | Target scenario |
| Baseline | Costs 15% over budget | Benefits at 80% of expectations | Most relevant for decisions |
| Pessimistic | Costs 30% over budget | Benefits at 50% of expectations | Decision floor |

### Sensitivity Test Variables

Test the following variables' impact on ROI:

| Variable | Test Range |
|----------|------------|
| Software subscription price increase | +10% / +20% / +30% |
| Slower location rollout | 1-3 fewer locations per month |
| Longer employee learning curve | Efficiency recovery time +50% |
| Delayed benefits | Benefit realization delayed 3-6 months |
| Key employee departure | IT Manager / Data Analyst departure = 3-month gap |

---

## Step 4: ROI Report Structure

### Standard ROI Report (5 Pages)

```
Page 1: Executive Summary
  - Total Investment: $XXX K (3-year)
  - Annualized Benefits: $XXX K
  - 3-Year ROI: XX%
  - Payback Period: XX months
  - Core Conclusion + Key Assumptions

Page 2: TCO Investment Breakdown
  - Investment breakdown by year / by category
  - Pie chart + bar chart

Page 3: Benefit Analysis
  - Breakdown by 5 benefit categories
  - Quantification basis and assumptions for each benefit item

Page 4: Sensitivity Analysis
  - ROI results under 3 scenarios
  - Identification of most critical variables

Page 5: Recommendation & Next Steps
  - Whether to recommend investment
  - Risk mitigation measures
  - How to track actual ROI
```

---

## Restaurant Digital ROI Industry Benchmarks

| Project Type | Typical ROI | Typical Payback | Reference |
|-------------|:---:|:---:|------|
| POS / KDS deployment | 150-250% | 6-12 months | Most predictable |
| QR code ordering | 200-400% | 3-6 months | Highest ROI |
| CRM / Loyalty | 100-200% | 12-18 months | Mid-term impact |
| Supply chain system | 80-150% | 18-24 months | Slow but sustainable |
| BI / Data analytics | 50-100% | 12-24 months | Hard to quantify but high value |
| AI demand forecasting | 100-200% | 12-18 months | Data quality determines success |
| Private domain operations | 150-300% | 6-12 months | Execution is key |

> Source: National Restaurant Association 2024 industry survey + compiled SaaS vendor case studies

---

## Deliverables
- ROI analysis report (5-page standard structure)
- Sensitivity analysis (3 scenarios + 5 variables)
- Payback period analysis

## Quality Checks
- [ ] Every benefit item has a clear quantification formula and assumptions (not "save $100K/year" out of thin air)
- [ ] ROI under the conservative scenario is still positive (or acceptable)
- [ ] Payback period is within an acceptable range
- [ ] Sensitivity analysis covers the most critical uncertainties
- [ ] Report structure is clear -- the CEO should grasp the key numbers at a glance
