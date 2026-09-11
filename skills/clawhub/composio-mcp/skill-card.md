## Description:

Helps agents configure, authenticate, verify, and use Composio CLI and MCP access to connect with external app toolkits such as Gmail, GitHub, Slack, Notion, Linear, and Jira.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to connect AI agents to Composio-managed external apps, recover from Composio CLI or MCP authentication failures, choose between project API keys and consumer keys, and configure supported MCP clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup helper can persistently add credentialed Composio access to multiple agent applications.

Mitigation: Prefer dry-run or manual setup, target one client explicitly, and review MCP configuration changes before restarting agent clients.

Risk: Composio project API keys and consumer keys may be exposed if passed directly on command lines or written into logs.

Mitigation: Use environment variables or a secret store, avoid putting real ak_* or ck_* keys on command lines, and rotate any key that appears in logs.

Risk: Connected Composio tools can access external apps through the agent.

Mitigation: Install only when this access is intended, inspect schemas and use dry-run behavior before mutating data or sending messages.

## Reference(s):

- [Composio Documentation](https://docs.composio.dev)
- [Composio Connect Documentation](https://docs.composio.dev/docs/composio-connect)
- [Consumer Project Boundaries and Auth Selection](https://docs.composio.dev/kb/guide/consumer-project-boundaries-and-auth-selection)
- [Composio GitHub Repository](https://github.com/ComposioHQ/composio)
- [Composio CLI Reference](references/cli-reference.md)
- [Composio MCP Config Reference](references/mcp-config.md)
- [MCP Platform Config Quirks](references/platform-quirks.md)
- [Composio Tool Inventory](references/tools-inventory.md)
- [Composio Troubleshooting](references/troubleshooting.md)
- [ClawHub Skill Page](https://clawhub.ai/afonsoft/skills/composio-mcp)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose CLI commands, MCP configuration changes, verification steps, and credential-handling guidance.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
