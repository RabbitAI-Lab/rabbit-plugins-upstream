## Description:

SellerSprite MCP helps agents operate SellerSprite MCP through an OOMOL-connected account for Amazon product, ASIN, keyword, traffic, market, review, trend, and trademark research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect SellerSprite MCP action schemas and run SellerSprite connector actions through the oo CLI for Amazon marketplace research. It supports read-heavy product, keyword, traffic, market, trend, review, and trademark workflows, with confirmation required before state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act through a user's OOMOL-connected SellerSprite MCP account.

Mitigation: Install and use it only when the agent is intended to access that connected account.

Risk: State-changing SellerSprite MCP actions may alter account data or saved research state.

Mitigation: Require explicit user confirmation of the exact action and payload before running any action tagged [write] or [destructive].

Risk: Incorrect payloads can send unintended requests to SellerSprite MCP.

Mitigation: Inspect the live action schema with oo connector schema before constructing each payload.

## Reference(s):

- [SellerSprite MCP homepage](https://open.sellersprite.com/mcp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sellersprite-mcp)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when the skill runs oo connector commands with --json.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
