# Omnichannel Operations Plan

> **Document ID**: RD-OMNI-____-____
> **Version**: V1.0
> **Date**: _________
> **Client**: _________

---

## 1. Omnichannel Current State

### 1.1 Current Channel Matrix

| Channel | Status | GMV Share | Growth Trend | Assessment |
|---------|:------:|:---------:|--------------|------------|
| Physical Stores | □ Active  □ None | ____% | | |
| Branded App / Mini-Program (WeChat/WhatsApp) | □ Active  □ None | ____% | | |
| Marketplaces (Amazon / Shopify) | □ Active  □ None | ____% | | |
| Social Commerce (TikTok / Instagram Shopping) | □ Active  □ None | ____% | | |
| On-Demand Delivery (Uber Eats / DoorDash / Deliveroo) | □ Active  □ None | ____% | | |
| Private Domain (WhatsApp Business / Messenger) | □ Active  □ None | ____% | | |
| Content & Community (Instagram / Pinterest) | □ Active  □ None | ____% | | |
| Cross-Border E-Commerce | □ Active  □ None | ____% | | |

### 1.2 Omnichannel Maturity Assessment

| Dimension | Current | Target | Gap |
|-----------|:------:|:------:|-----|
| Unified Inventory | L____ | L____ | |
| Unified Orders | L____ | L____ | |
| Unified Membership | L____ | L____ | |
| Unified Pricing | L____ | L____ | |

---

## 2. Omnichannel Strategy

### 2.1 Channel Positioning

| Channel | Strategic Role | Function | Investment Priority |
|---------|---------------|----------|:-------------------:|
| Physical Stores | Experience + Service + Instant Fulfillment | Foundation | P0 |
| Branded App / Mini-Program | Private-Domain Transactions + Member Services | Profit Channel | P0 |
| Marketplaces (Amazon / Shopify) | Public Traffic + Brand Credibility | Traffic + Volume | P1 |
| Social Commerce (TikTok / Instagram) | Content Discovery + New Customer Acquisition | Incremental Channel | P1 |
| On-Demand Delivery (Uber Eats / DoorDash) | Immediate Demand Fulfillment | Incremental Channel | P1 |
| Messaging (WhatsApp / Messenger) + Communities | Connection + Repeat Purchase + Referral | Customer Relationship | P0 |
| Content Platforms (Instagram / Pinterest) | Discovery + Word of Mouth | Brand Affinity | P2 |

### 2.2 Omnichannel KPIs

| Metric | Current | 6 Months | 12 Months | 18 Months |
|--------|:------:|:--------:|:---------:|:---------:|
| Online Sales Share | ____% | ____% | ____% | ____% |
| Omnichannel Member Count | ____K | ____K | ____K | ____K |
| Member Identification Rate | ____% | >70% | >85% | >95% |
| On-Demand Order Share | ____% | ____% | ____% | ____% |
| Private-Domain GMV Share | ____% | ____% | ____% | ____% |

---

## 3. Unified Inventory ("One Pool of Stock")

### 3.1 Inventory Sharing Strategy

| Inventory Type | Description | Allocation Rule |
|----------------|-------------|-----------------|
| Omnichannel Shared Stock | Available to all channels | First come, first served |
| Store-Exclusive Stock | Offline only | Not available online |
| E-Commerce Exclusive Stock | Online only | Not available offline |
| Safety Stock | Reserved (offline baseline / surge buffer) | Dynamically calculated (typically 15–30% reserved) |

### 3.2 Fulfillment Models

| Model | Best For | Speed | Cost |
|-------|----------|:-----:|------|
| Click & Collect (BOPIS) | Customer near a store | Immediate | Low |
| Ship from Store | Store inventory can cover | Same-Day / Next-Day (local) | Medium |
| Ship from DC | Store out of stock / long distance | 1–3 Days | Low |
| Drop Ship (Vendor Direct) | Long-tail / bulky / custom | 1–5 Days | Lowest |
| On-Demand Delivery (Uber Eats / DoorDash) | 30-min to 1-hr O2O | 30 min – 1 hr | High |

### 3.3 Order Routing Logic

