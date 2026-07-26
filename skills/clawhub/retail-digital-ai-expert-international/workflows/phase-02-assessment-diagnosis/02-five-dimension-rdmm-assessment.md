# 02 — Five-Dimension R-DMM Assessment

> **Trigger**: Research data collection is complete
> **Prerequisites**: Interview notes + system inventory + operational data + store visit records
> **Deliverables**: R-DMM five-dimension assessment results + industry benchmarking + gap analysis

---

## 1. R-DMM Assessment Seven-Step Method

```
Step 1: Define Assessment Scope → Step 2: Collect Assessment Data → Step 3: Five-Dimension Scoring →
Step 4: Industry Benchmarking → Step 5: Gap Analysis → Step 6: Maturity Leap Pathways → Step 7: Report
```

### Step 1: Define Assessment Scope

| Scope Option | Description |
|------|------|
| Enterprise-wide | Suitable for SMBs (<100 stores) |
| By region | If significant regional variation exists |
| By format | If the company operates multiple formats (e.g., company-owned + franchise) |
| Sample assessment | Large enterprises (select representative stores + HQ) |

### Step 2: Collect Assessment Data (1-2 weeks)

Use the standard tool: `tools/retail-digital-maturity-assessment-tool.md`

### Step 3: Five-Dimension Scoring (1 week)

**Score each of the five dimensions independently (1-5 scale, 0.5 increments allowed):**

| Dimension | Weight | Assessment Focus |
|------|:---:|------|
| Technology | 30% | POS → ERP → WMS → eCommerce → Data Platform → Integration Level |
| Operations | 20% | Assortment → Inventory → Pricing → Store Management → Decision Approach |
| Data | 20% | Collection → Quality → Governance → Analytics → Assetization |
| Organization | 15% | Team → Awareness → Training → Innovation Culture |
| Customer | 15% | Online → Membership → Private Channels → Personalization → Member Data |

### Step 4: Industry Benchmarking

Use benchmark data from `references/benchmark-data-and-industry-metrics.md` for the relevant retail format.

| Dimension | Client Score | Industry Average | Industry Leader | Gap |
|------|:---:|:---:|:---:|:---:|
| Technology | | | | |
| Operations | | | | |
| Data | | | | |
| Organization | | | | |
| Customer | | | | |

### Step 5: Gap Analysis (Findings → Insights → Advice)

Structure every key finding using the FIA framework:

```
Finding: Inventory accuracy is only 82%, well below the 95% industry benchmark
Insight: Root cause is not the absence of a system — it's the lack of daily cycle counting and handheld scanners
Advice: ① Establish ABC daily cycle count process ② Procure handheld scanners ($200/unit) ③ Target 95% accuracy within 3 months
```

### Step 6: Maturity Leap Pathway Design

```
Current: L2.4 → Target: L3.0
Transition Period: 12-18 months
Conditions for Leap:
  ✓ Master data standards unified
  ✓ Core system APIs integrated
  ✓ Inventory accuracy >95%
  ✓ At least 1 full-time digital role
```

### Step 7: Report Writing

Template: `templates/digital-maturity-assessment-report-template.md`

---

## 2. Scoring Practical Tips

### How to Score "Technology"

| Ask Yourself | Judgment |
|------|------|
| "If all systems suddenly went down, could the business still operate?" | Yes → L1; Yes but with major efficiency loss → L2-L3; No → L4+ |
| "Are systems connected or siloed?" | Each operates independently → L2; Some integration → L3; Fully integrated → L4 |
| "Is data real-time or T+1?" | T+1 → L3; Real-time → L4+ |

### How to Score "Operations"

| Ask Yourself | Judgment |
|------|------|
| "Is assortment / replenishment decisions driven by people or data?" | Purely experience-based → L1; Data-assisted → L3; AI-driven → L5 |
| "Are store KPIs posted on a wall or on a real-time dashboard?" | Paper on wall → L2; BI dashboard → L3; AI-powered alerts → L4+ |

### How to Score "Organization"

| Ask Yourself | Judgment |
|------|------|
| "Whose job is digitalization?" | No one → L1; Outsourced → L2; Dedicated hire → L3+ |
| "How often does the CEO review the digital dashboard?" | Never → L1; Monthly → L2; Weekly → L3; Daily → L4; Real-time → L5 |

---

## 3. Maturity Benchmarks by Retail Format

| Format | Technology | Operations | Data | Organization | Customer | Overall |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| Mom-and-Pop Convenience | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.00 |
| Community Supermarket / Grocery | 1.5 | 1.5 | 1.0 | 1.0 | 2.0 | 1.40 |
| Apparel / Beauty Specialty | 2.5 | 2.5 | 2.0 | 2.0 | 3.0 | 2.40 |
| Fast Fashion / Lifestyle | 3.5 | 3.0 | 3.0 | 3.0 | 3.5 | 3.20 |
| Hypermarket / Supermarket Chain | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 | 3.00 |
| Department Store / Shopping Mall | 3.0 | 2.5 | 2.5 | 2.5 | 3.5 | 2.80 |
| Consumer Electronics / Appliances | 3.0 | 3.0 | 2.5 | 2.5 | 3.5 | 2.90 |
| Home Improvement / Furniture | 2.5 | 2.5 | 2.0 | 2.0 | 3.0 | 2.40 |
| DTC Brand | 3.5 | 3.5 | 3.5 | 3.0 | 4.0 | 3.50 |
| Franchise Chain | 3.0 | 2.5 | 2.5 | 3.0 | 2.5 | 2.70 |
| Global 10K+ Stores | 4.5 | 4.5 | 4.5 | 5.0 | 4.5 | 4.60 |

---

## 4. Common Misconceptions

| Misconception | Correct Approach |
|------|------|
| Using the same scoring criteria across all formats | Use different benchmarks per format (a convenience store L3 is not the same as a global chain L3) |
| Only looking at systems, not utilization | Having a system but nobody uses it = L1 (idle system = no system) |
| Owner says it's good, so it's good | Frontline staff opinions carry equal or greater weight than the owner's |
| Inflated scores (uncomfortable giving honest ratings in front of the client) | Honesty = professionalism. Industry benchmarks let the client see the gap themselves |
