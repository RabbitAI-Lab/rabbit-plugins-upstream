# Marketplace Economics: Take Rates, Fee Structures, and the Real Cost

Fees marked **(published)** are from the marketplace operator's own published schedule. They are the operator's rate card and can change: re-verify before acting.

Fees marked **(unverified)** are not confirmed against operator sources. Never state an unverified fee as fact.

## B2B cloud marketplaces

- **AWS Marketplace** (published; fees on pre-tax total contract value): SaaS public offers 3%; server (AMI/container/ML) public offers 20%; private offers 3% under $1M, 2% from $1M to under $10M, 1.5% at $10M+; all renewals 1.5%; channel partner private offers add +0.5%; professional services 0.5% (private offers only); South Korea buyers +1% (from 2025-04-01).
- **Microsoft commercial marketplace** (published): 3% standard store service fee on transactable offers; BYOL/non-transactable listings 0% (but then discovery-only, not a transaction channel); qualifying private-offer renewals get a 50% fee discount. Caution: Microsoft's docs state prepaid Azure credits cannot pay publisher license fees - do not conflate that with MACC consumption-commitment eligibility for marketplace purchases, a distinct program with its own rules; verify before asserting drawdown behavior.
- **Google Cloud Marketplace** (unverified): partner docs publish no rate card - the fee is deliberately opaque, making it a negotiation input, not a known constant. Reported rates describe ~3% standard with reductions for large private offers and renewals.

Strategic reads: the B2B pattern is a fee that _falls_ with contract size and on renewal, structurally rewarding large private offers over public self-serve. The 20%-vs-3% gap by deployment method (server image vs SaaS) is the largest single fee-structure decision on the biggest cloud marketplace.

Fees at ~3% are no longer the deciding variable: the operators price marketplace revenue as committed-spend stickiness, not as a toll. The real cost is operational.

## SaaS app stores

- **Shopify App Store** (published): emerging developers (under $20M lifetime App Store earnings and under $100M company revenue) keep 100% of the first $1M per year, 85% above; high-volume developers keep 85% of everything; 2.9% processing fee on all app billing; themes 85%.
- **Atlassian Marketplace** (published): operator's share by app architecture, with a published schedule of future increases - from 2026-04-01: Forge 16%, Connect 20%, Data Center 25%; from 2026-10-01: Forge 17%, Connect 25%, Data Center 25%. Forge incentive: 100% of gross revenue to the partner up to $1M lifetime Forge revenue (from 2026-01-01). Payout at $500 accrued, 30-day refund window.
- **Salesforce AppExchange** (unverified): reported 15% of net revenue for standard paid apps, 25% for OEM, plus a per-app security-review fee and annual listing fee.

Strategic reads - the two most transferable lessons in this file:

- **The take rate is a policy lever, not a constant.** An operator sets different rates per technical architecture and publishes future increases to steer ISV build decisions. Any business case built on today's rate must be stress-tested against the operator's announced and plausible future rates - and against the build choice the rate is designed to push.
- **Introductory 0% bands are acquisition subsidies, not the price.** A discount that expires at a revenue threshold (a first-$1M band) means the true cost arrives exactly when the listing starts mattering. Model the post-threshold rate as the real rate.

## Retail marketplaces

- **Amazon US** (Amazon's own seller pricing page): Individual plan $0.99/item; Professional $39.99/month; referral fees by category roughly 5-45% of sale price ($0.30 minimum in most categories) - e.g. electronics 8%, home & kitchen 15%, jewelry 20% up to $250 then 5%, device accessories 45%; media items +$1.80 closing fee. Fulfilment, storage, aging-inventory surcharges, and advertising come on top; blended cost-to-serve commonly reaches 30-45% of selling price.
- **eBay** (eBay's own seller fees page): most categories 13.6% of the sale total up to $7,500 then 2.35% on the portion above, plus a $0.30 (orders $10 or under) or $0.40 (orders over $10) per-order fee. The category spread runs from 0.5% (the portion of a Business & Industrial sale, e.g. heavy equipment, over $15,000) to 15.3% (Books, Movies & TV, Music, up to $7,500) - e.g. NFT categories 5% flat, Business & Industrial (heavy equipment and similar) 3% up to $15,000 then 0.5% above, Guitars & Basses 6.7%, Athletic Shoes priced $150+ 8% with no per-order fee, Coins & Paper Money and select Collectibles (comic books, non-sport and sports trading cards, collectible card games) 13.25%, Jewelry & Watches and Women's Bags & Handbags 15% up to a $2,000-5,000 threshold then 9% above. The 13.25% vs. 13.6% figure once flagged as aggregator-level disagreement is not decimal noise: both are real, distinct category rates on eBay's own fee page.
- **Walmart, TikTok Shop, Etsy** (aggregator-checked, not primary-page-verified): reported ranges are Walmart 6-15% (some categories up to 20%) referral with no subscription or listing fee; TikTok Shop 6% flat referral, with a 3% introductory rate for a new seller's first 30 days; Etsy $0.20 per listing plus 6.5% transaction fee plus 3%+$0.25 payment processing, roughly 10-12% all-in before Offsite Ads. Verify on the operator's own fee page before using an exact figure in a business case.

Strategic read: on retail marketplaces the take rate is set by _product category_, not by the seller's negotiating position or contract size - the exact opposite of the B2B cloud pattern. A B2B team can negotiate its effective rate down by deal structure. A consumer brand can only change its rate by changing what it sells or where.

## Committed-spend drawdown - the B2B buying driver

Eligible cloud-marketplace purchases retire a customer's pre-committed cloud spend (the three hyperscalers each run such commitment programs). The "use it or lose it" dynamic makes committed buyers highly motivated, turns a new budget request into an allocation of already-promised money, and is why procurement presence outweighs fee levels in prioritization.

Aggregate committed spend across the three providers was estimated near $470B as of late 2025 (analyst estimate - Omdia; independent, but an estimate). Drawdown eligibility rules and caps differ per provider and change: verify per program before promising it to a buyer.

## Total cost-to-serve - the number the take rate hides

Model the full stack, not the headline fee:

- **B2B**: listing/metering engineering (commonly cited 4-8 weeks), legal harmonization (EULA, DPA, support SLA), tax and payout configuration, a private-offer deal desk, co-sell operations, optionally a cloud GTM tooling subscription, plus a fractional-to-dedicated owner.
- **B2C**: referral fee + fulfilment + storage and aging surcharges + returns reserve + effectively-mandatory retail-media budget + pricing/MAP enforcement + (international) tax registration and compliance per market.

A gross-to-net waterfall per marketplace - list price minus every named deduction down to contribution - is the honest comparison format. Comparing headline take rates alone systematically flatters the platforms with the heaviest hidden stack.
