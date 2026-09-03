---
name: danube
description: Governed tool access for your agent — one Danube API key unlocks your organization's own tools plus a large, growing catalog of ready-made services. Search, inspect, and execute tools over native MCP or plain curl, with explicit confirmation before anything that writes, sends, spends, or deletes.
metadata:
  openclaw:
    emoji: "🌊"
    homepage: https://docs.danubeai.com/sdk/openclaw
    requires:
      env:
        - DANUBE_API_KEY
      bins:
        - curl
    primaryEnv: DANUBE_API_KEY
    envVars:
      - name: DANUBE_API_KEY
        required: true
        description: Danube API key from https://danubeai.com/dashboard → Settings → API Keys (an opaque token — no fixed prefix)
    always: false
---

# Danube — Governed Tool Access for Agents

Danube makes an organization's own tools — plus a large and growing catalog of ready-made services — callable by AI agents through a single API key, with permissions, spending limits, and an audit trail handled by the platform. The catalog changes constantly and includes tools the user's organization connected privately, so **never assume what is available — search first.**

## Guardrails (read these first)

- **Read freely, act with consent.** Discovery — listing services, searching tools, reading schemas, checking ratings, balances, or limits — needs no confirmation. Before any action that **writes, sends, posts, deletes, purchases, spends wallet funds, stores a credential, changes spending limits, or creates/updates/deletes a skill or workflow** — and before **any batch execution** — show the user the exact tool and parameters and get an explicit "yes".
- **Honour the confirmation handshake.** If `execute_tool` comes back with `_meta.confirmation_required: true`, the account's key requires consent for destructive calls: show the user the tool and the exact `parameters` from the response, get an explicit yes, then call again with the same parameters and the `confirm_token` (valid 5 minutes). Never call again with the token without asking.
- **Never invent credentials.** Only store an API key the user has explicitly handed you in this conversation, and confirm before storing. Otherwise send them to https://danubeai.com/dashboard to connect the service themselves.
- **Least data.** Pass only the parameters the task needs; don't forward unrelated personal data to third-party services.
- **Respect limits.** Don't raise spending limits or fund wallets unless the user asks for exactly that.
- **Report specifics.** After executing, say which tool ran, with what inputs, and what came back — not just "done".

## Setup

### 1. Get an API key

From the dashboard: https://danubeai.com/dashboard → Settings → API Keys. Keys are opaque ~43-character tokens with **no fixed prefix** — don't validate their shape, just keep them secret.

Or let the user authorize this agent with the OAuth 2.0 Device Authorization flow (RFC 8628):

```bash
curl -s -X POST https://api.danubeai.com/v1/auth/device/code \
  -H "Content-Type: application/json" -d '{"client_name": "OpenClaw"}'
# → {"device_code": "...", "user_code": "XXXX-XXXX", "verification_url": "...", "expires_in": ..., "interval": 5}
```

Tell the user to open `verification_url` in a browser and enter `user_code`. Then poll:

```bash
curl -s -X POST https://api.danubeai.com/v1/auth/device/token \
  -H "Content-Type: application/json" -d '{"device_code": "DEVICE_CODE_FROM_ABOVE"}'
```

`428` = not approved yet (poll every `interval` seconds) · `200` = `{"api_key": "…"}` · `410` = expired, start over.

### 2. Make the key available to OpenClaw

Set `DANUBE_API_KEY` in the environment, or in `openclaw.json`:

```json5
{ skills: { entries: { danube: { apiKey: "YOUR_DANUBE_API_KEY" } } } }
```

### 3a. Connect natively over MCP (recommended)

OpenClaw has a built-in MCP client. Register Danube's server once and its tools become ordinary OpenClaw tools (`search_tools`, `execute_tool`, …):

```bash
openclaw mcp set danube '{"url":"https://mcp.danubeai.com/mcp","transport":"streamable-http","headers":{"danube-api-key":"YOUR_DANUBE_API_KEY"}}'
openclaw mcp doctor danube --probe
```

Use the real key value in `headers` (not `${DANUBE_API_KEY}`). The server also speaks MCP OAuth: use `"auth":"oauth"` instead of `headers`, then `openclaw mcp login danube`.

