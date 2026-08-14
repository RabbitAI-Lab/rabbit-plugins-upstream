## Description:

BridgeNode gives agents OpenAI-compatible chat completions and MCP access paid per request with Solana USDC via x402, without API keys, registration, or subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bridgenode](https://clawhub.ai/user/bridgenode)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when an AI agent needs paid LLM inference through an OpenAI-compatible endpoint or MCP tool without a provider API key. It teaches the agent how to discover models and prices, complete the x402 payment flow, and call BridgeNode with Solana USDC.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables agents to buy LLM inference with real Solana USDC per request.

Mitigation: Use a dedicated low-balance wallet, check the 402 amount and live model prices before signing, and apply per-call and daily spending limits where supported.

Risk: On-chain payments are generally not reversible after service is delivered, and exact-scheme pricing can charge for the requested max_tokens even when fewer tokens are produced.

Mitigation: Set conservative max_tokens values, review settlement receipts, and increase spending limits only after confirming expected costs.

## Reference(s):

- [BridgeNode ClawHub skill page](https://clawhub.ai/bridgenode/skills/bridgenode)
- [BridgeNode publisher profile](https://clawhub.ai/user/bridgenode)
- [BridgeNode homepage](https://bridgenode.cc)
- [BridgeNode models and pricing](https://bridgenode.cc/v1/models)
- [BridgeNode agent install map](https://bridgenode.cc/llms.txt)
- [BridgeNode MCP endpoint](https://bridgenode.cc/mcp)
- [BridgeNode skill repository](https://github.com/applefanaimail-blip/bridgenode-skill)
- [x402 documentation](https://docs.x402.org)
- [BridgeNode Python SDK](https://pypi.org/project/bridgenode-llm)
- [BridgeNode TypeScript SDK](https://www.npmjs.com/package/@bridgenode/llm)
- [BridgeNode x402-list service page](https://x402-list.com/services/bridgenode)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands, code examples, endpoint URLs, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may lead an agent to execute paid API or MCP calls that spend real Solana USDC when the user provides a funded wallet and signs payments.]

## Skill Version(s):

1.0.17 (source: server release metadata; artifact frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
