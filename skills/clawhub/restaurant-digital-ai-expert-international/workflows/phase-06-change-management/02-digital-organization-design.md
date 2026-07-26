# 02-Digital Organization Design

## Triggers
- Digital strategy is confirmed; need to design the supporting digital organization and talent system

---

## The Core Question

> "Who is responsible for digital? Who is responsible for data? Who is responsible for keeping the systems running?"

The majority of restaurant digital failures are not because the system was bad -- they are because "nobody was truly responsible."

---

## Step 1: Digital Organization Evolution Path

### Digital Organization by Enterprise Scale

| Stage | # of Locations | Digital Lead | Team Composition | Monthly Cost (USD K) |
|-------|:---:|-------------|-----------------|:---:|
| Nascent | 1-5 | The owner themself | No dedicated headcount. Vendor support only. | $0 |
| Initiating | 5-20 | Operations Manager (dual-hat) | 0-1 IT specialist | $0-$8 |
| Building | 20-100 | Dedicated IT Manager | 2-4 people (IT + Data + Ops support) | $15-$45 |
| Developing | 100-500 | CIO / VP of Digital | 8-15 people (Product R&D + Data + Ops + PMO) | $60-$180 |
| Maturing | 500-2,000 | CIO / CTO | 30-80 people (full IT organization) | $180-$700 |
| Leading | 2,000+ | Group CTO / CDO | 100-300+ people + AI Center of Excellence | $700-$3,500+ |

---

## Step 2: Digital Organization Structure Design

### Two Fundamental Architecture Models

**Model A: IT Embedded in Business (Recommended for 10-200 Locations)**

```
          CEO
           |
    +------+------+
    |             |
  VP Ops       IT Manager (5-10 people)
    |             |
    +- Store Ops  +- Infrastructure (2 ppl)
    +- Marketing  +- Application Systems (2 ppl)
    +- Supply Chain +- Data Analysis (1 ppl)
                   +- Ops Support (2 ppl)

Pros: IT directly serves the business. Low communication overhead.
Cons: IT only does "demand response." Lacks forward-looking capability.
```

**Model B: Independent Digital Center (Recommended for 200+ Locations)**

```
              CEO
               |
    +------+---+---+------+
    |      |       |      |
  VP Ops  CIO     CFO    CMO
          |
   +------+------+
   |             |
Digital Steering Committee
   |
   +- Product & Architecture (5-10 ppl)
   +- Data & AI (8-15 ppl)
   +- Infrastructure & Ops (5-10 ppl)
   +- PMO & Implementation (3-5 ppl)
   +- Information Security (2-3 ppl)
   +- Business Partners (1 per business line)

Pros: Independent decision-making, specialized division of labor, forward-looking planning.
Cons: May become disconnected from the business. (Mitigate with Business Partner roles.)
```

---

## Step 3: Key Role Definitions

### Restaurant-Specific Critical Digital Roles

#### 1. Digital Business Partner (Digital BP)

The most easily overlooked yet most important role.

| Dimension | Description |
|-----------|-------------|
| Responsibility | Does NOT write code. Goes deep into frontline operations (locations + supply chain). Translates business "pain" into IT "requirements." |
| Reports to | Dual reporting: solid line -> CIO, dotted line -> Business VP |
| Requirements | Understands business > understands tech. Someone who has managed restaurant operations is 10x better than a pure IT background. |
| Staffing | 1 person per 1-2 business lines |
| Typical Task | "Regional Manager says delivery orders are overwhelming. I spent 3 days in the location and found the printer jams during peak hours -> it's a hardware problem, not a software problem." |

#### 2. Restaurant Data Analyst

| Dimension | Description |
|-----------|-------------|
| Responsibility | From POS / CRM / delivery / inventory data, find "which menu item should be discontinued" and "which location has anomalies." |
| Requirements | SQL + Excel + BI tools + restaurant business sense |
| Typical Output | "Cross-referenced Top 10 by revenue vs. Top 10 by profit margin over the last 30 days -> found 3 high-volume, low-margin items -> recommended price increase or portion adjustment." |

#### 3. Chain System Implementation Manager

