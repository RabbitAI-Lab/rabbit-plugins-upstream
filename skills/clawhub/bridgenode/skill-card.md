## Description:

BridgeNode provides anonymous pay-per-request LLM inference for agents through an OpenAI-compatible chat completions API and MCP server, with x402 Solana USDC payments and free model access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bridgenode](https://clawhub.ai/user/bridgenode)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent builders use this skill to add LLM chat completions when they do not have a provider API key or want per-request pricing. Agents can use free models without a wallet, or paid models through x402 payments from the agent's own Solana USDC wallet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet-connected paid requests can spend real Solana USDC.

Mitigation: Prefer free models first, use a dedicated low-balance wallet, confirm the quoted amount before signing, and set per-call and daily spending caps where the client supports them.

Risk: The MCP wrapper example can run the latest npm package while handling wallet-connected requests.

Mitigation: Use a pinned audited MCP wrapper version or configure direct streamable-http access to https://bridgenode.cc/mcp.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bridgenode/skills/bridgenode)
- [BridgeNode website](https://bridgenode.cc)
- [Live models and pricing](https://bridgenode.cc/v1/models)
- [BridgeNode MCP endpoint](https://bridgenode.cc/mcp)
- [BridgeNode agent card](https://bridgenode.cc/.well-known/agent-card.json)
- [x402 documentation](https://docs.x402.org)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline bash, JSON, Python, and TypeScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include wallet and payment setup guidance, model and price lookup instructions, MCP configuration details, and settlement receipt handling.]

## Skill Version(s):

1.0.35 (source: server release metadata; artifact frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
