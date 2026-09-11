## Description:

Build internet-native payments with x402 - HTTP 402 for on-chain micropayments, no accounts or API keys. Use for paid APIs, paywalled content, agent payment flows, or per-call MCP tools. TypeScript, Python, and Go SDKs across EVM and Solana.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build paid APIs, paywalled endpoints, agent payment flows, per-call MCP tools, and usage-based billing with x402 across TypeScript, Python, Go, EVM, Solana, and other supported settlement networks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet and facilitator keys can authorize payments or settlements if copied into real deployments.

Mitigation: Use low-balance test accounts for examples, store keys in a dedicated secret manager, and rotate any key exposed during testing.

Risk: Automatic payment retries can spend funds unexpectedly when limits or destination checks are missing.

Mitigation: Add explicit spending limits, route allowlists, price checks, and review gates before enabling automatic payment behavior.

Risk: Bearer tokens used in lifecycle hook examples could be sent to an unintended endpoint.

Mitigation: Attach bearer tokens only for explicitly allowlisted final HTTPS origins and avoid global hooks that run for arbitrary destinations.

Risk: The public x402 facilitator is documented for development and testnet workflows, not as a production mainnet default.

Mitigation: Select a production facilitator from the facilitator directory or operate a reviewed self-hosted facilitator before mainnet use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/x402-development)
- [ClawHub metadata homepage](https://github.com/tenequm/skills/tree/main/skills/x402)
- [Core Concepts](references/core-concepts.md)
- [Protocol Specification](references/protocol-spec.md)
- [TypeScript SDK Reference](references/typescript-sdk.md)
- [Python SDK Reference](references/python-sdk.md)
- [Go SDK Reference](references/go-sdk.md)
- [EVM Scheme Reference](references/evm-scheme.md)
- [Solana Scheme Reference](references/svm-scheme.md)
- [Upto Scheme Reference](references/upto-scheme.md)
- [Aptos Scheme Reference](references/aptos-scheme.md)
- [NEAR Scheme Reference](references/near-scheme.md)
- [XRPL Scheme Reference](references/xrpl-scheme.md)
- [Stellar Scheme Reference](references/stellar-scheme.md)
- [Transport Implementations](references/transports.md)
- [Lifecycle Hooks Reference](references/lifecycle-hooks.md)
- [Extensions Reference](references/extensions.md)
- [x402 Foundation GitHub](https://github.com/x402-foundation/x402)
- [x402 Documentation](https://docs.x402.org)
- [x402 Facilitator Directory](https://docs.x402.org/dev-tools/facilitators)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline code blocks and implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces developer guidance and example commands for x402 payment integrations; does not execute payments directly.]

## Skill Version(s):

0.11.3 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