| Dimension | Description |
|-----------|-------------|
| Responsibility | Responsible for rolling out new systems across locations -- not "technical deployment," but "teaching store managers to use the system well." |
| Requirements | Has managed location operations + can use the system + has patience |
| Typical Task | "This week I'm going to 5 locations in the Southwest region for system launch training. Bringing back 3 issues to optimize." |

---

## Step 4: Incentive Mechanism Design

### Incorporate Digital into KPIs

| Role | Digital-Related KPIs | Weight |
|------|---------------------|:---:|
| Store Manager | "System operation accuracy rate," "Daily data entry completeness" | 5-10% |
| Regional Manager | "Regional system activeness," "Data quality score" | 10-15% |
| VP of Operations | "Digital coverage rate," "System usage rate," "Labor efficiency improvement" | 15-20% |
| CIO / Digital Lead | "Digital project ROI," "System availability rate," "Location digital satisfaction" | Core KPI |

### Incentive Methods

| Method | Target | Approach |
|--------|--------|----------|
| Positive bonus | All staff | "Digital Flagship Location" monthly award: $100-$500 |
| Skill-based pay | Store Managers / Head Chefs | Pass system operation assessment -> base pay +$50/month |
| Promotion linkage | Regional Managers | Regional managers with outstanding system rollout results get priority promotion |
| Recognition | All staff | "Digital Pioneer" award -- company-wide announcement |
| Negative constraint | Repeat non-compliers | 3 consecutive months of substandard data quality -> affects performance rating |

> Core principle: **Reward before you punish.** Use only positive incentives in Year 1. Introduce negative constraints only after the majority has accepted the system.

---

## Step 5: AI Organization Development

### AI Organization Maturity Ladder

| Stage | AI Org Form | Applicable Scale | Description |
|-------|------------|:---:|-------------|
| Awareness | No organization. Personal interest-driven. | 1-50 locations | Owner reads AI news on their own. |
| Exploration | 1-2 "AI Champions" (part-time) | 10-100 locations | Operations / IT staff with AI enthusiasm experiment part-time. |
| Application | 3-5 person AI team (dedicated) | 50-500 locations | Data engineer + ML engineer + business analyst, one each. |
| Platform | 10-20 person AI team (standalone dept) | 200-2,000 locations | AI lead + algorithms + data + engineering + product. |
| AI-Native | AI Center of Excellence + Business Line AI Ambassadors | 500-10,000+ locations | Centralized platform + distributed application. |

### AI Champion Profile

Who to select as an AI Champion?

- Has curiosity about new technology (already uses ChatGPT / Claude / Gemini on their own)
- Understands the business (knows where location pain points are)
- Has 2+ years with the company (understands company culture)
- Does NOT need a technical background
- Does NOT need to be the most educated person

---

## Step 6: Digital Talent Development

### Development Pathway

| Stage | Development Content | Method | Duration |
|-------|-------------------|--------|:---:|
| Novice | Restaurant business fundamentals + system operations | Rotational (1 month in a location) | 1-3 months |
| Competent | Requirements analysis + data modeling + system selection | Shadow projects + certification | 6-12 months |
| Core | Architecture design + project management + vendor management | Lead projects independently | 1-3 years |
| Expert | Digital strategy + organizational change + AI applications | Cross-industry learning + peer exchanges | 3-5 years |

### Talent Sources

| Source | Strengths | Weaknesses | Best For |
|--------|----------|-----------|----------|
| Promote from operations / locations | Understands the business best | Needs to supplement technical skills | Requirements analysis, project implementation |
| Hire from tech companies | Strong technical skills | Doesn't understand "restaurant culture" | Development, architecture |
| Recruit from competitors | Best fit | Expensive; prior experience may not transfer | Rapid build-out |
| Hire from consulting firms | Strong methodology | Lacks frontline feel | Strategy, PMO |

---

## Deliverables
- Digital organization structure chart (with reporting lines)
- Key role JDs (Digital BP, Data Analyst, Implementation Manager, etc.)
- Digital KPI and incentive mechanism plan
- AI organization development roadmap

## Quality Checks
- [ ] Digital is not one person's job -- there is a clear responsibility matrix
- [ ] Key roles have JDs, not just titles
- [ ] KPIs are tied to digital objectives (otherwise nobody will take it seriously)
- [ ] Incentive approach is "positive-first"
- [ ] AI organization evolution by scale has been considered
