## Description:

BridgeNode provides OpenAI-compatible LLM chat completions and MCP access paid per request with Solana USDC via x402, without API keys, registration, or subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[applefanaimail-blip](https://clawhub.ai/user/applefanaimail-blip)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and x402-capable agents use BridgeNode when they need paid, per-request LLM inference or MCP chat completions without managing a provider API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and generated content are sent to a third-party AI inference service.

Mitigation: Use non-sensitive prompts unless third-party processing is acceptable, and apply organization data-handling controls before use.

Risk: Each request can spend Solana USDC through x402 before inference.

Mitigation: Check the 402 quote before signing where the client allows it, configure wallet or spend controls outside the skill, and choose max_tokens deliberately.

Risk: Model pricing and availability can change.

Mitigation: Fetch live model and price data from https://bridgenode.cc/v1/models before issuing paid requests.

## Reference(s):

- [BridgeNode service website](https://bridgenode.cc)
- [BridgeNode model list and pricing](https://bridgenode.cc/v1/models)
- [BridgeNode MCP server](https://bridgenode.cc/mcp)
- [BridgeNode agent install map](https://bridgenode.cc/llms.txt)
- [BridgeNode source repository](https://github.com/applefanaimail-blip/bridgenode-skill)
- [ClawHub skill page](https://clawhub.ai/applefanaimail-blip/skills/bridgenode)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with API examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include OpenAI-compatible request bodies, x402 payment flow guidance, and MCP configuration details.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
