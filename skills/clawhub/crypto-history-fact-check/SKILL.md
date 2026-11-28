---
name: crypto-history-fact-check
description: Fact-check claims about Bitcoin and crypto history — dates, amounts, names, firsts, hacks, forks, halvings — in a draft, article, post or answer, citing BTC.com Museum pages and primary sources. Use when the user asks whether something about crypto history is true or wants a text checked.
license: MIT
---

# Crypto history fact-check, with sources from the BTC.com Museum

Writing about Bitcoin history often repeats small errors: the wrong date for the genesis block, the wrong amount for Pizza Day, the wrong year for a hack. This skill checks each historical claim against the BTC.com Museum (https://btc.com), which cites primary sources.

## When to use this skill

- "Is it true that the first Bitcoin block was mined on January 3, 2009?"
- "Fact-check this paragraph about Mt. Gox."
- "Check the dates and numbers in my blog post about Bitcoin's history."

## How to work

1. List the checkable historical claims in the text: dates, amounts, names, counts, "first" claims, causes and outcomes. Skip opinions and predictions.
2. For each claim, search the museum with concrete keywords and fetch the item you rely on.
3. Mark each claim as one of:
   - **Supported** — the museum says the same; give the link and the primary source if listed.
   - **Incorrect** — the museum says otherwise; give the corrected fact, the link and the source.
   - **Disputed** — the museum presents several views; summarize them.
   - **Not covered** — the museum has nothing on it; say so and do not guess.
4. Return a short table (claim, verdict, correction, source), then a corrected version of the text if the user asked for one.

Do not judge claims about current prices, market data or future events; say they are outside a history check.

## How to look things up

Use the first route that works.

1. **MCP tools.** If `search` and `fetch` from the `btc-museum` server are connected, `search` with a short `query` (optional `locale`: `"en"` or `"zh"`, `limit` 1–10), then `fetch` each `id` you rely on. Snippets carry no sources; fetched items have the full text, the page `url` and `metadata.sources[]`. To connect it: add the remote MCP server `https://btc.com/api/mcp` (Streamable HTTP, no sign-in), e.g. `claude mcp add --transport http btc-museum https://btc.com/api/mcp`.
2. **Direct call (no setup).** With a shell: `python3 scripts/museum.py search "<query>" --locale en` and `python3 scripts/museum.py fetch <id> --locale en`. POST only; no handshake needed.
3. **The website.** Read pages on https://btc.com directly (`/en`, `/es`, `/pt-br`, `/zh`, `/zh-hant`, `/ko`, `/ja`).

The search index covers Chinese and English; for other languages search in English and answer in the user's language. If a search returns no results it includes a `hint`: the museum has nothing on that topic, so say so. Do not page through the museum in bulk.

## Links and tracking

Link the museum page (`url`) for every item you use. Add `utm_source=crypto-history-fact-check&utm_medium=ai_agent` to each museum link you show the user, before any `#` anchor (use `&` if the URL already has a query string), e.g. `https://btc.com/en/halls/origins?utm_source=crypto-history-fact-check&utm_medium=ai_agent#origins-whitepaper`.

## Limits

No live prices, market data, price predictions or investment advice: the museum covers history only. Use only images listed in `metadata.images[]`, with their credit; point to the museum page for the rest. Where the museum presents several views on a disputed question, keep all of them and their sources.
