# Tax, Invoicing and Consumer Law

Three obligations that share one property: **they are triggered by thresholds and dates, not by intent**, and missing them is retroactive. Rates, thresholds and wording change — the structures below are stable, the figures must be verified against the current official source for the market before money moves.

**Before answering anything fiscal or legal**, read `## Store` (home market, registrations, markets shipped to) in `~/Clawic/data/ecommerce/memory.md`. While `home_market` is unset, name the jurisdiction you are assuming before answering (SKILL.md Rule 8). What this file does is name which question to take to an accountant in the store's own country, and when.

## The Registration Triggers

| Trigger | Consequence |
|---|---|
| Trading at all in most of the EU | VAT registration in the home country from the first sale for a business, with local small-business exemptions where they exist |
| EU cross-border B2C sales above the EU-wide threshold (currently €10,000/year, all countries combined) | Charge destination-country VAT; register for **OSS** to file one return instead of one per country |
| Importing goods to EU consumers, consignments at or below €150 | **IOSS** lets you collect import VAT at checkout instead of the courier billing the customer at the door |
| Consignments above the IOSS ceiling | Standard import procedure — duty plus import VAT, best handled DDP (`fulfillment.md`) |
| Digital products or services to EU consumers | Place of supply is the customer's country from the first sale; the physical-goods threshold logic does not apply the same way (`catalog.md`) |
| US: crossing a state's economic-nexus threshold (commonly $100k in sales or 200 transactions, varying and changing by state) | Register, collect and file in that state |
| US: selling via a marketplace | The marketplace usually collects and remits as facilitator — your registration and filing obligations do not automatically disappear (`marketplaces.md`) |
| Holding stock in another country (3PL, marketplace warehouse) | Usually creates a registration obligation there, regardless of sales volume — the most-missed trigger of all |

Two rules that prevent most damage: **check thresholds monthly against actual sales, not at year end** (`## Due`), and **register before storing inventory in a new country**, not after the first sale ships from it.

## Getting the Tax Right at Checkout

- **Tax-inclusive display for consumers in the EU and UK**, on the product page as well as the cart. US consumer prices are shown pre-tax with tax calculated at the address step (`checkout.md`).
- Tax is calculated on the **destination**, and depends on product class: reduced and zero rates exist for categories such as books, food and children's clothing in many markets, and a product without a tax class charges the standard rate — refundable to the customer, never to you (`catalog.md`).
- **B2B cross-border in the EU**: a valid, verified VAT number allows zero-rating under the reverse charge. Validate it against the official service at order time and store the validation result with the order — an unvalidated number leaves you owing the VAT you did not charge (`b2b.md`).
- Shipping is usually taxed at the rate of the goods it carries; a mixed basket needs apportionment, which is the sort of thing a tax engine exists to do.
- Refunds reverse the tax. Partial refunds reverse it proportionally, and the EU withdrawal refund includes the standard outbound shipping charged (`returns.md`).

## Invoices and Records

- Where invoices are mandatory, they are sequential, immutable and complete: seller identity and tax number, buyer details, invoice number and date, description, net, tax rate and amount per rate, and total. Corrections are **credit notes**, never edits (`orders.md`).
- Several markets are moving to structured e-invoicing and real-time reporting for at least B2B. Treat it as a platform requirement to check before choosing or migrating (`platforms.md`).
- Retention periods for orders, invoices and tax records run to several years in most markets and **survive replatforming** — export and keep the archive, do not assume the old platform will be there.
- Marketplace and processor reports are inputs to the return, not the return. Reconcile per channel; facilitator-collected tax that also gets self-declared is double payment, and nobody refunds it unprompted (`analytics.md`).

## Consumer Law That Changes the Store

| Obligation | Where it shows up |
|---|---|
| Right of withdrawal, 14 days in the EU/UK for distance sales | The returns policy and the pre-purchase disclosure (`returns.md`) |
| Legal guarantee of conformity, 2 years in the EU | Faults are a remedy obligation, not a return policy |
| Pre-contract information | Total price including tax, shipping cost, delivery time, withdrawal rights and identity of the trader, all before the order button |
| The order button must state that it creates a payment obligation | Wording such as "order with obligation to pay" |
| Price-reduction announcements must reference the lowest price applied in a prior period | Sale badges, "was" prices, countdowns (`conversion.md`) |
| Prohibited manipulative practices: fake urgency, fake scarcity, fake reviews, hidden costs | Product page, cart, review widgets |
| Review transparency: how reviews are collected and verified must be stated | Review widget disclosure (`retention.md`) |
| Cancellation of a subscription must be as easy as signup | The subscription flow (`subscriptions.md`) |
| Accessibility obligations for consumer-facing digital services in a growing number of markets | Storefront and checkout (`storefront.md`) |

## Privacy

- Personal data is processed under a lawful basis: contract performance for order data, consent for marketing and non-essential tags. They are different bases with different consequences — a customer who bought does not thereby consent to marketing everywhere.
- **Consent before non-essential tags fire**, with a reject option as easy as accept (`analytics.md`).
- Data-subject requests (access, deletion) have statutory deadlines. Deletion has limits: tax retention obligations override the request for the invoice record, and the answer is a partial deletion with an explanation, not a refusal.
- A processor register and a breach-notification procedure are required of most stores in the EU; the practical version is a list of every service that touches customer data, kept with the tracking plan.
- This is the legal basis for SKILL.md Rule 9: customer identity never leaves the store's own systems, and never enters `~/Clawic/data/`.

## Product and Marketing Compliance

- Product-specific rules travel with the category: safety marking and documentation, electrical and battery rules, cosmetics and food labelling, age restrictions, and market-surveillance obligations that in the EU require an identifiable responsible person inside the market for many product types.
- Claims are regulated: environmental claims, health claims, comparative advertising and "free" offers each have their own rules, and enforcement is increasing on the environmental ones (`catalog.md`).
- Importing means importer obligations — documentation, labelling and liability — even when the product is someone else's design.
- Selling into a new country adds that country's rules on top of the home market's. That is a cost line in the expansion decision, not a formality.

## The Calendar

Everything here is a dated obligation and belongs in `## Due` (SKILL.md Rule 8):

- VAT/GST return per its period; OSS returns quarterly in the EU, filed and paid by the deadline following the quarter
- Sales-tax filings per state, on the frequency that state assigns
- Threshold monitoring monthly: EU cross-border total, and each US state's running count
- Annual accounts, intrastat or equivalent statistical returns where volume requires them
- Registration reviews before any new country, new 3PL location, or new marketplace warehouse
- Policy review after any legal change that affects the disclosures above

**Write after tax or legal work**: registrations, tax regimes, markets and invoicing setup into `## Store`; every filing deadline into `## Due` with its period; the accountant or tax adviser into the shared `contacts.md`; the tax-engine subscription into `~/Clawic/data/finances/subscriptions.md`; and the registration record, the published policies and the disclosure checklist into `artifacts/<kebab-name>.md` with its `## Boxes` line (`memory-template.md`). The business's own tax numbers are working data and are kept; portal credentials are pointers only.
