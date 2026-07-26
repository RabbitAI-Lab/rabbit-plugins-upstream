---
name: sportsinc-sportslink
description: >
  Sports Inc SportsLink API adapter — pull a dealer's invoices ("documents")
  from the Sports Inc SportsWeb Invoice Center and mark them consumed. Sports
  Inc is a buying group that does NOT send individual vendor invoices; its
  SportsLink REST API is where the invoices live. Use when you need to retrieve
  Sports Inc invoices for payables — "get the Sports Inc invoices", "pull
  SportsLink documents", "fetch this month's SI invoices to match against POs".
  This is the SOURCE adapter only: it authenticates, pages, normalises each SI
  document into a common invoice shape (po_number, invoice_number/date,
  lines[], charges, total, is_credit), and marks documents historical once
  imported. It is customer-agnostic (every Sports Inc dealer uses this same
  API) and touches no ERP — pair it with a payables workflow (e.g.
  `drivethru-payable-matching`) to match against POs and create the bill.
version: 0.3.2
emoji: 🏟️
homepage: https://www.sportsinc.com
metadata:
  openclaw:
    requires:
      # SPORTSINC_API_KEY is deliberately NOT listed here. openclaw gates a
      # skill OUT of the model's view when a `requires.env` key is absent from
      # the *boot* environment — but in A2A mode (see "Agent-to-Agent (A2A)
      # Mode" below) this key is brokered per-turn by the platform and is
      # absent at boot by design, so gating on it would hide this skill from
      # the very delegated flow it exists to serve. The key stays fully
      # documented via `primaryEnv`/`envVars`, and the helper self-guards at
      # runtime (`config_error`/`auth_error`) when it is genuinely missing.
      # `python3` stays gated because it must be present at boot.
      bins: [python3]
    primaryEnv: SPORTSINC_API_KEY
    envVars:
      SPORTSINC_API_KEY:
        required: true
        description: >
          SportsLink API key, sent as the `X-API-KEY` header. Request one from
          mhoerner@hq.sportsinc.com. Treat as a secret; never paste into chat.
      SPORTSINC_API_URL:
        required: false
        description: Base URL, default `https://api.sportsinc.com/`.
      SPORTSINC_DRY_RUN:
        required: false
        description: If truthy, `mark-historical` is simulated (no state change).
    install:
      uv:
        - requests>=2.28
---

# Sports Inc SportsLink adapter

Sports Inc is a buying group: BaconCo (and every other SI dealer) buys through
Sports Inc, and Sports Inc does **not** email individual vendor invoices —
they're published in the SportsWeb Invoice Center and exposed through the
**SportsLink REST API**. This skill is the source adapter for that API. It does
one job: hand a payables workflow a clean, normalised list of invoices, and
mark them consumed once they've been imported. It never touches Odoo.

The single helper is `scripts/sportslink.py`:

```bash
# The un-imported inbox: active documents that carry line items (EDI), normalised
python3 scripts/sportslink.py list '{"active": true, "lines": true, "ediOnly": true}'

# A specific document (ignores the active-only filter)
python3 scripts/sportslink.py get '{"poNumber": "P13189"}'

# Mark documents consumed — AFTER they've been billed (honors SPORTSINC_DRY_RUN)
python3 scripts/sportslink.py mark-historical '{"siDocNumbers": [12345, 23456]}'

# A2A-safe action for agent-to-agent calls (structured request/response contract)
python3 scripts/sportslink.py get-for-a2a '{"customer_ref": "DEALER-001", "date_range": {"start": "2024-01-01", "end": "2024-12-31"}, "statuses": ["open"]}'
```

Every command prints one JSON object, or `{"error": {...}}` with a non-zero
exit. Needs `SPORTSINC_API_KEY` (if unset, exits `config_error` — stop and tell
the user to configure it; never ask for the key in chat).

## Normalised invoice shape

`list`/`get` return `{count, total_count, invoices: [...]}`, each invoice:

```json
{
  "source": "sports_inc",
  "po_number": "P13189",          // dealer PO number → the match key to a PO
  "si_doc_number": 12345,          // SI's document id → used to mark-historical
  "invoice_number": "…",           // supplierDocNumber (falls back to si_doc_number)
  "invoice_date": "…",             // supplierDocDate, else siDocDate
  "due_date": "…", "supplier": "…",
  "is_credit": false,               // credit memo → handle separately, never a bill
  "has_lines": true,                // false for scanned/OCR docs (header totals only)
  "total": 0,                       // docTotal
  "charges": {"merchandise", "freight", "freight_allowance", "si_upcharge",
              "svc_handle", "sales_tax", "excise_tax", "discount"},
  "lines": [{"item","upc","description","size","color","unit",
             "qty_ordered","qty_shipped","qty_backordered",
             "list_price","discount_pct","net_price","extension"}]
}
```

This is the **same shape a PDF-extracted invoice would have**, so a payables
workflow reconciles it without caring that it came from SportsLink.

