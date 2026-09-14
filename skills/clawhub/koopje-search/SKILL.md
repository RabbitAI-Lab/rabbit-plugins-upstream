---
name: koopje-search
description: Search koopje.ai for Belgian second-hand deals and auctions.
version: 1.0.8
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

Search ~155k Belgian second-hand listings and live auctions via the
koopje.ai REST API. The index aggregates 2dehands.be, auction houses,
Troc.com, Marktplaats, Zoekertjes.be and Belgian car dealers, plus user ads:

| source | what it is |
|---|---|
| `2dehands` | private sellers on 2dehands.be (Belgium's largest marketplace) |
| `trader` | professional occasion sellers on 2dehands.be |
| `troc` | Troc.com second-hand store inventory (Belgian stores) |
| `marktplaats` | Belgian listings on Marktplaats.nl |
| `zoekertjes` | free classifieds on Zoekertjes.be |
| `user` | user-submitted own ads (live at `https://koopje.ai/<category>/<slug>-<id>`, 30-day expiry) |
| car-dealer domains | Belgian cars carry their dealer/platform as source: `autoscout24.be`, `gocar.be`, `mazdastock.be`, `vroom.be`, `autohero.com`, `irisautocenter.be`, `autocadre.com` (resolved from listings, never the aggregator) |
| auction-house slugs | auction lots carry their house as source: `alleveilingen`, `vavato`, `troostwijk`, `auctelia`, `belga-veilingen`, `vlavem`, `auctionport`, `openbare-verkopen`, `bopa`, `hammertime`, `veilbalie`, `komerco`, `lussis`, `bell-auction`, `industrial-auctions`, `appelboom` (house name also in `seller_name`) |

Every result also carries `listing_type`: `veiling` (any auction house) or
`tweedehands` (everything else) — the binary filter, independent of source.

## When to use

Triggers: finding, comparing or pricing used items ("tweedehands",
"koopjes", "second-hand"), auction lots ("veiling"), or Belgian
marketplace listings — e.g. "find a used bike in Gent", "wat kost een
tweedehands espresso-machine?", "similar to <listing url>".

## Prerequisites

- `KOOPJE_API_KEY` env var, a `kk_...` key from koopje.ai (account →
  "API keys"; shown once at creation).

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
| `source` | exact origin: `2dehands`, `troc`, `marktplaats`, `zoekertjes`, a car-dealer domain (`autoscout24.be`, `gocar.be`, …), or an auction-house slug (`vavato`, `troostwijk`, …). Legacy aliases still work: `2dehands` → all tweedehands, `veiling` → all auctions. Default: all sources |
| `listing_type` | `tweedehands` (all second-hand) or `veiling` (all auction lots) — binary filter, independent of source |
| `type` | `auto` (default), `neural` (semantic), `keyword` |
| `price_min` / `price_max` | euros |
| `no_price` | `0` hides listings without a price |
| `limit` | 1–24, default 12 |

### Other endpoints

- `GET /v1/similar?url=<listing-url>&limit=12` — visually/semantically
  similar listings; url must be a listing already in the index.
- `GET /v1/answer?q=<question>&source=...` — Dutch natural-language answer
  with citations to real listings (RAG over the index).
- `POST /v1/agent` — the website agent as an API: JSON body
  `{"message": "...", "conversation": [...], "source": "..."}`,
  streams the answer as Server-Sent Events (multi-step: it runs its own
  searches). Limits: 10/min + 100/day per key.
- `GET /v1/contents?urls=<url1,url2,...>` — full details per listing URL
  (max 20 urls). Use after search when the user wants depth.
- `GET /v1/stats` — per-source listing counts; good connectivity check.
- Saved listings (need the user's key; login-gated like everything else):
  `GET /v1/saved` (newest first), `POST /v1/saved` with
  `{"url": ..., "title": ..., "price_value": ..., "price_text": ...,
  "thumbnail_url": ..., "source": ..., "location": ...}` (idempotent),
  `POST /v1/saved/remove` with `{"url": ...}`.
- Own listings (need the user's key): `POST /v1/listings` with
  `{title, location, own: true}` plus `description, price_value,
  category, source_url, images[]` (base64, max 5) → `{id, url}`;
  `POST /v1/listings/fetch-url` to prefill from an ad link;
  `POST /v1/listings/draft` with `{url, own: true}` for an unindexed
  draft → `POST /v1/listings/publish` with `{id, ...overrides}`;
  `GET /v1/listings/mine`, `POST /v1/listings/remove|renew`.
  Full fields in `references/api.md`.

## Reading results

`results[]` items carry: `url`, `title`, `description` (short snippet),
`price_value` + `price_text` (null when bidding/no price), `location`
(city), `source` (actual origin: `2dehands`, `trader`, `troc`,
`marktplaats`, `zoekertjes`, `user` (own ads at `koopje.ai/<category>/…`), a car-dealer domain (`autoscout24.be`,
`gocar.be`, …), or an auction-house slug — `alleveilingen`,
`vavato`, `troostwijk`, `auctelia`, `belga-veilingen`, `vlavem`, `auctionport`,
`openbare-verkopen`, `bopa`, `hammertime`, `veilbalie`, `komerco`,
`lussis`, `bell-auction`, `industrial-auctions`, `appelboom`), `listing_type`
(`tweedehands` or `veiling`), `thumbnail_url`, `_score` (similarity).

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
- 401 → key missing/revoked; 429 → rate limited (search/similar/contents/stats:
  60/min + 2,000/day per key; answer: 20/min + 200/day; agent: 10/min +
  100/day), back off and retry once. Other failures (400/403/404/500) come
  as `{"error": "..."}` — report the message, don't guess.
- Agent docs: `GET https://koopje.ai/llms.txt` lists every agent-readable
  page; `Accept: text/markdown` on `/`, `/docs`, `/api`, `/koppelen`
  returns Markdown instead of HTML. n8n users: ready-made agent template
  at https://koopje.ai/koppelen (n8n tab).
- Empty `results` ≠ error: rephrase the query broader (Dutch nouns help)
  before giving up.
- Never invent listings; only report what the API returned.

## Verification

`GET /v1/stats` returns `{"total": ..., "2dehands": ..., "veiling": ...}`
— if that fails, the key or connectivity is broken; tell the user instead
of guessing.
