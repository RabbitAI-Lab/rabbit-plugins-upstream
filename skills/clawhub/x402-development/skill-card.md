## Description: <br>
Build internet-native payments with the x402 open protocol - HTTP 402 Payment Required for on-chain micropayments with no accounts or API keys. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to build paid APIs, paywalled content, AI agent payment flows, MCP tools that charge per call, and multi-network x402 integrations across TypeScript, Python, and Go. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Examples can involve real wallet keys, token approvals, third-party facilitators, and real-money transactions. <br>
Mitigation: Use dedicated low-balance wallets, testnets, and a secret manager; verify facilitator and RPC providers; disclose third-party payment metadata handling; set spending limits for automated clients; and avoid broad or long-lived Permit2 approvals without a revocation plan. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/tenequm/skills/x402-development) <br>
- [Skill homepage](https://github.com/tenequm/skills/tree/main/skills/x402) <br>
- [x402 Foundation GitHub](https://github.com/x402-foundation/x402) <br>
- [x402 documentation](https://docs.x402.org) <br>
- [x402 protocol specification](https://github.com/x402-foundation/x402/tree/main/specs) <br>
- [Facilitator directory](https://docs.x402.org/dev-tools/facilitators) <br>
- [x402 Protocol Specification (v2)](references/protocol-spec.md) <br>
- [Core Concepts](references/core-concepts.md) <br>
- [TypeScript SDK Reference](references/typescript-sdk.md) <br>
- [Python SDK Reference](references/python-sdk.md) <br>
- [Go SDK Reference](references/go-sdk.md) <br>
- [Transport Implementations](references/transports.md) <br>
- [x402 Extensions Reference](references/extensions.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code blocks and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include wallet, facilitator, network, and environment-variable configuration guidance for x402 integrations.] <br>

## Skill Version(s): <br>
0.11.0 (source: server release metadata, skill frontmatter, and changelog, released 2026-07-30) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
