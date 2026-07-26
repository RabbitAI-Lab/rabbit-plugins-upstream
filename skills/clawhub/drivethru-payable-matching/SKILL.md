---
name: drivethru-payable-matching
description: >
  Payable matching for BaconCo — reconcile vendor documents in Odoo's Documents
  app against their purchase orders and correct incorrect PO line pricing. Use
  for requests like "check the Purchasing folder against the POs and fix the
  pricing", "match the vendor invoice / order confirmation / acknowledgement to
  its PO", "AP price matching / invoice-to-PO matching / three-way match",
  "reconcile the vendor documents and mark the POs checked", or "go through the
  Purchasing folder". The flow: read every document in a Documents-app folder
  (extracting text out-of-context so large batches don't bloat the context
  window — falling back to a page render + OCR/vision for scanned or
  custom-encoded PDFs that won't extract as text), pull the PO number / line
  items / unit prices from each, compare to the purchase order line by line,
  correct any wrong `price_unit`, post a "checked" log note on the PO (internal,
  never a "Send message"), and FILE every document into the `Matched` or
  `Questions` subfolder — escalating genuine questions to a reviewer (default
  Zach Tucker). Also runs the buying-group payables flow: pull Sports Inc
  invoices from the SportsLink API (via the `sportsinc-sportslink` adapter),
  reconcile each to its PO, correct price variances, and create the DRAFT vendor
  bill for a human to post ("get the Sports Inc invoices and bill them", "match
  the SI invoices to POs and create the payables"). Runs at volume on a low-cost
  model. Driven by the Odoo `drivethru_mcp` MCP server; complements the broader
  `drivethru-odoo` skill.
version: 0.6.0
emoji: 🧾
homepage: https://www.odoo.com
metadata:
  openclaw:
    requires:
      env: [ODOO_MCP_URL, ODOO_MCP_TOKEN]
      bins: [python3, uv]   # uv powers the scripts' self-bootstrap fallback
    primaryEnv: ODOO_MCP_TOKEN
    envVars:
      ODOO_MCP_URL:
        required: true
        description: >
          Full URL of the Odoo MCP endpoint, e.g.
          `https://odoo.example.com/drivethru_mcp/v1` — the MCP server exposed by
          the `drivethru_mcp` Odoo module, not the Odoo base URL.
      ODOO_MCP_TOKEN:
        required: true
        description: >
          The `drivethru.mcp_key` value from the `drivethru_mcp` module, sent as
          `Authorization: Bearer`. Treat as a secret; never paste into chat.
    install:
      uv:
        - mcp>=1.9.0
        - pymupdf>=1.24   # primary local PDF text extraction + page rasterization:
                          # honours ToUnicode/Type3 (custom-encoded) fonts pypdf can't
                          # read, and renders needs_vision docs without system poppler
        - pypdf>=4.0      # last-resort text-extraction fallback
---

# Payable matching (Purchasing folder → purchase orders)

Reconcile vendor documents against their purchase orders and fix PO line
pricing. A **vendor document** is an order confirmation, shipment
acknowledgement, or invoice filed in the Documents app's **Purchasing** folder;
its authority for what BaconCo will be billed is the vendor's own numbers.

The task, per document: read it → extract the **PO number, line items, and unit
prices** → find the PO in Odoo → compare **line by line** → correct any wrong
`price_unit` → post a "checked" note on the PO → **file the document** into
`Matched` (reconciled) or `Questions` (needs a human). Nothing stays in the
inbox.

This changes live financial data (PO prices, chatter, activities). The
standing request *"review the Purchasing folder and fix the pricing"*
authorizes the corrections and the "checked" notes; still, **only correct a
line when the vendor document unambiguously supports it** — when in doubt, route
it to Questions rather than guessing.

## Always use Log note, never Send message

Every annotation you leave on a PO or a document — the "checked" note, a
partial-shipment note, a question, any comment — MUST be an internal **Log
note**, never a **Send message**. In Odoo chatter, "Send message" notifies the
record's followers and can **email the vendor or customer**; a Log note stays
internal. These vendor documents are BaconCo's own AP working notes — nothing
here should ever leave Odoo as an email.

The helper's `matched` / `questions` commands and the `po_post_message` /
`documents_post_message` MCP tools post internal **log notes** — use them. Do
**not** reach for any "send message", email, or notify-followers path when
annotating a PO or document, and if a tool ever exposes a note-vs-message
choice, always choose the internal note.

## How you reach Odoo (runtime-aware — read this first)

This skill drives the same Odoo **`drivethru_mcp`** MCP as `drivethru-odoo`, and
`ODOO_MCP_URL` / `ODOO_MCP_TOKEN` are already configured. **Never say you "can't
reach Odoo" or "don't have the tools in this thread" and guess instead — call a
tool, or state the exact call you tried and the error you got.**

- **Native / callable MCP tools (preferred, no shell needed).** If the Odoo
  tools are attached to you natively, **call them directly** — e.g.
  `documents_list_folders {"name": "Purchasing"}`, whose `document_count` is how
  many documents are waiting to be matched. They may be **deferred** — if your
  runtime lazy-loads tools, search your tools for `documents_search`,
  `ap_search_purchase_orders`, `ap_update_po_lines`, `po_post_message`,
  `po_get_messages`, etc. and load them before calling. "I don't see them yet"
  is not "I don't have them."
- **Shell (`scripts/paymatch.py`) — only if you have a shell.** The helper below
  is a context-economy optimization (bulk PDF text extraction, one call per
  folder); prefer it for large batches when a shell is available.
- **Not connected at all?** Attaching the `drivethru_mcp` MCP natively — or
  giving the agent a shell — is an **operator step**; env vars alone don't
  attach the tools. See `drivethru-odoo`'s **Operator setup** and
  **Troubleshooting** sections before concluding you can't reach Odoo.

## The engine: `scripts/paymatch.py` (keep the work out of context)

Reading PDFs is the expensive part. `documents_get` returns each file as
**base64**, and a multimodal PDF reader adds a **page image** — both dwarf the
few hundred characters of text that matter. Do that per file across a folder,
many times a day, and the context window fills with bytes and renders (and the
token bill balloons). So **never loop `documents_get`/a PDF reader over the
folder.** Use the helper, which does the heavy, deterministic work locally and
returns only what the model needs.

```bash
# 1. Read the whole folder as TEXT (no base64, no render) — ONE call
python3 scripts/paymatch.py extract '{"folder": "Purchasing"}'

# 1b. Any document flagged needs_vision (scanned or custom-encoded) → render its
#     page(s) to PNG (+ OCR if tesseract is present), then read the image(s)
python3 scripts/paymatch.py render '{"document_id": 485}'

# 2. Per document: pull the PO trimmed to matchable fields (incl. qty_received)
python3 scripts/paymatch.py po-lines '{"po": "P13189"}'

# 2b. Partial shipment? Read the PO's prior log notes to see what's already checked
python3 scripts/paymatch.py notes '{"po": "P13137"}'

# 3. Correct any wrong line(s) in one call (PO must be confirmed)
python3 scripts/paymatch.py apply '{"po_id": 13145, "lines": [{"line_id": 40941, "price_unit": 11.94}]}'

# 4a. Clean/fixed → post the checked LOG NOTE AND file to Matched (one call)
python3 scripts/paymatch.py matched '{"po_id": 13145, "document_id": 481, "body": "Pricing checked against SanMar Order Confirmation ... corrected size S $13.94→$11.94."}'

# 4b. Genuine question → raise a reviewer activity AND file to Questions (one call)
python3 scripts/paymatch.py questions '{"document_id": 485, "question": "Totals don't reconcile — please review.", "reviewer": "Zach Tucker"}'
```

Every command prints one JSON object, or `{"error": {...}}` with a non-zero
exit. Requires `ODOO_MCP_URL` / `ODOO_MCP_TOKEN` (if missing, the script exits
with `config_error` — stop and tell the user to configure them; never ask for
the key in chat).

**Dependencies self-install.** The script's deps (`mcp`, `pymupdf`, `pypdf`)
are declared in the frontmatter `install.uv`, but not every OpenClaw host honors
it — so `scripts/_bootstrap.py` ensures them at startup: on a missing import it
builds a cached `uv` venv (in `$PAYMATCH_DATA_DIR` or `~/.drivethru/paymatch`)
and re-execs. Hosts that pre-install make it a no-op; otherwise the **first run
pays a one-time install**, then it's cached. So a `ModuleNotFoundError` (e.g.
`No module named 'anyio'`) is not a dead end — it self-heals on the next run, as
long as **`uv` is on PATH**. If the script exits saying `uv` is missing, that's
an operator step (install `uv`, or the host must honor `install.uv`); fall back
to the native `documents_*` / `ap_*` / `po_*` MCP tools in the meantime.

If you have **no shell** (e.g. a chat agent), use the native `documents_*` /
`ap_*` / `po_*` MCP tools directly — they do everything the script does; the
script is only a context-economy wrapper for bulk PDF extraction. Working
natively, still fetch **one document at a time** and drop the base64 — never
pull a whole folder's bytes into context. (If creds are unset or the MCP isn't
attached, see `drivethru-odoo`'s Troubleshooting — don't guess.)

