---
name: saas-revenue-leak-hunter
version: "1.0.0"
category: business
tags:
  - saas
  - revenue
  - churn
  - retention
  - monetization
  - pricing
  - metrics
  - mrr
  - runway
  - finance
model: claude-sonnet-4-20250514
trigger_keywords:
  - SaaS revenue
  - churn analysis
  - MRR
  - revenue leak
  - retention rate
  - pricing strategy
  - runway calculation
  - subscription metrics
  - LTV
  - CAC
pricing: "$9.99 one-time"
---

# SaaS Revenue Leak Hunter & Monetization Repair Engine

> **Find where your SaaS is losing revenue and fix it.** Analyzes churn patterns, pricing misalignment, feature gating, dunning failures, and upgrade friction — outputs a 90-day revenue rescue plan with prioritized fixes and projected MRR recovery.

## Why This Skill Exists

Most SaaS founders don't know they're losing 15-30% of potential revenue to preventable leaks: failed payments, poor tier gating, underpricing, manual churn, and missing upsell triggers. This skill acts as a fractional CFO for your SaaS.

## When to Activate

Activate when the user:
- Asks about SaaS metrics, churn, MRR, LTV, CAC, or runway
- Wants to analyze or reduce churn
- Needs pricing strategy or tier optimization
- Says "why am I losing revenue" or "how to increase MRR"
- Plans a pricing change or feature gating strategy
- Needs to calculate runway or burn rate

## Workflow

### Step 1: Revenue Audit — Identify Leak Sources

Analyze each revenue leak category:

#### 1.1 Payment Failure Leaks (Dunning)
| Metric | Formula | Healthy | Warning | Critical |
|--------|---------|---------|---------|----------|
| Failed payment rate | failed_charges / total_charges | <2% | 2-5% | >5% |
| Dunning recovery rate | recovered_after_retry / failed_total | >70% | 50-70% | <50% |
| Involuntary churn rate | churned_due_to_payment_failure / total_customers | <1% | 1-3% | >3% |

**Common leaks:**
- Retry strategy too aggressive (3 retries in 3 days = panic)
- Retry strategy too passive (1 retry in 14 days = forgotten)
- No email/SMS notification on failed payment
- Card update flow buried in settings

#### 1.2 Churn Leaks (Voluntary)
| Churn Type | Typical Rate | Fix Difficulty |
|-----------|-------------|----------------|
| Early churn (month 1) | 10-20% | Medium — onboarding fix |
| Mid-life churn (month 2-6) | 5-10% | Hard — product fit |
| Late churn (month 6+) | 2-5% | Easy — engagement + value reminder |

**Diagnostic questions:**
- What % of churned users completed onboarding?
- What % of churned users used the core feature ≥3 times in week 1?
- Are churned users concentrated in a specific plan tier?
- Is there a "churn signal" (usage drop pattern) 14 days before cancellation?

#### 1.3 Pricing & Tier Misalignment
- **Underpricing**: Are users on annual plans getting >40% discount? (standard is 15-20%)
- **Feature gating**: Are premium features gated too aggressively (hurting activation) or too loosely (leaving money on table)?
- **Free tier abuse**: What % of free users have been active >6 months without converting?
- **Plan distance**: Is the jump from Pro to Team too large (users get stuck) or too small (no incentive to upgrade)?

#### 1.4 Upsell & Expansion Revenue Leaks
- **Missing upgrade triggers**: No in-app prompt when user hits usage limit
- **No usage-based overage**: Users hit limit and wait instead of paying for more
- **No seat expansion**: Team admin doesn't see "add seat" option easily
- **Annual discount too steep**: Users save too much by switching to annual (lose monthly expansion)

#### 1.5 Onboarding-to-Paid Leaks
| Funnel Stage | Healthy Conversion | Common Leak |
|-------------|-------------------|-------------|
| Signup → Activation | >60% | Missing "aha moment" in first 5 minutes |
| Activation → Trial | >40% | No clear CTA after activation |
| Trial → Paid | >25% | Trial too long (14d) or too short (3d) |
| Paid → Month 2 retention | >85% | First-month value not demonstrated |

### Step 2: Quantify Each Leak

For each identified leak, calculate:

