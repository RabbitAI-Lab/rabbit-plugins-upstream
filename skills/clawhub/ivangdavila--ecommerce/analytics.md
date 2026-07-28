# Analytics — Numbers You Can Defend

Two tools disagreeing is almost never a bug: it is **two definitions, two denominators, or two attribution windows**. The work is to write the definitions down once, instrument them once, and read them the same way every month.

**Before quoting or comparing any number**, read `## Metrics` in `~/Clawic/data/ecommerce/memory.md` (or `metrics.md` if `## Boxes` points there) and the tracking plan artifact if one exists. A current-month number with no prior months is not an answer.

## The Definitions Are the Deliverable

Copy these into the store's tracking plan and change them only deliberately:

| Metric | Definition that must be written down |
|---|---|
| Session | The analytics tool's session, with its timeout and its restart rules — never assume two tools agree |
| Conversion rate | Orders ÷ sessions, same window, split by device. State whether cancelled and refunded orders are excluded (they should be for margin work, included for funnel work) |
| Revenue | Net of discounts, excluding tax and shipping unless stated. The platform, the analytics tool and the accountant each default to a different one |
| AOV | Revenue ÷ orders, same revenue definition |
| New customer | First paid order, keyed on the customer record, not on a cookie |
| CAC | Paid spend ÷ new customers in the same window. State whether agency fees and creative costs are included |
| Return rate | By units or by value — pick one; they differ by a lot in mixed-basket categories |
| Attribution window | Click and view windows, per platform, stated next to any ROAS figure |

A number without its definition and its `as of` date is a rumour. That is why every row written to `## Metrics` carries both (`memory-template.md`).

## The Tracking Plan

One document, versioned, owned: every event, when it fires, its properties, and which report depends on it (`artifacts/tracking-plan.md`).

Minimum ecommerce event set, and it maps to the funnel in `checkout.md`: `product_viewed · collection_viewed · search_performed · add_to_cart · cart_viewed · checkout_started · contact_completed · address_completed · shipping_selected · payment_started · order_placed · refund_issued`.

- Every event carries the same identifiers: product id, SKU, variant, price, currency, quantity, and the order id where one exists. Missing currency is the most common cause of a revenue figure that is off by a conversion rate.
- **Instrument the server for money events.** `order_placed` fired in the browser is lost to blockers, closed tabs and failed redirects; fired from the order-created webhook it matches the platform (`payments.md`).
- Version the plan and note the date of every change. Half of "the numbers broke in April" investigations end at a tag someone added in April.
- After every theme change, app install or replatform, re-verify the plan end to end. Analytics breaks on cutover more often than the store does (`platforms.md`).

## Consent and Measurement Loss

- In the EU/UK, non-essential tags require consent before firing; a consent banner installed after the tags is a compliance gap and a data gap at once.
- Expect a structural share of conversions to be **modelled rather than observed** after consent loss and browser restrictions. Model outputs are fine for pacing and useless for adjudicating between two channels.
- Server-side tagging and platform conversion APIs recover some signal and improve match quality; neither restores certainty, and both add a system to maintain.
- Consent state is data: the banner's own analytics (accept rate by market) explains year-on-year traffic "drops" that never happened (`tax.md`).

## Reconciling the Sources

Run this monthly; the deltas are stable once you know them, and a change in a delta is the alarm:

| Pair | Expected difference | Investigate when |
|---|---|---|
| Platform orders vs analytics orders | Analytics lower — blocked tags, consent | The gap moves more than a few points month to month |
| Platform revenue vs processor gross | Processor lower — pending, failed, multi-processor orders | Any unexplained residue after refunds and disputes (`payments.md`) |
| Processor gross vs bank payout | Fees, reserve, timing, FX | The formula in `payments.md` does not close |
| Ad platform conversions vs platform orders | Platforms over-claim, and they double-count each other | Sum of platform-claimed orders exceeds actual orders — always investigate before believing any single ROAS |
| Marketplace reports vs your order records | Fees, refunds, facilitator tax | Payout does not match the report (`marketplaces.md`) |

The point of reconciliation is not a perfect match; it is knowing the size and the cause of each gap so a new gap is visible.

## The Monthly Review

Once a month, on a fixed day, close last month and write one row (`## Due`):

1. Sessions, orders, CR, AOV, revenue, CM%, refund rate, CAC — with `as of` = the day you read them.
2. Top three movers versus the prior month, each with a named cause or an explicit "unknown".
3. Channel mix and concentration (`## Channels`).
4. Cohort payback for the cohorts that matured this month (`retention.md`).
5. Inventory position: dead stock, stockouts, cover on A items (`inventory.md`).
6. Anything overdue in `## Due`, stated in one line.

The discipline is the value: a store with 18 monthly rows in one file can answer "is this seasonal?" in seconds, and a store without them will argue about it for an hour.

## Dashboards Without Self-Deception

- One dashboard, up to about a dozen numbers, each with a definition and an owner. A 40-tile dashboard is read by nobody, which is why nobody notices when one of them breaks.
- Show trend, not a point: the current value against the same period last year and the prior period. Single numbers invite over-reaction to noise.
- Segment by device and by new-vs-returning by default; blended numbers hide mix shifts, which are the most common explanation for "everything got worse".
- Alert on the few things that are unambiguous: zero orders in an hour that normally has orders, checkout error rate, payment-method failure, feed disapproval count, stock at zero on an A item.
- Anomalies to check before believing them: bot traffic (sessions up, orders flat), tracking outage (orders flat in analytics, fine in the platform), and a mix shift (a cheap-traffic campaign lowering CR without losing an order).

**Write after analytics work**: the closed month's row into `## Metrics` with its `as of` date and definitions unchanged; the tracking plan and every change to it into `artifacts/tracking-plan.md`; the monthly review day and the tag-audit cadence into `## Due`; any reconciliation gap that turned out to be an incident into `incidents/<year>.md`; and the chosen analytics stack into `config.yaml` under `integrations` — each with its `## Boxes` line in the same turn (`memory-template.md`). Aggregates only: no customer-level exports leave the store (SKILL.md Rule 9).
