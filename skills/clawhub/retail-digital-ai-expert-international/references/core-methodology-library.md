# Core Methodology Library

> A consolidated reference of core methodologies for retail digitalization and AI consulting. Each methodology includes applicable scenarios, operational steps, and deliverable standards.

---

## 1. R-DMM: Retail Digital Maturity Model

### 1.1 Model Overview
R-DMM (Retail Digital Maturity Model) is a retail-industry-specific digital maturity assessment framework covering five dimensions (Technology, Operations, Data, Organization, Customer) across five maturity levels (L1 Initial -> L5 Leader).

### 1.2 Assessment Steps

```
Step 1: Define Assessment Scope
  -> Single-store assessment / full chain assessment / by region / by format
  -> Clarify assessment boundaries

Step 2: Collect Assessment Data (1-2 weeks)
  -> System inventory (POS/ERP/WMS/CRM, etc.)
  -> Operational data (KPIs, 12-24 months)
  -> Organizational structure (IT team / digital roles)
  -> Customer touchpoints (online / offline / messaging / membership)

Step 3: Five-Dimensional Scoring (1 week)
  -> Score each dimension 1-5 (decimals allowed, e.g., 2.5)
  -> Scoring basis: checklist + industry benchmark comparison + expert judgment

Step 4: Gap Analysis
  -> Current level vs. industry average vs. industry leader
  -> Identify TOP 5 critical gaps

Step 5: Leap Path Design
  -> What is required to reach target maturity
  -> Investment / timeline / risk estimation

Step 6: Report & Presentation
  -> "Findings -> Insights -> Recommendations" narrative logic
  -> Pyramid Principle: conclusions first
```

### 1.3 Five-Dimension Scoring Rubric

#### Technology (Weight: 30%)

| Score | Criteria |
|:---:|------|
| 1 | Standalone POS or fully manual, no network connectivity |
| 2 | Cloud POS + 1-2 SaaS tools (e.g., delivery platform / basic e-commerce), systems operate independently |
| 3 | Core systems SaaS-based, POS-ERP-e-commerce key interfaces integrated |
| 4 | Full-chain SaaS + localized AI applications + data middle platform, complete API layer |
| 5 | AI-native architecture + in-house / deeply customized platform + global unification, real-time intelligence |

#### Operations (Weight: 20%)

| Score | Criteria |
|:---:|------|
| 1 | Experience-driven, verbal management, gut-feel decisions |
| 2 | SOPs in place (paper or digital), basic process standardization |
| 3 | System-recorded data + BI dashboards, departmental KPI management |
| 4 | Data-driven daily decisions, predictive operations (proactive, not reactive) |
| 5 | AI-driven operations, self-adaptive + self-optimizing, zero manual intervention |

#### Data (Weight: 20%)

| Score | Criteria |
|:---:|------|
| 1 | No systems or paper-based bookkeeping only |
| 2 | Basic POS / e-commerce data, Excel-based analysis |
| 3 | Multi-system data + BI multi-dimensional analysis, basic data governance |
| 4 | Real-time data streams + IoT data, data governance framework, data middle platform |
| 5 | Enterprise-wide real-time data lake, enterprise-grade data governance, data as balance-sheet asset |

#### Organization (Weight: 15%)

| Score | Criteria |
|:---:|------|
| 1 | No IT role; the owner is everything |
| 2 | Outsourced or part-time IT; owner has basic digital awareness |
| 3 | Dedicated IT 1-5 people; management has digital consensus |
| 4 | Digital team 5-30 (product + engineering + data); CTO/CDO in place; digitalization is strategic |
| 5 | CDO/CAIO + AI Center of Excellence + data science team; digitalization = core competitive advantage |

#### Customer (Weight: 15%)

| Score | Criteria |
|:---:|------|
| 1 | No digital touchpoints; walk-in-only; no membership |
| 2 | Basic e-commerce / delivery platform presence; basic points-based membership |
| 3 | Own app/mini-program + third-party e-commerce; tiered loyalty + stored value + points; community presence |
| 4 | Omnichannel unified (online + offline + messaging); CDP + OneID + MA; personalized experiences |
| 5 | AI-powered omnichannel adaptive experiences; predictive + real-time personalization; AI-native customer engagement |

### 1.4 Composite Score Calculation

