# Pricing, Margin and Promotions

Every price decision in a store is the same decision: **what does this leave after all the costs that scale with the order?** Revenue is the number that lies; contribution margin is the number that decides.

**Before any price change, promo or threshold**, read `## Unit Economics` (current CM per SKU with its `as of` date) and `promotions/<year>.md` (what the last promo actually returned) in `~/Clawic/data/ecommerce/memory.md`. A CM row older than the last COGS refresh in `## Due` is recomputed before it is quoted.

## Contribution Margin, Fully Loaded

```
CM = price − COGS − payment fee − outbound freight − pick/pack
     − channel commission − (return rate × return handling cost)
CM% = CM ÷ price
Max safe discount % = CM% (at that point CM is zero)
```

Worked, one SKU: price 50, COGS 18, payment fee 1.00 (1.5% + 0.25), freight 4.50, pick/pack 1.50, commission 0, returns 8% × 6.00 = 0.48.
**CM = 24.52, CM% = 49%.** A 20% discount (10.00) leaves 14.52 (CM% 36% of the new price). A 40% discount leaves 4.52. A 50% discount sells below cost once one order in twelve comes back.

- Fixed costs (platform, apps, salaries, ads not tied to the order) sit **below** contribution margin. Mixing them in produces a "cost" per unit that changes with volume and makes every marginal decision wrong.
- **Discount on price, margin on the discounted price.** The most common arithmetic error in retail is quoting the old CM% next to the new price.
- Recompute CM per SKU quarterly and after any freight, fee, or supplier change. Set that as a `## Due` row (`memory-template.md`).

## Setting a Price

| Method | Use it when | Failure mode |
|---|---|---|
| Cost-plus (`price = COGS ÷ (1 − target CM%)`) | Commodity, thin differentiation, wholesale floors | Prices your product by your supplier's efficiency, not by what customers will pay |
| Competitive anchoring | Comparable products are one search away | A race to the bottom you did not start and cannot win against a bigger buyer |
| Value-based | Differentiated product, brand or bundle | Requires evidence — willingness-to-pay research, not opinion (`pricing` skill) |
| Charm and threshold pricing (x.99, x.95) | Mass-market consumer goods | Signals discount positioning; premium brands round |

Cost-plus example: COGS 18, target CM% 45% → variable costs beyond COGS ≈ 7.00 for this SKU, so `price = (18 + 7.00) ÷ (1 − 0.45) = 45.45`. Cost-plus that forgets freight, fees and returns is how a store sets a price that looks 60% margin and delivers 30%.

- Price by **category CM target**, not one blanket markup: heavy items need a higher markup for the same CM, and high-return categories need more still.
- **Price changes are cheap to test and expensive to guess.** A/B testing price is legally and technically messy; test with time-based cohorts on a subset of SKUs and read CM per session, not conversion (`conversion.md`).
- Displayed prices in the EU and UK are tax-inclusive to consumers; a "price rise" that is a VAT change must be handled deliberately (`tax.md`).

## Free Shipping and Thresholds

Free shipping is a discount equal to the freight cost, applied to every order that qualifies.

```
Threshold = AOV × 1.25            (band: 1.2-1.3)
Gate:  CM at the threshold basket − freight  >  CM at AOV
```

At AOV 44 the threshold is 55. Check the gate: if a 55 basket carries CM 27 and freight is 4.50, the store nets 22.50 against 21.50 at a 44 basket paying its own freight — the threshold works. If the gate fails, either the threshold is too low or freight is too high for the tactic, and a flat contribution to shipping beats free shipping.

- Show the progress bar (`Add 11 more for free shipping`) — the tactic works through the bar, not through the threshold itself.
- Never let free shipping stack with a percentage code unless the stacked CM is still positive (`Stacking Rules`).
- Free shipping over a threshold beats free shipping always for AOV, and loses to it for conversion. Which one wins is a CM-per-session test, not a preference.

## Promotions

| Mechanic | What it protects | What it costs |
|---|---|---|
| Threshold (`spend X get Y`) | Margin on small baskets | Nothing on orders that would have crossed anyway |
| Bundle / multi-buy | Perceived value without a headline discount | Cannibalizes single-unit sales — count the units, not the orders |
| Gift with purchase | Price integrity | The gift's COGS on every qualifying order |
| Percentage sitewide | Simplicity | The deepest cut, applied to your best sellers, which needed no discount |
| Category or overstock clearance | Cash from dead stock (`inventory.md`) | Trains customers to wait for the category |
| Free shipping day | AOV-neutral traffic spike | Full freight on every order, including the 20 ones |
| Loyalty-only or list-only offer | Retention, and no public price signal | Slower reach |

- **Judge every promo on realised CM, not revenue** — and against a baseline period, since some of the sales would have happened anyway. Incrementality is the only honest measure: revenue during the promo minus the baseline, at promo margin.
- Cap depth at `max_discount_pct` unless the goal is inventory exit and the alternative is a write-off.
- Sitewide discounting more than twice a year teaches customers the real price is the sale price; after that the full-price weeks fund nothing.
- Codes need expiry dates and volume caps, and should never be memorable words unless they are meant to spread (`fraud.md`).

## Stacking Rules

Write them once, enforce them server-side:

1. One code per order, and codes never combine with automatic promos unless explicitly allowed.
2. Loyalty points, store credit and gift cards are payment, not discount — they apply after the discount and do not compound with it.
3. A **CM floor per cart**: no order may be created below a stated CM (a small positive number, not zero, so freight variance does not turn it negative).
4. Exclusions declared at the product level (`catalog.md`): new arrivals, MAP-restricted brands, already-marked-down items.
5. Every rejection tells the customer which rule applied. Silent failures read as a broken checkout.

## Price Increases

- Increase on **new customers first, existing later**, and give notice to subscribers before their renewal (`subscriptions.md`).
- A 5% price rise on a 45% CM SKU raises CM by ~11% and rarely moves volume proportionally; when in doubt about a small rise, the honest expected value favours taking it.
- Communicate a rise once, factually, with the reason. Silence produces churn from the customers who notice, which are the ones who buy most often.
- Never raise a price and run a promo in the same month: the promo hides the signal you needed to read.

## Cross-Channel Price Consistency

- Marketplace prices carry commission (`marketplaces.md`); matching the store price there means selling at a lower CM, and pricing higher there means competing against your own listing.
- Decide the policy explicitly: same price everywhere and accept the CM gap, or channel-specific prices and accept the customer noticing. Both are defensible; drifting between them is not.
- MAP or resale-price constraints from suppliers are contractual — the floor goes per SKU into `## Unit Economics` of `memory.md` (as a `MAP floor` column, with currency), and the contract wording into `artifacts/policy-pricing.md`. Never in someone's memory.

**Write after pricing work**: recomputed CM per SKU or category into `## Unit Economics` with its `as of` date; every promotion into `promotions/<year>.md` with mechanic, scope, redemptions, revenue and **realised CM% against the baseline**; a price-strategy or stacking policy the store settles on into `artifacts/policy-pricing.md`; and the quarterly COGS and freight refresh into `## Due` — with its `## Boxes` line in the same turn (`memory-template.md`).
