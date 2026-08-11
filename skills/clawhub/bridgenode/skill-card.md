## Description:

BridgeNode provides anonymous pay-per-request LLM inference for AI agents through an OpenAI-compatible endpoint and MCP access, using Solana USDC micropayments via x402.

This skill is ready for commercial/non-commercial use.

## Publisher:

[applefanaimail-blip](https://clawhub.ai/user/applefanaimail-blip)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use BridgeNode to access OpenAI-compatible or MCP LLM inference without a provider API key, paying per request with Solana USDC through x402.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill guides agents to spend Solana USDC for each LLM request.

Mitigation: Install only when paid inference is intended, check live pricing before signing, and set local spending limits where supported.

Risk: Unused max_tokens and some empty reasoning-model responses may still be charged and are not refunded.

Mitigation: Choose max_tokens deliberately, use at least the documented minimum for reasoning models, and prefer streaming for long generations.

Risk: Requests require a funded Solana wallet with an existing USDC associated token account.

Mitigation: Confirm the wallet, USDC mint, and associated token account before enabling an agent to make paid calls.

## Reference(s):

- [BridgeNode website](https://bridgenode.cc)
- [BridgeNode models and live pricing](https://bridgenode.cc/v1/models)
- [BridgeNode MCP endpoint](https://bridgenode.cc/mcp)
- [BridgeNode agent install map](https://bridgenode.cc/llms.txt)
- [BridgeNode repository](https://github.com/applefanaimail-blip/bridgenode-skill)
- [BridgeNode x402-list entry](https://x402-list.com/services/bridgenode)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with endpoint tables and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Describes paid OpenAI-compatible and MCP usage; the artifact contains no executable code.]

## Skill Version(s):

1.0.7 (source: server release evidence; artifact frontmatter metadata.version is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
