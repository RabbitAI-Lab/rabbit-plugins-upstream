## Description: <br>
Build internet-native payments with the x402 open protocol - HTTP 402 Payment Required for on-chain micropayments with no accounts or API keys. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and engineers use this skill to build x402 paid APIs, paywalled content, agent payment flows, MCP payment integrations, and multi-network on-chain payment clients and servers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: x402 examples can move real funds when connected to mainnet wallets or automatic payment flows. <br>
Mitigation: Use testnets until reviewed, use dedicated low-balance wallets, and add explicit budgets, allowlists, and confirmation controls before enabling real-money or MCP auto-payment flows. <br>
Risk: Private key environment variables grant signing authority for payment clients, servers, or facilitators. <br>
Mitigation: Store keys in managed secrets, avoid committing them to source control, and scope wallets and facilitator keys to the minimum balance and permissions needed. <br>
Risk: Non-local payment services can expose payment headers and settlement requests over the network. <br>
Mitigation: Require HTTPS for deployed services and review facilitator endpoints before using them with production wallets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/x402-development) <br>
- [Publisher profile](https://clawhub.ai/user/tenequm) <br>
- [OpenClaw homepage](https://github.com/tenequm/skills/tree/main/skills/x402) <br>
- [x402 documentation](https://docs.x402.org) <br>
- [x402 protocol repository](https://github.com/x402-foundation/x402) <br>
- [x402 protocol specifications](https://github.com/x402-foundation/x402/tree/main/specs) <br>
- [Core concepts](references/core-concepts.md) <br>
- [Protocol specification](references/protocol-spec.md) <br>
- [TypeScript SDK](references/typescript-sdk.md) <br>
- [Python SDK](references/python-sdk.md) <br>
- [Go SDK](references/go-sdk.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline code snippets, commands, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference optional wallet, facilitator, API key, and network environment variables for payment integrations.] <br>

## Skill Version(s): <br>
0.10.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
