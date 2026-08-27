## Description:

Build with MPP (Machine Payments Protocol), an open HTTP 402 payment protocol for paid APIs, payment-gated content, AI agent payment flows, MCP tool payments, pay-per-token streaming, and metered billing across TypeScript, Python, and Rust SDKs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to design, implement, test, and operate MPP-enabled paid HTTP APIs, payment-aware agents, MCP tools, streaming sessions, subscriptions, and payment proxies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment integrations can expose wallet mnemonics, signing secrets, Stripe keys, wallet stores, session stores, subscription keys, or other financial credentials if copied into chats, logs, or unprotected environment files.

Mitigation: Use testnet/regtest or low-balance wallets during development, never paste exported private keys or mnemonics into chats or logs, and protect .env files and wallet/session/subscription stores as financial credentials.

Risk: Agents configured from generated guidance may spend funds unexpectedly or pay unintended recipients or hosts.

Mitigation: Set explicit spend caps plus recipient and host allowlists before granting agents payment authority.

Risk: The skill covers production payment rails, so incorrect implementation details can affect live payment flows.

Mitigation: Install only for MPP payment integrations and review generated code, configuration, and operational guidance before deploying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/mpp)
- [Publisher source homepage](https://github.com/tenequm/skills/tree/main/skills/mpp)
- [Payment HTTP Authentication Scheme IETF draft](https://datatracker.ietf.org/doc/draft-ryan-httpauth-payment/)
- [MPP documentation](https://mpp.dev)
- [Tempo documentation](https://docs.tempo.xyz)
- [Protocol Specification](references/protocol-spec.md)
- [mppx TypeScript SDK Reference](references/typescript-sdk.md)
- [Python SDK](references/python-sdk.md)
- [mpp Rust SDK](references/rust-sdk.md)
- [Tempo Payment Method](references/tempo-method.md)
- [Stripe Payment Method](references/stripe-method.md)
- [Lightning Payment Method](references/lightning-method.md)
- [Sessions](references/sessions.md)
- [Subscriptions](references/subscriptions.md)
- [Discovery and Proxy](references/discovery-and-proxy.md)
- [MCP and HTTP Transports](references/transports.md)
- [CLI Reference](references/cli.md)
- [Custom Payment Methods](references/custom-methods.md)
- [Production Gotchas](references/production-gotchas.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill output; generated guidance may include payment, wallet, and secret-handling instructions that require review before use.]

## Skill Version(s):

0.10.1 (source: frontmatter metadata and changelog, released 2026-08-21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
