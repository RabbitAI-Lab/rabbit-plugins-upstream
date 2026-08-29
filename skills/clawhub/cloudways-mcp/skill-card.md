## Description:

Operational guide for managing Cloudways servers and applications across one or several Cloudways accounts via the official hosted Cloudways MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[benkalsky](https://clawhub.ai/user/benkalsky)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to connect to and operate Cloudways MCP for server and application monitoring, maintenance, onboarding audits, automation planning, and controlled write operations across one or more Cloudways accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloudways write and destructive tools can affect live servers, applications, domains, SSL, backups, team access, billing, and subscriptions.

Mitigation: Use the skill's explicit confirmation workflow for all write tools and double confirmation for destructive actions, including a clear account, target, parameters, and expected impact.

Risk: Overprivileged or exposed Cloudways tokens can allow broad account changes.

Mitigation: Use the minimum Cloudways token role needed, keep tokens out of committed files and logs, avoid legacy API keys, and reserve FULL ACCESS for deliberate write workflows.

Risk: Multiple Cloudways accounts can lead to wrong-account operations or reused IDs across accounts.

Mitigation: Verify the account before every operation, keep per-account MCP connections separate, and never reuse server or application IDs across accounts.

Risk: Documented tool catalogs can lag behind the live Cloudways MCP server.

Mitigation: Treat the live connected MCP tools as the source of truth when a tool name or capability differs from the skill documentation.

## Reference(s):

- [Cloudways MCP skill page](https://clawhub.ai/benkalsky/skills/cloudways-mcp)
- [How to Use Cloudways MCP Server for AI-Based Server Management](https://support.cloudways.com/en/articles/14654372-how-to-use-cloudways-mcp-server-for-ai-based-server-management)
- [Cloudways MCP Server Tools](https://support.cloudways.com/en/articles/15798823-cloudways-mcp-server-tools)
- [Cloudways MCP v1.2 announcement](https://www.cloudways.com/blog/cloudways-mcp-v1-2-112-new-tools-role-based-access-tokens-and-full-cloudways-api-coverage/)
- [Cloudways API documentation](https://developers.cloudways.com/docs/)
- [Installation - Cloudways MCP Server](references/installation.md)
- [Tools Catalog - Cloudways MCP](references/tools-catalog.md)
- [Workflows - Monitoring](references/workflows-monitoring.md)
- [Workflows - Maintenance](references/workflows-maintenance.md)
- [Workflows - Onboarding and Audit](references/workflows-onboarding.md)
- [Workflows - Automation and Integration](references/workflows-automation.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with command snippets, confirmation prompts, tool names, and workflow checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a configured Cloudways MCP connection; write and destructive operations require explicit user confirmation.]

## Skill Version(s):

1.4.1 (source: evidence.release.version and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
