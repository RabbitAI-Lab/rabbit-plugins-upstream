## Description:

BridgeNode provides OpenAI-compatible chat completions and MCP access for agents that pay per request with Solana USDC through the x402 protocol.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bridgenode](https://clawhub.ai/user/bridgenode)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to route LLM chat completion requests through BridgeNode when they want pay-per-request inference without API keys. It is suited for OpenAI-compatible agents, MCP clients, and x402-capable clients with a Solana USDC wallet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause automatic spending of real Solana mainnet USDC for paid inference requests.

Mitigation: Use a dedicated low-balance wallet, check the 402 amount before signing, and configure strict per-call and daily spending caps where supported.

Risk: Changing BRIDGENODE_URL can route wallet-signed payment flows to an untrusted endpoint.

Mitigation: Use the default BridgeNode endpoint unless the replacement endpoint is fully trusted and reviewed.

Risk: Example commands and MCP registration can run package-managed clients that persist beyond a single test.

Mitigation: Prefer pinned package versions or the committed lockfile, and review persistent MCP registrations before leaving them enabled.

## Reference(s):

- [BridgeNode website](https://bridgenode.cc)
- [Models and live pricing](https://bridgenode.cc/v1/models)
- [OpenAI-compatible chat completions endpoint](https://bridgenode.cc/v1/chat/completions)
- [BridgeNode MCP server](https://bridgenode.cc/mcp)
- [Agent install map](https://bridgenode.cc/llms.txt)
- [x402 documentation](https://docs.x402.org)
- [BridgeNode ClawHub skill](https://clawhub.ai/bridgenode/skills/bridgenode)
- [BridgeNode x402-list entry](https://x402-list.com/services/bridgenode)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API examples, command snippets, JSON request and response examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses may include OpenAI-compatible chat completion payloads, MCP tool responses, payment challenge headers, and settlement receipt metadata.]

## Skill Version(s):

1.0.30 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