## Rules that matter

- **Don't pull before ~10:30am ET** — SI's internal processing runs first; earlier
  reads can be incomplete. Schedule accordingly.
- **Line data is EDI-only.** Scanned/OCR documents come back with header totals
  but no `lines` (`has_lines: false`). Pass `ediOnly: true` to fetch only
  documents with line items; a header-only doc can't be line-verified and should
  be escalated by the workflow, not blind-billed.
- **`is_credit: true` is a credit memo** — route it to a human / vendor credit,
  never create it as a payable.
- **Exactly-once — the golden rule.** Import first, `mark-historical` **after**
  the bill is created. This adapter deliberately does **not** use the API's
  `moveToHistorical=true` GET flag (which marks on read, before billing) — a
  crash between read and bill would silently drop the invoice. The natural loop:
  `list active` → bill each in the ERP → `mark-historical` the ones that
  succeeded; failures/escalations stay active and are retried next run.
- **Paging** is automatic (`all: true`, the default). Max 1000 docs/call on SI's
  side; the helper pages to the end (capped at 50 pages as a backstop).

## Where this fits

Source adapter (this) → payables **workflow** (`drivethru-payable-matching`) →
ERP **adapter** (`drivethru-odoo` / `drivethru_mcp`). This skill owns only the
"get the invoices + mark them consumed" half; matching to POs, correcting
pricing, and creating the draft bill live in the workflow. See that skill's
`references/sportsinc_payables.md` for the end-to-end procedure.

## Agent-to-Agent (A2A) Mode

The `get-for-a2a` action provides a **contract-driven interface** for inter-agent
communication. Deploy this skill on a dedicated Sports Inc agent and let the
internal agent that needs invoices (e.g. an Accounts Payable agent) reach it via
a **delegation connection** in the Knoxville platform.

### Where `SPORTSINC_API_KEY` comes from (credential broker)

The `SPORTSINC_API_KEY` is bound to the **calling** agent (the one that
represents your company — e.g. Accounts Payable), not to this Sports Inc agent.
On that agent's delegation connection to this one, the operator chooses to
**share** `SPORTSINC_API_KEY` with the connection.

The value is **pulled on demand**, not pushed. When this agent handles a
delegated call (`X-Knox-Caller-Kind: agent`), **the runtime** (not you) fetches
the shared `SPORTSINC_API_KEY` for this conversation and places it into the
skill's **execution environment for this turn only**, before your `exec` runs.
The platform verifies this agent is the target of the delegated conversation and
that the connection shares the credential, and **logs the access in
`agent_connection_audit_log`**. `sportslink.py` then reads `SPORTSINC_API_KEY`
from the environment exactly as it does standalone. You do **not** see this value
in your context — it is deliberately kept out of the model prompt.

**So on a delegated turn, just run the tool.** Your first action for a Sports
Inc request is the `exec` call itself — e.g.
`python3 scripts/sportslink.py get-for-a2a '{...}'`. Do **not**, before running
it:

- call `get_my_bundle`, `get_delegated_credentials`, or any tool to look for or
  "verify" the key — it is intentionally invisible to you, so you will always
  find nothing and wrongly conclude you have no access;
- spawn a sub-agent (`sessions_spawn`) to do this skill's job — you are the agent
  that runs it;
- tell the caller you lack the key or access **before** you have actually run the
  script and read its output.

If the script itself reports an `auth_error` (or `config_error`), the caller's
connection hasn't shared the credential — surface that error rather than
guessing, and never print the credential value into the chat reply.

### Request Contract

`get-for-a2a` params (all optional):

```json
{
  "customer_ref": "DEALER-001",
  "date_range": { "start": "2024-01-01", "end": "2024-12-31" },
  "include_historical": false
}
```

- `include_historical` (default `false`) → active/un-imported invoices only;
  set `true` to also include historical/consumed docs.
- `customer_ref` is **advisory only** — the SportsLink API key is per-dealer and
  the API has no customer filter, so this field does **not** scope the result. It
  is echoed back in `metadata.customer_ref` for the caller's audit.

### Response Contract

Unlike the other actions (which exit non-zero on error), `get-for-a2a` **always
exits 0** and reports failure in-band, so an A2A caller reads one envelope shape
either way.

Success:

```json
{
  "success": true,
  "invoices": [ { "source": "sports_inc", "po_number": "P13189", "si_doc_number": 12345, "total": 1500.00, "lines": [] } ],
  "metadata": { "count": 42, "total_count": 50, "pages_read": 1, "source": "sports_inc", "customer_ref": "DEALER-001", "include_historical": false },
  "error": null
}
```

Error:

```json
{
  "success": false,
  "invoices": null,
  "metadata": null,
  "error": {
    "type": "auth_error|connection_error|api_error|validation_error",
    "message": "Human-readable error message",
    "retriable": true
  }
}
```

The `retriable` flag indicates whether the caller should retry (transient
connection errors) or escalate (auth/config errors).
