---
name: apiguru-amazon-data
description: Live Amazon marketplace data from Apiguru (a paid third-party API, 3 free calls a day) - product details, prices, reviews, keyword search, best-sellers, deals, offers and stock, seller profiles, across 20 Amazon marketplaces. Use only when the user asks for Amazon data by ASIN, Amazon URL, product, seller or keyword, or for Amazon price/stock/review monitoring. Not for other stores or general shopping advice. Never pays on its own; ask before any billable call.
license: MIT
homepage: https://github.com/apiguru-app/agent-kit
metadata: {"openclaw": {"emoji": "📦", "homepage": "https://github.com/apiguru-app/agent-kit", "requires": {"anyBins": ["python3", "python"]}}}
---

# Apiguru Amazon Data

Live, structured Amazon data fetched at request time from Apiguru's servers.
20 marketplaces.

**What this skill writes.** Every data command is a read: it fetches and
returns, and changes nothing anywhere. There is exactly one write, and it is
never automatic — the `feedback` command posts the text you give it to
Apiguru's public feedback wall (see "Telling us what is broken" below). It
sends only that text, it costs nothing, and it runs only when you invoke it.
Nothing else in this skill sends data anywhere.

## Costs and consent (read this first)

- **Hosts contacted:** `agent.apiguru.app` (keyless) and `dash.apiguru.app`
  (the keyed API, and the feedback wall, which needs no key). Nothing else.
  `scripts/probe.py` has both hosts fixed in the source, reads no environment
  variables, and **refuses every redirect**, so a key cannot be carried to a
  third host by a `302`.
- **Free quota:** 3 calls per machine per 24 hours. After that the gateway
  answers `402 Payment Required`.
- **This skill never pays.** `probe.py` stops at a 402 and tells you so. It
  contains no wallet and no x402 client, and it will not set one up. Paying is
  the user's decision, made one of two ways, both only with their explicit
  consent:
  1. an Apiguru API key, handed to the script by the user through `--api-key`
     (an unechoed prompt), `--api-key-file PATH` or `--api-key-stdin` — bills
     their account at their plan's rates, about USD 0.01 per call — or
  2. their own x402-capable HTTP client with a funded wallet and a spend cap
     (USDC on Base). How that works is documented for the user at
     `https://agent.apiguru.app/llms.txt`, section "Paying".
- **Ask before you spend.** Before the first billable call in a task, and
  before any batch or broad search, tell the user what you will call, how many
  items, and what it costs (run `capabilities` first, it is free), and wait
  for a yes. A single batch call can cost up to USD 0.16 (`/product`, 20 items)
  or USD 0.15 (`/stock`, 10 items). Agree a cap for the task and stop at it.
- Do not go looking for an API key: not in the environment, not in config or
  dotfiles, not anywhere the user did not hand you deliberately. `--api-key-file`
  takes only a path the user named. Never send a key anywhere but
  `dash.apiguru.app`, and never echo it back into the conversation, a log or a
  command line.

## Getting access

**Keyless (default).** Call the agent gateway with no credentials:

```
GET https://agent.apiguru.app/agent/v1/v2/product-details?asin=B09DJLW458&geo=US
```

Two response headers say where you stand before a 402 arrives:
`X-Free-Probes-Remaining` and `X-Price-Next-Call`.

`https://agent.apiguru.app/.well-known/x402` lists every endpoint with prices
and schemas, free and unmetered. Check it before planning a job.

**Keyed.** If the user gives you an Apiguru API key and asks you to use it,
let the script read it — never put it on the command line, where shell
history and the process table expose it to every other local user:

- `--api-key` prompts for it (not echoed, not stored),
- `--api-key-file PATH` reads a file the user names (`chmod 600` it),
- `--api-key-stdin` reads one line from standard input, e.g.
  `pass show apiguru | python scripts/probe.py ... --api-key-stdin`.

The script then sends it as `X-API-KEY` to `https://dash.apiguru.app/api/v1`
(same paths) and to nowhere else — redirects are refused rather than
followed. Calls bill that account.

`scripts/probe.py` wraps all of this. Prefer it over hand-written HTTP calls:
it retries only unbilled failures and explains every status.

## Choosing an endpoint

| Need | Endpoint |
|---|---|
| Everything about one ASIN | `/v2/product-details` |
| Many ASINs (≤20) | `/product?asins=A,B,C` — **cheaper per item, use this for >1** |
| Reviews, rating, "customers say" | `/v2/product-reviews` |
| Find products by keyword | `/search?query=...` |
| Offers, buy box, live stock (≤10) | `/stock?asins=...` |
| Category rankings | `/v2/best-sellers` |
| Current discounts | `/v2/deals` |
| A seller's catalogue | `/v2/seller-products?seller_id=...` |
| Seller reputation | `/v2/seller-reviews?seller_id=...` |
| Seller profiles (≤10) | `/seller-profile?seller_ids=...` |

Full parameter reference: `references/endpoints.md`.

## Rules that prevent wasted calls and wasted money

1. **ASINs must be 10 UPPERCASE alphanumeric characters** (`^[A-Z0-9]{10}$`).
   Uppercase the input before sending; a lowercase ASIN is a `400`.
