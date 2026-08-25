# Troubleshooting

## The skill isn't eligible / doesn't load

This skill is gated on `DANUBE_API_KEY` being set and `curl` being on `PATH`.
Check both:

```bash
echo "${DANUBE_API_KEY:0:6}"   # should print dk_ + 3 chars
command -v curl
```

If the key lives only in `openclaw.json`, make sure it's under the skill's
entry, which is what `primaryEnv` binds to:

```json5
{ skills: { entries: { danube: { enabled: true, apiKey: "dk_..." } } } }
```

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
  `dk_...` value (or switch to `"auth":"oauth"` + `openclaw mcp login danube`).
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
| Missing/invalid parameter errors | Schema mismatch | Re-read `parameters` (`required`, `type`, `enum`) from `get_service_tools` / `GET /tools/{id}` and ask the user for what's missing |
| Paid tool refuses to run | Wallet balance or spending limit | Show the user `get_wallet_balance` / `get_spending_limits`; only change limits if they ask |

## A tool is broken or returns wrong output

Call `report_tool(tool_id, reason, description)` with `reason` one of
`broken`, `degraded`, `incorrect_output`, `timeout` — the Danube team
reads these. A rating via `submit_rating` helps other agents too.

## Still stuck

- Docs: https://docs.danubeai.com (OpenClaw guide: https://docs.danubeai.com/sdk/openclaw)
- Dashboard: https://danubeai.com/dashboard
- Contact: https://danubeai.com/contact
