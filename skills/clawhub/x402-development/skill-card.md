## Description:

Build internet-native payments with the x402 open protocol - HTTP 402 Payment Required for on-chain micropayments with no accounts or API keys. Use when developing paid APIs, paywalled content, AI agent payment flows, or MCP tools that charge per call. Covers the TypeScript, Python, and Go SDKs across EVM, Solana, Stellar, Aptos, NEAR, and XRPL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to build, test, and integrate x402 payment flows for paid APIs, paywalled content, AI agent payments, MCP tools, and multi-network on-chain settlement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill supports crypto payment flows, so applying examples with production keys or mainnet funds can create financial exposure.

Mitigation: Use testnet and low-balance keys for examples, keep production private keys away from general agents, and require spending caps, explicit approval, trusted endpoint or tool allowlists, and approval-revocation procedures before mainnet use.

Risk: Payment integration guidance can affect settlement behavior when copied into paid APIs, MCP tools, or agent payment workflows.

Mitigation: Review generated code and configuration before deployment, test payment paths against development or testnet facilitators, and require operator approval before enabling production settlement.

## Reference(s):

- [ClawHub source homepage](https://github.com/tenequm/skills/tree/main/skills/x402)
- [x402 GitHub repository](https://github.com/x402-foundation/x402)
- [x402 Documentation](https://docs.x402.org)
- [x402 Website](https://x402.org)
- [x402 Protocol Specification (v2)](references/protocol-spec.md)
- [Core Concepts](references/core-concepts.md)
- [TypeScript SDK Reference](references/typescript-sdk.md)
- [Python SDK Reference](references/python-sdk.md)
- [Go SDK Reference](references/go-sdk.md)
- [Transport Implementations](references/transports.md)
- [x402 Extensions Reference](references/extensions.md)
- [EVM Scheme Reference](references/evm-scheme.md)
- [Solana (SVM) Exact Scheme Reference](references/svm-scheme.md)
- [Aptos Exact Scheme Reference](references/aptos-scheme.md)
- [NEAR Exact Scheme Reference](references/near-scheme.md)
- [XRPL Exact Scheme Reference](references/xrpl-scheme.md)
- [Stellar Exact Scheme Reference](references/stellar-scheme.md)
- [Upto Scheme Reference](references/upto-scheme.md)
- [Lifecycle Hooks Reference](references/lifecycle-hooks.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code examples, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.11.1 (source: frontmatter, changelog, and server release evidence; released 2026-08-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
