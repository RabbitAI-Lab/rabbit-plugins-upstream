# Peak Season — The Weeks That Pay for the Year

Peak is not a bigger normal week. Traffic, CPMs, carrier load, support volume and error consequences all move at once, and the store that survives it decided most things in advance. **Planning starts a full quarter out**, because stock lead times and carrier negotiations do not compress.

**Before planning**, read `incidents/<year>.md` and last year's peak retro if `## Boxes` names one, plus `## Metrics` for last year's same weeks. Last year's incidents are this year's checklist — that is the entire reason those boxes exist.

## The Countdown

| When | Work |
|---|---|
| T-12 weeks | Forecast units per SKU; place purchase orders with the real lead time including customs (`inventory.md`) |
| T-10 weeks | Negotiate carrier capacity and rates; confirm cut-off dates and any peak surcharges (`fulfillment.md`) |
| T-8 weeks | Decide the promo calendar and its margin floors; brief creative (`pricing.md`) |
| T-6 weeks | Load-test the storefront and checkout at 3-5× last year's peak hour; fix what breaks (`storefront.md`) |
| T-4 weeks | Grow and warm the email/SMS list; peak is sold to people who already know you (`retention.md`) |
| T-3 weeks | Staff support and packing; write the macros for the three questions peak generates (`support.md`) |
| T-2 weeks | **Code freeze begins**; publish shipping cut-off dates on the site |
| T-1 week | Dry run: place real orders across every channel and payment method; verify feeds and stock sync |
| Peak | Monitor, do not build. Daily stock and margin check |
| T+1 week | Returns wave planning and staffing (`returns.md`) |
| T+3 weeks | Retro, written down |

## Forecasting Units

```
Peak units per SKU = last year's peak units × (this year's baseline ÷ last year's baseline)
                     × planned promo uplift
Cover = peak units + safety stock, with no reorder possible inside the window
```

- The growth multiplier comes from **baseline** comparison (a normal recent month against the same month last year), not from ambition. Ambition-based forecasts produce either dead stock in January or stockouts in the one week that pays.
- **There is no reorder inside peak**: the lead time is longer than the window. Whatever is not in the warehouse is not sold, so cover is a decision made at T-12.
- Overstocking a hero SKU costs carrying cost and a January discount; understocking costs the full margin plus the customer who buys elsewhere. For A items the asymmetry favours cover; for tail items it does not.
- New products launched into peak carry forecast risk with no history. Cap the buy and treat it as a test.

## Freeze Window

- **No deploys, app installs, theme edits, price-logic changes or platform migrations** from T-2 weeks until the end of the peak window. The one week that pays for the quarter is not the week to discover a checkout regression.
- The exception rule is written before the freeze: what qualifies as an emergency (checkout broken, payment method down, legal), who approves it, and that every exception is tested on staging first.
- Content changes (banners, copy, collection curation) are exempt if they route through a mechanism that cannot break checkout — decide which mechanism during planning, not during the incident.
- Freeze also means **no marketplace listing restructures**: re-indexing takes time the calendar does not have (`marketplaces.md`).

## Load and Reliability

- Load-test at 3-5× last year's peak *hour*, not peak day: the spike is what fails.
- Third-party dependencies fail before your store does. Know the fallback for each: shipping-rate API → cached flat rates; reviews or personalization widget → degrade to static; a payment method down → the alternatives already enabled (`checkout.md`, `payments.md`).
- Cache aggressively but never cache anything keyed to a session, and confirm price and stock invalidation still works under load (`storefront.md`).
- Alerting narrows to the unambiguous: zero orders in an hour that normally has orders, checkout error rate, payment failure rate, stock at zero on an A item, feed disapprovals (`analytics.md`).
- Somebody is on call with a phone that is not on silent, and the runbook for "orders stopped" is in `artifacts/` where they can find it, not in a chat thread (`orders.md`).

## Promo and Budget Discipline

- Set the margin floor per promo before the calendar is published, and hold it — peak is when the deepest discounts get approved by momentum (`pricing.md`).
- CPMs rise sharply through the peak window; the same ROAS target buys much less traffic. Decide in advance whether you are pacing to a ROAS floor or spending to a revenue target, because you cannot do both (`acquisition.md`).
- Email and SMS revenue peak here and so do unsubscribes. Plan the send calendar with a frequency cap and suppression for anyone who just bought (`retention.md`).
- Gift purchases change the mix: higher first-time-buyer share, higher gift-message and delivery-date sensitivity, and a return wave that lands in January under an extended window you should publish deliberately.

## Operations Through the Window

- Publish shipping cut-off dates per destination and per service prominently, and honour them. A missed published cut-off is the complaint that reaches social media.
- Pack capacity is the binding constraint for most stores: measure orders packed per hour before peak and staff to the forecast peak day, not the average.
- Carriers cap volume in peak and can refuse collections; the second carrier you kept at 10-20% of volume year-round is the reason you still ship (`fulfillment.md`).
- Support volume rises faster than orders because delivery anxiety rises. Pre-write the three macros (where is it, cut-off, gift returns) and answer publicly on the site before customers ask (`support.md`).
- Daily during peak: stock on A items, margin realised versus plan, error rates, carrier acceptance, and the one number that decides whether to keep spending.

## The Retro

Within three weeks, written into `artifacts/`, because in eleven months nobody remembers:

- What sold out, what did not sell, and what the forecast miss was in units and in margin
- Every incident with its detection time and its cost (`incidents/<year>.md`)
- Realised margin by promo against plan (`promotions/<year>.md`)
- Carrier performance against the published cut-offs
- Support volume, top reasons, and which one is preventable
- The three things to change next year, with a T-week for each

**Write after peak work**: the plan and its dates into `## Due` (including the T-12 kickoff for next year); the forecast and its outcome into `promotions/<year>.md` and `## Metrics`; every incident into `incidents/<year>.md` with detection time and revenue impact; and the retro, the freeze-window policy and the peak runbook into `artifacts/<kebab-name>.md` with their `## Boxes` lines (`memory-template.md`). If peak is run as a project, its summary also goes to `~/Clawic/data/projects/<project>.md`.
