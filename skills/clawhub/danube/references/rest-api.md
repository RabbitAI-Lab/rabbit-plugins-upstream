# Danube over plain HTTP (no MCP required)

Everything the Danube MCP tools do is also a REST call. Use this when the
agent only has `curl` and `DANUBE_API_KEY` (which is exactly what this skill
gates on), or when you want to see raw responses.

```bash
BASE="https://api.danubeai.com/v1"
AUTH="danube-api-key: ${DANUBE_API_KEY}"
```

All examples below assume those two variables. Responses are JSON.

## Discover

```bash
# Semantic search across every tool you can see (catalog + your org's private tools).
# Describe the outcome, not the API: "send an email", "create a GitHub issue", "translate text".
curl -s -G "$BASE/tools/search" -H "$AUTH" --data-urlencode "query=send an email"

# Narrow to one service, or by tag:
curl -s -G "$BASE/tools/search" -H "$AUTH" --data-urlencode "query=issue" --data-urlencode "service_id=<SERVICE_ID>"

# All services visible to this key (includes the organization's private services).
curl -s "$BASE/services" -H "$AUTH"
curl -s "$BASE/services?service_type=api" -H "$AUTH"        # api | mcp_server | website | internal

# Public catalog only — no key needed. category = communication | productivity | development |
# data | finance | marketing | social | analytics | security | infrastructure | ai_ml | design |
# education | health | other. sort = popular | new | name | trending.
curl -s "$BASE/services/public?category=communication&sort=popular&limit=20"

# Every tool of one service.
curl -s "$BASE/services/<SERVICE_ID>/tools" -H "$AUTH"

# Full definition of one tool (parameter schema, pricing).
curl -s "$BASE/tools/<TOOL_ID>" -H "$AUTH"
```

A tool object looks like:

```json
{
  "id": "6f0c4361-d0cc-45df-8ee6-87b9cc1e0d37",
  "name": "Gmail - Send Email",
  "description": "...",
  "service_id": "...",
  "parameters": {
    "to":      {"name": "to", "type": "string", "description": "...", "required": true,  "location": "body"},
    "subject": {"name": "subject", "type": "string", "description": "...", "required": true, "location": "body"},
    "body":    {"name": "body", "type": "string", "description": "...", "required": false, "location": "body", "enum": null, "default": null}
  },
  "is_paid": false,
  "price_per_call_cents": null,
  "tips": "optional usage notes written by the publisher"
}
```

Read `required`, `type`, `enum`, and `tips` before executing. Ask the user
for any required value you don't have.

## Execute

Get the user's explicit confirmation first for anything that writes, sends,
deletes, spends, or stores a credential (see the guardrails in `SKILL.md`).

```bash
# One tool. Wrap the parameters in "tool_input".
curl -s -X POST "$BASE/tools/call/<TOOL_ID>" \
  -H "$AUTH" -H "Content-Type: application/json" \
  -d '{"tool_input": {"to": "someone@example.com", "subject": "Hello", "body": "Hi there"}}'

# Up to 10 independent calls in one request. Each entry succeeds or fails on its own.
curl -s -X POST "$BASE/tools/call/batch" \
  -H "$AUTH" -H "Content-Type: application/json" \
  -d '{"calls": [
        {"tool_id": "<TOOL_ID_1>", "tool_input": {"q": "weather in Oslo"}},
        {"tool_id": "<TOOL_ID_2>", "tool_input": {"text": "hello", "target_lang": "DE"}}
      ]}'
# → {"results": [{"tool_id": "...", "success": true, "result": {...}, "error": null}, ...]}
```

### Reading results

