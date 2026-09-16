## Description:

Operational guide for managing Hostinger infrastructure across VPS, websites and hosting, domains, DNS, Reach email marketing, and billing via the official Hostinger MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[benkalsky](https://clawhub.ai/user/benkalsky)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure and operate Hostinger MCP access, select the smallest relevant tool category, and manage Hostinger account resources with explicit confirmation for account-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected Hostinger API token grants full account authority through the MCP server.

Mitigation: Keep tokens in environment variables or a keychain, never print token values, and install only when comfortable granting full Hostinger account access.

Risk: Write, destructive, billing, and purchase tools can change infrastructure, erase data, or spend money.

Mitigation: Require explicit confirmation for writes, double confirmation for destructive actions, and cost confirmation for money-spending actions before tool execution.

Risk: Loading every Hostinger MCP tool can increase context size and make tool selection less precise.

Mitigation: Load only the category-specific binary needed for the task, using the all-in-one server only for genuinely cross-category work.

Risk: Using npx fetches and executes the npm package without a separate pre-install verification step.

Mitigation: Prefer the documented pinned local install path with digest verification when supply-chain assurance matters.

## Reference(s):

- [Hostinger MCP Skill](https://clawhub.ai/benkalsky/skills/hostinger-mcp)
- [Hostinger MCP server repository](https://github.com/hostinger/api-mcp-server)
- [Hostinger hPanel](https://hpanel.hostinger.com)
- [Installation - Hostinger MCP Server](references/installation.md)
- [Tools Catalog - Hostinger MCP](references/tools-catalog.md)
- [Workflows - VPS](references/workflows-vps.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and MCP tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts the agent to prefer read-only operations, identify the active Hostinger account, and require confirmation before write, destructive, billing, or purchase actions.]

## Skill Version(s):

1.2.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
