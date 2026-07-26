# 01 — TCO & ROI Modeling

> **Trigger**: Selection results confirmed; financial justification needed
> **Deliverables**: TCO model + ROI calculation + sensitivity analysis

---

## 1. TCO Modeling Framework

### 1.1 Seven Cost Categories

| # | Cost Category | What's Included | Estimation Method |
|---|------|------|------|
| 1 | **Software / SaaS** | License fees / subscriptions / annual fees / add-on modules | Vendor quotes |
| 2 | **Hardware** | POS terminals / servers / networking / tablets / handheld scanners / ESL / IoT | Vendor quotes + market pricing |
| 3 | **Implementation & Deployment** | Installation / configuration / deployment / testing | Vendor quote × 1.2 (buffer) |
| 4 | **Integration & Customization** | API integrations / custom development / data migration | Implementation partner quote + self-estimate 20% extra |
| 5 | **Training & Change** | Training fees / productivity loss during training / change communication | Training quote + productivity loss = 1-2 weeks of 20-40% revenue reduction |
| 6 | **Ongoing Operations** | Annual maintenance / upgrades / technical support / cloud resources | Annual fee typically = 15-22% of software cost |
| 7 | **Hidden Costs** | System cutover disruption / learning curve / data cleansing / future exit | See table below |

### 1.2 Quantifying Hidden Costs

| Hidden Cost | Estimation Method | Example |
|------|------|------|
| Cutover productivity dip | 1-3 months at 20-40% efficiency loss × relevant labor cost | 50 staff × 2 weeks learning × 30% efficiency loss = $[X] |
| Data cleansing & backfill | Estimated person-days × daily rate | 3 people × 10 days = 30 person-days = $[X] |
| Legacy system parallel run | Legacy annual fee × overlap months ÷ 12 | Legacy POS $5K/year × 3 months parallel = $1,250 |
| Future exit / migration | Data export + new system import cost (amortized over 5 years) | Estimated $5-10K ÷ 5 |

### 1.3 TCO Benchmarks by Retail Format

| Format | Annual TCO / Store | % of Revenue | Primary Cost Drivers |
|------|:---:|:---:|------|
| Mom-and-Pop Convenience | $200-500 | 0.1-0.3% | POS subscription + payment processing fees |
| Community Supermarket | $800-2,000 | 0.5-1.0% | POS + inventory management + online storefront |
| Apparel Specialty | $1,500-5,000 | 1.0-2.5% | POS + ERP + CRM + omnichannel |
| Hypermarket | $5,000-20,000 | 2.0-4.0% | Full SaaS suite + IoT + BI |

---

## 2. Benefit Quantification

### 2.1 Five Benefit Categories

| # | Benefit Category | Quantification Method | Confidence |
|---|------|------|:---:|
| 1 | **Labor Savings** | Hours saved × hourly rate × (1 - cutover loss) | High |
| 2 | **Cost Reduction** | Procurement cost reduction % × annual procurement spend | Medium-High |
| 3 | **Shrinkage Reduction** | Shrinkage rate reduction % × annual shrinkage value | Medium |
| 4 | **Inventory Optimization** | Inventory reduction % × cost of capital | Medium-High |
| 5 | **Revenue Growth** | Incremental channel GMV × gross margin % | Medium-Low |

### 2.2 Benefit Quantification Example

| Benefit Source | Calculation Formula | Annual Benefit ($K) |
|------|------|:---:|
| Checkout efficiency gain | Save X hrs/day × 365 days × $[X]/hr | |
| Procurement cost reduction | Annual procurement $[X]K × price reduction [X]% | |
| Shrinkage reduction | Annual shrinkage $[X]K × reduction [X]% | |
| Inventory holding cost reduction | Avg inventory $[X]K × reduction [X]% × cost of capital [X]% | |
| Online incremental revenue | Daily incremental [X] orders × $[X] ATV × 365 days × gross margin % | |

---

## 3. ROI Calculation

### 3.1 Standard Formula

```
3-Year ROI = (3-Year Total Benefits - 3-Year TCO) / 3-Year TCO × 100%
Payback Period (months) = Total TCO / Annualized Benefits × 12
```

### 3.2 ROI Benchmarks

| Investment Type | Industry Median 3-Year ROI | Median Payback |
|------|:---:|:---:|
| POS / Checkout | 250% | 8 months |
| ERP / Inventory Management | 200% | 12 months |
| CRM / CDP | 280% | 8 months |
| WMS | 180% | 14 months |
| Omnichannel OMS | 220% | 10 months |
| AI Customer Service | 350% | 4 months |
| AI Recommendations | 250% | 6 months |

---

## 4. Sensitivity Analysis

### Three Scenarios

| Scenario | Description | Parameter Adjustment |
|------|------|------|
| Pessimistic | Cost overrun + benefits underperform | Costs +20%, Benefits × 70% |
| Base | Current estimates | No adjustment |
| Optimistic | Cost savings + benefits exceed | Costs -10%, Benefits × 120% |

### Analysis Table

| Scenario | TCO ($K) | 3-Year Benefits ($K) | 3-Year ROI | Payback (months) |
|------|:---:|:---:|:---:|:---:|
| Pessimistic | | | | |
| Base | | | | |
| Optimistic | | | | |

---

## 5. Detailed Calculation Template

Use tool: `tools/digital-roi-quick-calculator.md`
