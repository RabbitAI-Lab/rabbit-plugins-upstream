# Inventory — Stock, Reorders, and Not Overselling

Two failures, opposite costs. **Overselling** costs a refund, a review and sometimes a marketplace metric. **Stockouts** cost the margin of every unit you could have sold, and that number never appears in any report. Inventory work is the arithmetic that keeps both small.

**Before any reorder, promise, or sale planning**, read `## Suppliers` (lead times, MOQ) and `## Unit Economics` in `~/Clawic/data/ecommerce/memory.md`, or the files `## Boxes` points to. A reorder computed without the real lead time is a guess with a 35-day fuse.

## One Source of Truth

- Exactly one system owns the stock number; every other system subscribes. If the store and the marketplace both own it, they will disagree and the disagreement is discovered by a customer.
- **Channel buffer** = `peak units sold per sync interval × 2`. A SKU selling 6 units/hour at peak with a 30-minute sync holds a buffer of 6 units. Halving the sync interval halves the buffer and frees that stock for sale — the buffer is the price of latency, so buy less latency instead of hoarding stock.
- Sync interval by velocity, not by convenience: A items (top 20% of revenue) as near real-time as the channel allows; B items every 15 minutes; C items hourly is fine.
- **Adjustments are deltas, never absolute writes.** `qty = qty − 3` survives a concurrent sale; `qty = 47` overwrites it. Absolute writes during a sale is how a store oversells while someone is fixing an oversell.

```sql
-- The only correct decrement (SKILL.md Rule 3)
UPDATE stock SET qty = qty - :n
 WHERE sku = :sku AND qty >= :n;
-- rows affected 0  → sold out, fail the line item, do not charge
```

## Reorder Point and Safety Stock

```
Reorder point = (average daily units × lead time in days) + safety stock
Safety stock   = z × σ_daily × √(lead time in days)
z = 1.65 for ~95% service level; 1.28 for 90%; 2.33 for 99%
```

Worked example: 5 units/day average, σ 2 units/day, 35-day lead time, 95% service level.
Safety stock = 1.65 × 2 × √35 = 1.65 × 2 × 5.92 ≈ 20 units.
Reorder point = (5 × 35) + 20 = **195 units**. Order when on-hand plus on-order drops to 195.

- **Lead time is order-placed to goods-sellable**, including production, freight, customs and receiving — not the supplier's quoted production time. Stores that use the quoted time stock out every single cycle and blame the supplier.
- Higher service levels get expensive fast: the jump from 95% to 99% multiplies safety stock by 1.4 for a 4-point gain. Reserve 99% for A items and hero SKUs; C items can run at 90%.
- Seasonality breaks the average: compute average daily units over a window that matches the coming period, and for peak use last year's same weeks scaled by growth (`peak.md`).
- MOQ above the reorder quantity is a cash decision, not a stock decision: `MOQ × unit cost` is capital parked at 0% return until it sells (`Inventory Cash`).

## Inventory Cash and What to Stop Buying

| Measure | Formula | What it tells you |
|---|---|---|
| Turns | annual COGS ÷ average inventory value | How many times the money recycles; low turns with good margin still starves the business of cash |
| Days of cover | on-hand ÷ average daily units | Whether a SKU survives the next lead time |
| Sell-through | units sold ÷ units received, per period | Whether the last buy was the right size |
| GMROI | gross margin ÷ average inventory cost | Which SKUs earn their shelf space; the ranking that decides what to reorder |
| Dead stock | no sale in 90 days | Capital already lost; the only question is the exit price |

- **ABC classing**: A = top 20% of revenue (usually ~80% of it), B = next 30%, C = the tail. Count A items monthly, B quarterly, C annually. Applying one policy to all three wastes counting effort on items whose loss is a rounding error.
- Dead stock exits at whatever price clears it: bundle it with an A item, sell it to a liquidator, or write it off. Holding it costs storage plus the shelf space of something that sells; the sunk cost is already sunk (`pricing.md`).

## Counting: Cycle Counts Beat the Annual Stocktake

- A full annual count freezes the business for a day and produces one accurate moment per year. Cycle counting counts a slice continuously and produces accuracy you can trust in July.
- Count **A items monthly, B quarterly, C annually**; count blind (no expected quantity on the sheet) or the count becomes confirmation.
- The *variance* is the number that matters, not the new count. Persistent negative variance on one SKU is shrinkage, mispicking, or a bundle deducting the wrong component — three different fixes with the same symptom.
- Set the accuracy target at 98% of A-item locations. Below 95%, every downstream promise (availability, ship date, reorder) is unreliable and no algorithm fixes it.

## Backorders, Preorders and Allocation

| Mode | When it is right | Required guardrail |
|---|---|---|
| Backorder | Repeat customers, known restock date | Show the date on the product page and in the confirmation; charge on ship where the market allows |
| Preorder | New product, funding the buy | Cap the quantity at what the purchase order actually covers; a preorder overshoot is a refund campaign |
| Split shipment | Mixed cart, one line delayed | Second parcel's freight comes out of margin — ask the customer, and price the option (`fulfillment.md`) |
| Hold whole order | Customer prefers one delivery | Communicate the wait, and set a cancel-by date |

Allocation rule when stock is short across channels: fill by margin, not by order sequence — but never break a marketplace's shipping commitment, because the metric penalty outlives the margin gain (`marketplaces.md`).

## Multi-Location and 3PL

- Adding a second location doubles the ways stock can be wrong. Only do it when either freight cost or delivery time justifies it, and give each location its own count discipline.
- Allocation logic: ship from the location that can fulfil the whole order closest to the customer; splitting an order across warehouses costs a second parcel's freight and pick fee (`fulfillment.md`).
- With a 3PL, their system is the source of truth for *on-hand*, yours for *available to sell*. Reconcile weekly; the gap is receiving delays and damaged units, and it is always larger than either side expects.

## Stock-Related Failures and Their Real Causes

| Symptom | Real cause | Fix |
|---|---|---|
| Oversold despite stock showing available | Read-then-write decrement, or channel buffer smaller than one sync interval of sales | Atomic conditional write; recompute the buffer formula |
| Phantom stock: system says N, shelf says fewer | Returns marked restockable but never restocked; shrinkage; bundles deducting the wrong SKU | Cycle count with variance tracking; fix the bundle mapping (`catalog.md`) |
| Available drops with no sales | Abandoned cart reservations with no TTL | TTL plus sweeper, or no reservation at all |
| Constant stockouts on the same SKU | Reorder point computed on quoted lead time, or on a stale average | Recompute with the real lead time and current velocity |
| Cash tight while the warehouse is full | Ordering by MOQ convenience instead of GMROI | Reorder ranked by GMROI; liquidate dead stock |
| Stock correct in store, wrong on marketplace | Two systems own the number, or the channel's own buffer is stacking with yours | One owner; disable the channel's buffer or yours, never both |

**Write after inventory work**: supplier, lead time, MOQ and terms into `## Suppliers` (the person into the shared `contacts.md`); reorder points and any velocity or buffer change with its date into `## Suppliers` notes or `## Pain Points`; an oversell or count failure into `incidents/<year>.md` with units and revenue impact; the count cadence and dead-stock sweep into `## Due`; and a counting procedure, allocation policy or reorder model that finally worked into `artifacts/<kebab-name>.md` with its `## Boxes` line (`memory-template.md`).
