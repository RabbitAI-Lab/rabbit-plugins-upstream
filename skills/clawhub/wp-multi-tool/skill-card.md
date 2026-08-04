## Description: <br>
WordPress site health audit, performance optimization, database cleanup, autoload tuning, slow query detection, wp-config management, image size control, frontend speed fixes, and server diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[marcindudekdev](https://clawhub.ai/user/marcindudekdev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, site operators, and WordPress administrators use this skill to audit site health, inspect performance bottlenecks, and prepare WP-CLI diagnostics or carefully confirmed optimization actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: WP-CLI quick-fix commands can delete or modify WordPress database rows, plugin options, or wp-config.php settings. <br>
Mitigation: Require deliberate user confirmation before every write action and prefer a database export before cleanup, metadata deletion, configuration changes, or table optimization. <br>
Risk: The skill is useful only where the operator intends agent-assisted WordPress administration through WP-CLI. <br>
Mitigation: Install and use it only for WordPress environments where shell access, WP-CLI permissions, and administrative intent are already established. <br>


## Reference(s): <br>
- [WP Multitool homepage](https://wpmultitool.com) <br>
- [ClawHub skill page](https://clawhub.ai/marcindudekdev/skills/wp-multi-tool) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash and SQL code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include WP-CLI diagnostics, JSON command variants, decision guidance, and confirmation-gated write commands.] <br>

## Skill Version(s): <br>
1.9.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
