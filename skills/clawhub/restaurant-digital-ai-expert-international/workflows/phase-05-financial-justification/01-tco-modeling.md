# 01-TCO Modeling

## Triggers
- After preliminary technology selection, need to build a complete cost model

---

## TCO Model Overview

TCO != software costs. Restaurant digital TCO contains 7 major cost categories:

```
TCO = Software Costs + Hardware Costs + Implementation Costs + Operations Costs + Personnel Costs + Training Costs + Opportunity Costs
```

---

## Step 1: Software Costs

### SaaS Subscription Fees

| Pricing Model | Applicable Scenarios | Benchmark Unit Pricing (Global Market) |
|--------------|---------------------|---------------------------------------|
| Per location / month | POS, KDS, Inventory | $70-$400/location/month |
| Per user / month | CRM, BI, Scheduling | $15-$80/user/month |
| Per order volume | Delivery aggregator, marketing tools | $0.02-$0.15/order |
| % of transaction volume | QR ordering (some vendors) | 0.3-1% of transaction volume |
| Per API call / usage | AI capabilities, SMS/push notifications | AI: $0.001-$0.01/1K calls |

### One-Time Fees

| Fee Type | Estimated Range |
|----------|----------------|
| System deployment / initialization | $1,500-$15,000 |
| Custom integration development | $5,000-$30,000/integration |
| Data migration | $3,000-$15,000 (depending on volume and complexity) |
| Branding customization (UI/Logo/Domain) | $1,500-$10,000 |

---

## Step 2: Hardware Costs

### Per-Location Hardware Configuration

| Equipment | Quantity | Unit Price (USD) | Replacement Cycle | Annual Depreciation |
|-----------|:---:|------|:---:|------|
| POS Terminal (dual screen) | 1-2 units | $800-$2,500 | 5 years | $160-$500 |
| Receipt Printer | 1-2 units | $150-$400 | 3 years | $50-$133 |
| KDS Kitchen Display | 1-3 units | $300-$900 | 5 years | $60-$180 |
| Kitchen Printer | 1-2 units | $200-$600 | 3 years | $67-$200 |
| Router (Enterprise-grade) | 1 unit | $150-$600 | 5 years | $30-$120 |
| UPS (Backup Power) | 1 unit | $100-$300 | 3 years | $33-$100 |
| Tablet (Server / Manager) | 1-3 units | $400-$900 | 3 years | $133-$300 |
| **Per-Location Hardware Total** | | **$2,100-$7,200** | | **~$600-$1,500/year** |

### Hardware Strategy by Scale

| Number of Locations | Strategy | Per-Location Hardware Investment |
|:---:|----------|:---:|
| 1-10 | Purchase + self-maintain | $1,500-$3,000 |
| 10-100 | Bulk purchase + negotiate discount | $1,000-$2,500/location |
| 100-1,000 | Standardized procurement + spare units | $600-$1,800/location |
| 1,000+ | Framework agreement + equipment leasing | $500-$1,200/location (lease) |

---

## Step 3: Implementation Costs

### Implementation Fee Composition

| Fee Item | Estimate | Notes |
|----------|----------|-------|
| Project Management | 5-10% of contract value | Vendor PM + Client PM |
| System Deployment | 5-15% of contract value | Including environment setup, configuration |
| Data Migration | $3,000-$15,000 | Including cleaning, import, verification |
| Custom Development | $5,000-$30,000/integration | Count integrations first |
| Pilot Operations | $15,000-$50,000 (chains) | Including on-site support |
| Rollout Implementation | $300-$1,500/location | x number of locations |

---

## Step 4: Operations Costs (Annual)

| Fee Item | Estimate |
|----------|----------|
| System maintenance (vendor-provided services) | 10-18% of contract value/year |
| Infrastructure (cloud servers / network / security) | $150-$600/location/month |
| System upgrades | Usually included in maintenance; major versions separate |
| Technical support | Usually included in maintenance |

### Cloud Service Cost Estimates

| Scale | Monthly Cost | Notes |
|:---:|------|-------|
| 1-10 locations | $0 (fully SaaS, no self-managed servers) | Cloud costs included in SaaS fees |
| 10-100 locations | $600-$3,000/month | 2-4 VMs + managed DB + object storage |
| 100-1,000 locations | $6,000-$30,000/month | K8s cluster + middleware + DR |
| 1,000+ locations | $30,000-$300,000/month | Hybrid cloud + multi-region + dedicated links |

---

## Step 5: Personnel Costs

### Client-Side IT Team Personnel Costs (fully loaded: salary + benefits + office + management)

