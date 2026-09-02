# Troubleshooting

## The skill isn't eligible / doesn't load

This skill is gated on `DANUBE_API_KEY` being set and `curl` being on `PATH`.
Check both:

```bash
test -n "$DANUBE_API_KEY" && echo "DANUBE_API_KEY is set (${#DANUBE_API_KEY} chars)"   # keys are opaque tokens, no fixed prefix
command -v curl
```

If the key lives only in `openclaw.json`, make sure it's under the skill's
entry, which is what `primaryEnv` binds to:

```json5
{ skills: { entries: { danube: { enabled: true, apiKey: "YOUR_DANUBE_API_KEY" } } } }
```

`openclaw skills list --json` shows the skill's `eligible` flag and anything `missing`.

## Danube's MCP tools don't show up in OpenClaw

```bash
openclaw mcp list                      # is "danube" saved?
openclaw mcp doctor danube --probe     # can OpenClaw connect and list tools?
openclaw mcp status
```

Common causes:

- The server was saved without `"transport":"streamable-http"` — OpenClaw then
  assumes SSE, which Danube does not serve. Re-run the `openclaw mcp set danube '{...}'`
  command from `SKILL.md`.
- The header was saved as the literal string `${DANUBE_API_KEY}` instead of
  the key value. `openclaw mcp set` stores what you type; use the actual
  key value (or switch to `"auth":"oauth"` + `openclaw mcp login danube`).
- The agent is running with the `minimal` tool profile, which hides MCP tools.
  Use `coding` or `messaging`, or check `tools.deny` for `bundle-mcp`.

Sanity-check the server and the key from the shell:

```bash
curl -s https://mcp.danubeai.com/health                      # server up? (no auth needed)
curl -s -o /dev/null -w "%{http_code}\n" "https://api.danubeai.com/v1/tools/search?query=weather" \
  -H "danube-api-key: ${DANUBE_API_KEY}"                      # 200 = key accepted, 401 = rejected
```

## Errors while executing tools

