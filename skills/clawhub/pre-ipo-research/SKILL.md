---
name: pre-ipo-research
description: Query the public Pre-IPO Observer for Jarsy Private Equity Live and Presale assets, including valuations, trade availability, and freshness timestamps. Use when users ask to find, screen, compare, or summarize Pre-IPO assets or Jarsy-backed market snapshots.
---

# Pre-IPO Research

Use the public Pre-IPO Observer API for read-only research on Jarsy Private
Equity Live and Presale assets. Report the data source and freshness with every
material answer. This skill does not place trades, refresh Jarsy data, or use a
Jarsy login.

## Quick start

Run the bundled client with Node.js 18 or newer:

```bash
node scripts/query-preipo.mjs summary
node scripts/query-preipo.mjs search Anthropic --market live
node scripts/query-preipo.mjs list --stage Presale --sort valuation_desc --page-size 24
```

The default API is `https://preipo.polyos.ai`. If the deployment uses a
different endpoint, set `PREIPO_API_BASE_URL` or pass `--base`:

```bash
PREIPO_API_BASE_URL=https://example.com node scripts/query-preipo.mjs summary
node scripts/query-preipo.mjs search SpaceX --base https://example.com --json
```

## Workflow

1. Run `summary` first when the request needs market context, rankings, or a
   data freshness statement.
2. Run `search <keywords>` for a company, token, underlying name, or ticker.
   Use `list` when no keywords are needed.
3. Apply only supported filters: `--market live|presale`, `--stage`,
   `--trade buy_sell|buy_only|sell_only|inactive`, `--sort
   valuation_desc|price_desc|updated_desc|name_asc`, `--page`, and
   `--page-size` (6–48).
4. Paginate before claiming a filtered result set is complete. The response
   includes `total`, `page`, and `pageSize`.
5. For an answer to a user, state both applicable timestamps separately:
   - **数据更新时间 / snapshot import time**: `lastImport.importedAt`; it
     identifies the latest successful site-wide snapshot.
   - **标的记录更新时间 / asset record time**: `sourceUpdatedAt`; it identifies
     the source timestamp for that particular asset and may be absent.
6. Label the source as Jarsy. Treat price, valuation, volume, and trade status
   as point-in-time data, not investment advice. Do not imply execution,
   availability in a user's jurisdiction, or a current valuation when the
   snapshot is stale.

## Output guidance

For a company lookup, give the matching token, market (Live or Presale), stage,
buy/sell status, price, valuation, volume when available, and the individual
record timestamp. For aggregate questions, include the snapshot import time.
Use `--json` only when raw API data is requested or another program will
consume it.

If the API returns an error, report that current public data is unavailable and
do not substitute remembered values. Do not call `/api/admin/refresh`, ask for
refresh credentials, scrape Jarsy, or bypass authentication.

## Reference

Read `references/api.md` before extending the query client, constructing direct
API calls, or interpreting a field not covered above.
