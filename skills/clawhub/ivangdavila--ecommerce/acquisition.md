# Acquisition — Traffic, Spend and What a Customer May Cost

Two gates decide every acquisition question, and both come from margin, not from revenue: **break-even ROAS** and **payback**. Everything else — creative, channels, feeds, SEO — is how you move a number that those two gates judge.

**Before recommending spend or a new channel**, read `## Unit Economics` (CM%) and `## Metrics` (CAC, MER, repeat rate) in `~/Clawic/data/ecommerce/memory.md`. A channel recommendation made without CM% is a guess about the only variable that decides it.

## The Two Gates

```
Break-even ROAS = 1 ÷ CM%
Allowed CAC (cash-safe)  = first-order CM
Allowed CAC (LTV-based)  = contribution LTV ÷ target_ltv_cac
Payback month = the month a cohort's cumulative CM crosses its CAC
```

Worked at CM% 44 and AOV 47: break-even ROAS = 2.27, first-order CM = 20.7, contribution LTV 89 → LTV-based allowed CAC ≈ 30 at a 3:1 target. So a campaign at 2.0 ROAS loses money on the first order and only survives if the second order arrives before the cash does not. A store without financing runs at the cash-safe number and grows slower on purpose.

- Report **MER** (total revenue ÷ total ad spend) alongside platform ROAS. Every platform claims the same conversions; the claims sum to more than the store's revenue, and MER is the only number the bank agrees with.
- New-customer CAC is the number that matters, not blended CAC: retargeting your existing buyers inflates ROAS and buys nothing (`retention.md`).
- Set a **maximum CAC per channel** in advance and pause on breach. Ad platforms optimize toward whatever they are given; without a ceiling they find the customers who cost most.

## Channel Selection by Store Stage

| Stage | Where the next order comes from | What is a distraction |
|---|---|---|
| No product-market fit | One channel, small budget, learning what converts | Everything else, especially agency retainers |
| First traction (< ~500 orders/month) | The channel that already worked, plus owned email/SMS | Multi-channel expansion |
| Scaling | Paid social and paid search together, plus feed-driven shopping | Attribution debates that no volume can resolve |
| Mature | Incrementality testing, brand, retention as a growth channel | Chasing new platforms with unproven creative |

Organic and owned channels have no CAC but do have cost and lead time: SEO pays back in months, email pays back immediately but only to a list you already built. Neither replaces paid at the start; both reduce paid dependency later.

## Product Feeds

Shopping feeds are usually the highest-intent paid traffic a store can buy, and their performance is mostly a data problem.

- Required attributes disapprove items silently: `gtin`, `brand`, `condition`, `availability`, `price` matching the landing page exactly including currency and tax treatment (`catalog.md`).
- **Feed titles are optimized separately from page titles** — the first 60-70 characters carry brand + product + defining attribute, matching how people search, not how the brand writes.
- Availability and price sync at least as often as stock changes matter; a stale feed during a promo disapproves exactly the items being promoted (`inventory.md`).
- Exclude what should not be advertised: out-of-stock, negative-margin after channel fees, and regulated items. Segment the remainder by margin so bidding can differ where CM differs.
- One image standard for feeds: plain background, product filling the frame, no overlaid text — overlays are a common disapproval cause.

## Paid Media Discipline

- **Creative is the targeting.** In broad-audience auction systems, the ad decides who sees it; expect the creative volume budget to exceed the audience-configuration effort by an order of magnitude.
- Test creative in a structure with enough conversions to learn: campaigns fragmented into a dozen ad sets each get too few conversions to exit the learning phase and all perform badly for structural reasons.
- Landing-page match matters more than bid tuning: an ad promising a category and landing on the homepage wastes the click it just paid for.
- Budget pacing during peak is its own discipline — CPMs rise sharply and the same ROAS target buys much less (`peak.md`).
- Measure holdouts or geo-splits at least quarterly. Platform-reported conversions are a modelling output, not a measurement (`analytics.md`).

## SEO for a Store

Three page types carry organic revenue, and they need different work:

| Page type | Wins with | Common failure |
|---|---|---|
| Category / collection | The commercial keyword, unique intro copy, stable URL, curated internal links | Thin pages generated per filter combination, competing with each other |
| Product | Unique description, structured data (price, availability, reviews), real reviews, images with alt text | Manufacturer copy duplicated across every reseller |
| Informational / guide | The question that precedes the purchase, linked to the relevant category | Blog posts unlinked to anything buyable |

- **Faceted navigation is the biggest technical risk**: filter URLs multiply into thousands of near-duplicate pages that consume crawl budget. Decide which facets are indexable (usually one or two commercially valuable ones), canonicalize the rest, and write that rule into `artifacts/<kebab-name>.md` with its `## Boxes` line — crawl-budget and rendering depth in `storefront.md`.
- Structured data (Product, Offer, AggregateRating, BreadcrumbList) must match what is on the page. Marking up a price or a review count that the page does not show is a manual-action risk.
- Out-of-stock and discontinued products: keep the URL and the page, show alternatives, and only redirect when the product is genuinely replaced by another (`catalog.md`).
- Site speed and Core Web Vitals affect both rankings and conversion; on mobile the same fix pays twice (`storefront.md`).
- Deep methodology: `seo`.

## Attribution Without Illusions

- Every platform over-claims. The reconciliation is: platform-reported conversions for diagnosis and pacing; **MER and cohort payback for decisions**.
- Post-consent tracking loss is structural in Europe — a meaningful share of conversions are modelled rather than observed. Server-side tagging and the platform's conversion API recover some of it; neither restores certainty (`analytics.md`).
- Ask new customers where they heard of you at checkout, in one optional field. The self-reported data is noisy and biased, and it still catches channels that no pixel attributes.
- **The only clean measurement is an experiment**: turn a channel off in a region, or hold out a segment, and read total revenue. Everything else is a model with a vendor's incentive attached.

**Write after acquisition work**: CAC, MER and new-customer counts per month into `## Metrics` with their `as of` date; a new channel's fee, commission or platform cost into `## Channels`; the agency or freelancer into the shared `contacts.md`; an incrementality test or geo holdout into `experiments/<year>.md` with its pre-declared design; and a feed mapping, channel decision, or the store's max-CAC policy into `artifacts/<kebab-name>.md` with its `## Boxes` line (`memory-template.md`).