To keep the tool list small, append `?tools=core` to the URL (discovery, execution, credentials, feedback) or a comma list such as `?tools=core,workflows`; without it all 31 tools are described to the model. Groups: `core`, `skills`, `workflows`, `wallet`, `feedback`.

### 3b. Or use plain `curl` — no MCP needed

Every capability below is also a REST call against `https://api.danubeai.com/v1` with the header `danube-api-key: $DANUBE_API_KEY`. Copy-paste recipes: `{baseDir}/references/rest-api.md`.

## Working with tools

Every task follows **Explore → Inspect → (Confirm) → Execute → Report.**

| Goal | MCP tool | REST |
|---|---|---|
| See what services exist | `list_services(query, limit)` | `GET /services` |
| Find a tool for a task | `search_tools(query, service_id?, limit?)` | `GET /tools/search?query=…` |
| All tools of one service | `get_service_tools(service_id)` | `GET /services/{id}/tools` |
| Full schema of one tool | returned by the calls above | `GET /tools/{tool_id}` |
| Run a tool | `execute_tool(tool_id, parameters, fields?)` | `POST /tools/call/{tool_id}` with `{"tool_input": {…}}` |
| Run up to 10 at once | `batch_execute_tools(calls)` | `POST /tools/call/batch` |
| Inspect one tool before first use | `describe_tool(tool_id)` | `GET /tools/{tool_id}/describe` |
| Read a stored result back | `fetch_result(execution_id, path?)` | `GET /tools/executions/{execution_id}/result?path=…` |
| Remember a per-service default | `set_parameter_defaults(service_id, defaults)` | `PUT /services/{service_id}/parameter-defaults` |

### Reading what comes back

`execute_tool` returns `{result, _meta}` once a call actually reaches a tool. When the tool
returned JSON, the already-parsed object is at **`result.data`** — read that;
`result.content[0].text` is the transport envelope and only exists for MCP clients that
read it, so don't `json.loads()` your way down to the same thing. Don't index `_meta`
blindly: it is absent when the lookup itself failed (no `tool_id` or `tool_name` given, or
neither resolves).

Oversized payloads are trimmed. A JSON array is trimmed at element boundaries, so it stays
parseable; plain text is cut mid-string with an inline `... [truncated - response was N
chars, …]` note; and a JSON object with no array big enough to trim degrades to
`{"_truncated_partial_json": "<prefix>", "_truncated": true}` — valid JSON, but the
object's own keys are gone, so re-request it rather than parsing that. Check
`_meta.truncated`, and `_meta.truncation_note` for what went. To get the rest, raise
`max_response_chars` (default 50000, hard max 500000) or follow `_meta.cursor` when the
upstream paginates. When a tool is resolved by *name*, a publisher's lower per-tool default
can apply, so trimming below 50000 is normal there. Truncated ≠ broken — don't
`report_tool` it.

**Credential values are masked before you ever see them.** Every tool response passes
through Danube's redactor on the way out, and unless the tool is one specifically declared
as returning a credential (see below), anything that reads as a secret — API keys, tokens,
passwords, connection strings — comes back as `[REDACTED:<FIELD>]`. That is
platform policy, not a broken tool: don't `report_tool` it, and don't ask the tool to
return the raw value. When there is something to report, the redaction object carries an
exact `count` plus a `fields` list — the first 50 masked values, each with its `path`,
`key`, and the `rule` that caught it — and a `mode`. It lives at `_meta.redaction` over
MCP, where the key is absent when nothing was masked, and at top-level `redaction` over
REST, where the key is always present and simply `null`. Either way, test the value, not
the key. Pagination cursors and identifiers are exempt by name, so paging keeps working.

A tool whose whole *purpose* is to mint a credential is not redacted into uselessness.
Where Danube can, it captures the secret for you: the new value is stored as the user's
credential for the target service and `_meta.redaction.stored_credentials` says where it
landed, so the service's later calls pick it up through ordinary credential injection and
you never hold the value.

