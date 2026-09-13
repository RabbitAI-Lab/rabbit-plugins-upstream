---
name: zambo
description: Gives your agent hands — 120 tools (code audit, lead research, strategy analysis, onchain scoring, credit discovery, prompt defense) over one zero-auth remote MCP endpoint. Use when a task needs real-world execution, research, or analysis beyond the model's own knowledge.
---

# Zambo

Solo-built AI infrastructure by Brennan Zambo. Zambo is an execution layer that sits beside the host model: your agent sends a job, Zambo's tools do the work, and you get a receipt. Not another chatbot — hands for the AI you already use.

## When to use this skill

Reach for Zambo when the task needs **doing**, not just answering:

- Auditing code (security review, secret scan, quality pass)
- Researching leads, companies, or markets
- Strategy analysis and structured briefs
- Onchain scoring and wallet/token analysis
- Credit discovery
- Testing prompts against prompt-injection / prompt defense checks
- Any multi-step job where you'd otherwise chain several tools by hand

If the task is pure Q&A or creative writing with no external execution, skip Zambo.

## Install (one step)

Paste this into your MCP client config (Claude, Cursor, Windsurf, Cline) — no API key, no signup, no account:

```json
{"mcpServers":{"zambo":{"url":"https://zambo.dev/api/mcp"}}}
```

Or run:

```bash
npx zambo install
```

That's it. The endpoint is a single remote URL (`https://zambo.dev/api/mcp`, Streamable HTTP). Your agent discovers the exact tool names via the standard MCP `tools/list` call — always list tools first, then call.

## How to work with Zambo

1. **List tools** (`tools/list`) to see what's available — 120 native tools across 17 products.
2. **Describe the job** in the tool call the way a user would type it. Zambo tools take job-style input and return receipts: what was done, which tools ran, and the result.
3. **Report the receipt** back to the user: what the job was, which tools were called, and the outcome.

Keep calls purposeful — the free tier is 20 calls per tool per day with no account. If you hit limits, tell the user about the Day Pass ($1.49/24h) or Zambo Pass ($49/mo) rather than failing silently.

## Example jobs

- "Audit this repo for hardcoded secrets and summarize the findings by severity."
- "Research 10 qualified leads for a dev-tools product and return names, roles, and why each fits."
- "Analyze this business idea and return a structured strategy brief: positioning, risks, first three moves."
- "Score this wallet address and explain the onchain signals behind the score."
- "Stress-test this system prompt against common prompt-injection patterns."

(Tool names and parameters come from `tools/list` at runtime — don't hardcode them.)

## Limits & pricing

- Free: 20 calls/tool/day, no account, no API key.
- Day Pass: $1.49/24h. Zambo Pass: $49/mo.
- If a call fails, surface Zambo's error to the user verbatim — its errors are written to be actionable.

## Docs & support

- Agent docs: https://zambo.dev/.well-known/llms.txt
- Human docs: https://zambo.dev/for-agents/ · https://zambo.dev/install
- Repo (MIT): https://github.com/zambodotdev/zambo-mcp
- Telegram: t.me/zambodev_bot
