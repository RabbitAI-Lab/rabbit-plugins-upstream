# Airnode Hub HTTP contract

## Discover

`POST https://airnodehub.api3.org/resolve`

Body:

```json
{ "intent": "current USD price of ETH" }
```

The current response contains `intent` and `candidates`. A candidate includes `listing`, `airnode`, `operation`, `address`, `attestation`, `parameters`, `example`, `returns`, `payment`, and `why`.

Some deployments may also return `answerSource`. When present, preserve it: `localHeuristic` means model resolution failed and word overlap selected candidates. When absent, do not invent model-selection provenance.

## Inspect

A deployed Airnode's `GET /` returns its live OpenAPI document. The `x-airnode.address` field is the signer to verify. `x-airnode.payment.prices` names priced operations when payments are enabled.

The request schema for `POST /` contains one variant per operation. Read the live variant before sending parameters.

## Call

`POST <airnode-url>/`

```json
{ "operation": "coinPrice", "parameters": { "ids": "ethereum", "vs_currencies": "usd" } }
```

Success returns `airnode`, `requestHash`, `timestamp`, `data`, and `signature`.

Common statuses:

- `400`: missing, unknown, or mistyped parameter.
- `404`: unknown operation.
- `402`: priced operation needs x402 payment.
- `502`: upstream API failed.

A successful HTTP response is not trusted until request-bound attestation verification passes.