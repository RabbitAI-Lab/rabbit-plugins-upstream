# Marketplaces — Selling Where the Traffic Already Is

A marketplace rents you demand in exchange for margin, price transparency and the customer relationship. The decision is arithmetic first: **rebuild contribution margin with the channel's full fee stack before listing anything**, because a healthy SKU in your store can be a loss-maker there.

**Before listing or expanding a channel**, read `## Channels` (existing fee stacks and revenue share) and `## Unit Economics` in `~/Clawic/data/ecommerce/memory.md`. Channel concentration is a business risk that only shows up in the share column.

## The Fee Stack

```
Marketplace CM = price − COGS − referral/commission − fulfillment fees
                 − storage − ad levy − (higher return rate × return cost) − payment/currency fees
```

Worked against the store's own 49% CM SKU (price 50, COGS 18, freight 4.50, pick/pack 1.50, returns 8% × 6.00):
a 15% referral fee is 7.50, marketplace returns run at roughly double (16% × 6.00 = 0.96), and channel ads at 5% of revenue are 2.50 → CM = 50 − 18 − 7.50 − 4.50 − 1.50 − 0.96 − 2.50 = **15.04, CM% 30%**. Still profitable, but it cannot fund the same discount, the same free shipping, or the same CAC. Raising the marketplace price to protect margin is a decision about being visibly more expensive than your own store.

- Commission percentages vary by marketplace and category, and change; take the current published rate for the exact category rather than a remembered one, and record it in `## Channels` with the date.
- Marketplace-operated fulfillment adds per-unit pick and weight fees plus storage that escalates for slow-moving stock — the long-term storage penalty is what turns a mediocre SKU negative.
- Channel advertising has become close to mandatory for visibility on the largest marketplaces; budget it as a fee, not as an option, when modelling CM.

## When a Marketplace Is Right

| List | Do not list |
|---|---|
| CM after the full fee stack clears the store's floor | The margin only works at a price you would not defend publicly |
| Discovery is the constraint and you have no audience | Your own channel already reaches the same customer more cheaply |
| Product is a known, searched item (replacement parts, standard sizes) | Product needs explanation, fitting, or a brand story |
| Excess or seasonal inventory needs an exit (`inventory.md`) | The SKU is the brand's identity |
| Testing demand in a new country before opening a store there | You cannot service the market's return and support expectations |

Concentration rule: when one marketplace passes roughly a third of revenue, it sets your prices, your service standards and your risk. Treat that threshold as a strategic alarm and write it in `## Channels` (`memory-template.md`).

## Listing Quality Is the Whole Ranking

Marketplace search rewards conversion and sales velocity, so listing work compounds:

- **Title**: brand + product + defining attributes, front-loaded, within the marketplace's character limit and without keyword spam, which several platforms suppress.
- **Images**: main image on a white background with the product filling most of the frame is a hard requirement on the largest platforms; the remaining slots go to scale, in-use, detail and what-is-in-the-box.
- **Attributes and category**: the wrong category cripples a listing more than bad copy. Fill every applicable attribute — they power the filters buyers actually use.
- **Variants as one listing**, not several: splitting variants divides review count and sales velocity, which are the ranking inputs.
- **Reviews**: genuine only. Incentivized, solicited-with-conditions and gated reviews are prohibited on the major platforms and enforcement is account-level, not listing-level.
- Content changes take time to re-index; change one thing at a time and give it a fair window before judging.

## Account Health Is the Real Constraint

Suspension is not a warning, it is a revenue stop that can take weeks to reverse. The metrics differ by marketplace but the categories are constant:

| Metric | What breaks it |
|---|---|
| Order defect / negative feedback rate | Quality and description mismatches, and late responses to buyers |
| Late shipment rate | Cut-off times you cannot actually meet, and holidays not set (`orders.md`) |
| Pre-fulfillment cancellation rate | Overselling — the stock you did not have, which is an inventory problem (`inventory.md`) |
| Valid tracking rate | Handover scans not registering |
| Response time to buyer messages | Weekends, if the calendar is not configured |
| Policy violations | Prohibited claims, wrong category, IP complaints |

Guardrails worth building before volume: a buffer that respects the marketplace's own buffer (never both), a shipping template that matches your real cut-off, holiday mode configured in advance, and someone who reads the account-health dashboard weekly (`## Due`).

## Multi-Channel Operations

- One source of truth for stock, syncing at an interval proportional to velocity, with the buffer formula from `inventory.md`. Two systems owning the number produces the cancellation metric that suspends accounts.
- Normalize every channel's orders into one internal shape at intake, keeping the channel and external id; ops staff working across two consoles miss deadlines (`orders.md`).
- Returns arrive under the marketplace's policy, not yours, and often at a higher rate. Model that rate separately per channel rather than using the store average (`returns.md`).
- **Marketplace facilitator rules**: in many jurisdictions the marketplace collects and remits the sales tax or VAT on your behalf. That does not remove your registration and reporting obligations, and double-charging or under-reporting are both common — reconcile per channel (`tax.md`).
- Payout lag differs sharply by marketplace (days to weeks) and is a cash-flow constraint on how fast you can restock. It belongs in `## Channels`, and in the plan for peak (`peak.md`).

## Buy Box and Competing on the Same Listing

Where multiple sellers share a listing, the featured offer is won on a mix of price including shipping, fulfillment speed and reliability, seller metrics and stock availability.

- Losing the featured offer usually removes most of the listing's sales. Monitor it as a metric, not as an occasional check.
- Automated repricers protect it and race to the bottom if unconstrained: always set a floor derived from CM (`pricing.md`), never a floor derived from a competitor.
- Counterfeit and hijacked listings on your own brand are a brand-registry and enforcement problem; the cost of not registering the brand appears the first time it happens.
- Deep platform-specific playbooks: `amazon`, `etsy`, `marketplace`.

**Write after marketplace work**: the channel with its full fee stack, payout lag and share of revenue into `## Channels`; channel-specific CM into `## Unit Economics`; an account-health incident or suspension into `incidents/<year>.md`; the account-health review and payout reconciliation cadences into `## Due`; and the listing template, repricing floor policy or the decision to enter or leave a channel into `artifacts/<kebab-name>.md` with its `## Boxes` line (`memory-template.md`).
