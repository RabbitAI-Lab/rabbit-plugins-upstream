# 01-Technology Selection Process

## Triggers
- Strategic objectives and target architecture have been confirmed; need to select specific systems / tech stack / vendors

## Technology Selection Overall Process

```
Requirements Matrix -> Build vs. Buy Decision -> Vendor Long List -> RFP -> Short List -> PoC/Pilot -> Final Decision
```

---

## Step 1: Requirements Matrix Development

### Mandatory Action: Use "Capability Matrix" Instead of "Feature List"

Unprofessional approach: "We need a system that can manage loyalty members"
Professional approach: "We need loyalty management capability, specifically including: member tier management, points engine, coupon engine, RFM analysis, targeted push notifications, member tag profiles, visit frequency analysis, dormancy reactivation automation"

### Restaurant System Requirements Classification

Categorize requirements into four types:

| Type | Definition | Example | Strategy |
|------|-----------|--------|----------|
| Core Must-Have | Business cannot operate without this | POS payment, QR ordering, delivery order acceptance | Choose the most mature product; no experimentation |
| Differentiator | Needed to create competitive advantage | Refined loyalty operations, supply chain forecasting | Choose customizable products, or build in-house |
| Nice-to-Have | Good to have, fine without | AI recommendations, AR menus | Use SaaS built-in features first, optimize later |
| False Requirements | Owner wants it but doesn't actually need it | "I want an app" (a mini-program / PWA would suffice) | Guide client to abandon |

### Restaurant System Standard Capability Framework (12 Modules)

| Module | Core Capability Requirements | Mandatory / Optional |
|--------|----------------------------|:---:|
| POS Payment | Ordering / payment / checkout / refunds / shift handover | Mandatory |
| KDS Kitchen | Order screen routing / production management / order follow-up / 86'd items | Mandatory |
| CRM / Loyalty | Member profiles / tiers / points / coupons / tags / engagement | Mandatory |
| Delivery Aggregator | Uber Eats / DoorDash / Deliveroo[being consolidated by DoorDash; acquisition completed 2025-10-02] / Just Eat multi-platform aggregation | Mandatory (for delivery operators) |
| Inventory Management | Purchasing / receiving / stocktaking / cost cards / supplier management | Mandatory |
| Scheduling & Timekeeping | Shift scheduling / attendance / labor hours / labor efficiency reports | Recommended |
| Financial Reconciliation | Multi-platform reconciliation / cost accounting / profit analysis | Recommended |
| BI & Reporting | Operational dashboard / location ranking / anomaly alerts | Recommended |
| Supply Chain | Supplier collaboration / central kitchen / WMS / TMS | Mandatory for chains |
| Marketing Tools | Coupon distribution / group deals / flash sales / WhatsApp / social commerce | Recommended |
| Customer Service | In-app chat / ticketing / knowledge base / sentiment analysis | For large brands |
| AI Capabilities | Demand forecasting / smart scheduling / personalized recommendations / visual recognition | L4+ stage |

---

## Step 2: Build vs. Buy Decision

### Decision Tree

```
Is this related to core competitive differentiation?
  +-- Yes -> Is there no mature off-the-shelf solution in the market?
  |          +-- Yes -> Build in-house (e.g., unique AI pricing algorithm)
  |          +-- No -> Buy off-the-shelf + deep customization
  +-- No -> Is there a mature SaaS solution?
             +-- Yes -> Purchase directly
             +-- No -> Evaluate then decide
```

### Build vs. Buy Decision Matrix

| Decision Dimension | Favors Build | Favors Buy |
|-------------------|--------------|------------|
| Core differentiation? | Yes | No |
| Mature market solutions? | None / immature | Mature solutions available |
| Time-to-market urgency | Low (>12 months) | High (<3 months) |
| IT team capability | Strong (in-house dev team) | Weak (no dev team) |
| Customization degree | Very high (>50% needs customization) | Low (standard features sufficient) |
| Total cost of ownership | Cheaper long-term to build | Cheaper short-term via SaaS |
| Vendor lock-in risk | Unacceptable | Acceptable |

### Procurement Strategy by Client Size

| Client Size | Recommended Strategy | In-House % | Typical System Choices |
|-------------|---------------------|:---:|------------------------|
| 1-3 locations | 100% SaaS | 0% | Toast / Square / Lightspeed |
| 3-10 locations | Core SaaS + 2-3 tools | 0-5% | Square + Mailchimp / Toast + SevenRooms |
| 10-100 locations | SaaS main + 1-2 in-house differentiators | 5-15% | Core POS (Toast/Lightspeed) + in-house CRM/data |
| 100-1,000 locations | In-house platform + application SaaS | 20-40% | In-house middle-platform + best-of-breed SaaS per category |
| 1,000+ locations | In-house core + SaaS supplementary | 50-70% | In-house PaaS + open ecosystem |