| You see | It means | Do |
|---|---|---|
| `{"status": "success", "result": {...}}` (or the raw provider payload) | Worked | Report the specifics to the user |
| `{"status": "error", "error_type": "auth_required", "configuration_url": "..."}` | This user hasn't connected the service yet | Send the user to `configuration_url` (or https://danubeai.com/dashboard). For API-key services, if the user hands you a key and confirms, store it (see below) and retry |
| HTTP `401` | `DANUBE_API_KEY` is missing, wrong, or revoked | Ask the user to check Settings → API Keys |
| HTTP `403` | This API key is restricted (`allowed_services` / `allowed_tools`) or the tool is outside the org's policy | Tell the user which tool was blocked; don't retry |
| HTTP `404` | Tool ID no longer exists | Search again — never reuse IDs from memory |
| HTTP `429` with `upgrade_url` | Plan usage limit reached | Tell the user; don't loop |
| HTTP `429` without it | Rate limit | Back off and retry once |

## Credentials the user gives you

Only after the user explicitly provides a key in the conversation and confirms
they want it stored:

```bash
curl -s -X POST "$BASE/credentials/store" \
  -H "$AUTH" -H "Content-Type: application/json" \
  -d '{"service_id": "<SERVICE_ID>", "credential_type": "bearer", "credential_value": "<KEY THE USER GAVE YOU>"}'
# credential_type: "bearer" or "api_key" — the tool's schema / auth_required error says which
# → {"success": true, "service_id": "...", "service_name": "...",
#    "credential_type": "bearer", "stored_as": "value",
#    "deprecated": true, "notice": "Storing plaintext credential values ... is deprecated ..."}
```

### References instead of raw secrets — where they work

A `credential_value` matching `^(env|vault)://` is stored as a **reference**:
a pointer resolved when the tool runs, rather than the secret itself.

Resolution is **not** wired into every execution path. It happens on the
standard HTTP auth-injection path — an `api` service whose tool isn't one of
the provider-specific composite handlers — and in the in-VPC data-plane agent,
which runs the services an org has marked `local_only`. Services of type
`mcp_server`, and the composite handlers (Firecrawl, Notion, and friends), read
the stored string **as the secret** — so a `vault://…` string is sent as the
credential and the provider answers `401`, not a resolution error. Store a
reference only for a self-hosted deployment or a service that runs on the
data-plane agent; otherwise store the value. When in doubt, store the value.

```bash
# HashiCorp Vault KV v2. The #<field> suffix is required — vault://path/to/secret
# without it is rejected at resolve time, whatever the API's deprecation notice says.
# Read with the VAULT_ADDR / VAULT_TOKEN of the process that runs the tool: your
# data-plane agent or self-hosted deployment. The hosted service has no per-customer
# Vault setting, so it cannot reach your Vault.
curl -s -X POST "$BASE/credentials/store" \
  -H "$AUTH" -H "Content-Type: application/json" \
  -d '{"service_id": "<SERVICE_ID>", "credential_type": "bearer", "credential_value": "vault://secret/acme/api#token"}'

# Environment variable: resolved in the environment where the tool actually runs, so this
# is for self-hosted / data-plane deployments only. The hosted service accepts the store
# and then fails at execution time — env:// is off by design there (DANUBE_ALLOW_ENV_REFERENCES
# is a self-hosted/dev switch, not something Danube enables for hosted accounts).
curl -s -X POST "$BASE/credentials/store" \
  -H "$AUTH" -H "Content-Type: application/json" \
  -d '{"service_id": "<SERVICE_ID>", "credential_type": "bearer", "credential_value": "env://ACME_API_KEY"}'
```

The response echoes `"stored_as": "reference"` and carries no `deprecated`
flag — but a successful store says nothing about whether the reference will
resolve; that only surfaces when the tool runs. A plaintext value is still
accepted on the hosted service (deprecated); self-hosted deployments reject it
with HTTP `400`. Every API error goes through one envelope, so the token you
match on is at `error.details.error`, not at the top level:

```json
{"error": {"code": "validation_error",
           "message": "{'error': 'central_credential_ingestion_disabled', 'hint': '...'}",
           "details": {"error": "central_credential_ingestion_disabled",
                       "hint": "store a reference (env:// or vault://) or configure the data-plane secret resolver"}}}
```

(`message` is a Python `repr` of the same dict, single-quoted — read
`error.details`, not `error.message`.) The MCP `store_credential` tool reports
the same condition differently: HTTP `200` with `{"success": false, "error":
"central_credential_ingestion_disabled"}`, when the MCP server runs in the same
deployment mode as the backend. Never invent a variable name or vault path: use
only what the user gave you.

