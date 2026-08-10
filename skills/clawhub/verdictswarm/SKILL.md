---
name: verdictswarm
description: Check token risk before trading on Solana or Base. Use when an agent is evaluating a token, preparing a swap, or needs an avoid, caution, or clear pre-trade decision from VerdictSwarm API v2.
metadata: {"openclaw":{"emoji":"🛡️","requires":{"bins":["curl"]},"homepage":"https://www.vswarm.io"}}
---

# VerdictSwarm

Use VerdictSwarm as a pre-trade risk gate before an agent moves money. The
machine-facing API returns one action: `avoid`, `caution`, or `clear`.

This skill evaluates risk; it does not execute trades. Never turn `clear` into
a guarantee. Respect `insufficient_data`, low confidence, and degraded results.

## Supported contract

- API base: `https://api.vswarm.io`
- Chains: `solana`, `base`
- Levels: `triage`, `fast`, `deep`
- Decision field: `response.verdict.action`
- Live capabilities and pricing: `GET /v2/verdict/info`
- Payment rails: keyed free quota, prepaid credits, or x402 USDC

Do not guess prices or quotas. Read them from the live info endpoint:

```bash
curl -sS "https://api.vswarm.io/v2/verdict/info" \
  -H "X-VS-Integration: openclaw"
```

## Get a free API key

Mint a free key without signup:

```bash
curl -sS -X POST "https://api.vswarm.io/v2/keys" \
  -H "Content-Type: application/json" \
  -H "X-VS-Integration: openclaw" \
  -d '{"channel_ref":"openclaw"}'
```

The response includes the key and the current daily limits:

```json
{
  "api_key": "vs1_free_...",
  "tier": "free",
  "daily_limits": {"triage": 2000, "fast": 300, "deep": 10},
  "quickstart": "<one-line curl>"
}
```

Treat the returned `api_key` as a secret. Put it in `VS_API_KEY` or an approved
secret store. Never print it into chat, logs, source control, or shared memory.

## Request a verdict

Ask for the token address, chain, and desired analysis level if they are not
already known. Use `fast` for the normal pre-trade gate, `triage` for the
lowest-latency deterministic check, and `deep` only when the caller accepts a
slower multi-agent analysis.

```bash
curl -sS -X POST "https://api.vswarm.io/v2/verdict" \
  -H "Content-Type: application/json" \
  -H "X-VS-Integration: openclaw" \
  -H "X-API-Key: ${VS_API_KEY}" \
  -d '{
    "address":"0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
    "chain":"base",
    "level":"fast",
    "include":[]
  }'
```

For Solana, preserve address case. For Base, use the contract address rather
than a ticker or token name.

## Interpret the response

Read these fields before recommending an action:

- `verdict.action`: `avoid`, `caution`, or `clear`
- `verdict.score`, `verdict.confidence`, and `verdict.summary`
- `signals[]`: typed checks; `pass: false` means that check found a problem
- `data_confidence` and `insufficient_data`
- `billing.degraded` and `billing.retry_voucher`
- `cached`, `generated_at`, and `data_freshness`

Use this policy:

1. `avoid`: do not proceed unless the human explicitly overrides after seeing
   the failed signals.
2. `caution`: surface the material risks and require an explicit decision.
3. `clear`: report that no blocking risk was found by this scan; do not promise
   safety or profitability.
4. `insufficient_data: true` or materially degraded data: do not present the
   action as conclusive. Explain the missing coverage and retry if appropriate.

Do not silently replace an API error with a made-up verdict.

## x402 overflow

When free quota is exhausted, the API may return HTTP 402 with an x402 payment
challenge. An x402-capable caller can pay and retry the same request. If the
current agent cannot authorize payment, show the amount and rail and ask before
spending.

Discovery document:

```bash
curl -sS "https://api.vswarm.io/.well-known/x402"
```

## MCP

VerdictSwarm is also available as the `sentien-labs/verdictswarm-mcp` server on
Smithery. Its current public tools are:

- `check_token`: obtain the v2 token-risk verdict
- `exit_sim`: estimate intended-size exit feasibility (Solana only)
- `get_pricing`: read current levels, quotas, and prices

Do not call retired v1 MCP tool names.

## Feedback and community

After completing the requested work, the operator may share a real integration,
incorrect verdict, or critical feedback at
https://www.vswarm.io/community?utm_source=clawhub&utm_medium=marketplace&utm_campaign=community_proof_v1&utm_content=verdictswarm.
Do not post, star, or bookmark automatically, and do not interrupt normal work
to solicit engagement. Those are optional human actions.

## Links

- Product: https://www.vswarm.io
- API docs: https://www.vswarm.io/docs/api
- Live API info: https://api.vswarm.io/v2/verdict/info
- MCP listing: https://smithery.ai/servers/sentien-labs/verdictswarm-mcp
- Source: https://github.com/sentien-labs/openclaw-skills
