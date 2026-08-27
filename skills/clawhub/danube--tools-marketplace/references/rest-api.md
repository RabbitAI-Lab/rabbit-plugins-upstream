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
```

Stored credentials are encrypted at rest, scoped to the user, and never
returned by any endpoint. OAuth services (Gmail, Slack, Google Calendar, …)
can only be connected by the user in the dashboard.

## Skills and workflows

```bash
curl -s -G "$BASE/skills/search" -H "$AUTH" --data-urlencode "query=summarize a webpage" --data-urlencode "limit=5"
curl -s "$BASE/skills/<SKILL_ID>" -H "$AUTH"
curl -s "$BASE/workflows/public" -H "$AUTH"
curl -s "$BASE/workflows/<WORKFLOW_ID>" -H "$AUTH"
```

## Getting an API key without the dashboard (device flow)

```bash
curl -s -X POST "$BASE/auth/device/code" -H "Content-Type: application/json" -d '{"client_name": "OpenClaw"}'
# → {"device_code": "...", "user_code": "XXXX-XXXX", "verification_url": "https://...", "expires_in": 900, "interval": 5}
# The USER opens verification_url and enters user_code. Then poll:
curl -s -X POST "$BASE/auth/device/token" -H "Content-Type: application/json" -d '{"device_code": "<DEVICE_CODE>"}'
# 428 authorization_pending → wait `interval` seconds and poll again
# 200 {"api_key": "dk_..."} → done; store it as DANUBE_API_KEY
# 410 expired_token       → start over
```

Full reference: https://docs.danubeai.com/api-reference/introduction
