---
name: drivethru-production-scheduler
description: Schedule MRP production batches in Odoo (BaconCo) — the fluid shop-floor scheduler. Periodically read open `mrp.production.batch` records, rank them by the shop rule (event date → ship date → whatever is ready), pick an eligible machine for each, and write the schedule back. Reads purchase orders + vendor tracking to know when goods will land, and uses receipt-readiness as guidance (jobs generally shouldn't start before their components are in) that it refines from human feedback. Handles rush orders dropped in mid-day by re-ranking. Talks to Odoo through the `drivethru_mcp` MCP server. Use whenever the user asks to schedule/plan production, build a machine schedule, slot in a rush order, or check whether a batch's goods are in yet.
version: 0.1.0
emoji: 🗓️
homepage: https://www.odoo.com
metadata:
  openclaw:
    requires:
      env: [ODOO_MCP_URL, ODOO_MCP_TOKEN]
      bins: [python3]
    primaryEnv: ODOO_MCP_TOKEN
    envVars:
      ODOO_MCP_URL:
        required: true
        description: >
          Full URL of the Odoo MCP endpoint, e.g.
          `https://odoo.example.com/drivethru_mcp/v1` (the MCP server exposed by
          the `drivethru_mcp` Odoo module, not the Odoo base URL).
      ODOO_MCP_TOKEN:
        required: true
        description: >
          The `drivethru.mcp_key` value from the Odoo `drivethru_mcp` module,
          sent as `Authorization: Bearer`. Treat as a secret; never paste into
          chat.
    install:
      uv:
        - mcp>=1.9.0
---

# Production scheduler (Odoo MRP batches)

You schedule the shop floor. Each open `mrp.production.batch` is a job that
needs a **machine** and a **time slot**. Your job, per batch, is to choose:

- `primary_workcenter_id` — the machine
- `production_center_id` — derived from the machine if you omit it
- `date_planned_start` / `date_planned_finished` — the slot

You do this against a live, changing queue: **rush orders drop in frequently**,
so treat every pass as a re-plan, not a one-shot.

This skill drives the Odoo **`drivethru_mcp`** MCP server. The transport is
`scripts/odoo_mcp.py`:

```bash
python3 scripts/odoo_mcp.py tools                       # discover tools + schemas
python3 scripts/odoo_mcp.py call <tool> '{"...":"..."}'  # call a tool
echo '{"...":"..."}' | python3 scripts/odoo_mcp.py call <tool>
```

Every call prints one JSON object, or `{"error": {...}}` with a non-zero exit.
`ODOO_MCP_URL` / `ODOO_MCP_TOKEN` must be set — if not, stop and tell the user.
**Run `tools` first and trust its `inputSchema` over any tool signature below.**

## The scheduling rule (in priority order)

Schedule batches in this order — this is exactly what `production_schedule_queue`
returns, already ranked:

1. **Event date** (`event_date`) — the customer's in-hands/event date. The
   hardest deadline. Earliest first.
2. **Ship date** (`ship_date`) — the requested ship (commitment) date. Breaks
   ties / used when there's no event date. Earliest first.
3. **Whatever is ready** — among equal dates, batches that are **fully
   received** (`is_fully_received`) go first, because they can run now.

Never re-derive this ordering by hand — call `production_schedule_queue` and
work its `rank` order. When a rush order lands, just call it again; the new
batch appears at its correct rank.

## Receipt readiness: a rule of thumb, not a wall

As a general starting point, a job usually shouldn't start before its
components are received — starting early strands it on the floor. **But the
tools do not enforce this.** You can schedule a start on a not-yet-received
batch whenever it makes sense; the readiness signals are there for you to reason
with, not to block you.

- Check `is_fully_received` and `expected_ready_date` (from the supply picture —
  see below) before you commit a start.
- When a batch isn't in yet, prefer to schedule its start **on or after**
  `expected_ready_date` — unless there's reason to slot it earlier.
- This is guidance you **refine from feedback**. When a human corrects a call
  ("go ahead and set batch 88 for 8am, the blanks land first thing" / "never
  start the embroidery batches before the thread's in"), remember it — those
  learned preferences, not a hard-coded rule, are what should shape future
  decisions.

## Which machine can run a job

The tools pre-filter eligible machines for you. On `production_get_batch`, use
`eligible_workcenters` (each includes its current `scheduled_batches` load, so
you can find a real gap) and `eligible_production_centers`. The rules behind the
filter — decoration-method match, `allow_production_batch`, `minimum_piece_count`,
capacity (`units_per_hour`, `min/max_mo_quantity`) — are in
[`references/scheduling_algorithm.md`](references/scheduling_algorithm.md).

## Knowing when goods will arrive

`production_batch_supply` (or the `supply` block on `production_get_batch`) is
the "when can this start?" answer for one batch:

- `purchase_orders` — the POs feeding it (`status_from_vendor`, `date_planned`,
  per-line `qty_received`).
- `receipts` — the incoming transfers, each with `scheduled_date`,
  `vendor_tracking` (carrier, tracking number, status, `delivery_date`), and an
  `expected_arrival`.
- Readiness rollup: `is_fully_received`, `receipt_status`,
  **`expected_ready_date`** (the latest arrival across open receipts = when the
  whole batch is on hand), `has_unknown_eta`, `blocked_on_receipt`.

When goods are late or the ETA is unknown (`has_unknown_eta`), surface it — that
batch can't be started and may need purchasing/vendor follow-up.

## Reading any field you need

The curated payloads cover scheduling. For anything else on
`mrp.production.batch`, `purchase.order`, `stock.picking`, `decoration`,
`mrp.production`, `vendor.tracking`, etc., use the generic **read-only** tools:
`mfg_list_models` → `mfg_fields {"model": ...}` → `mfg_read {"model": ...,
"ids"|"domain": ..., "fields": ...}`.

## Tool cheat-sheet (verify with `tools`)

| Purpose | Tool |
| --- | --- |
| Ranked worklist (start here each pass) | `production_schedule_queue` |
| Full planning snapshot (batches + machine load + reference data) | `production_overview` |
| One batch: decorations, eligible machines, MOs, `supply` | `production_get_batch` |
| One batch: supply/receipt/tracking only ("can it start yet?") | `production_batch_supply` |
| Write one schedule decision | `production_schedule_batch` |
| Write many at once (atomic by default) | `production_bulk_schedule` |
| Run Odoo's native slot allocator | `production_plan_batch` |
| Machines + their scheduled load | `production_list_workcenters` / `production_get_workcenter` |
| Reference data | `production_list_production_centers`, `production_list_decoration_methods` |
| Read any field on any mfg model | `mfg_list_models`, `mfg_fields`, `mfg_read` |

## A scheduling pass, end to end

1. **Rank.** `production_schedule_queue` (add `{"include_eta": true}` to see
   expected-ready dates for the not-yet-received batches; `{"unscheduled_only":
   true}` for just the backlog).
2. **Inspect** the batches you'll place: `production_get_batch` for eligible
   machines + their load and the `supply` block, or `production_batch_supply`
   when you only need readiness.
3. **Place ready batches** onto an eligible machine in a real gap, honoring the
   priority order. Use `production_bulk_schedule` for a whole day (`atomic:
   true` rolls back the batch of writes on any error).
4. **Unreceived batches:** by default, schedule the start on/after
   `expected_ready_date`, or leave it unscheduled and flag the blocker — but
   this is a judgment call, not a wall, and prior human feedback may say
   otherwise for this shop/decoration type.
5. **Rush order?** Re-run step 1 and reflow — don't hand-insert.

## Working inside an Odoo Discuss conversation

You may be answering a **person in an Odoo Discuss DM** (your replies post back
into their thread):

- Be concise and conversational — summarize the plan (batch → machine → slot),
  don't dump raw JSON. Surface a tool error's human-readable message.
- **Confirm before writes.** Scheduling changes live Odoo data. State exactly
  what you'll place where, then call the write tool. Never invent ids — look
  them up first.
- Reach for `docs_get {"slug": "production_scheduling"}` (an Odoo operator doc)
  for the shop's authoritative rules.

## Errors

- `config_error` (exit 2) — `ODOO_MCP_URL` / `ODOO_MCP_TOKEN` missing.
- `invalid_arguments` (exit 2) — bad CLI usage or non-JSON arguments.
- `connection_error` — Odoo unreachable, transport error, or key rejected.
- A tool that ran but failed returns a normal MCP result with `isError: true`
  and a human-readable message — surface it.

## References

- [`references/scheduling_algorithm.md`](references/scheduling_algorithm.md) —
  the ranking, machine-eligibility, and reflow algorithm in detail (with
  pseudocode).
- [`references/receipt_readiness.md`](references/receipt_readiness.md) —
  reading the supply/tracking picture and the expected-arrival reasoning behind
  the "usually don't start before received" guideline.
