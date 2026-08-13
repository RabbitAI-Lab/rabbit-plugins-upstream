## Description:

BridgeNode provides anonymous pay-per-request LLM inference for AI agents through an OpenAI-compatible endpoint and MCP access, using Solana USDC micropayments via x402 without API keys, registration, subscriptions, or stored data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[applefanaimail-blip](https://clawhub.ai/user/applefanaimail-blip)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent builders, and MCP-capable agents use this skill to call BridgeNode's paid LLM inference service when they need OpenAI-compatible chat completions without maintaining a provider API key. It is especially relevant for agents that can hold Solana USDC, perform x402 payment handshakes, and enforce their own spending limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may spend real Solana USDC for each LLM request.

Mitigation: Install only when paid BridgeNode inference is intended, configure client-side per-call and daily caps, and verify each 402 payment quote before signing where possible.

Risk: Prompts are sent to an external inference service despite the artifact's privacy-focused claims.

Mitigation: Review data handling requirements before use and avoid sending prompts that violate the user's or organization's policy for external services.

Risk: The documented exact pricing scheme charges for input tokens plus max_tokens before processing, so over-large max_tokens values can increase cost.

Mitigation: Set max_tokens deliberately, prefer streaming for long generations, and monitor quoted amounts before signing payment transactions.

## Reference(s):

- [BridgeNode service](https://bridgenode.cc)
- [BridgeNode model and pricing endpoint](https://bridgenode.cc/v1/models)
- [BridgeNode MCP endpoint](https://bridgenode.cc/mcp)
- [BridgeNode agent install map](https://bridgenode.cc/llms.txt)
- [BridgeNode source repository](https://github.com/applefanaimail-blip/bridgenode-skill)
- [BridgeNode ClawHub listing](https://clawhub.ai/applefanaimail-blip/skills/bridgenode)
- [BridgeNode x402-list entry](https://x402-list.com/services/bridgenode)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with endpoint tables, curl examples, and Python SDK guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance centers on paid LLM requests, x402 payment flow, model selection, max_tokens behavior, streaming, and MCP access.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