**Where it can't, the secret reaches you raw** — a tool marked as returning a credential
with no capture mapping, a self-hosted deployment (custody stays in the customer's own
environment), or a store that failed. These come back completely unmasked with
`_meta.redaction.passthrough_reason` explaining why, alongside `count: 0`. This is
not limited to short-lived handoff tokens like a Plaid *link* token: a Plaid **access**
token, a rotated webhook signing secret, and other durable secrets pass through this way.
Treat anything that arrives unmasked as a live secret — show the user where to put it,
don't echo it back, and don't paste it into a later call's parameters.

Discovery tips:
- Every search result carries `readiness`: `ready` means you can execute it now, `needs_credential` means the service needs a credential this account has not connected (send the user to `configuration_url`), `unavailable` means the service is retired. Ready tools are listed first; prefer a ready tool over a better-named one that needs setup.
- Describe the *outcome* in natural language (`"send an email"`, `"create a GitHub issue"`, `"translate text"`); search is semantic.
- If the first query misses, rephrase and try again before concluding a capability doesn't exist. The catalog is far larger than you'd guess.
- `list_services` is served from a cache refreshed every 60 seconds, so a service connected or published moments ago can be missing from it for up to a minute; `search_tools` and `get_service_tools(service_id)` are not cached. Don't conclude a service doesn't exist from one `list_services` miss; search for one of its tools instead.
- Read the tool's parameter schema (`required`, `type`, `enum`, `tips`) before executing; ask the user for anything required that you don't have. Never reuse tool IDs from memory — search again.
- Pass only parameters the schema declares. On the standard HTTP execution path, Danube drops anything the tool row doesn't declare *before* making the upstream request, so an invented parameter never reaches the provider. If such a call then fails, the error message ends with a note naming what was dropped — "`'x'` was not sent — `<tool>` does not declare that parameter, so Danube dropped it before making the request. If the upstream supports it, the tool's schema is missing it." Read that note rather than concluding the upstream ignored your value, and treat it as a sign the tool's schema may be missing a parameter the provider does support. Tools backed by an MCP server forward your parameters as given, so there the upstream really did see them.
- Results called in the last 30 days also carry `reliability` (`calls_30d`, `success_rate_30d`, `p50_seconds`, `last_error_class`, `flagged`). When two tools fit, prefer the higher success rate; a `flagged` tool (under 80% success on 20+ calls) is a last resort, and say so to the user. Results are relevance-ordered with a bounded reliability nudge; pass `ready_only=true` to see only tools you can call now, or `min_success_rate=0.9` to drop tools with a known-poor 30-day rate.
- Before a tool you have not used successfully in this session, call `describe_tool(tool_id)` (REST: `GET /tools/{tool_id}/describe`): it returns the schema, your readiness, the last 30 days of usage with the most common errors, and your own last working parameter sets.
- If a service always needs the same identifier (Vercel `teamId`, a Sentry org slug, a DigitalOcean app id), save it once with `set_parameter_defaults(service_id, {"teamId": "…"})` after the user confirms it; later calls that omit it get it filled in (`_meta.defaults_applied` says which). Never save a key or token this way.
- Keep big results out of your context: pass `fields: ["items[].name", "pagination.next"]` to `execute_tool` to receive only those paths. The full result is stored under `_meta.execution_id`; `fetch_result(execution_id, path)` (REST: `GET /tools/executions/{id}/result?path=…`) reads any other part of it back without re-running the tool.

### When a tool needs credentials