```
Composite Score = Technology x 0.30 + Operations x 0.20 + Data x 0.20 + Organization x 0.15 + Customer x 0.15

Maturity Determination:
  1.0-1.5 -> L1 Initial
  1.6-2.5 -> L2 Developing
  2.6-3.5 -> L3 Integrated
  3.6-4.5 -> L4 Intelligent
  4.6-5.0 -> L5 Leader
```

---

## 2. AI Scenario Prioritization: RICE+ Model

### 2.1 Scoring Framework

| Dimension | Weight | Scoring Criteria (1-5) |
|------|:---:|------|
| **R**each (Coverage) | 25% | 1 = impacts <10% of stores/categories; 3 = 30-60%; 5 = >90% |
| **I**mpact (Business Impact) | 30% | 1 = impacts <1% of revenue/profit; 3 = 3-10%; 5 = >20% |
| **C**onfidence (Technical Feasibility) | 20% | 1 = pure exploration / 0-30%; 3 = proven solutions exist / 60-80%; 5 = validated / 95%+ |
| **E**ffort (Implementation Difficulty, Inverse) | 15% | 1 = extremely difficult (>$750K / >12 months); 3 = moderate ($75K-$300K / 4-8 months); 5 = very easy (<$15K / <2 months) |
| **+AI** (AI Suitability) | 10% | 1 = rule engine / human is better; 3 = AI can enhance; 5 = AI is the optimal solution |

### 2.2 Composite Score Formula

```
RICE+ = R x 0.25 + I x 0.30 + C x 0.20 + E x 0.15 + AI x 0.10

Priority Determination:
  >= 4.0 -> P0: Launch immediately
  3.0-3.9 -> P1: Short-term priority (within 3-6 months)
  2.0-2.9 -> P2: Medium-term roadmap (within 6-12 months)
  < 2.0  -> P3: Watch / not recommended at this time
```

### 2.3 15 AI Scenarios: Typical RICE+ Scores (Mid-to-Large Chain Reference)

| AI Scenario | R | I | C | E | AI | Composite | Priority |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Intelligent Customer Service | 5 | 4 | 5 | 5 | 5 | 4.70 | P0 |
| Personalized Recommendations | 5 | 4 | 5 | 4 | 5 | 4.55 | P0 |
| AI Content Generation (AIGC) | 5 | 3 | 5 | 5 | 5 | 4.40 | P0 |
| Demand Forecasting | 5 | 5 | 4 | 3 | 4 | 4.30 | P0 |
| Intelligent Replenishment | 5 | 5 | 4 | 3 | 4 | 4.30 | P0 |
| Customer Insight & Segmentation | 5 | 4 | 4 | 4 | 4 | 4.25 | P0 |
| Dynamic Pricing | 4 | 4 | 4 | 3 | 4 | 3.85 | P1 |
| Visual Search | 3 | 3 | 4 | 3 | 5 | 3.50 | P1 |
| Intelligent Sales Advisor | 4 | 4 | 4 | 3 | 3 | 3.70 | P1 |
| Assortment & Merchandising | 4 | 5 | 3 | 2 | 4 | 3.75 | P1 |
| Virtual Try-On | 2 | 3 | 4 | 3 | 5 | 3.20 | P2 |
| Inventory Optimization | 4 | 4 | 3 | 2 | 3 | 3.35 | P2 |
| Shelf Optimization | 3 | 3 | 3 | 2 | 4 | 2.95 | P2 |
| Loss Prevention & Risk Control | 3 | 4 | 3 | 2 | 4 | 3.20 | P2 |
| Store Location Intelligence | 2 | 4 | 4 | 3 | 3 | 3.25 | P2 |
| Supply Chain Optimization | 4 | 5 | 3 | 1 | 4 | 3.55 | P1 |

---

## 3. Vendor Selection: 7-Dimension Decision Matrix

### 3.1 Seven-Dimension Assessment Model

