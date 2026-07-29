# Checkout — Cart to Paid Order

The funnel where money is lost fastest, because every field is a chance to leave. Two rules govern everything here: **remove a step before optimizing a step**, and **measure per step, never in aggregate** — a 70% abandonment number tells you nothing, a 41% drop at the shipping-method step tells you what to fix.

**Before diagnosing a drop**, read `## Metrics` in `~/Clawic/data/ecommerce/memory.md` for the store's own funnel baseline and `experiments/<year>.md` for what has already been tried. Half of "we should test X" has been tested.

## Instrument the Steps First

| Step | Event to count | Common killer |
|---|---|---|
| Cart viewed | `cart_viewed` | Shipping cost unknown at this point — the single most cited abandonment reason |
| Checkout started | `checkout_started` | Forced account creation |
| Contact captured | `contact_completed` | Email validation rejecting valid addresses (plus-addressing, long TLDs) |
| Shipping address | `address_completed` | Autocomplete fighting manual entry; required fields that do not exist in the country |
| Shipping method | `shipping_selected` | Rate shown here for the first time, or a rate endpoint timing out and showing nothing |
| Payment | `payment_started` | Wallet not offered, or card form rejecting a valid card format |
| Paid | `order_placed` | 3DS challenge in a popup blocked by the browser |

Drop rate per step = 1 − (step ÷ previous step). The step with the worst *relative* drop is the work; the one with the biggest absolute loss is the one to size first. Compare against the store's own history, not benchmarks — traffic mix moves the numbers more than any change you make.

## The Removals That Beat Every Test

Ordered by effect per hour of work, and none of them needs a test to justify:

1. **Guest checkout.** Account creation before payment is a hard stop for first-time buyers; offer account creation *after* the order, prefilled.
2. **Total shipping cost visible in the cart**, estimated from a default location before the address exists. A surprise at step 5 is worse than a number at step 1.
3. **Express wallets above the form** (Apple Pay, Google Pay, PayPal, plus the local method the market expects). They skip four steps and carry their own address data.
4. **One page or one visible progress indicator.** Multi-step is fine if the customer can see how many steps remain; invisible length is what feels endless.
5. **Address autocomplete with a manual escape hatch.** Autocomplete alone strands anyone whose address the provider does not know, and they are exactly the deliveries that go wrong.
6. **Correct input types and autofill tokens** (`autocomplete="cc-number"`, numeric keypad for postal code and card). On mobile this is worth more than layout work.
7. **Errors inline, next to the field, keeping the entered data.** A checkout that clears the card field on error loses a share of customers per attempt.

## Rates, Taxes and Totals in the Checkout

- **Never call an external rate API synchronously without a fallback.** When the carrier endpoint is slow or down, show a cached flat rate rather than an empty method list; a checkout with no shipping option is a checkout with no orders (`fulfillment.md`).
- Tax display follows the market: consumer prices in the EU and UK are shown **tax-inclusive** everywhere, including the product page; US prices are shown pre-tax and tax appears at the address step (`tax.md`).
- Currency and price presentation should switch on the customer's market, but the *charged* currency must match what was displayed — a conversion between display and charge is a dispute waiting to be filed.
- Discount field placement is a real trade-off: a prominent code box sends customers to a coupon site mid-checkout. Collapse it behind a link, and never show it to traffic arriving without a code.

## Abandoned Cart Recovery

The ladder, and the reason for each rung:

| Send | Timing after abandonment | Content | Incentive |
|---|---|---|---|
| 1 | 1 hour | Cart contents, one-click return to the filled cart | None — most recoveries at this stage are interruptions, not price objections |
| 2 | 24 hours | Objection handling: shipping, returns policy, stock level, one review | None |
| 3 | 72 hours | Last call, expiring | Discount or free shipping, capped by `max_discount_pct` |

- Discount on the first email trains the customer to abandon deliberately. This is the most expensive mistake in lifecycle email and it does not show up in the flow's own reporting, because the flow keeps getting more "recoveries".
- Browse-abandonment and cart-abandonment are different audiences; sending both to the same person in a day is how a store gets marked as spam.
- Measure recovery as *incremental* revenue against a holdout, not as revenue attributed to the flow — a share of those customers were coming back anyway.
- SMS recovers faster and costs more per send; it belongs to send 1 or 3, never both.

## Mobile Checkout

Mobile carries most sessions and converts at roughly half the desktop rate in typical DTC stores. Treat the gap as structural and design for capture, not just for conversion:

- Sticky add-to-cart and a persistent cart total; the customer must never scroll to find the next action.
- Wallets first — they are the reason mobile conversion is recoverable at all.
- Any field that can be inferred (country from locale, city from postal code) is inferred and editable.
- Test on a real mid-range Android on a throttled connection; a checkout that is fast on the developer's phone is a checkout tested by nobody (`storefront.md`).

## Cart Mechanics That Break Quietly

| Symptom | Cause | Fix |
|---|---|---|
| Cart empties between pages | Cookie blocked, session bound to a domain the CDN rewrites, or a third-party cookie assumption | Server-side cart keyed to a first-party token |
| Item silently removed at checkout | Stock check at checkout finds it sold out | Say what changed and why, keep the rest of the cart intact (`inventory.md`) |
| Prices differ between cart and checkout | Cart cached with an old price after a price change | Recompute at checkout from stored prices, always (SKILL.md Rule 1) |
| Duplicate orders | Double-click, or a retried submit | Disable the button on submit *and* an idempotency key server-side (`payments.md`) |
| Discount applies to a bundle it should not | No exclusion rules | Stacking policy and a CM floor per cart (`pricing.md`) |
| Free-shipping bar promises a threshold the shipping rule does not honour | Two sources of truth for the threshold | One config value, read by both |

## Reading a Sudden Conversion Drop

In this order, because each step is cheaper than the next:

1. **Place a real test order** on the live store, on mobile, with a real card. Most "mystery drops" end here.
2. Check payment-method health and the shipping-rate endpoint (`payments.md`, `fulfillment.md`).
3. Check what deployed or which app updated in the window — theme changes, app installs and consent-banner updates are the usual three.
4. Only then look at analytics: if tracking broke, conversion did not drop, the *measurement* did (`analytics.md`).
5. Check traffic mix — a spike of cheap or bot traffic lowers conversion rate without losing a single order (`acquisition.md`).

**Write after checkout work**: funnel baselines and any monthly movement into `## Metrics` with their `as of` date; a completed or abandoned test into `experiments/<year>.md` with the decision; a checkout outage into `incidents/<year>.md` with duration, orders affected and how it was detected; and a recovery-flow design or a checkout configuration that finally worked into `artifacts/<kebab-name>.md` with its `## Boxes` line (`memory-template.md`).