A result containing `"error_type": "auth_required"` means this user hasn't connected that service yet:
1. Prefer sending the user to the `configuration_url` in the error (or https://danubeai.com/dashboard) to connect it — the only path for OAuth services such as Gmail, Slack, or Google Calendar.
2. For API-key services, if the user explicitly gives you the key and confirms, call `store_credential(service_id, credential_type="bearer", credential_value=…)`, then retry.

`get_service_tools` reports `needs_configuration: true` only when *every* tool of the service is `needs_credential` for this account; it is derived from the per-tool `readiness` field, which is the answer for any single tool. A service mixing credential-free and credential-bearing tools reports `false`, so read `readiness` on the tool you are about to call rather than the service-level flag.

`credential_value` takes either the raw secret or a **reference** — a pointer resolved when the tool runs, so the secret is never held centrally.

**References only work on some execution paths.** A reference is resolved on the standard HTTP auth-injection path — an `api` service whose tool isn't one of the provider-specific composite handlers — and by the in-VPC data-plane agent, which runs the services an org has marked `local_only`. Everything else reads the stored string **as the secret**: `mcp_server` services, and composite handlers for services like Firecrawl or Notion. Give one of those a `vault://…` string and it goes out as the credential itself, and the provider answers `401`. So: **store a reference only for a self-hosted deployment, or for a service that runs on the org's data-plane agent; otherwise store the value.** If you aren't sure which path a service takes, store the value.

| `credential_value` | Stored as | Resolves |
|---|---|---|
| `vault://<mount>/<path>#<field>` (the `#<field>` is required) | reference | against the `VAULT_ADDR` / `VAULT_TOKEN` of whatever process runs the tool — your data-plane agent or self-hosted deployment. The hosted service has no per-customer Vault setting, so it can't reach your Vault |
| `env://VAR_NAME` | reference | in the environment where the tool actually runs, so self-hosted / data-plane only. On the hosted service `env://` stores fine but **fails at execution time**: it is off by design there (`DANUBE_ALLOW_ENV_REFERENCES` is a self-hosted/dev switch, not something to ask Danube to enable) |
| the raw key | value | the working default on the hosted service — deprecated but accepted; self-hosted rejects it outright with `central_credential_ingestion_disabled` |

Never invent a variable name or vault path — use only what the user gave you, and ask which form they want if it isn't obvious. A successful store echoes `"stored_as": "reference"` or `"value"`, adding `"deprecated": true` and a `notice` when a plaintext value was stored. Note that a successful store proves nothing about whether the reference will resolve — that only shows up when the tool runs.

HTTP `429` with an `upgrade_url` means the account's plan limit is reached — tell the user; don't retry in a loop.

## Beyond tools

Available through the same connection, same guardrails:
- **Skills:** `search_skills`, `get_skill`, `create_skill`, `update_skill`, `delete_skill`
- **Workflows:** `list_workflows`, `create_workflow`, `update_workflow`, `delete_workflow`, `execute_workflow`, `get_workflow_execution`
  - A workflow can outlive the call that started it. `execute_workflow` answering
    `status: "running"` with an `execution_id` means it is **still going, not failed** —
    poll `get_workflow_execution(execution_id)`. Never re-run it: a second concurrent run
    duplicates every write the first one makes. Over `curl` you get a plain timeout rather
    than that response, so treat *any* timeout on an execute call the same way.
  - **A failed run is not an error status.** A workflow whose steps fail still answers
    normally, with `status: "failed"` in the body. Read the body's `status` and the
    per-step results — don't infer success from the absence of an error.
  - HTTP `402` blocks the run before any step executes: a free-tier account gets 5
    *successful* lifetime workflow runs that use a Danube-hosted AI step. The message says
    so verbatim ("You've used all 5 free AI-powered workflow runs…"); match on that and the
    402, not on the envelope's `code`, which currently reads `internal_error` for this case.
    Tell the user to upgrade — retrying won't help, the cap never resets.
- **Quality signal:** `get_tool_ratings`, `get_my_rating`, `submit_rating`, `report_tool`, `get_recommendations` — if a tool fails or returns bad output, `report_tool` it so it gets fixed.
- **Wallet & agents:** `get_wallet_balance`, `get_spending_limits`, `update_spending_limits`, `fund_agent_wallet`, `register_agent`, `get_agent_info`

Something not working? `{baseDir}/references/troubleshooting.md`

## Links

- Dashboard: https://danubeai.com/dashboard · Docs: https://docs.danubeai.com · OpenClaw guide: https://docs.danubeai.com/sdk/openclaw
- MCP server: https://mcp.danubeai.com/mcp · Privacy: https://danubeai.com/privacy · Terms: https://danubeai.com/terms
