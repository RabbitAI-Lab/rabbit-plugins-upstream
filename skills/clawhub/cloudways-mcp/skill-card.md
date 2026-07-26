## Description: <br>
Operational guide for managing Cloudways servers and applications across one or several Cloudways accounts via the official Cloudways MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[benkalsky](https://clawhub.ai/user/benkalsky) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agency teams use this skill to connect agents to the official Cloudways MCP server, inspect Cloudways infrastructure, run monitoring and audit workflows, and plan maintenance actions with explicit confirmation for writes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent may receive credentials or tokens that grant Cloudways account access. <br>
Mitigation: Start with READ tokens for audits and monitoring, use LIMITED tokens for narrow workflows, reserve FULL ACCESS only for required account-wide changes, and never print tokens in responses. <br>
Risk: Write or destructive Cloudways operations can stop services, overwrite applications, change access, or delete resources. <br>
Mitigation: Require explicit confirmation of account, target server or application, tool, parameters, and expected impact before writes; use double confirmation for destructive actions. <br>
Risk: Multiple Cloudways accounts can expose similarly named resources with non-interchangeable IDs. <br>
Mitigation: Verify the MCP connection/account before every operation and never reuse server or application IDs across accounts. <br>


## Reference(s): <br>
- [Installation - Cloudways MCP Server](references/installation.md) <br>
- [Tools Catalog - Cloudways MCP](references/tools-catalog.md) <br>
- [Workflows - Monitoring](references/workflows-monitoring.md) <br>
- [Workflows - Maintenance](references/workflows-maintenance.md) <br>
- [Workflows - Onboarding & Audit](references/workflows-onboarding.md) <br>
- [Workflows - Automation](references/workflows-automation.md) <br>
- [How to Use Cloudways MCP Server for AI-Based Server Management](https://support.cloudways.com/en/articles/14654372-how-to-use-cloudways-mcp-server-for-ai-based-server-management) <br>
- [Cloudways MCP Server Tools](https://support.cloudways.com/en/articles/15798823-cloudways-mcp-server-tools) <br>
- [Cloudways MCP v1.2 Announcement](https://www.cloudways.com/blog/cloudways-mcp-v1-2-112-new-tools-role-based-access-tokens-and-full-cloudways-api-coverage/) <br>
- [Cloudways API Documentation](https://developers.cloudways.com/docs/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with command snippets, tables, and confirmation prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses read, write, and destructive risk labels for Cloudways MCP operations and asks for explicit confirmation before write actions.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
