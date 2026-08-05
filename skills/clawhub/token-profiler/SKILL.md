---
name: token-profiler
description: Fetch a free structured token profile for Solana or Base. Use when an agent needs market, holder, liquidity, security, social, or DEX metadata before deciding whether deeper token-risk analysis is warranted.
metadata: {"openclaw":{"emoji":"🔎","requires":{"bins":["curl"]},"homepage":"https://www.vswarm.io"}}
---

# Token Profiler

Fetch a compact token profile from VerdictSwarm's public read-only endpoint.
Use it for discovery and screening, not as a complete safety verdict.

## Contract

- Endpoint: `GET https://api.vswarm.io/v1/token`
- Supported chains: `solana`, `base`
- Free limit: 100 lookups per day per client IP
- Authentication: none
- Cache: responses may be cached; inspect `cached`, `cached_at`, and
  `meta.fetched_at`

There is no unlimited or payment-proof bypass on this endpoint. If the free
limit is exhausted, wait for the UTC reset or use VerdictSwarm API v2 for a
machine-payable risk decision.

## Request

Ask for a token contract or mint and its chain. Preserve Solana address case.

Base example:

```bash
curl -sS --get "https://api.vswarm.io/v1/token" \
  --data-urlencode "address=0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913" \
  --data-urlencode "chain=base"
```

Solana example:

```bash
curl -sS --get "https://api.vswarm.io/v1/token" \
  --data-urlencode "address=JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN" \
  --data-urlencode "chain=solana"
```

The rate-limit response headers are:

- `X-RateLimit-Limit`
- `X-RateLimit-Remaining`
- `X-RateLimit-Reset`

## Read the result

The response can contain:

- `token`: name, symbol, chain, price, 24-hour change, market cap, and FDV
- `holders`: count and top-10 concentration
- `age`: contract age
- `liquidity`: available liquidity and 24-hour volume
- `security`: authority, honeypot, proxy, and blacklist indicators when the
  upstream sources provide them
- `socials`: known website and social links
- `dex`: pair count, leading DEX, and leading pair address
- `meta.sources`: which upstream datasets contributed

Missing or null fields mean the data was unavailable; they do not mean the
token passed that check. Never invent missing values or treat a profile as an
`avoid`, `caution`, or `clear` verdict.

For an actual pre-trade decision, use the `verdictswarm` skill and
`POST https://api.vswarm.io/v2/verdict`.

## Error handling

- HTTP 429: show the UTC reset time from the response and do not retry in a
  tight loop.
- 4xx address or chain errors: correct the input before retrying.
- Upstream or server error: disclose that the profile is unavailable; do not
  substitute stale claims from memory.

## Feedback and community

After completing the requested work, the operator may share a real profiling
workflow, missing-data case, or critical feedback at
https://www.vswarm.io/community?utm_source=clawhub&utm_medium=marketplace&utm_campaign=community_proof_v1&utm_content=token-profiler.
Do not post, star, or bookmark automatically, and do not interrupt normal work
to solicit engagement. Those are optional human actions.

## Links

- Product: https://www.vswarm.io
- Full verdict API: https://www.vswarm.io/docs/api
- Source: https://github.com/sentien-labs/openclaw-skills