| Role | Annual Salary Range (USD, Global Market) | Scale When Needed |
|------|------|:---:|
| IT Manager / CIO | $80,000-$250,000 | 50+ locations |
| System Administrator | $50,000-$90,000 | 10+ locations |
| Data Analyst | $65,000-$130,000 | 30+ locations |
| Product Manager (Digital) | $85,000-$160,000 | 100+ locations |
| Backend Developer | $80,000-$160,000 | When in-house development needed |
| Frontend / Mobile Developer | $70,000-$130,000 | When in-house app needed |
| AI / ML Engineer | $120,000-$250,000 | When AI projects initiate |

---

## Step 6: Training Costs

| Training Phase | Audience | Delivery Method | Cost |
|---------------|----------|-----------------|------|
| System Go-Live Training | All frontline users | On-site + manual + assessment | $300-$1,000/location |
| Administrator Training | IT / Ops administrators | On-site + certification | $1,000-$3,000/person |
| Annual Refresher Training | New hires + role changers | Video + online assessment | $50-$150/person |
| Change Management Training | All staff | Workshop + communication | $1,500-$6,000/cycle |

---

## Step 7: Hidden Costs (Most Easily Overlooked!)

| Hidden Cost | Description | How to Estimate |
|-------------|-------------|-----------------|
| **Learning Curve Loss** | Operational efficiency drops during new system onboarding | 20-30% efficiency drop for 1-2 months x labor cost |
| **Data Quality Cost** | Inaccurate data leading to poor decisions | 2-5% of returns/waste attributable to data errors |
| **Integration Cost** | Ongoing development to keep systems connected | Integration dev + maintenance = 3-10% of contract value/year |
| **Switching Cost** | Migrating from one system to another | Old system fees during overlap + data migration = 10-20% of contract value |
| **Redundancy Cost** | Dual system fees during transition period | 2-3 months overlap x old system monthly fees |
| **Organizational Friction Cost** | Employee resistance, low engagement internal costs | Estimated 20-30% extension of implementation timeline x time cost |

> **Core Formula**: Hidden Costs ~ 30-40% of visible costs
> Never budget using "visible costs" alone -- you must add hidden costs.

---

## 3-Year / 5-Year TCO Summary Template

Use `templates/roi-and-business-case-template.md` for the TCO template.

### TCO Summary Example (100-Location Quick Service Chain, 3-Year)

| Cost Category | Year 1 ($K) | Year 2 ($K) | Year 3 ($K) | 3-Year Total | % of Total |
|---------------|:---:|:---:|:---:|:---:|:---:|
| Software Subscriptions | 540 | 570 | 600 | 1,710 | 38% |
| Hardware Purchases | 360 | 45 | 60 | 465 | 10% |
| Implementation / Migration | 240 | 30 | 15 | 285 | 6% |
| Operations / Cloud | 120 | 135 | 150 | 405 | 9% |
| Personnel (IT Team) | 240 | 270 | 300 | 810 | 18% |
| Training | 45 | 30 | 30 | 105 | 2% |
| Hidden Costs | 150 | 105 | 90 | 345 | 8% |
| **Annual Total** | **1,695** | **1,185** | **1,245** | **4,125** | 100% |
| Contingency (15%) | 255 | 180 | 187 | 622 | -- |
| **Including Contingency** | **1,950** | **1,365** | **1,432** | **4,747** | -- |

---

## Budget Rules of Thumb

| Scale | Digital Budget as % of Annual Revenue | Reference Range |
|:---:|:---:|------|
| Startup / Early-Stage | 1.5-3% | For foundational systems (approx. 1-2 employee annual salaries) |
| Independent Full-Service | 1-2% | Primarily SaaS subscriptions + hardware |
| Regional Chain (10-100 locs) | 2-4% | Systems + data + lightweight IT team |
| National Chain (100-1,000 locs) | 3-6% | Platform + in-house dev + AI + IT team |
| Global (1,000+ locs) | 4-8% | In-house PaaS + AI + data + global IT org |

---

## Deliverables
- 3-5 year TCO model (all 7 cost categories covered)
- Cost analysis by year / by location / by module
- Hidden cost assessment report

## Quality Checks
- [ ] Hidden costs are included (not just mentioned verbally)
- [ ] TCO covers at least 3 years
- [ ] Hardware depreciated by replacement cycle (not expensed all at once)
- [ ] Contingency of 15%+ is included (scope changes + unexpected costs)
- [ ] Per-location costs and HQ costs are presented separately
