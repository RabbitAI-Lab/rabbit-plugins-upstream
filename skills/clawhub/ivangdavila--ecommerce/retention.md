# Retention — Second Orders, LTV and the Flows That Produce Them

Acquisition buys a customer once; retention decides whether that purchase was an investment or an expense. The whole discipline reduces to one question per category: **what is the natural repurchase cycle, and is this customer inside it or past it?**

**Before designing flows or quoting LTV**, read `## Metrics` (repeat rate, AOV, CM%) and `## Unit Economics` in `~/Clawic/data/ecommerce/memory.md`. An LTV built on revenue rather than contribution margin overstates what you can spend to acquire by roughly the inverse of CM% (SKILL.md Rule 5).

## The Numbers That Govern It

```
Contribution LTV = AOV × CM% × orders per year × years retained
Repeat rate (90d) = customers with ≥2 orders within 90 days ÷ customers in the cohort
Repurchase cycle  = median days between order 1 and order 2 (median, never mean — one annual buyer distorts the mean)
Churn proxy       = no order in 3 × repurchase cycle
```

Worked: AOV 47, CM% 44%, 2.4 orders/year, retained 1.8 years → contribution LTV = 47 × 0.44 × 2.4 × 1.8 = **89.3**. At `target_ltv_cac` 3 that allows a CAC of ~30 — and the cash gate still applies: first-order CM is 47 × 0.44 = 20.7, so anything above that CAC is funded from working capital until the second order lands (`acquisition.md`).

- **The second order is the whole game.** The probability of a third order given a second is far higher than the probability of a second given a first, in every category. Spend the retention budget on the window between order 1 and order 2.
- Consumables and replenishables can reach 25-40% 90-day repeat rates; considered purchases (furniture, electronics) are structurally lower and should be measured on a 12-24 month window instead. Measuring a mattress store on 90-day repeat rate produces despair and bad decisions.
- **Compare cohorts of equal maturity only.** A cohort measured at day 40 always looks worse than one measured at day 90; that comparison is the most common reporting error in retention.

## Cohorts, Read Correctly

Build the table once: acquisition month down the side, months since acquisition across the top, cumulative contribution margin per customer in the cells.

- The **shape** of the curve matters more than any single number: a curve that flattens means a stable repeat base; one that keeps rising means genuine loyalty; one that stops after month one means the store is a one-time-purchase business and should be run as one.
- Compare acquisition channels by cohort, not by first-order ROAS. A channel with a worse CAC and a much better curve is the better channel, and blended reporting hides this completely (`analytics.md`).
- The month a cohort's cumulative CM crosses its CAC is the **payback month**. That number, not the ratio, decides how fast the store can grow without financing.

## RFM Without Ceremony

Segment on three fields the store already has — recency, frequency, monetary value — and act differently on five groups:

| Segment | Rule of thumb | Action |
|---|---|---|
| New (1 order, inside the cycle) | Order 1, days since < cycle | Onboarding and second-order flow; the highest-value intervention in the store |
| Active repeat | ≥2 orders, inside the cycle | Cross-sell to adjacent categories; do not discount — they are already buying |
| At risk | Past 1× cycle, inside 2× | Reminder with utility (restock, care, how-to), no discount yet |
| Lapsed | Past 2-3× cycle | Win-back with an incentive, capped by `max_discount_pct` |
| Best customers | Top decile by contribution | Early access, human contact, and never a worse offer than a stranger gets |
| Never let a discount reach | Anyone who buys full price at the natural cycle | The offer costs margin and buys nothing |

The last row is the one stores skip: an always-on discount flow pays customers who were going to buy anyway. Suppress it for active repeat buyers and measure the difference with a holdout.

## The Flow Ladder

Timings anchor to the **repurchase cycle**, not to a calendar copied from another store.

| Flow | Trigger | Content | Discount |
|---|---|---|---|
| Order confirmation | Purchase | What was bought, when it arrives, how to reach a human | Never — this is the most-opened email a store sends; use it for expectations, not promotions |
| Shipping and delivery | Dispatch, out for delivery, delivered | Tracking on your own domain | Never |
| Onboarding / how to use | Delivery + 2-3 days | Setup, care, getting value — reduces returns as much as it builds loyalty | Never |
| Review request | Delivery + 7-14 days, after the value moment | One question, one click | Small incentive, disclosed if given |
| Replenishment / second order | 0.7 × repurchase cycle | The obvious next item, or the same one | Only if the category needs it |
| At risk | 1× cycle | Utility content, new arrivals in their category | None |
| Win-back | 2-3× cycle | Direct: "here is what changed" | Yes, capped |
| Post-return recovery | Refund issued | Alternative product, size help — the return is not a goodbye | Small |

- **Suppression rules matter more than the flows**: nobody receives two flows in a day, a discount flow never reaches an active repeat buyer, and any customer with an open support ticket is suppressed from promotional sends entirely.
- Measure every flow against a **holdout** (5-10% receiving nothing). Attribution inside an email platform credits the flow for orders that were coming anyway; the holdout is the only number that is real.
- Owned channels beat rented ones on margin because they have no CAC — but list quality decays. Send frequency that grows unsubscribes faster than revenue is a loan against next year (`acquisition.md`).

## Loyalty and Subscription-Adjacent Mechanics

| Mechanic | Works when | Fails when |
|---|---|---|
| Points | Repeat cycle is short and the category is competitive | Points become a liability nobody redeems and the discount is permanent |
| Tiers with real benefits (early access, free returns, human support) | Best customers are identifiable and the benefits cost less than the retained margin | Tiers reward spending the customer would do anyway |
| Paid membership | The benefit is worth more than the fee to a real segment | The fee is a discount on frequency you already had |
| Replenishment subscription | Genuinely consumable products | Applied to considered purchases (`subscriptions.md`) |
| Referral | Product is talked about, and payout waits for the return window | Payout before the window closes invites farming (`fraud.md`) |

Points and store credit are money: treat balances with the same atomic write discipline as stock and carry the liability in the accounting (SKILL.md Rule 3).

## Reviews and UGC

- Ask once, at the value moment, with one question. A review request that arrives before delivery collects nothing but annoyance.
- Publish the negative ones. Visible criticism raises trust in the positive ones and is required in several markets if you claim reviews are genuine (`conversion.md`).
- Respond to bad reviews factually and briefly, then resolve privately — publicly offered compensation becomes the price of a bad review (`support.md`).
- Review content is product feedback: the phrase that recurs in three-star reviews usually names the next return-rate fix (`returns.md`).

**Write after retention work**: repeat rate, cohort payback month, contribution LTV and their `as of` dates into `## Metrics`; a flow's holdout-measured incremental result into `experiments/<year>.md`; the repurchase cycle per category and the suppression rules into `artifacts/policy-lifecycle.md`; the chosen ESP into `config.yaml` under `integrations`; and the flow review cadence into `## Due` — each with its `## Boxes` line in the same turn (`memory-template.md`). Segment sizes are stored, customer lists are not (SKILL.md Rule 9).
