---
name: quorumz-news
description: Current geo-tagged world news for agents, split into viewpoints with a count of the media, social and on-the-ground posts behind each. Use when a user asks what people are saying about a country, conflict or public story, wants the distinct positions on a story, or wants an early signal ahead of the wider press. Pay per call with an API key (free 7-day trial) or with x402 in USDC on Base, Polygon or Arbitrum.
version: 1.0.2
metadata:
  openclaw:
    homepage: https://sense.quorumz.com/agents
    primaryEnv: QUORUMZ_API_KEY
    envVars:
      - name: QUORUMZ_API_KEY
        required: false
        description: API key from https://sense.quorumz.com/agents/keys (free 7-day trial). Without it, pay per call with x402.
---

# Quorumz agent news

Use this when an agent needs current geo-tagged news that is split into viewpoints, with a count of the posts supporting each viewpoint.

## When to use it

- A user asks what people are saying about a country, a conflict, or a public story.
- A user wants the distinct positions on a story, not one headline.
- A user wants an early signal that is ahead of the wider press.

Do not use it for a generic web search, a weather lookup, or a map of flights and ships.

## How to call it

Base URL: https://api.quorumz.com

1. Check the data for free: GET https://api.quorumz.com/api/agent/v1/sample returns one recent quorum. No key, no payment.
2. Use an API key if you have one: when `QUORUMZ_API_KEY` is set in your environment, send it as
   `Authorization: Bearer <key>` on every call. With no key, ask your human to get a free one at
   https://sense.quorumz.com/agents/keys (sign in with an email and a 6-digit code, about a minute).
   The first 100 calls that return events, within 7 days, are free; then each call is paid from
   credits your human buys by card. A key with nothing left answers 402 and says how to add credits.
3. No key, but USDC on Base (eip155:8453), Polygon (eip155:137) or Arbitrum (eip155:42161): call the
   route with no payment header. It answers HTTP 402. Read the PAYMENT-REQUIRED header (base64 JSON),
   sign the exact amount to the payTo address on one of its accepts, and retry the same URL with
   PAYMENT-SIGNATURE. PAYMENT-RESPONSE is the settlement receipt. No account is needed.

Every 402 body also says, in plain words, how to go on (`message`, `get_started`). The catalog of
routes and prices is free: GET https://api.quorumz.com/api/agent/v1. Empty pages are free. A missing id
is a 404 and is not charged.

## Routes

- GET /api/agent/v1/quorums?country=LB — $0.01 per quorum returned
- GET /api/agent/v1/quorums/{quorum_id} — $0.01
- GET /api/agent/v1/events?stream=alpha&country=LB — $0.02 per event
- GET /api/agent/v1/events?stream=news&country=LB — $0.005 per event
- GET /api/agent/v1/articles/{article_id} — $0.005

country is an ISO alpha-2 code. cell is a geohash of precision 3, 4, or 5 and applies to alpha. Pass next_cursor back to page older results.

## What you get

A quorum has viewpoints. Each viewpoint has a label, a summary, support_count, and support_by_source split into media, socials, and iWitness. News and articles include the quorums related to that story.

## Clients

- TypeScript, as Vercel AI SDK tools: `npm install @quorumz/ai-sdk ai zod`
- Python, sync and async: `pip install quorumz`

Both read the key from `QUORUMZ_API_KEY`.

## As an MCP server

`https://api.quorumz.com/mcp` (streamable HTTP) has the same feeds as tools: `search_quorums`,
`list_alpha_events`, `list_news`, `get_quorum`, `get_article`, and `sample_quorum` (free). It takes the
same API key as `Authorization: Bearer <key>`. Pay-per-call x402 is on the HTTP routes above.

## Also read

- Docs: https://sense.quorumz.com/agents/docs
- Discovery: https://api.quorumz.com/.well-known/x402
- OpenAPI: https://api.quorumz.com/openapi.json
- Machine summary: https://sense.quorumz.com/llms.txt
- Support: support@quorumz.com
