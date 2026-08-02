# Fraud, Chargebacks and Abuse

Fraud costs are visible; **false declines are not**, and in most stores they are larger. Every rule written here has two costs — the fraud it stops and the good orders it kills — and both get measured.

**Before tuning a rule or answering a dispute**, read `disputes/<year>.md` (the store's own loss patterns and deadlines) and `## Metrics` (dispute rate) in `~/Clawic/data/ecommerce/memory.md`. Three losses for the same reason is a process fix, not bad luck.

## The Three Categories, Which Need Different Answers

| Category | What it is | Where the money goes |
|---|---|---|
| True fraud | Stolen card, account takeover, reshipper | Chargeback + goods + freight + fee |
| Friendly fraud / first-party misuse | Real customer disputes a real order — "not received", "not authorized" (family member), buyer's remorse routed through the bank | Same cost, different defence: evidence beats screening |
| Policy abuse | Serial returns, wardrobing, duplicate discount accounts, referral farming, repeated "not received" | Margin, not disputes — and screening never catches it (`returns.md`) |

Never fix one with the other's tool. Tightening authorization rules does nothing about wardrobing; a returns policy does nothing about a stolen card.

## Screening Signals, Weighted Honestly

No single signal decides. Score them, and set the thresholds by `fraud_posture`.

| Signal | Weight | Note |
|---|---|---|
| Billing ≠ shipping country | High | Country mismatch, not address mismatch — gift orders make addresses differ constantly |
| AVS / postal-code mismatch | Medium | Weak outside the US and UK; many issuers do not check it at all |
| CVV failure | High | A genuine customer mistypes once, not three times |
| Multiple cards, one account or device, short window | High | The classic card-testing pattern |
| Multiple accounts, one address or device | Medium | Discount abuse more often than card fraud |
| Order value far above your AOV | Medium | Correlate with method: high value + express + first order is the classic profile |
| Express shipping on a first order | Medium | Fraud wants the goods before the cardholder notices |
| Freight forwarder or known reshipper address | High | Legitimate for some international customers — decline politely, offer prepayment |
| Email created minutes before the order | Medium | Combine with anything else and it becomes high |
| Mismatch between card country, IP country and shipping | Medium | VPNs make this noisy on its own |
| Repeat customer with clean history | Strong negative | Weight history first, always — it is the cheapest signal you own |

Card testing has its own signature: a burst of small authorizations, high decline rate, often on the cheapest SKU or a gift card. Response is rate limiting and a challenge on the payment endpoint, not order-level review — and it should be alerted on, because processors notice before you do (`payments.md`).

## Thresholds and the Cost of Reviewing

```
Review is worth it when:  fraud rate in the segment × average order value  >  review cost per order
```

At a 12 review cost and a 60 AOV, reviewing pays only where the segment's fraud rate exceeds 20% — which almost no segment does. That arithmetic is why blanket manual review destroys more value than it saves, and why review queues should be small, fast and aimed at the top decile of score.

| `fraud_posture` | Auto-approve | Review | Auto-decline |
|---|---|---|---|
| `loose` | Everything except the top decile of score | Top decile | Only confirmed patterns (card testing, known reshipper) |
| `balanced` | Clean history or low score | Score above threshold, or two high-weight signals | Confirmed patterns plus very high score |
| `strict` | Clean history only | Any high-weight signal | Two high-weight signals, or high value + first order + express |

Measure all three of: dispute rate, **manual-review rate**, and **decline rate**. A rule change that halves disputes while doubling declines usually lost money, and only the first number appears in the fraud tool's dashboard.

## 3DS as a Liability Tool

- Successful 3DS authentication shifts liability for **fraudulent** disputes to the issuer. It does nothing for "not received" or "not as described" — those stay with the merchant whatever the authentication (`payments.md`).
- Selective 3DS beats blanket 3DS: route the high-score decile to a challenge and keep the rest frictionless with exemptions. Blanket 3DS is a conversion tax paid on every order to insure against a minority.
- A challenge that fails is not a decline; offer another method in-session.

## Disputes: The Clock and the Evidence Pack

**The day a dispute opens it becomes a `## Due` row and a row in `disputes/<year>.md`** (SKILL.md Rule 8). The processor's response deadline is earlier than the network's; the processor's date is the real one. A missed deadline is an automatic loss.

Evidence pack by reason code — assemble the same set every time:

| Reason | What wins |
|---|---|
| Product not received | Carrier tracking with the delivery scan and address, proof of the shipping address matching the order, signature or photo if available, delivery-notification emails |
| Product not as described | Product page as it was at purchase (archived), photographs, the policy the customer accepted, any support thread showing a remedy offered |
| Unauthorized / fraudulent | AVS and CVV results, 3DS result, device and IP data, prior order history from the same customer, delivery evidence to the cardholder's address |
| Duplicate / already refunded | The refund's own transaction record, with dates |
| Subscription cancelled | The cancellation flow's record, the terms accepted at signup, and the notice sent before renewal (`subscriptions.md`) |

- Fight only what you can evidence. A low win rate is not a badge of diligence: representment costs staff time, and the fee is kept either way.
- **Rate matters more than any single case.** Card-network monitoring programs put merchants above published dispute-rate and count thresholds into remediation, with fees and, eventually, processing loss. Hold the monthly rate an order of magnitude below the program threshold and treat any month above half of it as an incident. Verify the current thresholds with the processor before quoting them.
- Prevention beats representment on every dimension: a recognisable billing descriptor, dispatch and delivery emails, an easy refund path, and a phone number in the confirmation prevent more disputes than any evidence pack wins.

## Account Takeover and Store-Side Security

- Stored payment methods make accounts worth stealing. Require re-authentication before changing email, password, shipping address, or using a saved card from a new device.
- Notify the old address on an email change — that message is the customer's only chance to stop it.
- Loyalty points and store credit are currency: apply the same conditional atomic write as stock so a balance cannot be spent twice (SKILL.md Rule 3), and rate-limit redemption.
- Admin access to the store is the crown jewel: individual accounts with least privilege, MFA everywhere, and access removed the day someone leaves. Credentials are referenced by pointer, never written down (`memory-template.md`).

## Promotion and Referral Abuse

| Abuse | Control |
|---|---|
| One-per-customer code used many times | Enforce on payment fingerprint and address, not only on email |
| Self-referral loops | Payout only after the referred order clears the return window |
| Stacking codes to a negative total | Stacking rules and a CM floor per cart (`pricing.md`) |
| Leaked codes on coupon sites | Codes with expiry and volume caps; never a code that is also a memorable word unless it is meant to spread |
| Price-error exploitation | Price sanity check at checkout: reject any line more than X% below cost before the order is created |

**Write after risk work**: every dispute into `disputes/<year>.md` with its deadline, evidence sent and outcome, plus its `## Due` row on the day it opens; dispute rate, decline rate and manual-review rate into `## Metrics`; a card-testing burst or an ATO incident into `incidents/<year>.md`; and the rule set with its thresholds and the evidence-pack checklist into `artifacts/policy-fraud.md` with its `## Boxes` line (`memory-template.md`). Cases are identified by order number — never by customer name, email, IP or card digits (SKILL.md Rule 9).
