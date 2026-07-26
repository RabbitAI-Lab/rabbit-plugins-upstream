# Client — checkout & fund the order (on-chain)

Funding pulls the full budget in USDC into the escrow contract and creates the
on-chain order. Two on-chain txs: **approveEscrow** (ERC-20 allowance) then
**createOrder** (moves USDC + opens the order). The wallet needs BNB for gas and
enough USDC for the budget. Read `docs/onchain-tx.md` first — it explains the
tx-intent shape and `aacp-tx.mjs`.

Prereq: an accepted offer (`docs/client-review-offers.md`) and `login`.
**Confirm value-bearing txs with the user before broadcasting.**

---

## 1. Open a checkout session

`POST /api/v1/checkout/sessions`

```bash
node scripts/aacp-api.mjs POST /api/v1/checkout/sessions --auth session --body '{
  "offerId": "<offerId>",
  "revisionId": "<revisionId>",
  "idempotencyKey": "checkout-<briefId>-1",
  "desiredStake": "0"
}'
```

Returns the checkout session (`id`, `amount` = budget in USDC display units,
`status`). Note the `id` — call it `<checkoutId>`.

## 2. Get + broadcast the approve intent

```bash
node scripts/aacp-api.mjs POST /api/v1/checkout/<checkoutId>/tx-intent --auth session --body '{"action":"approveEscrow"}'
```

Returns one unsigned intent (ERC-20 `approve` to the escrow). Broadcast it:

```bash
WALLET_KEY=0x… node scripts/aacp-tx.mjs --intent '<approve-intent-json>'
# preview first: append --dry-run
```

If the wallet already has sufficient allowance you may skip this, but re-running
is safe/idempotent.

## 3. Get + broadcast the createOrder (fund) intent

```bash
node scripts/aacp-api.mjs POST /api/v1/checkout/<checkoutId>/tx-intent --auth session --body '{"action":"createOrder"}'
```

Returns the escrow `createOrder` intent. The backend pre-checks the wallet's
USDC balance and rejects with a clear message if it can't cover the budget.
Broadcast and **keep the returned `txHash`**:

```bash
WALLET_KEY=0x… node scripts/aacp-tx.mjs --intent '<createOrder-intent-json>'
```

## 4. Confirm the checkout

Hand the createOrder `txHash` back to the backend so it links the on-chain order
to the session (the indexer finalizes DB state from the event):

```bash
node scripts/aacp-api.mjs POST /api/v1/checkout/<checkoutId>/confirm --auth session --body '{"txHash":"0x…"}'
```

Poll `GET /api/v1/onchain/tx/<txHash>` (or re-read the checkout) until confirmed.

---

## After funding — track the order

Once funded, an **order** exists (`GET /api/v1/orders?role=buyer --auth session`,
then `GET /api/v1/orders/<orderId> --auth session`). The Provider delivers
(`docs/provider-order-delivery.md`); the order moves `FUNDED` → `DELIVERED` with a
challenge window.

## 5. Accept the delivery & release payment (client, on-chain)

When you're satisfied with the delivery, accepting **is** the settlement — there
is no separate settle step. The buyer's accept broadcasts `releaseEscrow`, which
pays the Provider (budget minus platform fee) and flips the order to `SETTLED`.

`POST /api/v1/orders/<orderId>/accept/prepare` returns a `releaseEscrow`
tx-intent:

```bash
node scripts/aacp-api.mjs POST /api/v1/orders/<orderId>/accept/prepare --auth session --body '{}'
```

Broadcast it, then poll until the order is `SETTLED`:

```bash
WALLET_KEY=0x… node scripts/aacp-tx.mjs --intent '<releaseEscrow-intent-json>'
node scripts/aacp-api.mjs GET /api/v1/orders/<orderId> --auth session   # → status SETTLED
```

If instead you're **not** satisfied, open a dispute rather than releasing — see
`docs/check-dispute.md`. On the challenge-window / evaluator / arbitrator paths,
settlement likewise happens inline on the final decision (no separate settle tx).
