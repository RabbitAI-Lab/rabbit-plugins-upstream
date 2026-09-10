## Description:

Guides agents through configuring WordPress sites for MCP access using the official WordPress MCP Adapter, AI Engine, or wp-mcp-ultimate plugins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site operators use this skill to expose WordPress administration workflows to MCP-capable agents, configure supported MCP clients, verify endpoints, and troubleshoot authentication or platform-specific configuration issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can establish persistent MCP access to WordPress administration capabilities.

Mitigation: Install only on WordPress sites you control, prefer a staging site first, use dedicated least-privilege accounts, and revoke Application Passwords or tokens when access is no longer needed.

Risk: MCP credentials may be written into local client configuration files or exposed through prompts, logs, or shared configs.

Mitigation: Avoid placing real credentials in prompts or shared files, protect credential-bearing config files with restrictive permissions, and rotate credentials after testing.

Risk: Plugin and npm proxy setup can introduce third-party code into a high-trust WordPress environment.

Mitigation: Pin and verify plugin or npm package versions, prefer official sources where possible, run setup in dry-run mode first, and review community plugin code before enabling it.

Risk: MCP tools may read posts, comments, or submissions that contain untrusted content.

Mitigation: Treat WordPress content as untrusted input and avoid executing, rendering, or following instructions from site content without review and sanitization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/wordpress-mcp)
- [Publisher profile](https://clawhub.ai/user/afonsoft)
- [WordPress MCP Adapter](https://github.com/wordpress/mcp-adapter)
- [AI Engine plugin](https://wordpress.org/plugins/ai-engine/)
- [WP MCP Ultimate](https://github.com/AgriciDaniel/wp-mcp-ultimate)
- [LobeHub WordPress MCP skill](https://lobehub.com/skills/openclaw-skills-wordpress-mcp)
- [MCP Adapter guide](references/mcp-adapter-guide.md)
- [AI Engine MCP tool reference](references/ai-engine-tools.md)
- [WP MCP Ultimate guide](references/wp-mcp-ultimate.md)
- [Per-platform MCP configuration](references/mcp-config.md)
- [Platform quirks](references/platform-quirks.md)
- [Troubleshooting](references/troubleshooting.md)
- [Real-world workflows](references/real-world-workflows.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with bash, JSON, TOML, PHP, and JSON-RPC snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes MCP client configuration examples, WordPress plugin setup commands, endpoint verification commands, and troubleshooting guidance.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