---

## Step 3: Vendor Long List Construction

### Information Source Priority

1. **Peer recommendations** (especially CTO/CIO referrals from same scale / same format) -- most reliable
2. **Industry events** (National Restaurant Association Show, MURTEC, FSTEC) -- market understanding
3. **Analyst reports** (Gartner / IDC / Forrester) -- reference but don't blindly trust
4. **Vendor websites / Demos** -- requires cross-validation
5. **Social media / review sites** (G2, Capterra, restaurant operator forums) -- supplementary reference

### Long List Standard Format

```
Vendor Name | Product | Founded | Funding Round | Total Clients | Restaurant Client % | Target Segment | Notes
```

> See `references/restaurant-tech-vendor-landscape.md` for detailed information on 60+ vendors.

---

## Step 4: Short List Screening Criteria

Select 3-5 vendors from the long list:

| Screening Criteria | Weight | Passing Standard |
|-------------------|:---:|------------------|
| Restaurant industry focus | 20% | Restaurant clients >50% of total revenue |
| Client scale match | 20% | Has same-scale client case studies |
| Product functionality match | 25% | Core requirement coverage >80% |
| Company stability | 15% | Founded >3 years, profitable or Series B+ |
| Service capability | 10% | Local service team present |
| Openness / API maturity | 5% | API coverage, data export capability |
| Price reasonableness | 5% | Within client budget range |

---

## Step 5: Tech Stack Recommendations

### Tech Stack by Client Stage

**L1-L2 (Early Digitalization): 100% SaaS + Zero In-House + Zero Servers**

| Domain | Recommended | Rationale |
|--------|-------------|-----------|
| POS | Toast / Square / Lightspeed | Fast onboarding, 1-day training |
| Delivery | Uber Eats / DoorDash / Deliverect | Direct use, no integration needed |
| Payment | Stripe / Adyen / Square | Low rates, robust |
| Loyalty | POS built-in | Don't get a separate CRM yet |
| Data | POS built-in reporting | Sufficient for now |
| Cloud | None (SaaS-included) | No self-managed needed |

**L2-L3 (Systematization): Main SaaS + API Integration + Lightweight Data**

| Domain | Recommended | Rationale |
|--------|-------------|-----------|
| POS | Toast / Lightspeed / Oracle MICROS | Open APIs, mature ecosystem |
| KDS | Otter / Fresh KDS / POS-native | High integration |
| CRM | SevenRooms / Punchh (PAR) / Thanx | Specialized restaurant CRM |
| Delivery Aggregator | Deliverect / ItsaCheckmate / Otter | Multi-platform order consolidation |
| Inventory | MarketMan / Craftable / PeachWorks | Restaurant-specific |
| BI | Restaurant365 / Plate IQ / xtraCHEF | Restaurant-vertical |
| Cloud | AWS / Azure / GCP | EC2/VM sufficient, no K8s needed |

**L3-L4 (Data-Driven): Middle-Platform Architecture + Hybrid Cloud + AI Introduction**

| Domain | Recommended | Rationale |
|--------|-------------|-----------|
| Business Platform | In-house / open-source based customization | Decouple application layer |
| Data Platform | Databricks / Snowflake / ClickHouse | Real-time + batch |
| API Gateway | Kong / Apigee / AWS API Gateway | Unified API management |
| Container Platform | K8s (EKS/AKS/GKE) | Elastic scaling |
| AI Engine | OpenAI API / Anthropic API / Google Vertex AI | On-demand calls |
| Cloud | AWS / Azure / GCP / Hybrid | Hybrid architecture |

**L4-L5 (Intelligent): PaaS Foundation + Microservices + AI-Native**

| Domain | Recommended | Rationale |
|--------|-------------|-----------|
| PaaS Foundation | In-house | Open ecosystem |
| Microservices | Istio + K8s | Service mesh |
| Data Platform | In-house + open source (Apache ecosystem) | Full autonomy |
| AI Platform | Multi-model gateway + in-house Agent platform | Model-agnostic |
| Edge Computing | In-store edge nodes | Offline-capable |
| Cloud | Multi-cloud + private cloud | No single cloud lock-in |

---

## Deliverables
- Requirements capability matrix (12-module checklist + priorities)
- Build vs. buy decision analysis
- Vendor long list -> short list
- Recommended tech stack

## Quality Checks
- [ ] Every build decision has a clear core rationale
- [ ] Short list contains at least 3, at most 5 vendors
- [ ] Tech stack recommendation matches client size/stage
- [ ] No over-engineering (lower the barrier, lower the cost, the better)
