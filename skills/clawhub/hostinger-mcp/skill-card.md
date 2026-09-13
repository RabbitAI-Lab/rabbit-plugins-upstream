## Description:

Operational guide for managing Hostinger infrastructure, including VPS, websites, domains, DNS, Reach, and billing, through the official Hostinger MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[benkalsky](https://clawhub.ai/user/benkalsky)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Hostinger infrastructure through MCP tools while routing to the smallest needed tool category and requiring explicit confirmation for write, destructive, and billing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Hostinger MCP server receives full authority over the connected Hostinger account, including billing, DNS, VPS, and production operations.

Mitigation: Use the skill only with accounts or tokens that are appropriate for that authority, keep tokens out of command lines and config files, and remove stale MCP connections after use.

Risk: Destructive and money-spending tools can delete resources, wipe VPS data, alter DNS, or charge a payment method.

Mitigation: Require explicit target, account, impact, and cost confirmation before writes; double-confirm destructive actions and inspect current state before execution.

Risk: A registry-installed MCP package or dependency could inherit account authority if compromised or installed unpinned.

Mitigation: Prefer the pinned package version documented by the skill, load only the needed category binary, and review or verify the npm package and dependencies before production or billing use.

## Reference(s):

- [Installation - Hostinger MCP Server](references/installation.md)
- [Tools Catalog - Hostinger MCP](references/tools-catalog.md)
- [Workflows - VPS](references/workflows-vps.md)
- [Hostinger API MCP Server](https://github.com/hostinger/api-mcp-server)
- [Hostinger hPanel](https://hpanel.hostinger.com)
- [Hostinger API Reference](https://developers.hostinger.com/)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands, configuration examples, and MCP tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes confirmation patterns for write, destructive, and money-spending Hostinger operations.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
