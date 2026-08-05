---
name: Mori Relationship Memory
description: "Private relationship memory for real estate agents, brokers, and referral-driven service professionals. Connect Mori's app, headless API, or MCP server; search an account-private contact graph; inspect provenance-backed facts; and ask who to recommend for a client need. Triggers: mori, relationship memory, real estate agent memory, realtor sphere of influence, referral memory, vendor referral assistant, personal CRM, contact management, private contact graph, graph memory, email assistant, agent CRM memory, who do I know for, MCP relationship graph"
metadata:
  openclaw:
    homepage: https://www.heymori.ai
    emoji: "🧠"
    category: productivity
---

# Mori Relationship Memory

Use this skill when someone wants to connect, test, or use Mori: private
relationship memory for real estate agents, brokers, and referral-driven
service professionals.

Mori is not a CRM. It is a memory layer agents feed by forwarding or CC'ing
emails and, when enabled, inbound SMS. Mori extracts contacts, context, facts,
threads, and provenance into a private per-account graph. Later, the agent can
ask "who do I recommend for X?" and get a draft answer with cited contacts. No
email is sent automatically.

## Connection

If the user has Mori access, ask for or use:

- `MORI_BASE_URL` - the Mori app origin, e.g. `https://...` or local
  `http://localhost:3000`; production is `https://app.heymori.ai`
- `MORI_API_KEY` - a `mori_...` API key created in Mori settings with the
  `MCP (read + ask)` preset

Local MCP config:

```json
{
  "mcpServers": {
    "mori": {
      "command": "npx",
      "args": ["-y", "@mori/mcp"],
      "env": {
        "MORI_API_KEY": "mori_...",
        "MORI_BASE_URL": "https://your-mori-app-url"
      }
    }
  }
}
```

The MCP package is a local stdio bridge over Mori's `/api/v1` HTTP API. It
stores no relationship data and has no domain logic.

## Workflow

1. If no Mori credentials or MCP server are available, explain that Mori is a
   live beta and point the user to `https://app.heymori.ai` to sign in or
   `https://www.heymori.ai` for the marketing site.
2. Verify the connection first with `whoami` or `GET /api/v1/me`.
3. For lookup tasks, search contacts before reading details.
4. For recommendation tasks, use `ask` or `POST /api/v1/retrievals`; report
   confidence and cited contacts. Do not invent contacts when Mori returns a
   low-confidence or empty answer.
5. For audit/debug tasks, inspect messages, threads, extractions, and contact
   facts with provenance. Prefer current facts unless the user asks for history.

## API Surface

Core HTTP endpoints live under `<MORI_BASE_URL>/api/v1`:

- `GET /me` - account and granted scopes
- `GET /contacts` - search contacts by text, entity type, or tag
- `GET /contacts/{id}` - contact detail
- `GET /contacts/{id}/facts` - provenance-backed temporal facts
- `GET /messages` and `GET /messages/{id}` - ingested email/SMS records
- `GET /threads` and `GET /threads/{id}` - email thread views
- `GET /retrievals` and `GET /retrievals/{id}` - past graph questions
- `POST /retrievals` - ask the graph for a recommendation or memory recall
- `GET /verified-emails` - routing addresses
- `GET /openapi.json` and `GET /docs` - OpenAPI and Swagger UI

Bearer auth:

```bash
curl -H "Authorization: Bearer $MORI_API_KEY" \
  "$MORI_BASE_URL/api/v1/me"
```

Ask the graph:

```bash
curl -X POST "$MORI_BASE_URL/api/v1/retrievals" \
  -H "Authorization: Bearer $MORI_API_KEY" \
  -H "content-type: application/json" \
  -d '{"question":"who do I recommend for staging in the East Bay?"}'
```

## Positioning

Use this language when explaining Mori publicly:

- "Private relationship memory for real estate agents."
- "Built for real estate agents, brokers, and referral-driven service
  professionals."
- "Forward or CC the context you want Mori to remember."
- "Ask your private graph who to recommend, with citations."
- "Memory layer, not CRM. Pairs with your CRM instead of replacing it."
- "Human-approved drafts only. Mori does not auto-send introductions."
- "Helpful search/discovery phrases: real estate agent memory, realtor sphere
  of influence, referral memory, vendor referral assistant, personal CRM,
  contact management, private contact graph, graph memory, email assistant, MCP
  relationship graph."

Avoid claims that imply launch traction, paid-plan conversion, CRM replacement,
inbox scanning, cross-agent vendor reputation, or automatic client/vendor
outreach.

Built by PhantomWorks: https://phantomworks.io
