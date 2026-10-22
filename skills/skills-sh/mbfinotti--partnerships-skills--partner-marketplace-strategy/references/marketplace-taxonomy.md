# Marketplace Taxonomy and Depth-of-Participation Ladders

Five categories of third-party marketplace, each doing a different job. Misreading the job - expecting demand from a procurement rail, or procurement leverage from a discovery directory - is the root of most failed listings.

Every ordering below is a default, not a law: it shifts with context and with who executes it. Re-rank it against what the Interview already told you.

Effort here always means engineering weeks, deal-desk rework, contractual commitment, coordination and reversibility, never a fee. Take rates are subject matter, not the effort axis.

## Which category first

No single ordering spans all five. The Interview's B2B/B2C answer picks the list, and a blended rank across both would be false precision - no company chooses between a hyperscaler and Amazon.

**B2B software**

- efficiency: `hyperscaler cloud > integration directory > SaaS app store`
- value: `hyperscaler cloud > SaaS app store > integration directory`
- effort: `SaaS app store == hyperscaler cloud > integration directory`
- compliance cost: `SaaS app store > hyperscaler cloud > integration directory`

The effort tie is real, not a dodge: each rung costs about a quarter of coordinated work before a first dollar can transact, and neither compresses by adding an owner.

- Hyperscaler cloud: metering, entitlement, tax and payout setup.
- SaaS app store: billing integration and a platform review cycle.

The directory ranks second on an hour of work and a ceiling to match: run it in parallel as hygiene, never as the quarter's bet.

The order starves the SaaS app store: the same effort as the cloud rung, plus a permanent revenue share and an architecture the operator can reprice. Promote it above the cloud rung when the Interview says buyers live inside one platform's daily workflow and hold no committed cloud spend - and then delete the cloud listing from the memo rather than staging it.

**B2C / retail**

- efficiency: `dominant retail marketplace > regional champion`
- value: `dominant retail marketplace > regional champion`
- effort: `regional champion > dominant retail marketplace`
- compliance cost: `regional champion > dominant retail marketplace`

The order starves regional champions: tax registration, EPR obligations and localization land before the first order, each a standing job in a jurisdiction nobody on the team operates in. Promote one when the home market is proven and the target geography's incumbent is a different platform - a geography the dominant marketplace does not serve is reachable no other way.

## The five categories

- **Hyperscaler / cloud marketplaces** - a procurement and transaction rail for B2B software. The buying driver is committed-spend drawdown (a purchase retires budget the customer already promised to the cloud provider) plus co-sell access to the provider's field sellers. Take rates depend on how the product is delivered: 3% for SaaS listings but 20% for server images (AMI/container/ML) on AWS Marketplace, falling with deal size and on renewal, so resolve the deployment method before quoting a rate. Beyond that, the real cost is operational. Examples: AWS Marketplace, Microsoft commercial marketplace, Google Cloud Marketplace.
- **Integration directories** - discovery and credibility surfaces, usually free or near-free, rarely transactable. They support an integration story and search presence. They do not carry a revenue motion on their own.
- **SaaS app stores** - distribution attached to a platform that owns the buyer's workflow. Discovery genuinely exists here, but the platform charges for it: revenue shares in the 15-25% band are typical. The strategic question is whether one platform owns your ICP's daily workflow deeply enough to justify going all-in. Examples: Salesforce AppExchange, Shopify App Store, Atlassian Marketplace.
- **Retail / consumer marketplaces** - demand plus fulfilment for physical goods. The platform supplies traffic and (optionally) logistics, and takes a category-set referral fee plus fulfilment and effectively-mandatory ad spend. Blended cost-to-serve commonly reaches 30-45% of selling price on the dominant platforms. Examples: Amazon, Walmart Marketplace, eBay, Etsy, TikTok Shop.
- **Regional champions** - the dominant local marketplace in a geography. Examples: Allegro (Poland/CEE), Bol.com (Benelux), Otto and Zalando (Germany), Cdiscount and ManoMano (France), Mercado Libre (Latin America), Shopee/Lazada and Coupang (Asia). Gating steps are tax registration (VAT), compliance (EPR), and localization - not logistics.

## Depth-of-participation ladder - B2B cloud marketplaces

The one ladder where value and effort genuinely climb together, and the rungs are cumulative - so rank the destination you fund, not the sequence you walk.

- efficiency: `private offer > transactable > list-only > channel offer`
- value: `private offer > channel offer > transactable > list-only`
- effort: `channel offer > private offer == transactable > list-only`
- compliance cost: `channel offer > private offer > transactable > list-only`

