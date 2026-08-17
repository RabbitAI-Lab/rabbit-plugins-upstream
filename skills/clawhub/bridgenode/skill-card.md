## Description:

BridgeNode enables AI agents to use OpenAI-compatible chat completions and MCP inference endpoints without API keys, paying per request with Solana USDC through x402.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bridgenode](https://clawhub.ai/user/bridgenode)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and AI agents use BridgeNode when they need pay-per-request LLM inference without provider API keys or account registration and can authorize Solana USDC x402 payments per call.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause an agent to spend real Solana USDC for LLM calls.

Mitigation: Install only when paid inference is intended, use a separate low-balance wallet, set per-call and daily spending caps where supported, and check quoted payment amounts before autonomous use.

Risk: Wallet secrets used for x402 signing can expose funds if mishandled.

Mitigation: Keep SVM_PRIVATE_KEY out of source control and logs, and avoid sharing it with untrusted tools or prompts.

## Reference(s):

- [BridgeNode homepage](https://bridgenode.cc)
- [BridgeNode ClawHub skill page](https://clawhub.ai/bridgenode/skills/bridgenode)
- [BridgeNode models and pricing](https://bridgenode.cc/v1/models)
- [BridgeNode MCP endpoint](https://bridgenode.cc/mcp)
- [x402 documentation](https://docs.x402.org)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell, Python, TypeScript, JSON, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing instructions for paid inference calls, including endpoints, models, pricing checks, MCP usage, and x402 payment flow.]

## Skill Version(s):

1.0.20 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
