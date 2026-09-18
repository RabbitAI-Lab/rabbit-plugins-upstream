## Description:

Operates McDonald's China MCP through OOMOL's mcdonalds_cn_mcp connector, including live tool discovery and JSON tool invocation for ordering, coupon, campaign, and points-mall workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to discover available McDonald's China MCP tools and invoke them through an OOMOL-connected account. It is suited for ordering, coupon, campaign, and points-mall workflows where live schemas are checked before sending JSON payloads.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The connected account may perform account-changing actions such as spending points, claiming coupons, creating addresses, or creating orders.

Mitigation: Require explicit user confirmation of the exact payload and intended effect before any account-changing action.

Risk: First-time setup includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Avoid the pipe-to-shell installer path unless the oo CLI installer source and integrity have been independently verified.

Risk: Tool names, input fields, and behavior can change because actions are discovered through the live MCP connector.

Mitigation: Inspect the live action schema before constructing each payload and keep requests aligned with the returned contract.

## Reference(s):

- [McDonald's China MCP homepage](https://open.mcd.cn/mcp/doc)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mcdonalds-cn-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