| Symptom | Cause | Fix |
|---|---|---|
| `error_type: auth_required` | The user hasn't connected that service on Danube | Send them to the `configuration_url` in the error, or https://danubeai.com/dashboard → connect the service. For API-key services the user may hand you the key to store (confirm first) |
| `invalid_grant` / "token expired" | The service's OAuth grant was revoked or expired | User re-authorizes the service in the dashboard |
| `401 Unauthorized` from `api.danubeai.com` | Bad or revoked `DANUBE_API_KEY` | Regenerate at https://danubeai.com/dashboard → Settings → API Keys |
| `403` | The API key is scoped to specific services/tools, or the org's policy blocks this tool | Tell the user what was blocked; don't work around it |
| `404 Tool not found` | Stale tool ID | Re-run `search_tools` — never reuse IDs from earlier sessions |
| `429` with `upgrade_url` | Plan usage cap reached | Stop and tell the user; don't retry in a loop |
| `429` without `upgrade_url` | Rate limit | Wait and retry once |
| `central_credential_ingestion_disabled` from `store_credential` | A self-hosted deployment refuses to hold a plaintext secret centrally | Store a reference instead — `vault://<mount>/<path>#<field>` (the `#<field>` is required), or `env://VAR_NAME` if the secret is in the environment where tools run. Ask the user which they have; never invent a name or path |
| `Failed to resolve credential reference: …` at execution time | A stored `env://` / `vault://` reference could not be read where the tool ran. The message says which: the variable isn't set, `VAULT_ADDR`/`VAULT_TOKEN` is missing, the reference is missing its `#<field>`, or `env://` is off in this deployment mode | `env://` and `vault://` resolve in the process that runs the tool — a self-hosted deployment or the data-plane agent. On the hosted service `env://` is off by design (`DANUBE_ALLOW_ENV_REFERENCES` is a self-hosted/dev switch), and there is no per-customer Vault setting, so `vault://` can't reach *your* Vault. On the hosted service, store the plaintext value instead. Otherwise have the user check the variable or the Vault path |
| `401` from the *provider* (not from `api.danubeai.com`) right after storing a reference | The service reads the stored string as the secret — `mcp_server` services and provider-specific handlers (Firecrawl, Notion, …) don't resolve references, so the `vault://…` / `env://…` text was sent as the credential | Re-store the actual value for that service. Don't read this as a bad Danube key. On a **self-hosted** deployment plaintext is refused (the row above), so an `mcp_server` service has no working store through this endpoint — say so rather than looping between the two errors |
| `402` from `execute_workflow`, message "You've used all 5 free AI-powered workflow runs…" | Free-tier account, all 5 lifetime *successful* runs using a Danube-hosted AI step are spent. Refused before any step executes, so nothing partially ran and no execution row exists | Tell the user to upgrade at https://danubeai.com/dashboard → Settings; don't retry, the cap never resets. **Match on the 402 and the message, not on the error envelope's `code`** — 402 isn't in the status→code map, so `code` currently reads `internal_error` for this. Don't read that as a Danube outage or `report_tool` it |
| Which steps count toward that cap | The hosted tools that call a model: `Danube - Webpage Summary`, `Extract Structured Data`, `Company Research`, `Discover APIs`, `Summarize Text`, `Extract Entities`, `Classify Text`, `Generate Structured Data`, `Translate Text`. `Danube - Screenshot` is pure browser capture and is free of the cap, as is any third-party tool whose name merely sounds similar | Calling these directly with `execute_tool` is unaffected — only workflows are gated. In an **instructions-mode** workflow the gate looks at `allowed_tool_ids`, so merely *offering* the orchestrator a hosted-AI tool trips it even if no step calls one; drop it from `allowed_tool_ids` if you don't need it |
| `status: "running"` with an `execution_id` from `execute_workflow` | The workflow outlived the request that started it. It was **not** cancelled and has **not** failed | Poll `get_workflow_execution(execution_id)`. Never re-run the workflow — a second concurrent run can exhaust rate limits and duplicate every write the first one makes. Over `curl` there is no such response: the request just times out (or your gateway reports its own `504`), so treat any timeout on an execute call this way |
| The run came back with `status: "failed"` but no error status | Normal. Only a run that never started is an error status; a run whose *steps* failed completes and reports itself as failed | Read the body's `status` and per-step results rather than inferring success from a 2xx |
| A result looks cut off, or `_meta.truncated` is set | The response exceeded the MCP layer's size cap (default 50000 chars; when a tool is resolved by *name*, a publisher's lower per-tool default can apply; 32000 per call inside `batch_execute_tools`). Separately, a few backend handlers cap content themselves (Firecrawl scrape/crawl, Google Drive download), and that cap applies over REST too | Read `_meta.truncation_note` for what went. Re-run with a higher `max_response_chars` (hard max 500000), or follow `_meta.cursor` if the upstream paginates. A trimmed JSON array is still valid JSON — don't treat it as malformed or `report_tool` it. A JSON *object* too big to trim by elements comes back as `{"_truncated_partial_json": …, "_truncated": true}` instead, with its own keys gone — re-request that one rather than parsing it. Note `batch_execute_tools` puts `truncated` and `cursor` at each element's top level, not under `_meta`, and raising the cap there is per call (`calls[].max_response_chars`) |
| Missing/invalid parameter errors | Schema mismatch | Re-read `parameters` (`required`, `type`, `enum`) from `get_service_tools` / `GET /tools/{id}` and ask the user for what's missing |
| Paid tool refuses to run | Wallet balance or spending limit | Show the user `get_wallet_balance` / `get_spending_limits`; only change limits if they ask |

## A tool is broken or returns wrong output

Call `report_tool(tool_id, reason, description)` with `reason` one of
`broken`, `degraded`, `incorrect_output`, `timeout`, `other` — the Danube team
reads these. A rating via `submit_rating` helps other agents too.

Pass the tool's UUID as `tool_id`: the MCP `report_tool` and `submit_rating`
tools reject anything else rather than guessing. Look it up with
`search_tools` — and if what you're closing out wasn't a marketplace tool call
at all, just skip the report instead of passing a tool name or a placeholder
string.

## Still stuck

- Docs: https://docs.danubeai.com (OpenClaw guide: https://docs.danubeai.com/sdk/openclaw)
- Dashboard: https://danubeai.com/dashboard
- Contact: https://danubeai.com/contact
