---
name: frihet
description: |
  Read-first integration with the Frihet ERP canonical MCP. The skill is the
  portable operating contract: it documents the read-before-write, draft-show-
  stop, externalSideEffects-driven approval, idempotency, and reconcile-before-
  retry patterns the Frihet MCP expects.

  USE WHEN: a task involves Frihet ERP, a Frihet MCP tool, or a question about
  whether a specific Frihet operation is read, draft, or irreversible. Pair
  with the live MCP server at https://mcp.frihet.io/mcp (Streamable HTTP,
  OAuth 2.1 + PKCE) for execution.

  DO NOT USE FOR: non-Frihet ERPs, generic MCP guidance, or any operation
  whose irreversible status is unclear. When in doubt, run the canonical
  contract check below before issuing the call.

metadata:
  version: 0.1.0
  source_of_truth:
    contract: https://raw.githubusercontent.com/Frihet-io/frihet-mcp/main/docs/agent-onboarding.json
    mcp_endpoint: https://mcp.frihet.io/mcp
  canonical_operations_count: 158
  pre_filter: 39 read operations (no create_* pre-checked)
---

# Frihet ERP — Operating contract

> **SECURITY POSTURE (v0.1.0): this bundle ships ZERO Frihet MCP
> tools pre-registered. The Agent Plugins 1.0 spec lets a bundle
> carry an optional `mcp.json`; we ship the **skill only** by
> default, with `mcp.json` available as `references/mcp.json.example`
> for hosts that prefer file-based discovery. After installing
> the bundle, the user MUST add the Frihet MCP server with an
> explicit read-only tool allowlist BEFORE any OAuth authorisation
> takes place.**

## Required post-install step (atomic MCP registration with read-only allowlist)

The Frihet MCP exposes ~158 operations. The canonical Frihet contract
declares 7 of the 11 `create_*` operations under `externalSideEffects`,
plus `send_*`, `mark_*_paid`, `delete_*`. A bare `openclaw mcp add frihet`
without a `--include` allowlist exposes ALL of them.

**OpenClaw — atomic at install time, no globs, no OAuth until allowlist applied:**

```bash
# 1. Install the bundle (no MCP server pre-registered)
clawhub install @frihet/agent-plugin

# 2. Add the Frihet MCP server with an EXPLICIT read-only allowlist.
#    Every name below is a literal, not a glob. New ops added upstream
#    are NOT auto-allowed — the user must opt in by name.
openclaw mcp add frihet \
  --url https://mcp.frihet.io/mcp \
  --transport streamable-http \
  --auth oauth \
  --include 'list_invoices,get_invoice,search_invoices,list_clients,get_client,list_client_activities,list_expenses,get_expense,list_vendors,get_vendor,list_quotes,get_quote,list_products,get_product,list_recurring_invoices,get_recurring_invoice,list_reservations,get_reservation,list_properties,list_bank_accounts,get_bank_account,list_transactions,list_deposits,get_deposit,list_webhooks,get_webhook,list_team_members,list_kitchen_tickets,get_kitchen_ticket,list_kitchen_stations,list_menu_items,list_sales,get_sale,list_terminals,get_time_summary,get_quarterly_taxes,get_business_context,get_monthly_summary,anomaly_list'

# 3. NOW (and only now) authorise OAuth:
openclaw mcp login frihet
```