## Procedure

1. **Read the folder once.** `paymatch.py extract '{"folder": "Purchasing"}'`
   → `documents[]` with `document_id`, `name`, and extracted `text`. Work from
   that text. Extraction runs PyMuPDF → `pdftotext` → `pypdf` and **quality-gates
   the result**, so a document flagged `needs_vision: true` is one no text pass
   could read reliably — either scanned/image-only, OR a **custom-encoded PDF**
   (Type3 / no usable ToUnicode — e.g. some Charles River Apparel shipment
   confirmations) that renders perfectly but extracts as empty/garbage.
   **Do not escalate a `needs_vision` document as "unreadable" — read it.**
   Run `paymatch.py render '{"document_id": <id>}'` to rasterise its page(s) to
   PNG (plus OCR text when `tesseract` is installed), then read the image(s)
   with vision to pull the PO number and line items and match as normal. (No
   shell? Fetch with `documents_get {"document_id"}` and read the bytes with a
   vision reader — same idea.) The old failure mode — "couldn't get a reliable
   PO number from unattended extraction, please review manually" — is exactly
   this case, and the render/vision fallback resolves it instead of punting.

2. **Extract from each document's text (not its filename).** The PO number is
   **inside** the document; a filename may show the vendor's order number
   instead (e.g. `Order Acknowledgement 48482500.pdf` whose real PO is
   `P13183`). Capture item/style, color, size, quantity, and **unit price** per
   line.

