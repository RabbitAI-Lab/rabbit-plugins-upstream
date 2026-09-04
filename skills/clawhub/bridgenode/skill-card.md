## Description:

BridgeNode provides pay-per-request LLM inference for AI agents through an OpenAI-compatible API and MCP server, using x402 payments with Solana USDC and no provider API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bridgenode](https://clawhub.ai/user/bridgenode)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent builders use this skill when an agent needs LLM chat completions or MCP-based inference without a provider API key and can pay per request from its own Solana USDC wallet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause an agent to spend real Solana mainnet USDC for inference requests.

Mitigation: Use a dedicated low-balance wallet, set per-call and daily spending caps where supported, and review the exact 402 payment amount before signing.

Risk: Using unpinned MCP or npm package commands such as @latest can change executed client code over time.

Mitigation: Pin MCP and npm package versions before operational use and review package updates before upgrading.

Risk: Reasoning models can consume the requested token budget and return an empty answer without a refund after service is provided.

Mitigation: Use an adequate max_tokens value, especially at least 200 for reasoning models, and prefer streaming for long generations.

## Reference(s):

- [BridgeNode service homepage](https://bridgenode.cc)
- [Live models and pricing](https://bridgenode.cc/v1/models)
- [OpenAI-compatible chat completions endpoint](https://bridgenode.cc/v1/chat/completions)
- [BridgeNode MCP endpoint](https://bridgenode.cc/mcp)
- [Agent install map](https://bridgenode.cc/llms.txt)
- [x402 documentation](https://docs.x402.org)
- [Python SDK package](https://pypi.org/project/bridgenode-llm)
- [TypeScript SDK package](https://www.npmjs.com/package/@bridgenode/llm)
- [MCP wrapper package](https://www.npmjs.com/package/@bridgenode/mcp)
- [ClawHub skill page](https://clawhub.ai/bridgenode/skills/bridgenode)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, JSON examples, and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents through paid API or MCP requests; actual model output and costs depend on live BridgeNode endpoints and signed x402 payment amounts.]

## Skill Version(s):

1.0.29 (source: ClawHub release evidence; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
