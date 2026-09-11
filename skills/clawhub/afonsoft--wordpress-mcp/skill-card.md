## Description:

Helps agents configure and troubleshoot WordPress MCP integrations through mcp-adapter, AI Engine, or wp-mcp-ultimate, including plugin installation, client configuration, endpoint verification, and credential handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site operators use this skill to connect agent clients to WordPress sites, select an MCP plugin path, install and configure it, verify MCP endpoints, and troubleshoot client or hosting issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can grant an agent durable WordPress management authority.

Mitigation: Prefer a staging site first, verify the site is controlled by the user, use dedicated least-privilege WordPress users, and install only when durable agent access is acceptable.

Risk: Plugin and proxy setup can involve remote downloads and executable setup paths.

Mitigation: Pin plugin and npm versions, verify downloads, use HTTPS endpoints only, and review commands before running them on a WordPress host.

Risk: Application Passwords, bearer tokens, and OAuth credentials may be persisted in agent configuration files.

Mitigation: Protect configuration files, avoid logging credentials, rotate exposed secrets, and remove or rotate credentials when the integration is no longer needed.

Risk: Some MCP features can modify plugins, themes, database state, site content, and authentication behavior.

Mitigation: Avoid database, plugin, and theme MCP features unless explicitly needed, review proposed changes before execution, and remove authentication-enabling mu-plugin changes if MCP access is discontinued.

## Reference(s):

- [mcp-adapter guide](references/mcp-adapter-guide.md)
- [AI Engine tools](references/ai-engine-tools.md)
- [wp-mcp-ultimate guide](references/wp-mcp-ultimate.md)
- [MCP client configuration](references/mcp-config.md)
- [Platform quirks](references/platform-quirks.md)
- [Real-world workflows](references/real-world-workflows.md)
- [Troubleshooting](references/troubleshooting.md)
- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/wordpress-mcp)
- [afonsoft skills collection](https://github.com/afonsoft/skills)
- [WordPress MCP Adapter](https://github.com/wordpress/mcp-adapter)
- [AI Engine plugin](https://wordpress.org/plugins/ai-engine/)
- [WP MCP Ultimate](https://github.com/AgriciDaniel/wp-mcp-ultimate)
- [LobeHub WordPress MCP skill](https://lobehub.com/skills/openclaw-skills-wordpress-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON, TOML, shell commands, and MCP request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce WordPress plugin installation steps, MCP client configuration snippets, endpoint verification commands, and troubleshooting guidance.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
