---
name: drivethru-digitize-outsourcing
description: >
  Outsource embroidery digitizing end to end for BaconCo (Odoo). On a routine,
  read the `digitize.demand` records that are Ready to send out, pull the
  decoration's embroidery artwork + specs (production PNG, AI source file,
  height/width, thread-colour names, ship date), download the two files, decide
  rush from the ship date, submit the job to the outside digitizer via the
  `artworklady-digitizing` skill with a brief that states the size and colours,
  and — only on a confirmed submission — transition the demand to Outsource in
  Odoo. Talks to Odoo through the `drivethru_mcp` MCP server (digitize_demand_*
  + decoration_* tools) and hands the actual portal submission to the
  `artworklady-digitizing` skill. Idempotent: it only ever works Ready demands
  and marks them outsourced after a confirmed send, so a retry can't double-post.
  Use whenever the user asks to outsource digitizing, send embroidery jobs to
  the digitizer / Artwork Lady, or run the digitizing-outsourcing routine.
version: 0.1.0
emoji: 🧵
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
          `https://staging.baconco.com/drivethru_mcp/v1` (the MCP server exposed
          by the `drivethru_mcp` Odoo module, not the Odoo base URL). Test
          against STAGING, never production.
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

# Digitize outsourcing (Odoo → outside digitizer)

You run the embroidery **digitizing outsourcing** loop. Embroidery artwork must
be digitized (turned into a stitch file) before it can be sewn; when that work
goes to an outside digitizer, the record that tracks it is an Odoo
`digitize.demand`. Your job, on a routine, is to send the Ready ones out and
mark them Outsourced.

This is the **ERP half** of the loop. The **portal half** — actually posting the
job into the digitizer's web form — is the separate
[`artworklady-digitizing`](../artworklady-digitizing/SKILL.md) skill, which you
invoke. Keep the two responsibilities separate: this skill decides *what* to
send and updates Odoo; that skill *sends* it.

```
digitize_demand_search (Ready)  →  pull decoration art + ship date
      →  download the PNG + AI files to disk
      →  rush?  hold for human approval
      →  build the brief (H × W + thread colours)
      →  artworklady-digitizing submit (dry run, then confirm)
      →  on status=="submitted":  digitize_demand_outsource   (Ready → Outsource)
```

## Transport

Odoo is driven through the `drivethru_mcp` MCP server via `scripts/odoo_mcp.py`:

```bash
python3 scripts/odoo_mcp.py tools                        # discover tools + schemas
python3 scripts/odoo_mcp.py call <tool> '{"...":"..."}'  # call a tool
echo '{"...":"..."}' | python3 scripts/odoo_mcp.py call <tool>
```

Every call prints one JSON object, or `{"error": {...}}` with a non-zero exit.
`ODOO_MCP_URL` / `ODOO_MCP_TOKEN` must be set — if not, stop and tell the user.
**Run `tools` first and trust its `inputSchema` over any signature below.**

## The routine, step by step

### 1. Read the Ready queue

```bash
python3 scripts/odoo_mcp.py call digitize_demand_search '{}'
```

With no arguments this returns `state=ready` demands — the queue. Read the
roll-up (`sendable_count`, `blocked_count`, `rush_count`) and each row:

| Field | Use |
|---|---|
| `outsource_ready` / `blockers` | Only send rows where `outsource_ready` is true. Report the blocked ones (with their `blockers`), don't force them. |
| `decoration.id` | The job reference you send to the digitizer, and the record whose files you download. |
| `art.embroidery_png`, `art.ai_file` | The two files to download (`cdn_url` / `web_url`, `present`). |
| `art.height_in`, `art.width_in`, `art.color_names` | The brief — size and thread colours. |
| `earliest_ship_date`, `days_until_ship`, `is_rush` | The rush decision (step 3). |

**Skip anything already outsourced.** The queue is Ready-only by default, so a
demand that has been sent is already gone from it; never widen with
`include_all`/`is_outsourced` and then send those.

### 2. Download the two files

For each sendable demand, download the decoration's **embroidery production PNG**
and its **AI source file** to disk. The robust path is the `decoration_get_image`
tool, which returns the bytes when they're stored inline and the CDN url when
they've been offloaded:

```bash
python3 scripts/odoo_mcp.py call decoration_get_image \
  '{"model":"decoration","record_id":<DECO_ID>,"field":"embroidery_production_png"}'
python3 scripts/odoo_mcp.py call decoration_get_image \
  '{"model":"decoration","record_id":<DECO_ID>,"field":"decoration_ai_file"}'
```

* If the result has `data_base64`, decode it to a file (`emb_<id>.png`,
  `emb_<id>.ai`).
* If it has only `cdn_url` (binary offloaded) or the file is over the 20 MB
  transport guard, download that url — or the row's `art.*.web_url` — over HTTP
  (honouring `HTTPS_PROXY`).

