## Description:

BridgeNode gives agents OpenAI-compatible and MCP-accessible LLM inference paid per request with Solana USDC via x402, without API keys, registration, subscriptions, or server-side data storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[applefanaimail-blip](https://clawhub.ai/user/applefanaimail-blip)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use bridgenode when an agent needs LLM chat completions through an OpenAI-compatible API or MCP tool and can authorize x402 Solana USDC payments per request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each request can spend real USDC on Solana mainnet.

Mitigation: Configure spending caps, avoid unattended wallet signing unless the flow is trusted, and verify the amount, recipient, mint, memo, and network before signing each x402 payment requirement.

Risk: The skill uses prepaid exact pricing based on input tokens plus max_tokens, so users may pay for unused output capacity.

Mitigation: Set max_tokens deliberately, fetch current model prices from the live model list, and check the payment amount returned in the 402 response before signing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/applefanaimail-blip/skills/bridgenode)
- [BridgeNode website](https://bridgenode.cc)
- [Live model list and prices](https://bridgenode.cc/v1/models)
- [MCP server endpoint](https://bridgenode.cc/mcp)
- [Agent install map](https://bridgenode.cc/llms.txt)
- [Repository listed in skill metadata](https://github.com/applefanaimail-blip/bridgenode-skill)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with inline endpoint references, curl examples, Python setup notes, and configuration names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance centers on OpenAI-compatible chat completions, MCP usage, x402 payment handling, model selection, request options, and error handling.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
