## Description:

Helps agents build, edit, inspect, and troubleshoot WordPress Elementor sites through the elementor-mcp MCP server, including Pro/free feature branching, classic versus Elementor 4 atomic page handling, dynamic data binding, setup guidance, and recovery from common write errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[benkalsky](https://clawhub.ai/user/benkalsky)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site builders use this skill when they want an agent to set up, inspect, build, or edit Elementor pages while respecting WordPress credentials, Elementor Pro/free differences, and classic/atomic engine constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control a WordPress/Elementor site and may create, modify, or delete site content.

Mitigation: Use it only on sites intended for agent edits, require explicit user requests for write actions, and review site changes before publishing.

Risk: The setup flow stores a reusable WordPress application password in .mcp.json.

Mitigation: Use a least-privileged application password, keep .mcp.json out of shared or tracked directories, and revoke or rotate the password after the build.

Risk: Plain HTTP can expose WordPress credentials during MCP or REST requests.

Mitigation: Prefer HTTPS, avoid WP_ALLOW_HTTP on live sites, and allow plaintext only for explicitly named local or development hosts.

Risk: Downloading the latest plugin release can install mutable code.

Mitigation: Pin a known release and provide an independently checked SHA-256 when practical.

## Reference(s):

- [SiteAgent Elementor Studio on ClawHub](https://clawhub.ai/benkalsky/skills/siteagent-elementor-studio)
- [elementor-mcp GitHub repository](https://github.com/Digitizers/elementor-mcp)
- [wordpress-api-pro GitHub repository](https://github.com/Digitizers/wordpress-api-pro)
- [Engine and Premium Plugin](references/engine-and-premium.md)
- [Building on Elementor 4 Atomic V4](references/atomic-v4.md)
- [Elementor 4 Design System CRUD](references/design-system-crud.md)
- [Converting Classic V3 Designs to Atomic V4](references/v3-to-v4-conversion.md)
- [Brand Kit](references/brand-kit.md)
- [Forms](references/forms.md)
- [Header and Footer](references/header-footer.md)
- [Dynamic Data Stacks](references/dynamic-data.md)
- [Pro Widgets and Features](references/pro-widgets.md)
- [Error Recovery](references/error-recovery.md)
- [Section Recipe Library](references/recipes.md)
- [Studio Lifecycle](references/lifecycle.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose MCP tool calls, WordPress/Elementor configuration steps, and generated page or widget content; setup actions require explicit user confirmation.]

## Skill Version(s):

1.6.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
