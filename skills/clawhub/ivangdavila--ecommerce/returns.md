# Returns — Refunds, Exchanges and the Cost of Getting Goods Back

A return is a second, unpaid fulfillment plus a refund. The store's job is not to minimize returns — it is to **prevent the avoidable ones, absorb the legal ones cheaply, and keep the abusive ones from becoming a policy for everyone**.

**Before changing any policy or answering an edge case**, read the returns policy artifact if `## Boxes` names one, and `## Metrics` for the store's current return rate. A policy change made without the current rate is a guess about the biggest variable in it.

## What a Return Actually Costs

```
Return cost = inbound freight + inspection labour + restocking labour
            + refurb/repack + (write-off rate × unit cost) + payment fee kept
            + the original outbound freight, already spent
```

A 50 item with 4.50 outbound freight and a 3.80 return label costs roughly 12-14 before the write-off decision. That is why the CM formula (SKILL.md Rule 4) carries `return rate × return handling cost` per SKU, and why a 30% return category needs a different price than a 5% one.

## The Legal Floor, Then Your Policy

The floor is not negotiable; anything above it is a marketing decision that must be priced.

| Jurisdiction | The floor |
|---|---|
| EU / EEA | 14-day right of withdrawal from delivery, no reason required; refund within 14 days of being informed, including standard outbound shipping (not the express upgrade); may withhold until goods return or proof of dispatch; customer pays return shipping only if that was disclosed before purchase |
| EU / EEA | Separate 2-year legal guarantee of conformity for faulty goods, independent of any commercial warranty and of the withdrawal window |
| UK | Comparable 14-day cancellation regime under consumer contract regulations |
| US | No federal right of return; the policy is whatever you published — but card networks enforce their own view during a dispute, so an unpublished or hidden policy loses chargebacks |
| Everywhere | Faulty is not a return: it is a remedy — repair, replace or refund — and the clock is not the return window |

Exclusions that survive scrutiny in the EU: made-to-measure and personalized goods, sealed hygiene or health items once unsealed, sealed audio/video once unsealed, perishables, and digital content where the customer explicitly consented to immediate delivery and waived withdrawal (`catalog.md`). Anything else claimed as an exclusion is a dispute waiting to be lost. Verify the current wording for the market in `tax.md`.

## Designing the Policy

- **Publish the window, the condition standard, who pays return freight, and the refund timeline** in one place, in plain language, linked from the product page and the checkout. A hidden policy raises support volume and loses disputes.
- Longer windows reduce returns in practice — urgency to decide is what produces the impulse return — and they raise the write-off risk on seasonal goods. 30 days is a common, defensible step above the legal 14.
- **Free returns**: a conversion lever with a direct margin cost. Rule of thumb for the decision: free returns are affordable when `CM% > return rate × (return cost ÷ price)` still leaves the target margin. Apparel at 30% returns needs a different answer than a 70%-CM accessory (SKILL.md Where Experts Disagree).
- Store credit at a premium (e.g. 110% of value) converts a refund into retained revenue for customers who accept it — offered, never forced, and never in place of a legal refund.

## The Flow

1. **Request** through a self-service portal, not email. The portal captures the reason code, which is the only durable output of the whole process.
2. **Authorize** with an RMA number and a label or instructions. Auto-approve inside the window and under a value threshold; route the rest to a human.
3. **Receive** and scan against the RMA. Unidentified parcels are the largest source of "I returned it weeks ago" tickets.
4. **Inspect within 48 hours** against a written condition grid, with photos for anything below full-refund condition.
5. **Refund** to the original payment method within the legal window, or issue the agreed alternative. One system issues refunds (`payments.md`).
6. **Disposition**: restock, refurb, liquidate, or write off — decided by the grid, not per case.
7. **Close the loop**: the reason code goes into the product's record so the catalog can be fixed (`catalog.md`).

## Partial Refunds and Condition

| Condition on arrival | Refund |
|---|---|
| Unused, sealed, complete | Full |
| Used beyond inspection, resellable after refurb | Full minus refurb cost, disclosed with photos |
| Missing accessory or packaging that must be replaced | Full minus replacement cost at your cost, not retail |
| Damaged by the customer | Diminished-value deduction, documented; in the EU the customer is liable only for value lost through handling beyond what is needed to establish nature and function |
| Not received after the agreed window | No refund; one reminder, then close |
| Faulty or not as described | Full refund including both freight legs — this is not a return, it is a remedy |

Deductions require evidence at the moment of inspection. A deduction argued from memory two weeks later becomes a chargeback the store loses.

## Reason Codes Are the Product Feedback Loop

Keep the list short enough that packers use it honestly: **too small · too large · not as pictured · quality below expectation · arrived damaged · arrived late · changed mind · wrong item sent · faulty**.

| Dominant reason | The real fix |
|---|---|
| Too small / too large | Size chart with measured garment dimensions, model reference, and per-product fit feedback (`catalog.md`) |
| Not as pictured | Colour accuracy, scale reference, and honest photography |
| Quality below expectation | Copy is overselling, or the supplier changed something — check the last delivery |
| Arrived damaged | Packaging, not the carrier, until proven otherwise (`fulfillment.md`) |
| Arrived late | Delivery promise vs actual performance (`fulfillment.md`) |
| Wrong item sent | Pick accuracy — measure it; above ~0.5% is a process fault |

A store that fixes the top reason code each quarter cuts its return rate faster than any policy change.

## Abuse Without Punishing Everyone

Measure per customer, act per customer:

| Return rate (last 12 months, by value) | Action |
|---|---|
| Under 15% | Normal, no action |
| 15-30% | Monitor; check for one category dominating |
| Over 30%, or over 5 returns in 12 months | Review history: wardrobing, serial "not received", or a genuine fit problem you are causing |
| Confirmed abuse | Require returns before refund, remove free-return eligibility, and as a last step decline future orders — with a written record of why |

- **"Item not received" claims** are a separate pattern from returns; repeated claims from the same account belong in `fraud.md`, not here.
- Never apply an abuse restriction to a first-time customer or to a faulty-goods claim; the false-positive costs more than the fraud.

## Exchanges

- Exchanges retain revenue that refunds lose, and the size-swap exchange is the highest-value option in apparel. Make the exchange path the *default* choice in the portal, with refund one click away.
- Ship the replacement on receipt of the return scan, not on inspection, for customers with clean history — the wait is what turns exchanges back into refunds.
- An exchange for a different-priced item is a refund plus a new order in the accounting, whatever the portal calls it; make sure the tax and the fees are recomputed (`tax.md`).

**Write after returns work**: return rate and refund rate per month into `## Metrics`; the return cost component per SKU or category into `## Unit Economics`; a dominant reason code and what was changed because of it into `## Pain Points`; a repeated "not received" pattern into `disputes/<year>.md` or `fraud.md`'s box; and the published policy, condition grid and disposition rules into `artifacts/policy-returns.md` with its `## Boxes` line (`memory-template.md`). Customers appear as counts and order numbers, never by name (SKILL.md Rule 9).