Stored credentials are encrypted at rest, scoped to the user, and never
returned by any endpoint. OAuth services (Gmail, Slack, Google Calendar, …)
can only be connected by the user in the dashboard.

## Skills and workflows

```bash
curl -s -G "$BASE/skills/search" -H "$AUTH" --data-urlencode "query=summarize a webpage" --data-urlencode "limit=5"
curl -s "$BASE/skills/<SKILL_ID>" -H "$AUTH"
curl -s "$BASE/workflows/public" -H "$AUTH"
curl -s "$BASE/workflows/<WORKFLOW_ID>" -H "$AUTH"

# Run one (same confirmation rule as any other write), then poll its execution.
# Name the execution yourself with a UUID you generate: a run can outlive the HTTP
# request that started it, and if you didn't supply an id up front a timeout leaves
# you with no way to address the run that is still in flight. (The MCP
# execute_workflow tool does this for you; over curl it's on you.)
# Use a FRESH UUID each run: an unparseable one is a 400, and so is reusing one that
# already names an execution.
EXEC_ID=$(uuidgen | tr 'A-Z' 'a-z')   # or python3 -c 'import uuid;print(uuid.uuid4())'
curl -s -X POST "$BASE/workflows/<WORKFLOW_ID>/execute" \
  -H "$AUTH" -H "Content-Type: application/json" \
  -d "{\"inputs\": {\"url\": \"https://example.com\"}, \"execution_id\": \"$EXEC_ID\"}"
curl -s "$BASE/workflows/executions/$EXEC_ID" -H "$AUTH"
```

**A non-2xx is not how a workflow reports failure.** A run whose *steps* failed comes back
`200` with `status: "failed"` in the body and the failure recorded per step. Read the
body's `status`. The cases below are the ones specific to executing a workflow; the usual
`401` (bad key) and `422` (malformed body) apply here as everywhere else.

| Status | Means | Do |
|---|---|---|
| `200`, body `status: "failed"` | The run started and one or more steps failed | Read the per-step results — this is where step errors live, not in an HTTP code |
| `404` | No such workflow, or it's private and not yours. A malformed workflow id lands here too, not on a `400` | Search or list workflows again — don't retry the id |
| `402` | Free-tier account, all 5 lifetime *successful* runs using a Danube-hosted AI step are spent. Refused before any step ran, so nothing is half-done and no execution row exists | Tell the user to upgrade; the cap never resets. Match on the `402` and on `error.message` ("You've used all 5 free AI-powered workflow runs…") — `error.code` reads `internal_error` here, since 402 isn't in the status→code map |
| `400` | The execution record couldn't be created — in practice a reused or unparseable `execution_id` | Generate a fresh UUID and re-POST |
| a timeout, or your gateway's own `504` | The run outlived the HTTP request. Not cancelled, not failed — Danube itself never returns 504 here | Poll `GET /workflows/executions/$EXEC_ID`. Never re-POST — a second concurrent run duplicates every write the first one makes |

Every *error* response above uses the one envelope documented earlier in this file —
`error.code` / `error.message` / `error.details`. There is no top-level `detail` key.

## Getting an API key without the dashboard (device flow)

```bash
curl -s -X POST "$BASE/auth/device/code" -H "Content-Type: application/json" -d '{"client_name": "OpenClaw"}'
# → {"device_code": "...", "user_code": "XXXX-XXXX", "verification_url": "https://...", "expires_in": 600, "interval": 5}
# The USER opens verification_url and enters user_code. Then poll:
curl -s -X POST "$BASE/auth/device/token" -H "Content-Type: application/json" -d '{"device_code": "<DEVICE_CODE>"}'
# 428 authorization_pending → wait `interval` seconds and poll again
# 200 {"api_key": "…"}     → done; store it as DANUBE_API_KEY (opaque token, no fixed prefix)
# 410 expired_token       → start over
```

Full reference: https://docs.danubeai.com/api-reference/introduction