3. **Pull the PO.** `paymatch.py po-lines '{"po": "<PO#>"}'` → the PO trimmed to
   `{po_id, name, vendor, partner_ref, state, amount_untaxed, freight_cost,
   fees_cost, lines:[{line_id, sku, style, description, qty, price_unit}]}`.
   Confirm the vendor / `partner_ref` line up with the document. The PO must be
   `state: "purchase"` to edit lines. (`found: false` with `candidates` means
   the PO# didn't resolve — that's a Questions case.)

4. **Compare line by line.** Pair each document line to a PO line by **(style/
   item, color, size)** — never by row order. Size upcharges are normal (base
   sizes one price; 2XL/3XL/4XL higher) — that's correct pricing, not an error.

5. **Correct mismatches** in one call:
   `paymatch.py apply '{"po_id", "lines":[{"line_id","price_unit"}]}'`. Set
   `freight_cost`/`fees_cost` only when the **document itself** gives an
   authoritative figure — a pre-existing freight estimate or partner fee the
   document doesn't itemize is not a line error; note it for the invoice match.

6. **File the document — always.**
   - **Reconciled** (matched, or corrected with confidence) →
     `paymatch.py matched '{"po_id", "document_id", "body": "<what you checked/fixed>"}'`
     (posts the checked note + moves the doc to `Matched`).
   - **Genuine question** →
     `paymatch.py questions '{"document_id", "question": "<what to resolve>", "reviewer": "Zach Tucker"}'`
     (raises the activity + moves the doc to `Questions`). Pass `po_id` +
     `po_note` too if the PO also warrants a note.

## Totals are a cross-check, not the source of truth

A shipment acknowledgement is often **one box of a multi-shipment order**: it
covers a subset of the PO's lines, so its total is legitimately **less** than
the PO total — the rest ships later. Match on lines; a total gap fully explained
by un-shipped lines is **not** a discrepancy. Say so in the checked note so a
human isn't confused by the header total.

## Partial shipments: track cumulative coverage and call the last one

When a document is a **partial shipment** (it reconciles cleanly but covers only
some of the PO's lines), do two things before you file it:

1. **Name the lines this shipment covers.** In the `matched` log note, list the
   specific lines / SKUs this acknowledgement checks (e.g. *"Shipment of P13137
   — checked lines 3,4,7,9,10,11 (styles …), all $1.79 and matching"*). That is
   what turns the PO's chatter into a running ledger of what has been checked.

2. **Look back before you post, and call the final shipment.** Read the PO's
   prior log notes with `paymatch.py notes '{"po": "P13137"}'` (or the
   `po_get_messages` tool) and cross-check `qty_received` / `qty` per line from
   `po-lines`. If the lines you just checked, **unioned with the lines earlier
   notes already checked, now cover every line on the PO** (nothing left on
   back-order / un-received), then this is the last piece — **say so explicitly
   in the note**, e.g. *"✅ Final shipment — all 11 lines on P13137 are now fully
   checked across all shipments; PO complete."* If lines still remain, state
   which ones are still outstanding instead of implying completion.

Only claim "fully checked" when the prior log notes (and `qty_received`) actually
show the rest was checked — those notes are the evidence, which is exactly why
every annotation is an internal log note that accumulates on the PO.

## When to escalate (Questions) vs. just fix (Matched)

Escalate only a **real** ambiguity: can't read the PO#, the PO doesn't resolve,
prices don't reconcile, unexpected/missing lines, or the wrong vendor. An
unambiguous correction the vendor document plainly supports (a size priced $2
off the vendor's own confirmation) is a **Matched** fix — applying it is exactly
what the task asks. Don't manufacture a question where the document is clear;
don't guess where it isn't.

## Report

Per document: PO number, lines changed (old → new) or "no change", whether the
checked note was posted, and Matched vs Questions (and why). End with a folder
tally so the inbox state is obvious.

## Creating the payable (draft) and buying-group sources

The same reconcile-then-file loop extends to **creating the vendor bill** once a
PO's pricing is reconciled:

```bash
python3 scripts/paymatch.py bill '{"po_id": 13145, "vendor_bill_number": "<inv#>", "invoice_date": "2026-07-22", "expected_total": 1041.90, "tolerance": 0.02, "reviewer_user_id": 6, "review_note": "..."}'
```

`bill` creates the bill in **draft** and schedules a review activity — it never
posts (a human posts it). `expected_total` (the invoice total) is verified within
`tolerance`; a mismatch returns `success:false` and no bill is created, so you
escalate rather than bill blind.

### Sports Inc (buying group — no per-invoice documents)

Sports Inc doesn't email individual invoices; they live in the **SportsLink
API**. The `sportsinc-sportslink` adapter pulls them (normalised to the same
invoice shape a PDF would give) and marks them consumed. The end-to-end loop —
pull active SI invoices → reconcile to the PO → **auto-fix price variances,
escalate quantity/line variances** → create the **draft** bill → **mark the SI
doc consumed only after the bill exists** (exactly-once) — plus credit/scanned
handling and the SI-fee/`expected_total` nuance, is the dedicated procedure in
[`references/sportsinc_payables.md`](references/sportsinc_payables.md). Read it
before running the SI payables flow.

Scope note: this skill reconciles and drafts; a human posts. Only create bills
when the task is payables (folder pricing review alone stops at the "checked"
note + filing).

#### Agent-to-Agent (A2A) Mode for Sports Inc

For deployments with a **dedicated Sports Inc agent**, this agent can fetch the
invoices by *delegating* to that agent over A2A instead of running
`sportsinc-sportslink` itself. **This** agent owns `SPORTSINC_API_KEY` (it
represents your company) and *shares* it with the Sports Inc agent for the
duration of each delegated call. The A2A call is orchestrated by **you (the
agent) using the platform MCP tools** — there is no Python helper for it.

**Setup (platform console):**

1. **Create the Sports Inc agent** and install the `sportsinc-sportslink` skill.
   Do **not** bind `SPORTSINC_API_KEY` to it — the key lives on this agent.
2. **Bind `SPORTSINC_API_KEY` to this agent** (the caller) on its Credentials tab.
3. **Bind a delegation connection**: caller = this agent, target = the Sports Inc
   agent, with a label/instructions describing when to use it.
4. **Share the credential** on that connection: on this agent's Connections tab,
   under the Sports Inc connection, check `SPORTSINC_API_KEY` in "Credentials to
   share with this connection". Nothing is shared unless you check it.

**A2A call flow (agent-executed MCP tools):**

1. `get_my_bundle()` → its `structuredContent.connections[]` lists your bound
   agents; each entry is `{ targetAgentUid, displayName, label, instructions }`.
   Pick the Sports Inc one (match on `displayName`/`label`).
2. `start_agent_conversation({ agent_uid: <targetAgentUid> })` → returns a
   `conversation_id`.
3. `send_message({ conversation_id, content })` where `content` is the JSON
   request for the Sports Inc agent, e.g. `{"action": "get-for-a2a", "params":
   {"include_historical": false}}`. The reply is the `get-for-a2a` envelope
   (`{success, invoices, metadata, error}`) — on `success:false`, read
   `error.retriable` to decide retry vs. escalate.

Then continue the normal reconciliation/draft-bill loop with the returned
`invoices` (same normalised shape as `sportslink.py list`).

**How the handoff works (pull/broker):**

- The delegation binding is the allowlist — only bound agents are reachable, and
  the call chain is depth-limited (max 5) against loops.
- The shared credential is **pulled on demand, not pushed**. When the Sports Inc
  agent handles the delegated call, its runtime calls
  `get_delegated_credentials({ conversation_id })`. The platform verifies it is
  the target of that delegated conversation and that the connection shares the
  credential, **logs the access** in `agent_connection_audit_log`, and returns a
  `{ env_key: value }` map. The runtime exposes it as env for the turn, so the
  Sports Inc agent's `sportsinc-sportslink` skill reads `SPORTSINC_API_KEY`
  normally. The secret only moves when the target actually asks for it, and every
  access is audited — nothing is provisioned permanently onto the Sports Inc agent.

## Deep reference

Full matching rules, the exact MCP tool payload shapes, a worked five-document
example, and the **low-cost model recommendation + per-match economics** are in
[`references/matching_procedure.md`](references/matching_procedure.md). Read it
when you need the details behind a step; the SKILL above is the operating loop.
