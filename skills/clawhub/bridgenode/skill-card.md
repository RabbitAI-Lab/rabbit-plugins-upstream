## Description:

BridgeNode teaches agents to call an OpenAI-compatible inference API and MCP server, paying per request with Solana USDC through x402 without API keys or registration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bridgenode](https://clawhub.ai/user/bridgenode)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External developers and AI agents use this skill when they need OpenAI-compatible chat completions or MCP inference without provider API keys and can pay per request with Solana USDC via x402. It helps agents discover endpoints, check live prices, understand the payment flow, and use curl, Python, TypeScript, or MCP clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests can spend real Solana USDC on mainnet.

Mitigation: Use a small-balance wallet, check live prices and quoted 402 amounts before signing, and set available per-call and daily spending limits.

Risk: Unattended loops or repeated tool calls can make repeated paid requests.

Mitigation: Avoid unattended execution, enforce local budgets, and require review before agents sign payment requests.

Risk: Reasoning models can consume the max_tokens budget and return an empty answer without a refund.

Mitigation: Use an adequate max_tokens value for reasoning models, start with small tests, and treat empty paid responses as a cost risk.

## Reference(s):

- [BridgeNode ClawHub Skill](https://clawhub.ai/bridgenode/skills/bridgenode)
- [BridgeNode Website](https://bridgenode.cc)
- [Live Models and Prices](https://bridgenode.cc/v1/models)
- [BridgeNode Agent Map](https://bridgenode.cc/llms.txt)
- [x402 Documentation](https://docs.x402.org)
- [BridgeNode MCP Endpoint](https://bridgenode.cc/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown guidance with inline shell, JSON, Python, and TypeScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents through OpenAI-compatible API or MCP calls that may require x402 Solana USDC payment when used.]

## Skill Version(s):

1.0.24 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
