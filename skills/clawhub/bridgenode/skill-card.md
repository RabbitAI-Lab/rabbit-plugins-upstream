## Description:

BridgeNode provides pay-per-request AI inference for agents through an OpenAI-compatible API and MCP server, using Solana USDC payments over x402 without API keys or registration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bridgenode](https://clawhub.ai/user/bridgenode)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and agent operators use this skill when an agent needs LLM chat completions through an OpenAI-compatible endpoint or MCP tool and should pay per request with Solana USDC instead of using provider API keys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill can spend real Solana USDC for each paid inference request.

Mitigation: Use a dedicated wallet with a small USDC balance, check live prices and the quoted 402 amount before signing, and configure client-side spending caps where supported.

Risk: Example flows require a wallet key for signing x402 payments.

Mitigation: Keep wallet keys out of committed files, avoid production keys in example .env files, and use only the minimum wallet balance needed for the task.

Risk: A low max_tokens value on reasoning models can produce an empty answer that is still charged.

Mitigation: Set an adequate max_tokens budget for reasoning models and review model-specific pricing before sending paid requests.

## Reference(s):

- [BridgeNode website](https://bridgenode.cc)
- [Live models and pricing](https://bridgenode.cc/v1/models)
- [OpenAI-compatible API base](https://bridgenode.cc/v1)
- [BridgeNode MCP server](https://bridgenode.cc/mcp)
- [Agent install map](https://bridgenode.cc/llms.txt)
- [ClawHub skill page](https://clawhub.ai/bridgenode/skills/bridgenode)
- [x402 documentation](https://docs.x402.org)
- [Python SDK](https://pypi.org/project/bridgenode-llm)
- [TypeScript SDK](https://www.npmjs.com/package/@bridgenode/llm)
- [MCP wrapper](https://www.npmjs.com/package/@bridgenode/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with API endpoints, MCP setup, shell commands, and SDK examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces instructions for paid OpenAI-compatible and MCP inference calls; outputs may cause an agent to sign Solana USDC payments when followed.]

## Skill Version(s):

1.0.26 (source: ClawHub release evidence; SKILL.md frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
