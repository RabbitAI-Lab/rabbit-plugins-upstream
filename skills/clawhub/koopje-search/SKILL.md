---
name: koopje-search
description: Search koopje.ai for Belgian second-hand deals and auctions.
version: 1.0.3
author: Lukas, koopje.ai
license: MIT
metadata:
  openclaw:
    requires:
      env:
        - KOOPJE_API_KEY
  hermes:
    tags: [koopje, search, second-hand, belgium, api]
---

# koopje.ai search API

Search ~60k Belgian second-hand listings and live auctions via the
koopje.ai REST API. The index aggregates five sources:

| source | what it is |
|---|---|
| `2dehands` | private sellers on 2dehands.be (Belgium's largest marketplace) |
| `trader` | professional occasion sellers on 2dehands.be |
| `troc` | Troc.com second-hand store inventory (Belgian stores) |
| `marktplaats` | Belgian listings on Marktplaats.nl |
| `veiling` | auction lots — the lots come from these auction houses (see them in each result's `seller_name`): Vavato, Troostwijk, Belga-Veilingen, Openbare-verkopen, AuctionPort, Bopa, Vlavem, Auctelia, VeilBalie, Appelboom, Hammertime, Komerco, Lussis, Bell-Auction, Industrial-Auctions |

## When to use

Triggers: finding, comparing or pricing used items ("tweedehands",
"koopjes", "second-hand"), auction lots ("veiling"), or Belgian
marketplace listings — e.g. "find a used bike in Gent", "wat kost een
tweedehands espresso-machine?", "similar to <listing url>".

## Prerequisites

- `KOOPJE_API_KEY` env var, a `kk_...` key from koopje.ai (account →
  "API-sleutels"; shown once at creation).

## How to call

All endpoints: `https://koopje.ai`, auth header on every request:
`Authorization: Bearer $KOOPJE_API_KEY`. JSON responses, CORS enabled.

### POST-free quickstart — GET /v1/search

```
curl -s "https://koopje.ai/v1/search?q=vintage+stoel&price_max=200&limit=5" \
  -H "Authorization: Bearer $KOOPJE_API_KEY"
```

Key parameters (full list in `references/api.md`):

| param | notes |
|---|---|
| `q` | required, natural language or keywords (Dutch works best) |
| `source` | `2dehands` (all second-hand: 2dehands + trader + Troc + Marktplaats BE) or `veiling` (auctions). Default: all sources |
| `type` | `auto` (default), `neural` (semantic), `keyword` |
| `price_min` / `price_max` | euros |
| `no_price` | `0` hides listings without a price |
| `limit` | 1–24, default 12 |

### Other endpoints

- `GET /v1/similar?url=<listing-url>&limit=12` — visually/semantically
  similar listings; url must be a listing already in the index.
- `GET /v1/answer?q=<question>&source=...` — Dutch natural-language answer
  with citations to real listings (RAG over the index).
- `GET /v1/contents?urls=<url1,url2,...>` — full details per listing URL
  (max 20 urls). Use after search when the user wants depth.
- `GET /v1/stats` — per-source listing counts; good connectivity check.

## Reading results

`results[]` items carry: `url`, `title`, `description` (short snippet),
`price_value` + `price_text` (null when bidding/no price), `location`
(city), `source` (actual origin: `2dehands`, `trader`, `troc`,
`marktplaats`, or `veiling` — for auctions the lot's auction house is in
`seller_name`: Vavato, Troostwijk, Belga-Veilingen, Openbare-verkopen,
AuctionPort, Bopa, Vlavem, Auctelia, VeilBalie, Appelboom, Hammertime,
Komerco, Lussis, Bell-Auction, Industrial-Auctions), `thumbnail_url`,
`_score` (similarity).

Report to the user in Dutch where possible; always include price,
location and the actual source: name the site or auction house
explicitly (2dehands, Troc.com, Marktplaats.nl, or for auctions the
auction house from `seller_name` — e.g. Vavato, Troostwijk,
Belga-Veilingen); link the `url`. Auction items
(`source: "veiling"`) have no fixed price — say so instead of quoting
`price_text` as a sale price.

## Pitfalls

- `limit` caps at 24 — paginate by refining the query, not by offsetting.
- `source` is binary (`2dehands` vs `veiling`); the fine-grained site is
  only visible per-result in the `source` field of the response.
- 401 → key missing/revoked; 429 → rate limited, back off and retry once.
- Empty `results` ≠ error: rephrase the query broader (Dutch nouns help)
  before giving up.
- Never invent listings; only report what the API returned.

## Verification

`GET /v1/stats` returns `{"total": ..., "2dehands": ..., "veiling": ...}`
— if that fails, the key or connectivity is broken; tell the user instead
of guessing.
