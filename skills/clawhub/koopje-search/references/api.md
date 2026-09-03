# koopje.ai /v1 API reference

Base: `https://koopje.ai` — all requests need `Authorization: Bearer kk_...`.
All responses JSON; `/v1/*` sends `Access-Control-Allow-Origin: *`.

Errors: 401 missing/invalid key · 401 revoked key · 400 invalid params ·
429 rate limited.

## GET /v1/search

Semantic + keyword search over the unified index.

| param | type | required | description |
|---|---|---|---|
| `q` | string | yes | natural language or keywords (Dutch works best) |
| `type` | string | no | `auto` (default) · `neural` · `keyword` |
| `source` | string | no | `2dehands` (all second-hand: 2dehands + professional traders + Troc.com stores + Marktplaats BE) · `veiling` (auctions from alleveilingen.be auction houses: Vavato, Troostwijk, Belga-Veilingen, Openbare-verkopen, AuctionPort, Bopa, Vlavem, Auctelia, VeilBalie, Appelboom, Hammertime, Komerco, Lussis, Bell-Auction, Industrial-Auctions) |
| `price_min` | number | no | minimum price in euro |
| `price_max` | number | no | maximum price in euro |
| `no_price` | bool | no | `0` hides listings without a price (default `1` shows them) |
| `limit` | number | no | 1–24, default 12 |
| `offset` | number | no | skip N results ("toon meer" pagination) |
| `postcode` | string | no | 4-digit Belgian postcode ("2000") — results filtered to `max_km` around it and annotated with `_distance_km` |
| `lat` / `lng` | number | no | raw user coordinates (alternative to `postcode`) |
| `max_km` | number | no | radius in km around the user location (omit = no limit). Listings without any locatable city/coords are excluded when a location filter is active |

Response:

```json
{
  "requestId": "…",
  "resolvedSearchType": "auto",
  "results": [
    {
      "url": "https://www.2dehands.be/v/…",
      "title": "…",
      "description": "short snippet",
      "price_value": 60.0,
      "price_text": "60 EUR",
      "location": "Borgerhout",
      "source": "2dehands",
      "thumbnail_url": "…",
      "_score": 0.83
    }
  ]
}
```

`source` values in results: `2dehands` (private sellers on 2dehands.be),
`trader` (professional occasion sellers on 2dehands.be), `troc` (Troc.com
store inventory), `marktplaats` (Belgian listings on Marktplaats.nl),
`veiling` (auction lots — the lot's auction house is in `seller_name`:
Vavato, Troostwijk, Belga-Veilingen, Openbare-verkopen, AuctionPort,
Bopa, Vlavem, Auctelia, VeilBalie, Appelboom, Hammertime, Komerco,
Lussis, Bell-Auction, Industrial-Auctions). Auction lots have no fixed
price.

Each result also carries `_price_kind` (`fixed`, `bid`, `auction`,
`free`, `none`), and — when a location filter was given — `_distance_km`
(+ `_distance_approx` when derived from a city centroid). The envelope
echoes `userLocation` (`label`, `lat`, `lng`, `maxKm`, `approx`) and
`distance` (`maxKm`, `hidden`: rows dropped for lack of location).

## GET /v1/similar

| param | type | required | description |
|---|---|---|---|
| `url` | string | yes | URL of a listing in the index (2dehands, troc, marktplaats, veiling urls work) |
| `limit` | number | no | 1–24, default 12 |

Same response shape as search.

## GET /v1/answer

RAG answer (Dutch) over the index with citations.

| param | type | required | description |
|---|---|---|---|
| `q` | string | yes | the question in natural language |
| `source` | string | no | source filter, same values as search |

Response includes the answer text plus `citations` linking to the
underlying listings.

## GET /v1/contents

| param | type | required | description |
|---|---|---|---|
| `urls` | string | yes | comma-separated listing URLs, max 20 |

Full listing details (description, attributes, seller, images) for the
given URLs — use to deepen search results before reporting.

## GET /v1/stats

No parameters. Returns `{"total": N, "2dehands": N, "veiling": N,
"trader": N, "troc": N, "marktplaats": N}` — per-source listing counts.

## Getting a key

Log in at koopje.ai → menu (top right) → *API-sleutels* → create. Keys
are `kk_` + 32 chars and shown exactly once. Store as `KOOPJE_API_KEY`.
