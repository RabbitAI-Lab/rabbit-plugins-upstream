# Pre-IPO Observer public API

Base URL defaults to `https://preipo.polyos.ai`. It can be overridden with the
`PREIPO_API_BASE_URL` environment variable for a compatible deployment.

All endpoints below are public, read-only JSON endpoints. Responses are cached
for up to 60 seconds. Never use the protected refresh endpoint for research.

## `GET /api/summary`

Returns dashboard aggregates and freshness metadata:

```json
{
  "stats": {
    "total": 62,
    "liveCount": 28,
    "presaleCount": 34,
    "buyEnabledCount": 59,
    "sellEnabledCount": 62
  },
  "stages": [{ "stage": "Live", "count": 28 }],
  "valuations": [{ "token": "EXAMPLE", "companyName": "Example", "valuationMillions": 1234 }],
  "lastImport": {
    "importedAt": "2026-08-17T16:06:02.202Z",
    "sourceAssetCount": 62,
    "liveCount": 28,
    "presaleCount": 34
  },
  "latestSourceRecordAt": "2026-08-17T16:00:00.000Z"
}
```

`lastImport.importedAt` is the most recent successful site-wide import. It is
not the update time of every individual asset. `latestSourceRecordAt` is only
the maximum individual-source timestamp, and also does not replace per-asset
timestamps.

## `GET /api/assets`

Returns a paginated asset list.

| Parameter | Accepted values | Default |
| --- | --- | --- |
| `q` | company, token, underlying name, or underlying ticker keyword | none |
| `market` | `live`, `presale` | all |
| `stage` | `Live`, `Locking Period`, `Presale`, `Early Access` | all |
| `trade` | `buy_sell`, `buy_only`, `sell_only`, `inactive` | all |
| `sort` | `valuation_desc`, `price_desc`, `updated_desc`, `name_asc` | `valuation_desc` |
| `page` | integer 1–10000 | `1` |
| `pageSize` | integer 6–48 | `12` |

Example:

```text
/api/assets?q=anthropic&market=live&sort=valuation_desc&page=1&pageSize=12
```

The response has `items`, `total`, `page`, and `pageSize`. Each item can
contain these fields:

| Field | Meaning |
| --- | --- |
| `token` | Jarsy asset token / code |
| `market` | App grouping: `live` or `presale` |
| `stage` | Jarsy lifecycle label |
| `companyName` | Display company name |
| `underlyingName`, `underlyingTicker` | Underlying company identity when supplied |
| `buyActive`, `sellActive` | Snapshot boolean flags for platform availability |
| `priceUsd`, `priceDate` | Price and its source date, if supplied |
| `valuationMillions` | Valuation in USD millions, if supplied |
| `volumeUsd`, `supply` | Snapshot market metrics, if supplied |
| `sourceUpdatedAt` | Per-asset Jarsy record update time, if supplied |
| `sourceUrl`, `proofUrl`, `scanUrl` | Source and related Jarsy links, if supplied |

Values can be `null`; present them as unavailable rather than zero. Price,
valuation, volume, and status are Jarsy point-in-time snapshots and are not
investment advice.