```
Incoming Order →
  ① Has a designated pickup store? → Lock that store's inventory
  ② Find nearest store to delivery address with stock → Ship from Store
  ③ Nearest store out of stock → Ship from DC
  ④ DC also out of stock → Cross-store transfer / Drop Ship
```

---

## 4. Private-Domain & Direct-to-Consumer Operations

### 4.1 Private-Domain Channel Matrix

| Touchpoint | Function | Operating Strategy |
|------------|----------|--------------------|
| WhatsApp Business / Messenger | 1:1 Connection + Tags + Service | Post-payment opt-in + dedicated sales associate |
| Communities / Groups | Content + Campaigns + Referrals | Segmented operations (by store / tier / interest) |
| Branded App / Mini-Program | Transactions + Membership + Engagement | Flash sales / group buys / member day / points redemption |
| Live Shopping (TikTok / Instagram Live) | Live-Streaming + Content | Brand story + store live-streams + influencer collaborations |
| Social Channels (Instagram / TikTok) | Content + Reach | Brand affinity + campaign notifications |

### 4.2 AIPL Operating Cadence

| Stage | Goal | Activities | Frequency |
|-------|------|------------|:---------:|
| A to I (Awareness to Interest) | Follow + Claim Offer | Welcome gift, hero product showcase, limited-time discount | New user triggered |
| I to P (Interest to Purchase) | First-Order Conversion | First-order discount, new-customer exclusive price, gift with purchase | Within 7 days of following |
| P to L (Purchase to Loyalty) | Repeat & Loyalty | Stored value, member day, birthday perks, dedicated consultant | Ongoing + lifecycle triggered |
| L to Advocacy | Referral & Viral Growth | Group buy, affiliate commission, invite-a-friend rewards | Monthly campaigns |

---

## 5. Omnichannel Technology Architecture

### 5.1 Target Architecture

```
           ┌──────────────────────────────────────┐
           │         Omnichannel Middleware         │
           │  ┌────────┬────────┬────────┬────────┐ │
           │  │Product │ Order  │Inventory│ Member │ │
           │  │ Center │ Center │ Center │ Center │ │
           │  └────────┴────────┴────────┴────────┘ │
           └──────────────────────────────────────┘
                              │
      ┌───────────────────────┼───────────────────────┐
      │                       │                       │
  ┌───▼───┐             ┌─────▼─────┐           ┌─────▼─────┐
  │Offline │             │  Online    │           │ On-Demand │
  │  POS   │             │E-Com / App │           │    O2O    │
  └───────┘             └───────────┘           └───────────┘
```

### 5.2 Core Systems

| System | Recommended Solution | Key Capability |
|--------|----------------------|----------------|
| OMS | | Omnichannel order routing + inventory allocation + fulfillment tracking |
| Inventory Middleware | | Real-time inventory + channel allocation + safety stock |
| CDP | | OneID + tags + profiles + segmentation |
| MA | | Automated journeys + multi-touchpoint triggers |

---

## 6. Implementation Plan

| Phase | Timeline | Focus | Milestone |
|-------|----------|-------|-----------|
| Phase 1 | Months 0–3 | Branded app / mini-program + private-domain foundation | App launch + opt-in rate >40% |
| Phase 2 | Months 3–6 | On-demand delivery + O2O go-live | Inventory accuracy >95% + O2O live |
| Phase 3 | Months 6–12 | Omnichannel unified inventory | Unified inventory / orders / membership across channels |
| Phase 4 | Months 12–18 | AI-powered omnichannel | AI smart routing + personalized recommendations |

---

## 7. Investment & ROI

| Investment Item | Year 1 | Year 2 |
|-----------------|:------:|:------:|
| OMS + Inventory Middleware | $____ | $____ |
| CDP + MA | $____ | $____ |
| App / E-Commerce | $____ | $____ |
| On-Demand Delivery Integration | $____ | $____ |
| Operations Team | $____ | $____ |
| **Total** | **$____** | **$____** |
| **Projected Incremental GMV** | **$____** | **$____** |

---

> The omnichannel operations plan should be reviewed quarterly and strategy adjusted semi-annually.
