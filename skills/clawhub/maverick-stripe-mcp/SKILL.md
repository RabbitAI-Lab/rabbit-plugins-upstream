---
name: maverick-stripe-mcp
description: Search and read ordinary single-account Stripe data through Stripe's official remote MCP with MCP-native OAuth. The config-level allowlist hides all write, mixed, feedback, and preview-only top-level tools. Use for sandbox-first inspection of Stripe payments, customers, invoices, subscriptions, account context, and documentation.
homepage: https://docs.stripe.com/mcp
metadata:
  openclaw:
    emoji: '💳'
    requires:
      bins:
        - mcporter
      env:
        - MAVERICK_STRIPE_MCP_REFRESH_TOKEN
        - MAVERICK_STRIPE_MCP_CLIENT_ID
        - MAVERICK_STRIPE_MCP_ACCESS_TOKEN
    primaryEnv: MAVERICK_STRIPE_MCP_REFRESH_TOKEN
    setup:
      script: scripts/setup.sh
    install:
      - id: node
        kind: node
        package: mcporter@0.12.3
        bins:
          - mcporter
        label: Install mcporter (node)
---

# Stripe

## How to use this skill

This skill uses Stripe's official remote MCP server at `https://mcp.stripe.com`. Maverick's config-level allowlist is the source of truth for which of Stripe's advertised tools are visible to the assistant.

**Step 1 — Discover the live tool catalog and any server-published usage instructions.** Always run this first; do not rely on tool names from memory:

```sh
mcporter --config {baseDir}/mcporter.json list maverick-stripe-mcp --schema
```

The output includes the server's `Instructions:` field, if published, and a JSON Schema for every tool's parameters. Treat this as the authoritative reference for the rest of the session.

**Step 2 — Call an allowlisted read tool** using the form `maverick-stripe-mcp.<tool>`:

```sh
mcporter --config {baseDir}/mcporter.json call maverick-stripe-mcp.<tool> <arg>=<value> ...
```

Add `--output json` for structured output and transport-error envelopes:

```sh
mcporter --config {baseDir}/mcporter.json call --output json maverick-stripe-mcp.<tool> ...
```

## Safety

The exposed tool set is intentionally read-only. `stripe_api_write`, `create_refund`, the mixed read/write `stripe_report`, `send_stripe_mcp_feedback`, and the Treasury-preview `get_balance_summary` are invisible at the mcporter protocol layer. Refunds, subscriptions, invoices, payment links, customer/payment mutations, and every other write remain unavailable until Maverick has a real execution-time approval gate.

`stripe_api_read` is documented as GET-only, but it accepts broad Stripe API paths and may reach preview GET endpoints. mcporter filters exact tool names, not tool arguments, so do not describe this allowlist as a resource-path restriction.

Use Stripe sandbox for validation and confirm the selected Stripe environment before account-data reads. The broker does not persist sandbox/live mode, so local authorization or sync state proves neither environment. Sandbox and live MCP authorizations are separate; never infer one from the other or switch environments without the user's explicit intent.

## Authentication

Ordinary single-account authorization uses Stripe's MCP-native OAuth flow: protected-resource discovery, dynamic public-client registration, Authorization Code with PKCE S256, and refresh tokens. Credentials are provisioned by `scripts/setup.sh` into mcporter's local vault; mcporter sends and refreshes the resource-bound bearer token for the official remote MCP.

Setup needs `bash`, `jq`, `basename`, and `mcporter` (>= v0.11.0). Run setup only after fresh authorization or credential rotation. Re-running it with stale values can overwrite a refresh token already rotated in the vault.

Dashboard revocation is user-visible and invalidates the remote grant. Maverick does not currently receive a provider-revocation callback, so its local grant can remain `active`/`synced` until a remote call fails or the user disconnects. Those local states prove only that authorization was saved and the bundle/credential projection succeeded; they are not evidence that Stripe remains authorized.

Stripe Connect connected-account operations are a separate exception. They require a restricted key plus `Stripe-Account` context and must never be described as MCP-native OAuth. This bundle does not implement or expose that path.

## References

- Stripe MCP overview and OAuth notes: <https://docs.stripe.com/mcp>
- Model Context Protocol authorization: <https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization>
- Stripe restricted API keys: <https://docs.stripe.com/keys/restricted-api-keys>
- mcporter config reference: <https://github.com/openclaw/mcporter/blob/main/docs/config.md>
