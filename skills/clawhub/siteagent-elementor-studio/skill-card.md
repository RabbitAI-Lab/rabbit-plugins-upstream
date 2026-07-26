## Description: <br>
Helps agents build, edit, inspect, and troubleshoot WordPress Elementor sites through the elementor-mcp MCP server, including first-session setup and engine-aware guidance for Elementor Pro, Free, classic, and atomic/V4 sites. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[benkalsky](https://clawhub.ai/user/benkalsky) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and site builders use this skill to connect an authorized WordPress site to Elementor MCP, then build, edit, inspect, or troubleshoot Elementor pages using native widgets, design tokens, forms, dynamic data, and recovery guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow installs WordPress plugins and stores a reusable WordPress Application Password in local MCP configuration. <br>
Mitigation: Install only for authorized sites, use a dedicated low-privilege Application Password, keep .mcp.json private, and revoke or rotate the password after setup or handoff. <br>
Risk: A live contact form can send or collect visitor data before recipients and privacy terms are confirmed. <br>
Mitigation: Confirm form recipients, notification settings, and privacy terms before enabling live contact forms. <br>
Risk: Using the latest unpinned elementor-mcp release can change setup behavior between runs. <br>
Mitigation: Pin EMCP_PIN_VERSION when reproducibility matters and review the plugin release before installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/benkalsky/skills/siteagent-elementor-studio) <br>
- [Elementor MCP plugin repository](https://github.com/Digitizers/elementor-mcp) <br>
- [SiteAgent worker repository](https://github.com/Digitizers/SiteAgent) <br>
- [wordpress-api-pro companion toolkit](https://github.com/Digitizers/wordpress-api-pro) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON configuration, and MCP tool-call parameter examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Setup can write a local .mcp.json for the target WordPress site after explicit user confirmation.] <br>

## Skill Version(s): <br>
1.3.2 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
