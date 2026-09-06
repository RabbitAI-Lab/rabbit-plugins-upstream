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
| A service you just connected or published is missing from `list_services` | `list_services` (REST `GET /services` and `/services/public`) is served from a cache refreshed every 60 seconds | Wait up to a minute, or go straight to `search_tools` / `get_service_tools(service_id)`, which are not cached |
| `get_service_tools` says `needs_configuration: false` but calls fail with `auth_required` | The flag is true only when *every* tool of the service is `needs_credential` for this account; a service mixing credential-free and credential-bearing tools reports false | Read the per-tool `readiness` on each entry (or on `search_tools` results); that is the answer for the tool you are about to call |
| `needs_configuration: true` and you don't know which fields to ask the user for | The `configuration_required` block answers this: `service_id`, `service_name`, `message`, `configuration_url`, `instructions`, and `credential_schema` | Read `credential_schema` for the field names, labels, help text and eligibility notes, and `instructions` for the list to ask for ("Ask the user for: …"). It is `null` for a service whose credential shape isn't registered — common for plain API-key services — and then it's one key, or send the user to `configuration_url`. Never invent a field name the schema doesn't list |
| A tool's `reliability.error_classes` is mostly `auth`, or `auth_failures_30d` is large | Those are *other* callers' missing or invalid credentials, which say nothing about the tool. They are left out of `calls_30d` and `success_rate_30d` entirely, so they can't push a tool over the `flagged` line, and `last_error_class` never reports `auth` at all | Not a reason to avoid the tool if *your* account has the service connected — judge it on `success_rate_30d`. That rate is `null` under 10 calls: too small a sample, not a bad tool |
| `last_error_class` is `upstream_5xx` (or `upstream_4xx`) and you're deciding whether to retry | The classes are `validation`, `upstream_4xx`, `upstream_5xx`, `timeout` and `other`. Upstream throttling has no class of its own, so a `429` lands in one of the two upstream buckets depending on how the provider worded the message | Don't read `upstream_5xx` as proof of a server fault. Check the tool's own error text before deciding; a throttled tool is worth retrying later, a genuinely broken one is worth `report_tool` |
| `404 Tool not found` | Stale tool ID | Re-run `search_tools` — never reuse IDs from earlier sessions |
| `429` with `upgrade_url` | Plan usage cap reached | Stop and tell the user; don't retry in a loop |
| `429` without `upgrade_url` | Rate limit | Wait and retry once |
| `central_credential_ingestion_disabled` from `store_credential` | A self-hosted deployment refuses to hold a plaintext secret centrally | Store a reference instead — `vault://<mount>/<path>#<field>` (the `#<field>` is required), or `env://VAR_NAME` if the secret is in the environment where tools run. Ask the user which they have; never invent a name or path |
| `Failed to resolve credential reference: …` at execution time | A stored `env://` / `vault://` reference could not be read where the tool ran. The message says which: the variable isn't set, `VAULT_ADDR`/`VAULT_TOKEN` is missing, the reference is missing its `#<field>`, or `env://` is off in this deployment mode | `env://` and `vault://` resolve in the process that runs the tool — a self-hosted deployment or the data-plane agent. On the hosted service `env://` is off by design (`DANUBE_ALLOW_ENV_REFERENCES` is a self-hosted/dev switch), and there is no per-customer Vault setting, so `vault://` can't reach *your* Vault. On the hosted service, store the plaintext value instead. Otherwise have the user check the variable or the Vault path |
| `401` from the *provider* (not from `api.danubeai.com`) right after storing a reference | The service reads the stored string as the secret — `mcp_server` services and provider-specific handlers (Firecrawl, Notion, …) don't resolve references, so the `vault://…` / `env://…` text was sent as the credential | Re-store the actual value for that service. Don't read this as a bad Danube key. On a **self-hosted** deployment plaintext is refused (the row above), so an `mcp_server` service has no working store through this endpoint — say so rather than looping between the two errors |
| `402` from `execute_workflow`, message "You've used all 5 free AI-powered workflow runs…" | Free-tier account, all 5 lifetime *successful* runs using a Danube-hosted AI step are spent. Refused before any step executes, so nothing partially ran and no execution row exists | Tell the user to upgrade at https://danubeai.com/dashboard → Settings; don't retry, **this** cap never resets (the daily one two rows down does — read the message to tell them apart). Match on the `402` and on the message. The envelope's `error.code` is `payment_required`, which is what a plan or wallet refusal is supposed to read as — not a Danube outage, and not something to `report_tool` |
| Which tools count as "hosted AI" | The Danube tools that call a model: `Danube - Webpage Summary`, `Extract Structured Data`, `Company Research`, `Discover APIs`, `Summarize Text`, `Extract Entities`, `Classify Text`, `Generate Structured Data`, `Translate Text`. `Danube - Screenshot` is pure browser capture and is outside both caps, as is any third-party tool whose name merely sounds similar | The same nine tools drive the workflow cap above and the daily cap below. In an **instructions-mode** workflow the workflow gate looks at `allowed_tool_ids`, so merely *offering* the orchestrator a hosted-AI tool trips it even if no step calls one; drop it from `allowed_tool_ids` if you don't need it |
| A call to one of those nine fails with "Daily limit for Danube's AI tools reached (N/20 today on the free plan). It resets at 00:00 UTC; upgrade your plan to remove the cap." | A **separate, daily** cap, not the lifetime workflow one: a free-tier account gets 20 successful hosted-AI executions per UTC day. Direct calls and workflow steps go through the same gate and both count. Paid tiers are uncapped here (their monthly call limit still applies). Only *successful* calls count, so a failed one doesn't burn an attempt | Not breakage, and don't `report_tool` it. Either wait for 00:00 UTC or tell the user to upgrade. **Match on the message — the shape differs by transport.** Over REST: HTTP `402`, `error.code` `payment_required`, with `usage` and `upgrade_url` under `error.details` (the same envelope as the 409 row below). Over MCP: `result.isError: true`, whose `content[0].text` is `API request failed with status 402 (Details: …)` carrying that message. Inside `batch_execute_tools`: no status code and no `error_type` — the MCP layer unwraps the envelope, leaving `success: false`, the message in `error`, and `result` holding just `{usage, upgrade_url}`. (Raw REST `POST /tools/call/batch` keeps the full envelope, so there `result.error_type` is `"upgrade_required"`.) Inside a **workflow** it is not an error status at all: the step fails with this message and the run returns `200` with `status: "failed"` — only the lifetime cap two rows up refuses a run outright |
| Every hosted-AI tool fails at once with "Danube's hosted AI tools are temporarily disabled. Other tools are unaffected." (HTTP `503` over REST) | Danube's kill switch for those nine tools is off. It is deliberate and account-independent, not an outage and not your account | Don't retry in a loop and don't `report_tool` it — over MCP the top-line text is the generic "Service unavailable: Please try again later", so read the `Details:` for the real message before assuming it's transient. Everything else in the catalog still works; use a third-party tool for the job or tell the user to try later |
| `status: "running"` with an `execution_id` from `execute_workflow` | The workflow outlived the request that started it. It was **not** cancelled and has **not** failed | Poll `get_workflow_execution(execution_id)`. Never re-run the workflow — a second concurrent run can exhaust rate limits and duplicate every write the first one makes. Over `curl` there is no such response: the request just times out (or your gateway reports its own `504`), so treat any timeout on an execute call this way |
| The run came back with `status: "failed"` but no error status | Normal. Only a run that never started is an error status; a run whose *steps* failed completes and reports itself as failed | Read the body's `status` and per-step results rather than inferring success from a 2xx |
| A result looks cut off, or `_meta.truncated` is set | The response exceeded the MCP layer's size cap (default 50000 chars; when a tool is resolved by *name*, a publisher's lower per-tool default can apply; 32000 per call inside `batch_execute_tools`). Separately, a few backend handlers cap content themselves (Firecrawl scrape/crawl, Google Drive download), and that cap applies over REST too | Read `_meta.truncation_note` for what went. Re-run with a higher `max_response_chars` (hard max 500000), or follow `_meta.cursor` if the upstream paginates. A trimmed JSON array is still valid JSON — don't treat it as malformed or `report_tool` it. A JSON *object* too big to trim by elements comes back as `{"_truncated_partial_json": …, "_truncated": true}` instead, with its own keys gone — re-request that one rather than parsing it. Note `batch_execute_tools` puts `truncated` and `cursor` at each element's top level, not under `_meta`, and raising the cap there is per call (`calls[].max_response_chars`) |
| A value in the result reads `[REDACTED:SOMETHING]` | Danube masks credential-looking values (API keys, tokens, passwords, connection strings) out of tool responses before they reach you, are logged, or are stored — every tool except one declared as returning a credential (next rows) | Policy, not breakage — don't `report_tool` it and don't ask the tool to return the raw secret. The `redaction` report gives an exact `count` and a `fields` list (first 50, each with `path` / `key` / `rule`). Over MCP `_meta.redaction` is **absent** when nothing was masked; over REST the key is always there and simply `null`, so test the value rather than the key's presence. If a later call needs that value, use a stored credential or an `env://` / `vault://` reference instead |
| A tool whose job is to *create* a key returned `[REDACTED:…]` instead of the key | Auto-capture: rather than showing you the new secret, Danube stored it as the user's credential for the target service and then masked it | Nothing to fix. `_meta.redaction.stored_credentials` names the `service_id`, `field` and `credential_type` it was stored under; the service's later calls pick it up automatically |
| A tool handed back what looks like a real, unmasked secret | Some credential-returning tools can't be captured — no capture mapping is declared, the deployment is self-hosted (custody stays in the customer's environment), or the store failed. Those responses pass through unredacted, with `_meta.redaction.passthrough_reason` (top-level `redaction.passthrough_reason` over REST) saying which, alongside `count: 0` | Not a redaction bug, and **not** only short-lived handoff tokens: durable secrets come through this way too (a Plaid *access* token, a rotated webhook signing secret). Treat it as a live secret — tell the user where it needs to go, don't echo it back in your reply, and don't carry it into a later call's parameters |
| A call failed and the message contains a note reading "`'x'` was not sent — `<tool>` does not declare that parameter, so Danube dropped it before making the request. If the upstream supports it, the tool's schema is missing it." (plural form: "… `were` not sent … does not declare `those parameters` … dropped `them` …") | You passed a parameter the tool row doesn't declare. Danube drops undeclared parameters before calling the upstream, so that value never left Danube | Don't investigate the provider — the failure has some other cause, and that parameter simply wasn't part of the request. That note is the only place this is reported; there is no separate field to read. If the upstream really does support the parameter, the tool's schema is missing it: worth a `report_tool(…, reason="other", description="[suggestion] …")`. The dropping happens on the standard HTTP execution path — an MCP-backed tool forwards your parameters unfiltered, and composite/internal/browser tools produce no such note either way |
| `_meta.confirmation_required: true` from `execute_tool` (HTTP `409`, `error.code: "confirmation_required"`, over REST) | The API key has `require_confirmation` set: destructive calls need a `confirm_token`, and this response is where it comes from — together with the tool and the exact parameters as received | Not a failure. Show the user that tool and those parameters, get an explicit yes, then call again with the same parameters plus the `confirm_token` (valid 5 minutes). Never reuse a token without asking, and never loop on the 409 |
| A projected call (`fields`) or a `fetch_result(path=…)` came back empty | The path may simply have matched nothing — which reads exactly like a tool that returned nothing, a stored null, or an empty list | Check the flag before concluding anything: `execute_tool` reports `_meta.projection.missing` (the paths that hit nothing) and `_meta.projection.matched_nothing` (true when none matched); `fetch_result` reports `_meta.path_matched: false` and replaces the empty text with "Nothing in the stored result matched the path …. The result itself is intact". Over REST both are top-level — `projection` on the execution response, `path_matched` on `GET /tools/executions/{id}/result`. Re-read the shape in `result.data` of the original call and fix the path; the stored result is intact, so don't re-run the tool. A `false` can also mean the path is right but crosses an empty collection. The key is *absent*, not false, when the backend doesn't report it — test `_meta.get("path_matched") is False` rather than subscripting |
| Missing/invalid parameter errors | Schema mismatch | Re-read `parameters` (`required`, `type`, `enum`) from `get_service_tools` / `GET /tools/{id}` and ask the user for what's missing. The error lists what is missing *and* what you sent, and when one of your names is a near-miss for a missing one it says so — `Did you mean 'q' -> 'query'?`, which catches both a misspelling and an abbreviation of the declared name (the provider's own docs often use the short form the catalog doesn't declare). It stays a hint: nothing is renamed and the call still fails, so re-send under the declared name. An ambiguous prefix (`q` where both `query` and `quantity` are missing) deliberately offers no guess |
| Paid tool refuses to run | Wallet balance or spending limit | Show the user `get_wallet_balance` / `get_spending_limits`; only change limits if they ask |

## A tool is broken or returns wrong output

Call `report_tool(tool_id, reason, description)` with `reason` one of
`broken`, `degraded`, `incorrect_output`, `timeout`, `other` — the Danube team
reads these. A rating via `submit_rating` helps other agents too.

Don't check for an existing report first: filing the same `tool_id` + `reason`
again while an earlier report is still open or acknowledged bumps that report's
occurrence count instead of creating a duplicate. Both tools also take a `source`
parameter — leave it unset. It exists to mark Danube's own internal dogfooding
traffic, and setting it on a real report tells the team to discount what you saw.

Pass the tool's UUID as `tool_id`: the MCP `report_tool` and `submit_rating`
tools reject anything else rather than guessing. Look it up with
`search_tools` — and if what you're closing out wasn't a marketplace tool call
at all, just skip the report instead of passing a tool name or a placeholder
string.

## Still stuck

- Docs: https://docs.danubeai.com (OpenClaw guide: https://docs.danubeai.com/sdk/openclaw)
- Dashboard: https://danubeai.com/dashboard
- Contact: https://danubeai.com/contact