| Dimension | Weight | Assessment Method | Data Sources |
|------|:---:|------|------|
| **Format Fit** | 25% | Demo + scenario testing + customer references | POC, client references, peer case studies |
| **TCO (Total Cost of Ownership)** | 20% | 3-5 year full-cost modeling (including hidden costs) | Vendor quotes + client references + industry benchmarks |
| **API & Extensibility** | 15% | API documentation review + developer ecosystem + ISV network | API docs, marketplace, existing integration cases |
| **Omnichannel Capability** | 12% | Inventory / order / membership / pricing unification capability | Demo + scenario testing + client references |
| **Implementation & Training** | 10% | Implementation methodology + training system + go-live commitment | RFP response + client references + site visits |
| **Stability & Support** | 10% | SLA + failure frequency + support responsiveness + customer satisfaction | RFP response + client reference checks + contract terms |
| **Data Sovereignty & Compliance** | 8% | Data storage location / portability / privacy compliance / security certifications | Contract terms + security certifications + architecture review |

### 3.2 Vendor Scorecard Template

| Vendor | Format Fit (25) | TCO (20) | API (15) | Omnichannel (12) | Implementation (10) | Stability (10) | Compliance (8) | Total |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | | | | | | | | |
| B | | | | | | | | |
| C | | | | | | | | |

### 3.3 Full Vendor Evaluation Process

```
Week 1-2: Longlist Screening
  -> Requirements checklist -> Market scan -> Initial screening to 8-10 vendors -> RFI (Request for Information)

Week 3-4: Shortlist Evaluation
  -> RFI response analysis -> 7-dimension scoring -> Narrow to 3-4 vendors -> RFP (Request for Proposal)

Week 5-6: In-Depth Evaluation
  -> Demo -> PoC (Proof of Concept) -> Client reference checks (minimum 2 peer-level clients)
  -> Team evaluation (technical / service / implementation teams)

Week 7-8: Contract & Decision
  -> Contract review (SLA / exit clauses / data migration) -> Price negotiation -> Final decision
```

---

## 4. Retail Digitalization ROI / TCO Calculation Model

### 4.1 TCO (5-Year Total Cost of Ownership)

```
TCO = Software Subscription + Hardware + Implementation & Integration + Training & Change Management
    + Ongoing Operations + Internal Personnel + Upgrades & Expansion + Hidden Costs

Hidden Cost Checklist:
  - Data migration costs (cleansing / import / validation)
  - Business disruption losses during system cutover
  - Productivity dip during employee learning curve
  - Ongoing maintenance of custom developments
  - Contract exit / data migration costs
  - Ongoing maintenance of multi-system integrations
```

### 4.2 Five-Step ROI Calculation

```
Step 1: Quantify Costs
  CT = TCO (total 5-year costs)

Step 2: Quantify Benefits
  B_direct    = Direct benefits (labor savings + procurement savings + shrink reduction)
  B_indirect  = Indirect benefits (efficiency gains + experience improvement + data as asset)
  B_strategic = Strategic benefits (competitive moat + innovation velocity + risk resilience)

Step 3: Calculate ROI
  ROI = (B_total - C_total) / C_total x 100%
  3-year ROI -> medium-term return
  5-year ROI -> long-term return

Step 4: Calculate Payback Period
  Payback = C_total / Annual_Benefit

Step 5: Sensitivity Analysis
  Pessimistic scenario (B -30%, C +20%)
  Base case scenario
  Optimistic scenario (B +20%, C -10%)
```

### 4.3 ROI Benchmark Reference (Industry Average)

| Digital Investment | 3-Year ROI (Median) | Payback (Median) | Success Rate |
|------|:---:|:---:|:---:|
| POS / Checkout | 250% | 8 months | 85% |
| ERP / Inventory Management | 200% | 12 months | 75% |
| CRM / CDP | 280% | 8 months | 65% |
| WMS | 180% | 14 months | 80% |
| OMS Omnichannel | 220% | 10 months | 70% |
| Private Domain / Direct-to-Consumer | 300% | 6 months | 60% |
| AI Customer Service | 350% | 4 months | 85% |
| AI Recommendations | 250% | 6 months | 80% |
| AI Forecasting + Replenishment | 190% | 12 months | 72% |
| RFID Full-Category | 130% | 24 months | 85% |

---

## 5. Retail Private-Domain / DTC Engagement AIPL Model

### 5.1 Model Framework

| Stage | Definition | Key Metrics | Industry Benchmark |
|------|------|------|:---:|
| **A**wareness | Consumer knows your brand/store | Impressions / messaging opt-ins / social follows | -- |
| **I**nterest | Shows interest in your products | App/website UV / browse depth / coupon-claim rate | Claim rate 15-25% |
| **P**urchase (First Purchase) | Completes first purchase | Conversion rate / first-order AOV / membership sign-up rate | Conversion 8-15% |
| **L**oyalty | Repeat purchase + advocacy | Repurchase rate / stored-value rate / referral rate | 30-day repurchase 20-35% |

