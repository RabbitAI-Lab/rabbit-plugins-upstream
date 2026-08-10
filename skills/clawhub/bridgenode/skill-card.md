## Description:

BridgeNode lets agents access pay-per-request LLM inference through OpenAI-compatible and MCP endpoints funded with Solana USDC x402 payments, without API keys, registration, or subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[applefanaimail-blip](https://clawhub.ai/user/applefanaimail-blip)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use BridgeNode when an agent needs chat-completion inference without a provider API key and can authorize per-request Solana USDC payments via x402. MCP-based agents can use the hosted MCP endpoint for paid inference tool calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each signed request can spend real USDC on Solana mainnet.

Mitigation: Confirm the amount, recipient, token mint, and network before signing any x402 payment request.

Risk: The exact pricing scheme charges for input tokens plus max_tokens before processing, even if fewer output tokens are generated.

Mitigation: Set conservative max_tokens values and configure per-call and daily spending caps such as BRIDGENODE_MAX_PER_CALL and BRIDGENODE_DAILY_CAP.

Risk: Prompts and responses are sent to an external paid inference service.

Mitigation: Avoid sending sensitive prompts unless the service's privacy claims and data handling are acceptable for the use case.

## Reference(s):

- [BridgeNode service](https://bridgenode.cc)
- [OpenAI-compatible API base](https://bridgenode.cc/v1)
- [Model list and live prices](https://bridgenode.cc/v1/models)
- [Chat completions endpoint](https://bridgenode.cc/v1/chat/completions)
- [BridgeNode MCP endpoint](https://bridgenode.cc/mcp)
- [Agent install map](https://bridgenode.cc/llms.txt)
- [Source repository](https://github.com/applefanaimail-blip/bridgenode-skill)
- [ClawHub skill page](https://clawhub.ai/applefanaimail-blip/skills/bridgenode)
- [ClawHub publisher profile](https://clawhub.ai/user/applefanaimail-blip)

## Skill Output:

**Output Type(s):** [Text, API calls, Shell commands, Configuration guidance]

**Output Format:** [OpenAI-compatible JSON responses, MCP tool responses, and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid per request with Solana USDC via x402; supports streaming responses and model-specific max token limits.]

## Skill Version(s):

1.0.6 (source: server release evidence; artifact metadata reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
