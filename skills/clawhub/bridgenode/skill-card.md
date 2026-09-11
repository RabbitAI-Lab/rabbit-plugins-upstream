## Description:

BridgeNode provides AI agents with OpenAI-compatible and MCP LLM inference that can be used without API keys and paid per request with Solana USDC through x402.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bridgenode](https://clawhub.ai/user/bridgenode)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and AI agents use this skill to call LLM chat completions through an OpenAI-compatible endpoint or MCP server when they want no-key access, live model pricing, free-model options, or per-request Solana USDC payment through x402.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid requests can spend real USDC through automatic wallet signing.

Mitigation: Use free models first, keep a dedicated low-balance Solana wallet, set per-call and daily spending caps where supported, and verify every 402 amount, asset, network, and recipient before signing.

Risk: Mutable package installs such as latest npm or pip packages can change payment-handling behavior over time.

Mitigation: Pin exact npm and pip package versions and review updates before allowing automated payment flows.

Risk: Wallet keys may be exposed if copied into shared projects or committed files.

Mitigation: Keep wallet keys out of shared workspaces and store them only in local secret or environment mechanisms.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bridgenode/skills/bridgenode)
- [BridgeNode Website](https://bridgenode.cc)
- [Models and Live Pricing](https://bridgenode.cc/v1/models)
- [BridgeNode MCP Server](https://bridgenode.cc/mcp)
- [BridgeNode Agent Map](https://bridgenode.cc/llms.txt)
- [x402 Documentation](https://docs.x402.org)
- [Artifact README](artifact/README.md)
- [Artifact Examples](artifact/examples/README.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with endpoint details, curl commands, SDK examples, MCP configuration, and payment-flow instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include instructions for paid Solana USDC requests, free-model access, max_tokens cost controls, and client-side spending limits.]

## Skill Version(s):

1.0.31 (source: ClawHub release evidence; artifact/SKILL.md frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
