# Fulfillment — Getting the Parcel There Without Eating the Margin

Shipping is the second-largest cost line after COGS in most stores and the largest source of contactable complaints. The work is arithmetic first (cost per order), process second (pick, pack, hand over), communication third (the customer's anxiety between dispatch and delivery).

**Before quoting a rate, a delivery promise, or a 3PL decision**, read `## Unit Economics` (freight already priced into CM) and `## Channels` (marketplace shipping commitments) in `~/Clawic/data/ecommerce/memory.md`. A delivery promise made without the current carrier performance is a refund scheduled in advance.

## Cost Per Order, Not Cost Per Parcel

```
Fulfillment cost per order = freight + packaging + pick/pack labour
                            + (failed-delivery rate × redelivery cost)
                            + (loss/damage rate × replacement cost + freight)
```

Worked: freight 4.20, packaging 0.55, labour 1.20 (4 min at a 18/hour loaded rate), failed delivery 3% × 3.80 = 0.11, loss/damage 0.4% × 26 = 0.10 → **6.16 per order**. That number, not the carrier's headline rate, is what belongs in the contribution-margin formula (SKILL.md Rule 4) and in the free-shipping threshold decision (`pricing.md`).

- Recompute it quarterly and after any packaging change; it drifts with fuel surcharges, carrier annual increases and product mix.
- Labour per order falls fast with batch picking and rises with SKU count and personalization. Measure it once with a stopwatch rather than assuming.

## Rates: Zones, Weight and the Dimensional Trap

- Carriers bill on **the greater of actual weight and dimensional weight**: `L × W × H ÷ divisor`, with the divisor set in the contract. A light bulky product is billed as if it were heavy, which is why packaging redesign is often the cheapest freight saving available.
- Zone and weight break points create cliffs: 1,010 g on a 1 kg band costs a full band more. Know the top three break points for your best-selling parcels and design packaging to sit just under them.
- **Never pass raw carrier rates to the customer.** Choose one:

| Rate strategy | Fits | Watch |
|---|---|---|
| Flat rate | Narrow weight range, one country | Loses money on the heaviest orders; check the tail, not the average |
| Banded by cart value | Simple, aligns with AOV goals | Disconnected from real cost; reprice when the mix moves |
| Real-time carrier rates | Wide product range, many destinations | Needs a cached fallback or checkout breaks when the API is slow (`checkout.md`) |
| Free above a threshold | AOV growth | Threshold = AOV × 1.25 **and** CM at that basket must still cover freight (`pricing.md`) |
| Free always | High-margin, low-weight | It is a permanent discount; price it into the product |

- Negotiate on volume with the numbers in front of you: parcels per month, average billed weight, zone mix, and the competitor quote. Discounts are per-lane, so a single blended discount is usually worse than it looks.

## Choosing a Carrier, and Choosing Two

- Selection order: **coverage of your destinations → delivery-time consistency → price → tracking quality → claims process.** Price first is how stores end up with the cheapest carrier in the worst region.
- Run a **second carrier for at least 10-20% of volume**, permanently. It is the only way to have a working alternative during a strike, a peak-season meltdown, or a service failure — switching carriers cold takes weeks of integration and rate negotiation.
- Delivery-time *consistency* beats speed: a reliable 4-day service produces fewer contacts than an average 2-day service with a long tail.
- Home delivery vs pickup point: pickup points cut cost and failed deliveries and are the default in several European markets. Offer both and let the customer choose; the choice itself reduces complaints.

## Packaging

- Right-size the box: dimensional weight, damage rate and unboxing all improve together. A void-fill-heavy parcel is paying to ship air on every order.
- Damage rate above ~1% is a packaging problem, not a carrier problem — carriers do not damage some stores more than others.
- Fragile, liquid, battery and aerosol items have carriage rules and labelling requirements; the flag lives on the product (`catalog.md`) and must reach the label at pack time.
- Branded packaging is marketing spend: judge it against the return rate it prevents and the repeat rate it might lift (`retention.md`), not against how it looks.

## In-House vs 3PL

Break-even, honestly stated: 3PL wins when your own cost per order plus the founder-hours consumed exceeds the 3PL's per-order fee. Typical decision drivers:

| Keep in house | Move to a 3PL |
|---|---|
| Low volume, or personalization/assembly per order | Volume where picking dominates a working day |
| Product needs handling judgement (fragile, made-to-order) | Standard boxes, standard flows |
| Cash is short — a 3PL wants onboarding, storage and minimums | Growth is blocked by fulfillment capacity |
| Multi-country demand met from one origin acceptably | Regional warehouses cut freight and duty materially (`tax.md`) |

3PL contract items that cost real money later: receiving fees per unit vs per pallet, long-term storage penalties, minimum monthly fees, pick fees for multi-line orders, returns handling fee, and the exit clause — who pays to get your inventory out, and how fast.

## The Delivery Exception Ladder

Most support volume is here. Decide once, apply without deliberation:

| Situation | Threshold | Action |
|---|---|---|
| No tracking movement | 48 h after dispatch | Open a carrier trace, tell the customer before they ask |
| In transit, past the promise | 2 days past | Proactive email with the new estimate; no compensation yet |
| Marked delivered, not received | Any | Check the scan location and the neighbour, then reship or refund by value — the investigation costs more than most parcels |
| Failed delivery attempts | 2 | Contact for an alternative address or a pickup point before the parcel returns |
| Returned to sender | On receipt | Refund minus original shipping where the law allows, or reship at the customer's cost — one policy, applied to everyone |
| Damaged on arrival | Any | Photo, replace immediately, file the carrier claim in parallel; never make the replacement wait for the claim |
| Lost | Carrier's declared window | File the claim, replace now; claim reimbursement is slow and often partial |

Carrier claims have short filing windows and require the original invoice value and packaging evidence. Track them: unclaimed losses are pure margin gone (`## Due`).

## Cross-Border

- **DDP vs DAP** is the biggest single lever on international conversion. DAP means the customer gets a customs bill at the door and a share of them refuse the parcel; DDP means you collect duty and tax at checkout and the parcel arrives clean. DDP costs integration work and is almost always worth it above modest international volume (`tax.md`).
- Landed cost = product + freight + duty + import tax + broker fee. Quote it at checkout or expect refusals and returns billed both ways.
- Every parcel needs a commercial invoice with an accurate description, HS code, country of origin and value. Under-declaring value is fraud, and it also voids the insurance you would need.
- Deep carrier, customs and incoterm work: `shipping`.

**Write after fulfillment work**: cost per order and any freight change into `## Unit Economics` with its `as of` date; carrier, service level and 3PL choice into `## Store`; the 3PL or carrier account manager into the shared `contacts.md`; a systemic delivery failure into `incidents/<year>.md`; carrier claim deadlines and the quarterly freight refresh into `## Due`; and a packing spec, exception policy or 3PL comparison into `artifacts/<kebab-name>.md` with its `## Boxes` line (`memory-template.md`). Tracking numbers stay out of every file (SKILL.md Rule 9).
