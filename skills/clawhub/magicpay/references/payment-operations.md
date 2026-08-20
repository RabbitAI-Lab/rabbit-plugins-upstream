# Native Payment Operations

Use this workflow for the unified MagicPay balance, direct crypto transfers,
and HTTP-native x402 purchases. It is separate from browser checkout and never
uses `authorize-payment` or `magicpay commit`.

## Contents

- [Total, exact balance, and funding](#total-exact-balance-and-funding)
- [Direct-transfer contract](#direct-transfer-contract)
- [Balance and state meanings](#balance-and-state-meanings)
- [x402 purchase contract](#x402-purchase-contract)
- [Seller result presentation](#seller-result-presentation)

## Total, exact balance, and funding

- `magicpay payment-balance` returns `magicpay.total-balance/v1` with
  `authority: authoritative_unified`. Its `available` quantity is the sole
  customer spend authority for x402, crypto transfers, and card payments.
- `magicpay payment-balance --asset-namespace <value> --asset-id <value>
  --network <value>` returns a diagnostic exact-asset projection. Never require
  that rail-specific balance to fund a customer payment; MagicPay selects and
  converts infrastructure inventory behind the unified balance.
- Immediately before creating any crypto, x402, or card payment approval, run
  `magicpay payment-balance` without asset flags. Tell the user, in the language
  they are using, that the unified balance was checked and include both the
  available USD amount and maximum debit required. If it is insufficient, do
  not create the approval. After approval, the backend atomically rechecks and
  reserves the same unified balance before provider submission.
- `magicpay funding-address --idempotency-key <key> --asset-namespace <value>
  --asset-id <value> --network <value>` creates or replays one native funding
  intent. Present the exact returned address, asset, and network; reuse the same
  key and refresh the unified balance only after Ledger confirmation. It is not
  `magicpay top-up-link`.

## Direct-transfer contract

1. Run `magicpay status`.
2. Resolve the exact requested delivery asset, network, and scale.
3. Run `magicpay payment-balance` without asset flags and verify the unified
   `available >= maximumDebit`. Do not block on the user's USDT/USDC or network
   breakdown; delivery liquidity and conversion are backend responsibilities.
   State the successful unified-balance check and both amounts to the user
   before continuing.
4. Require the user-intended display amount, asset, network, destination, and
   maximum debit. Convert display amounts to canonical integers with exact
   string arithmetic; never use floating point or guess a fee buffer.
5. Start or reuse one dedicated payment/crypto intent session and retain its
   exact `intentSessionId`.
6. Create one stable idempotency key for this user intent. Run `magicpay
   direct-transfer` once with the session id, exact tuple, principal, maximum
   debit, and destination.
7. Run `magicpay requests`. Share the operation-backed approval URL when
   present and execute its exact returned poll command. Do not create another
   approval or route the transfer through browser checkout.
8. Retain the returned `operationId`. Read it with `magicpay payment-operation`
   and branch only on structured `state`, `nextAction`, and `retry.mode`.
9. Run `magicpay reconcile-payment-operation` only when the operation explicitly
   directs reconciliation. Pending, unknown, busy, or reconciliation-required
   state never permits a replacement operation or idempotency key.
10. Claim settlement only for terminal `completed`, then refresh the unified
    balance. Approval, reservation, provider submission, callback acceptance,
    and session `in_progress` are not settlement.

## Balance and state meanings

- `posted`: booked quantity in the unified customer liability.
- `reserved`: maximum debit held by active approved operations; explain it as
  in flight, not as another MagicCard balance.
- `available`: unified spendable quantity after active reservations.
- `awaiting_approval`: no reservation exists yet.
- `reserved`, `external_not_submitted`, `external_pending`,
  `reconciliation_required`, `settlement_confirmed`, and `failure_confirmed`:
  the same operation may still own its reservation.
- `completed`: settlement and Ledger consequence are terminal.
- `definitively_failed`: release is terminal; do not reuse that failed attempt.

Denial, expiry, cancellation, and definitive failure are terminal for the
current approval/operation attempt. A user may request a new intent only after
that prior terminal result is established. Ambiguous or pending state always
continues the original operation.

## x402 purchase contract

Choose exactly one source:

- **Direct known URL:** use `--resource-url <known-https-x402-url>` when the
  user or trusted context identifies it as x402. Make zero MagicSearch calls
  and zero browser calls: do not launch, attach, authorize a card payment, or
  commit. GET is the default. When the seller's trusted API contract requires
  JSON POST, preserve its exact body with `--resource-method POST
  --resource-body '<json>'`; never guess a method, package code, or body.
- **Discovery:** when an x402 purchase target is unknown, use the intent-first
  MagicSearch flow below. Do not expose or reconstruct the hidden payable URL.

```bash
magicsearch intent "<purchase request>" --json

# Only when the draft requests typed clarification:
magicsearch clarify --request <intentDraftId> --revision <revision> \
  --answer <field=value> --json

magicpay start-session "<short task>" --intent-draft <intentDraftId>
magicsearch resolve-intent --request <intentDraftId> \
  --session <intentSessionId> --json
```

Branch only on the structured resolution. For `methodType: "x402"`, pass the
returned opaque `selectionRef` exactly once as `--selection-ref <selectionRef>`.
For `methodType: "mcp" | "api" | "reversed_api" | "browser"`, use the returned
URL in the existing non-x402 browser product flow. MagicSearch discovers a
target; it never approves or executes payment.

1. Run `magicpay status`, then start or reuse one dedicated payment intent
   session and retain its exact `intentSessionId`.
2. Run `magicpay payment-balance` without asset flags and verify unified
   `available >= maximumDebit`. Do not require Base USDC or any other
   network-specific customer balance; MagicPay supplies and converts settlement
   inventory behind the scenes. State the successful unified-balance check and
   both amounts to the user before continuing.
3. Accept either the canonical HTTPS resource URL or the exact MagicSearch
   `selectionRef`. Create one stable idempotency key for this user intent.
4. Run `magicpay x402-purchase --session <intentSessionId> --idempotency-key
   <key> --maximum-debit <integer> ((--resource-url <url> [--resource-method
   GET]) | (--resource-url <url> --resource-method POST --resource-body
   '<json>') | --selection-ref <ref>)`
   once. Do not create a separate `authorize-payment` request.
5. Retain the returned `operationId`. Run `magicpay requests --session
   <intentSessionId>`, locate the request for that operation, share its approval
   URL, immediately run its exact returned `pollCommand`, and remain attached.
   When approval is detected, acknowledge it briefly before another long
   operation read.
6. Continue only through that request and operation. Approval resumes the same
   x402 operation; never change the session, idempotency key, operation id,
   seller resource URL/method/body, or maximum debit during polling or
   reconciliation.
7. Read `magicpay payment-operation <operationId>`. Run `magicpay
   reconcile-payment-operation <operationId>` only when its structured
   `nextAction` directs reconciliation.
8. Claim purchase success only when the operation is terminal `completed` and
   `magicpay x402-purchase-result --operation-id <operationId>` returns the
   operation-owned result. Approval, HTTP success, submission, or pending state
   is not completion.

Denial, expiry, a changed seller requirement, or definitive failure ends that
attempt without a paid result. Insufficient balance remains attached to the
same operation and may be resumed after top-up; it never authorizes a
replacement purchase automatically.

## Seller result presentation

Fetch `magicpay x402-purchase-result --operation-id <operationId>` only after
the retained operation is terminal `completed`. Require the operation-owned
`magicpay.x402-result/v1` contract and its existing integrity validation.

- For `application/json`, decode Base64 and parse JSON, then present the
  meaningful structured seller response.
- For `text/*`, decode the bounded UTF-8 text.
- For binary or unknown media, present safe type, length, and digest metadata;
  do not dump raw Base64 into chat.
- Missing, expired, malformed, oversized, length-mismatched, or digest-mismatched
  data is not a usable purchase result. Do not claim success from the seller
  HTTP status or `resultRef` alone.

Complete with the bought resource, terminal state, backend-resolved source and
settlement facts, and decoded result or safe artifact summary. Retain
`operationId`, `resultRef`, `sha256`, and `expiresAt`, then refresh the unified
balance. Rail and settlement assets are receipt facts, not separate customer
balances.
