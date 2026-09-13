## Description:

Helps agents build, edit, inspect, and troubleshoot WordPress Elementor sites through the elementor-mcp MCP server, including Pro/free-path selection, classic versus Elementor 4 atomic page handling, dynamic data bindings, setup guidance, and error recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[benkalsky](https://clawhub.ai/user/benkalsky)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site builders, and agency operators use this skill to guide WordPress and Elementor page creation, editing, inspection, setup, and troubleshooting through an Elementor MCP connection. It is intended for Elementor projects, including sites that may use Elementor Pro, Elementor 4 atomic pages, ACF, or JetEngine dynamic data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path persists a reusable WordPress Application Password in local MCP configuration.

Mitigation: Use a least-privileged WordPress account, keep the credentialed configuration out of version control, restrict file permissions, and revoke or rotate the Application Password after setup.

Risk: The setup path can install remote plugin code and may use the latest release by default.

Mitigation: Pin the elementor-mcp release and verify it with an independently obtained SHA-256 before installing on production or client sites.

Risk: Using plaintext HTTP for a live WordPress site can expose reusable credentials.

Mitigation: Use HTTPS for live sites and allow plaintext HTTP only for hosts that are explicitly named and known to be appropriate for local development.

Risk: Elementor automation can create or modify live site structure.

Mitigation: Review proposed changes before execution and verify page structure or rendered output after write operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/benkalsky/skills/siteagent-elementor-studio)
- [Building on Elementor 4 (atomic / V4)](references/atomic-v4.md)
- [Brand kit - token vocabulary & intake](references/brand-kit.md)
- [Elementor 4 design system CRUD](references/design-system-crud.md)
- [Dynamic data stacks](references/dynamic-data.md)
- [Engine & the Premium plugin](references/engine-and-premium.md)
- [When a write fails - errors, governance & self-correction](references/error-recovery.md)
- [Forms - Elementor MCP](references/forms.md)
- [Header / Footer](references/header-footer.md)
- [Studio lifecycle](references/lifecycle.md)
- [Pro-only widgets & features](references/pro-widgets.md)
- [Section recipe library](references/recipes.md)
- [Converting a classic design to the atomic engine](references/v3-to-v4-conversion.md)
- [Car wash studio build pack](references/verticals/car-wash.md)
- [Dental studio build pack](references/verticals/dental.md)
- [Local business studio build pack](references/verticals/local-business.md)
- [Portfolio studio build pack](references/verticals/portfolio.md)
- [Salon studio build pack](references/verticals/salon.md)
- [elementor-mcp repository referenced by artifact](https://github.com/Digitizers/elementor-mcp)
- [wordpress-api-pro repository referenced by artifact](https://github.com/Digitizers/wordpress-api-pro)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code blocks, shell commands, configuration snippets, and Elementor MCP tool-call parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide credentialed WordPress setup and Elementor MCP actions; setup and write operations are framed for explicit user confirmation.]

## Skill Version(s):

1.5.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