### 5.2 AIPL Optimization by Touchpoint

| Touchpoint | A -> I | I -> P | P -> L | L -> Advocacy |
|------|------|------|------|------|
| Mobile App / Mini-Program | New-user welcome offer | Flash deals + hero product recs | Stored value + community + member day | Referral coupons |
| Messaging (WhatsApp/WeChat) | In-store QR code opt-in | Dedicated advisor + 1:1 recs | Community check-in + exclusive perks | Group-buy / affiliate |
| Livestream | Short-video traffic driving | Livestream-exclusive pricing + flash | Fan club + repurchase coupons | Share-the-stream rewards |
| Community (Groups) | New-member welcome + icebreaker | Group-exclusive + flash sales | Check-in + points + exclusive events | Invite-a-friend rewards |

---

## 6. Change Management: ADKAR for Retail

### 6.1 Five-Stage Retail Implementation

| ADKAR | Target: Owner / Store Manager | Target: Associate / Advisor | Success Signal |
|------|------|------|------|
| **A**wareness | "The store next door adopted this system, and their average ticket went up 15%" | "With the AI advisor, your monthly commission could go up by $XX" | Proactively asks "When can we get this?" |
| **D**esire | Calculate ROI + competitive pressure + industry trends | Tie benefits to personal gain (commission / efficiency / less drudgery) | Expresses willingness to learn and use |
| **K**nowledge | Manager bootcamp + digital dashboard training | Video tutorials (3 min each) + sandbox practice + mentor pairing | Completes one full operation independently |
| **A**bility | Use data for decisions (dashboard -> analysis -> decision) | Checkout / inventory lookup / member lookup becomes muscle memory | 3 peak-hour transactions with zero errors |
| **R**einforcement | Digital KPIs incorporated into performance reviews + regular retrospectives | Immediate positive feedback + zero-error operation rewards | DAU >85%; not using the system = cannot do the job |

### 6.2 Common Resistance & Countermeasures

| Resistance Source | Typical Expression | Countermeasure |
|------|------|------|
| Owner / CEO | "Too expensive / not sure if it's worth it" | Calculate ROI first; small-scale pilot; let results do the talking |
| Store Manager | "This adds to my workload" | Lead with efficiency gains -> then the system; prove the system reduces burden |
| Store Associate | "I can't use this / can't learn it" | 3-minute video tutorials + mentorship + instant rewards |
| Franchisee | "HQ is coming to micromanage me again" | Enablement > control; start with supply chain (cost savings) -> then systems |
| IT Department | "Another new system to learn..." | Training + certification + career development path |

---

## 7. Retail Franchise Chain: Five-Layer Control Model

### 7.1 Five-Layer Architecture

```
L5 Enablement Layer -> AI operational diagnostics / intelligent recommendations / best-practice push / online training
L4 Data Transparency Layer -> Real-time revenue dashboards / category rankings / anomaly alerts / inventory visibility
L3 Standardization Layer -> Unified POS / unified inventory / unified membership / unified store inspections
L2 Supply Chain Layer -> Unified procurement / unified distribution / cost transparency / quality standards
L1 Brand Foundation Layer -> Brand VI / store design standards / core product / legal compliance
```

### 7.2 Layered Implementation Strategy

| Layer | Mandatory or Voluntary | Implementation Sequence | Critical Success Factor |
|------|:---:|:---:|------|
| L1 Brand Layer | Mandatory | Day 1 of franchise | Contract terms + security deposit + regular inspections |
| L2 Supply Chain Layer | Semi-mandatory (collective procurement = cost savings) | Month 1-3 of franchise | Collective procurement pricing has decisive advantage |
| L3 Standardization Layer | Mandatory | Month 3-6 of franchise | System is simple and easy to use + adequate training |
| L4 Data Transparency Layer | Mandatory (back-end) + Voluntary (front-end) | Month 6-9 of franchise | Data helps franchisees discover problems |
| L5 Enablement Layer | Voluntary (but compelling) | Month 9+ of franchise | AI recommendations truly help franchisees |

