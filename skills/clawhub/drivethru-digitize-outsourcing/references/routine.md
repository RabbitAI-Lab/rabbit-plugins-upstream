# Digitize outsourcing — routine details

The full detail behind the six steps in `SKILL.md`. Read this when the happy
path isn't enough.

## The `digitize.demand` workflow

```
not_ready → ready → outsource → sew_out → done
```

* **not_ready ⇄ ready** flips automatically in Odoo from the decoration's
  readiness (production PNG, thread colours, non-zero size) plus a linked sale
  order. You never write these — you read `state=ready`.
* **ready → outsource** is the only transition you make, via
  `digitize_demand_outsource`. Once a demand is at `outsource` (or beyond) Odoo
  freezes the readiness recheck, so it can't be dragged back to Ready.
* **sew_out / done** happen when the digitized file comes back and is uploaded
  in Odoo — not your concern.

So the queue you work is exactly `state=ready`, and marking a demand
`outsource` is what removes it from that queue.

## Reading a row

`digitize_demand_search` enriches every row from the linked decoration. The
fields that matter to the routine:

- `id` — the **digitize.demand** id (what you pass to `digitize_demand_outsource`).
- `decoration.id` — the **decoration** id (the `job_reference`, and the
  `record_id` you download files from).
- `outsource_ready` (bool) + `blockers` (list) — send only when true; otherwise
  report the blockers. Common blocker: `no AI source file on the decoration`
  (the AI is not part of Odoo's Ready predicate but the digitizer needs it, so a
  demand can be Ready yet not sendable).
- `art.embroidery_png` / `art.ai_file` — each `{present, cdn_url, web_url}`.
- `art.height_in`, `art.width_in`, `art.color_names` (list of thread-colour
  names) — the brief.
- `earliest_ship_date`, `days_until_ship`, `is_rush`, `rush_threshold_days`.

## Downloading the PNG + AI

Prefer `decoration_get_image` — it handles both storage shapes:

```bash
python3 scripts/odoo_mcp.py call decoration_get_image \
  '{"model":"decoration","record_id":<DECO_ID>,"field":"embroidery_production_png"}'
```

Fields: `embroidery_production_png` and `decoration_ai_file`.

- **Inline bytes** → the result has `data_base64`. Decode it and write to disk.
- **CDN offloaded** (production usually offloads binaries) → the result has
  `cdn_url` and no bytes, OR the file exceeds the 20 MB transport guard and the
  tool refuses it. In both cases download `cdn_url` (or the search row's
  `art.<file>.web_url`) over HTTP. Honour `HTTPS_PROXY`; the CDN link is a direct
  file url like the one `digitize.demand` itself fetches server-side.
- **Neither works** → not sendable. Report and skip; don't submit a half job.

Suggested local names, so a crash leaves obvious artefacts:
`emb_<demand_id>.png`, `emb_<demand_id>.ai`. Use absolute paths in the submit
call. Verify each file is non-empty before submitting.

## Rush → hold for approval (temporary gate)

A row is rush when `is_rush` is true — the ship date is within
`rush_threshold_days` (5 by default; Odoo env `DRIVETHRU_DIGITIZE_RUSH_DAYS`).
Reason over `days_until_ship` if you want to second-guess it (e.g. a negative
value is already overdue).

Rush demands are **held for human approval** and not auto-submitted. Surface
them as a short list — demand id, decoration, customer, `earliest_ship_date`,
`days_until_ship` — and submit one only after a human explicitly approves it
(they re-run you scoped to those ids, or say to include them). This gate is
temporary and will be removed once the flow is trusted.

## Turnaround mapping

The digitizer's `turnaround` is `sameday | nextday | rushorder`. Default map:

| Situation | `turnaround` |
|---|---|
| Non-rush (the normal path) | `nextday` |
| Approved rush | `rushorder` |
| Ship date is immediate (approved) | `sameday` |

Turnaround is about how fast the digitizer works, which tracks ship urgency —
adjust per demand and defer to any human instruction.

## The brief (`message`)

State the size and colours plainly:

```
Embroidery digitizing. Size: <width>in W × <height>in H.
Thread colours: <comma-separated art.color_names>. Digitize to DST.
```

Add placement/garment context from the row when present. `file_types` defaults
to `["dst"]` (the stitch file we want back).

## Exactly-once

The portal returns HTTP 200 with an **empty body** — no id — so nothing can
correlate a resubmission. The discipline that makes this safe:

1. Work only `state=ready`. A sent demand is at `outsource` and gone from the queue.
2. Per demand: submit (`confirm:true`) → on `status:"submitted"` immediately call
   `digitize_demand_outsource`. Don't batch the sends and mark them all at the end.
3. If `digitize_demand_outsource` fails right after a confirmed submit, **stop and
   report** — the job was sent; a human must reconcile it. Do not resend.
4. A crash *before* the submit returns leaves the demand Ready — correct, since it
   was never sent — and it's retried next pass.

`digitize_demand_outsource` is idempotent (already-sent → `already_outsourced`),
and its `note` records the job reference + submitted-at in the demand's chatter
for the audit trail.

## Worked example (one demand)

```bash
# 1. queue
python3 scripts/odoo_mcp.py call digitize_demand_search '{}'
#   → row: id=812, decoration.id=4590, outsource_ready=true, is_rush=false,
#          art.width_in=3.5, art.height_in=2.0, art.color_names=["White","Navy"]

# 2. files
python3 scripts/odoo_mcp.py call decoration_get_image \
  '{"model":"decoration","record_id":4590,"field":"embroidery_production_png"}'  # → data_base64 or cdn_url
python3 scripts/odoo_mcp.py call decoration_get_image \
  '{"model":"decoration","record_id":4590,"field":"decoration_ai_file"}'
#   → write emb_812.png, emb_812.ai

# 3. not rush → proceed. 4. brief built from the art fields.

# 5. dry run, then confirm (artworklady-digitizing skill)
python3 <artworklady-digitizing>/scripts/artworklady_digitizing.py submit '{
  "job_reference":"4590","turnaround":"nextday","file_types":["dst"],
  "files":["/abs/emb_812.png","/abs/emb_812.ai"],
  "message":"Embroidery digitizing. Size: 3.5in W × 2.0in H. Thread colours: White, Navy. Digitize to DST."}'          # confirm:false → dry_run
#   …then the same with "confirm":true → status:"submitted"

# 6. mark outsourced (only on submitted)
python3 scripts/odoo_mcp.py call digitize_demand_outsource \
  '{"demand_id":812,"note":"Artwork Lady — job_reference 4590, submitted 2026-09-18T14:03Z"}'
```
