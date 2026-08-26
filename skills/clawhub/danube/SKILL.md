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
        description: Danube API key (starts with dk_) from https://danubeai.com/dashboard → Settings → API Keys
    always: false
---

# Danube — Governed Tool Access for Agents

Danube makes an organization's own tools — plus a large and growing catalog of ready-made services — callable by AI agents through a single API key, with permissions, spending limits, and an audit trail handled by the platform. The catalog changes constantly and includes tools the user's organization connected privately, so **never assume what is available — search first.**

## Guardrails (read these first)

- **Read freely, act with consent.** Discovery — listing services, searching tools, reading schemas, checking ratings, balances, or limits — needs no confirmation. Before any action that **writes, sends, posts, deletes, purchases, spends wallet funds, stores a credential, changes spending limits, or creates/updates/deletes a skill or workflow** — and before **any batch execution** — show the user the exact tool and parameters and get an explicit "yes".
- **Never invent credentials.** Only store an API key the user has explicitly handed you in this conversation, and confirm before storing. Otherwise send them to https://danubeai.com/dashboard to connect the service themselves.
- **Least data.** Pass only the parameters the task needs; don't forward unrelated personal data to third-party services.
- **Respect limits.** Don't raise spending limits or fund wallets unless the user asks for exactly that.
- **Report specifics.** After executing, say which tool ran, with what inputs, and what came back — not just "done".

## Setup

### 1. Get an API key

From the dashboard: https://danubeai.com/dashboard → Settings → API Keys (keys start with `dk_`).

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

`428` = not approved yet (poll every `interval` seconds) · `200` = `{"api_key": "dk_..."}` · `410` = expired, start over.

### 2. Make the key available to OpenClaw

Set `DANUBE_API_KEY` in the environment, or in `openclaw.json`:

```json5
{ skills: { entries: { danube: { apiKey: "dk_..." } } } }
```

### 3a. Connect natively over MCP (recommended)

OpenClaw has a built-in MCP client. Register Danube's server once and its tools become ordinary OpenClaw tools (`search_tools`, `execute_tool`, …):

```bash
openclaw mcp set danube '{"url":"https://mcp.danubeai.com/mcp","transport":"streamable-http","headers":{"danube-api-key":"dk_..."}}'
openclaw mcp doctor danube --probe
```

Use the real key value in `headers` (not `${DANUBE_API_KEY}`). The server also speaks MCP OAuth: use `"auth":"oauth"` instead of `headers`, then `openclaw mcp login danube`.

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
| Run a tool | `execute_tool(tool_id, parameters)` | `POST /tools/call/{tool_id}` with `{"tool_input": {…}}` |
| Run up to 10 at once | `batch_execute_tools(calls)` | `POST /tools/call/batch` |

Discovery tips:
- Describe the *outcome* in natural language (`"send an email"`, `"create a GitHub issue"`, `"translate text"`); search is semantic.
- If the first query misses, rephrase and try again before concluding a capability doesn't exist. The catalog is far larger than you'd guess.
- Read the tool's parameter schema (`required`, `type`, `enum`, `tips`) before executing; ask the user for anything required that you don't have. Never reuse tool IDs from memory — search again.

### When a tool needs credentials

A result containing `"error_type": "auth_required"` means this user hasn't connected that service yet:
1. Prefer sending the user to the `configuration_url` in the error (or https://danubeai.com/dashboard) to connect it — the only path for OAuth services such as Gmail, Slack, or Google Calendar.
2. For API-key services, if the user explicitly gives you the key and confirms, call `store_credential(service_id, credential_type="bearer", credential_value=…)`, then retry.

HTTP `429` with an `upgrade_url` means the account's plan limit is reached — tell the user; don't retry in a loop.

## Beyond tools

Available through the same connection, same guardrails:
- **Skills:** `search_skills`, `get_skill`, `create_skill`, `update_skill`, `delete_skill`
- **Workflows:** `list_workflows`, `create_workflow`, `update_workflow`, `delete_workflow`, `execute_workflow`, `get_workflow_execution`
- **Quality signal:** `get_tool_ratings`, `get_my_rating`, `submit_rating`, `report_tool`, `get_recommendations` — if a tool fails or returns bad output, `report_tool` it so it gets fixed.
- **Wallet & agents:** `get_wallet_balance`, `get_spending_limits`, `update_spending_limits`, `fund_agent_wallet`, `register_agent`, `get_agent_info`

Something not working? `{baseDir}/references/troubleshooting.md`

## Links

- Dashboard: https://danubeai.com/dashboard · Docs: https://docs.danubeai.com · OpenClaw guide: https://docs.danubeai.com/sdk/openclaw
- MCP server: https://mcp.danubeai.com/mcp · Privacy: https://danubeai.com/privacy · Terms: https://danubeai.com/terms