### 7.3 Three Principles of Franchisee Digitalization
1. **Enablement > Control**: Make franchisees want to use it voluntarily -- "using the system = earning more."
2. **Supply Chain First**: Help franchisees save on procurement costs first -> natural acceptance of other systems follows.
3. **Incentive Alignment**: System usage is directly tied to franchisee financial interests.

---

## 8. Omnichannel Maturity Model

### 8.1 Five-Level Omnichannel Maturity

| Level | Core Characteristic | Inventory | Orders | Membership | Representative |
|:---:|------|:---:|:---:|:---:|------|
| L1 No Channel | Offline only | Store-only inventory | Store POS only | No membership | Traditional mom-and-pop |
| L2 Multi-Channel | Offline + independent e-commerce | Per-channel siloed | Per-channel siloed | Per-channel siloed | Traditional brands |
| L3 Cross-Channel | Partial integration | Partial sharing | Partial integration | Partial identification | Traditional chains |
| L4 Omnichannel | Unified online + offline | Single pool of inventory | Omnichannel routing | OneID | Sephora / Watsons |
| L5 Unified Commerce | AI-driven omnichannel | Real-time globally optimal | AI intelligent fulfillment | AI personalization | Walmart / Amazon |

### 8.2 Omnichannel Leap Conditions

| Leap | Prerequisites | Biggest Obstacle |
|------|------|------|
| L1 -> L2 | Online channel launched + basic e-commerce capability | Lack of e-commerce operating skills |
| L2 -> L3 | Inventory visibility (accuracy >95%) | Inaccurate inventory |
| L3 -> L4 | OneID resolution + OMS omnichannel routing | Organizational silos (online/offline team rivalry) |
| L4 -> L5 | AI capability + data flywheel | Technology architecture + organizational change |

---

## 9. Category Management Digitalization: Eight Steps

| Step | Traditional | Digital | AI-Powered |
|------|------|------|------|
| 1. Category Definition | Experience-based segmentation | Data + customer decision tree | AI auto-clustering |
| 2. Category Role | Experience-based judgment | KPI data-driven | AI multi-factor classification |
| 3. Category Assessment | Monthly/quarterly manual | Real-time category dashboards | AI anomaly detection + root cause |
| 4. Category Scorecard | Excel | BI auto-generation | AI prediction + recommendations |
| 5. Category Strategy | Annual/quarterly planning | Agile / rolling planning | AI simulation + scenario testing |
| 6. Category Tactics | Manual | Systematic execution | AI recommendations + automation |
| 7. Category Execution | Manual monitoring | Task system + auto-tracking | AI autonomous optimization |
| 8. Category Review | Monthly/quarterly meetings | Real-time + exception-based | AI auto-summary + recommendations |

---

## 10. MECE Five-Dimension Needs Diagnosis

For the open-ended problem of "Our retail business is not performing well / not profitable / we want to go digital," decompose using MECE:

```
Problem: Store is not profitable ->
  Dimension 1: Insufficient foot traffic?
    +-- Location issue
    +-- Brand awareness
    +-- Competitive diversion

  Dimension 2: Low conversion rate?
    +-- Wrong product assortment / pricing
    +-- Poor merchandising / experience
    +-- Weak sales advisors
    +-- Stock-outs / inaccurate inventory

  Dimension 3: Low average transaction value?
    +-- Product price band is too low
    +-- Insufficient cross-selling / add-on selling
    +-- Weak membership program
    +-- Unbalanced category structure

  Dimension 4: Low gross margin?
    +-- High procurement costs
    +-- Overly conservative pricing strategy
    +-- High shrink / waste
    +-- Excessive discounting

  Dimension 5: Costs too high?
    +-- Labor costs (poor scheduling / low productivity)
    +-- Rent (unfavorable lease terms)
    +-- Shrink (lax management)
    +-- Energy (no IoT management)
    +-- Systems / IT costs
```

---

> **Usage Notes**: Each methodology can be used independently or in combination. For any given client engagement, select the 2-3 most applicable methodologies. There is no need to deploy every methodology in every project.

> **Cross-References**: See `references/retail-ai-application-framework.md` for AI scenario technical details, `references/global-retail-best-practices-deep-dive.md` for enterprise case studies demonstrating these methodologies in practice, and `references/benchmark-data-and-industry-metrics.md` for industry KPI benchmarks.