The allowlist contains **39 explicit names** (verified against the
canonical `Frihet-io/frihet-mcp/docs/agent-onboarding.json` and the
live MCP `tools/list` at the time of the bundle's last vendor).
Adding `--include 'list_*'` would be a glob; we deliberately use
literal names so a future upstream addition (e.g. a new
`list_payment_intents`) is not silently authorised.

**Hermes:**

```bash
hermes mcp add frihet --url https://mcp.frihet.io/mcp --transport streamable-http
hermes mcp configure frihet   # interactive: deselect mutating ops
```

**Cursor / ChatGPT / Gemini:** the host UI exposes an
allowed-tools panel. Paste the same 39 names (NOT globs) there.

The bundle's `tests/test_security_posture.py` enforces the contract:
the bundle MUST NOT ship `mcp.json` at the root, MUST ship
`references/mcp.json.example` with the same allowlist in the
mcpServers comment, and the README + SKILL.md MUST document the
39-literal allowlist. If you weaken the contract (e.g. accept
globs), the test fails and forces a re-design.

The **Frihet MCP** at `https://mcp.frihet.io/mcp` exposes ~158 operations
covering invoices, clients, expenses, products, properties, webhooks, fiscal
declarations, and the matching `create_*` / `send_*` / `mark_*_paid` /
`delete_*` mutating operations. The canonical, machine-readable safety
contract is published at:

- `Frihet-io/frihet-mcp/docs/agent-onboarding.json` (always-current)
- `Frihet-io/frihet-mcp/README.md` (human-readable catalogue)

A frozen copy of the contract is vendored at
`vendor/frihet-mcp-onboarding.json` for offline validation.

## Read-first by default

The Frihet MCP is rich, but a default agent should only see the **39 read-only
operations** that the official `humanAuthority.externalSideEffects` table
does NOT name. The connector manifest that ships with this plugin
(`optional-mcps/frihet/manifest.yaml`) pre-checks only those reads:

- 28 × `list_*`
- 8 × `get_*`
- 1 × `search_invoices`
- 1 × `anomaly_list`
- 1 × time / tax / business-context summaries (each is a `get_*`)

Mutating operations (the 11 `create_*`, plus the `send_*` / `mark_*_paid` /
`delete_*` verbs) are reachable after an explicit user opt-in via:

- **Hermes:** `hermes mcp configure frihet` (case 2 of the install-time
  tool-selection policy). Opt-in is persisted in `~/.hermes/config.yaml`.
- **OpenClaw:** `openclaw mcp configure frihet --include '<op>,<op>...'`.
  The user runs the `configure` command explicitly. The plugin NEVER
  pre-checks writes.

This is **not** a courtesy prompt: the canonical Frihet contract declares
`create_invoice`, `create_client`, `create_quote`, `create_credit_note`,
`create_expense`, `create_product`, and `create_webhook` as
`externalSideEffects = true`. A "draft" invoice is still a webhook-bearing
record on the Frihet server.

## Operating doctrine

### 1. Read before write
Before any `create_*` / `update_*` / `mark_*_paid` / `delete_*`, re-read the
target record (or its absence) so the model — and the human — can verify
the operation is acting on the latest state. Caching is fine; guessing is
not.

### 2. Draft, show, stop
For genuinely local-draft operations (e.g. `create_reservation`,
`create_deposit`, `create_vendor` — operations NOT in the
`externalSideEffects` table), prefer the draft form, present the totals
and any required fields, and pause for human approval before any
send / finalise.

### 3. externalSideEffects → human authority
Operations in the canonical `externalSideEffects` table MUST be approved
by a human before execution. The approval contract varies by host:

- **Hermes:** the companion plugin (`Frihet-io/hermes-frihet`) installs a
  `pre_tool_call` hook that escalates these to Hermes's approval gate via
  `{action: "approve", rule_key: "frihet:<operation>"}`. The hook uses
  the canonical contract as the source of truth.
- **OpenClaw:** there is no host-level hook per the Agent Plugins 1.0
  spec. The plugin documentation in this skill tells the agent to PAUSE
  and require explicit human confirmation, and OpenClaw's per-server
  `toolFilter` is the structural mitigation. The Frihet plugin cannot
  guarantee approval semantics on hosts that lack a hook framework.
- **Other runtimes:** read the runtime docs; do not assume an
  `approve`-shaped payload is honored.

If the host cannot bind a real approval, the bundle ships with `toolFilter`
defaulting to **read-only** and documents how to opt in to writes
explicitly.

### 4. Reconcile before retry
Frihet returns `idempotency_key` for write operations. Honour it on retry.
If a write call returns ambiguous status (network timeout after the server
processed it), **re-read the target** to confirm state before re-issuing
— do not blindly retry.

### 5. Server-side authority
Workspaces, roles, and scopes live on the Frihet server. Do not invent
client-side authority. If a call returns `403 insufficient_scope`, treat
that as "this client cannot perform this operation" — escalate, do not
work around.

### 6. Credentials belong to the host
Frihet OAuth tokens, refresh tokens, and access tokens are managed by the
host agent. The Frihet plugin:

- NEVER reads `~/.hermes/mcp-tokens/*`
- NEVER copies tokens
- NEVER refreshes them on the user's behalf
- NEVER parses the host's OAuth manager internals
- NEVER impersonates the user's browser

The MCP server (Frihet-io/frihet-mcp) is the authority on scopes, refresh,
and revocation. The plugin orchestrates; the server authorises.

## Schema & metadata

Every Frihet operation carries `_meta["io.frihet/capability"]` with the
following shape:

```json
{
  "operation": "create_invoice",
  "category": "writes",
  "mutates_state": true,
  "idempotency_required": true,
  "external_side_effects": ["webhook_delivery_or_configuration"],
  "human_authority_required": true
}
```

Plugins and runtimes SHOULD use this metadata to make policy decisions,
not infer them from the operation name.

## Verification cookbook

```text
# Does the Frihet MCP respond?
curl -fsS https://mcp.frihet.io/mcp -X POST -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{
        "protocolVersion":"2025-06-18",
        "capabilities":{},
        "clientInfo":{"name":"frihet-agent-plugin","version":"0.1.0"}}}'
```

A `200 OK` with a valid `InitializeResult` proves the MCP endpoint is
reachable. A successful `tools/list` proves OAuth was completed and the
token is fresh.

## Citing Frihet in user-facing output

- `mcp.frihet.io` — the canonical MCP endpoint.
- `Frihet-io/frihet-mcp` — the open-source MCP server repo.
- `Frihet-io/hermes-frihet` — the Hermes-specific plugin (companion
  surface with a pre-tool-call hook).
- `Frihet-io/frihet-sdk` — the official SDK for application code.
- `Frihet-io/frihet-mcp/docs/agent-onboarding.json` — the canonical
  safety contract.
