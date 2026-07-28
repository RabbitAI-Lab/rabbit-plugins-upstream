# Payments — The Money Path From Cart to Bank

Every payment problem is a disagreement between two systems about one of five states: **authorized, captured, settled, refunded, disputed**. Name the state and the two systems before proposing a fix.

**Contents:** [The Five States](#the-five-states) · [Idempotency and Webhooks](#idempotency-and-webhooks) · [Declines and Retries](#declines-and-retries) · [SCA and 3DS](#sca-and-3ds) · [Fees and What They Really Cost](#fees-and-what-they-really-cost) · [Payout Reconciliation](#payout-reconciliation) · [Refunds and Voids](#refunds-and-voids) · [Stored Cards and Off-Session Charges](#stored-cards-and-off-session-charges) · [PCI Scope](#pci-scope) · [Test the Failure Paths](#test-the-failure-paths)

**Before answering any payment question**, read `## Store` (processor, `pci_scope`, markets) and `## Channels` (fee stack) in `~/Clawic/data/ecommerce/memory.md`. A fee quoted without the store's actual stack is a guess.

## The Five States

| State | What it means | What breaks here |
|---|---|---|
| Authorized | Funds held on the card, nothing moved | The hold expires — card-not-present auths commonly last around 7 days; capture after expiry fails and the order looks paid but is not |
| Captured | Charge submitted, money leaving the customer | Capture at ship time is correct only if shipping happens inside the auth window; otherwise capture at order and refund on cancel |
| Settled | Processor has the funds, payout pending | Payout lag (1-14 days by processor and channel) is a cash-flow fact — record it in `## Channels`, not in the accounting |
| Refunded | Money returned, wholly or partly | Most processors keep the fixed fee, some keep the percentage too; a refunded order rarely returns to zero cost |
| Disputed | Issuer pulled the funds pending evidence | The amount plus a dispute fee leaves immediately; winning returns the amount, rarely the fee (`fraud.md`) |

Order status and payment state are two different machines. Never derive one from the other by assumption: an order marked "paid" because a redirect landed on the thank-you page is a guess, and the customer who closes the tab first makes it a wrong one.

## Idempotency and Webhooks

The two mechanisms that make the money path replay-safe. Both are required; either alone leaves a hole.

- **Idempotency key = a deterministic function of the operation**, e.g. `order:{id}:capture`. A fresh UUID per attempt is the same as no key. Keys expire at the processor (commonly 24 hours) — after that a retry is a new charge, so late retries need a lookup, not a key.
- Reusing a key with a *different* payload returns an error rather than a charge. That error is a bug signal: the same operation is being built two different ways.
- **Verify the signature against the raw request body** before any parsing. Body-parser middleware that rewrites JSON invalidates the signature — the most common cause of "signature verification failed" on a correct secret.
- **Dedupe on the provider's event id** in a unique-constrained table, inside the same transaction as the state change:

```sql
-- Insert first: the unique violation IS the duplicate check.
INSERT INTO processed_events (event_id, received_at) VALUES ($1, now());
-- unique violation → already handled, return 200 and stop.
UPDATE orders SET payment_state = 'captured', charge_id = $2
 WHERE id = $3 AND payment_state IN ('authorized');   -- never move backwards
```

- **Return 2xx inside the provider's timeout** (seconds), then do the work asynchronously. A slow handler is retried, which is how one order becomes three.
- **Events arrive out of order.** `charge.refunded` can land before `charge.succeeded`. The state machine must ignore backwards transitions rather than apply them, and reconciliation catches whatever the ordering lost.
- Build a replay path: a command that re-fetches events for a window and re-runs them. Without it, an outage means manual data entry.

## Declines and Retries

| Decline class | Examples | Retry? |
|---|---|---|
| Hard | lost/stolen card, invalid account, pickup card, revoked authorization | Never — retrying a hard decline attracts fees and network attention |
| Soft | insufficient funds, issuer unavailable, do-not-honor, velocity limits | Yes, with backoff and a cap; a different day and a smaller amount both help |
| 3DS-required | authentication needed | Not a decline — route to the challenge (`SCA and 3DS`) |
| Fraud-suspected by your own rules | score above threshold | Not a retry decision — score it (`fraud.md`) |

- Card networks **cap re-attempts of a declined authorization** and fine merchants who exceed the cap; the current number is published by the processor. Never build an unbounded retry loop, and never retry the identical amount on the same day more than the cap allows.
- Decline *rate* is a business metric, not an engineering one: a 3-point improvement in authorization rate is usually worth more than a conversion test, and it is invisible unless it is measured per market and per method.
- Recurring charges have their own ladder (`subscriptions.md`); one-off checkout declines get a retry prompt in-session with an alternative method, which converts better than any email.

## SCA and 3DS

- In the EEA and the UK, strong customer authentication applies to most consumer card payments; the processor applies it, but the **exemptions decide the friction**: low-value transactions (with a cumulative counter that resets after a handful of them), transaction-risk analysis at low fraud rates, merchant-initiated transactions, and trusted-beneficiary listing.
- **3DS shifts liability for *fraudulent* disputes to the issuer.** It does nothing for "item not received" or "not as described" — those remain yours whatever the authentication. Choosing 3DS for everything trades conversion for a shield that only covers one dispute category.
- Frictionless 3DS is the goal: pass the full data set (email, billing address, shipping address, device data) so the issuer can approve without a challenge. Missing fields cause challenges that read to the customer as a broken checkout.
- `fraud_posture: strict` routes more traffic to 3DS; `loose` uses exemptions harder. Both are legitimate; the cost of each shows up in different columns (`fraud.md`).

## Fees and What They Really Cost

Effective rate = total fees ÷ gross processed. Quote that, never the headline percentage.

| Fee line | Where it hides |
|---|---|
| Percentage + fixed | The fixed part dominates small baskets: on a 12-unit order, a 0.25 fixed fee is 2.1% on its own |
| Cross-border / international card | Applied on the *card's* country, not the customer's shipping address |
| Currency conversion | 1-2% typical on top, whether the processor converts or the platform does |
| Platform payment fee | Charged by the storefront platform when you do not use its native processor — stacks on top of the processor's |
| Chargeback fee | Per dispute, kept even when you win |
| Payout / instant-payout fee | Optional but silently enabled on some accounts |
| Wallet and BNPL premiums | BNPL commonly costs several points more than cards; justified only if it lifts CM per session, not AOV alone |

Interchange++ pricing beats blended pricing above a volume where the effective rate is stable enough to model — ask for both quotes and compute the effective rate on last month's real transaction mix rather than on an average basket.

## Payout Reconciliation

Run it monthly, and after any month where the bank number surprises anyone:

```
payout = gross − refunds − disputes − fees − reserve ± FX ± timing
```

- Work from the processor's **balance transaction export**, not the dashboard summary: only the transaction level shows the fee per charge and the reserve movements.
- Two timing traps: a charge captured on the 31st settles in the next month, and a refund of last month's order lands as a negative this month. Reconcile by *settlement* date for cash and *order* date for revenue, and never mix them in one table.
- A mismatch that survives the formula is one of: a manual refund issued in the dashboard that the store never saw, a dispute nobody opened a `## Due` row for, or a second processor nobody mentioned.

## Refunds and Voids

- **Void before capture is free**; refund after capture usually is not. Cancelling an unshipped order the same day should void, not refund — an easy setting to get wrong and an easy few points of margin to recover.
- Refunds originate in **one** system. If the store can refund and the dashboard can refund, someone will do both, and the double refund is discovered at reconciliation (`returns.md`).
- Partial refunds need a rule for the shipping component: EU withdrawal obliges refunding the *standard* outbound shipping, not the express upgrade (`tax.md`).
- Refunds after the payout window pull from future payouts; on a low-volume store that can produce a negative balance and a debit from the bank account. Keep a reserve when the refund rate is above ~15%.

## Stored Cards and Off-Session Charges

- Save the processor's **token**, never the card. Flag the mandate type at the first charge (customer-initiated vs merchant-initiated) — a later off-session charge with the wrong flag gets declined for missing authentication.
- Network tokens and automatic card-updater services materially reduce declines caused by reissued cards; they are usually a checkbox and worth more than most checkout optimizations.
- The first charge of a saved-card series must be authenticated in-session, or every later charge is unenforceable and disputable.

## PCI Scope

| `pci_scope` | What it means | The rule |
|---|---|---|
| `redirect` | Customer pays on the processor's page | Smallest scope; conversion cost is the page change, mitigated by wallets |
| `hosted-fields` | Processor's iframe fields inside your form | The default recommendation: your DOM, their scope |
| `self-hosted-fields` | Card data touches your page or server | Full audit obligations, quarterly scans, and a breach liability the store cannot insure away |

Never log a request body that could carry card data, never echo card data back in an error message, and never store PAN, CVV or expiry anywhere — including in `~/Clawic/data/` (SKILL.md Rule 9).

## Test the Failure Paths

The happy path is tested by every customer. These are not:

- Declined card, then successful retry in the same session
- 3DS challenge abandoned halfway
- Webhook delivered twice, and delivered out of order
- Double-click on the pay button (the classic double order)
- Refund of a partially shipped order
- Payment succeeded, order creation failed — does the reconciliation job find it?
- Currency other than the default, and a card issued outside the home market

**Write after any payment work**: processor, methods, `pci_scope` and market coverage into `## Store`; the fee stack and payout lag per channel into `## Channels`; a reconciliation gap or an outage into `incidents/<year>.md` with orders affected and revenue impact; a dispute into `disputes/<year>.md` plus its deadline in `## Due`; and a reconciliation procedure or a webhook-handler design that finally worked into `artifacts/<kebab-name>.md` with its `## Boxes` line (`memory-template.md`). Every key in what you write is a pointer, never a value.
