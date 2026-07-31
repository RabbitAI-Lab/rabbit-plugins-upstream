# Sports Inc payables — end-to-end (SportsLink → match → bill → post-on-match)

Sports Inc is a buying group that doesn't send individual vendor invoices; the
invoices live in the SportsLink API. This is the automated payables loop for
them: pull the invoices, reconcile each to its Odoo PO, correct price variances,
create the bill, **post it when its total matches the invoice** (else leave it
in draft), and mark the SI document consumed — with a human handling anything
flagged.

Three skills cooperate (this is the ports-and-adapters split in practice):

- **Source adapter** — `sportsinc-sportslink` (`sportslink.py`): fetch invoices,
  mark consumed. Customer-agnostic.
- **Workflow** — this skill: reconcile invoice ↔ PO, correct/escalate, create the
  draft bill. Source- and ERP-agnostic.
- **ERP adapter** — `drivethru-odoo` / `drivethru_mcp` (`paymatch.py`,
  `ap_create_vendor_bill` / `ap_post_vendor_bill`): the Odoo writes.

## Configured policy (BaconCo)

- **Posting: post on match, draft on mismatch.** Create the bill, then **post it
  when the bill total matches the invoice `expected_total` within tolerance**
  (`paymatch.py post`, backed by the guarded `ap_post_vendor_bill`). A bill that
  doesn't match is **left in draft** and escalated to the reviewer — never post a
  mismatch. When a run should stay hands-off (a human reviews before posting),
  skip the `post` step and leave every bill in draft.
- **On variance: auto-fix price, escalate qty/line.** A unit-price difference is
  treated as the SI invoice being authoritative — correct the PO line (like the
  pricing review), then bill. A **quantity / missing-line / total-structure**
  variance is **not** auto-fixed — escalate it (leave the SI doc active, raise an
  activity to the reviewer, create no bill).
