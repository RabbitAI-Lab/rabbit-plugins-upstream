---
name: shruwd
description: Track how a brand shows up in ChatGPT and Google AI Overviews answers, and act on the findings, through Shruwd's MCP server.
version: 1.0.0
metadata:
  openclaw:
    requires:
      env:
        - SHRUWD_API_KEY
      bins:
        - npx
    primaryEnv: SHRUWD_API_KEY
    envVars:
      - name: SHRUWD_API_KEY
        required: true
        description: Shruwd API key (dashboard → Account → API keys). Needs a Shruwd account; see https://shruwd.io/pricing.
      - name: SHRUWD_API_URL
        required: false
        description: API base URL. Defaults to https://shruwd.io/api/v1.
    homepage: https://shruwd.io
---

# Shruwd

Shruwd measures a brand's AI-search visibility: how often ChatGPT and Google AI Overviews mention it, its share
of voice against competitors, and which AI crawlers read its site. This skill connects the
`shruwd-mcp` server (source: https://github.com/ilpr/shruwd-mcp, MIT) so you can set up a brand,
track prompts and competitors, and read results.

**External service.** Every tool call goes to the Shruwd API at shruwd.io with the user's API key.
The user needs a Shruwd account. The key is bound to one workspace and acts with the user's role
in it.

## Setup

Add the server, pinned to a reviewed version:

```bash
openclaw mcp add shruwd --command npx --arg -y --arg shruwd-mcp@0.1.3 --env SHRUWD_API_KEY="$SHRUWD_API_KEY"
openclaw mcp doctor shruwd --probe
```

Or call it one-off through mcporter:

```bash
mcporter call --stdio "npx -y shruwd-mcp@0.1.3" shruwd_get_workspace
```

## Using it

1. Start with `shruwd_get_workspace` to see the plan, usage and existing brands.
2. New brand: `shruwd_create_brand` (needs `owner`), then `shruwd_add_prompts` and
   `shruwd_add_competitor`.
3. `shruwd_run_measurement` starts a cycle. Results arrive over the following hours, so don't
   report numbers until `shruwd_list_cycles` shows the cycle has closed.
4. Read the results with `shruwd_get_visibility`, `shruwd_get_visibility_series` and
   `shruwd_get_crawlers`.

Nothing is hard-deleted. Archiving a brand stops scheduling and keeps its history, removing a
prompt deactivates it, and removing a competitor closes it as of now.

Full docs: https://shruwd.io/docs · Machine-readable: https://shruwd.io/llms.txt
