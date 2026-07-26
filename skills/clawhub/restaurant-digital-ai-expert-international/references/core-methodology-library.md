# Core Methodology Library (Restaurant Contextualized)

## 1. Problem Diagnosis & Structured Thinking

### 1.1 MECE Applied to Restaurants

**MECE Breakdown of "Our Restaurant Is Underperforming":**

```
Revenue = Traffic x Average Ticket x Repeat Rate

Traffic Decline:
  +-- External Factors (uncontrollable)
  |   +-- Overall trade area foot traffic declining
  |   +-- New competitor openings / competitor promotions
  |   +-- Seasonal fluctuation
  +-- Internal Factors (controllable)
      +-- Signage / storefront not eye-catching enough
      +-- Poor online reviews / low ratings
      +-- Delivery platform ranking decline
      +-- Marketing spend insufficient

Average Ticket Too Low:
  +-- Menu structure irrational (lacking high-margin items)
  +-- Order recommendations not optimized
  +-- Combo meal design weak
  +-- Beverage / alcohol attach rate low

Low Repeat Rate:
  +-- Inconsistent food quality
  +-- Poor service experience
  +-- No loyalty / stored-value lock-in
  +-- Strong competitor substitution
```

### 1.2 SPIN Selling Framework (Restaurant Edition)

| SPIN Dimension | Restaurant Scenario Example Questions |
|------|------|
| **S**ituation | "What POS are you using now? Which delivery platforms are you on? Can you see daily revenue in real time?" |
| **P**roblem | "How long do guests wait during peak hours? How many order delays? How much food waste? How long does reconciliation take?" |
| **I**mplication | "If order times slow by 5 more minutes, how many guests will you lose? If a food safety incident occurs, can the store stay open?" |
| **N**eed-Payoff | "If throughput improves 30%, reconciliation goes from 2 hours to 5 minutes, and food waste drops 20% -- how much would that save annually?" |

### 1.3 5-Whys Root Cause Analysis (Restaurant Edition)

Example: "Food cost ratio too high (42% vs. industry average 30%)"

```
Why 1: Why is the food cost ratio high?
  -> Purchase prices are high + significant waste

Why 2: Why are purchase prices high?
  -> All spot purchases per store, no collective bargaining power

Why 3: Why is waste significant?
  -> Prep based on experience/guesswork, often over-prep; no system to track shrinkage

Why 4: Why is prep based on guesswork?
  -> No historical data to reference, no forecasting tools

Why 5: Why is there no data?
  -> No inventory management system; everything recorded manually

-> Root Cause: No inventory system + spot purchasing = food cost is uncontrolled
-> Countermeasure: Deploy inventory management system + join a group purchasing platform
```

---

## 2. Strategic Planning Frameworks

### 2.1 Run / Grow / Transform in Restaurant IT Investment Portfolio

| Category | Allocation | Restaurant Examples |
|------|:---:|------|
| **Run (Operations)** | 50-60% | Keep POS running, network stability, data backup, security |
| **Grow (Growth)** | 25-35% | Loyalty system upgrade, direct channel ops, delivery ops optimization, new channel expansion |
| **Transform (Innovation)** | 10-15% | AI ordering, intelligent scheduling, automated BOH, supply chain AI |

### 2.2 SoR / SoD / SoI System Classification

| Category | Restaurant Systems | Investment Logic |
|------|------|------|
| **SoR (Systems of Record)** | POS, accounting system, inventory | Stability > Innovation; choose mature vendors |
| **SoD (Systems of Differentiation)** | Loyalty CRM, direct channel, customized ordering | Moderate innovation; build competitive differentiation |
| **SoI (Systems of Innovation)** | AI forecasting, voice ordering, CV quality inspection | Rapid validation; allow for failure |

### 2.3 BCG Matrix (Restaurant Business Portfolio)

| Quadrant | Restaurant Examples | Digital Strategy |
|------|------|------|
| **Stars**: High growth, high share | App ordering, direct channel community | Continue investing, build moat |
| **Cash Cows**: Low growth, high share | Core POS, mature delivery operations | Maintain, avoid major overhauls |
| **Question Marks**: High growth, low share | AI voice ordering, autonomous kitchen | Selective investment, rapid validation |
| **Dogs**: Low growth, low share | Paper coupons, table-side call bells | Deprecate and retire |

---

## 3. Change Management Frameworks

### 3.1 ADKAR (Restaurant Edition)

For details, see Section 7 of the main SKILL.md.

### 3.2 Kotter's 8-Step Change Model (Restaurant Deployment Edition)

