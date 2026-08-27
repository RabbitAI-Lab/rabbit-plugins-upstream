## Description:

This skill helps agents operate McDonald's China MCP through OOMOL's oo CLI by discovering live tools and running read or account-changing MCP actions with user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to let an agent interact with a connected McDonald's China account, discover live ordering, coupon, campaign, and points-mall tools, and run MCP actions through OOMOL.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill can operate a connected McDonald's China account and may create orders, change addresses, claim coupons, or redeem points.

Mitigation: Require explicit user confirmation for the exact payload and expected effect before any order, address, coupon, or points action.

Risk: The available MCP tools and schemas are discovered live, so payload assumptions can become stale.

Mitigation: Run the schema inspection command for the selected action before constructing or executing a payload.

Risk: The release security summary says the skill under-discloses account-changing capabilities.

Mitigation: Treat the connector as read/write account access, not as read-only search, and review actions before installation and execution.

## Reference(s):

- [McDonald's China MCP homepage](https://open.mcd.cn/mcp/doc)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mcdonalds-cn-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live MCP action schemas before constructing payloads; account-changing actions require explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
