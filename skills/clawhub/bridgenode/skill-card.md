## Description:

BridgeNode provides OpenAI-compatible and MCP LLM inference for agents, with optional pay-per-request Solana USDC payments via x402, free models, tool calling, and live model pricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bridgenode](https://clawhub.ai/user/bridgenode)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External developers and AI agents use BridgeNode to access LLM chat completions without provider API keys, using free models or signing x402 Solana USDC payments for paid models. It is useful when agents need OpenAI-compatible HTTP or MCP inference with transparent per-request pricing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid requests can spend real Solana USDC from the agent wallet.

Mitigation: Use free models first, connect only a dedicated low-balance wallet for paid use, set hard per-call and daily spending limits, and verify the network, USDC mint, amount, and recipient before signing.

Risk: Remote MCP/package execution can run wallet-enabled code without a pinned version.

Mitigation: Pin MCP and package versions instead of using @latest, and avoid one-shot npx execution for wallet-enabled workflows.

Risk: Automatic signing examples may be used without mandatory spending controls.

Mitigation: Require local spending caps before signing any payment and fail closed when limits are absent or exceeded.

Risk: Some free or reasoning models may be slow, overloaded, or return empty answers with too-small token budgets.

Mitigation: Prefer the documented reliable free model when starting, retry transient failures, and use max_tokens of at least 200 for reasoning-prone models.

## Reference(s):

- [BridgeNode Skill on ClawHub](https://clawhub.ai/bridgenode/skills/bridgenode)
- [BridgeNode Website](https://bridgenode.cc)
- [Live Models and Pricing](https://bridgenode.cc/v1/models)
- [Chat Completions Endpoint](https://bridgenode.cc/v1/chat/completions)
- [MCP Endpoint](https://bridgenode.cc/mcp)
- [A2A Agent Card](https://bridgenode.cc/.well-known/agent-card.json)
- [OpenAPI Description](https://bridgenode.cc/openapi.json)
- [x402 Protocol Documentation](https://docs.x402.org)
- [x402 Discovery Metadata](https://bridgenode.cc/.well-known/x402)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request examples, code snippets, and shell commands; runtime API responses are OpenAI-compatible JSON or SSE text streams.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid calls require explicit x402 payment signing with Solana USDC; free models and free trials are available.]

## Skill Version(s):

1.0.34 (source: ClawHub release evidence; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
