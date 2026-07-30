# Orders — The Lifecycle and Everything That Gets Stuck In It

An order is a state machine with money attached. Most operational pain comes from two things: states that exist in the platform but not in the process, and orders that stop moving without anyone being told.

**At the start of any operations question**, read `## Store` (platform, channels) and `incidents/<year>.md` if `## Boxes` names it — a stuck-order pattern that already happened has a cause on file.

## The State Machine

| State | Enters when | Leaves when | Alert if stuck |
|---|---|---|---|
| Pending payment | Checkout created the order, no capture | Payment confirmed | > 1 hour (payment timeout or a dropped webhook) |
| Payment review | Fraud score or manual flag | Approved or cancelled | > 24 hours (`fraud.md`) |
| Processing | Paid, awaiting pick | Handed to carrier | > 24 business hours |
| Partially shipped | One or more lines dispatched | All lines dispatched | > 72 hours since the first parcel |
| Shipped | Carrier accepted | Delivery scan | No movement 48 h after dispatch (`fulfillment.md`) |
| Delivered | Carrier confirms | Return window closes | — |
| Completed | Return window passed | — | — |
| Cancelled / refunded | Explicit action | — | Refund not settled in 5 days |

Rules that keep it honest:

- **States only move forward.** A late webhook must never push a shipped order back to processing (`payments.md`).
- Every transition writes who or what caused it and when. "The order changed itself" is always an integration nobody documented.
- Payment state and fulfillment state are separate fields. Collapsing them into one status is why "paid but not shipped" and "shipped but not paid" become invisible.

## The Sweep That Catches Everything

Run it daily at low volume, hourly above roughly 100 orders/day. Each query is a list that should normally be empty:

| Query | Why it matters |
|---|---|
| Paid in the processor, no order in the store | Lost webhook — money taken, nothing shipping (`payments.md`) |
| Order in the store, no payment, older than the timeout | Auto-cancel and release stock, or it holds inventory forever |
| Authorized but never captured, approaching the auth expiry | Capture now or lose the sale silently |
| Processing beyond the SLA | Pick failure, stock discrepancy, or an address that failed validation |
| Shipped without a tracking number | The carrier handover never registered |
| Refund initiated, not settled | A refund that fails quietly becomes a dispute |
| Partially shipped for more than 72 hours | Waiting on a backorder nobody is chasing (`inventory.md`) |
| Orders with a total below the SKU cost | A discount stacking bug in production (`pricing.md`) |

An empty list is a result: record the sweep in `## Due` so the one week it is skipped is visible.

## Editing, Splitting and Cancelling

- **Editing a paid order changes money.** Adding a line requires a new charge, removing one requires a partial refund, and both must go through the same idempotent path as checkout, never a manual dashboard adjustment that the store never learns about.
- **Address changes before dispatch** are free and should be self-service inside a short window; after handover they are a carrier intercept with a fee, or a redelivery. Publish which is which.
- **Cancellation before dispatch** should void rather than refund where the payment is not yet captured (`payments.md`), and must return stock in the same transaction.
- **Splitting** an order costs a second parcel's freight and pick fee. Split automatically only when one line is delayed beyond the promise; otherwise ask (`fulfillment.md`).
- Every edit is recorded on the order with its reason. Reason-less edits are how a store discovers, months later, that a staff member was discounting by hand.

## Order Numbers and Idempotency at the Human Layer

- Order numbers are customer-facing and permanent: sequential with a market prefix (`ES-10442`) beats a UUID nobody can read over the phone, and beats an obviously sequential number starting at 1 that tells competitors your volume — start the sequence somewhere unremarkable.
- Never reuse a number, including after a cancellation. Refunds, invoices, tax records and carrier claims all key on it.
- Duplicate orders from the same customer minutes apart are usually a double submit, occasionally a genuine second order. Detect and *ask* rather than auto-merging; merging a real second order loses a sale and a customer's trust in one move (`checkout.md`).

## Fulfillment Handover

- The pick list is generated from the order, and the packing slip is generated from the pick — printing the customer's own cart as the pick list is how substituted or short-picked lines ship unnoticed.
- Scan-verify at pack for stores above a few hundred orders a month: scanning the SKU against the order catches the mispick that would otherwise cost a return, a reship and a review.
- Batch by picking path, not by order arrival. Wave picking cuts the walk, which is most of the labour in the cost-per-order formula (`fulfillment.md`).
- Cut-off time is a promise: publish it, honour it, and change it in advance of peak rather than during it (`peak.md`).

## Order Data and Documents

- The invoice is a legal document in most EU markets: sequential numbering, seller tax details, buyer details, the tax breakdown per rate, and immutability once issued. Corrections are credit notes, never edits (`tax.md`).
- Keep order and invoice records for the statutory retention period of the home market — commonly several years — and keep them exportable from the platform. Retention obligations survive replatforming (`platforms.md`).
- Customer-facing order data (name, address, contents) lives in the store and only in the store. Local notes reference the order number (SKILL.md Rule 9).

## Multi-Channel Order Intake

- Marketplace orders arrive with their own rules: shipping-time commitments, carrier restrictions, buyer-messaging rules, and a cancellation metric that penalises you for stock you did not have (`marketplaces.md`).
- Normalize every channel into one internal order shape at intake, keeping the channel and its external id. Ops staff working in two consoles is where the shipping deadline gets missed.
- Never let a marketplace's SLA be met by breaking a store order's promise — fill by margin, but treat marketplace commitments as fixed constraints (`inventory.md`).

**Write after operations work**: a stuck-order pattern, a mispick rate, or an SLA breach into `## Pain Points`; an outage or systemic failure into `incidents/<year>.md` with duration, orders affected, revenue impact and how it was detected; the sweep and cut-off cadences into `## Due`; and the sweep queries, the state machine as implemented, or an ops runbook into `artifacts/<kebab-name>.md` with its `## Boxes` line (`memory-template.md`).