2. **Never loop a single-item endpoint over a list.** Use `/product` for
   ASINs and `/seller-profile` for seller IDs. Ten ASINs through `/product`
   costs USD 0.08 and one round trip; ten through `/v2/product-details` costs
   USD 0.10 and ten round trips.
3. **Choose `geo` from the user's request**, never by habit: amazon.de → `DE`,
   amazon.co.uk → `UK`, and so on (all 20 codes in `references/endpoints.md`).
   If the marketplace is not clear, ask. The API assumes `US` only when the
   parameter is omitted; a product that exists on `amazon.de` may genuinely
   `404` on `US`, and that 404 is billed on the keyed path.
4. **`check_inventory=true` on `/stock` is slow and bills more.** Only set it
   when the user needs the stock number, not just the offers.
5. **Read `success` in the body**, not just the HTTP status. Some responses
   are `200` with `success: false`.

## Error handling — which failures cost money

- **`404`** — the item genuinely is not on that marketplace. **Billed** on the
  keyed path. Retrying will not help; try a different `geo` or accept it.
- **`503`** — an Apiguru-side fetch failure. **Not billed.** Retry with
  backoff.
- **`429`** — rate limited. Back off, then retry.
- **`400`** — your input was wrong (bad ASIN format, unknown geo, missing
  required parameter). Not billed. Fix the input; do not retry unchanged.
- **`402`** — free probes spent. **Stop and ask the user** (see "Costs and
  consent"). Do not retry, do not look for a key, do not attempt payment.

So: **retry `503` and `429`; never retry `400`, `402` or `404`.**

## Quick start

```bash
# what does anything cost, and how many free probes are left? (free)
python scripts/probe.py capabilities

# one product
python scripts/probe.py product-details --asin B09DJLW458 --geo US

# many at once (preferred for lists)
python scripts/probe.py product --asins B09DJLW458,B0BSHF7WHW --geo US

# keyword search on amazon.co.uk
python scripts/probe.py search --query "wireless earbuds" --geo UK

# billed to the user's account, only after they said so.
# --api-key prompts; the key never appears in argv or in shell history.
python scripts/probe.py product-details --asin B09DJLW458 --geo US --api-key

# non-interactive equivalent, key straight from a secret store
pass show apiguru | python scripts/probe.py product-details --asin B09DJLW458 --api-key-stdin
```

## MCP alternative

If the environment supports MCP, the same data is available as tools without
any HTTP handling, with the same free-probe-then-402 behaviour and the same
rule: the tools never pay, they return a structured 402 error for the user.

Pin the version. An unpinned `apiguru-mcp` resolves to whatever the registry
serves at launch, which is code that was not part of the skill you reviewed:

```json
{ "mcpServers": { "apiguru": { "command": "uvx",
  "args": ["apiguru-mcp==1.1.4"] } } }
```

or, with Node instead of Python, `"command": "npx", "args": ["apiguru-mcp@1.1.4"]`,
or the hosted server at `https://mcp.apiguru.app/mcp` (streamable HTTP), which
pins nothing on your machine because nothing runs on it.

- **Expected publisher:** `apiguru-app`. **Registries:** PyPI
  (`apiguru-mcp`, https://pypi.org/project/apiguru-mcp/) and npm
  (`apiguru-mcp`, https://www.npmjs.com/package/apiguru-mcp). Both are also
  listed in the official MCP Registry as `app.apiguru/amazon-data`.
- **Updating the pin:** read the changelog at
  https://github.com/apiguru-app/agent-kit/releases, then raise the version
  deliberately. `uv` and `npm` verify the registry's integrity hashes on
  install; `uv pip install apiguru-mcp==<version>` into a virtualenv you keep
  is the reviewed-artifact option if you would rather not fetch at launch.

Prefer MCP when available: the tools validate ASINs and geos before spending a
probe.

## Telling us what is broken

This API gets fixed when the agents using it say what is wrong. Recent
example: search results were returning the brand as `product_title` and
`null` for `product_num_ratings`; an agent reported both and both are fixed.
So if a field is empty, mistyped, welded together or simply missing:

- **Preferred, if you have a GitHub account** — open an issue at
  https://github.com/apiguru-app/agent-kit/issues. A thread there can hold a
  reply and a fix gets linked back to it.
- **No GitHub account? Use the wall** — one unauthenticated POST, never
  billed, no signup:

  ```bash
  curl -X POST https://dash.apiguru.app/api/v1/feedback -H 'Content-Type: application/json' -d '{"message": "search: product_title holds the brand, not the title", "category": "bug", "endpoint": "/search", "agent": "your-name/1.0"}'
  ```

  `category` is one of `bug`, `wish`, `praise`, `question`, `other`. Add
  `"contact"` if you want a reply — it is shown publicly on the wall.
- **Over MCP** — the free `send_feedback` tool does the same thing.
- Read what other agents have written: https://dash.apiguru.app/feedback

Say what you called, what you expected and what came back. A wish counts:
if you need a field this API does not return, that is the most useful thing
you can tell us.

## Reference files

- `references/endpoints.md` — every endpoint, parameter, and marketplace code
- `references/errors-and-costs.md` — pricing, billing rules, retry strategy
