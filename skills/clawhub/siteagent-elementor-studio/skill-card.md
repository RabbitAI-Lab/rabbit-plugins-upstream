## Description:

Helps with WordPress and Elementor work via the elementor-mcp MCP server, including page building, editing, site inspection, setup, Pro/free feature branching, Elementor 4 atomic/V4 handling, dynamic-data binding, and recovery from schema or governance errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[benkalsky](https://clawhub.ai/user/benkalsky)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site builders use this skill to connect an authorized WordPress site to Elementor MCP, inspect the site's Elementor state, and build or edit Elementor pages with engine-aware guidance. It is intended for Elementor-based WordPress work, not Bricks, Divi, Beaver Builder, or non-Elementor builds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can install WordPress plugins and modify an Elementor site.

Mitigation: Use only on WordPress sites the operator is authorized to modify, prefer a development or staging site, and require explicit confirmation before setup or write actions.

Risk: The generated .mcp.json can contain a reusable WordPress application password.

Mitigation: Use a least-privileged WordPress application password, keep .mcp.json out of shared folders and version control, and revoke the password after setup or handoff.

Risk: Using latest or custom MCP plugin tags can weaken release pinning assumptions.

Mitigation: Avoid EMCP_PIN_VERSION=latest or custom tags unless an independently obtained SHA-256 digest is supplied.

Risk: Live contact forms may collect personal data.

Mitigation: Review each form's privacy notice, recipient, and data-handling requirements before publishing.

## Reference(s):

- [SiteAgent Elementor Studio ClawHub Page](https://clawhub.ai/benkalsky/skills/siteagent-elementor-studio)
- [Digitizers elementor-mcp](https://github.com/Digitizers/elementor-mcp)
- [Digitizers wordpress-api-pro](https://github.com/Digitizers/wordpress-api-pro)
- [Building on Elementor 4 (atomic / V4)](references/atomic-v4.md)
- [Brand kit - token vocabulary and intake](references/brand-kit.md)
- [Elementor 4 design system CRUD](references/design-system-crud.md)
- [Dynamic data stacks (ACF and Crocoblock/JetEngine)](references/dynamic-data.md)
- [Engine and the Premium plugin](references/engine-and-premium.md)
- [When a write fails - errors, governance, and self-correction](references/error-recovery.md)
- [Forms - Elementor MCP](references/forms.md)
- [Header / Footer](references/header-footer.md)
- [Studio lifecycle](references/lifecycle.md)
- [Pro-only widgets and features](references/pro-widgets.md)
- [Section recipe library](references/recipes.md)
- [Converting a classic design to the atomic engine](references/v3-to-v4-conversion.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and MCP tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May result in WordPress and Elementor site changes only after explicit user request or confirmation.]

## Skill Version(s):

1.7.1 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
