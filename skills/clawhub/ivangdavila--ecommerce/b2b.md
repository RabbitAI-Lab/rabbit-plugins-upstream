# B2B and Wholesale — Selling to Buyers, Not Shoppers

A wholesale order is a different product: larger, less frequent, negotiated, often unpaid at dispatch, and tax-treated differently. Running it on retail assumptions produces two predictable failures — **margin given away in tiers nobody modelled** and **credit extended to buyers nobody checked**.

**Before quoting terms or a price list**, read `## Unit Economics` (retail CM per SKU) and the shared `~/Clawic/data/contacts/contacts.md` (existing accounts and their context). A wholesale price set without the retail CM is a discount with no floor.

## What Changes Versus DTC

| Dimension | DTC | B2B |
|---|---|---|
| Price | One public price | Tiered price lists per account or group, often confidential |
| Payment | At checkout | Net terms, deposits, or proforma before dispatch |
| Tax | Charged to the consumer | Zero-rated cross-border in the EU with a **validated** VAT number; exemption certificates in the US (`tax.md`) |
| Minimum | None | MOQ per order and often per SKU, plus case-pack multiples |
| Fulfillment | Parcel | Pallets, freight, delivery windows, booking-in requirements |
| Returns | Statutory consumer rights | Contractual only — consumer withdrawal rights do not apply between businesses |
| Support | Ticket | A named person, a phone number, and an expectation of one |
| Catalog | Everything | A subset, sometimes with buyer-specific SKUs or packaging |

## Pricing Tiers

```
Wholesale price = retail price × (1 − wholesale discount)
Floor: wholesale CM = wholesale price − COGS − outbound freight − handling  ≥  target CM on volume
```

- Wholesale is a volume trade: lower CM% per unit is fine if the order size and the payment reliability compensate. Compute CM **per order**, not per unit, because freight and handling barely scale with quantity.
- Common structure: 2-4 tiers by annual committed volume, with the entry tier at the MOQ. More tiers than that becomes a negotiation surface nobody can hold.
- **Never quote a wholesale price that undercuts your own retail after the buyer's markup** — you have just built a competitor with your own margin. If the buyer's retail price would sit below yours, either the tier is wrong or the account is wrong.
- MAP or resale-price expectations must be contractual and enforceable in the jurisdiction: the floor per SKU into `## Unit Economics` of `memory.md` (a `MAP floor` column, with currency), the clause itself into the terms document in `artifacts/<kebab-name>.md`. Pricing mechanics in `pricing.md`.
- Price-list changes need notice, and open quotes must be honoured for their stated validity. Quotes carry an expiry date for exactly this reason.

## Credit and Getting Paid

- **Terms are a loan.** Net 30 on a 4,000 order is 4,000 of your working capital lent at 0%, and the risk is the buyer's solvency, not their intentions.
- New accounts start on **proforma or card payment**, moving to terms after a demonstrated payment history — typically a handful of clean orders. Existing relationships are not evidence; paid invoices are.
- Set a **credit limit per account** and enforce it at order entry, including orders already shipped and unpaid. A limit that is checked manually is a limit that is exceeded during a busy week.
- Credit checks for anything material; trade references are weak evidence and easy to arrange.
- Dunning for invoices is a ladder like any other: reminder before due, on due, +7, +14, then stop supply. Stopping supply is the only lever that works, and using it late costs more than using it early.
- Watch concentration: an account above roughly 20% of revenue prices your business, and its insolvency is your incident (`## Channels`).

## Ordering and Catalog for Buyers

- Buyers want speed, not discovery: a login-gated catalog with their prices, fast reorder from history, bulk entry by SKU and quantity, CSV upload, and stock visibility. Recreating the retail browsing experience wastes the one thing the buyer values.
- Case packs and MOQ enforced at the line level, with a clear message rather than a silent rounding.
- Stock visibility for wholesale should show **available to promise** — on-hand minus retail allocation — or you will sell the same units twice (`inventory.md`).
- Buyer-specific SKUs, private-label variants and custom packaging are catalog entries, not exceptions in someone's memory (`catalog.md`).
- Quotes, proformas, order confirmations and invoices are separate documents with different legal weight. Number them separately and keep them immutable (`orders.md`).

## Tax and Documentation

- **EU cross-border B2B**: zero-rating under the reverse charge requires a valid VAT number validated at order time, with the validation result stored against the order. An unvalidated number leaves the VAT owed by you (`tax.md`).
- **US**: an exemption certificate per state, on file, current, and re-collected before it expires. An expired certificate is the same as none in an audit.
- Export documentation for cross-border freight: commercial invoice, packing list, HS codes, country of origin, incoterms agreed in writing. Incoterms decide who pays duty and who carries the risk in transit — agree them before the first pallet, not after the first problem (`fulfillment.md`).
- Retention rules apply to the whole document chain, not only the invoice (`tax.md`).

## Channel Conflict

- Wholesale and DTC compete for the same end customer. Decide the boundary explicitly: exclusive territories, exclusive SKUs, or a price and service difference that both sides can defend.
- The common resolution is product segmentation — a wholesale range and a DTC range that overlap partially — plus a promise not to undercut your stockists during their season.
- Your own marketplace listings compete with your stockists' listings on the same platform. That is the most common cause of a lost account, and it is worth deciding before it happens (`marketplaces.md`).
- Dropship-for-retailer arrangements blur the line further: you fulfil, they own the customer. Price it as wholesale plus fulfillment, never as retail.

## Onboarding an Account

A repeatable sequence removes most later disputes:

1. Qualify: what do they sell, where, and does it fit the brand boundary above.
2. Collect: legal entity, tax number (validated), delivery and invoicing addresses, booking-in requirements, and a named contact.
3. Terms: tier, MOQ, payment terms, credit limit, lead time, returns and damages policy, MAP if any — in one signed document.
4. Set up: price list, catalog access, delivery profile, invoicing details.
5. First order on proforma, whatever the size.
6. Review at 3 and 12 months: volume against tier, payment behaviour, margin realised.

**Write after B2B work**: the account's terms, tier, MOQ, credit limit and lead time into `## Wholesale Accounts` of `memory.md` (created with that exact heading the first time an account is onboarded, and split to `~/Clawic/data/ecommerce/wholesale-accounts.md` past the threshold, with its `## Boxes` line); the person into the shared `~/Clawic/data/contacts/contacts.md` with role `wholesale account`; wholesale CM per SKU into `## Unit Economics`; a payment-terms breach or a channel-conflict incident into `## Pain Points`; and the price list, terms template and onboarding checklist into `artifacts/<kebab-name>.md` (`memory-template.md`). Tax numbers of businesses are working data; portal and bank credentials are pointers only.