Private offer and transactable tie on effort because each costs roughly a quarter before returning anything, in departments that cannot substitute for each other.

- Engineering builds metering, entitlement and payout.
- The deal desk rebuilds around negotiated terms and a written comp-neutrality policy.

Aim the business case at the private-offer rung and treat transactable as the toll: a case that stops at transactable has paid nearly the whole cost for the smaller half of the value.

Default rung: transactable, funded as a private-offer program. The condition that moves you up is first transactions closed, renewals first.

1. **List-only ("contact me")** - near-zero effort, near-zero revenue. Buys exactly one thing: proof that target buyers search there. Gate to climb: that evidence exists.
2. **Transactable public offer** - the listing can be bought. Requires metering/entitlement engineering (commonly cited at 4-8 weeks), legal document harmonization, tax and payout setup. Gate: those capabilities funded and owned.
3. **Private offer** - negotiated price and custom terms. It is the enterprise workhorse and where most cloud-marketplace revenue actually flows. Requires a deal desk rebuilt around private offers and comp neutrality in writing - political capital, not engineering. Gate: first transactions proven (renewals are the documented low-risk path) and field alignment started.
4. **Channel / multiparty private offer** - routes a reseller or SI into the transaction (CPPO on one major cloud; multiparty offers on others) for a small fee uplift, on top of a three-party contract and a standing co-sell operation. Gate: a real channel motion exists to route.

The order starves the channel rung. Promote it when a reseller or SI motion already exists and is asking to be routed, or when a target account will only buy through its incumbent reseller: there it is not an upgrade but the only path to that deal.

Delete every rung the user's effort ceiling rules out from the memo, and name which ones you deleted. A ruled-out rung parked at the bottom reappears later as scope.

## Depth-of-participation ladder - SaaS app stores

- efficiency: `transactable paid app > free listing > deep platform bet`
- value, effort and compliance cost all order the same way: `deep platform bet > transactable paid app > free listing`

1. **Free listing / basic integration** - directory presence tied to the integration: an hour of work, and a credibility surface, not a revenue one.
2. **Transactable / paid app** - platform billing, revenue share applies, and the platform's review becomes a dependency on every release.
3. **Deep platform bet** - build on the platform's preferred architecture, pursue featuring and co-marketing.

The order starves the deep bet: a quarter or more of engineering aimed at an architecture only one operator accepts, and the least reversible commitment in this file. Promote it when that platform owns the ICP's daily workflow _and_ the operator's fee schedule pays for the migration.

Operators price architectures differently to steer exactly this choice: on AWS Marketplace a SaaS listing takes 3% where a server image takes 20%. That gap is the decision this rung actually turns on.

## Depth-of-participation ladder - retail marketplaces (1P / 3P / hybrid)

- efficiency: `3P > 1P > hybrid`
- value: `hybrid > 3P > 1P`
- effort: `hybrid > 3P > 1P`
- compliance cost: `hybrid > 1P > 3P`

3P returns the most control and margin per unit of operational work. 1P buys simplicity by surrendering the one variable that decides a consumer channel - price - which is why it ranks below a heavier option.

- **3P (seller)** - you sell direct on the platform: keep retail price minus referral, fulfilment, and ad fees, and own pricing, inventory, and customer service. It is the default for margin and pricing control. Documented platform pressure pushes smaller vendors here.
- **1P (vendor / wholesale)** - the platform buys wholesale and controls price and fulfilment. Simpler operations, lost pricing control, margin set by wholesale terms and allowances (typically 10-15% of payments in deductions). Reserve for specific high-velocity products.
- **Hybrid** - both at once on the same product line. Requires a firewall between 1P and 3P teams (pricing not shared) and a written pricing policy before entry.

The order starves hybrid: it doubles the operating surface and carries this file's heaviest compliance load - MAP enforcement plus a pricing firewall someone must audit. Promote it only when a specific high-velocity SKU has already proven its 1P economics and the firewall and pricing policy exist in writing.

International sequencing for consumer brands has an established default: validate the home market first, expand to adjacent markets of the same platform, then regional champions - gated on tax/compliance/localization readiness each time.

## Reading the ladders as strategy

- Depth follows evidence, never ambition: each rung's gate is proof from the rung below.
- The most defensible pattern in both worlds is concentration - prove one platform at real depth before adding a second, rather than shallow presence everywhere.
- A platform that owns the buyer's procurement (committed spend) or workflow (daily-use app platform) justifies depth. One that owns neither justifies at most a list-only or 3P toe-hold with a delist trigger attached.
