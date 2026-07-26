# Scheduling algorithm

The data model and the algorithm behind a scheduling pass. The Odoo
`drivethru_mcp` tools do the heavy lifting (ranking, machine eligibility,
receipt readiness) server-side; this is the reasoning you layer on top.

## Entities

| Entity | Odoo model | Meaning |
| --- | --- | --- |
| Production batch | `mrp.production.batch` | The scheduling unit — a batch of MOs sharing a machine + slot. |
| Manufacturing order | `mrp.production` | One order inside a batch. |
| Workcenter | `mrp.workcenter` | A machine (e.g. "Manual Press A"). |
| Production center | `production.center` | A group of workcenters (e.g. "Screen Print Floor"). |
| Decoration | `decoration` | An imprint on a product, carrying artwork/readiness. |
| Decoration method | `decoration_method` | A process type (Screen Print, Embroidery, DTF, Heat Press). |
| Purchase order | `purchase.order` | A vendor order for the batch's components. |
| Receipt | `stock.picking` (incoming) | Goods arriving for the batch. |
| Vendor tracking | `vendor.tracking` | Carrier / tracking number / status / delivery date. |

## The four writable scheduling fields

| Field | Notes |
| --- | --- |
| `primary_workcenter_id` | The machine. Must be eligible (see below). |
| `production_center_id` | Derived from the machine if omitted. |
| `date_planned_start` | ISO datetime. Not gated — mind receipt readiness (see `receipt_readiness.md`). |
| `date_planned_finished` | Auto-computed as `start + Σ MO.duration_expected` unless set explicitly. |

## Priority ranking

`production_schedule_queue` returns open batches already sorted by the shop
rule. The sort key is:

```
key(batch) = (
    event_date or FAR_FUTURE,   # 1. event date, earliest first
    ship_date  or FAR_FUTURE,   # 2. ship date, earliest first
    0 if is_fully_received else 1,   # 3. ready jobs first
    id,                          # stable tiebreak
)
```

So: event dates drive everything; ship date breaks ties or orders the
event-less batches; among identical dates, the batch whose goods are in gets
the slot. Undated batches sink to the bottom. Work the returned `rank` order.

Rush handling is falling out of this for free: a rush batch with a near event
or ship date re-ranks to the top the next time you call
`production_schedule_queue`. Never hand-insert a rush job into a stale plan —
re-rank and reflow.

## Machine eligibility

A batch may only be assigned a machine that can actually run its work.
`production_get_batch` pre-computes `eligible_workcenters` and
`eligible_production_centers`, but the rules are:

- The batch's methods = its `decoration_ids` → `decoration_method`.
- A **production center** is eligible when its `decoration_method_ids` overlaps
  the batch's methods **and** `minimum_piece_count <= batch.piece_count`.
- A **workcenter** is an eligible `primary_workcenter_id` when it is `active`,
  `allow_production_batch = true`, its `decoration_method_ids` overlaps the
  batch's methods, and it belongs to an eligible production center.
- Respect capacity: `units_per_hour`, `min_mo_quantity`, `max_mo_quantity` on
  the workcenter; the batch's `calculated_duration` (minutes); and the machine's
  current `scheduled_batches` (inlined on the workcenter payloads) so you slot
  into a real gap rather than double-booking.

Also worth checking before committing a start: `art_status` (artwork done?),
`is_screens_burned` (screens ready?), `licensing_hold` (CLC approval pending?).
A batch that's blocked upstream shouldn't jump the queue onto a machine.

## A pass in pseudocode

```
queue = call("production_schedule_queue", {"include_eta": true})["queue"]

for batch in queue:                       # already in priority rank
    if not batch["is_fully_received"]:
        # Goods aren't all in yet. Default: start on/after the ETA — but this
        # is judgment (and learned shop preferences), not a hard block.
        if batch.get("expected_ready_date"):
            target_start = max(now, batch["expected_ready_date"])
            # (only place it now if you also have a machine gap then)
        else:
            flag_blocked(batch)            # unknown ETA — chase purchasing
            continue

    detail = call("production_get_batch", {"batch_id": batch["id"]})
    machine = pick_machine(detail["eligible_workcenters"])  # capacity + open gap
    if machine is None:
        flag_no_capacity(batch)
        continue

    slot = first_open_gap(machine, duration=detail["calculated_duration_minutes"])
    plan.append({
        "batch_id": batch["id"],
        "primary_workcenter_id": machine["id"],
        "date_planned_start": slot.start,
    })

call("production_bulk_schedule", {"atomic": true, "updates": plan})
```

`pick_machine` / `first_open_gap` are your judgment calls over the pre-filtered
candidates and their `scheduled_batches`. Keep the batch of writes atomic so a
single rejection doesn't leave a half-applied day.

## After writing

- `production_bulk_schedule` returns `results` (with `changes_applied`) and, in
  non-atomic mode, per-entry `errors`. Read them back.
- Optionally run `production_plan_batch` to let Odoo's native slot allocator
  finalize workorder timing (requires `primary_workcenter_id` already set).
- `is_scheduled_late` / `is_scheduled_close` on a batch tell you if the slot you
  chose still misses/nears the ship date — re-check after a reflow.