```markdown
## Revenue Leak Quantification

### Leak #1: Failed Payment Recovery
- Current failed payment rate: 4.2% (⚠️ Warning)
- Current dunning recovery rate: 45% (🔴 Critical)
- Monthly failed charges: $3,200
- Monthly recovered: $1,440
- Monthly lost: **$1,760**
- If recovery improved to 70%: $2,240 recovered → **+$800/mo**

### Leak #2: Early Churn (Month 1)
- Month-1 churn rate: 18% (🔴 Critical)
- New signups/month: 200
- Lost customers/month: 36
- Average MRR per customer: $49
- Monthly revenue lost: **$1,764**
- If churn reduced to 10%: 20 lost → save **$784/mo**

### Leak #3: Missing Upgrade Triggers
- Users hitting usage limit/month: ~120
- Current conversion to upgrade: 8%
- If upgrade prompts added (target 15%): 18 upgrades vs 10
- Additional revenue: 8 × $29 (upgrade delta) = **+$232/mo**

### Total Identified Leaks: $3,756/month ($45,072/year)
```

### Step 3: Generate 90-Day Revenue Rescue Plan

```markdown
# 90-Day Revenue Rescue Plan

## Phase 1: Quick Wins (Days 1-30) — Projected: +$1,800/mo

### Week 1: Fix Dunning
- [ ] Switch to Stripe Smart Retries (adaptive retry timing)
- [ ] Set up 3-email dunning sequence:
  - Email 1 (day 1): "Payment failed — update card" (friendly)
  - Email 2 (day 3): "Your subscription is paused" (urgency)
  - Email 3 (day 7): "Final notice — update card to keep access" (scarcity)
- [ ] Add card update link directly in email (1-click, no login required)
- [ ] Add billing alert in-app banner for failed payments
- **Projected impact**: +$800/mo

### Week 2-3: Onboarding Repair
- [ ] Map the "aha moment" (first dashboard created within 5 minutes)
- [ ] Add progress checklist in onboarding (4 steps with checkmarks)
- [ ] Add in-app tooltip on core feature after signup
- [ ] Send day-3 email with example use case
- **Projected impact**: +$784/mo (reduced month-1 churn from 18% to 10%)

### Week 4: Upgrade Triggers
- [ ] Add usage limit banner at 80% and 100% of plan limit
- [ ] Add "Upgrade for unlimited" CTA on limit modal
- [ ] Add seat management page for Team plan
- [ ] Create "Annual Plan - Save 2 months" upgrade offer at month 2
- **Projected impact**: +$232/mo

## Phase 2: Structural Fixes (Days 31-60) — Projected: +$1,200/mo

### Pricing Tier Optimization
- [ ] Audit feature distribution across tiers
- [ ] Move 1 high-value feature from Free to Pro to increase conversion
- [ ] Add mid-tier between Pro ($49) and Team ($149) at $89
- [ ] Test annual discount: 20% (not 40%)
- **Projected impact**: +$600/mo

### Win-Back Campaign
- [ ] Build list of churned users in last 90 days
- [ ] Send "We miss you — 50% off for 3 months" email
- [ ] Target only users who completed onboarding
- **Projected impact**: +$400/mo

### Expansion Revenue
- [ ] Add API access as paid add-on ($29/mo)
- [ ] Add priority support as paid add-on ($19/mo)
- [ ] Create "Power User" survey for top 10% users
- **Projected impact**: +$200/mo

## Phase 3: Growth Acceleration (Days 61-90) — Projected: +$800/mo

### Referral Program
- [ ] Build "Give $20, Get $20" referral system
- [ ] Add referral prompt after user creates 3rd project
- [ ] Track referral-attributed signups
- **Projected impact**: +$400/mo

### Annual Migration Campaign
- [ ] Email all monthly subscribers with "Switch to annual, save 20%"
- [ ] Add countdown timer (limited time offer)
- [ ] Track annual conversion rate
- **Projected impact**: +$200/mo (improved cash flow + retention)

### Feature Launch as Upsell
- [ ] Ship 1 new "Pro-only" feature per month
- [ ] Show teaser in Free plan (locked)
- [ ] Track free-to-pro conversion after feature launch
- **Projected impact**: +$200/mo

## Summary
| Phase | Timeline | Projected Monthly Impact |
|-------|----------|------------------------|
| Phase 1 | Days 1-30 | +$1,800/mo |
| Phase 2 | Days 31-60 | +$1,200/mo |
| Phase 3 | Days 61-90 | +$800/mo |
| **Total** | **90 days** | **+$3,800/mo ($45,600/yr)** |
```

## Output Constraints

- Every revenue leak must include dollar amount and recovery estimate
- Every recommendation must be specific enough to implement (not "improve retention")
- Priority must be based on ROI (impact × ease of implementation)
- All calculations must show the formula used
- Conservative projections only — better to under-promise and over-deliver

## What This Skill Does NOT Do

- Does not access your Stripe/billing data directly (analyzes what you provide)
- Does not replace a CPA or financial advisor
- Does not handle tax optimization or legal entity structuring
- Does not forecast market conditions or competitive dynamics
