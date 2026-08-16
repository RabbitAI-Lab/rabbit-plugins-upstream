## Description:

BridgeNode provides pay-per-request LLM inference for AI agents through OpenAI-compatible chat completions and MCP access, using Solana USDC micropayments via x402 without API keys or registration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bridgenode](https://clawhub.ai/user/bridgenode)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill when an agent needs paid LLM inference but does not have a provider API key. It guides agents through BridgeNode endpoints, model selection, live pricing checks, MCP access, and x402 payment flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause an agent to spend real USDC on Solana mainnet for each paid inference request.

Mitigation: Use a dedicated low-balance wallet, configure per-call and daily spend caps when available, check live prices, and verify the 402 payment amount before signing.

Risk: Automatic SDK or MCP flows may sign payment transactions during normal agent operation.

Mitigation: Avoid connecting a primary wallet to automatic flows and limit wallet funding to the intended operating budget.

Risk: Costs depend on request settings, including max_tokens, and some completed provider responses may not be refundable.

Mitigation: Set conservative max_tokens values, review model pricing before use, and increase token budgets deliberately for reasoning models.

## Reference(s):

- [BridgeNode homepage](https://bridgenode.cc)
- [Models and live pricing](https://bridgenode.cc/v1/models)
- [Agent install map](https://bridgenode.cc/llms.txt)
- [BridgeNode MCP endpoint](https://bridgenode.cc/mcp)
- [ClawHub skill page](https://clawhub.ai/bridgenode/skills/bridgenode)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance with endpoint references, shell commands, and Python or TypeScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes OpenAI-compatible API and MCP usage guidance; paid requests require Solana USDC and x402 payment signing.]

## Skill Version(s):

1.0.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
