# Polymarket access policy

An access policy limits which endpoints Polymarket connections may call through Maton. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/polymarket#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Polymarket: its 43 read-only endpoints. Endpoints that return credentials, start jobs, or spend credits are left out. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create polymarket --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "v1/account/balances"},
    {"method": "GET", "path": "v1/asset-prices/history"},
    {"method": "GET", "path": "v1/combos"},
    {"method": "GET", "path": "v1/events"},
    {"method": "GET", "path": "v1/events/slug/{id}"},
    {"method": "GET", "path": "v1/events/{id}"},
    {"method": "GET", "path": "v1/incentives/earnings"},
    {"method": "GET", "path": "v1/market/id/{id}"},
    {"method": "GET", "path": "v1/market/slug/{id}"},
    {"method": "GET", "path": "v1/markets"},
    {"method": "GET", "path": "v1/markets/{id}/bbo"},
    {"method": "GET", "path": "v1/markets/{id}/book"},
    {"method": "GET", "path": "v1/markets/{id}/settlement"},
    {"method": "GET", "path": "v1/order/{id}"},
    {"method": "GET", "path": "v1/orders/open"},
    {"method": "GET", "path": "v1/partners/{id}/events/{id}"},
    {"method": "GET", "path": "v1/portfolio/activities"},
    {"method": "GET", "path": "v1/portfolio/positions"},
    {"method": "GET", "path": "v1/price-history"},
    {"method": "GET", "path": "v1/rfqs"},
    {"method": "GET", "path": "v1/rfqs/quotes"},
    {"method": "GET", "path": "v1/rfqs/trades"},
    {"method": "GET", "path": "v1/rfqs/user-id"},
    {"method": "GET", "path": "v1/search"},
    {"method": "GET", "path": "v1/series"},
    {"method": "GET", "path": "v1/series/id/{id}"},
    {"method": "GET", "path": "v1/sports"},
    {"method": "GET", "path": "v1/sports/players"},
    {"method": "GET", "path": "v1/sports/teams"},
    {"method": "GET", "path": "v1/sports/teams/provider"},
    {"method": "GET", "path": "v1/sports/{id}/events"},
    {"method": "GET", "path": "v2/leagues"},
    {"method": "GET", "path": "v2/leagues/{id}"},
    {"method": "GET", "path": "v2/leagues/{id}/events"},
    {"method": "GET", "path": "v2/order/{id}"},
    {"method": "GET", "path": "v2/orders/open"},
    {"method": "GET", "path": "v2/sports"},
    {"method": "GET", "path": "v2/sports/{id}"},
    {"method": "GET", "path": "v2/sports/{id}/events"},
    {"method": "GET", "path": "v2/tags"},
    {"method": "GET", "path": "v2/tags/slug/{id}"},
    {"method": "GET", "path": "v2/tags/{id}"},
    {"method": "GET", "path": "v2/tags/{id}/events"}
  ],
  "deny": []
}
```

## Endpoints

The Polymarket endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| GET | v1/account/balances | read | portfolio | Get Account Balances. |
| GET | v1/asset-prices/history | read | asset prices | Get a bucketed OHLC price series for one or more assets. |
| GET | v1/combos | read | combos | Get a combo by its exact symbol. |
| POST | v1/combos | write | combos | Create or return the combo instrument for a set of legs. |
| GET | v1/events | read | events | Get Events. |
| GET | v1/events/slug/{id} | read | events | Get Event By Slug. |
| GET | v1/events/{id} | read | events | Get Event By ID. |
| GET | v1/incentives/earnings | read | incentives | Get Your Incentive Earnings. |
| GET | v1/market/id/{id} | read | markets | Get Market By ID. |
| GET | v1/market/slug/{id} | read | markets | Get Market By Slug. |
| GET | v1/markets | read | markets | Get Markets. |
| GET | v1/markets/{id}/bbo | read | markets | Get Market BBO. |
| GET | v1/markets/{id}/book | read | markets | Get Market Book. |
| GET | v1/markets/{id}/settlement | read | markets | Get Market Settlement. |
| POST | v1/order/close-position | write | orders | Close Position Order. |
| POST | v1/order/preview | write | orders | Preview an order without placing it. Kept out of read with the other order endpoints. |
| GET | v1/order/{id} | read | orders | Get Order. |
| POST | v1/order/{id}/cancel | write | orders | Cancel Order. |
| POST | v1/order/{id}/modify | write | orders | Modify Order. |
| POST | v1/orders | write | orders | Create Order. |
| POST | v1/orders/batched | write | orders | Create Multiple Orders. |
| POST | v1/orders/batched/cancel | write | orders | Cancel Multiple Orders. |
| POST | v1/orders/batched/modify | write | orders | Modify Multiple Orders. |
| GET | v1/orders/open | read | orders | Get Open Orders. |
| POST | v1/orders/open/cancel | write | orders | Cancel All Open Orders. |
| GET | v1/partners/{id}/events/{id} | read | partners | Get Event By Partner External ID. |
| GET | v1/portfolio/activities | read | portfolio | Get Activities. |
| GET | v1/portfolio/positions | read | portfolio | Get User Positions. |
| GET | v1/price-history | read | price history | Get Price History. |
| GET | v1/rfqs | read | rfqs | Get RFQs. |
| POST | v1/rfqs | write | rfqs | Create RFQ. |
| GET | v1/rfqs/quotes | read | rfqs | Get quotes. |
| POST | v1/rfqs/quotes | write | rfqs | Create quote. |
| GET | v1/rfqs/trades | read | rfqs | Get RFQ trades. |
| GET | v1/rfqs/user-id | read | rfqs | Get RFQ user ID. |
| DELETE | v1/rfqs/{id} | write | rfqs | Delete RFQ. |
| DELETE | v1/rfqs/{id}/quotes/{id} | write | rfqs | Delete quote. |
| PUT | v1/rfqs/{id}/quotes/{id}/accept | write | rfqs | Accept quote. |
| PUT | v1/rfqs/{id}/quotes/{id}/confirm | write | rfqs | Confirm quote. |
| GET | v1/search | read | search | Search. |
| GET | v1/series | read | series | Get Series. |
| GET | v1/series/id/{id} | read | series | Get Series By ID. |
| GET | v1/sports | read | sports | Get Sports. |
| GET | v1/sports/players | read | sports | Get Sports Players. |
| GET | v1/sports/teams | read | sports | Get Sports Teams. |
| GET | v1/sports/teams/provider | read | sports | Get Sports Teams For Provider. |
| GET | v1/sports/{id}/events | read | sports | Get Sports Events. |
| GET | v2/leagues | read | sports | Get All Leagues. |
| GET | v2/leagues/{id} | read | sports | Get League By Slug. |
| GET | v2/leagues/{id}/events | read | sports | Get Events By League Slug. |
| GET | v2/order/{id} | read | orders | Get Order v2. |
| POST | v2/order/{id}/modify | write | orders | Modify Order v2. |
| POST | v2/orders | write | orders | Create Order v2. |
| GET | v2/orders/open | read | orders | Get Open Orders v2. |
| GET | v2/sports | read | sports | Get All Sports. |
| GET | v2/sports/{id} | read | sports | Get Sport By Slug. |
| GET | v2/sports/{id}/events | read | sports | Get Events By Sport Slug. |
| GET | v2/tags | read | tags | Get Tags. |
| GET | v2/tags/slug/{id} | read | tags | Get Tag By Slug. |
| GET | v2/tags/{id} | read | tags | Get Tag By ID. |
| GET | v2/tags/{id}/events | read | tags | Get Events For A Tag. |