If neither file can be fetched, that demand is not sendable — report it and move
on. See [`references/routine.md`](references/routine.md) for the download
details and file naming.

### 3. Rush → hold for human approval

Decide rush from the ship date: a row is rush when `is_rush` is true (ship date
within the window) — reason over `days_until_ship` yourself if you disagree.

**Rush demands are NOT sent automatically.** Escalate them for human approval:
list each rush demand (id, decoration, customer, `earliest_ship_date`,
`days_until_ship`) and stop short of submitting it. Send it only once a human
explicitly approves — e.g. they re-run you scoped to those specific demand ids,
or tell you to include them. (This gate is temporary and will be removed later.)

Non-rush, `outsource_ready` demands proceed without approval.

### 4. Build the brief

The `message` you send the digitizer must clearly state the **height × width and
the thread colours**, e.g.:

```
Embroidery digitizing. Size: 3.5in W × 2.0in H. Thread colours: White, Navy, Red.
Left chest. Digitize to DST.
```

Build it from `art.width_in`, `art.height_in`, and `art.color_names`. Add
placement/decoration context if the row carries it.

### 5. Submit to the digitizer (dry run, then confirm)

Hand the actual submission to the **`artworklady-digitizing`** skill. Its creds
(`ARTWORKLADY_USERNAME`/`PASSWORD`, and, behind the egress proxy, the TLS SPKI
pins) are that skill's concern — if it exits `config_error`, stop and tell the
user to configure them; never ask for them in chat.

**Always dry-run first** (default `confirm:false`) to validate the fill, then
submit with `confirm:true`:

```bash
python3 <artworklady-digitizing>/scripts/artworklady_digitizing.py submit '{
  "job_reference": "<DECO_ID>",
  "turnaround": "nextday",
  "file_types": ["dst"],
  "files": ["/abs/emb_<id>.png", "/abs/emb_<id>.ai"],
  "message": "Embroidery digitizing. Size: 3.5in W × 2.0in H. Thread colours: White, Navy. …"
}'
```

* `job_reference` = the **decoration id** (what that skill expects).
* `files` — the PNG first (the mandatory upload slot), the AI second. Both go up.
* `turnaround` — `nextday` by default; `rushorder` for an approved rush;
  `sameday` only when the ship date is immediate.
* Success is judged on the real submit response (HTTP 200 → `status:"submitted"`).
  Treat **only** `status:"submitted"` as sent — never a `dry_run`, an `error`, or
  the sight of `/thanks`.

### 6. Mark it Outsourced — exactly once

**Only** on `status:"submitted"`, transition the demand:

```bash
python3 scripts/odoo_mcp.py call digitize_demand_outsource \
  '{"demand_id": <DEMAND_ID>, "note": "Artwork Lady — job_reference <DECO_ID>, submitted <ISO time>"}'
```

This moves the demand `ready → outsource`, stamps `outsource_date`, and flags
`is_outsourced` on the demand and the decoration. Do this **immediately after**
each confirmed submission, one demand at a time.

`digitize_demand_outsource` is **idempotent** (a demand already outsourced comes
back as `already_outsourced`), but the window between a confirmed send and this
call is the one risk: the portal returns no id, so a resend can't be detected.
If this call fails after a confirmed submit, **stop and report it** — do not
re-submit the job.

## Idempotency & exactly-once (read this)

* Work **only** `state=ready` demands. Once sent they're at `outsource` and drop
  out of the default queue, so a re-run never re-sends them.
* Submit **first**, mark outsourced **after** a `submitted` result — and put the
  outsource call right after the submit for each demand, so a crash leaves the
  demand Ready (correct: it was never actually sent) rather than sent-but-unmarked.
* The portal does **not** dedupe and returns no id. The demand's state + the
  chatter `note` (job reference + submitted-at) are your audit trail.

## A pass, end to end

1. `digitize_demand_search '{}'` → the Ready queue.
2. If `sendable_count` is 0, report `blocked_count` + top blockers and stop.
3. Split rush (`is_rush`) from the rest; escalate rush for approval (step 3).
4. For each approved, sendable demand: download PNG + AI → build the brief →
   `artworklady-digitizing submit` dry run → confirm → `digitize_demand_outsource`.
5. Report: how many outsourced, which were held for rush approval, which were
   blocked (and why).

## Errors

- `config_error` (exit 2) — `ODOO_MCP_URL` / `ODOO_MCP_TOKEN` missing (this skill),
  or `ARTWORKLADY_USERNAME`/`PASSWORD` missing (the digitizing skill).
- `connection_error` — Odoo unreachable or key rejected.
- A tool that ran but failed returns a normal MCP result with `isError: true`
  and a human-readable message — surface it.
- `portal_error` from the digitizing skill — the submit did not return HTTP 200;
  the demand stays Ready and is retried next pass. Do NOT mark it outsourced.

## References

- [`references/routine.md`](references/routine.md) — the download details, the
  turnaround/rush mapping, file naming, and the exactly-once reasoning in full.