| Step | Restaurant-Specific Execution |
|------|------|
| 1. Urgency | "The place next door deployed this system and now their labor efficiency is 30% higher than yours" |
| 2. Coalition | Owner + most capable store manager + most influential head chef |
| 3. Vision | "In 3 months, you'll work 2 fewer hours per day and see all data on your phone" |
| 4. Communication | Mention at every meeting, post in team chat, brief at every morning huddle |
| 5. Empowerment | Give store managers operational flexibility, grant a 1-week "safe to make mistakes" grace period with the new system |
| 6. Quick Wins | Show "Today's revenue is +8% vs. same day last week" within the first week |
| 7. Consolidation | Month 1 success -> replicate at store #2 -> Month 3 all stores |
| 8. Institutionalize | Digital usage rate included in store manager KPIs, monthly digital ops review meeting |

### 3.3 Change Readiness Assessment (5 Dimensions)

| Dimension | Level 1 (Not Ready) | Level 5 (Fully Ready) |
|------|------|------|
| **Leadership Commitment** | Owner verbally says "support" but is never involved | Owner personally learns the system, reviews data weekly, includes in KPIs |
| **Sense of Urgency** | "Things are fine as they are" | Clear recognition that not changing means falling behind or being eliminated |
| **Trust Foundation** | Staff fear system will replace them, fear transparency will hurt bonuses | Open communication: "The system helps you, not replaces you" |
| **Capability Readiness** | Average team age 50+, can barely use a smartphone | Young staff willing to lead learning, training system in place |
| **Cultural Fit** | "We've done it this way for 10+ years" | "Let's try it, we can always adjust" |

---

## 4. Financial Analysis Frameworks

### 4.1 Restaurant TCO (Total Cost of Ownership) Estimation Checklist

| Cost Item | One-Time | Annual | Notes |
|------|:---:|:---:|------|
| POS software subscription | -- | Yes | SaaS annual fee |
| POS hardware | Yes | -- | Terminals / tablets / KDS screens / printers |
| Network equipment | Yes | Yes | Enterprise router + annual broadband |
| Implementation / deployment | Yes | -- | System installation + configuration + integrations |
| Training | Yes | Yes | Initial training + ongoing training |
| Data migration | Yes | -- | Historical data cleansing + migration |
| System integrations | Yes | Yes | API development + maintenance |
| Support & maintenance | -- | Yes | Technical support + SLA |
| Upgrades | -- | Yes | Major version upgrade fees |

### 4.2 Restaurant Digitalization ROI Calculation Template

```
Investment Side:
  5-Year TCO = SaaS fees (5yr) + Hardware + Implementation + Training + Support (5yr)
             = $XXX,XXX

Return Side (Annual):
  Labor savings: X FTEs x $XX,XXX/year = $XX,XXX/year
  Food waste reduction: Annual food purchases x XX% = $XX,XXX/year
  Revenue growth: Annual revenue x XX% = $XX,XXX/year
  Commission savings: Delivery volume x 22% x direct channel conversion rate = $XX,XXX/year
  Risk reduction: $XX,XXX (food safety / compliance / reconciliation gaps, etc.)
  Total Annual Return = $XX,XXX

ROI Calculation:
  5-Year Total Return = Annual Return x 5 = $XXX,XXX
  5-Year ROI = (5yr Total Return - 5yr TCO) / 5yr TCO x 100% = XXX%
  Payback Period = TCO / Annual Return = XX months
```

### 4.3 Sensitivity Analysis

| Scenario | Assumption Change | ROI Change | Assessment |
|------|------|------|------|
| Base Case | -- | 250% | Strongly recommended |
| Conservative | Returns at 60% of expected | 90% | Still worth doing |
| Pessimistic | Returns at 30% of expected + costs 20% over | 10% | Not worth doing |

> **Decision Rule**: Only proceed if conservative-case ROI > 50%.

---

## 5. Data Architecture Framework

### 5.1 Restaurant Data Domain Partitioning

```
Business Data Domain       Operations Data Domain      Customer Data Domain
+-- Orders / Transactions  +-- Scheduling / Labor      +-- Member basic info
+-- Dishes / Menu           +-- Food Safety / Inspect   +-- Purchase behavior
+-- Inventory / Purchasing  +-- Energy / Equipment      +-- Tags / Profiles
+-- Finance / Reconciliation+-- Throughput / Quality    +-- Marketing / Reach
+-- Supply Chain            +-- Store / Performance     +-- Feedback / Reviews
```

### 5.2 Restaurant Data Governance Checklist

| Master Data Type | Standard Requirements | Owner |
|------|------|------|
| Menu Item Master | Unified code, name, category, spec, cost card | Menu Manager |
| Store Master | GLN code, address, type, sq. footage, seating | Operations |
| Supplier Master | Unified ID, qualifications, rating, collaboration history | Procurement |
| Employee Master | Employee ID, skills, hours, compensation | HR |
| Member Master | OneID, tier, points, stored value, tags | CRM |

---

> **Cross-References**: This library complements the frameworks in the main SKILL.md (ADKAR, digital maturity model, ROI frameworks) and the AI Application Framework in `restaurant-ai-application-framework.md`. For vendor-specific methodology applications (e.g., Toast-specific deployment playbook, Square migration methodology), see `restaurant-tech-vendor-landscape.md`.