- **Reviewer:** Zach Tucker (`reviewer_user_id: 6` in BaconCo's Odoo). Keep this
  in tenant config, not hard-coded in prose.
- **Tolerance:** a small **absolute** amount (a few cents, e.g. `0.02`) for the
  `expected_total` match check on both create and post — once prices are
  reconciled the SI docTotal should equal the computed bill to within rounding.
- **Chatter: internal log notes only.** Every PO note or escalation this loop
  posts (via `po_post_message`) is an internal Odoo **log note**, never a "Send
  message" — nothing here is emailed to the vendor.

## The exactly-once loop (do not deviate)

You are creating payables — double-billing is the cardinal sin. The SportsLink
`active`/historical flag is the idempotency mechanism; the sequence is fixed:

1. **Pull the inbox.** `sportslink.py list '{"active": true, "lines": true, "ediOnly": true}'`
   → normalised invoices that are not yet imported and carry line items.
2. **Process each invoice** (below). Create the draft bill in Odoo.
3. **Mark consumed only after the draft is created.**
   `sportslink.py mark-historical '{"siDocNumbers": [<si_doc_number>]}'`.
4. **Anything that fails or is escalated stays active** — it simply reappears on
   the next run. Never `mark-historical` a doc you didn't bill.

Never use the API's `moveToHistorical=true` GET flag — it marks on read, before
billing, so a crash drops the invoice. Belt-and-suspenders on the Odoo side:
before creating, check the PO's `invoice_count` / existing bills for the same
`supplier_doc_number`, in case a prior run's mark-historical failed after the
bill was created.

## Per-invoice procedure

For each normalised invoice from the adapter:

1. **Credit?** `is_credit: true` → do not bill. Escalate to the reviewer (vendor
   credit is a human decision). Leave active.
2. **No lines?** `has_lines: false` (scanned/OCR doc) → can't line-verify.
   Escalate to the reviewer for a header-only decision. Leave active.
3. **Find the PO.** `paymatch.py po-lines '{"po": "<po_number>"}'`. If it doesn't
   resolve (`found: false`) or the vendor doesn't line up → escalate, leave
   active.
4. **Reconcile lines** by (item/style, size, color): compare the invoice
   `net_price` to the PO line `price_unit`, and `qty_shipped` to `qty`.
   - **Price variance only** → `paymatch.py apply '{"po_id", "lines":[{"line_id",
     "price_unit": <invoice net_price>}]}'` (SI invoice is authoritative on
     price), then continue.
   - **Quantity / missing line / extra line / total-structure variance** →
     **escalate** (`paymatch.py questions '{"document_id"? , "question", ...}'`
     or a PO note + reviewer activity), leave the SI doc active, create no bill.
     (Sports Inc docs are API rows, not Documents-app files, so escalate on the
     PO chatter via `po_post_message` and/or a tracked task — there's no
     Documents folder to file.)
5. **Verify the SI charges tie out.** `docTotal` includes SI-specific charges
   (`si_upcharge`, `svc_handle`, `freight`, `sales_tax`, less `discount` /
   `freight_allowance`). Odoo's bill create() **auto-appends the Sports Inc fee
   lines** for `buying_group: "si"` POs — so pass the invoice `total` (docTotal)
   as `expected_total`; do not pre-add the SI fees yourself (you'll double them).
6. **Create the draft bill.**
   ```
   paymatch.py bill '{
     "po_id": <id>,
     "vendor_bill_number": "<supplier_doc_number or si_doc_number>",
     "invoice_date": "<invoice_date>",
     "expected_total": <invoice total>,
     "tolerance": 0.02,
     "reviewer_user_id": 6,
     "review_note": "SI SportsLink doc <si_doc_number>; matched PO <po_number>; <price fixes>."
   }'
   ```
   If the create returns `success: false` (the computed bill total missed
   `expected_total` beyond tolerance) → **do not** mark historical; escalate with
   the discrepancy and leave the doc active.
7. **Mark consumed.** On a successful draft, `sportslink.py mark-historical
   '{"siDocNumbers": [<si_doc_number>]}'`.
8. **Post it if it matches.** Post the draft (created bill `id` from step 6) so
   it hits the ledger — unless this is a draft-only run:
   ```
   paymatch.py post '{
     "bill_id": <created bill id>,
     "expected_total": <invoice total>,
     "tolerance": 0.02,
     "note": "SI SportsLink doc <si_doc_number>; matched PO <po_number>; posted on match."
   }'
   ```
   `post` re-checks the total and **refuses** (leaving the bill in draft) if it
   no longer matches within tolerance — treat a refusal as an escalation to the
   reviewer, exactly like a create mismatch. Posting an already-posted bill is a
   safe no-op (`already_posted: true`), so a re-run never double-posts.

## Scheduling & resilience

- **Run after ~10:30am ET** (SI processing completes first). This is a scheduled
  batch — a good fit for a cron/Routine trigger.
- The loop is self-healing: transient API failures retry (the adapter backs off);
  anything unresolved stays active and is retried next run; a run can be killed
  and restarted safely because nothing is marked consumed until its bill exists.
- **Notify on exceptions.** Summarise per run: posted N bills and left M in
  draft (list PO / amounts, posted vs draft), corrected P prices, escalated Q
  (with reasons), and any hard failures. Draft bills + escalations are the
  human's queue.

## Why an agent, not a custom Odoo module

The deterministic mechanics (auth, paging, normalisation, mark-historical) live
in `sportslink.py`; the ERP writes are single tool calls. The **agent** adds the
judgment (which variances to auto-fix vs. escalate, credit/scanned handling, PO
resolution) and the resilience (retry, anomaly detection, human-readable failure
notices) that a deterministic module would force you to hand-code and redeploy
per edge case. Keep the mechanics in scripts (out of the model's context) and the
judgment in the agent — the same division that makes the folder pricing review
cheap.

## Not testable without live access

`sportslink.py` needs `SPORTSINC_API_KEY` and reaches `api.sportsinc.com`, and
billing writes to live Odoo. Smoke-test in stages: (1) `list` read-only against a
recent date; (2) one `bill` on a known PO with `SPORTSINC_DRY_RUN=1` so nothing
is marked consumed; (3) confirm the draft in Odoo and the reviewer activity;
then enable `mark-historical`. Confirm the `vendor_bill_number` convention
(supplier vs. SI doc number) and the bill's vendor/partner for `buying_group:si`
POs during that first pass.
