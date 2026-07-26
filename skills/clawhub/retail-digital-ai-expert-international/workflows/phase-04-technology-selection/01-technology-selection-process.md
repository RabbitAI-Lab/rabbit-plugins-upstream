# 01 — Technology Selection Process

> **Trigger**: Target architecture confirmed; need to select specific systems / vendors
> **Deliverables**: Detailed requirements checklist + build-vs-buy decision + tech stack recommendations

---

## 1. Selection Process Overview

```
Step 1: Requirements Checklist → Step 2: Build vs. Buy → Step 3: Long-List (RFI) →
Step 4: Short-List (RFP) → Step 5: 7-Dimension Scoring → Step 6: PoC → Step 7: Decision
```

---

## 2. Step 1: Requirements Checklist

### Functional Requirements (MoSCoW Classification)

| Category | Definition | Example |
|:---:|------|------|
| **M**-Must | Non-negotiable; system is useless without it | POS must support offline mode |
| **S**-Should | Highly important but has workarounds | Should integrate with WhatsApp / WeChat for member sync |
| **C**-Could | Nice-to-have | Could support AI-powered recommendations |
| **W**-Won't | Explicitly out of scope this time | Cross-border capabilities not required for this phase |

### Non-Functional Requirements

| Requirement | Standard |
|------|------|
| Store scale | Support current __ stores, scalable to __ stores within 3 years |
| Daily transaction volume | Peak __ transactions/second |
| Availability SLA | 99.5%+ |
| Response time | Checkout <2 seconds, lookups <1 second |
| Offline capability | Operate offline during network outage, auto-sync on recovery |
| Data residency | Data stored in [Region / Country] |
| Security certifications | SOC 2 / ISO 27001 / GDPR compliant |

---

## 3. Step 2: Build vs. Buy Decision

### Decision Framework

| Decision Dimension | Favor Buy (SaaS) | Favor Build (In-House) |
|------|:---:|:---:|
| Store count | <200 stores | >500 stores |
| Industry standardization | High (needs = industry standard) | Low (needs = competitive differentiator) |
| IT team capability | <10 people | >30 people |
| Market solution maturity | Mature solutions available | No suitable solutions |
| Time requirement | <3 months | >12 months |
| Budget | <$250K/year | >$2.5M/year |
| Customization needs | <20% | >50% |

### Decision Matrix

```
                      Buy SaaS   Hybrid (SaaS + In-House)   Build In-House
Stores <50              ✓
Stores 50-200           ✓                 ✓
Stores 200-500                            ✓                   ✓
Stores 500-2000                           ✓                   ✓
Stores 2000+                                                    ✓ (core) + SaaS (non-core)
```

### Core Principle

> **Under 200 stores: Never build core systems (POS / ERP / WMS) in-house**
> **Competitive differentiators (data / AI / membership) can be considered for in-house build**
> **If it can be bought, is industry-standard, and doesn't create differentiation → always use SaaS**

---

## 4. Step 3: Long-List Screening (RFI)

### RFI (Request for Information) Template Structure

```
1. Company introduction & requirements overview
2. Vendor basic information (founded / size / funding / customers)
3. Product functional coverage (provide function checklist; vendor marks ✓ / ✗ / Partial)
4. Technical architecture (deployment model / API / extensibility)
5. Pricing model (license / subscription / transaction-based)
6. Implementation capability (methodology / typical duration / training)
7. Customer references (3 of similar scale / retail format)
8. Service & support (SLA / response time / support channels)
```

### Long-List → Short-List Screening Criteria

- RFI response completeness
- Functional coverage >80% of Must requirements
- At least 3 customers of similar scale / format
- Pricing within 50-150% of budget range
- Local service team presence

---

## 5. General Tech Stack Recommendations

### By Retail Format

| Format | POS | ERP | WMS | CRM | eCommerce |
|------|------|------|------|------|------|
| Mom-and-Pop Convenience | Square / Toast | — | — | — | Uber Eats / DoorDash |
| Community Supermarket | Lightspeed / Shopify POS | Lightspeed Inventory | — | Shopify CRM | Shopify |
| Apparel Specialty | Shopify POS / Lightspeed | NetSuite / Brightpearl | Extensiv / ShipStation | Klaviyo / Braze | Shopify / BigCommerce |
| Fast Fashion | Cegid / Oracle Xstore | SAP / D365 | Manhattan / Blue Yonder | Salesforce | Shopify / Adobe Commerce |
| Hypermarket | Oracle Retail / SAP | SAP / Oracle Retail | Blue Yonder / Geek+ | Salesforce / In-House | In-House + Amazon / Instacart |
| DTC Brand | Shopify POS | NetSuite / D365 | Extensiv / ShipStation | Klaviyo / Braze | Shopify |
| Franchise Chain | Lightspeed / Oracle Xstore | NetSuite / D365 | Geek+ / Manhattan | Shopify / BigCommerce | Shopify / BigCommerce |
| Global 10K+ Stores | Oracle / SAP | SAP / D365 | Manhattan / In-House | Salesforce | Shopify / In-House |

Detailed vendor information: see `references/retail-technology-vendor-landscape.md`

---

## 6. Common Pitfalls

1. **Vendor demos make everything look essential** → Confirm core requirements first; demos are for validation only
2. **Comparing only price, not TCO** → SaaS annual fees look low but implementation costs are high; open source is free but labor costs are high
3. **Ignoring integration costs** → Selecting a cheap option that costs 3x more to integrate with existing systems
4. **Not considering needs 3 years out** → Works today but can't handle double the stores next year
