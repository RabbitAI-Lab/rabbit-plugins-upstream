## Description:

Operational guide for managing Cloudways servers and applications across one or several Cloudways accounts through the official Cloudways MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[benkalsky](https://clawhub.ai/user/benkalsky)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agency teams use this skill to monitor, audit, configure, and maintain Cloudways-hosted servers and applications through Cloudways MCP. It is suited to interactive operational work where account selection, scoped credentials, and explicit confirmation for write actions are required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloudways write and destructive operations can interrupt service, delete resources, overwrite application state, or change account billing.

Mitigation: Start with READ tokens, escalate only to LIMITED or FULL ACCESS for specific workflows, and require explicit target confirmation before writes with double confirmation for destructive actions.

Risk: Inventory and detail responses may include credentials or other secrets that persist in transcripts, logs, or automation records.

Mitigation: Avoid pasting raw Cloudways responses, request only the fields needed, filter sensitive inventories outside chat when zero-secret handling is required, and rotate any exposed credentials.

Risk: Multiple Cloudways accounts can expose similarly named resources or overlapping numeric IDs, creating wrong-account execution risk.

Mitigation: Verify the account or MCP connection prefix before every operation and never reuse server or application IDs across accounts.

Risk: Automation can run high-impact actions without enough human review.

Mitigation: Use direct Cloudways API automation with narrowly scoped tokens for routine reporting, and keep write or destructive workflows behind human approval unless explicitly designed and reviewed.

## Reference(s):

- [Cloudways MCP skill page](https://clawhub.ai/benkalsky/skills/cloudways-mcp)
- [Installation - Cloudways MCP Server](references/installation.md)
- [Tools Catalog - Cloudways MCP](references/tools-catalog.md)
- [Workflows - Monitoring](references/workflows-monitoring.md)
- [Workflows - Maintenance](references/workflows-maintenance.md)
- [Workflows - Onboarding & Audit](references/workflows-onboarding.md)
- [Workflows - Automation & Integration](references/workflows-automation.md)
- [How to Use Cloudways MCP Server for AI-Based Server Management](https://support.cloudways.com/en/articles/14654372-how-to-use-cloudways-mcp-server-for-ai-based-server-management)
- [Cloudways MCP Server Tools](https://support.cloudways.com/en/articles/15798823-cloudways-mcp-server-tools)
- [Cloudways MCP v1.2 announcement](https://www.cloudways.com/blog/cloudways-mcp-v1-2-112-new-tools-role-based-access-tokens-and-full-cloudways-api-coverage/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline commands, tables, and confirmation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce operational checklists, MCP connection configuration, Cloudways API examples, and risk-aware confirmation text.]

## Skill Version(s):

1.5.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
