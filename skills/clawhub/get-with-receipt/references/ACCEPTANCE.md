# Acceptance checklist

Before using Receipt for a paid task, confirm:

1. The connection is `https://receiptprotocol.com/mcp`, `streamable-http`, OAuth.
2. Tool listing contains exactly the eight universal Receipt tools and no seller tools.
3. `receipt.get_account` returns without a charge or provider execution.
4. `receipt.discover` returns without a charge or provider execution.
5. `receipt.quote` happens before any `receipt.purchase`.
6. The user sees the seller, capability/offer, and price before approving.
7. The successful result includes the transaction ID and signed Receipt URL.
8. Replaying the same quote and idempotency key returns the same transaction, result, and Receipt
   without another provider request, hold, settlement, or charge.
9. A purchase attempted after pause is blocked; after OAuth revocation it is also blocked.

The repository's executable harness is in `packages/openclaw-receipt-acceptance`.
