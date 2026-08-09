## Description:

Build with MPP (Machine Payments Protocol) - the open protocol for machine-to-machine payments over HTTP 402. Use when building paid APIs, payment-gated content or endpoints, AI agent payment flows, MCP tool payments, pay-per-token streaming, or metered pay-as-you-go billing. Covers the mppx TypeScript SDK (Hono/Express/Next.js/Elysia middleware), pympp Python SDK, and mpp Rust SDK, with Tempo stablecoins, Stripe cards, Lightning Bitcoin, and custom payment rails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to build payment-enabled HTTP APIs, paid content endpoints, agent payment flows, MCP tool payments, streaming metering, and pay-as-you-go billing with MPP SDKs and payment rails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment flows can spend real funds or authorize access to payment rails.

Mitigation: Start with testnet or regtest, use explicit spending limits, and avoid auto-approval with mainnet funds unless limits and authorization policies are in place.

Risk: The skill discusses mnemonics, private keys, Stripe keys, and MPP signing secrets.

Mitigation: Keep secrets out of logs and source control, and store operational credentials in a managed secret store.

Risk: Session and settlement settings can affect whether channels are closed and vouchers are redeemed.

Mitigation: Review session storage, recovery, and settlement schedules before production deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/mpp)
- [Metadata Homepage](https://github.com/tenequm/skills/tree/main/skills/mpp)
- [Payment HTTP Authentication Scheme](https://datatracker.ietf.org/doc/draft-ryan-httpauth-payment/)
- [Tempo Documentation](https://docs.tempo.xyz)
- [MPP Core Protocol Specification](references/protocol-spec.md)
- [mppx TypeScript SDK Reference](references/typescript-sdk.md)
- [pympp Python SDK](references/python-sdk.md)
- [mpp Rust SDK](references/rust-sdk.md)
- [mppx CLI](references/cli.md)
- [Tempo Payment Method](references/tempo-method.md)
- [Stripe Payment Method](references/stripe-method.md)
- [Lightning Payment Method](references/lightning-method.md)
- [Custom Payment Methods](references/custom-methods.md)
- [Sessions](references/sessions.md)
- [Subscription Intent (Tempo)](references/subscriptions.md)
- [Discovery and the Payments Proxy](references/discovery-and-proxy.md)
- [Transports](references/transports.md)
- [Production Gotchas](references/production-gotchas.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include payment, network, SDK, session, and secret-management configuration guidance.]

## Skill Version(s):

0.10.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
