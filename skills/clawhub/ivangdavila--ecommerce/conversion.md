# Conversion — Product Pages, Trust and Tests That Mean Something

Conversion work fails in two predictable ways: **testing things too small to detect**, and **optimizing conversion rate while destroying margin per session**. The metric is revenue per session — better, contribution margin per session — and the discipline is sizing the test before running it.

**Before proposing a test**, read `experiments/<year>.md` if `## Boxes` names it. Roughly half of "we should try X" has already been tried, and the inconclusive ones are the ones most likely to be proposed again.

## Where the Money Actually Is

Size the opportunity before choosing the work: `monthly sessions × step drop-off × CM per order`. A 5% improvement on a step that 40,000 sessions reach beats a 30% improvement on one that 900 reach.

| Surface | Typical leverage | First look |
|---|---|---|
| Checkout steps | Highest per unit of work — the traffic is already committed | Step drop-offs (`checkout.md`) |
| Product page | High volume, many independent levers | Above-the-fold completeness |
| Collection / category page | Where undecided traffic goes to leave | Filters, sort, and the number of products above the fold |
| Site search | Searchers convert several times better than browsers; a zero-result search is a lost order | Zero-result and no-click queries (`storefront.md`) |
| Cart | Small traffic, high intent | Shipping cost visibility, cross-sell relevance |
| Speed | Affects every surface at once | LCP and INP on mobile (`storefront.md`) |

## The Product Page

Above the fold on mobile, in this order: image, title, price with tax treatment, variant selector, availability, delivery estimate, add-to-cart. Everything else is below.

| Element | Why it moves orders |
|---|---|
| Delivery date, not "ships in 2-3 days" | Removes the calculation the customer would otherwise abandon over |
| Real stock level when genuinely low | Honest scarcity converts; invented scarcity is punished by regulators and by returning customers (`tax.md`) |
| Reviews with photos, and the negative ones visible | An all-5-star page reads as fake; visible criticism raises trust in the rest |
| Size/fit or compatibility data, measured | The top return reason for most categories, fixed here rather than in support (`returns.md`) |
| Return policy summary in one line | Reduces the perceived risk of the decision at the moment it is made |
| Variant selector showing unavailable combinations as unavailable | Hiding them makes customers think the page is broken |
| Total cost clarity (tax, shipping estimate) | Surprise at checkout is the most-cited abandonment reason (`checkout.md`) |

Cross-sells belong on the cart page (highest conversion), post-purchase (no payment re-entry), and the product page (lowest intent) — in that order. A post-purchase offer cannot lose the sale you already have, which is why it is the safest place to be aggressive.

## Test Sizing Before Test Running

```
n per variation ≈ 16 × p × (1 − p) ÷ MDE²      (MDE absolute; ~80% power, 95% two-sided)
```

Baseline 3%, chasing a 10% relative lift → MDE = 0.003 → n = 16 × 0.03 × 0.97 ÷ 0.000009 ≈ **51,700 sessions per variation**. At 40,000 sessions/month split two ways, that test takes about 2.6 months — which is the real finding, and it is available before running anything.

- Below ~10,000 sessions/month, most A/B tests are undetectable. Do the removals that need no test (`checkout.md`), run before/after with a long baseline, or test on the highest-traffic surface only, accepting that the result is directional.
- **Run at least one full week** (day-of-week effects are large in retail) and stop at the pre-declared sample. Peeking and stopping at significance inflates false positives; declare the sample and the stop date in `experiments/<year>.md` before starting.
- Minimum ~100 conversions per variation before reading anything, whatever the calculator says.
- One change per test unless you are testing a whole redesign as a package — in which case you learn "the package won" and nothing about why.
- **Primary metric = revenue per session or CM per session.** Conversion rate as a primary metric approves every discount test ever run.

## Reading a Result

| Situation | Read |
|---|---|
| Winner, sample reached, one week+ | Ship it, write the effect size into `experiments/<year>.md`, and re-measure a month later — most lifts shrink |
| Winner, sample not reached | Not a winner — the row in `experiments/<year>.md` says inconclusive, with the achieved sample |
| Loser | The most valuable result, if the hypothesis was specific — the `experiments/<year>.md` row says why you believed it |
| No difference | Also a result: the surface does not matter as much as assumed; stop working on it |
| Segment-only win (mobile only, new visitors only) | Legitimate if the segment was pre-declared; a segment found after the fact is a hypothesis, not a finding |
| Conversion up, revenue per session down | A discount in disguise. Do not ship |

Novelty effects fade in weeks and seasonality moves everything: never compare a test period against last month, only against the concurrent control.

## Personalization and Recommendations

- Recommendation quality beats recommendation placement. "Frequently bought together" from real co-purchase data beats "you may also like" from category adjacency by a wide margin.
- Returning-visitor personalization (recently viewed, previously bought) is cheap and safe. Behavioural segment personalization needs traffic most stores do not have — the arithmetic in `Test Sizing` applies per segment.
- Never personalize price without disclosure. Differential pricing detected by a customer is a trust event, and in several markets a legal one (`tax.md`).

## Ethical Urgency, and Why It Is Also the Profitable Kind

- Real stock counts, real deadlines, real demand figures. Countdown timers that reset, "last one" on a product with 200 in stock, and fake "12 people are viewing" are prohibited practices in EU consumer law and are increasingly enforced.
- Fake or curated-only reviews carry the same exposure; incentivized reviews must be disclosed.
- "Was" prices must reflect a real prior price applied for a real period — the EU rule ties a price-reduction announcement to the lowest price applied in a prior window (`tax.md`).
- The commercial argument is identical to the legal one: manufactured urgency raises first-order conversion and lowers repeat rate, and repeat rate is where the margin lives (`retention.md`).

**Write after conversion work**: every test into `experiments/<year>.md` with hypothesis, primary metric, **pre-declared sample**, achieved sample, result and decision — including the abandoned and inconclusive ones; the funnel and CR/RPS baselines into `## Metrics` with their `as of` date; and a page template, a research finding or a design decision that keeps being re-litigated into `artifacts/<kebab-name>.md` with its `## Boxes` line (`memory-template.md`).
