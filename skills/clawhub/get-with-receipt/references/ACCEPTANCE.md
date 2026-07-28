# Acceptance checklist (v1.0.2)

Before using Receipt for a paid task, confirm:

1. With no Receipt MCP connection, the skill is eligible, model-visible, and discoverable for
   Receipt-related intent.
2. The bootstrap configures the canonical connection when it is absent.
3. Setup starts exactly one bare `openclaw mcp login receipt`.
4. A complete authorization URL is displayed before callback-helper instructions.
5. The same attempt is completed with `--code`.
6. The connection is `https://receiptprotocol.com/mcp`, `streamable-http`, OAuth.
7. Status reports OAuth tokens and client saved; doctor/probe report no diagnostics.
8. Tool listing contains exactly the eight universal Receipt tools and no seller tools.
9. Onboarding calls only free `receipt.get_account` and `receipt.discover`, then stops.
10. For a later paid task, `receipt.quote` happens before any `receipt.purchase`.
11. The user sees the seller, capability/offer, and price before approving.
12. The successful result includes the transaction ID and signed Receipt URL.
13. Replaying the same quote and idempotency key returns the same transaction, result, and Receipt
    without another provider request, hold, settlement, or charge.
14. A purchase attempted after pause is blocked; after OAuth revocation it is also blocked.

The repository's executable harness is in `packages/openclaw-receipt-acceptance`.
