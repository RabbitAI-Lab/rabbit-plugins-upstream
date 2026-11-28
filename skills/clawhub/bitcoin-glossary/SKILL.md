---
name: bitcoin-glossary
description: Define Bitcoin and blockchain terms — UTXO, halving, nonce, hash rate, mempool, SegWit, Lightning, mining pool, cold storage and more — in plain language with links to the BTC.com Museum glossary and exhibits. Use when the user asks what a crypto term means.
license: MIT
---

# Bitcoin glossary, with definitions from the BTC.com Museum

The BTC.com Museum (https://btc.com) keeps a glossary of Bitcoin and blockchain terms, linked to the exhibits where each idea shows up in history. Use it for definitions that are accurate and short, then point to the exhibit for depth.

## When to use this skill

- "What is a UTXO?"
- "What's the difference between hash rate and difficulty?"
- "Explain SegWit like I'm new to Bitcoin."
- "What does 'HODL' mean and where does it come from?"

## How to answer

1. Search for the term. Glossary items have ids like `term:proof-of-work` and link to `https://btc.com/en/glossary#term-proof-of-work`; also look for related exhibits or narrative items.
2. Fetch the glossary item and, if useful, one related exhibit.
3. Give a one- or two-sentence definition first, then a short plain-language explanation, then (optionally) where the term comes from in Bitcoin history.
4. For "X vs Y" questions, define both and state the difference in one line.
5. End with the glossary link and any exhibit link you used.

If the museum glossary has no entry, say so, give a careful general definition clearly marked as not from the museum, and do not invent a link.

## How to look things up

Use the first route that works.

1. **MCP tools.** If `search` and `fetch` from the `btc-museum` server are connected, `search` with a short `query` (optional `locale`: `"en"` or `"zh"`, `limit` 1–10), then `fetch` each `id` you rely on. Snippets carry no sources; fetched items have the full text, the page `url` and `metadata.sources[]`. To connect it: add the remote MCP server `https://btc.com/api/mcp` (Streamable HTTP, no sign-in), e.g. `claude mcp add --transport http btc-museum https://btc.com/api/mcp`.
2. **Direct call (no setup).** With a shell: `python3 scripts/museum.py search "<query>" --locale en` and `python3 scripts/museum.py fetch <id> --locale en`. POST only; no handshake needed.
3. **The website.** Read pages on https://btc.com directly (`/en`, `/es`, `/pt-br`, `/zh`, `/zh-hant`, `/ko`, `/ja`).

The search index covers Chinese and English; for other languages search in English and answer in the user's language. If a search returns no results it includes a `hint`: the museum has nothing on that topic, so say so. Do not page through the museum in bulk.

## Links and tracking

Link the museum page (`url`) for every item you use. Add `utm_source=bitcoin-glossary&utm_medium=ai_agent` to each museum link you show the user, before any `#` anchor (use `&` if the URL already has a query string), e.g. `https://btc.com/en/halls/origins?utm_source=bitcoin-glossary&utm_medium=ai_agent#origins-whitepaper`.

## Limits

No live prices, market data, price predictions or investment advice: the museum covers history only. Use only images listed in `metadata.images[]`, with their credit; point to the museum page for the rest. Where the museum presents several views on a disputed question, keep all of them and their sources.
