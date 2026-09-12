## Description:

Use when exposing a WordPress site to AI agents via MCP, or when WordPress MCP setup fails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site operators use this skill to configure, troubleshoot, and verify MCP access for WordPress through mcp-adapter, AI Engine, or wp-mcp-ultimate. It helps agents produce setup guidance, client configuration, shell commands, and verification steps for WordPress MCP integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help configure agent access to administer a WordPress site using powerful credentials.

Mitigation: Install only when WordPress administration through an agent is intended, use a dedicated least-privilege WordPress account, and prefer manual review or dry-run steps before writing configuration.

Risk: Credentials may be entered on command lines, written into MCP client configuration, or exposed through troubleshooting output.

Mitigation: Use HTTPS, protect local config files, avoid printing secrets, and rotate any credential that appears in command history or logs.

Risk: Database features, dynamic REST features, plugin activation, user creation, option updates, sudo, or arbitrary PHP can expand the operational blast radius.

Mitigation: Enable only needed features, pin plugin and npm versions, and require explicit approval for high-privilege or write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/wordpress-mcp)
- [Publisher profile](https://clawhub.ai/user/afonsoft)
- [Publisher source repository](https://github.com/afonsoft/skills)
- [WordPress MCP Adapter](https://github.com/wordpress/mcp-adapter)
- [AI Engine plugin](https://wordpress.org/plugins/ai-engine/)
- [LobeHub WordPress MCP skill](https://lobehub.com/skills/openclaw-skills-wordpress-mcp)
- [mcp-adapter guide](references/mcp-adapter-guide.md)
- [MCP configuration guide](references/mcp-config.md)
- [Platform quirks](references/platform-quirks.md)
- [Troubleshooting guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands, JSON/TOML configuration snippets, and WordPress MCP verification steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include setup and verification scripts; credentials and high-privilege WordPress actions require review before execution.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
