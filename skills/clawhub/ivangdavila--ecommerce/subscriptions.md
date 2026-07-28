# Subscriptions — Recurring Revenue in a Physical-Goods Store

A subscription is a promise to charge and ship repeatedly. Its economics are ruled by two numbers that a one-off store never has to face: **churn** and **involuntary failure**. Most subscription stores lose more revenue to failed cards than to unhappy customers, and only one of those is a product problem.

**Before designing or debugging a subscription program**, read `## Metrics` (churn, repeat rate) and the dunning ladder artifact if `## Boxes` names one. Retention curves for subscriptions are read differently from one-off cohorts (`retention.md`).

## Does This Product Even Want a Subscription?

| Fits | Does not fit |
|---|---|
| Genuinely consumed on a predictable cycle (coffee, supplements, razors, pet food) | Considered, durable purchases dressed up as a subscription |
| Value is convenience or price certainty | Value is "we would like recurring revenue" |
| The customer can predict their own usage | Consumption varies so much that every cycle needs an edit |
| Restock timing is boring to manage manually | Choice is part of the pleasure of buying |

The honest alternative for products that do not fit: a **replenishment reminder** at 0.7 × repurchase cycle with a one-click reorder. It captures most of the revenue with none of the churn management or the cancellation friction (`retention.md`).

## The Numbers

```
Monthly churn c → average lifetime ≈ 1 ÷ c cycles
Subscriber LTV  = per-cycle CM ÷ churn rate
Involuntary churn share = failed-payment cancellations ÷ all cancellations
```

Worked: per-cycle CM 14, monthly churn 8% → average lifetime 12.5 cycles → LTV ≈ 175. Cut churn to 6% and lifetime becomes 16.7 cycles, LTV 233 — a 33% LTV gain from two points of churn, which is why churn work outranks acquisition work in a subscription store.

- Churn is **highest at cycle 1-2** and flattens after; a single blended churn number hides whether the problem is onboarding or fatigue. Report churn by cycle number, not by month.
- Track **voluntary and involuntary separately**. Involuntary churn is a payments problem with a technical fix; voluntary churn is a product or value problem. Reporting them together guarantees the wrong fix.
- Prepaid plans (3, 6, 12 cycles) remove churn inside the term and bring cash forward, at the cost of a discount. Compare `prepaid CM × cycles` against `monthly CM × expected lifetime` before offering one.

## Dunning: The Ladder for Failed Payments

Cards expire, get reissued and hit limits. This is normal traffic, not customer intent.

| Attempt | Timing | Change | Message |
|---|---|---|---|
| 1 | On failure | — | Silent for soft declines; a hard decline goes straight to attempt 2's message |
| 2 | +2 days | Retry, same amount | "Your payment did not go through — update your card" with a one-click link |
| 3 | +4 days | Retry, consider a different day of month | Reminder with the shipment date at risk |
| 4 | +7 days | Final retry | "Your next box is on hold" — the consequence, not a plea |
| Close | +10-14 days | Pause the subscription rather than cancelling it | Cancellation is a decision the customer did not make; a pause keeps the record intact |

- **Never retry a hard decline** (lost, stolen, invalid account) — update the method instead. Card networks cap re-attempts of a declined authorization and fine merchants beyond it; the processor publishes the current number (`payments.md`).
- **Card-updater services and network tokens** prevent a large share of these failures before dunning starts. Enabling them is usually a checkbox and the highest-return item in this file.
- Send the pre-renewal notice **before** the charge for anything above a trivial amount, and always where the law requires it — surprise renewals are the single largest source of subscription disputes (`fraud.md`).
- Every dunning message links to a self-service card update that does not require a login the customer has forgotten.

## Cancellation, Pause and Skip

- **Offer pause and skip before cancel.** A skip preserves the subscription and most of its LTV; a cancellation loses all of it. Most cancellations at cycle 2-3 are "I have too much of it", which a skip solves exactly.
- The cancel path must be **as easy as the signup path** — a legal requirement in a growing number of markets and, regardless, an obligation-free way to avoid chargebacks and complaints. Retention offers may be shown once, not as a maze.
- Ask one question on cancel — too much product, too expensive, no longer needed, quality, service — and route each to a different offer: skip, downgrade cadence, smaller size, human contact. Answering all five with a discount wastes margin on four of them.
- Win-back for cancelled subscribers works at 2-3× the cycle, with what changed rather than with a discount (`retention.md`).

## Operating the Program

- **Cadence flexibility beats discount depth.** Letting the customer set every 4, 6 or 8 weeks reduces churn more than another 5% off, because the top cancellation reason is accumulation.
- Charge and ship dates must be separated in the system: charge fails → hold the shipment, do not ship unpaid and reconcile later.
- Forecast inventory from subscriber count × cadence, and hold the stock — a subscription stockout breaks a promise, not a wish (`inventory.md`).
- Price increases for existing subscribers need notice and, in many markets, an active right to cancel before the new price applies. Grandfathering the earliest cohort is cheap goodwill (`pricing.md`).
- Address changes matter more than in one-off retail: one wrong address repeats every cycle. Confirm the address on any cycle following a customer edit.

## Subscription Disputes

- Evidence pack for a "cancelled subscription" dispute: the terms accepted at signup with the timestamp, the pre-renewal notice sent, the cancellation flow's record showing no cancellation, and the fulfillment proof for the disputed cycle (`fraud.md`).
- A dispute rate concentrated in subscriptions is a disclosure problem, not a fraud problem: the descriptor, the renewal notice and the cancel path are the three fixes, in that order.
- Refund the current cycle without argument when the customer cancelled and the notice failed. The disputed cycle costs more than the refund and damages the rate that matters.

**Write after subscription work**: churn by cycle, involuntary share, subscriber count and per-cycle CM into `## Metrics` with their `as of` date; the dunning ladder, cadence options and cancellation flow that the store settles on into `artifacts/policy-dunning.md`; the chosen subscription app into `config.yaml` under `integrations`; a dispute pattern into `disputes/<year>.md`; and the pre-renewal notice cadence into `## Due` — each with its `## Boxes` line in the same turn (`memory-template.md`).
