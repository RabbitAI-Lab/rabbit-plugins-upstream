# Installing the `appstore-api` skill package

Prerequisites:

1. A ReplyNodes workspace API key (minted from the console); scope and entitlement checks happen at the shared control plane.
2. Your workspace gateway base URL, issued at onboarding - never assume a host.
3. Keep the key in an environment variable or secret store; do not commit or embed it anywhere.

Before distributing this package, verify it:

```sh
bash services/social-data-skills/catalog/package_check_appstore.sh   # from the repository root; must exit 0
```

## OpenClaw

1. Copy this package directory into the OpenClaw agent's skills folder so `SKILL.md` and `llms.txt` are discovered automatically.
2. Provide the long-lived fetcher key through the agent's secret configuration; use `https://api.replynodes.com` and never paste the key into a conversation.
3. Instruct naturally, for example: "Look up com.example.app with the appstore-api skill, list related apps, and report meta.availability and null counters honestly."

## Hermes

1. Register the three function definitions printed in [references/endpoints.md](references/endpoints.md) (Hermes-style function-calling section).
2. Execute each call by issuing the mapped HTTPS GET with `Authorization: Bearer YOUR_FETCHER_KEY`.
3. There are no continuation tokens: search returns one bounded page (default 20, max 50).

## ChatGPT

1. Import [references/appstore-public-v1.openapi.json](references/appstore-public-v1.openapi.json) as an action schema.
2. Choose Bearer authentication and save the fetcher key as a stored credential rather than pasting it into conversations.
3. Exactly three operations exist (`get_app`, `search_apps`, `get_similar_apps`) and all are GET-only; nothing else can be invoked.

## Claude

1. Preferred: point an MCP-compatible client at [references/appstore-mcp.schema.json](references/appstore-mcp.schema.json) (streamable HTTP transport, bearer authentication).
2. Alternative: declare the native tool-use JSON from [references/endpoints.md](references/endpoints.md) directly in your tool list.
3. Surface `meta.availability`, `meta.missing_fields`, and null counters honestly to the user instead of inventing values.

## generic HTTP

1. Call any documented route with the client of your choice; worked curl snippets live in [references/endpoints.md](references/endpoints.md).
2. Send the Authorization header on every documented request.
3. Retry only on 502/503 with backoff; treat 400/404 as terminal for the attempt and honor `Retry-After` on 429.

## MCP agents

1. Load [references/appstore-mcp.schema.json](references/appstore-mcp.schema.json) as the server manifest.
2. Substitute `{base_url}` in the transport URL with your workspace gateway base URL.
3. Expose exactly the three declared read-only tools; they map 1:1 onto the implemented operations recorded in `manifest.json`.

Uninstalling removes the copied directory and nothing else: the package
installs no daemons, hooks, or background activity of any kind.
