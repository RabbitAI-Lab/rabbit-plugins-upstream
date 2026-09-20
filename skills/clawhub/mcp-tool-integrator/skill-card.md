## Description:

AI-powered assistant to scaffold, configure, debug, and integrate MCP servers connecting AI agents with tools such as GitHub, Slack, Notion, Airtable, Postgres, and filesystems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent builders, and DevOps engineers use this skill to plan MCP architecture, scaffold MCP servers, configure tool connections, and debug integration failures. It is suited for agents that need guidance, code snippets, shell commands, and configuration patterns for multi-tool MCP deployments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Referenced MCP packages, server registries, and protocol behavior may change after release.

Mitigation: Verify current MCP package sources and official MCP documentation before installing or configuring integrations.

Risk: Credentialed or write-capable tool integrations can expose data or perform unintended actions.

Mitigation: Use least-privilege credentials, read-only defaults, explicit confirmation for write actions, and audit logging.

Risk: Marketplace metadata may be rejected if malformed frontmatter is required for installation.

Mitigation: Fix the malformed frontmatter before publishing or installing in environments that require valid skill metadata.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gechengling/skills/mcp-tool-integrator)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code blocks, configuration snippets, diagnostic tables, and setup steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP architecture recommendations, server scaffolds, debugging reports, and security checklists.]

## Skill Version(s):

4.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
