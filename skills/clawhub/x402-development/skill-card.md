## Description:

Build internet-native payments with the x402 open protocol - HTTP 402 Payment Required for on-chain micropayments with no accounts or API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build paid APIs, paywalled endpoints, AI-agent payment flows, MCP tools that charge per call, and multi-network x402 integrations across supported SDKs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment examples can involve real wallets, private keys, and on-chain funds.

Mitigation: Use testnets or low-balance dedicated wallets, store secrets in a vault or managed wallet service, and avoid placing primary wallet keys in agent environments.

Risk: Autonomous payment flows can spend funds without sufficient operator review.

Mitigation: Add confirmation steps, spending policies, and transaction limits before allowing agents to make or settle payments.

Risk: Untrusted facilitator endpoints can affect payment verification and settlement behavior.

Mitigation: Use known facilitator endpoints, query supported networks at runtime, and choose production facilitators from documented sources for mainnet deployments.

Risk: The public x402.org facilitator is documented for development and testnet workflows, not as a production mainnet default.

Mitigation: Switch facilitator URL, network IDs, and wallet addresses before production deployment, and test with small amounts first.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/x402-development)
- [ClawHub publisher profile](https://clawhub.ai/user/tenequm)
- [Skill homepage](https://github.com/tenequm/skills/tree/main/skills/x402)
- [x402 Foundation GitHub](https://github.com/x402-foundation/x402)
- [x402 documentation](https://docs.x402.org)
- [x402 website](https://x402.org)
- [Facilitator directory](https://docs.x402.org/dev-tools/facilitators)
- [Core Concepts](references/core-concepts.md)
- [Protocol Specification](references/protocol-spec.md)
- [TypeScript SDK Reference](references/typescript-sdk.md)
- [Python SDK Reference](references/python-sdk.md)
- [Go SDK Reference](references/go-sdk.md)
- [EVM Scheme Reference](references/evm-scheme.md)
- [Solana Scheme Reference](references/svm-scheme.md)
- [Stellar Scheme Reference](references/stellar-scheme.md)
- [Aptos Scheme Reference](references/aptos-scheme.md)
- [NEAR Scheme Reference](references/near-scheme.md)
- [XRPL Scheme Reference](references/xrpl-scheme.md)
- [Transport Reference](references/transports.md)
- [Extensions Reference](references/extensions.md)
- [Lifecycle Hooks Reference](references/lifecycle-hooks.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill; examples may include wallet keys, facilitator endpoints, SDK package versions, and network identifiers.]

## Skill Version(s):

0.11.2 (source: server release metadata, skill metadata, and changelog, released 2026-08-21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
