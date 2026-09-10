## Description:

Build with MPP (Machine Payments Protocol), an HTTP 402 payment protocol for paid APIs, payment-gated endpoints, agent payment flows, MCP tool payments, and metered billing across TypeScript, Python, and Rust SDKs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to add machine-to-machine payments to APIs, agent workflows, MCP tools, streaming services, and metered billing systems. It provides implementation guidance for MPP servers and clients across supported payment methods and SDKs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment-enabled agent workflows can move real funds or reserve channel deposits when mainnet wallets, Stripe keys, or payment credentials are used.

Mitigation: Start with testnet or sandbox rails, avoid unattended mainnet approvals, use low-balance or delegated wallets with spend limits, and review payment or skill-registration commands before running them.

Risk: Wallet mnemonics, MPP signing secrets, and Stripe API keys may be required for examples or deployments.

Mitigation: Keep secrets out of source control, scope credentials to the deployment, and rotate MPP signing keys with an overlap window for in-flight challenges.

Risk: Session billing can leave deposits reserved or revenue unredeemed if state and settlement are not configured correctly.

Mitigation: Use a persistent store in production, configure settlement or close sweeps, and set a clear idle-channel close policy.

Risk: The skill spans multiple payment rails and upstream SDK packages with different trust, dependency, and versioning assumptions.

Mitigation: Choose only the rails the deployment trusts, pin package versions, and verify SDK compatibility before production rollout.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/mpp)
- [Publisher profile](https://clawhub.ai/user/tenequm)
- [Source homepage](https://github.com/tenequm/skills/tree/main/skills/mpp)
- [MPP website](https://mpp.dev)
- [Payment HTTP Authentication Scheme draft](https://datatracker.ietf.org/doc/draft-ryan-httpauth-payment/)
- [Tempo documentation](https://docs.tempo.xyz)
- [Stripe MPP documentation](https://docs.stripe.com/payments/machine/mpp)
- [Protocol specification](references/protocol-spec.md)
- [TypeScript SDK reference](references/typescript-sdk.md)
- [Python SDK reference](references/python-sdk.md)
- [Rust SDK reference](references/rust-sdk.md)
- [CLI reference](references/cli.md)
- [Production gotchas](references/production-gotchas.md)
- [Sessions reference](references/sessions.md)
- [Subscriptions reference](references/subscriptions.md)
- [Tempo payment method](references/tempo-method.md)
- [Stripe payment method](references/stripe-method.md)
- [Lightning payment method](references/lightning-method.md)
- [Custom payment methods](references/custom-methods.md)
- [Discovery and payments proxy](references/discovery-and-proxy.md)
- [Transport bindings](references/transports.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code blocks, command examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers SDK usage, protocol concepts, payment method behavior, MCP transport guidance, CLI workflows, and production risk controls.]

## Skill Version(s):

0.10.2 (source: frontmatter, changelog, evidence.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
