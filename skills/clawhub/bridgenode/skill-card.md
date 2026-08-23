## Description:

BridgeNode provides pay-per-request LLM inference for agents through an OpenAI-compatible API and MCP server, using x402 payments with Solana USDC instead of API keys or subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bridgenode](https://clawhub.ai/user/bridgenode)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to let an agent discover BridgeNode endpoints, pricing, payment flow, SDK examples, and MCP access for paid or free LLM chat completions. It is useful when an agent needs inference without a provider API key and can pay per request from its own Solana USDC wallet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables paid Solana mainnet USDC inference requests, so an agent can spend real funds per request.

Mitigation: Use a dedicated low-balance wallet, verify live prices and the exact 402 amount before signing, and set local spending caps where supported.

Risk: Wallet private key exposure could compromise the payment wallet.

Mitigation: Keep SVM_PRIVATE_KEY out of version control and away from production funds; use a wallet dedicated to this service.

Risk: Incorrect token limits or reasoning-model settings can cause unexpectedly costly requests or empty answers that may not be refunded.

Mitigation: Set max_tokens deliberately, use streaming for long generations, check current pricing, and follow the documented reasoning-model guidance.

## Reference(s):

- [BridgeNode ClawHub Skill](https://clawhub.ai/bridgenode/skills/bridgenode)
- [BridgeNode Website](https://bridgenode.cc)
- [BridgeNode Models and Live Pricing](https://bridgenode.cc/v1/models)
- [BridgeNode MCP Endpoint](https://bridgenode.cc/mcp)
- [BridgeNode Agent Install Map](https://bridgenode.cc/llms.txt)
- [x402 Documentation](https://docs.x402.org)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown instructions with inline shell, Python, TypeScript, JSON, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes OpenAI-compatible chat completion calls, MCP setup guidance, x402 payment flow details, and Solana USDC wallet requirements.]

## Skill Version(s):

1.0.25 (source: server release evidence; artifact SKILL.md frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
