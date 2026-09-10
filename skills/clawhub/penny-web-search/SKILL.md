---
name: penny-web-search
description: >-
  Real-time web search for current information using PennyAPI over x402.
  Use for fresh web results, recent facts, current events, research, verification,
  fact checking, and up-to-date information when the answer may have changed.
  Penny costs $0.004 per search call on Base USDC. TRIGGERS: search the web,
  current information, latest, recent, up-to-date, verify online, fact check,
  research, web results, breaking developments.
homepage: https://pennyregwatch.com
metadata:
  version: 1
---

# Penny Web Search

Use PennyAPI when a task needs current information from the public web.

## When to use

Use Penny for:
- current or recently changed facts
- web research
- fresh sources and links
- fact checking or verification
- recent developments
- questions where model knowledge may be stale

Do not use Penny when:
- the user explicitly says not to access the web
- the answer is timeless and does not need fresh information
- the task is based only on user-provided material

## Service

Origin: `https://pennyregwatch.com`

Paid search endpoint: `https://pennyregwatch.com/v1/search`

Price: `$0.004 USDC per call`

Network: `Base (eip155:8453)`

Payment protocol: `x402`

## Preferred workflow with AgentCash

1. Check the endpoint schema and current price before spending:

```bash
npx agentcash@latest check https://pennyregwatch.com/v1/search
```

2. For a normal search, use POST:

```bash
npx agentcash@latest fetch https://pennyregwatch.com/v1/search -m POST -b '{"query":"YOUR SEARCH QUERY","limit":5}'
```

3. GET is also supported:

```bash
npx agentcash@latest fetch 'https://pennyregwatch.com/v1/search?query=YOUR%20SEARCH%20QUERY&limit=5'
```

AgentCash handles the x402 challenge, wallet signature, payment, and retry.

## Input guidance

Required:
- `query`: natural-language web search query

Optional:
- `limit`: number of results requested

Prefer specific queries that express the information need clearly.

## Spending rules

- Penny costs $0.004 per call.
- Prefer one well-formed search before issuing additional calls.
- Do not make duplicate searches unless the first result is insufficient.
- Never fabricate a successful payment or result.
- A failed non-2xx request should not be treated as fulfilled.

## Result handling

Return useful facts from Penny's response and preserve source URLs when present.

Distinguish:
- information returned by Penny
- your own inference
- information from other sources

For time-sensitive claims, prefer the freshest credible source in the returned results.

## Troubleshooting

If the endpoint is not recognized:

```bash
npx agentcash@latest discover https://pennyregwatch.com
```

If AgentCash has not persisted Penny as a provider:

```bash
npx agentcash@latest add https://pennyregwatch.com
```

Do not guess alternate Penny endpoint paths. Use `/v1/search`.
