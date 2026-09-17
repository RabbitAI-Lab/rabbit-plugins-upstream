## Description:

Validates proposed x402 USDC payment configuration for a read-only MCP product on Cloudflare Workers before paid tools or deployment are added.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kadopi](https://clawhub.ai/user/kadopi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to check network, asset, price, recipient, and facilitator settings for an x402 USDC payment path before deploying a Cloudflare Workers MCP server or adding a paid read-only tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user may trust an unverified remote MCP endpoint or source repository.

Mitigation: Confirm the remote MCP endpoint and source repository are trusted before installing or routing agent work through the skill.

Risk: A Mainnet payment action may be attempted before the business owner has approved the paid path.

Mitigation: Use testnet validation first and require explicit business approval immediately before any paid Mainnet action.

Risk: Buyer private keys or payment signatures could be exposed through prompts, logs, or support messages.

Mitigation: Keep buyer private keys only in the payment client and never place private keys or payment signatures in prompts, source files, logs, or support messages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kadopi/skills/x402-mcp-starter)
- [MCP Service Card](https://x402-mcp-starter.kadopi.workers.dev/.well-known/agent-card.json)
- [Product page](https://aegis-sales-bot.kadopi.workers.dev/products/x402-mcp-starter)
- [MCP Registry search](https://registry.modelcontextprotocol.io/?q=io.github.kadopi%2Fx402-mcp-starter)
- [Listed source repository](https://github.com/kadopi/x402-mcp-starter)

## Skill Output:

**Output Type(s):** [Text, Configuration, Guidance]

**Output Format:** [Markdown or plain text guidance with configuration values and approval boundaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference an MCP endpoint for validation and paid sample behavior; does not require private keys in prompts.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
