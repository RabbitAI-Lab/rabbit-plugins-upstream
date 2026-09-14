## Description:

BridgeNode gives agents OpenAI-compatible LLM inference and MCP access paid per request with Solana USDC via x402, with free models and no API keys or registration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bridgenode](https://clawhub.ai/user/bridgenode)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and AI agents use this skill to route chat-completion requests through BridgeNode when they need pay-per-request LLM inference, MCP access, or tool-calling support without managing provider API keys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid requests can automatically spend real Solana USDC.

Mitigation: Review the payment flow before installation, use a dedicated low-balance wallet, and set strict per-call and daily spending caps where supported.

Risk: Mutable package execution can install a later MCP wrapper than the reviewed artifact.

Mitigation: Pin the MCP package to a reviewed exact version instead of using @latest.

Risk: An agent may sign an unexpected payment amount, network, asset, or recipient.

Mitigation: Verify the exact 402 payment amount, USDC asset, Solana network, and recipient before signing each paid request.

## Reference(s):

- [BridgeNode website](https://bridgenode.cc)
- [Models and live pricing](https://bridgenode.cc/v1/models)
- [OpenAI-compatible chat completions endpoint](https://bridgenode.cc/v1/chat/completions)
- [BridgeNode MCP endpoint](https://bridgenode.cc/mcp)
- [BridgeNode agent install map](https://bridgenode.cc/llms.txt)
- [x402 documentation](https://docs.x402.org)
- [ClawHub skill page](https://clawhub.ai/bridgenode/skills/bridgenode)

## Skill Output:

**Output Type(s):** [text, markdown, code, tool calls, shell commands, configuration, guidance]

**Output Format:** [OpenAI-compatible chat completions, MCP tool results, Markdown guidance, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid requests use exact x402 quotes before signing; free models and trial calls can run without payment.]

## Skill Version(s):

1.0.33 (source: server release metadata; artifact frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
